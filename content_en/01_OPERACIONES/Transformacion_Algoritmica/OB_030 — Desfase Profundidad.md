---
title: "OB_030 — Depth Shift"
atlas_direct: true
lang: en
---

# OB_030_Depth_Shift

## Status
Status:: [[Terminada|Finished]]

---

## 1. Operation data

**Internal number:** OB_030  
**Operational regime:** [[Lista_Transformacion_Algoritmica|Algorithmic Transformation List]]  
**Source image:** Digital photograph

**Operational description:**  
Each pixel is shifted by a distance proportional to its estimated depth, in a fixed direction. This is a false parallax: it pretends that the photograph has volume and that the camera is moving sideways, but the depth does not come from any measurement of space — it is inferred from the image itself, from its luminance, or from where it is in focus.

Since pixels of equal depth move together, with large amplitudes the image folds back on itself and the isolines of the map become visible: winding bands and concentric rings appear, the photograph reorganized as a contour line map.

The color is not altered at any time: no value changes, only its location.

---

## 2. Tools

**Tools / medium:**

- Python
- NumPy
- OpenCV
- Depth estimation by luminance or local sharpness
- Coordinate remapping

**Script:** `OB030_desfase_profundidad.py`  
**Dependencies:** `requirements.txt`  
**Test note:** `OB030_NOTA.md`  
**Parameters per result:** `OB030_PARAMETROS_RESULTADOS.txt`

---

## 3. Procedure and variables

**Procedure:**

1. Read the photograph and convert it to luminance.
2. Build a depth map from that luminance (lighter areas are taken as distant, following atmospheric haze) or from local detail (in-focus areas are taken as close).
3. Blur the map with a Gaussian, which defines the size of the resulting bands.
4. Optionally quantize the map into steps, to separate the image into discrete layers.
5. Shift each pixel a distance proportional to its depth, in a fixed direction.
6. Fill in what the shift leaves out of frame using reflection.
7. Preserve the original dimensions of the image.

**Controlled variables:**

- Shift amplitude, as a fraction of the longer side
- Displacement direction in degrees
- Depth origin (luminance, inverted luminance, sharpness)
- Depth map smoothing (sigma)
- Map quantization into levels
- Interpolation and edge mode

**Uncontrolled / accidental variables:**

- Appearance of concentric rings where the map has local maxima
- Folding of the image over itself
- Areas that are emptied and filled via reflection
- Ambiguous reading between photograph and topographic map
- Collision of different materials dragged into the same band

---

## 4. Visual sequence

The file uses exclusively the results made with the tree image. The ball tests are kept inside `030_PROCESO/resultados/PELOTA_fuera_de_secuencia`, but are not part of this sequence.

Steps 01–10 are the historical sweep of August 7, 2026, of increasing amplitude. Steps 11–13 correspond to the reconstructed script and carry their documented parameters.

| | | |
| --- | --- | --- |
| Step 01<br>![[OB030_step01.jpg.webp\|200]] | Step 02<br>![[OB030_step02.jpg.webp\|200]] | Step 03<br>![[OB030_step03.jpg.webp\|200]] |
| Step 04<br>![[OB030_step04.jpg.webp\|200]] | Step 05<br>![[OB030_step05.jpg.webp\|200]] | Step 06<br>![[OB030_step06.jpg.webp\|200]] |
| Step 07<br>![[OB030_step07.jpg.webp\|200]] | Step 08<br>![[OB030_step08.jpg.webp\|200]] | Step 09<br>![[OB030_step09.jpg.webp\|200]] |
| Step 10<br>![[OB030_step10.jpg.webp\|200]] | Step 11<br>![[OB030_step11.jpeg.webp\|200]] | Step 12<br>![[OB030_step12.jpeg.webp\|200]] |
| Step 13<br>![[OB030_step13.jpeg.webp\|200]] |  |  |
---

## 5. Visual selection

### Crisis / threshold according to AI-assisted reading / ChatGPT

### Step 05
![[OB030_step05.jpg.webp]]

### Crisis / threshold according to my perception

### Step 06
![[OB030_step06.jpg.webp]]

---

## 6. Crisis and formal-perceptual reading

**The operation affects the surface, tone, contour, figure-ground, legibility, and support of the image:**

The general organization survives: the sky at the top, the mass of the tree in the center, the ground at the bottom, and the colors exactly where they were, because no color value is modified. What is lost is the correspondence between the matter and what it describes: each zone becomes a weave of bands that no longer accounts for what was there.

The crisis appears when the eye reads a subject and a topographic map at the same time and cannot decide which of the two it is looking at. The image begins to report on its own light distribution instead of reporting on the scene: the visible bands are the isolines of the depth map of this particular photograph, and no other image would produce the same ones.

The contour erodes without being erased: it does not disappear, it stretches and folds, and at the local maxima of the map it closes in on itself, forming rings.

---

## 7. Final evaluation and artistic reference

**Operation notes / what I learned:**  
Depth can be fabricated from the image itself and function identically as a deformation structure. The result does not depend on the depth being correct, but on it being consistent: it is enough for pixels of equal value to move together for cartography to appear.

The original script for this operation was lost and had to be reconstructed by measuring the displacement field of the historical outputs. That left a lesson in method: without the script and without the parameters in the filename, a result is not reproducible even if the image is preserved.

**Final_status:**  
Works:: [[SI|YES]]

**How it destroys the image:**  
Works_on:: [[Aparencial|Apparent]]

**Level and richness of crisis:**  
Crisis:: [[Baja|Low]]

**Decision:**  
Selection:: [[Guardar|Save]] [[Combinable|Combinable]]

---

### Possible artistic reference

Reference:: [[Roberto Matta|Roberto Matta]], [[Vincent van Gogh|Vincent van Gogh]], [[Alex McAdoo|Alex McAdoo]]

**Possible works:**  
- [Roberto Matta — _Invasion of the Night_](https://www.google.com/search?q=Roberto+Matta+Invasion+of+the+Night&udm=2#sv=CAMSURoyKhBlLW1FWjlNRE5GQjNEUVFNMg5tRVo5TURORkIzRFFRTToOZnp5Nk5zeHFRY0pKb00gBCoXCgFzEhBlLW1FWjlNRE5GQjNEUVFNGAEwARgHIKqm5ckKSggQAhgBIAIoAQ)

- [Vincent van Gogh — _The Starry Night_](https://www.google.com/search?q=Vincent+van+Gogh+La+noche+estrellada&udm=2)

- [Alex McAdoo - Cowgill Ave](https://www.google.com/search?q=Alex+McAdoo+Cowgill+Ave&udm=2)
