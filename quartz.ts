import {
  loadQuartzConfig,
  loadQuartzLayout,
} from "./quartz/plugins/loader/config-loader"

import * as ExternalPlugin from "./.quartz/plugins"

type ExplorerNode = {
  slugSegment?: string
  slugSegments?: string[]
  displayName?: string
  isFolder: boolean
  data: Record<string, unknown> | null
  children: ExplorerNode[]
}

ExternalPlugin.Explorer({
  filterFn: (node: ExplorerNode) => {
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

    // Ocultar carpetas internas OB_001..., OB_002...
    if (
      node.isFolder &&
      /^OB[_\-\s]?\d+/i.test(displayName)
    ) {
      return false
    }

    // Ocultar notas Lista_...
    if (
      !node.isFolder &&
      (
        /^Lista(?:[_\-\s]|$)/i.test(displayName) ||
        /^Lista(?:[_\-\s]|$)/i.test(finalSlug)
      )
    ) {
      return false
    }

    return true
  },

  order: ["filter", "map", "sort"],
})

const config = await loadQuartzConfig()

export default config

export const layout = await loadQuartzLayout()
