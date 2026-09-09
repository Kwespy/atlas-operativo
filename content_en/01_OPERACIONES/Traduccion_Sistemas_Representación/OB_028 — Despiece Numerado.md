---
title: "OB_028 — Numbered Exploded View"
atlas_direct: true
lang: en
---

# OB_028_Despiece_Numerado

## Status
Status:: [[En revisión|Under review]]

---

## 1. Operation data

**Internal number:** OB_028  
**Operational regime:** [[Lista_Traduccion_Sistemas_Representacion|Lista Traduccion Sistemas Representacion]]  
**Source image:** Digital photograph

**Operational description:**  
A digital photograph is segmented into regions and translated into the visual language of a technical exploded view. Each region retains its photographic pixels, but begins to function as a separate and potentially identifiable part through contours, assembly lines, marks, and numbering.

The mediation is algorithmic, but the primary regime is one of translation: the image ceases to present itself as a continuous photographic surface and begins to be read as a component diagram.

---

## 2. Tools

**Tools / medium:**

- Python
- OpenCV
- NumPy
- scikit-image, SLIC segmentation

**Script:** [[OB028_despiece_numerado.py|OB028 despiece numerado.py]]  
**Dependencies:** [[requirements.txt|requirements.txt]]  
**Test note:** [[OB028_NOTA.md|OB028 NOTA.md]]  
**Parameters per result:** [[OB028_PARAMETROS_RESULTADOS.txt|OB028 PARAMETROS RESULTADOS.txt]]

---

## 3. Procedure and variables

**Procedure:**

1. Proportionally reduce the image to speed up processing.
2. Segment the photograph into visual regions.
3. Extract the pixels corresponding to each region.
4. Calculate a displacement direction and distance for each part.
5. Distribute the parts across quantized directions and layers.
6. Optionally incorporate contours, lines, origin points, and numbering.
7. Crop excess outer space without eliminating parts.

**Controlled variables:**

- Approximate number of parts
- Compactness and smoothing of the segmentation
- Explosion distance and variation
- Number of directions and layers
- Presence of ghost image
- Guide lines, contours, marks, and numbering
- Maximum processing size

**Uncontrolled / accidental variables:**

- Specific shape of the detected regions
- Voids produced between parts
- Overlaps and accumulations between parts and lines
- Degree of local recognition of each fragment
- Mental reconstruction performed by the observer

---

## 4. Visual sequence

### Initial image
![[Input_003.jpeg|200]]

### Step 01
![[OB028_step01.jpg.webp|200]]

### Step 02
![[OB028_step02.jpg.webp|200]]

### Step 03
![[OB028_step03.jpg.webp|200]]

### Step 04
![[OB028_step04.jpg.webp|200]]

### Step 05
![[OB028_step05.jpg.webp|200]]

### Step 06
![[OB028_step06.jpg.webp|200]]

### Step 07
![[OB028_step07.jpg.webp|200]]

### Step 08
![[OB028_step08.jpg.webp|200]]

### Step 09
![[OB028_step09.jpg.webp|200]]

### Step 10
![[OB028_step10.jpg.webp|200]]

### Step 11
![[OB028_step11.jpg.webp|200]]

### Step 12
![[OB028_step12.jpg.webp|200]]

### Step 13
![[OB028_step13.jpg.webp|200]]

### Step 14
![[OB028_step14.jpg.webp|200]]

### Step 15
![[OB028_step15.jpg.webp|200]]

### Step 16
![[OB028_step16.jpg.webp|200]]

---

## 5. Visual selection

### Crisis / threshold according to AI-assisted reading / ChatGPT

Pending review of the complete sequence.

### Crisis / threshold according to my perception

Pending selection.

---

## 6. Crisis and formal-perceptual reading

**The operation affects continuity, position, the relationship between part and whole, recognition, and the reading of the support:**

The parts remain photographic and retain recognizable information from the original technical image, but they no longer occupy a continuous surface. The scene oscillates between photograph and assembly diagram: it can be mentally reconstructed, although its unity is subordinated to the reading of separate, numbered, and displaced components.

The crisis appears when the parts still allow the photographic origin to be recognized, but the whole is perceived first as an inventory, diagram, or technical manual.

---

## 7. Final evaluation and artistic reference

**Operation notes / what I learned:**  
The algorithm alone does not constitute the regime of the operation. Segmentation and displacement are means to translate a raster photograph into the representation system of a numbered technical exploded view.

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
