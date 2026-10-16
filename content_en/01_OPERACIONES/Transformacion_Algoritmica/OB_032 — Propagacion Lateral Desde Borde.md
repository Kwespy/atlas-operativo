---
title: "OB_032 — Lateral Propagation From Edge"
atlas_direct: true
lang: en
---

# OB_032_Lateral_Propagation_From_Edge

## Status
Status:: [[Terminada|Finished]]

---

## 1. Operation Data

**Internal number:** OB_032  
**Operational regime:** [[Lista_Transformacion_Algoritmica|Algorithmic Transformation List]]  
**Source image:** Digital photograph — frontal portrait ([[Input_005.jpeg.webp|Input 005.jpeg.webp]])

**Operational description:**  
Each edge pixel stops functioning as a boundary and begins functioning as a source: it emits a straight trace copying pre-existing color from the image, taken a few pixels behind the edge, and drags it into the neighboring region. The length of the trace is not random: it is fixed by the image itself through the strength of the gradient, luminance, or local saturation. Only a percentage of the edges emit.

The contour, which used to separate figure from background, becomes the origin of the invasion: the color on one side of the edge crosses over to the other. Color is never invented, only copied and displaced. The only randomness is which edges emit, determined by a seed.

**Family:** directional drag from detected contours. The closest precedent is experiment `Propagacion_de_bordes`, which dilates color from the edges isotropically, like a stain growing in all directions. Here, however, propagation is directional and of variable length: each edge drags in a single direction, according to its gradient.

---

## 2. Tools

**Tools / medium:**

- Python
- NumPy
- OpenCV
- Edge detection (Canny or Sobel)
- Line tracing along the gradient

**Script:** `OB032_propagacion_lateral_desde_borde.py`. Includes instructions inside on how to run it and what it requires.  
**Parameters per result:** found in the metadata of each image (*ImageDescription* EXIF field).

---

## 3. Procedure and Variables

**Procedure:**

1. Read the photograph and smooth it with a Gaussian blur.
2. Detect edges using Canny (fine and selective) or Sobel (all high-gradient zones).
3. Discard edges with gradient strength below a minimum threshold.
4. Randomly choose, using a fixed seed, the percentage of edges that will emit.
5. For each emitter, sample the color a few pixels behind the edge.
6. Draw a straight line from the edge in the chosen direction (horizontal, vertical, along the gradient, or parallel to the contour), with a length proportional to the modulator and an opacity that fades towards the end.
7. Preserve the original dimensions of the image.

**Controlled variables:**

- Edge detection method and thresholds
- Prior smoothing
- Minimum edge strength
- Property determining length (gradient, luminance, saturation)
- Drag direction
- Minimum and maximum trace length
- Trace opacity and decay
- Percentage of emitting edges
- Source color sampling distance
- Protected region and final blending with the original

**Uncontrolled / accidental variables:**

- Convergent trace bundles when many neighboring edges share the same orientation
- Radial halo around the head: hair, as the highest contrast zone, emits outward in all directions
- Traces crossing the entire image and leaving the frame
- Veil effect: the overlap of many fine traces reveals the figure underneath as if through a screen
- Material differences depending on the color origin (dark traces from hair, light from background, warm from skin)

---

## 4. Visual Sequence

All steps originate from [[Input_005.jpeg.webp|Input 005.jpeg.webp]]. The order is chronological, and the parameters for each can be found in its image metadata.

Steps 01–02 test horizontal drag with short traces. Steps 03–06 shift to drag along the gradient with long traces and few emitters. Steps 07–17 sweep the detection threshold, emitter percentage, and minimum length along that same direction.

### Initial image
![[Input_005.jpeg.webp|200]]

### Step 01
![[OB032_step01.jpeg.webp|200]]

### Step 02
![[OB032_step02.jpeg.webp|200]]

### Step 03
![[OB032_step03.jpeg.webp|200]]

### Step 04
![[OB032_step04.jpeg.webp|200]]

### Step 05
![[OB032_step05.jpeg.webp|200]]

### Step 06
![[OB032_step06.jpeg.webp|200]]

### Step 07
![[OB032_step07.jpeg.webp|200]]

### Step 08
![[OB032_step08.jpeg.webp|200]]

### Step 09
![[OB032_step09.jpeg.webp|200]]

### Step 10
![[OB032_step10.jpeg.webp|200]]

### Step 11
![[OB032_step11.jpeg.webp|200]]

### Step 12
![[OB032_step12.jpeg.webp|200]]

### Step 13
![[OB032_step13.jpeg.webp|200]]

### Step 14
![[OB032_step14.jpeg.webp|200]]

### Step 15
![[OB032_step15.jpeg.webp|200]]

### Step 16
![[OB032_step16.jpeg.webp|200]]

### Step 17
![[OB032_step17.jpeg.webp|200]]

---

## 5. Visual Selection

### Crisis / threshold according to AI-assisted reading

### Step 16
![[OB032_step16.jpeg.webp]]



### Crisis / threshold according to my perception

### Step 09
![[OB032_step09.jpeg.webp]]

---

## 6. Crisis and Formal-Perceptual Reading

**The operation affects the contour, figure-ground relationship, color, and legibility of the image:**

The operation acts precisely upon the location where the image separates figure from background. The contour is not erased: edge pixels do not overwrite themselves, so the drawing survives. What is lost is its containment function, as each edge becomes a vanishing point from which matter flows outward or inward.

With few emitters, the image reads as a photograph with lines superimposed: the two layers do not touch. With too many, the traces form a homogeneous hairstyle that obscures the figure. In the intermediate zone, the traces overlap until they become a veil, and the face is read through its own displaced color. Hair, being the zone of highest contrast, emits more forcefully and turns into a radial halo: precisely the area that defined the boundary of the head is the first to lose its edge.

---

## 7. Final Evaluation and Artistic Reference

**Operation notes / what I learned:**  
The parameter driving the reading is not the length of the traces but how many edges emit. With traces over 800 px, the detection threshold alone decides whether the image remains stable (few threads) or collapses (a mass). Minimum length and emitter percentage are what allow one to stay at the intermediate point.

The filename generated by the script prior to cataloging did not include detection thresholds, so separate runs ended up with the same name. Actual parameters for each were retrieved from the experimentation log and saved in the metadata of each step.

**Final_status:**  
Works:: [[SI|YES]]

**How it destroys the image:**  
Works_on:: [[Configurativo|Configurative]]

**Level and richness of crisis:**  
Crisis:: [[Media|Medium]]

**Decision:**  
Selection:: [[Combinable|Combinable]]

---

### Potential Artistic Reference

Reference:: [[Arnulf Rainer|Arnulf Rainer]], [[Kumi Yamashita|Kumi Yamashita]], 

**Possible works:**  
- [Arnulf Rainer - Face Farces 1969](https://www.google.com/search?q=Arnulf+Rainer+Face+Farces+1969&udm=2)

- [Kumi Yamashita — _Constellation_, 2004]()
