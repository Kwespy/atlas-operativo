---
lang: en
---

# OB_029_Barrido_Oscilatorio_por_Luminancia

## Status
Status:: [[En revisión|Under review]]

---

## 1. Operation Data

**Internal number:** OB_029  
**Operational regime:** [[Lista_Traduccion_Sistemas_Representacion|Lista Traduccion Sistemas Representacion]]  
**Source image:** Digital photograph

**Operational description:**  
A raster digital photograph is converted into a single linear path that traverses the frame in a serpentine manner. The luminance of each zone ceases to be expressed as tone and instead controls the amplitude and local frequency of the oscillation.

Although the procedure is executed via an algorithm, the main regime is translation: the two-dimensional matrix of pixels becomes a continuous graphic signal. The image is no longer composed of color surfaces, but by the behavior of a line.

---

## 2. Tools

**Tools / medium:**

- Python
- Pillow
- Luminance sampling
- Raster path drawing

**Script:** [[OB029_barrido_oscilatorio_luminancia.py|OB029 barrido oscilatorio luminancia.py]]  
**Dependencies:** [[requirements.txt|requirements.txt]]  
**Test note:** [[OB029_NOTA.md|OB029 NOTA.md]]  
**Parameters by result:** [[OB029_PARAMETROS_RESULTADOS.txt|OB029 PARAMETROS RESULTADOS.txt]]

---

## 3. Procedure and Variables

**Procedure:**

1. Read the photograph respecting its technical EXIF orientation.
2. Temporarily reduce it to a lower-resolution luminance matrix.
3. Traverse the matrix row by row, alternating direction to build a continuous serpentine.
4. Convert the darkness of each sample into the amplitude and frequency of the oscillation.
5. Draw all points as a single line on a uniform background.
6. Maintain the original image dimensions in the result.

**Controlled variables:**

- Horizontal sampling resolution
- Maximum oscillation amplitude
- Base frequency
- Additional frequency produced by darkness
- Line thickness and color
- Background color

**Uncontrolled / accidental variables:**

- Intersections between contiguous rows
- Local accumulation of line
- Appearance and disappearance of silhouettes
- Ambiguous reading between signal, screen, and photograph
- Shapes produced by the global continuity of the path

---

## 4. Visual Sequence

The entry uses only the historical results produced with the ball image. The tree tests are preserved within `029_PROCESO/resultados`, but do not form part of this sequence.

### Step 01
![[OB029_step01.png.webp|200]]

### Step 02
![[OB029_step02.png.webp|200]]

### Step 03
![[OB029_step03.png.webp|200]]

### Step 04
![[OB029_step04.png.webp|200]]

### Step 05
![[OB029_step05.png.webp|200]]

### Step 06
![[OB029_step06.png.webp|200]]

### Step 07
![[OB029_step07.png.webp|200]]

### Step 08
![[OB029_step08.png.webp|200]]

### Step 09
![[OB029_step09.png.webp|200]]

### Step 10
![[OB029_step10.png.webp|200]]

### Step 11
![[OB029_step11.png.webp|200]]

### Step 12
![[OB029_step12.png.webp|200]]

### Step 13
![[OB029_step13.png.webp|200]]

### Step 14
![[OB029_step14.png.webp|200]]

### Step 15
![[OB029_step15.png.webp|200]]

### Step 16
![[OB029_step16.png.webp|200]]

### Step 17
![[OB029_step17.png.webp|200]]

### Step 18
![[OB029_step18.png.webp|200]]

---

## 5. Visual Selection

### Crisis / threshold according to AI-assisted reading / ChatGPT

Pending selection within the ball sequence.

### Crisis / threshold according to my perception

Pending selection.

---

## 6. Crisis and Formal-Perceptual Reading

**The operation affects the surface, tone, contour, figure-ground, legibility, and support of the image:**

The photograph remains recoverable through densities, amplitude changes, and line intersections, but it disappears as a continuous tonal surface. The crisis appears when the ball still emerges as a volume or silhouette while, at the same time, the gaze first recognizes an autonomous oscillatory signal.

The visual support shifts from a pixel matrix to a single path: each point depends on the previous one, and the complete image is subordinated to the temporal continuity of the sweep.

---

## 7. Final Evaluation and Artistic Reference

**Operation notes / what I learned:**  
Luminance can retain figurative information without being represented as gray. When translated into linear movement, the image simultaneously approximates a graph, a signal, and a continuous drawing.

**Final_status:**  
Works:: [[SI|SI]]

**How it destroys the image:**  
Works_on:: [[Formal|Formal]]

**Level and richness of crisis:**  
Crisis:: [[Pendiente|Pending]]

**Decision:**  
Selection:: [[Revisar|Revisar]]

---

### Possible artistic reference

Reference:: [[Pendiente|Pending]]
