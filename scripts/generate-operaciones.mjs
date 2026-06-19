import fs from "fs"
import path from "path"

const root = process.cwd()
const contentDir = path.join(root, "content")
const operacionesDir = path.join(contentDir, "01_OPERACIONES")
const outputFile = path.join(contentDir, "index.md")

const START = "<!-- OPERACIONES_AUTO_START -->"
const END = "<!-- OPERACIONES_AUTO_END -->"

function walk(dir) {
  let results = []
  if (!fs.existsSync(dir)) return results

  for (const item of fs.readdirSync(dir)) {
    const fullPath = path.join(dir, item)
    const stat = fs.statSync(fullPath)

    if (stat.isDirectory()) {
      results = results.concat(walk(fullPath))
    } else if (item.endsWith(".md")) {
      results.push(fullPath)
    }
  }

  return results
}

function clean(value = "") {
  return value
    .replace(/\[\[([^\]|]+)(?:\|[^\]]+)?\]\]/g, "$1")
    .replace(/"/g, "")
    .trim()
}

function getInlineField(text, field) {
  const regex = new RegExp("^\\s*" + field + "::\\s*(.+)$", "m")
  const match = text.match(regex)
  return match ? clean(match[1]) : ""
}

function getTitle(text, filePath) {
  const heading = text.match(/^#\s+(.+)$/m)
  if (heading) return heading[1].trim()

  return path.basename(filePath, ".md").replace(/_/g, " ").trim()
}

function getFamily(filePath) {
  const relative = path.relative(operacionesDir, filePath).replace(/\\/g, "/")
  return relative.split("/")[0] || "Sin familia"
}

function cleanLabel(value = "") {
  return value.replace(/_/g, " ").trim()
}

function getWikiLink(filePath, title) {
  const relative = path
    .relative(contentDir, filePath)
    .replace(/\\/g, "/")
    .replace(/\.md$/, "")

  return "[[" + relative + "|" + title + "]]"
}

const files = walk(operacionesDir)

const operaciones = files
  .filter(file => /^OB_\d{3}/i.test(path.basename(file)))
  .map(file => {
    const text = fs.readFileSync(file, "utf8")

    return {
      file,
      title: getTitle(text, file),
      familia: getFamily(file),
      estado: getInlineField(text, "Estado"),
      funciona: getInlineField(text, "Funciona"),
      trabaja: getInlineField(text, "Trabaja_en_lo"),
      crisis: getInlineField(text, "Crisis"),
    }
  })
  .filter(op => op.estado.includes("Terminada"))
  .sort((a, b) => a.title.localeCompare(b.title, "es"))

const grupos = {}

for (const op of operaciones) {
  if (!grupos[op.familia]) grupos[op.familia] = []
  grupos[op.familia].push(op)
}

let lista = ""

for (const familia of Object.keys(grupos).sort((a, b) => a.localeCompare(b, "es"))) {
  lista += "\n### " + cleanLabel(familia) + "\n\n"

  for (const op of grupos[familia]) {
    lista += "- " + getWikiLink(op.file, op.title) + "\n"

    const datos = []
    if (op.trabaja) datos.push("Trabaja en: " + op.trabaja)
    if (op.crisis) datos.push("Crisis: " + op.crisis)
    if (op.funciona) datos.push("Funciona: " + op.funciona)

    if (datos.length > 0) {
      lista += "  " + datos.join(" · ") + "\n"
    }

    lista += "\n"
  }
}

let indexText = ""

if (fs.existsSync(outputFile)) {
  indexText = fs.readFileSync(outputFile, "utf8")
} else {
  indexText = `# Atlas Operativo

## OPERACIONES

${START}
${END}
`
}

const generatedBlock = START + "\n" + lista.trim() + "\n" + END

if (indexText.includes(START) && indexText.includes(END)) {
  const regex = new RegExp(START + "[\\s\\S]*?" + END)
  indexText = indexText.replace(regex, generatedBlock)
} else {
  indexText += "\n\n## OPERACIONES\n\n" + generatedBlock + "\n"
}

fs.writeFileSync(outputFile, indexText, "utf8")

console.log("Index actualizado sin sobrescribir el texto. Operaciones terminadas: " + operaciones.length)
