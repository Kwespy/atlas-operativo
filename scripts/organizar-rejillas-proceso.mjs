import fs from "node:fs"
import path from "node:path"

const roots = [path.resolve("content"), path.resolve("content_en")]

function walk(dir) {
  const files = []
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name)
    if (entry.isDirectory()) files.push(...walk(full))
    else if (entry.isFile() && entry.name.endsWith(".md")) files.push(full)
  }
  return files
}

function tableFor(block) {
  const steps = [...block.matchAll(/^### (Step[^\n]+)\r?\n+!\[\[([^\n\]]+)\]\]\s*$/gm)]
    .map(match => ({
      title: match[1].trim(),
      image: match[2].trim().replaceAll("|", "\\|"),
    }))

  if (steps.length < 2) return block

  const cells = steps.map(step => `${step.title}<br>![[${step.image}]]`)
  while (cells.length % 3) cells.push("")
  const rows = []
  for (let i = 0; i < cells.length; i += 3) rows.push(`| ${cells.slice(i, i + 3).join(" | ")} |`)

  return [
    "| | | |",
    "| --- | --- | --- |",
    ...rows,
  ].join("\n") + "\n"
}

function transform(text) {
  const section = /(^## 4\. (?:Secuencia visual|Visual sequence)\r?\n)([\s\S]*?)(?=^---\s*$)/gm
  return text.replace(section, (_whole, heading, body) => {
    const groupedSteps = /(?:(?:^### Step[^\n]+\r?\n+!\[\[[^\n\]]+\]\]\s*\r?\n+){2,})/gm
    return heading + body.replace(groupedSteps, tableFor)
  })
}

let updated = 0
for (const root of roots) {
  if (!fs.existsSync(root)) continue
  for (const file of walk(root)) {
    const before = fs.readFileSync(file, "utf8")
    const after = transform(before)
    if (after !== before) {
      fs.writeFileSync(file, after, "utf8")
      updated++
    }
  }
}

console.log(`Rejillas de proceso actualizadas: ${updated} páginas.`)
