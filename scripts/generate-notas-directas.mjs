import fs from "node:fs"
import path from "node:path"

const OPERACIONES = path.resolve("content", "01_OPERACIONES")

function getMarkdownFiles(directory) {
  if (!fs.existsSync(directory)) return []

  const results = []

  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    if (entry.name.startsWith(".")) continue
    if (entry.name === ".venv") continue
    if (entry.name === "__pycache__") continue
    if (entry.name === "node_modules") continue

    const fullPath = path.join(directory, entry.name)

    if (entry.isDirectory()) {
      results.push(...getMarkdownFiles(fullPath))
    } else if (entry.isFile() && entry.name.toLowerCase().endsWith(".md")) {
      results.push(fullPath)
    }
  }

  return results
}

function findFichaNote(operationDirectory) {
  const fichaDirectories = fs
    .readdirSync(operationDirectory, { withFileTypes: true })
    .filter((entry) => entry.isDirectory() && /ficha/i.test(entry.name))
    .map((entry) => path.join(operationDirectory, entry.name))

  for (const fichaDirectory of fichaDirectories) {
    const files = getMarkdownFiles(fichaDirectory)

    const preferred =
      files.find((file) => /^OB[_-]?\d+/i.test(path.basename(file))) ??
      files[0]

    if (preferred) return preferred
  }

  return null
}

function createTitle(folderName) {
  const match = folderName.match(/^(OB[_-]?\d+)[_-]+(.+)$/i)

  if (!match) {
    return folderName.replaceAll("_", " ")
  }

  const code = match[1]
    .toUpperCase()
    .replace(/^OB-/, "OB_")

  const name = match[2]
    .replaceAll("_", " ")
    .replace(/\s+/g, " ")
    .trim()

  return `${code} — ${name}`
}

function rebasePath(target, sourceDirectory, destinationDirectory) {
  const original = target
  let value = target.trim()

  if (
    !value.startsWith(".") ||
    value.startsWith("http://") ||
    value.startsWith("https://")
  ) {
    return original
  }

  let opening = ""
  let closing = ""

  if (value.startsWith("<") && value.endsWith(">")) {
    opening = "<"
    closing = ">"
    value = value.slice(1, -1)
  }

  const suffixPosition = value.search(/[?#]/)

  const pathname =
    suffixPosition >= 0
      ? value.slice(0, suffixPosition)
      : value

  const suffix =
    suffixPosition >= 0
      ? value.slice(suffixPosition)
      : ""

  const absolutePath = path.resolve(sourceDirectory, pathname)

  let relativePath = path
    .relative(destinationDirectory, absolutePath)
    .replaceAll(path.sep, "/")

  if (!relativePath.startsWith(".")) {
    relativePath = `./${relativePath}`
  }

  return `${opening}${relativePath}${suffix}${closing}`
}

function rewriteLinks(content, sourceFile, destinationFile) {
  const sourceDirectory = path.dirname(sourceFile)
  const destinationDirectory = path.dirname(destinationFile)

  // Enlaces y embeds de Obsidian:
  // [[../archivo]] y ![[../imagen.png]]
  content = content.replace(
    /(!?\[\[)([^\]]+)(\]\])/g,
    (complete, opening, inside, closing) => {
      const pipePosition = inside.indexOf("|")

      const target =
        pipePosition >= 0
          ? inside.slice(0, pipePosition)
          : inside

      const alias =
        pipePosition >= 0
          ? inside.slice(pipePosition)
          : ""

      const rewritten = rebasePath(
        target,
        sourceDirectory,
        destinationDirectory,
      )

      return `${opening}${rewritten}${alias}${closing}`
    },
  )

  // Enlaces Markdown:
  // [texto](../archivo) y ![](../imagen.png)
  content = content.replace(
    /(!?\[[^\]]*\]\()([^)]+)(\))/g,
    (complete, opening, inside, closing) => {
      const trimmed = inside.trim()

      const targetMatch = trimmed.match(
        /^(<[^>]+>|\S+)([\s\S]*)$/,
      )

      if (!targetMatch) return complete

      const target = targetMatch[1]
      const extra = targetMatch[2] ?? ""

      const rewritten = rebasePath(
        target,
        sourceDirectory,
        destinationDirectory,
      )

      return `${opening}${rewritten}${extra}${closing}`
    },
  )

  return content
}

