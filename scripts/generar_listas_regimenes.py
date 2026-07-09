#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
BASE = CONTENT / "01_OPERACIONES"

REGIMENES = {
    "Captura_Materializacion": {
        "titulo": "Captura y Materialización",
        "archivo_lista": "Lista_Captura_Materializacion.md",
        "titulo_lista": "Lista Captura Materialización",
    },
    "Intervencion_Fisica": {
        "titulo": "Intervención Física",
        "archivo_lista": "Lista_Intervencion_Fisica.md",
        "titulo_lista": "Lista Intervención Física",
    },
    "Traduccion_Sistemas_Representación": {
        "titulo": "Traducción de Sistemas de Representación",
        "archivo_lista": "Lista_Traduccion_Sistemas_Representación.md",
        "titulo_lista": "Lista Traducción Sistemas Representación",
    },
    "Transformacion_Algoritmica": {
        "titulo": "Transformación Algorítmica",
        "archivo_lista": "Lista_Transformacion_Algoritmica.md",
        "titulo_lista": "Lista Transformación Algorítmica",
    },
}


def numero_operacion(path):
    match = re.search(r"OB[_ -]?(\d+)", path.stem, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return 9999


def buscar_fichas(carpeta):
    fichas = []

    for archivo in carpeta.rglob("*.md"):
        if archivo.name.startswith("."):
            continue

        if archivo.name.startswith("Lista_"):
            continue

        if archivo.name == "index.md":
            continue

        if not any("_FICHA" in parte for parte in archivo.parts):
            continue

        if not archivo.stem.startswith("OB_"):
            continue

        fichas.append(archivo)

    return sorted(fichas, key=lambda p: (numero_operacion(p), p.stem.lower()))


def wikilink(archivo, carpeta):
    ruta_relativa = archivo.relative_to(carpeta).with_suffix("").as_posix()
    titulo = archivo.stem
    return f"- [[{ruta_relativa}|{titulo}]]"


def generar_lista(fichas, carpeta):
    if not fichas:
        return "_No se encontraron operaciones en este régimen._"

    return "\n".join(wikilink(ficha, carpeta) for ficha in fichas)


def escribir_regimen(nombre_carpeta, config):
    carpeta = BASE / nombre_carpeta

    if not carpeta.exists():
        print(f"NO EXISTE: {carpeta}")
        return

    fichas = buscar_fichas(carpeta)
    lista = generar_lista(fichas, carpeta)

    archivo_lista = carpeta / config["archivo_lista"]
    archivo_index = carpeta / "index.md"

    contenido_lista = f"""---
title: {config["titulo_lista"]}
---

# {config["titulo_lista"]}

{lista}
"""

    contenido_index = f"""---
title: {config["titulo"]}
---

# {config["titulo"]}

{lista}
"""

    archivo_lista.write_text(contenido_lista, encoding="utf-8")
    archivo_index.write_text(contenido_index, encoding="utf-8")

    print(f"OK: {config['titulo']}")
    print(f"   {len(fichas)} operaciones encontradas")
    print(f"   actualizado: {archivo_lista.relative_to(ROOT)}")
    print(f"   actualizado: {archivo_index.relative_to(ROOT)}")


def main():
    for nombre_carpeta, config in REGIMENES.items():
        escribir_regimen(nombre_carpeta, config)


if __name__ == "__main__":
    main()
