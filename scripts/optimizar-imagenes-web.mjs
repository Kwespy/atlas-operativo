import fs from "node:fs"
import fsp from "node:fs/promises"
import path from "node:path"
import os from "node:os"
import crypto from "node:crypto"
import { execFile } from "node:child_process"
import { promisify } from "node:util"
import sharp from "sharp"

const execFileAsync = promisify(execFile)

const root = path.resolve(process.argv[2] ?? "")
const cacheDirectory = path.resolve(
  process.argv[3] ?? ".image-cache",
)

const MAX_SIZE = 2400
const QUALITY = 85
const EFFORT = 4

const supportedExtensions = new Set([
  ".jpg",
  ".jpeg",
  ".png",
  ".tif",
  ".tiff",
  ".heic",
  ".heif",
])

const heicExtensions = new Set([
  ".heic",
  ".heif",
])

if (!root || !fs.existsSync(root)) {
  console.error(`No existe la carpeta: ${root}`)
  process.exit(1)
}

async function walk(directory) {
  const results = []

  const entries = await fsp.readdir(directory, {
    withFileTypes: true,
  })

  for (const entry of entries) {
    if (
      entry.name === ".git" ||
      entry.name === ".venv" ||
      entry.name === "node_modules" ||
      entry.name === "__pycache__"
    ) {
      continue
    }

    const fullPath = path.join(directory, entry.name)

    if (entry.isDirectory()) {
      results.push(...await walk(fullPath))
    } else if (entry.isFile()) {
      results.push(fullPath)
    }
  }

  return results
}

function createCacheKey(relativePath, stats) {
  return crypto
    .createHash("sha1")
    .update([
      relativePath,
      stats.size,
      Math.trunc(stats.mtimeMs),
      MAX_SIZE,
      QUALITY,
      EFFORT,
      "heic-sips-v2",
    ].join("|"))
    .digest("hex")
}

async function prepareInput(sourcePath) {
  const extension = path
    .extname(sourcePath)
    .toLowerCase()

  if (!heicExtensions.has(extension)) {
    return {
      inputPath: sourcePath,
      cleanup: async () => {},
    }
  }

  const temporaryPath = path.join(
    os.tmpdir(),
    `atlas-heic-${crypto.randomUUID()}.jpg`,
  )

  await execFileAsync(
    "/usr/bin/sips",
    [
      "-s",
      "format",
      "jpeg",
      sourcePath,
      "--out",
      temporaryPath,
    ],
    {
      maxBuffer: 10 * 1024 * 1024,
    },
  )

  return {
    inputPath: temporaryPath,
    cleanup: async () => {
      await fsp.rm(temporaryPath, {
        force: true,
      })
    },
  }
}

function replaceImageName(text, oldName, newName) {
  const variants = new Set([
    oldName,
    oldName.normalize("NFC"),
    oldName.normalize("NFD"),
    encodeURI(oldName),
    encodeURI(oldName.normalize("NFC")),
    encodeURI(oldName.normalize("NFD")),
  ])

  let result = text

  for (const variant of variants) {
    const replacement = variant.includes("%")
      ? encodeURI(newName)
      : newName

    result = result.split(variant).join(replacement)
  }

  return result
}

function formatMB(bytes) {
  return `${(bytes / 1024 / 1024).toFixed(1)} MB`
}

await fsp.mkdir(cacheDirectory, {
  recursive: true,
})

const files = await walk(root)

const images = files.filter((filePath) =>
  supportedExtensions.has(
    path.extname(filePath).toLowerCase(),
  ),
)

const conversions = []

let originalBytes = 0
let optimizedBytes = 0
let cacheHits = 0
let failures = 0
let keptOriginals = 0
let heicConverted = 0

console.log(
  `Optimizando ${images.length} imágenes para la web...`,
)