function addGeneratedFrontmatter(content, title) {
  const frontmatterRegex =
    /^---\r?\n([\s\S]*?)\r?\n---\r?\n?/

  const match = content.match(frontmatterRegex)

  if (!match) {
    return `---
title: ${JSON.stringify(title)}
atlas_direct: true
---

${content}`
  }

  let existingFrontmatter = match[1]

  existingFrontmatter = existingFrontmatter
    .replace(/^title:.*(?:\r?\n|$)/m, "")
    .replace(/^atlas_direct:.*(?:\r?\n|$)/m, "")
    .trim()

  const newFrontmatter = [
    "---",
    `title: ${JSON.stringify(title)}`,
    "atlas_direct: true",
    existingFrontmatter,
    "---",
    "",
  ]
    .filter((line, index) => {
      if (index === 3 && line === "") return false
      return true
    })
    .join("\n")

  return newFrontmatter + content.slice(match[0].length)
}

function removePreviouslyGeneratedNotes(regimeDirectory) {
  for (const entry of fs.readdirSync(regimeDirectory, {
    withFileTypes: true,
  })) {
    if (!entry.isFile()) continue
    if (!entry.name.toLowerCase().endsWith(".md")) continue

    const fullPath = path.join(regimeDirectory, entry.name)
    const content = fs.readFileSync(fullPath, "utf8")

    if (/^atlas_direct:\s*true\s*$/m.test(content)) {
      fs.rmSync(fullPath)
    }
  }
}

if (!fs.existsSync(OPERACIONES)) {
  console.error(`No existe la carpeta: ${OPERACIONES}`)
  process.exit(1)
}

let total = 0

const regimeDirectories = fs
  .readdirSync(OPERACIONES, { withFileTypes: true })
  .filter((entry) => entry.isDirectory())
  .map((entry) => path.join(OPERACIONES, entry.name))

for (const regimeDirectory of regimeDirectories) {
  removePreviouslyGeneratedNotes(regimeDirectory)

  const operationDirectories = fs
    .readdirSync(regimeDirectory, { withFileTypes: true })
    .filter(
      (entry) =>
        entry.isDirectory() &&
        /^OB[_-]?\d+/i.test(entry.name),
    )
    .sort((a, b) =>
      a.name.localeCompare(b.name, "es", {
        numeric: true,
      }),
    )

  let regimeTotal = 0

  for (const operation of operationDirectories) {
    const operationDirectory = path.join(
      regimeDirectory,
      operation.name,
    )

    const sourceFile = findFichaNote(operationDirectory)

    if (!sourceFile) {
      console.warn(
        `Sin ficha Markdown: ${operationDirectory}`,
      )
      continue
    }

    const title = createTitle(operation.name)

    const safeFilename = `${title
      .replaceAll("/", "-")
      .replaceAll(":", " -")}.md`

    const destinationFile = path.join(
      regimeDirectory,
      safeFilename,
    )

    let content = fs.readFileSync(sourceFile, "utf8")

    content = rewriteLinks(
      content,
      sourceFile,
      destinationFile,
    )

    content = addGeneratedFrontmatter(
      content,
      title,
    )

    fs.writeFileSync(
      destinationFile,
      content.trimEnd() + "\n",
      "utf8",
    )

    regimeTotal += 1
    total += 1
  }

  console.log(
    `${path.basename(regimeDirectory)}: ${regimeTotal} notas directas`,
  )
}

console.log(`Total generado: ${total} notas directas.`)
