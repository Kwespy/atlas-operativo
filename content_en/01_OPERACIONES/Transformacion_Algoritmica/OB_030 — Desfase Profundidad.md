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
Each pixel is displaced by a distance proportional to its estimated depth, in a fixed direction. It is a false parallax: it pretends that the photograph has volume and that the camera is moving sideways, but the depth does not come from any measurement of space — it is inferred from the image itself, from its luminance or from where it is in focus.

Since pixels of equal depth move together, with large amplitudes the image folds back on itself and the isolines of the map become visible: winding bands and concentric rings appear, the photograph reorganized as a contour map.

The color is never altered at all: no value changes, it only changes location.

---

## 2. Tools

**Tools / medium:**

- Python
- NumPy
- OpenCV
- Depth estimation by luminance or local sharpness
- Coordinate remap

**Script:** `OB030_desfase_profundidad.py`  
**Dependencies:** `requirements.txt`  
**Test note:** `OB030_NOTA.md`  
**Parameters by result:** `OB030_PARAMETROS_RESULTADOS.txt`

---

## 3. Procedure and variables

**Procedure:**

1. Read the photograph and convert it to luminance.
2. Build a depth map from that luminance (bright areas are taken as distant, following atmospheric haze) or from local detail (focused areas are taken as close).
3. Blur the map with a Gaussian, which defines the size of the resulting bands.
4. Optionally quantize the map into steps, to separate the image into discrete sheets.
5. Shift each pixel a distance proportional to its depth, in a fixed direction.
6. Fill in by reflection what the displacement leaves outside the frame.
7. Preserve the original dimensions of the image.

**Controlled variables:**

- Shift amplitude, as a fraction of the longer side
- Displacement direction in degrees
- Origin of depth (luminance, inverted luminance, sharpness)
- Depth map smoothing (sigma)
- Map quantization into levels
- Interpolation and border mode

**Uncontrolled / accidental variables:**

- Appearance of concentric rings where the map has local maxima
- Folding of the image back on itself
- Areas that empty out and are filled by reflection
- Ambiguous reading between photograph and topographic map
- Collision of different materials dragged into the same band

---

## 4. Visual sequence

The entry uses only the results produced with the tree image. The ball tests are kept inside `030_PROCESO/resultados/PELOTA_fuera_de_secuencia`, but are not part of this sequence.

Steps 01–10 are the historical sweep of August 7, 2026, of increasing amplitude. Steps 11–13 correspond to the reconstructed script and carry their documented parameters.

### Step 01
![[OB030_step01.jpg.webp|200]]

### Step 02
![[OB030_step02.jpg.webp|200]]

### Step 03
![[OB030_step03.jpg.webp|200]]

### Step 04
![[OB030_step04.jpg.webp|200]]

### Step 05
![[OB030_step05.jpg.webp|200]]

### Step 06
![[OB030_step06.jpg.webp|200]]

### Step 07
![[OB030_step07.jpg.webp|200]]

### Step 08
![[OB030_step08.jpg.webp|200]]

### Step 09
![[OB030_step09.jpg.webp|200]]

### Step 10
![[OB030_step10.jpg.webp|200]]

### Step 11
![[OB030_step11.jpeg.webp|200]]

### Step 12
![[OB030_step12.jpeg.webp|200]]

### Step 13
![[OB030_step13.jpeg.webp|200]]

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

The general organization survives: the sky above, the mass of the tree in the center, the ground below, and the colors exactly where they were, because no color value is modified. What is lost is the correspondence between the matter and what it describes: each zone becomes a fabric of bands that no longer accounts for what was there.

The crisis appears when the eye reads a subject and a topographic map at the same time and cannot decide which of the two it is looking at. The image begins to inform about its own light distribution rather than informing about the scene: the visible bands are the isolines of the depth map of this particular photograph, and no other image would produce the same ones.

The contour erodes without being erased: it does not disappear, it stretches and folds, and at the local maxima of the map it closes in on itself forming rings.

---

## 7. Final evaluation and artistic reference

**Operation notes / what I learned:**  
Depth can be manufactured from the image itself and function equally as a deformation structure. The result does not depend on the depth being correct, but on it being consistent: it is enough for pixels of equal value to move together for cartography to appear.

The original script for this operation was lost and had to be reconstructed by measuring the displacement field of the historical outputs. That left a lesson in method: without the script and without the parameters in the filename, a result is not reproducible even if the image is preserved.

**Final_status:**  
Works:: [[SI|YES]]

**How it destroys the image:**  
Works_on:: [[Aparencial|Appurtenant]]

**Level and richness of crisis:**  
Crisis:: [[Baja|Low]]

**Decision:**  
Selection:: [[Guardar|Keep]] [[Combinable|Combinable]]

---

### Possible artistic reference

Reference:: [[Roberto Matta|Roberto Matta]], [[Vincent van Gogh|Vincent van Gogh]], [[Alex McAdoo|Alex McAdoo]]

**Possible works:**  
- [Roberto Matta — _Invasion of the Night_](https://www.google.com/search?q=Roberto+Matta+Invasion+of+the+Night&udm=2#sv=CAMSURoyKhBlLW1FWjlNRE5GQjNEUVFNMg5tRVo5TURORkIzRFFRTToOZnp5Nk5zeHFRY0pKb00gBCoXCgFzEhBlLW1FWjlNRE5GQjNEUVFNGAEwARgHIKqm5ckKSggQAhgBIAIoAQ)

- [Vincent van Gogh — _The Starry Night_](https://www.google.com/search?q=Vincent+van+Gogh+La+noche+estrellada&udm=2)

- [Alex McAdoo - Cowgill Ave](https://www.google.com/search?q=Alex+McAdoo+Cowgill+Ave&udm=2)
