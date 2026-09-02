from PIL import Image, ImageDraw, ImageFont, ImageOps
import numpy as np
import os

# ==========================================
# CONFIGURACIÓN
# ==========================================

IMAGE_PATH = "pelota.jpg"   # nombre exacto de tu imagen
COLS = 96                   # MÁS DETALLE REAL
ROWS = None                 # se calcula automáticamente según la proporción vertical/horizontal
NUM_COLORS = 64             # mantenemos 64 colores
CELL_SIZE = 8               # cuadrado visual más pequeño

# Remapeo de ejemplo
REMAP = {
30: 10,
    10: 30,

    31: 11,
    11: 31,

    32: 12,
    12: 32,

    33: 13,
    13: 33,

    34: 14,
    14: 34,

    35: 15,
    15: 35,

    36: 16,
    16: 36,

    37: 17,
    17: 37,

    38: 18,
    18: 38,

    39: 19,
    19: 39,

    40: 20,
    20: 40,

    # Intercambios que se mantienen
    2: 41,
    41: 2,

    3: 43,
    43: 3,

    4: 44,
    44: 4,

    5: 45,
    45: 5,

    6: 46,
    46: 6,

    7: 47,
    47: 7,

    8: 48,
    48: 8,

    9: 49,
    49: 9,

    21: 56,
    56: 21,

    23: 60,
    60: 23,

    25: 42,
    42: 25,

    26: 55,
    55: 26,

    29: 53,
    53: 29,

    # Números restantes reorganizados
    1: 50,
    50: 1,

    22: 59,
    59: 22,

    24: 62,
    62: 24,

    27: 57,
    57: 27,

    28: 58,
    58: 28,

    51: 61,
    61: 51,

    52: 63,
    63: 52,

    54: 64,
    64: 54,
}
# ==========================================
# FUNCIONES
# ==========================================

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
    margin_top = 60
    margin_left = 60
    margin_right = 20
    margin_bottom = 20

    W = cols * cell_size + margin_left + margin_right
    H = rows * cell_size + margin_top + margin_bottom

    canvas = Image.new("RGB", (W, H), (245, 243, 238))
    draw = ImageDraw.Draw(canvas)

    try:
        font_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 20)
        font_small = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 8)
        font_cell = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 7)
    except:
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
        draw.text((x, 40), f"{c+1:02d}", fill=(70, 70, 70), font=font_small)

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

    canvas = Image.new("RGB", (W, H), (245,243,238))
    draw = ImageDraw.Draw(canvas)

    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 12)
    except:
        font = ImageFont.load_default()

    draw.text((20, 10), "Paleta de 64 colores", fill=(40,40,40), font=font)

    for i, color in enumerate(colors):
        row = i // cols_per_row
        col = i % cols_per_row
        x = margin + col * (sw + gap)
        y = 40 + row * (sh + 24)

        draw.rectangle([x, y, x+sw, y+sh], fill=color, outline=(120,120,120))
        draw.text((x + 15, y + sh + 4), str(i+1), fill=(30,30,30), font=font)

    canvas.save(output_path)

# ==========================================
# EJECUCIÓN
# ==========================================

os.makedirs("salida", exist_ok=True)

# 1. Imagen promediada por retícula
small, real_rows = average_grid_image(IMAGE_PATH, COLS, ROWS)
small.save("salida/01_promedio_reticula.png")

# 2. Cuantizar a 64 colores
idx, colors = quantize_to_palette(small, NUM_COLORS)

# 3. Matriz original
orig_quant = build_color_image_from_index(idx, colors)
up_orig = upscale_nearest(orig_quant, CELL_SIZE)
up_orig.save("salida/02_matriz_color_original.png")

# 4. Matriz original numerada
diagram_orig = draw_grid_numbers(idx, colors, CELL_SIZE, title="Matriz cromática original")
diagram_orig.save("salida/03_matriz_color_original_numerada.png")

# 5. Paleta
save_palette_legend(colors, "salida/04_paleta_64_colores.png")

# 6. Remapeo
idx_remap = remap_indices(idx, REMAP)

# 7. Matriz remapeada
remap_img = build_color_image_from_index(idx_remap, colors)
up_remap = upscale_nearest(remap_img, CELL_SIZE)
up_remap.save("salida/05_matriz_color_remapeada.png")

# 8. Matriz remapeada numerada
diagram_remap = draw_grid_numbers(idx_remap, colors, CELL_SIZE, title="Matriz cromática remapeada")
diagram_remap.save("salida/06_matriz_color_remapeada_numerada.png")

print("Listo.")
print(f"Filas calculadas automáticamente: {real_rows}")
print("Se generaron los archivos en la carpeta 'salida'.")
