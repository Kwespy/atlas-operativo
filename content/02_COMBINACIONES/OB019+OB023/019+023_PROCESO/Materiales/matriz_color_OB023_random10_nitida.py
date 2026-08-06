from PIL import Image, ImageDraw, ImageFont, ImageOps
import numpy as np
import random
from pathlib import Path

# ==========================================
# CONFIGURACIÓN
# ==========================================

# Busca primero en el Escritorio y, si no está, prueba en la carpeta actual.
POSSIBLE_IMAGE_PATHS = [
    Path.home() / "Desktop" / "OB023_step10.png",
    Path("OB023_step10.png"),
]

# MÁS NITIDEZ REAL = más detalle interno, no solo archivo más pesado
COLS = 220                    # antes 140 -> ahora más detalle
ROWS = None                   # se calcula automáticamente según la proporción vertical/horizontal
NUM_COLORS = 156              # se mantiene como lo dejaste
CELL_SIZE = 6                 # cada celda sale más grande y nítida
NUM_VARIANTS = 14             # se mantiene como lo dejaste
SAVE_NUMBERED = True          # también guarda versiones numeradas
SEED = None                   # fija un número si quieres repetir exactamente la misma serie

# Salida
RESULT_SCALE = 1              # con CELL_SIZE=6 ya sale grande; puedes subir a 2 si quieres enorme
NUMBERED_SCALE = 1

# Compresión PNG
# OJO: en PNG el peso NO significa mejor calidad. PNG es sin pérdida.
# Aquí bajo la compresión para que pese más, pero lo que realmente mejora la nitidez es COLS.
PNG_COMPRESS_LEVEL = 1        # 0-9 | más bajo = menos compresión = más peso
PNG_OPTIMIZE = False

# Si quieres seguir intentando un máximo aproximado, pon por ejemplo 2.0
# Si quieres máxima nitidez sin preocuparte por el peso, deja None.
MAX_FILE_SIZE_MB = None

# ==========================================
# FUNCIONES
# ==========================================

def resolve_image_path():
    for path in POSSIBLE_IMAGE_PATHS:
        if path.exists():
            return str(path)
    raise FileNotFoundError(
        "No encontré 'OB023_step10.png'. Pon la imagen en tu Escritorio o en la misma carpeta del script."
    )


def average_grid_image(image_path, cols, rows):
    img = ImageOps.exif_transpose(Image.open(image_path)).convert("RGB")
    arr = np.array(img)

    h, w, _ = arr.shape

    if rows is None:
        rows = round(cols * h / w)

    cell_h = h / rows
    cell_w = w / cols

    small = Image.new("RGB", (cols, rows))

    for r in range(rows):
        for c in range(cols):
            y0 = int(r * cell_h)
            y1 = int((r + 1) * cell_h)
            x0 = int(c * cell_w)
            x1 = int((c + 1) * cell_w)

            cell = arr[y0:y1, x0:x1]
            avg = tuple(np.mean(cell.reshape(-1, 3), axis=0).astype(int))
            small.putpixel((c, r), avg)

    return small, rows


def quantize_to_palette(img, num_colors=64):
    q = img.convert("P", palette=Image.ADAPTIVE, colors=num_colors)
    palette = q.getpalette()[:num_colors * 3]

    colors = []
    for i in range(num_colors):
        r = palette[i * 3]
        g = palette[i * 3 + 1]
        b = palette[i * 3 + 2]
        colors.append((r, g, b))

    idx = np.array(q)
    return idx, colors


def remap_indices(idx, remap):
    new_idx = idx.copy()
    for old_val, new_val in remap.items():
        old_zero = old_val - 1
        new_zero = new_val - 1
        new_idx[idx == old_zero] = new_zero
    return new_idx


def build_color_image_from_index(idx, colors):
    rows, cols = idx.shape
    img = Image.new("RGB", (cols, rows))

    for r in range(rows):
        for c in range(cols):
            img.putpixel((c, r), colors[idx[r, c]])

    return img


def upscale_nearest(img, cell_size):
    w, h = img.size
    return img.resize((w * cell_size, h * cell_size), Image.Resampling.NEAREST)


