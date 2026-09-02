#!/usr/bin/env python3
"""
KWY — Atlas Operativo
Traducción automática ES -> EN usando Gemini API Free Tier.

Entrada:
    content/

Salida:
    content_en/

Caché:
    scripts/atlas-gemini-translation-cache.json

Características:
- No modifica ATLAS_OPERATIVO.
- No modifica ATLAS_WEB_PUBLICO.
- Solo vuelve a traducir Markdown nuevo o modificado.
- Copia imágenes y assets sin alterarlos.
- Conserva destinos de wikilinks, embeds, URLs y código.
- Guarda progreso después de cada archivo para poder reanudar.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "content"
DEST = ROOT / "content_en"
CACHE_FILE = ROOT / "scripts" / "atlas-gemini-translation-cache.json"

MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.5-flash-lite")
DELAY_SECONDS = float(os.environ.get("KWY_GEMINI_DELAY", "6.5"))
PROMPT_VERSION = "kwy-atlas-gemini-v1"

PROTECTED_FRONTMATTER_KEYS = {
    "tags", "tag", "aliases", "alias", "cssclasses", "cssclass",
    "date", "created", "modified", "lastmod", "updated", "last-modified",
    "published", "publishdate", "publish", "draft", "comments",
    "permalink", "socialimage", "image", "cover", "url", "slug",
}

INSTRUCTIONS = """Translate the supplied Markdown document from Spanish into clear, natural English.

Context: this is the public website of an artistic research project called Operational Atlas.

STRICT RULES:
1. Return ONLY the translated Markdown. Do not wrap the response in a code fence and do not add commentary.
2. Preserve Markdown structure, headings, lists, tables, HTML structure, Obsidian syntax and YAML frontmatter structure.
3. Translate faithfully. Do not summarize, expand, reinterpret, explain or improve the ideas.
4. Keep every placeholder such as __KWYPROTECT_0000__ EXACTLY unchanged.
5. Keep technical identifiers unchanged: OB_001, OB019+OB023, filenames, paths, variable names and code identifiers.
6. Keep YAML keys unchanged. Translate human-readable values such as title or description unless protected.
7. Translate visible Obsidian inline property labels when appropriate:
   Estado -> Status
   Funciona -> Works
   Trabaja_en_lo -> Works_on
   Seleccion -> Selection
   Crisis -> Crisis
8. Use simple, precise international English appropriate for contemporary visual art and artistic research.
9. Preferred terminology:
   Atlas Operativo -> Operational Atlas
   Pintura Híbrida -> Hybrid Painting
   operación -> operation
   operaciones -> operations
   combinación -> combination
   combinaciones -> combinations
   Terminada -> Finished
   Pendiente -> Pending