for (let index = 0; index < images.length; index += 1) {
  const sourcePath = images[index]

  const relativePath = path
    .relative(root, sourcePath)
    .replaceAll(path.sep, "/")

  const sourceStats = await fsp.stat(sourcePath)

  const cacheKey = createCacheKey(
    relativePath,
    sourceStats,
  )

  const cachedPath = path.join(
    cacheDirectory,
    `${cacheKey}.webp`,
  )

  const targetPath = `${sourcePath}.webp`

  let preparedInput = null

  try {
    if (fs.existsSync(cachedPath)) {
      cacheHits += 1
    } else {
      preparedInput = await prepareInput(sourcePath)

      if (
        heicExtensions.has(
          path.extname(sourcePath).toLowerCase(),
        )
      ) {
        heicConverted += 1
      }

      const temporaryOutput =
        `${cachedPath}.tmp-${process.pid}`

      await sharp(preparedInput.inputPath, {
        failOn: "none",
        limitInputPixels: false,
      })
        .rotate()
        .resize({
          width: MAX_SIZE,
          height: MAX_SIZE,
          fit: "inside",
          withoutEnlargement: true,
        })
        .webp({
          quality: QUALITY,
          effort: EFFORT,
          smartSubsample: true,
          alphaQuality: 95,
        })
        .toFile(temporaryOutput)

      await fsp.rename(
        temporaryOutput,
        cachedPath,
      )
    }

    await fsp.copyFile(
      cachedPath,
      targetPath,
    )

    const targetStats = await fsp.stat(targetPath)

    if (targetStats.size >= sourceStats.size) {
      await fsp.rm(targetPath, {
        force: true,
      })

      keptOriginals += 1
      continue
    }

    originalBytes += sourceStats.size
    optimizedBytes += targetStats.size

    conversions.push({
      sourcePath,
      oldName: path.basename(sourcePath),
      newName: path.basename(targetPath),
    })
  } catch (error) {
    failures += 1

    await fsp.rm(targetPath, {
      force: true,
    }).catch(() => {})

    console.warn(`No se pudo optimizar: ${relativePath}`)

    console.warn(
      error instanceof Error
        ? error.message
        : String(error),
    )
  } finally {
    if (preparedInput) {
      await preparedInput.cleanup()
    }
  }

  if (
    (index + 1) % 25 === 0 ||
    index + 1 === images.length
  ) {
    console.log(
      `Procesadas ${index + 1}/${images.length}`,
    )
  }
}

const markdownFiles = files.filter(
  (filePath) =>
    path.extname(filePath).toLowerCase() === ".md",
)

let updatedNotes = 0

for (const markdownPath of markdownFiles) {
  const originalContent = await fsp.readFile(
    markdownPath,
    "utf8",
  )

  let updatedContent = originalContent

  for (const conversion of conversions) {
    updatedContent = replaceImageName(
      updatedContent,
      conversion.oldName,
      conversion.newName,
    )
  }

  if (updatedContent !== originalContent) {
    await fsp.writeFile(
      markdownPath,
      updatedContent,
      "utf8",
    )

    updatedNotes += 1
  }
}

for (const conversion of conversions) {
  await fsp.rm(conversion.sourcePath, {
    force: true,
  })
}

const savedBytes =
  originalBytes - optimizedBytes

const savingPercentage =
  originalBytes > 0
    ? (
        (savedBytes / originalBytes) *
        100
      ).toFixed(1)
    : "0.0"

console.log("")
console.log(`Convertidas a WebP: ${conversions.length}`)
console.log(`HEIC procesadas con macOS: ${heicConverted}`)
console.log(`Notas actualizadas: ${updatedNotes}`)
console.log(`Recuperadas de caché: ${cacheHits}`)
console.log(`Originales más pequeños conservados: ${keptOriginals}`)
console.log(`Errores: ${failures}`)
console.log(`Peso anterior: ${formatMB(originalBytes)}`)
console.log(`Peso web: ${formatMB(optimizedBytes)}`)
console.log(
  `Ahorro: ${formatMB(savedBytes)} (${savingPercentage} %)`,
)
