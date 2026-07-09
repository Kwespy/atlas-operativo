from PIL import Image, ImageDraw, ImageOps
import numpy as np
import cv2
from skimage import measure
import math
import os

# ============================================================
# CRISIS POR ZONAS
# Cada zona usa una fuente distinta de datos para construir
# el relieve topográfico.
#
# pelota  -> luminosidad corregida
# lado izq / vaso -> canal rojo
# mesa    -> canal azul
# muro    -> saturación
# ============================================================

# ----------------------------
# ARCHIVOS
# ----------------------------
INPUT_IMAGE = "pelota.jpg"
OUTPUT_IMAGE = "foto_topografica_crisis_zonas.png"
OUTPUT_RELIEF = "foto_relieve_crisis_zonas.png"

# ----------------------------
# VARIABLES GENERALES
# ----------------------------
N_LEVELS = 24
LINE_WIDTH = 1
LINE_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)

# ----------------------------
# BLURS POR ZONA
# ----------------------------
SCENE_BLUR_WALL = 14
SCENE_BLUR_TABLE = 12
SCENE_BLUR_LEFT = 10

# ----------------------------
# PELOTA: LIMPIEZA DE SUPERFICIE
# ----------------------------
DARK_PERCENTILE = 35
LOCAL_DARK_DIFFERENCE = 12
BALL_BLUR_FRACTION = 0.24

# ----------------------------
# DIVISIÓN ESPACIAL
# ----------------------------
# línea aproximada donde empieza la mesa
TABLE_START_FRACTION = 0.64

# ancho aproximado de la zona izquierda donde cae el vaso
LEFT_ZONE_WIDTH_FRACTION = 0.36

DRAW_BALL_BORDER = False


# ============================================================
# 1. SELECCIONAR LA PELOTA
# ============================================================

