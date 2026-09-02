#!/usr/bin/env node

import fs from "node:fs/promises"
import path from "node:path"
import os from "node:os"
import { execFile } from "node:child_process"
import { promisify } from "node:util"
import sharp from "sharp"

const execFileAsync = promisify(execFile)

const ROOT = path.resolve(process.argv[2] || "")
if (!ROOT) {
  console.error("Uso: node optimizar-imagenes-web.mjs <carpeta>")
  process.exit(1)
}

const MAX_SIZE = 2400
const QUALITY = 85
const EFFORT = 4
const RASTER = new Set([
  ".jpg", ".jpeg", ".png", ".tif", ".tiff", ".heic", ".heif",
])

async function walk(dir) {
  const out = []
  for (const entry of await fs.readdir(dir, { withFileTypes: true })) {
    if (entry.name === ".DS_Store") continue
    const full = path.join(dir, entry.name)
    if (entry.isDirectory()) {
      out.push(...await walk(full))
    } else if (entry.isFile()) {
      out.push(full)
    }
  }
  return out
}

function variants(value) {
  const values = new Set([
    value,
    value.normalize("NFC"),
    value.normalize("NFD"),
  ])
  for (const v of [...values]) {
    try {
      values.add(encodeURI(v))
    } catch {}
  }
  return [...values].sort((a, b) => b.length - a.length)
}

function replaceAllLiteral(text, from, to) {
  if (!from || from === to) return text
  return text.split(from).join(to)
}

function escapeRegExp(value) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")
}

const allFiles = await walk(ROOT)
const images = allFiles.filter((file) =>
  RASTER.has(path.extname(file).toLowerCase()),
)

let converted = 0
let heicConverted = 0
let errors = 0
let oldBytes = 0
let webBytes = 0

const conversions = []

for (let i = 0; i < images.length; i++) {
  const source = images[i]
  const ext = path.extname(source).toLowerCase()
  const oldName = path.basename(source)
  const newName = `${oldName}.webp`
  const target = `${source}.webp`

  let tempInput = null

  try {
    const before = await fs.stat(source)
    oldBytes += before.size

    let input = source

    if (ext === ".heic" || ext === ".heif") {
      tempInput = path.join(
        os.tmpdir(),
        `kwy-heic-${process.pid}-${i}.jpg`,
      )

      await execFileAsync("/usr/bin/sips", [
        "-s", "format", "jpeg",
        source,
        "--out", tempInput,
      ])

      input = tempInput
      heicConverted += 1
    }

    await sharp(input)
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
      })
      .toFile(target)

    const after = await fs.stat(target)
    webBytes += after.size

    // Política obligatoria: si la conversión funcionó, WebP siempre gana.
    await fs.rm(source)

    conversions.push({
      oldName,
      newName,
      stem: path.basename(source, path.extname(source)),
    })

    converted += 1
  } catch (error) {
    errors += 1
    console.error(`ERROR: ${source}`)
    console.error(`  ${error.message}`)
    try { await fs.rm(target) } catch {}
  } finally {
    if (tempInput) {
      try { await fs.rm(tempInput) } catch {}
    }
  }

  const done = i + 1
  if (done % 25 === 0 || done === images.length) {
    console.log(`Procesadas ${done}/${images.length}`)
  }
}

// Un basename se actualiza una sola vez aunque exista físicamente
// en varias operaciones.
const markdownConversions = new Map()

for (const conversion of conversions) {
  const key = conversion.oldName.normalize("NFC").toLowerCase()
  const existing = markdownConversions.get(key)

  if (existing && existing.newName !== conversion.newName) {
    throw new Error(`Conflicto de conversión para ${conversion.oldName}`)
  }

  if (!existing) markdownConversions.set(key, conversion)
}

// Para wikilinks Obsidian sin extensión: solo reemplazar cuando el stem
// conduce de forma inequívoca a un único nombre WebP.
const stemTargets = new Map()

for (const conversion of markdownConversions.values()) {
  const key = conversion.stem.normalize("NFC").toLowerCase()
  if (!stemTargets.has(key)) stemTargets.set(key, new Set())
  stemTargets.get(key).add(conversion.newName)
}

console.log(
  `Nombres únicos a actualizar en Markdown: ${markdownConversions.size}`,
)

const markdownFiles = (await walk(ROOT)).filter(
  (file) => path.extname(file).toLowerCase() === ".md",
)

let updatedNotes = 0

for (const md of markdownFiles) {
  let content = await fs.readFile(md, "utf8")
  let updated = content

  for (const conversion of markdownConversions.values()) {
    for (const oldVariant of variants(conversion.oldName)) {
      const newVariant = oldVariant.includes("%")
        ? encodeURI(conversion.newName)
        : conversion.newName

      updated = replaceAllLiteral(updated, oldVariant, newVariant)
    }
  }

  // ![[archivo|200]] -> ![[archivo.jpg.webp|200]]
  // solo si ese stem tiene un único destino posible.
  for (const [stemKey, targets] of stemTargets.entries()) {
    if (targets.size !== 1) continue
    const target = [...targets][0]

    const stems = new Set()
    for (const conversion of markdownConversions.values()) {
      if (conversion.stem.normalize("NFC").toLowerCase() === stemKey) {
        stems.add(conversion.stem)
      }
    }

    for (const stem of stems) {
      for (const stemVariant of variants(stem)) {
        const re = new RegExp(
          `!\\[\\[${escapeRegExp(stemVariant)}(\\|[^\\]]+)?\\]\\]`,
          "g",
        )
        updated = updated.replace(
          re,
          (_match, alias = "") => `![[${target}${alias}]]`,
        )
      }
    }
  }

  if (updated !== content) {
    await fs.writeFile(md, updated, "utf8")
    updatedNotes += 1
  }
}

const mb = (bytes) => bytes / 1024 / 1024
const saved = oldBytes - webBytes
const pct = oldBytes ? (saved / oldBytes) * 100 : 0

console.log("")
console.log(`Convertidas a WebP: ${converted}`)
console.log(`HEIC procesadas con macOS: ${heicConverted}`)
console.log(`Notas actualizadas: ${updatedNotes}`)
console.log("Política de imagen: WebP obligatorio")
console.log("Cache permanente de imágenes: NO")
console.log(`Errores: ${errors}`)
console.log(`Peso anterior: ${mb(oldBytes).toFixed(1)} MB`)
console.log(`Peso web: ${mb(webBytes).toFixed(1)} MB`)
console.log(`Ahorro: ${mb(saved).toFixed(1)} MB (${pct.toFixed(1)} %)`)

if (errors > 0) {
  process.exitCode = 1
}
