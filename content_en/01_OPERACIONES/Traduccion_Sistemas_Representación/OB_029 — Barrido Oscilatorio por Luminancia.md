---
title: "OB_029 — Oscillatory Luminance Sweep"
atlas_direct: true
lang: en
---

# OB_029_Oscillatory_Luminance_Sweep

## Status
Status:: [[En revisión|Under review]]

---

## 1. Operation data

**Internal number:** OB_029  
**Operational regime:** [[Lista_Traduccion_Sistemas_Representacion|Lista Traduccion Sistemas Representacion]]  
**Source image:** Digital photograph

**Operational description:**  
A raster digital photograph is converted into a single linear path that moves across the frame in a serpentine pattern. The luminance of each area is no longer expressed as a tone, instead controlling the local amplitude and frequency of the oscillation.

Although the procedure is executed through an algorithm, the main regime is translation: the two-dimensional pixel matrix becomes a continuous graphic signal. The image is no longer composed of color surfaces, but by the behavior of a line.

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

## 3. Procedure and variables

**Procedure:**

1. Read the photograph respecting its technical EXIF orientation.
2. Temporarily reduce it to a lower-resolution luminance matrix.
3. Traverse the matrix row by row, alternating directions to build a continuous serpentine pattern.
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

- Crossings between adjacent rows
- Local accumulation of line
- Appearance and disappearance of silhouettes
- Ambiguous reading between signal, raster, and photograph
- Shapes produced by the global continuity of the path

---

## 4. Visual sequence

This file uses exclusively the historical results made with the ball image. The tree tests are kept inside `029_PROCESO/resultados`, but do not form part of this sequence.

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

## 5. Visual selection

### Crisis / threshold according to AI-assisted reading / ChatGPT

Pending selection within the ball sequence.

### Crisis / threshold according to my perception

Pending selection.

---

## 6. Crisis and formal-perceptual reading

**The operation affects the surface, tone, contour, figure-ground, legibility, and support of the image:**

The photograph remains recoverable through densities, amplitude changes, and line crossings, but it disappears as a continuous tonal surface. The crisis occurs when the ball still emerges as a volume or silhouette while, at the same time, the gaze first recognizes an autonomous oscillatory signal.

The visual support shifts from a pixel matrix to a single path: each point depends on the previous one, and the complete image is subordinated to the temporal continuity of the sweep.

---

## 7. Final evaluation and artistic reference

**Operation notes / what I learned:**  
Luminance can retain figurative information without being represented as gray. When translated into linear movement, the image simultaneously approximates a graph, a signal, and a continuous drawing.

**Final_status:**  
Works:: [[SI|YES]]

**How it destroys the image:**  
Works_on:: [[Formal|Formal]]

**Level and richness of crisis:**  
Crisis:: [[Pendiente|Pending]]

**Decision:**  
Selection:: [[Revisar|Review]]

---

### Possible artistic reference

Reference:: [[Pendiente|Pending]]
