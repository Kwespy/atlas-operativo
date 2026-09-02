import fs from "fs"
import path from "path"

const root = process.argv[2]

if (!root) {
  console.error("Uso: node scripts/localize-en-display.mjs <carpeta>")
  process.exit(1)
}

const rootPath = path.resolve(root)

function walk(dir) {
  let files = []

  if (!fs.existsSync(dir)) return files

  for (const item of fs.readdirSync(dir)) {
    const full = path.join(dir, item)
    const stat = fs.statSync(full)

    if (stat.isDirectory()) {
      files = files.concat(walk(full))
    } else if (item.endsWith(".md")) {
      files.push(full)
    }
  }

  return files
}

/*
 * Rutas ES -> EN.
 *
 * SOLO se aplica a segmentos de ruta.
 * No renombra archivos OB ni archivos Lista_.
 */
const replacements = [
  ["01_OPERACIONES", "01_OPERATIONS"],
  ["02_COMBINACIONES", "02_COMBINATIONS"],

  ["Captura_Materializacion",
   "Capture and Materialization"],

  ["Intervencion_Fisica",
   "Direct Material Intervention"],

  ["Traduccion_Sistemas_Representación",
   "Translation Between Representation Systems"],

  ["Traduccion_Sistemas_Representacion",
   "Translation Between Representation Systems"],

  ["Transformacion_Algoritmica",
   "Algorithmic Transformation"],
]

function escapeRegex(value) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")
}

/*
 * Cambiar solamente segmentos de rutas dentro de Markdown.
 *
 * Ej:
 * 01_OPERACIONES/Captura_Materializacion/OB_001...
 *
 * pasa a:
 *
 * 01_OPERATIONS/Capture and Materialization/OB_001...
 */
for (const file of walk(rootPath)) {
  let text = fs.readFileSync(file, "utf8")
  const original = text

  /*
   * El primer segmento de los wikilinks no era capturado
   * por el reemplazo de segmentos anterior.
   *
   * ES:
   * [[01_OPERACIONES/Captura_Materializacion/OB_001...]]
   *
   * EN:
   * [[01_OPERATIONS/Capture and Materialization/OB_001...]]
   */
  text = text.replaceAll(
    "01_OPERACIONES/",
    "01_OPERATIONS/",
  )

  text = text.replaceAll(
    "02_COMBINACIONES/",
    "02_COMBINATIONS/",
  )

  for (const [from, to] of replacements) {
    const escaped = escapeRegex(from)

    // segmento seguido por /
    text = text.replace(
      new RegExp(`(^|[/\\\\])${escaped}(?=[/\\\\])`, "g"),
      (_, prefix) => prefix + to,
    )
  }

  /*
   * Nombres visibles de los links a las listas de régimen.
   * El destino Lista_... se mantiene porque esa nota sigue
   * existiendo y está oculta en Explorer.
   */
  text = text.replace(
    /\[\[([^\]]*Lista_Captura_Materializacion)(?:\|[^\]]*)?\]\]/g,
    "[[$1|Capture and Materialization]]",
  )

  text = text.replace(
    /\[\[([^\]]*Lista_Intervenci[oó]n_F[ií]sica)(?:\|[^\]]*)?\]\]/gi,
    "[[$1|Direct Material Intervention]]",
  )

  text = text.replace(
    /\[\[([^\]]*Lista_Traduccion_Sistemas_Representacion)(?:\|[^\]]*)?\]\]/g,
    "[[$1|Translation Between Representation Systems]]",
  )

  text = text.replace(
    /\[\[([^\]]*Lista_Transformacion_Algoritmica)(?:\|[^\]]*)?\]\]/g,
    "[[$1|Algorithmic Transformation]]",
  )

  if (text !== original) {
    fs.writeFileSync(file, text, "utf8")
  }
}

/*
 * Ahora renombramos SOLO las carpetas de la copia EN.
 */

function renameDir(oldPath, newPath) {
  if (!fs.existsSync(oldPath)) return

  fs.mkdirSync(path.dirname(newPath), {
    recursive: true,
  })

  if (fs.existsSync(newPath)) {
    console.error("ERROR: ya existe:", newPath)
    process.exit(1)
  }

  fs.renameSync(oldPath, newPath)

  console.log(
    "  " +
    path.basename(oldPath) +
    " -> " +
    path.basename(newPath)
  )
}

/*
 * Primero regímenes, después carpetas principales.
 */

const operationsES =
  path.join(rootPath, "01_OPERACIONES")

if (fs.existsSync(operationsES)) {
  renameDir(
    path.join(
      operationsES,
      "Captura_Materializacion",
    ),
    path.join(
      operationsES,
      "Capture and Materialization",
    ),
  )

  renameDir(
    path.join(
      operationsES,
      "Intervencion_Fisica",
    ),
    path.join(
      operationsES,
      "Direct Material Intervention",
    ),
  )

  renameDir(
    path.join(
      operationsES,
      "Traduccion_Sistemas_Representación",
    ),
    path.join(
      operationsES,
      "Translation Between Representation Systems",
    ),
  )

  renameDir(
    path.join(
      operationsES,
      "Traduccion_Sistemas_Representacion",
    ),
    path.join(
      operationsES,
      "Translation Between Representation Systems",
    ),
  )

  renameDir(
    path.join(
      operationsES,
      "Transformacion_Algoritmica",
    ),
    path.join(
      operationsES,
      "Algorithmic Transformation",
    ),
  )
}

renameDir(
  path.join(rootPath, "01_OPERACIONES"),
  path.join(rootPath, "01_OPERATIONS"),
)

renameDir(
  path.join(rootPath, "02_COMBINACIONES"),
  path.join(rootPath, "02_COMBINATIONS"),
)

console.log("✓ Estructura inglesa temporal preparada.")
