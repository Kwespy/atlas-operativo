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

echo "1. Desactivando Tag Index..."

python3 - "$QUARTZ/quartz.config.ts" <<'PY'
from pathlib import Path
import re
import sys

archivo = Path(sys.argv[1])

if archivo.exists():
    texto = archivo.read_text(encoding="utf-8")

    texto_nuevo = re.sub(
        r'(?m)^[ \t]*Plugin\.TagPage\([^\n]*\),?[ \t]*\n?',
        '',
        texto
    )

    archivo.write_text(texto_nuevo, encoding="utf-8")
    print("Tag Index desactivado.")
PY

rm -rf "$PUBLICO/Tag Index"
rm -rf "$QUARTZ/content/Tag Index"
rm -rf "$QUARTZ/public/tags"
rm -rf "$QUARTZ/public/Tag Index"

echo "2. Sincronizando operaciones..."

mkdir -p "$PUBLICO/01_OPERACIONES"

rsync "${RSYNC_OPTS[@]}" \
  "$ORIGEN/01_OPERACIONES/" \
  "$PUBLICO/01_OPERACIONES/"

echo "3. Preparando combinaciones sin subcarpetas visibles..."

rm -rf "$PUBLICO/02_COMBINACIONES"
mkdir -p "$PUBLICO/02_COMBINACIONES"

python3 - \
  "$ORIGEN/02_COMBINACIONES" \
  "$PUBLICO/02_COMBINACIONES" <<'PY'
from pathlib import Path
from urllib.parse import unquote, quote
import re
import shutil
import sys

origen = Path(sys.argv[1])
destino = Path(sys.argv[2])

ignoradas = {
    ".venv",
    "venv",
    "__pycache__",
    ".git",
    ".obsidian",
    "node_modules",
}

if not origen.exists():
    print("No existe la carpeta 02_COMBINACIONES.")
    raise SystemExit(0)

destino.mkdir(parents=True, exist_ok=True)


def ignorar(ruta):
    return any(parte in ignoradas for parte in ruta.parts)


# Copiar imágenes y otros archivos conservando su ruta.
# No se copian las notas dentro de las subcarpetas.
for archivo in origen.rglob("*"):
    if not archivo.is_file():
        continue

    if ignorar(archivo):
        continue

    if archivo.name == ".DS_Store":
        continue

    if archivo.suffix.lower() == ".md":
        continue

    relativa = archivo.relative_to(origen)
    salida = destino / relativa

    salida.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(archivo, salida)


def localizar_archivo(referencia, nota):
    referencia = unquote(referencia.strip())

    if not referencia:
        return None

    if referencia.startswith(("http://", "https://", "/")):
        return None

    referencia = referencia.split("#", 1)[0]

    candidato = (nota.parent / referencia).resolve()

    try:
        candidato.relative_to(origen.resolve())

        if candidato.exists() and candidato.is_file():
            return candidato
    except ValueError:
        pass

    nombre = Path(referencia).name

    coincidencias = [
        archivo
        for archivo in origen.rglob(nombre)
        if archivo.is_file() and not ignorar(archivo)
    ]

    if coincidencias:
        return coincidencias[0]

    return None


def corregir_wikilink(match, nota):
    referencia = match.group(1)
    alias = match.group(2) or ""

    archivo = localizar_archivo(referencia, nota)

    if archivo is None or archivo.suffix.lower() == ".md":
        return match.group(0)

    nueva_ruta = archivo.relative_to(origen).as_posix()

    return f"![[{nueva_ruta}{alias}]]"


def corregir_markdown(match, nota):
    texto_alternativo = match.group(1)
    referencia = match.group(2).strip()

    archivo = localizar_archivo(referencia, nota)

    if archivo is None or archivo.suffix.lower() == ".md":
        return match.group(0)

    nueva_ruta = archivo.relative_to(origen).as_posix()
    nueva_ruta = quote(nueva_ruta, safe="/")

    return f"![{texto_alternativo}]({nueva_ruta})"


notas = [
    nota
    for nota in origen.rglob("*.md")
    if not ignorar(nota)
]

for nota in notas:
    texto = nota.read_text(encoding="utf-8")

    texto = re.sub(
        r'!\[\[([^\]|]+)(\|[^\]]+)?\]\]',
        lambda match: corregir_wikilink(match, nota),
        texto
    )

    texto = re.sub(
        r'!\[([^\]]*)\]\(([^)]+)\)',
        lambda match: corregir_markdown(match, nota),
        texto
    )

    salida = destino / nota.name

    if salida.exists():
        nombre_combinacion = nota.relative_to(origen).parts[0]
        salida = destino / f"{nombre_combinacion}_{nota.name}"

    salida.write_text(texto, encoding="utf-8")

    print(f"Nota publicada: {salida.name}")

print("Combinaciones preparadas sin subcarpetas de notas.")
PY

echo "4. Sincronizando inputs..."

if [ -d "$ORIGEN/04_INPUTS" ]; then
  mkdir -p "$PUBLICO/04_INPUTS"

  rsync "${RSYNC_OPTS[@]}" \
    "$ORIGEN/04_INPUTS/" \
    "$PUBLICO/04_INPUTS/"
fi

echo "5. Limpiando archivos auxiliares..."

find "$PUBLICO" \
  -type d \( -name ".venv" -o -name "venv" -o -name "__pycache__" \) \
  -prune -exec rm -rf {} +

find "$PUBLICO" -name ".DS_Store" -delete
find "$PUBLICO" -name "*.pyc" -delete

echo "6. Copiando hacia Quartz/content..."

mkdir -p "$QUARTZ/content"

rsync "${RSYNC_OPTS[@]}" \
  "$PUBLICO/" \
  "$QUARTZ/content/"

rm -rf "$QUARTZ/content 2"
rm -rf "$QUARTZ/content/Tag Index"

echo "7. Generando índices..."

cd "$QUARTZ"

node scripts/generate-notas-directas.mjs
node scripts/generate-listas-regimenes.mjs
node scripts/generate-operaciones.mjs

echo "8. Construyendo la web..."

npx quartz build

echo ""
echo "Atlas sincronizado correctamente."
echo "Las combinaciones aparecen como notas directas."
echo "Las carpetas FICHA, PROCESO y Materiales no aparecerán."
echo "Tag Index fue eliminado."
