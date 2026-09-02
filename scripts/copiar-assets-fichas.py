#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import unquote
import re
import shutil
import sys

if len(sys.argv) != 3:
    raise SystemExit("Uso: copiar-assets-fichas.py MASTER STAGING")

MASTER = Path(sys.argv[1]).resolve()
STAGING = Path(sys.argv[2]).resolve()
OPERACIONES = MASTER / "01_OPERACIONES"

IGNORADAS = {
    ".venv", "venv", "__pycache__", ".git",
    ".obsidian", "node_modules",
}

WIKI = re.compile(r'!\[\[([^\]]+)\]\]')
MARKDOWN = re.compile(r'!\[[^\]]*\]\(([^)]+)\)')

def ignorar(path: Path) -> bool:
    return any(part in IGNORADAS for part in path.parts)

def find_ficha(operation_dir: Path):
    ficha_dirs = sorted(
        p for p in operation_dir.iterdir()
        if p.is_dir() and "ficha" in p.name.lower()
    )
    for ficha_dir in ficha_dirs:
        notes = sorted(
            p for p in ficha_dir.glob("*.md")
            if p.is_file() and not ignorar(p)
        )
        if not notes:
            continue
        preferred = [
            p for p in notes
            if re.match(r"^OB[_-]?\d+", p.stem, re.IGNORECASE)
        ]
        return preferred[0] if preferred else notes[0]
    return None

def normalize_reference(raw: str) -> str:
    ref = unquote(raw.strip())
    if "|" in ref:
        ref = ref.split("|", 1)[0].strip()
    if "#" in ref:
        ref = ref.split("#", 1)[0].strip()
    return ref

def resolve_asset(raw: str, note: Path):
    reference = normalize_reference(raw)
    if not reference:
        return None
    low = reference.lower()
    if low.startswith(("http://", "https://", "data:", "mailto:", "/")):
        return None

    direct = (note.parent / reference).resolve()
    try:
        direct.relative_to(MASTER)
        if direct.is_file() and not ignorar(direct):
            return direct
    except ValueError:
        pass

    ref_path = Path(reference)
    operation_dir = note.parent.parent

    # Obsidian permite embeds sin extensión, por ejemplo ![[OB015_step01]].
    if not ref_path.suffix:
        stem = ref_path.name.lower()
        matches = [
            p for p in operation_dir.rglob("*")
            if p.is_file()
            and not ignorar(p)
            and p.stem.lower() == stem
            and p.suffix.lower() != ".md"
        ]
        return matches[0] if len(matches) == 1 else None

    name = ref_path.name.lower()

    # Primero: nombre exacto dentro de la misma operación.
    matches = [
        p for p in operation_dir.rglob("*")
        if p.is_file()
        and not ignorar(p)
        and p.name.lower() == name
    ]
    if len(matches) == 1:
        return matches[0]

    # Último fallback: nombre exacto y único en todo el master.
    matches = [
        p for p in MASTER.rglob("*")
        if p.is_file()
        and not ignorar(p)
        and p.name.lower() == name
    ]
    if len(matches) == 1:
        return matches[0]

    return None

if not OPERACIONES.is_dir():
    raise SystemExit(f"ERROR: no existe {OPERACIONES}")

fichas = []
for regime in sorted(p for p in OPERACIONES.iterdir() if p.is_dir() and not ignorar(p)):
    for operation in sorted(p for p in regime.iterdir() if p.is_dir() and not ignorar(p)):
        note = find_ficha(operation)
        if note:
            fichas.append(note)

copied = set()
warnings = []

for note in fichas:
    text = note.read_text(encoding="utf-8")

    refs = []
    refs.extend(m.group(1) for m in WIKI.finditer(text))
    refs.extend(m.group(1).strip() for m in MARKDOWN.finditer(text))

    for raw in refs:
        asset = resolve_asset(raw, note)
        if asset is None:
            ref = normalize_reference(raw)
            if ref and not ref.lower().startswith(("http://", "https://", "data:", "mailto:", "/")):
                warnings.append((ref, note))
            continue
        if asset.suffix.lower() == ".md":
            continue

        relative = asset.relative_to(MASTER)
        target = STAGING / relative
        target.parent.mkdir(parents=True, exist_ok=True)

        key = relative.as_posix()
        if key not in copied:
            shutil.copy2(asset, target)
            copied.add(key)

for ref, note in warnings:
    print(f"ADVERTENCIA: no resuelto: {ref} <- {note}")

print(f"Fichas analizadas: {len(fichas)}")
print(f"Assets de fichas copiados: {len(copied)}")
