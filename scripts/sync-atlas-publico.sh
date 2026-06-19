#!/bin/bash

set -e

BASE="/Users/kwy/Library/Mobile Documents/iCloud~md~obsidian/Documents"

PRIVADO="$BASE/ATLAS_OPERATIVO"
PUBLICO="$BASE/ATLAS_WEB_PUBLICO"
QUARTZ="$BASE/ATLAS_WEB_QUARTZ"

echo "1. Sincronizando desde ATLAS_OPERATIVO hacia ATLAS_WEB_PUBLICO..."

rsync -av --delete \
  --exclude=".obsidian" \
  --exclude=".DS_Store" \
  "$PRIVADO/01_OPERACIONES/" \
  "$PUBLICO/01_OPERACIONES/"

rsync -av --delete \
  --exclude=".obsidian" \
  --exclude=".DS_Store" \
  "$PRIVADO/02_COMBINACIONES/" \
  "$PUBLICO/02_COMBINACIONES/"

rsync -av --delete \
  --exclude=".obsidian" \
  --exclude=".DS_Store" \
  "$PRIVADO/04_INPUTS/" \
  "$PUBLICO/04_INPUTS/"

echo "2. Copiando ATLAS_WEB_PUBLICO hacia Quartz/content..."

cd "$QUARTZ"

rsync -av --delete \
  --exclude=".obsidian" \
  --exclude=".DS_Store" \
  "$PUBLICO/" \
  "$QUARTZ/content/"

echo "3. Borrando notas auxiliares si existen..."

rm -f "$QUARTZ/content/Operaciones.md"
rm -f "$QUARTZ/content/operaciones.md"

echo "4. Generando Index automático solo dentro de Quartz/content..."

node scripts/generate-operaciones.mjs

echo "5. Construyendo sitio estático..."

npx quartz build

echo "Listo. Sincronización terminada. Quartz NO quedó abierto."
echo "Para previsualizar: npx quartz build --serve"
