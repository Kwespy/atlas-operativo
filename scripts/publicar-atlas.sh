#!/bin/bash
set -euo pipefail

BASE="/Users/kwy/Library/Mobile Documents/iCloud~md~obsidian/Documents"
MASTER="$BASE/ATLAS_OPERATIVO"
QUARTZ="$BASE/ATLAS_WEB_QUARTZ"
TMPROOT="$(mktemp -d /tmp/kwy-atlas-publish.XXXXXX)"
STAGING="$TMPROOT/staging"
IMG_CACHE="$TMPROOT/image-cache"
BUILD="$TMPROOT/site"

cleanup() {
  rc=$?
  if [ "$rc" -eq 0 ]; then
    rm -rf "$TMPROOT"
  else
    echo ""
    echo "ERROR: publicación detenida. Temporal conservado en:"
    echo "  $TMPROOT"
  fi
}
trap cleanup EXIT

export PATH="/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin:/usr/local/bin:${PATH:-}"

[ "$MASTER" = "$BASE/ATLAS_OPERATIVO" ] || exit 1
[ "$QUARTZ" = "$BASE/ATLAS_WEB_QUARTZ" ] || exit 1
[ -d "$MASTER" ] || { echo "ERROR: falta ATLAS_OPERATIVO"; exit 1; }
[ -d "$QUARTZ/.git" ] || { echo "ERROR: falta repo Quartz"; exit 1; }

cd "$QUARTZ"

[ "$(git branch --show-current)" = "v5" ] || { echo "ERROR: branch no es v5"; exit 1; }

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
if command -v nvm >/dev/null 2>&1; then
  nvm use 22.16.0 >/dev/null
fi
[ "$(node -p 'process.versions.node')" = "22.16.0" ] || { echo "ERROR: se requiere Node 22.16.0"; exit 1; }

if [ ! -d node_modules ]; then
  echo "[1/8] Instalando dependencias..."
  npm ci
else
  echo "[1/8] Dependencias listas."
fi

if [ ! -d .quartz ]; then
  echo "[2/8] Instalando plugins Quartz..."
  node quartz/bootstrap-cli.mjs plugin install --concurrency 4
else
  echo "[2/8] Plugins Quartz listos."
fi

if [ -z "${GEMINI_API_KEY:-}" ]; then
  GEMINI_API_KEY="$(security find-generic-password -a "$USER" -s "KWY_GEMINI_API_KEY" -w 2>/dev/null || true)"
  export GEMINI_API_KEY
fi
[ -n "${GEMINI_API_KEY:-}" ] || { echo "ERROR: falta GEMINI_API_KEY en Keychain"; exit 1; }

echo "[3/8] Seleccionando Markdown + assets referenciados..."
mkdir -p "$STAGING/01_OPERACIONES" "$IMG_CACHE"

rsync -a \
  --exclude=".venv/" \
  --exclude="venv/" \
  --exclude="__pycache__/" \
  --exclude=".git/" \
  --exclude=".obsidian/" \
  --exclude="node_modules/" \
  --include="*/" \
  --include="*.md" \
  --exclude="*" \
  "$MASTER/01_OPERACIONES/" \
  "$STAGING/01_OPERACIONES/"

python3 scripts/copiar-assets-fichas.py "$MASTER" "$STAGING"
python3 scripts/preparar-combinaciones.py \
  "$MASTER/02_COMBINACIONES" \
  "$STAGING/02_COMBINACIONES"

find "$STAGING" -name ".DS_Store" -delete
find "$STAGING" -name "*.pyc" -delete

echo "[4/8] Convirtiendo imágenes seleccionadas a WebP..."
node scripts/optimizar-imagenes-web.mjs "$STAGING" "$IMG_CACHE"

RAW="$(find "$STAGING" -type f \( \
  -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o \
  -iname "*.heic" -o -iname "*.heif" -o \
  -iname "*.tif" -o -iname "*.tiff" \
\) -print -quit)"
[ -z "$RAW" ] || { echo "ERROR: raster original en staging: $RAW"; exit 1; }

