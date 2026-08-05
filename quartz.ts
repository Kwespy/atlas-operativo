import {
  loadQuartzConfig,
  loadQuartzLayout,
} from "./quartz/plugins/loader/config-loader"

import * as ExternalPlugin from "./.quartz/plugins"

ExternalPlugin.Explorer({
  filterFn: (node) => {
    const nodeWithSlug = node as typeof node & {
      slug?: string
    }

    const slug = String(
      node.data?.slug ?? nodeWithSlug.slug ?? "",
    )

    const finalSlug =
      slug.split("/").filter(Boolean).at(-1) ?? ""

    const displayName = String(
      node.displayName ?? "",
    ).trim()

    /*
     * Ocultar las carpetas originales:
     * OB_001_Fotografia_de_pantalla
     * OB_002_Perdida_de_Resolucion
     * etc.
     *
     * Al ocultar la carpeta OB, también quedan ocultas
     * automáticamente FICHA y PROCESO.
     */
    if (
      node.isFolder &&
      /^OB[_\-\s]?\d+/i.test(displayName)
    ) {
      return false
    }

    /*
     * Ocultar las notas Lista_...
     * Aunque su título visible sea distinto,
     * también revisamos el slug real.
     */
    if (
      !node.isFolder &&
      (
        /^Lista(?:[_\-\s]|$)/i.test(displayName) ||
        /^Lista(?:[_\-\s]|$)/i.test(finalSlug)
      )
    ) {
      return false
    }

    /*
     * Mantener visibles:
     * - 01_OPERACIONES
     * - los cuatro regímenes
     * - las notas directas OB_001 — ...
     * - el resto normal de la web
     */
    return true
  },

  order: ["filter", "map", "sort"],
})

const config = await loadQuartzConfig()

export default config

export const layout = await loadQuartzLayout()
