#!/bin/bash

set -euo pipefail

BASE="/Users/kwy/Library/Mobile Documents/iCloud~md~obsidian/Documents"

ORIGEN="$BASE/ATLAS_OPERATIVO"
PUBLICO="$BASE/ATLAS_WEB_PUBLICO"
QUARTZ="$BASE/ATLAS_WEB_QUARTZ"

RSYNC_OPTS=(
  -av
  --delete
  --delete-excluded
  --exclude='.venv/'
  --exclude='venv/'
  --exclude='__pycache__/'
  --exclude='*.pyc'
  --exclude='.DS_Store'
  --exclude='.git/'
  --exclude='.obsidian/'
  --exclude='node_modules/'
)

echo "1. Sincronizando ATLAS_OPERATIVO hacia ATLAS_WEB_PUBLICO..."

mkdir -p "$PUBLICO/01_OPERACIONES"

# Eliminar categorías antiguas que ya no forman parte de los cuatro regímenes
rm -rf "$PUBLICO/01_OPERACIONES/Captura_Recaptura_Transferencia"
rm -rf "$PUBLICO/01_OPERACIONES/Color_Tono_Registro"
rm -rf "$PUBLICO/01_OPERACIONES/Interfaz_Maquina_Cuerpo"
rm -rf "$PUBLICO/01_OPERACIONES/Resolucion_Perdida_Interferencia"
rm -rf "$PUBLICO/01_OPERACIONES/Superposicion_Espacio_Ambigüedad_Perceptiva"

# Copiar operaciones
rsync "${RSYNC_OPTS[@]}" \
  "$ORIGEN/01_OPERACIONES/" \
  "$PUBLICO/01_OPERACIONES/"

# Copiar combinaciones cuando exista la carpeta
if [ -d "$ORIGEN/02_COMBINACIONES" ]; then
  mkdir -p "$PUBLICO/02_COMBINACIONES"
  rsync "${RSYNC_OPTS[@]}" \
    "$ORIGEN/02_COMBINACIONES/" \
    "$PUBLICO/02_COMBINACIONES/"
fi

# Copiar inputs cuando exista la carpeta
if [ -d "$ORIGEN/04_INPUTS" ]; then
  mkdir -p "$PUBLICO/04_INPUTS"
  rsync "${RSYNC_OPTS[@]}" \
    "$ORIGEN/04_INPUTS/" \
    "$PUBLICO/04_INPUTS/"
fi

echo "2. Limpiando archivos que no deben publicarse..."

find "$PUBLICO" \
  -type d \( -name ".venv" -o -name "venv" -o -name "__pycache__" \) \
  -prune -exec rm -rf {} +

find "$PUBLICO" -name ".DS_Store" -delete
find "$PUBLICO" -name "*.pyc" -delete

echo "3. Copiando ATLAS_WEB_PUBLICO hacia Quartz/content..."

mkdir -p "$QUARTZ/content"

rsync "${RSYNC_OPTS[@]}" \
  "$PUBLICO/" \
  "$QUARTZ/content/"

# Eliminar una posible copia accidental llamada “content 2”
rm -rf "$QUARTZ/content 2"

echo "4. Borrando notas auxiliares si existen..."

rm -f "$QUARTZ/content/Operaciones.md"
rm -f "$QUARTZ/content/operaciones.md"

echo "5. Generando Index automático..."

cd "$QUARTZ"
node scripts/generate-listas-regimenes.mjs
node scripts/generate-operaciones.mjs

echo "6. Construyendo sitio estático..."

npx quartz build

echo ""
echo "Listo. Sincronización terminada."
echo "Quartz no quedó abierto."
echo "Para previsualizar: npx quartz build --serve"
