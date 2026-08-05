from PIL import Image, ImageDraw, ImageOps
import numpy as np
import math
from datetime import datetime
import os

# =========================
# CONFIGURACIÓN
# =========================
input_files = [
    "input_02.jpeg",
    "input_03.jpeg"
]

# Más grande = más crisis / menos detalle
cell_size = 600

# Aumenta o reduce el tamaño de los puntos
dot_scale = 1.20

# Ángulos clásicos de retícula CMYK
angles = {
    "C": 15,
    "M": 75,
    "Y": 0,
    "K": 45
}

# =========================
# FUNCIÓN: HALFTONE POR CANAL
# =========================
def halftone_channel(channel_img, angle, cell_size, dot_scale):
    w, h = channel_img.size
    margin = cell_size * 4

    # padding para evitar bordes raros al rotar
    padded = Image.new("L", (w + 2 * margin, h + 2 * margin), 0)
    padded.paste(channel_img, (margin, margin))

    rotated = padded.rotate(angle, expand=True, resample=Image.Resampling.BICUBIC)
    rw, rh = rotated.size

    arr = np.array(rotated, dtype=np.float32) / 255.0

    # fondo blanco = papel
    screen = Image.new("L", (rw, rh), 255)
    draw = ImageDraw.Draw(screen)

    for y in range(0, rh, cell_size):
        for x in range(0, rw, cell_size):
            block = arr[y:y + cell_size, x:x + cell_size]
            if block.size == 0:
                continue

            ink = block.mean()

            radius = (cell_size / 2.0) * math.sqrt(ink) * dot_scale

            if radius < 0.3:
                continue

            cx = x + block.shape[1] / 2.0
            cy = y + block.shape[0] / 2.0

            draw.ellipse(
                (cx - radius, cy - radius, cx + radius, cy + radius),
                fill=0
            )

    # desrotar
    unrot = screen.rotate(-angle, expand=True, resample=Image.Resampling.BICUBIC)

    # recorte al tamaño original con padding
    uw, uh = unrot.size
    crop_w = w + 2 * margin
    crop_h = h + 2 * margin
    left = (uw - crop_w) // 2
    top = (uh - crop_h) // 2
    unrot = unrot.crop((left, top, left + crop_w, top + crop_h))

    # quitar padding
    final = unrot.crop((margin, margin, margin + w, margin + h))
    return final

# =========================
# PROCESAR CADA IMAGEN
# =========================
for input_path in input_files:
    if not os.path.exists(input_path):
        print(f"No se encontró el archivo: {input_path}")
        continue

    # timestamp único por imagen
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dot_scale_str = str(dot_scale).replace(".", "p")
    base_name = os.path.splitext(os.path.basename(input_path))[0]

    output_path = f"{base_name}_reticula_CMYK_cs{cell_size}_ds{dot_scale_str}_{timestamp}.png"

    # cargar imagen y respetar orientación EXIF
    img = Image.open(input_path)
    img = ImageOps.exif_transpose(img)
    img = img.convert("RGB")
    orig_w, orig_h = img.size

    # convertir a CMYK y separar canales
    cmyk = img.convert("CMYK")
    c, m, y, k = cmyk.split()

    # generar retícula por canal
    c_screen = halftone_channel(c, angles["C"], cell_size, dot_scale)
    m_screen = halftone_channel(m, angles["M"], cell_size, dot_scale)
    y_screen = halftone_channel(y, angles["Y"], cell_size, dot_scale)
    k_screen = halftone_channel(k, angles["K"], cell_size, dot_scale)

    # recomponer a RGB
    C = 1.0 - (np.array(c_screen, dtype=np.float32) / 255.0)
    M = 1.0 - (np.array(m_screen, dtype=np.float32) / 255.0)
    Y = 1.0 - (np.array(y_screen, dtype=np.float32) / 255.0)
    K = 1.0 - (np.array(k_screen, dtype=np.float32) / 255.0)

    R = 255 * (1 - C) * (1 - K)
    G = 255 * (1 - M) * (1 - K)
    B = 255 * (1 - Y) * (1 - K)

    result = np.dstack([R, G, B]).clip(0, 255).astype(np.uint8)
    result_img = Image.fromarray(result, mode="RGB")

    # asegurar tamaño/orientación original
    result_img = result_img.resize((orig_w, orig_h), Image.Resampling.BICUBIC)

    # guardar
    result_img.save(output_path)
    print(f"Imagen guardada en: {output_path}")