def draw_grid_numbers(idx, colors, cell_size=8, title=""):
    rows, cols = idx.shape
    margin_top = 70
    margin_left = 70
    margin_right = 24
    margin_bottom = 24

    W = cols * cell_size + margin_left + margin_right
    H = rows * cell_size + margin_top + margin_bottom

    canvas = Image.new("RGB", (W, H), (245, 243, 238))
    draw = ImageDraw.Draw(canvas)

    try:
        font_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", max(20, int(cell_size * 1.8)))
        font_small = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", max(8, int(cell_size * 0.9)))
        font_cell = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", max(7, int(cell_size * 0.8)))
    except Exception:
        font_title = ImageFont.load_default()
        font_small = ImageFont.load_default()
        font_cell = ImageFont.load_default()

    draw.text((20, 15), title, fill=(40, 40, 40), font=font_title)

    for r in range(rows):
        for c in range(cols):
            val = int(idx[r, c]) + 1
            color = colors[int(idx[r, c])]

            x0 = margin_left + c * cell_size
            y0 = margin_top + r * cell_size
            x1 = x0 + cell_size
            y1 = y0 + cell_size

            draw.rectangle([x0, y0, x1, y1], fill=color, outline=(160, 160, 160))

            brightness = sum(color) / 3
            text_color = (255, 255, 255) if brightness < 120 else (20, 20, 20)

            text = str(val)
            bbox = draw.textbbox((0, 0), text, font=font_cell)
            tw = bbox[2] - bbox[0]
            th = bbox[3] - bbox[1]

            draw.text(
                (x0 + (cell_size - tw) / 2, y0 + (cell_size - th) / 2 - 1),
                text,
                fill=text_color,
                font=font_cell
            )

    for c in range(cols):
        x = margin_left + c * cell_size
        draw.text((x, 45), f"{c+1:02d}", fill=(70, 70, 70), font=font_small)

    for r in range(rows):
        y = margin_top + r * cell_size
        draw.text((10, y), f"{r+1:02d}", fill=(70, 70, 70), font=font_small)

    return canvas


def save_palette_legend(colors, output_path):
    cols_per_row = 8
    sw = 50
    sh = 30
    gap = 10
    margin = 20

    rows_needed = int(np.ceil(len(colors) / cols_per_row))
    W = margin * 2 + cols_per_row * sw + (cols_per_row - 1) * gap
    H = 50 + rows_needed * (sh + 24) + margin

    canvas = Image.new("RGB", (W, H), (245, 243, 238))
    draw = ImageDraw.Draw(canvas)

    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 12)
    except Exception:
        font = ImageFont.load_default()

    draw.text((20, 10), f"Paleta de {len(colors)} colores", fill=(40, 40, 40), font=font)

    for i, color in enumerate(colors):
        row = i // cols_per_row
        col = i % cols_per_row
        x = margin + col * (sw + gap)
        y = 40 + row * (sh + 24)

        draw.rectangle([x, y, x + sw, y + sh], fill=color, outline=(120, 120, 120))
        draw.text((x + 15, y + sh + 4), str(i + 1), fill=(30, 30, 30), font=font)

    save_png(canvas, output_path)


def random_derangement(values, rng):
    values = list(values)
    if len(values) < 2:
        return values[:]

    shuffled = values[:]
    while True:
        rng.shuffle(shuffled)
        if all(a != b for a, b in zip(values, shuffled)):
            return shuffled


def generate_progressive_random_remap(num_colors, amount, rng):
    total = list(range(1, num_colors + 1))

    min_moved = 4
    max_moved = num_colors
    moved_count = int(round(min_moved + amount * (max_moved - min_moved)))
    moved_count = max(2, min(moved_count, num_colors))

    chosen = rng.sample(total, moved_count)
    permuted = random_derangement(chosen, rng)

    remap = dict(zip(chosen, permuted))
    return remap, moved_count


def format_remap(remap):
    pairs = sorted(remap.items(), key=lambda x: x[0])
    return ", ".join([f"{k}->{v}" for k, v in pairs])


def save_png(img, output_path):
    """Guarda PNG RGB con poca compresión. Si MAX_FILE_SIZE_MB es None, no fuerza límite."""
    candidate = img.copy()

    if MAX_FILE_SIZE_MB is None:
        candidate.save(output_path, format="PNG", compress_level=PNG_COMPRESS_LEVEL, optimize=PNG_OPTIMIZE)
        size_mb = Path(output_path).stat().st_size / (1024 * 1024)
        print(f"Guardado: {Path(output_path).name} | {candidate.size[0]}x{candidate.size[1]} | {size_mb:.2f} MB")
        return candidate.size, size_mb

    max_bytes = int(MAX_FILE_SIZE_MB * 1024 * 1024)

    while True:
        candidate.save(output_path, format="PNG", compress_level=PNG_COMPRESS_LEVEL, optimize=PNG_OPTIMIZE)
        file_size = Path(output_path).stat().st_size

        if file_size <= max_bytes:
            size_mb = file_size / (1024 * 1024)
            print(f"Guardado: {Path(output_path).name} | {candidate.size[0]}x{candidate.size[1]} | {size_mb:.2f} MB")
            return candidate.size, size_mb

        new_w = max(1, int(candidate.size[0] * 0.95))
        new_h = max(1, int(candidate.size[1] * 0.95))
        if (new_w, new_h) == candidate.size:
            size_mb = file_size / (1024 * 1024)
            print(f"Aviso: no se pudo reducir más: {Path(output_path).name} | {candidate.size[0]}x{candidate.size[1]} | {size_mb:.2f} MB")
            return candidate.size, size_mb

        candidate = candidate.resize((new_w, new_h), Image.Resampling.NEAREST)


