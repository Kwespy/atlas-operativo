from PIL import Image, ImageOps
import numpy as np
import os
from datetime import datetime

# =========================================================
# INPUTS
# =========================================================

INPUTS = [
    "input_02.jpeg",
    "input_03.jpeg"
]

# =========================================================
# PARÁMETROS PRINCIPALES
# =========================================================
# RGB        -> dirección
# brillo     -> distancia
# saturación -> curvatura

DISTANCIA_MAX = 30     # qué tan lejos puede llegar un píxel
PASOS = 32              # cantidad de pasos de la estela
CURVATURA_MAX = 2.4     # fuerza máxima de la curva
FUERZA_NEUTROS = 1.78   # cuánto se mueven/curvan también los tonos poco saturados
PESO_ORIGINAL = 0.05    # cuánto de la imagen original se conserva debajo

# Si quieres acelerar, puedes bajar esto a 0.75 o 0.5
ESCALA_PROCESO = 1.0

# =========================================================
# DIRECCIONES BASE PARA RGB
# =========================================================
# R =   0°
# G = 120°
# B = 240°

ANG_R = 0.0
ANG_G = 2.0 * np.pi / 3.0
ANG_B = 4.0 * np.pi / 3.0

# =========================================================
# FUNCIÓN PRINCIPAL
# =========================================================

def procesar_imagen(input_path):
    print(f"\nProcesando: {input_path}")

    # -----------------------------------------------------
    # 1. ABRIR Y RESPETAR ORIENTACIÓN
    # -----------------------------------------------------
    img = Image.open(input_path)
    img = ImageOps.exif_transpose(img)
    img = img.convert("RGB")

    ancho_original, alto_original = img.size

    # -----------------------------------------------------
    # 2. ESCALA INTERNA OPCIONAL
    # -----------------------------------------------------
    if ESCALA_PROCESO != 1.0:
        nuevo_ancho = max(1, int(ancho_original * ESCALA_PROCESO))
        nuevo_alto = max(1, int(alto_original * ESCALA_PROCESO))
        img = img.resize((nuevo_ancho, nuevo_alto), Image.Resampling.LANCZOS)

    arr = np.asarray(img, dtype=np.float32)
    alto, ancho, _ = arr.shape

    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]

    # -----------------------------------------------------
    # 3. PORCENTAJES RGB -> DIRECCIÓN
    # -----------------------------------------------------
    suma = r + g + b + 1e-6

    pr = r / suma
    pg = g / suma
    pb = b / suma

    vx = (
        pr * np.cos(ANG_R) +
        pg * np.cos(ANG_G) +
        pb * np.cos(ANG_B)
    )

    vy = (
        pr * np.sin(ANG_R) +
        pg * np.sin(ANG_G) +
        pb * np.sin(ANG_B)
    )

    magnitud = np.sqrt(vx * vx + vy * vy)
    vx = vx / np.maximum(magnitud, 1e-6)
    vy = vy / np.maximum(magnitud, 1e-6)

    # perpendicular al vector (para la curvatura)
    px = -vy
    py = vx

    # -----------------------------------------------------
    # 4. BRILLO -> DISTANCIA
    # -----------------------------------------------------
    brillo = (
        0.2126 * r +
        0.7152 * g +
        0.0722 * b
    ) / 255.0

    # brillo bajo = distancia menor
    # brillo alto = distancia mayor
    distancia = (0.22 + 0.78 * brillo) * DISTANCIA_MAX

    # -----------------------------------------------------
    # 5. SATURACIÓN / DIFERENCIA ENTRE CANALES -> CURVATURA
    # -----------------------------------------------------
    max_rgb = np.max(arr, axis=2)
    min_rgb = np.min(arr, axis=2)

    saturacion = (max_rgb - min_rgb) / 255.0

    # que también los tonos neutros se muevan algo
    actividad = FUERZA_NEUTROS + (1.0 - FUERZA_NEUTROS) * saturacion

    # signo de la curva:
    # rojo dominante curva hacia un lado,
    # azul dominante hacia el otro,
    # verde queda más intermedio
    signo_curva = (pr - pb)

    # magnitud de la curva
    curvatura = signo_curva * actividad * CURVATURA_MAX

    # -----------------------------------------------------
    # 6. COORDENADAS
    # -----------------------------------------------------
    yy, xx = np.indices((alto, ancho))

    # -----------------------------------------------------
    # 7. ACUMULADORES
    # -----------------------------------------------------
    acumulado = arr * PESO_ORIGINAL
    pesos = np.full((alto, ancho), PESO_ORIGINAL, dtype=np.float32)

    # -----------------------------------------------------
    # 8. CONSTRUIR ESTELA CURVA
    # -----------------------------------------------------
    for paso in range(1, PASOS + 1):
        t = paso / PASOS

        # avance principal
        avance_x = vx * distancia * t
        avance_y = vy * distancia * t

        # curvatura: máxima hacia la mitad del recorrido
        # NO es random, es completamente determinista
        offset_curva = (
            np.sin(np.pi * t)
            * curvatura
            * DISTANCIA_MAX
            * 0.35
        )

        curva_x = px * offset_curva
        curva_y = py * offset_curva

        nx = np.rint(xx + avance_x + curva_x).astype(np.int32)
        ny = np.rint(yy + avance_y + curva_y).astype(np.int32)

        valido = (
            (nx >= 0) & (nx < ancho) &
            (ny >= 0) & (ny < alto)
        )

        ox = xx[valido]
        oy = yy[valido]
        dxv = nx[valido]
        dyv = ny[valido]

        # peso de la estela: ligeramente más fuerte hacia el final
        alpha = 0.30 + 0.70 * t

        np.add.at(acumulado, (dyv, dxv), arr[oy, ox] * alpha)
        np.add.at(pesos, (dyv, dxv), alpha)

        print(f"  paso {paso}/{PASOS}")

    # -----------------------------------------------------
    # 9. NORMALIZAR
    # -----------------------------------------------------
    resultado = acumulado / np.maximum(pesos[:, :, None], 1e-6)
    resultado = np.clip(resultado, 0, 255).astype(np.uint8)

    salida = Image.fromarray(resultado)

    # si procesaste más pequeño, lo devolvemos al tamaño original
    if ESCALA_PROCESO != 1.0:
        salida = salida.resize((ancho_original, alto_original), Image.Resampling.LANCZOS)

    # -----------------------------------------------------
    # 10. GUARDAR CON NOMBRE ÚNICO
    # -----------------------------------------------------
    nombre_base = os.path.splitext(os.path.basename(input_path))[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")

    output_path = f"{nombre_base}_derretimiento_rgb_curvo_{timestamp}.png"
    salida.save(output_path)

    print(f"Guardado: {output_path}")

# =========================================================
# EJECUCIÓN
# =========================================================

for archivo in INPUTS:
    if os.path.exists(archivo):
        procesar_imagen(archivo)
    else:
        print(f"No se encontró el archivo: {archivo}")
