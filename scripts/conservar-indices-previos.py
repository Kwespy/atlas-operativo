#!/usr/bin/env python3
"""Incorpora entradas nuevas a los índices sin reescribir las antiguas."""

from pathlib import Path
import re
import subprocess
import sys

if len(sys.argv) != 3 or sys.argv[1] not in {"es", "en"}:
    raise SystemExit("Uso: conservar-indices-previos.py es|en MANIFEST_IDS")

language = sys.argv[1]
ids = set(Path(sys.argv[2]).read_text(encoding="utf-8").splitlines())
root = Path(__file__).resolve().parent.parent
content = root / ("content_en" if language == "en" else "content")


def committed(relative: Path) -> str:
    result = subprocess.run(
        ["git", "show", f"HEAD:{relative.as_posix()}"],
        cwd=root, check=True, capture_output=True, text=True,
    )
    return result.stdout


def entries(text: str) -> dict[str, str]:
    found = {}
    lines = text.splitlines(keepends=True)
    for index, line in enumerate(lines):
        if not line.startswith("- [["):
            continue
        match = re.search(r"OB_(\d{3})(?!\d)", line)
        if not match or match.group(1) not in ids:
            continue
        end = index + 1
        while end < len(lines) and lines[end].startswith("  "):
            end += 1
        number = match.group(1)
        if number in found:
            raise SystemExit(f"ERROR: OB_{number} duplicada en un índice")
        found[number] = "".join(lines[index:end]).rstrip() + "\n"
    return found


regime_headings = {
    "es": {
        "Captura_Materializacion": "Captura Materializacion",
        "Intervencion_Fisica": "Intervencion Fisica",
        "Traduccion_Sistemas_Representación": "Traduccion Sistemas Representación",
        "Transformacion_Algoritmica": "Transformacion Algoritmica",
    },
    "en": {
        "Captura_Materializacion": "Capture Materialization",
        "Intervencion_Fisica": "Physical Intervention",
        "Traduccion_Sistemas_Representación": "Representation Systems Translation",
        "Transformacion_Algoritmica": "Algorithmic Transformation",
    },
}

index_path = content / "Index.md"
new_entries = entries(index_path.read_text(encoding="utf-8"))
if set(new_entries) != ids:
    missing = ", ".join(sorted(ids - set(new_entries)))
    raise SystemExit(f"ERROR: faltan en el índice las operaciones: {missing}")

base = committed(Path(content.name) / "Index.md")
for regime, heading in regime_headings[language].items():
    selected = [
        new_entries[number] for number in sorted(ids)
        if f"/{regime}/" in new_entries[number]
    ]
    if not selected:
        continue
    section = re.search(
        rf"(?ms)^### {re.escape(heading)}\n(.*?)(?=^### |^<!-- OPERACIONES_AUTO_END -->)",
        base,
    )
    if not section:
        raise SystemExit(f"ERROR: falta el régimen {heading} en {index_path}")
    body = section.group(1).rstrip() + "\n\n" + "\n".join(selected) + "\n"
    base = base[:section.start(1)] + body + base[section.end(1):]

index_path.write_text(base, encoding="utf-8")
print(f"Índice {language.upper()}: {len(new_entries)} operaciones nuevas añadidas")

if language == "en":
    for regime in regime_headings[language]:
        directory = content / "01_OPERACIONES" / regime
        if not directory.is_dir():
            continue
        for list_path in directory.glob("Lista_*.md"):
            candidate = entries(list_path.read_text(encoding="utf-8"))
            if not candidate:
                continue
            relative = list_path.relative_to(root)
            original = committed(relative)
            marker = "<!-- AUTO-LISTA-REGIMEN:END -->"
            if marker not in original:
                raise SystemExit(f"ERROR: falta marcador en {list_path}")
            addition = "".join(candidate[number] for number in sorted(candidate))
            list_path.write_text(original.replace(marker, addition + marker, 1), encoding="utf-8")
            print(f"Lista inglesa actualizada: {list_path.name}")
