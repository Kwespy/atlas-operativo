import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"
import * as ExternalPlugin from "./.quartz/plugins"

ExternalPlugin.Explorer({
  title: "Explorer",
  folderClickBehavior: "collapse",
  folderDefaultState: "collapsed",
  useSavedState: false,

  filterFn: (node) => {
    const parts = Array.isArray(node.slugSegments)
      ? node.slugSegments
      : []

    const operationsIndex = parts.findIndex(
      (part) =>
        String(part)
          .toLowerCase()
          .replace(/[-_\s]/g, "") === "01operaciones",
    )

    // Fuera de 01_OPERACIONES no cambiar nada
    if (operationsIndex === -1) {
      return true
    }

    const depth = parts.length - operationsIndex

    // Mostrar 01_OPERACIONES y los cuatro regímenes
    if (depth <= 2) {
      return true
    }

    // Dentro de cada régimen:
    // mostrar solo las notas directas y ocultar las carpetas OB_...
    if (depth === 3) {
      if (node.isFolder) {
        return false
      }

      const filename = String(node.slugSegment ?? "")
        .toLowerCase()
        .replace(/[-_\s]/g, "")

      // Ocultar las notas Lista_...
      if (filename.startsWith("lista")) {
        return false
      }

      return filename !== "index"
    }

    // Ocultar FICHA, PROCESO y todo el contenido interior
    return false
  },

  order: ["filter", "map", "sort"],
})

const config = await loadQuartzConfig()

export default config

export const layout = await loadQuartzLayout()
