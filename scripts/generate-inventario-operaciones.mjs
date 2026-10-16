import fs from "node:fs"
import path from "node:path"

const root = process.cwd()
const content = path.join(root, "content")
const operations = path.join(content, "01_OPERACIONES")
const output = path.join(content, "INVENTARIO_OPERACIONES.md")

const provisional = {
  OB_028: "OB028_step09.jpg.webp",
  OB_029: "OB029_step12.png.webp",
  OB_033: "OB033_step09.jpg.webp",
  OB_034: "OB034_step07.jpg.webp",
  OB_035: "OB035_step12.png.webp",
}

function walk(dir) {
  const found = []
  for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, item.name)
    if (item.isDirectory()) found.push(...walk(full))
    else if (item.isFile()) found.push(full)
  }
  return found
}

function clean(value = "") {
  return value
    .replace(/\[\[([^\]|]+)(?:\|[^\]]+)?\]\]/g, "$1")
    .replace(/\*\*/g, "")
    .replace(/\s+/g, " ")
    .trim()
}

function cell(value = "") {
  return clean(value).replace(/\|/g, "\\|")
}

function field(text, label) {
  const match = text.match(new RegExp(`^\\s*${label}::\\s*(.+)$`, "m"))
  return match ? clean(match[1]) : "Pendiente"
}

function section(text, heading) {
  const at = text.search(heading)
  if (at < 0) return ""
  return text.slice(at).split(/^---\s*$/m, 1)[0]
}

function images(text) {
  return [...text.matchAll(/!\[\[([^\]|]+)(?:\\?\|[^\]]+)?\]\]/g)]
    .map(match => match[1].trim())
}

function description(text) {
  const match = text.match(/\*\*Descripción operativa:\*\*\s*\n([\s\S]*?)(?=\n---|\n\*\*|\n##)/)
  return match ? clean(match[1]) : "No especificada"
}

function scriptAvailable(text) {
  const match = text.match(/^\*\*Script[^*]*:\*\*\s*(.+)$/m)
  if (!match) return "No"
  const value = match[1].toLowerCase()
  return /\.(py|js|mjs|sh)\b/.test(value) && !/perdido|no recuperado|sin verificar/.test(value)
    ? "Sí"
    : "No"
}

function findAsset(reference, operationDir) {
  const name = path.basename(reference)
  const candidates = walk(operationDir).filter(file => path.basename(file) === name)
  if (candidates.length === 1) return candidates[0]
  const all = walk(content).filter(file => path.basename(file) === name)
  return all.length === 1 ? all[0] : null
}

const fichas = walk(operations)
  .filter(file => /\/\d{3}_FICHA\/OB_\d{3}.*\.md$/i.test(file))
  .sort()

const rows = fichas.map(file => {
  const text = fs.readFileSync(file, "utf8")
  const code = path.basename(file).match(/^(OB_\d{3})/i)?.[1]?.toUpperCase()
  const opDir = path.dirname(path.dirname(file))
  const regimeDir = path.dirname(opDir)
  const regime = path.basename(regimeDir).replaceAll("_", " ")
  const title = clean(text.match(/^#\s+(.+)$/m)?.[1] ?? path.basename(opDir))
    .replace(new RegExp(`^${code}\\s*[—-]\\s*`, "i"), "")
  const direct = fs.readdirSync(regimeDir, { withFileTypes: true })
    .filter(item => item.isFile() && new RegExp(`^${code}\\b`, "i").test(item.name))
    .map(item => path.join(regimeDir, item.name))[0]
  const target = direct ?? file
  const link = path.relative(content, target).replace(/\\/g, "/").replace(/\.md$/, "")
  const perception = section(text, /###\s+Crisis\s*\/\s*umbral según mi percepción/i)
  const chosen = images(perception)[0] ?? provisional[code] ?? null
  const asset = chosen ? findAsset(chosen, opDir) : null
  const assetLink = asset
    ? `![[${path.relative(content, asset).replace(/\\/g, "/")}\\|200]]`
    : "Pendiente"
  const note = images(perception).length ? "" : " (provisional)"

  return {
    code,
    title,
    regime,
    rule: description(text),
    works: field(text, "Funciona"),
    script: scriptAvailable(text),
    image: assetLink + note,
    link,
  }
})

rows.sort((a, b) => a.code.localeCompare(b.code, "es", { numeric: true }))

const table = [
  "| Código | Nombre | Régimen | Regla | Funciona | Script disponible | Imagen seleccionada según mi percepción |",
  "| --- | --- | --- | --- | --- | --- | --- |",
  ...rows.map(row => `| ${row.code} | [[${row.link}|${cell(row.title)}]] | ${cell(row.regime)} | ${cell(row.rule)} | ${cell(row.works)} | ${row.script} | ${row.image} |`),
]

const markdown = [
  "# Inventario de operaciones",
  "",
  "La miniatura corresponde a la imagen elegida en la sección «Crisis / umbral según mi percepción» de cada ficha. Cuando la ficha todavía no la define, se muestra una selección provisional para revisión.",
  "",
  ...table,
  "",
].join("\n")

fs.writeFileSync(output, markdown, "utf8")
console.log(`Inventario actualizado: ${rows.length} operaciones.`)
