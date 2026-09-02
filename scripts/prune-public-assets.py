from pathlib import Path
import re

ROOT = Path("content")

ASSET_EXTS = {
    ".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif",
    ".mp4", ".mov", ".webm", ".m4v"
}

# patrones markdown/html/wikilinks
PATTERNS = [
    re.compile(r'!\[[^\]]*\]\(([^)]+)\)'),             # ![](...)
    re.compile(r'\[[^\]]*\]\(([^)]+)\)'),              # [](...)
    re.compile(r'<img[^>]+src=["\']([^"\']+)["\']'),   # <img src="">
    re.compile(r'<video[^>]+src=["\']([^"\']+)["\']'), # <video src="">
    re.compile(r'<source[^>]+src=["\']([^"\']+)["\']') # <source src="">
]

def normalize_link(raw: str):
    raw = raw.strip()
    if not raw:
        return None

    # ignorar externas
    if raw.startswith("http://") or raw.startswith("https://") or raw.startswith("data:"):
        return None

    # sacar anchors/query
    raw = raw.split("#")[0].split("?")[0].strip()

    if not raw:
        return None

    return raw

def all_markdown_files(root: Path):
    return list(root.rglob("*.md"))

def all_assets(root: Path):
    return [
        p for p in root.rglob("*")
        if p.is_file() and p.suffix.lower() in ASSET_EXTS
    ]

def collect_referenced_assets(root: Path):
    used = set()

    for md in all_markdown_files(root):
        text = md.read_text(encoding="utf-8", errors="ignore")

        for rx in PATTERNS:
            for m in rx.findall(text):
                link = normalize_link(m)
                if not link:
                    continue

                candidate = (md.parent / link).resolve()

                try:
                    rel = candidate.relative_to(root.resolve())
                    used.add(root / rel)
                except Exception:
                    pass

        # respaldo extra: si un nombre exacto aparece en el markdown, lo cuenta
        for asset in all_assets(root):
            if asset.name in text:
                used.add(asset)

    return used

def main():
    if not ROOT.exists():
        print("ERROR: no existe content/")
        return

    assets = all_assets(ROOT)
    used = collect_referenced_assets(ROOT)

    removed = []
    kept = []

    for asset in assets:
        if asset in used:
            kept.append(asset)
        else:
            removed.append(asset)

    size_removed = sum(p.stat().st_size for p in removed) / 1024 / 1024
    size_kept = sum(p.stat().st_size for p in kept) / 1024 / 1024

    print(f"Assets totales: {len(assets)}")
    print(f"Assets usados: {len(kept)}")
    print(f"Assets a eliminar: {len(removed)}")
    print(f"Peso usado: {size_kept:.1f} MB")
    print(f"Peso a eliminar: {size_removed:.1f} MB")

    for p in removed:
        p.unlink()

    # borrar carpetas vacías
    for d in sorted(ROOT.rglob("*"), reverse=True):
        if d.is_dir():
            try:
                next(d.iterdir())
            except StopIteration:
                d.rmdir()

    print("✓ Limpieza pública completada.")
    
if __name__ == "__main__":
    main()
