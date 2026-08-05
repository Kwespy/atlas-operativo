import fs from "node:fs"
import path from "node:path"

const CONTENT = path.resolve("content")
const OPERACIONES = path.join(CONTENT, "01_OPERACIONES")

const REGIMENES = [
  {
    folder: "Captura_Materializacion",
    listFile: "Lista_Captura_Materializacion.md",
    title: "Captura y materialización",
  },
  {
    folder: "Intervencion_Fisica",
    listFile: "Lista_Intervencion_Fisica.md",
    title: "Intervención física",
  },
  {
    folder: "Traduccion_Sistemas_Representación",
    listFile: "Lista_Traduccion_Sistemas_Representación.md",
    title: "Traducción entre sistemas de representación",
  },
  {
    folder: "Transformacion_Algoritmica",
    listFile: "Lista_Transformacion_Algoritmica.md",
    title: "Transformación algorítmica",
  },
]

const START = "<!-- AUTO-LISTA-REGIMEN:START -->"
const END = "<!-- AUTO-LISTA-REGIMEN:END -->"

function escapeRegExp(text) {
  return text.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")
}

function getMarkdownFiles(directory) {
  if (!fs.existsSync(directory)) return []

  const results = []

  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    if (entry.name.startsWith(".")) continue
    if (entry.name === "node_modules") continue
    if (entry.name === "__pycache__") continue
    if (entry.name === ".venv") continue

    const fullPath = path.join(directory, entry.name)

    if (entry.isDirectory()) {
      results.push(...getMarkdownFiles(fullPath))
    } else if (entry.isFile() && entry.name.toLowerCase().endsWith(".md")) {
      results.push(fullPath)
    }
  }

  return results
}

function getTitle(filePath) {
  const content = fs.readFileSync(filePath, "utf8")

  const h1 = content.match(/^#\s+(.+)$/m)

  if (h1) {
    return h1[1]
      .trim()
      .replace(/\[\[|\]\]/g, "")
  }

  return path.basename(filePath, ".md").replaceAll("_", " ")
}

function getOperationNumber(filePath) {
  const match = filePath.match(/OB[_-]?(\d+)/i)
  return match ? Number(match[1]) : 999999
}

function findExistingListFile(regimeDirectory, preferredName) {
  const preferredPath = path.join(regimeDirectory, preferredName)

  if (fs.existsSync(preferredPath)) {
    return preferredPath
  }

  const possibleList = fs
    .readdirSync(regimeDirectory)
    .find(
      (name) =>
        /^Lista_.*\.md$/i.test(name) ||
        /^Lista .*\.md$/i.test(name),
    )

  if (possibleList) {
    return path.join(regimeDirectory, possibleList)
  }

  return preferredPath
}

function createStaticList(regimeDirectory, listPath) {
  const markdownFiles = getMarkdownFiles(regimeDirectory)

  const operationFiles = markdownFiles
    .filter((filePath) => filePath !== listPath)
    .filter((filePath) => {
      const filename = path.basename(filePath).toLowerCase()

      if (filename === "index.md") return false
      if (filename.startsWith("lista_")) return false
      if (filename.startsWith("lista ")) return false

      const segments = filePath.split(path.sep)

      return segments.some((segment) => /_FICHA$/i.test(segment))
    })
    .sort((a, b) => {
      const numberA = getOperationNumber(a)
      const numberB = getOperationNumber(b)

      if (numberA !== numberB) {
        return numberA - numberB
      }

      return a.localeCompare(b, "es")
    })

  return operationFiles.map((filePath) => {
    const relativePath = path
      .relative(regimeDirectory, filePath)
      .replaceAll(path.sep, "/")
      .replace(/\.md$/i, "")

    const title = getTitle(filePath)

    return `- [[${relativePath}|${title}]]`
  })
}

function updateListFile(listPath, regimeTitle, listItems) {
  let content

  if (fs.existsSync(listPath)) {
    content = fs.readFileSync(listPath, "utf8")
  } else {
    content = `# ${regimeTitle}\n`
  }

  const generatedContent =
    listItems.length > 0
      ? listItems.join("\n")
      : "_Todavía no hay operaciones publicables en este régimen._"

  const automaticBlock = `${START}
${generatedContent}
${END}`

  const automaticBlockRegex = new RegExp(
    `${escapeRegExp(START)}[\\s\\S]*?${escapeRegExp(END)}`,
    "m",
  )

  const dataviewRegex = /```dataview\s*[\s\S]*?```/i

  if (automaticBlockRegex.test(content)) {
    content = content.replace(automaticBlockRegex, automaticBlock)
  } else if (dataviewRegex.test(content)) {
    content = content.replace(dataviewRegex, automaticBlock)
  } else {
    content = `${content.trimEnd()}\n\n${automaticBlock}\n`
  }

  fs.mkdirSync(path.dirname(listPath), { recursive: true })
  fs.writeFileSync(listPath, content, "utf8")
}

if (!fs.existsSync(OPERACIONES)) {
  console.error(`No se encontró la carpeta: ${OPERACIONES}`)
  process.exit(1)
}

let totalOperations = 0

for (const regimen of REGIMENES) {
  const regimeDirectory = path.join(OPERACIONES, regimen.folder)

  if (!fs.existsSync(regimeDirectory)) {
    console.warn(`No se encontró el régimen: ${regimen.folder}`)
    continue
  }

  const listPath = findExistingListFile(
    regimeDirectory,
    regimen.listFile,
  )

  const listItems = createStaticList(regimeDirectory, listPath)

  updateListFile(listPath, regimen.title, listItems)

  totalOperations += listItems.length

  console.log(
    `${regimen.title}: ${listItems.length} operaciones`,
  )
}

console.log(
  `Listas estáticas actualizadas. Total: ${totalOperations} operaciones.`,
)
