#!/bin/bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

CONFIG="$ROOT/quartz.config.yaml"
ES_CONTENT="$ROOT/content"
EN_CONTENT="$ROOT/content_en"
EN_BUILD="${TMPDIR:-/tmp}/kwy-atlas-en-build"
OUT="${KWY_OUT:-$ROOT/public}"

if [ ! -f "$CONFIG" ]; then
  echo "ERROR: no existe quartz.config.yaml"
  exit 1
fi

if [ ! -d "$ES_CONTENT" ]; then
  echo "ERROR: no existe content/"
  exit 1
fi

if [ ! -d "$EN_CONTENT" ]; then
  echo "ERROR: no existe content_en/. Ejecuta primero translate_atlas.py."
  exit 1
fi

if ! find "$EN_CONTENT" -name "*.md" -print -quit | grep -q .; then
  echo "ERROR: content_en/ no contiene Markdown."
  exit 1
fi

BACKUP="$(mktemp)"
cp "$CONFIG" "$BACKUP"

cleanup() {
  cp "$BACKUP" "$CONFIG" 2>/dev/null || true
  rm -f "$BACKUP"
  rm -rf "$EN_BUILD"
}
trap cleanup EXIT

patch_config() {
  local locale="$1"
  local baseurl="$2"
  local page_title="$3"

  python3 - "$locale" "$baseurl" "$page_title" <<'PY'
from pathlib import Path
import re
import sys

locale, baseurl, page_title = sys.argv[1], sys.argv[2], sys.argv[3]
p = Path("quartz.config.yaml")
s = p.read_text(encoding="utf-8")

def replace_once(pattern, replacement, label):
    global s
    s2, n = re.subn(pattern, replacement, s, count=1, flags=re.M)
    if n != 1:
        raise SystemExit(f"ERROR: no pude modificar {label} en quartz.config.yaml")
    s = s2

replace_once(r"^(\s*locale:\s*).*$", lambda m: m.group(1) + locale, "locale")
replace_once(r"^(\s*baseUrl:\s*).*$", lambda m: m.group(1) + baseurl, "baseUrl")
replace_once(r"^(\s*pageTitle:\s*).*$", lambda m: m.group(1) + page_title, "pageTitle")

p.write_text(s, encoding="utf-8")
PY
}

echo "1. Construyendo Atlas ES..."
patch_config "es-ES" "kwespy.github.io/atlas-operativo" "Atlas Operativo"
KWY_LANG=es node quartz/bootstrap-cli.mjs build -d content -o "$OUT"

echo
echo "2. Preparando fuente EN con los mismos assets..."
rm -rf "$EN_BUILD"
rsync -a "$ES_CONTENT/" "$EN_BUILD/"
find "$EN_BUILD" -type f -name "*.md" -delete
rsync -a "$EN_CONTENT/" "$EN_BUILD/"

echo "   Localizando nombres visibles EN..."
node scripts/localize-en-display.mjs "$EN_BUILD"

echo
echo "3. Construyendo Atlas EN..."
patch_config "en-US" "kwespy.github.io/atlas-operativo/en" "Operational Atlas"
KWY_LANG=en node quartz/bootstrap-cli.mjs build -d "$EN_BUILD" -o "$OUT/en"

echo
echo "4. Restaurando configuración..."
cp "$BACKUP" "$CONFIG"
rm -f "$BACKUP"
BACKUP=""

echo
echo "5. Añadiendo hreflang + selección automática por navegador..."

python3 <<'PY'
from pathlib import Path
import os
import html as html_lib
import json

PUBLIC = Path(os.environ.get("KWY_OUT", "public"))
SITE = "https://kwespy.github.io"
BASE = "/atlas-operativo"

def url_for(relative_html: Path, lang_prefix=""):
    rel = relative_html.as_posix()

    if rel == "index.html":
        suffix = ""
    elif rel.endswith("/index.html"):
        suffix = rel[:-len("index.html")]
    elif rel.endswith(".html"):
        suffix = rel[:-5]
    else:
        suffix = rel

    prefix = BASE + ("/en" if lang_prefix == "en" else "")
    if suffix:
        if not suffix.startswith("/"):
            suffix = "/" + suffix
        return SITE + prefix + suffix
    return SITE + prefix + "/"

def inject_before_head_close(text, block):
    if "</head>" in text:
        return text.replace("</head>", block + "\n</head>", 1)
    return block + "\n" + text

for es_file in PUBLIC.rglob("*.html"):
    rel = es_file.relative_to(PUBLIC)

    if rel.parts and rel.parts[0] == "en":
        continue
    if es_file.name == "404.html":
        continue

    en_file = PUBLIC / "en" / rel
    if not en_file.exists():
        continue

    es_url = url_for(rel)
    en_url = url_for(rel, "en")

    alternates = (
        f'<link rel="alternate" hreflang="es" href="{html_lib.escape(es_url)}">\n'
        f'<link rel="alternate" hreflang="en" href="{html_lib.escape(en_url)}">\n'
        f'<link rel="alternate" hreflang="x-default" href="{html_lib.escape(en_url)}">'
    )

    router = f"""<script data-kwy-language-router>
(function () {{
  try {{
    var ua = navigator.userAgent || "";
    if (/bot|crawler|spider|slurp|bingpreview|facebookexternalhit/i.test(ua)) return;

    var langs = (Array.isArray(navigator.languages) && navigator.languages.length)
      ? navigator.languages
      : [navigator.language || "en"];

    var spanish = langs.some(function (lang) {{
      return String(lang).toLowerCase().indexOf("es") === 0;
    }});

    if (!spanish) {{
      window.location.replace({json.dumps(en_url)} + window.location.search + window.location.hash);
    }}
  }} catch (e) {{}}
}})();
</script>"""

    text = es_file.read_text(encoding="utf-8")
    text = inject_before_head_close(text, alternates + "\n" + router)
    es_file.write_text(text, encoding="utf-8")

for en_file in (PUBLIC / "en").rglob("*.html"):
    rel = en_file.relative_to(PUBLIC / "en")
    es_file = PUBLIC / rel

    if not es_file.exists() or en_file.name == "404.html":
        continue

    es_url = url_for(rel)
    en_url = url_for(rel, "en")

    alternates = (
        f'<link rel="alternate" hreflang="es" href="{html_lib.escape(es_url)}">\n'
        f'<link rel="alternate" hreflang="en" href="{html_lib.escape(en_url)}">\n'
        f'<link rel="alternate" hreflang="x-default" href="{html_lib.escape(en_url)}">'
    )

    text = en_file.read_text(encoding="utf-8")
    text = inject_before_head_close(text, alternates)
    en_file.write_text(text, encoding="utf-8")

print("✓ Router e hreflang añadidos.")
PY

rm -rf "$EN_BUILD"
trap - EXIT

echo
echo "✓ Atlas bilingüe construido correctamente."
echo "ES: https://kwespy.github.io/atlas-operativo/"
echo "EN: https://kwespy.github.io/atlas-operativo/en/"
