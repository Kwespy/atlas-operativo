#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import unquote, quote
import re
import shutil
import sys

source = Path(sys.argv[1]).resolve()
dest = Path(sys.argv[2]).resolve()
ignored = {".venv", "venv", "__pycache__", ".git", ".obsidian", "node_modules"}

def skip(path):
    return any(part in ignored for part in path.parts)

def external(ref):
    r = ref.strip().lower()
    return r.startswith(("http://", "https://", "data:", "mailto:", "/"))

def resolve(ref, note):
    ref = unquote(ref.strip()).split("#", 1)[0].strip()
    if not ref or external(ref):
        return None

    direct = (note.parent / ref).resolve()
    try:
        direct.relative_to(source)
        if direct.is_file() and not skip(direct):
            return direct
    except ValueError:
        pass

    parts = note.relative_to(source).parts
    combo_root = source / parts[0] if parts else source
    name = Path(ref).name

    if not Path(name).suffix:
        matches = [
            p for p in combo_root.rglob("*")
            if p.is_file() and not skip(p)
            and p.stem.lower() == name.lower()
            and p.suffix.lower() != ".md"
        ]
    else:
        matches = [
            p for p in combo_root.rglob("*")
            if p.is_file() and not skip(p)
            and p.name.lower() == name.lower()
        ]

    if len(matches) == 1:
        return matches[0]

    matches = [
        p for p in source.rglob("*")
        if p.is_file() and not skip(p)
        and p.name.lower() == name.lower()
    ]
    return matches[0] if len(matches) == 1 else None

copied = set()
warnings = []

def copy_asset(path):
    rel = path.relative_to(source)
    out = dest / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    if rel.as_posix() not in copied:
        shutil.copy2(path, out)
        copied.add(rel.as_posix())
    return rel

def wiki(match, note):
    ref = match.group(1)
    alias = match.group(2) or ""
    path = resolve(ref, note)
    if path is None:
        if not external(ref):
            warnings.append((ref, note))
        return match.group(0)
    if path.suffix.lower() == ".md":
        return match.group(0)
    return f"![[{copy_asset(path).as_posix()}{alias}]]"

def markdown(match, note):
    alt = match.group(1)
    ref = match.group(2).strip()
    path = resolve(ref, note)
    if path is None:
        if not external(ref):
            warnings.append((ref, note))
        return match.group(0)
    if path.suffix.lower() == ".md":
        return match.group(0)
    rel = quote(copy_asset(path).as_posix(), safe="/")
    return f"![{alt}]({rel})"

if not source.exists():
    print("02_COMBINACIONES no existe; se omite.")
    raise SystemExit(0)

dest.mkdir(parents=True, exist_ok=True)
notes = sorted(p for p in source.rglob("*.md") if not skip(p))

for note in notes:
    text = note.read_text(encoding="utf-8")
    text = re.sub(r'!\[\[([^\]|]+)(\|[^\]]+)?\]\]', lambda m: wiki(m, note), text)
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', lambda m: markdown(m, note), text)

    out = dest / note.name
    if out.exists():
        prefix = note.relative_to(source).parts[0]
        out = dest / f"{prefix}_{note.name}"
    out.write_text(text, encoding="utf-8")

for ref, note in warnings:
    print(f"ADVERTENCIA combinación: no resuelto: {ref} <- {note}")

print(f"Notas de combinaciones: {len(notes)}")
print(f"Assets de combinaciones: {len(copied)}")