echo "[5/8] Regenerando content..."
rm -rf content
mkdir -p content
rsync -a "$STAGING/" content/
cp scripts/home-index.md content/index.md

node scripts/generate-notas-directas.mjs
node scripts/generate-listas-regimenes.mjs
node scripts/generate-operaciones.mjs
python3 scripts/prune-public-assets.py

RAW="$(find content -type f \( \
  -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o \
  -iname "*.heic" -o -iname "*.heif" -o \
  -iname "*.tif" -o -iname "*.tiff" \
\) -print -quit)"
[ -z "$RAW" ] || { echo "ERROR: raster original llegó a content: $RAW"; exit 1; }

echo "[6/8] Traduciendo ES → EN..."
rm -rf content_en
python3 scripts/translate_atlas.py

ES_MD="$(find content -type f -name "*.md" | wc -l | tr -d " ")"
EN_MD="$(find content_en -type f -name "*.md" | wc -l | tr -d " ")"
EN_ASSETS="$(find content_en -type f ! -name "*.md" | wc -l | tr -d " ")"

[ "$ES_MD" -gt 0 ] || { echo "ERROR: content sin Markdown"; exit 1; }
[ "$ES_MD" = "$EN_MD" ] || { echo "ERROR: ES=$ES_MD EN=$EN_MD"; exit 1; }
[ "$EN_ASSETS" = "0" ] || { echo "ERROR: content_en contiene assets"; exit 1; }

echo "[7/8] Construyendo ES + EN..."
KWY_OUT="$BUILD" bash scripts/build-bilingual-site.sh

ES_HTML="$(find "$BUILD" -path "$BUILD/en" -prune -o -type f -name "*.html" -print | wc -l | tr -d " ")"
EN_HTML="$(find "$BUILD/en" -type f -name "*.html" | wc -l | tr -d " ")"

[ "$ES_HTML" -gt 0 ] || { echo "ERROR: build ES vacío"; exit 1; }
[ "$ES_HTML" = "$EN_HTML" ] || { echo "ERROR: HTML ES=$ES_HTML EN=$EN_HTML"; exit 1; }

grep -q "pageTitle: Atlas Operativo" quartz.config.yaml
grep -q "locale: es-ES" quartz.config.yaml
grep -q "baseUrl: kwespy.github.io/atlas-operativo" quartz.config.yaml

python3 -c 'from pathlib import Path
bad=[]
for p in Path("content").rglob("*"):
    if p.is_file() and p.stat().st_size > 95*1024*1024:
        bad.append((p, p.stat().st_size))
if bad:
    for p,n in bad:
        print(f"ERROR archivo demasiado grande para GitHub: {p} ({n/1024/1024:.1f} MB)")
    raise SystemExit(1)
'

echo "[8/8] Git + GitHub..."
git add -A -- content content_en
git add -- \
  .gitignore \
  scripts/publicar-atlas.sh \
  scripts/copiar-assets-fichas.py \
  scripts/preparar-combinaciones.py \
  scripts/optimizar-imagenes-web.mjs

BAD="$(git diff --cached --name-only --diff-filter=AM -- content | grep -Ei '\.(jpg|jpeg|png|heic|heif|tif|tiff)$' || true)"
[ -z "$BAD" ] || { echo "ERROR: raster original staged"; echo "$BAD"; exit 1; }

if ! git diff --cached --quiet; then
  git commit -m "Simplificar publicación del Atlas"
  git push origin v5
else
  echo "Git: no hay cambios nuevos."
fi

WEBP="$(find content -type f -iname "*.webp" | wc -l | tr -d " ")"
MP4="$(find content -type f -iname "*.mp4" | wc -l | tr -d " ")"

echo ""
echo "✓ PUBLICACIÓN COMPLETA"
echo "ES Markdown: $ES_MD"
echo "EN Markdown: $EN_MD"
echo "WebP: $WEBP"
echo "MP4: $MP4"
echo "HTML ES/EN: $ES_HTML / $EN_HTML"
echo "ATLAS_OPERATIVO intacto."
echo "Sin cache permanente de imágenes."
echo "https://kwespy.github.io/atlas-operativo/"
