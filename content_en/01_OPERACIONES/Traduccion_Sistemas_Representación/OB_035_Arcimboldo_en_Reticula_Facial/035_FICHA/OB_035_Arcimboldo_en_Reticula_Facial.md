---
lang: en
---

# OB_035 — Arcimboldo in a facial grid

## Status

Status:: [[En revisión|In review]]

---

## 1. Operation data

**Internal number:** OB_035  
**Operational regime:** [[Lista_Traduccion_Sistemas_Representación|Representation Systems Translation List]]  
**Source image:** Digital photograph — frontal portrait ([[Input_005.jpeg.webp|Input 005.jpeg.webp]])

**Operational description:**  
The portrait is translated into a topology of 468 facial landmarks, contour nodes, and a Delaunay triangulation. Each cell receives a piece from a corpus of body fragments, deformed via an affine transformation according to its geometry. In the current version, the eyes, hair, clothing, and background of the photograph are preserved; the skin is reconstructed using the corpus.

**Family:** photograph → triangular topology → body corpus reconstruction.

---

## 2. Tools

**Tools / medium:**

- Python
- NumPy and OpenCV
- MediaPipe Face Landmarker and Selfie Segmentation
- Corpus of 32 transparent photographic cutouts of body parts

**Script:** `OB035_arcimboldo_reticula_facial.py`.  
**Parameters per result:** found in the metadata of each image (EXIF, *ImageDescription* field).

---

## 3. Procedure and variables

**Procedure:**

1. Detect 468 facial landmarks and segment the silhouette.
2. Build a facial triangular network and complete the figure using Delaunay.
3. Assign and deform a body piece from the corpus in each triangle.
4. Preserve the original eyes, hair, clothing, and background as protected layers.
5. Fill the cells to prevent black or transparent voids within the grid.

**Controlled variables:**

- Density of the inner mesh and contour nodes.
- Segmentation threshold and figure-ground separation.
- Corpus seed and assignment mode.
- Protection of eyes, hair, clothing, and background.
- Cell filling, feathered edge, and interpolation.

**Uncontrolled / accidental variables:**

- Emergence of recognizable anatomical fragments at incompatible scales.
- False continuities between body pieces from different origins.
- Edges shared by the mesh with hair, ears, neck, or clothing.

---

## 4. Visual sequence

All steps originate from [[Input_005.jpeg.webp|Input 005.jpeg.webp]]. The order is chronological; the parameters for each result are in their metadata.

|  |  |  |
| --- | --- | --- |
| Initial image<br>![[Input_005.jpeg.webp\|180]] | Step 01<br>![[OB035_step01.jpeg.webp\|180]] | Step 02<br>![[OB035_step02.jpeg.webp\|180]] |
| Step 03<br>![[OB035_step03.jpeg.webp\|180]] | Step 04<br>![[OB035_step04.jpeg.webp\|180]] | Step 05<br>![[OB035_step05.jpeg.webp\|180]] |
| Step 06<br>![[OB035_step06.jpeg.webp\|180]] | Step 07<br>![[OB035_step07.jpeg.webp\|180]] | Step 08<br>![[OB035_step08.jpeg.webp\|180]] |
| Step 09<br>![[OB035_step09.jpeg.webp\|180]] | Step 10<br>![[OB035_step10.jpeg.webp\|180]] | Step 11<br>![[OB035_step11.png.webp\|180]] |
| Step 12<br>![[OB035_step12.png.webp\|180]] | Step 13<br>![[OB035_step13.jpeg.webp\|180]] | Step 14<br>![[OB035_step14.jpeg.webp\|180]] |
| Step 15<br>![[OB035_step15.jpeg.webp\|180]] | Step 16<br>![[OB035_step16.jpeg.webp\|180]] |  |

---

## 5. Visual selection

### Crisis / threshold according to AI-assisted reading

Pending.

### Crisis / threshold according to my perception

Pending.

---

## 6. Crisis and formal-perceptual reading

The operation preserves the spatial organization of the portrait, but replaces the matter that produces its recognition: the skin becomes a field of hands, feet, joints, and other body fragments. Tension arises between the continuity of the grid and the anatomical discontinuity of each piece; the face remains legible through its topology even though its surface no longer belongs to it.

The preservation of the eyes, hair, clothing, and background maintains areas of recognition while the skin turns into an alien body assemblage. The locus of crisis remains pending perceptual selection.

---

## 7. Final evaluation and artistic reference

**Operation notes / what I learned:**  
Pending.

**Final_status:**  
Works:: Pending

**How it destroys the image:**  
Works_on:: Pending

**Level and richness of crisis:**  
Crisis:: Pending

**Decision:**  
Selection:: Pending

### Possible artistic reference

Reference:: Pending

**Possible works:**  
Pending.