# ==========================================
# EJECUCIÓN
# ==========================================

def main():
    image_path = resolve_image_path()
    image_name = Path(image_path).stem
    desktop = Path.home() / "Desktop"
    output_dir = desktop / f"{image_name}_salida_random_nitida"
    output_dir.mkdir(parents=True, exist_ok=True)

    numbered_dir = output_dir / "numeradas"
    if SAVE_NUMBERED:
        numbered_dir.mkdir(exist_ok=True)

    rng = random.Random(SEED)
    result_cell_size = CELL_SIZE * RESULT_SCALE
    numbered_cell_size = CELL_SIZE * NUMBERED_SCALE

    # 1. Imagen promediada por retícula
    small, real_rows = average_grid_image(image_path, COLS, ROWS)
    save_png(small, output_dir / "01_promedio_reticula.png")

    # 2. Cuantizar a la cantidad de colores configurada
    idx, colors = quantize_to_palette(small, NUM_COLORS)

    # 3. Matriz original
    orig_quant = build_color_image_from_index(idx, colors)
    up_orig = upscale_nearest(orig_quant, result_cell_size)
    save_png(up_orig, output_dir / "02_matriz_color_original.png")

    # 4. Matriz original numerada
    diagram_orig = draw_grid_numbers(idx, colors, numbered_cell_size, title="Matriz cromática original")
    save_png(diagram_orig, output_dir / "03_matriz_color_original_numerada.png")

    # 5. Paleta
    save_palette_legend(colors, output_dir / f"04_paleta_{NUM_COLORS}_colores.png")

    # 6. Generar variantes aleatorias de menos a más
    report_lines = []
    report_lines.append(f"Imagen fuente: {image_path}")
    report_lines.append(f"Filas calculadas automáticamente: {real_rows}")
    report_lines.append(f"Columnas: {COLS}")
    report_lines.append(f"Colores: {NUM_COLORS}")
    report_lines.append(f"CELL_SIZE: {CELL_SIZE}")
    report_lines.append(f"Compresión PNG: {PNG_COMPRESS_LEVEL}")
    report_lines.append("")

    for i in range(NUM_VARIANTS):
        amount = i / (NUM_VARIANTS - 1) if NUM_VARIANTS > 1 else 1.0
        remap, moved_count = generate_progressive_random_remap(NUM_COLORS, amount, rng)
        idx_remap = remap_indices(idx, remap)

        remap_img = build_color_image_from_index(idx_remap, colors)
        up_remap = upscale_nearest(remap_img, result_cell_size)

        n = i + 1
        out_name = output_dir / f"{n:02d}_matriz_color_remapeada.png"
        final_size_px, final_mb = save_png(up_remap, out_name)

        title = f"Matriz cromática remapeada {n:02d} | intensidad {amount:.0%}"
        if SAVE_NUMBERED:
            diagram_remap = draw_grid_numbers(idx_remap, colors, numbered_cell_size, title=title)
            save_png(diagram_remap, numbered_dir / f"{n:02d}_matriz_color_remapeada_numerada.png")

        report_lines.append(f"VARIANTE {n:02d}")
        report_lines.append(f"Intensidad: {amount:.0%}")
        report_lines.append(f"Cantidad de índices remapeados: {moved_count}")
        report_lines.append(f"Tamaño final guardado: {final_size_px[0]}x{final_size_px[1]} | {final_mb:.2f} MB")
        report_lines.append(format_remap(remap))
        report_lines.append("")

    with open(output_dir / "remapeos_usados.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    print("\nListo.")
    print(f"Imagen usada: {image_path}")
    print(f"Filas calculadas automáticamente: {real_rows}")
    print(f"Se generaron los archivos en: {output_dir}")
    if SAVE_NUMBERED:
        print(f"Versiones numeradas en: {numbered_dir}")


if __name__ == "__main__":
    main()