"""

def text_hash(text: str) -> str:
    # La caché depende del contenido, no del modelo.
    # Así podemos cambiar de modelo gratuito sin volver a traducir todo.
    payload = PROMPT_VERSION + "\n" + text
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()

def load_cache() -> dict:
    if not CACHE_FILE.exists():
        return {}
    try:
        data = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}

def save_cache(cache: dict) -> None:
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = CACHE_FILE.with_suffix(".tmp")
    tmp.write_text(
        json.dumps(cache, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    tmp.replace(CACHE_FILE)

def protect_markdown(text: str):
    protected: list[str] = []

    def protect(fragment: str) -> str:
        token = f"__KWYPROTECT_{len(protected):04d}__"
        protected.append(fragment)
        return token

    # Fenced code blocks.
    text = re.sub(
        r"(?ms)^(```|~~~)[^\n]*\n.*?^\1[ \t]*$",
        lambda m: protect(m.group(0)),
        text,
    )

    # HTML comments, including automatic Index markers.
    text = re.sub(
        r"(?s)<!--.*?-->",
        lambda m: protect(m.group(0)),
        text,
    )

    # Obsidian embeds. Keep exact syntax because | can encode dimensions.
    text = re.sub(
        r"!\[\[[^\]]+\]\]",
        lambda m: protect(m.group(0)),
        text,
    )

    # Normal wikilinks:
    # protect the TARGET while allowing the visible alias to be translated.
    wikilink = re.compile(r"(?<!!)\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")

    def protect_wikilink(match):
        target = match.group(1)
        alias = match.group(2)

        target_token = protect(target)

        if alias is None:
            visible = target.split("#", 1)[0].split("/")[-1]
            visible = visible.replace("_", " ")
        else:
            visible = alias

        return f"[[{target_token}|{visible}]]"

    text = wikilink.sub(protect_wikilink, text)

    # Inline code.
    text = re.sub(
        r"`[^`\n]+`",
        lambda m: protect(m.group(0)),
        text,
    )

    # URLs. Visible Markdown link text remains translatable.
    text = re.sub(
        r"https?://[^\s<>\]\"')]+",
        lambda m: protect(m.group(0)),
        text,
    )

    # Structural frontmatter fields that should not be translated.
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            fm_end = end + 4
            fm = text[:fm_end]
            body = text[fm_end:]

            def protect_fm_line(match):
                key = match.group(1).lower()
                if key in PROTECTED_FRONTMATTER_KEYS:
                    return protect(match.group(0))
                return match.group(0)

            fm = re.sub(
                r"(?m)^([A-Za-z][A-Za-z0-9_-]*)\s*:.*$",
                protect_fm_line,
                fm,
            )
            text = fm + body

    return text, protected

def restore_protected(text: str, protected: list[str]) -> str:
    for i, original in enumerate(protected):
        token = f"__KWYPROTECT_{i:04d}__"
        if token not in text:
            raise ValueError(f"Gemini perdió el marcador protegido {token}")
        text = text.replace(token, original)
    return text

def ensure_english_lang(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            fm = text[:end]
            rest = text[end:]

            if re.search(r"(?m)^lang\s*:", fm):
                fm = re.sub(r"(?m)^lang\s*:.*$", "lang: en", fm)
            else:
                fm += "\nlang: en"

            return fm + rest

    return "---\nlang: en\n---\n\n" + text

def strip_accidental_fence(text: str) -> str:
    text = text.strip()
    match = re.match(
        r"^```(?:markdown|md)?\s*\n([\s\S]*?)\n```$",
        text,
        flags=re.I,
    )
    return match.group(1).strip() if match else text

def extract_text(data: dict) -> str:
    candidates = data.get("candidates") or []
    if not candidates:
        feedback = data.get("promptFeedback")
        raise RuntimeError(
            "Gemini no devolvió candidatos."
            + (f" promptFeedback={feedback}" if feedback else "")
        )

    candidate = candidates[0]
    finish_reason = candidate.get("finishReason", "")

    if finish_reason == "MAX_TOKENS":
        raise RuntimeError("La respuesta alcanzó MAX_TOKENS.")

    content = candidate.get("content") or {}
    parts = content.get("parts") or []

    chunks = [
        part.get("text", "")
        for part in parts
        if isinstance(part, dict) and part.get("text")
    ]

    result = "".join(chunks).strip()

    if not result:
        raise RuntimeError(
            f"Gemini devolvió una respuesta sin texto. finishReason={finish_reason}"
        )

    return result

def translate_one(markdown: str) -> str:
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY no está configurada.")

    prepared, protected = protect_markdown(markdown)

    model_encoded = urllib.parse.quote(MODEL, safe="-._")
    endpoint = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model_encoded}:generateContent"
    )

    payload = {
        "system_instruction": {
            "parts": [{"text": INSTRUCTIONS}]
        },
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prepared}],
            }
        ],
        "generationConfig": {
            "temperature": 0.1,
            "maxOutputTokens": 32768,
            "thinkingConfig": {
                "thinkingLevel": "minimal"
            },
        },
    }

    encoded = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    waits = [15, 30, 60, 120, 240]
    last_error = None

    for attempt in range(len(waits) + 1):
        request = urllib.request.Request(
            endpoint,
            data=encoded,
            method="POST",
            headers={
                "x-goog-api-key": api_key,
                "Content-Type": "application/json; charset=utf-8",
            },
        )

        try:
            with urllib.request.urlopen(request, timeout=300) as response:
                data = json.loads(response.read().decode("utf-8"))

            translated = extract_text(data)
            translated = strip_accidental_fence(translated)
            translated = restore_protected(translated, protected)
            translated = ensure_english_lang(translated)
            return translated.rstrip() + "\n"

        except urllib.error.HTTPError as exc:
            try:
                details = exc.read().decode("utf-8", errors="replace")
            except Exception:
                details = ""

            last_error = RuntimeError(
                f"HTTP {exc.code}: {details[:1000]}"
            )

            # 429 = free-tier rate limit. Wait and retry.
            if exc.code == 429 and attempt < len(waits):
                retry_after = exc.headers.get("Retry-After")
                try:
                    wait = max(float(retry_after), waits[attempt]) if retry_after else waits[attempt]
                except Exception:
                    wait = waits[attempt]

                print(
                    f"  Límite temporal de Gemini (429). "
                    f"Esperando {int(wait)} s...",
                    file=sys.stderr,
                )
                time.sleep(wait)
                continue

            # Retry temporary server errors.
            if exc.code in {500, 502, 503, 504} and attempt < len(waits):
                wait = waits[attempt]
                print(
                    f"  Error temporal {exc.code}. Esperando {wait} s...",
                    file=sys.stderr,
                )
                time.sleep(wait)
                continue

            break

        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
            if attempt < len(waits):
                wait = waits[attempt]
                print(
                    f"  Error temporal de red. Esperando {wait} s...",
                    file=sys.stderr,
                )
                time.sleep(wait)
                continue
            break

        except Exception as exc:
            last_error = exc
            break

    raise RuntimeError(f"Traducción falló: {last_error}")

def copy_assets_and_collect_markdown():
    # content_en/ debe contener SOLO Markdown traducido.
    # Las imágenes/assets se reutilizan desde content/ durante el build.
    md_files = []
    expected = set()

    for src in sorted(SOURCE.rglob("*")):
        if src.is_dir() or src.suffix.lower() != ".md":
            continue

        rel = src.relative_to(SOURCE)
        expected.add(rel)

        dst = DEST / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        md_files.append((src, dst, rel))

    return md_files, expected

def remove_stale(expected):
    if not DEST.exists():
        return

    for item in sorted(DEST.rglob("*"), reverse=True):
        rel = item.relative_to(DEST)

        if item.is_file() and rel not in expected:
            item.unlink()
        elif item.is_dir():
            try:
                item.rmdir()
            except OSError:
                pass

def main():
    if not SOURCE.exists():
        raise SystemExit(f"ERROR: no existe la carpeta fuente: {SOURCE}")

    if not os.environ.get("GEMINI_API_KEY", "").strip():
        raise SystemExit("ERROR: GEMINI_API_KEY no está disponible.")

    DEST.mkdir(parents=True, exist_ok=True)
    cache = load_cache()

    md_files, expected = copy_assets_and_collect_markdown()

    unchanged = []
    pending = []

    for src, dst, rel in md_files:
        original = src.read_text(encoding="utf-8")
        h = text_hash(original)
        key = rel.as_posix()

        if cache.get(key) == h and dst.exists():
            unchanged.append((key, h))
        else:
            pending.append((src, dst, rel, original, h))

    print(f"Markdown total: {len(md_files)}")
    print(f"Sin cambios: {len(unchanged)}")
    print(f"Para traducir: {len(pending)}")
    print(f"Modelo: {MODEL}")
    print("Modo: Gemini Free Tier / secuencial")
    print()

    new_cache = {key: h for key, h in unchanged}

    for number, (src, dst, rel, original, h) in enumerate(pending, start=1):
        key = rel.as_posix()
        print(f"[{number}/{len(pending)}] Traduciendo: {key}")

        try:
            translated = translate_one(original)
        except Exception as exc:
            save_cache(new_cache)
            raise SystemExit(
                f"\nERROR traduciendo {key}:\n{exc}\n\n"
                "El progreso anterior quedó guardado. "
                "Puedes ejecutar el script otra vez para continuar."
            ) from exc

        dst.write_text(translated, encoding="utf-8")
        new_cache[key] = h
        save_cache(new_cache)

        print("  ✓ listo")

        if number < len(pending):
            time.sleep(DELAY_SECONDS)

    remove_stale(expected)
    save_cache(new_cache)

    print()
    print("Traducción inglesa actualizada correctamente.")
    print(f"Archivos reutilizados desde caché: {len(unchanged)}")
    print(f"Archivos traducidos ahora: {len(pending)}")
    print(f"ES: {SOURCE}")
    print(f"EN: {DEST}")

if __name__ == "__main__":
    main()
