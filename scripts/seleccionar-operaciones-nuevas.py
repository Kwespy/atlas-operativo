#!/usr/bin/env python3
"""Copia al staging solo operaciones cuyo OB_### aún no figura en Quartz."""

from pathlib import Path
import re
import sys

if len(sys.argv) != 5:
    raise SystemExit("Uso: seleccionar-operaciones-nuevas.py MASTER CONTENT STAGING MANIFEST")

master, content, staging, manifest = map(Path, sys.argv[1:])
source = master / "01_OPERACIONES"
published = content / "01_OPERACIONES"
target = staging / "01_OPERACIONES"
pattern = re.compile(r"^OB[_-]?(\d{3})(?:\D|$)", re.IGNORECASE)
ignored = {".venv", "venv", "__pycache__", ".git", ".obsidian", "node_modules"}

if not source.is_dir() or not published.is_dir():
    raise SystemExit("ERROR: faltan las carpetas de operaciones del Atlas o de Quartz")

already = set()
for path in published.rglob("*"):
    if not (path.is_dir() or path.suffix.lower() == ".md"):
        continue
    match = pattern.match(path.name)
    if match:
        already.add(match.group(1))

new = {}
for regime in sorted(p for p in source.iterdir() if p.is_dir()):
    for operation in sorted(p for p in regime.iterdir() if p.is_dir()):
        match = pattern.match(operation.name)
        if not match:
            continue
        number = match.group(1)
        if number in new:
            raise SystemExit(f"ERROR: OB_{number} aparece más de una vez en el Atlas")
        new[number] = operation

selected = {number: path for number, path in new.items() if number not in already}
for number, operation in sorted(selected.items()):
    fichas = list(operation.glob("*_FICHA/OB_*.md"))
    if len(fichas) != 1:
        raise SystemExit(f"ERROR: OB_{number} debe tener una ficha Markdown única: {operation}")
    print(f"Nueva: OB_{number} ({operation.parent.name})")

    def technical_reference(match):
        name = Path(match.group(1)).name
        if name.lower().endswith(".md"):
            internal_note = any(
                "codigo" in path.relative_to(operation).parts
                for path in operation.rglob(name)
            )
            if not internal_note:
                return match.group(0)
        return f"`{name}`"

    for note in operation.rglob("*.md"):
        if any(part in ignored for part in note.relative_to(operation).parts):
            continue
        if not any(part.endswith("_FICHA") for part in note.relative_to(operation).parts[:-1]):
            continue
        output = target / note.relative_to(source)
        output.parent.mkdir(parents=True, exist_ok=True)
        text = note.read_text(encoding="utf-8")
        text = text.replace("ATLAS_OPERATIVO/04_INPUTS/", "")
        text = re.sub(
            r"(?<!!)\[\[([^\]|]+\.(?:py|txt|md))(?:\|[^\]]+)?\]\]",
            technical_reference,
            text,
            flags=re.IGNORECASE,
        )
        output.write_text(text, encoding="utf-8")

manifest.parent.mkdir(parents=True, exist_ok=True)
manifest.write_text("".join(f"{number}\n" for number in sorted(selected)), encoding="utf-8")
print(f"Operaciones nuevas: {len(selected)}")