def seleccionar_pelota(imagen_rgb):
    alto, ancho = imagen_rgb.shape[:2]

    max_preview = 1100
    scale = min(1.0, max_preview / max(ancho, alto))

    if scale < 1:
        preview = cv2.resize(
            imagen_rgb,
            (int(ancho * scale), int(alto * scale)),
            interpolation=cv2.INTER_AREA
        )
    else:
        preview = imagen_rgb.copy()

    clicks = []

    def refrescar():
        canvas = preview.copy()

        texto = "Click 1: centro de la pelota"
        if len(clicks) == 1:
            texto = "Click 2: borde exterior"
        elif len(clicks) == 2:
            texto = "ENTER aceptar | R reiniciar | Q salir"

        if len(clicks) >= 1:
            x, y = clicks[0]
            cv2.circle(canvas, (int(x * scale), int(y * scale)), 5, (0, 255, 0), -1)

        if len(clicks) == 2:
            cx, cy = clicks[0]
            ex, ey = clicks[1]
            radio = int(math.hypot(ex - cx, ey - cy))

            cv2.circle(
                canvas,
                (int(cx * scale), int(cy * scale)),
                int(radio * scale),
                (0, 255, 0),
                2
            )

        cv2.putText(
            canvas,
            texto,
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (0, 255, 0),
            2,
            cv2.LINE_AA
        )

        cv2.imshow("Selecciona la pelota", cv2.cvtColor(canvas, cv2.COLOR_RGB2BGR))

    def click(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN and len(clicks) < 2:
            clicks.append((x / scale, y / scale))
            refrescar()

    cv2.namedWindow("Selecciona la pelota", cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("Selecciona la pelota", click)
    refrescar()

    while True:
        tecla = cv2.waitKey(20) & 0xFF

        if tecla in [13, 10, 32] and len(clicks) == 2:
            break

        if tecla in [ord("r"), ord("R")]:
            clicks = []
            refrescar()

        if tecla in [ord("q"), ord("Q"), 27]:
            cv2.destroyAllWindows()
            raise SystemExit("Proceso cancelado.")

    cv2.destroyAllWindows()

    cx, cy = clicks[0]
    ex, ey = clicks[1]
    radio = math.hypot(ex - cx, ey - cy)

    return int(cx), int(cy), int(radio)


# ============================================================
# 2. CARGAR IMAGEN
# ============================================================

if not os.path.exists(INPUT_IMAGE):
    raise FileNotFoundError(f"No encuentro '{INPUT_IMAGE}'")

imagen_pil = Image.open(INPUT_IMAGE)
imagen_pil = ImageOps.exif_transpose(imagen_pil)
imagen_pil = imagen_pil.convert("RGB")

imagen_rgb = np.array(imagen_pil)
alto_total, ancho_total = imagen_rgb.shape[:2]

# canales base
R = imagen_rgb[:, :, 0]
G = imagen_rgb[:, :, 1]
B = imagen_rgb[:, :, 2]

gris = cv2.cvtColor(imagen_rgb, cv2.COLOR_RGB2GRAY)
hsv = cv2.cvtColor(imagen_rgb, cv2.COLOR_RGB2HSV)
S = hsv[:, :, 1]  # saturación

print("\nSelecciona la pelota:")
print("1. Click en el centro.")
print("2. Click en el borde.")
print("3. ENTER para aceptar.\n")

cx, cy, radio = seleccionar_pelota(imagen_rgb)

if radio < 30:
    raise ValueError("Radio demasiado pequeño.")

print(f"Centro seleccionado: ({cx}, {cy})")
print(f"Radio seleccionado: {radio}px")


# ============================================================
# 3. MÁSCARAS DE ZONAS
# ============================================================

Y, X = np.ogrid[:alto_total, :ancho_total]

mascara_pelota = ((X - cx) ** 2 + (Y - cy) ** 2) <= radio ** 2

table_y = int(alto_total * TABLE_START_FRACTION)
left_x = int(ancho_total * LEFT_ZONE_WIDTH_FRACTION)

mascara_mesa = (Y >= table_y)
mascara_izquierda = (X < left_x) & (Y < table_y)
mascara_muro = (Y < table_y)

# prioridad de zonas:
# 1 pelota
# 2 izquierda / vaso
# 3 mesa
# 4 muro
mascara_izquierda = mascara_izquierda & (~mascara_pelota)
mascara_mesa = mascara_mesa & (~mascara_pelota)
mascara_muro = mascara_muro & (~mascara_pelota) & (~mascara_izquierda)


# ============================================================
# 4. PELOTA CORREGIDA
# ============================================================

sigma_local = max(2, int(radio * 0.025))

suavizado_local = cv2.GaussianBlur(
    gris,
    (0, 0),
    sigmaX=sigma_local,
    sigmaY=sigma_local
)

valores_pelota = gris[mascara_pelota]
limite_oscuro = np.percentile(valores_pelota, DARK_PERCENTILE)

mascara_costuras = (
    ((gris < (suavizado_local - LOCAL_DARK_DIFFERENCE)) | (gris < limite_oscuro))
    & mascara_pelota
)

tam_kernel = max(3, int(radio * 0.018))
if tam_kernel % 2 == 0:
    tam_kernel += 1

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (tam_kernel, tam_kernel))

mascara_costuras = cv2.dilate(
    mascara_costuras.astype(np.uint8),
    kernel,
    iterations=1
)

radio_relleno = max(5, int(radio * 0.08))

pelota_rellena = cv2.inpaint(
    gris,
    (mascara_costuras * 255).astype(np.uint8),
    radio_relleno,
    cv2.INPAINT_TELEA
)

sigma_ball = max(8, int(radio * BALL_BLUR_FRACTION))

relieve_pelota = cv2.GaussianBlur(
    pelota_rellena,
    (0, 0),
    sigmaX=sigma_ball,
    sigmaY=sigma_ball
)


# ============================================================
# 5. RELIEVES POR ZONA
# ============================================================

# muro / fondo superior -> saturación
relieve_muro = cv2.GaussianBlur(
    S,
    (0, 0),
    sigmaX=SCENE_BLUR_WALL,
    sigmaY=SCENE_BLUR_WALL
)

# mesa -> canal azul
relieve_mesa = cv2.GaussianBlur(
    B,
    (0, 0),
    sigmaX=SCENE_BLUR_TABLE,
    sigmaY=SCENE_BLUR_TABLE
)

# izquierda / vaso -> canal rojo
relieve_izquierda = cv2.GaussianBlur(
    R,
    (0, 0),
    sigmaX=SCENE_BLUR_LEFT,
    sigmaY=SCENE_BLUR_LEFT
)


# ============================================================
# 6. FUSIONAR TODO EN UN SOLO CAMPO DE RELIEVE
# ============================================================

relieve_final = np.zeros((alto_total, ancho_total), dtype=np.uint8)

relieve_final[mascara_muro] = relieve_muro[mascara_muro]
relieve_final[mascara_mesa] = relieve_mesa[mascara_mesa]
relieve_final[mascara_izquierda] = relieve_izquierda[mascara_izquierda]
relieve_final[mascara_pelota] = relieve_pelota[mascara_pelota]


# ============================================================
# 7. SUAVIZAR LEVEMENTE LA TRANSICIÓN ENTRE ZONAS
# ============================================================

relieve_final = cv2.GaussianBlur(
    relieve_final,
    (0, 0),
    sigmaX=2,
    sigmaY=2
)


# ============================================================
# 8. EXTRAER CURVAS TOPOGRÁFICAS
# ============================================================

minimo = np.percentile(relieve_final, 6)
maximo = np.percentile(relieve_final, 94)

niveles = np.linspace(minimo, maximo, N_LEVELS)

resultado = Image.new("RGB", (ancho_total, alto_total), BACKGROUND_COLOR)
dibujo = ImageDraw.Draw(resultado)

for nivel in niveles:
    curvas = measure.find_contours(relieve_final, nivel)

    for curva in curvas:
        if len(curva) < 35:
            continue

        puntos = [(float(p[1]), float(p[0])) for p in curva]
        dibujo.line(puntos, fill=LINE_COLOR, width=LINE_WIDTH)


# ============================================================
# 9. OPCIONAL: BORDE DE LA PELOTA
# ============================================================

if DRAW_BALL_BORDER:
    dibujo.ellipse(
        (cx - radio, cy - radio, cx + radio, cy + radio),
        outline=LINE_COLOR,
        width=2
    )


# ============================================================
# 10. GUARDAR
# ============================================================

resultado.save(OUTPUT_IMAGE)
Image.fromarray(relieve_final).save(OUTPUT_RELIEF)

print("\nListo.")
print(f"Imagen final: {OUTPUT_IMAGE}")
print(f"Relieve usado: {OUTPUT_RELIEF}")
