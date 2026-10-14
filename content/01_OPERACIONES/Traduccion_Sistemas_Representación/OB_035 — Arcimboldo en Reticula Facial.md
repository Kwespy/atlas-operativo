---
title: "OB_035 — Arcimboldo en Reticula Facial"
atlas_direct: true
---

# OB_035 — Arcimboldo en retícula facial

## Estado

Estado:: [[En revisión]]

---

## 1. Datos de la operación

**Número interno:** OB_035  
**Régimen operativo:** [[Lista_Traduccion_Sistemas_Representación]]  
**Imagen de origen:** Fotografía digital — retrato frontal ([[Input_005.jpeg.webp]])

**Descripción operativa:**  
El retrato se traduce a una topología de 468 puntos de referencia faciales, nodos de contorno y una triangulación de Delaunay. Cada celda recibe una pieza de un corpus de fragmentos corporales, deformada mediante una transformación afín según su geometría. En la versión actual se conservan los ojos, el pelo, la ropa y el fondo de la fotografía; la piel queda reconstruida con el corpus.

**Familia:** fotografía → topología triangular → reconstrucción con corpus corporal.

---

## 2. Herramientas

**Herramientas / medio:**

- Python
- NumPy y OpenCV
- MediaPipe Face Landmarker y Selfie Segmentation
- Corpus de 32 recortes fotográficos transparentes de partes del cuerpo

**Script:** `OB035_arcimboldo_reticula_facial.py`.  
**Parámetros por resultado:** están en los metadatos de cada imagen (EXIF, campo *ImageDescription*).

---

## 3. Procedimiento y variables

**Procedimiento:**

1. Detectar 468 landmarks del rostro y segmentar la silueta.
2. Construir una red triangular facial y completar la figura mediante Delaunay.
3. Asignar y deformar una pieza corporal del corpus en cada triángulo.
4. Conservar ojos, pelo, ropa y fondo originales como capas protegidas.
5. Rellenar las celdas para impedir vacíos negros o transparentes dentro de la retícula.

**Variables controladas:**

- Densidad de la malla interior y nodos del contorno.
- Umbral de segmentación y separación figura-fondo.
- Semilla y modo de asignación del corpus.
- Protección de ojos, pelo, ropa y fondo.
- Relleno de celdas, borde difuso e interpolación.

**Variables no controladas / accidentales:**

- Aparición de fragmentos anatómicos reconocibles en escalas incompatibles.
- Continuidades falsas entre piezas corporales de procedencias distintas.
- Bordes que la malla comparte con pelo, orejas, cuello o ropa.

---

## 4. Secuencia visual

Todos los steps provienen de [[Input_005.jpeg.webp]]. El orden es cronológico; los parámetros de cada resultado están en sus metadatos.

|  |  |  |
| --- | --- | --- |
| Imagen inicial<br>![[Input_005.jpeg.webp\|180]] | Step 01<br>![[OB035_step01.jpeg.webp\|180]] | Step 02<br>![[OB035_step02.jpeg.webp\|180]] |
| Step 03<br>![[OB035_step03.jpeg.webp\|180]] | Step 04<br>![[OB035_step04.jpeg.webp\|180]] | Step 05<br>![[OB035_step05.jpeg.webp\|180]] |
| Step 06<br>![[OB035_step06.jpeg.webp\|180]] | Step 07<br>![[OB035_step07.jpeg.webp\|180]] | Step 08<br>![[OB035_step08.jpeg.webp\|180]] |
| Step 09<br>![[OB035_step09.jpeg.webp\|180]] | Step 10<br>![[OB035_step10.jpeg.webp\|180]] | Step 11<br>![[OB035_step11.png.webp\|180]] |
| Step 12<br>![[OB035_step12.png.webp\|180]] | Step 13<br>![[OB035_step13.jpeg.webp\|180]] | Step 14<br>![[OB035_step14.jpeg.webp\|180]] |
| Step 15<br>![[OB035_step15.jpeg.webp\|180]] | Step 16<br>![[OB035_step16.jpeg.webp\|180]] |  |

---

## 5. Selección visual

### Crisis / umbral según lectura asistida por IA

Pendiente.

### Crisis / umbral según mi percepción

Pendiente.

---

## 6. Crisis y lectura formal-perceptiva

La operación conserva la organización espacial del retrato, pero reemplaza la materia que produce su reconocimiento: la piel pasa a ser un campo de manos, pies, articulaciones y otros fragmentos corporales. La tensión aparece entre la continuidad de la retícula y la discontinuidad anatómica de cada pieza; el rostro sigue siendo legible por su topología aunque su superficie ya no le pertenezca.

La conservación de ojos, pelo, ropa y fondo sostiene zonas de reconocimiento mientras la piel se vuelve un ensamblaje corporal ajeno. El lugar de crisis queda pendiente de selección perceptiva.

---

## 7. Evaluación final y referente artístico

**Notas de la operación / qué aprendí:**  
Pendiente.

**Estado_final:**  
Funciona:: Pendiente

**Cómo destruye la imagen:**  
Trabaja_en_lo:: Pendiente

**Nivel y riqueza de crisis:**  
Crisis:: Pendiente

**Decisión:**  
Seleccion:: Pendiente

### Referente artístico posible

Referente:: Pendiente

**Obras posibles:**  
Pendiente.
