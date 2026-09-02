from PIL import Image, ImageOps
import numpy as np
import cv2
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
# PARÁMETROS
# =========================================================

ANCHO_PROCESO = 10100

SUAVIZADO = 180.0

BINS_RGB = 80

TAMANO_MINIMO = 800

SATURACION = 100.0

UNIFICACION = 100.00

INTENSIDAD = 100.0


# =========================================================
# FUNCIÓN PRINCIPAL
# =========================================================

def procesar_imagen(INPUT):

    print(f"\nProcesando: {INPUT}")

    img_pil = Image.open(INPUT)
    img_pil = ImageOps.exif_transpose(img_pil)
    img_pil = img_pil.convert("RGB")

    ancho_original, alto_original = img_pil.size
    original = np.array(img_pil, dtype=np.uint8)

    # =====================================================
    # REDUCIR PARA PROCESAR MÁS RÁPIDO
    # =====================================================

    if ancho_original > ANCHO_PROCESO:

        escala = ANCHO_PROCESO / ancho_original

        ancho = ANCHO_PROCESO
        alto = int(alto_original * escala)

        img = cv2.resize(
            original,
            (ancho, alto),
            interpolation=cv2.INTER_AREA
        )

    else:

        img = original.copy()
        alto, ancho = img.shape[:2]

    print(f"Original: {ancho_original} x {alto_original}")
    print(f"Procesando internamente: {ancho} x {alto}")

    # =====================================================
    # 1. SUAVIZADO
    # =====================================================

    blur = cv2.GaussianBlur(
        img,
        (0, 0),
        sigmaX=SUAVIZADO,
        sigmaY=SUAVIZADO
    )

    # =====================================================
    # 2. PORCENTAJES RGB
    # =====================================================

    f = blur.astype(np.float32)

    suma = f.sum(axis=2) + 0.000001

    r = f[:, :, 0] / suma
    g = f[:, :, 1] / suma
    b = f[:, :, 2] / suma

    # =====================================================
    # 3. CUANTIZAR RGB
    # =====================================================

    rq = np.floor(r * BINS_RGB).astype(np.int32)
    gq = np.floor(g * BINS_RGB).astype(np.int32)
    bq = np.floor(b * BINS_RGB).astype(np.int32)

    rq = np.clip(rq, 0, BINS_RGB - 1)
    gq = np.clip(gq, 0, BINS_RGB - 1)
    bq = np.clip(bq, 0, BINS_RGB - 1)

    labels_rgb = (
        rq
        + BINS_RGB * gq
        + (BINS_RGB ** 2) * bq
    )

    # =====================================================
    # 4. BUSCAR REGIONES VECINAS
    # =====================================================

    resultado = img.astype(np.float32).copy()

    familias = np.unique(labels_rgb)

    print(f"Familias cromáticas encontradas: {len(familias)}")

    for familia in familias:

        ys, xs = np.where(labels_rgb == familia)

        if len(xs) < TAMANO_MINIMO:
            continue

        x0 = xs.min()
        x1 = xs.max() + 1
        y0 = ys.min()
        y1 = ys.max() + 1

        mapa_local = labels_rgb[y0:y1, x0:x1]

        mascara = (
            mapa_local == familia
        ).astype(np.uint8)

        cantidad, componentes, stats, _ = cv2.connectedComponentsWithStats(
            mascara,
            connectivity=8
        )

        for grupo in range(1, cantidad):

            tamano = stats[
                grupo,
                cv2.CC_STAT_AREA
            ]

            if tamano < TAMANO_MINIMO:
                continue

            region = componentes == grupo

            yy, xx = np.where(region)

            yy = yy + y0
            xx = xx + x0

            colores = img[
                yy,
                xx
            ].astype(np.float32)

            # color medio
            color_medio = colores.mean(axis=0)

            # porcentajes RGB medios
            rr = r[yy, xx].mean()
            gg = g[yy, xx].mean()
            bb = b[yy, xx].mean()

            porcentajes = np.array(
                [rr, gg, bb],
                dtype=np.float32
            )

            dominante = np.argmax(porcentajes)

            ordenados = np.sort(porcentajes)

            dominancia = (
                ordenados[-1]
                - ordenados[-2]
            )

            # =================================================
            # SATURAR CANAL DOMINANTE
            # =================================================

            color_nuevo = color_medio.copy()

            fuerza = (
                SATURACION
                * (0.30 + dominancia * 3.0)
            )

            fuerza = np.clip(
                fuerza,
                0.0,
                1.0
            )

            color_nuevo[dominante] += (
                255 - color_nuevo[dominante]
            ) * fuerza

            for canal in range(3):

                if canal != dominante:

                    color_nuevo[canal] *= (
                        1.0
                        - 0.30 * fuerza
                    )

            color_nuevo = np.clip(
                color_nuevo,
                0,
                255
            )

            # =================================================
            # UNIFICAR REGIÓN
            # =================================================

            resultado[yy, xx] = (
                resultado[yy, xx]
                * (1.0 - UNIFICACION)
                +
                color_nuevo
                * UNIFICACION
            )

    # =====================================================
    # MEZCLA FINAL
    # =====================================================

    resultado = np.clip(
        resultado,
        0,
        255
    ).astype(np.uint8)

    resultado = cv2.addWeighted(
        img,
        1.0 - INTENSIDAD,
        resultado,
        INTENSIDAD,
        0
    )

    # =====================================================
    # VOLVER AL TAMAÑO ORIGINAL
    # =====================================================

    if ancho != ancho_original or alto != alto_original:

        resultado = cv2.resize(
            resultado,
            (ancho_original, alto_original),
            interpolation=cv2.INTER_CUBIC
        )

    # =====================================================
    # GUARDAR CON NOMBRE ÚNICO
    # =====================================================

    nombre_base = os.path.splitext(
        os.path.basename(INPUT)
    )[0]

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S_%f"
    )

    OUTPUT = (
        f"{nombre_base}_"
        f"saturacion_vecindad_RGB_"
        f"{timestamp}.jpg"
    )

    Image.fromarray(resultado).save(
        OUTPUT,
        quality=96
    )

    print(f"Guardado: {OUTPUT}")


# =========================================================
# EJECUCIÓN
# =========================================================

for archivo in INPUTS:

    if os.path.exists(archivo):

        procesar_imagen(archivo)

    else:

        print(
            f"No se encontró el archivo: {archivo}"
        )

print("\nTERMINADO")
