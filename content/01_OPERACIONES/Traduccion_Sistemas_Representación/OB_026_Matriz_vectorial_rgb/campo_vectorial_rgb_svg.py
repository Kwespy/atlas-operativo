from PIL import Image, ImageOps, ImageDraw
import numpy as np
import os
from datetime import datetime
from math import cos, sin, pi

# =========================================================
# INPUTS
# =========================================================

INPUTS = [
    "input_02.jpeg",
    "input_03.jpeg"
]

# =========================================================
# PARÁMETROS
# =========================================================

# cada cuántos píxeles tomar una muestra
# más bajo = más detalle
# más alto = más síntesis
MUESTREO = 2

# largo mínimo y máximo de cada vector
LONGITUD_MIN = 600.0
LONGITUD_MAX = 658.0

# grosor mínimo y máximo del vector
GROSOR_MIN = 1588.0
GROSOR_MAX = 1590.0

# color de los vectores:
# "negro"    -> todos negros
# "original" -> color RGB del píxel
MODO_COLOR = "original"

# fondo del PNG
FONDO = "white"

# opacidad general (0–255)
OPACIDAD = 230

# escala final de salida
ESCALA_SALIDA = 1.0

# =========================================================
# DIRECCIONES BASE RGB
# =========================================================
# R = 0°
# G = 120°
# B = 240°

ANG_R = 0.0
ANG_G = 2.0 * pi / 3.0
ANG_B = 4.0 * pi / 3.0

VR = np.array([cos(ANG_R), sin(ANG_R)], dtype=np.float32)
VG = np.array([cos(ANG_G), sin(ANG_G)], dtype=np.float32)
VB = np.array([cos(ANG_B), sin(ANG_B)], dtype=np.float32)

# =========================================================
# FUNCIÓN PRINCIPAL
# =========================================================

def procesar_imagen(input_path):
    print(f"\nProcesando: {input_path}")

    # -----------------------------------------------------
    # ABRIR IMAGEN
    # -----------------------------------------------------
    img = Image.open(input_path)
    img = ImageOps.exif_transpose(img)
    img = img.convert("RGB")

    ancho, alto = img.size
    arr = np.asarray(img, dtype=np.float32)

    ancho_salida = int(ancho * ESCALA_SALIDA)
    alto_salida = int(alto * ESCALA_SALIDA)

    # -----------------------------------------------------
    # CREAR LIENZO NUEVO
    # -----------------------------------------------------
    salida = Image.new("RGBA", (ancho_salida, alto_salida), FONDO)
    draw = ImageDraw.Draw(salida, "RGBA")

    contador = 0

    # -----------------------------------------------------
    # RECORRER MUESTRAS
    # -----------------------------------------------------
    for y in range(0, alto, MUESTREO):
        for x in range(0, ancho, MUESTREO):
            r, g, b = arr[y, x]

            suma = r + g + b + 1e-6
            pr = r / suma
            pg = g / suma
            pb = b / suma

            # -------------------------------------------------
            # DIRECCIÓN = mezcla proporcional RGB
            # -------------------------------------------------
            v = pr * VR + pg * VG + pb * VB
            magnitud = np.sqrt(v[0] * v[0] + v[1] * v[1])

            if magnitud < 1e-6:
                continue

            v = v / magnitud

            # -------------------------------------------------
            # BRILLO = longitud
            # -------------------------------------------------
            brillo = (
                0.2126 * r +
                0.7152 * g +
                0.0722 * b
            ) / 255.0

            longitud = LONGITUD_MIN + brillo * (LONGITUD_MAX - LONGITUD_MIN)

            # -------------------------------------------------
            # SATURACIÓN = grosor
            # -------------------------------------------------
            max_rgb = max(r, g, b)
            min_rgb = min(r, g, b)
            saturacion = (max_rgb - min_rgb) / 255.0

            grosor = GROSOR_MIN + saturacion * (GROSOR_MAX - GROSOR_MIN)
            grosor = max(1, int(round(grosor * ESCALA_SALIDA)))

            # -------------------------------------------------
            # CENTRO DEL VECTOR
            # -------------------------------------------------
            cx = x * ESCALA_SALIDA
            cy = y * ESCALA_SALIDA

            dx = v[0] * longitud * 0.5 * ESCALA_SALIDA
            dy = v[1] * longitud * 0.5 * ESCALA_SALIDA

            x1 = cx - dx
            y1 = cy - dy
            x2 = cx + dx
            y2 = cy + dy

            # -------------------------------------------------
            # COLOR
            # -------------------------------------------------
            if MODO_COLOR == "original":
                color = (int(r), int(g), int(b), OPACIDAD)
            else:
                color = (0, 0, 0, OPACIDAD)

            # -------------------------------------------------
            # DIBUJAR VECTOR
            # -------------------------------------------------
            draw.line(
                [(x1, y1), (x2, y2)],
                fill=color,
                width=grosor
            )

            contador += 1

        print(f"  fila {y} / {alto}")

    # -----------------------------------------------------
    # GUARDAR PNG
    # -----------------------------------------------------
    nombre_base = os.path.splitext(os.path.basename(input_path))[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    output_path = f"{nombre_base}_campo_vectorial_RGB_{timestamp}.png"

    salida.save(output_path)

    print(f"Vectores dibujados: {contador}")
    print(f"Guardado: {output_path}")

# =========================================================
# EJECUCIÓN
# =========================================================

for archivo in INPUTS:
    if os.path.exists(archivo):
        procesar_imagen(archivo)
    else:
        print(f"No se encontró el archivo: {archivo}")

print("\nTERMINADO")
