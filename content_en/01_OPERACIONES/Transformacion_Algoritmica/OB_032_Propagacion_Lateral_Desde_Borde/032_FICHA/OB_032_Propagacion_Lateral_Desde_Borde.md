---
lang: en
---

# OB_032_Lateral_Propagation_From_Edge

## Status
Status:: [[Terminada|Finished]]

---

## 1. Operation data

**Internal number:** OB_032  
**Operational regime:** [[Lista_Transformacion_Algoritmica|Algorithmic Transformation List]]  
**Source image:** Digital photograph — front portrait ([[Input_005.jpeg.webp|Input 005.jpeg.webp]])

**Operational description:**  
Every edge pixel stops functioning as a boundary and begins functioning as a source: it emits a straight trace that copies pre-existing color from the image, sampled a few pixels behind the edge, and drags it into the neighboring region. The length of the trace is not random: it is determined by the image itself, through the strength of the gradient, luminance, or local saturation. Only a percentage of the edges emit.

The outline, which separated the figure from the background, becomes the origin of the invasion: the color from one side of the edge crosses over to the other. The color is never invented, only copied and displaced. The only randomness is which edges emit, and that is fixed by a seed.

**Family:** directional drag from detected contours. The closest precedent is experiment `Propagacion_de_bordes`, which dilates color from the edges isotropically, like a stain growing in all directions. Here, by contrast, the propagation is directional and of variable length: each edge drags toward a single side, according to its gradient.

---

## 2. Tools

**Tools / medium:**

- Python
- NumPy
- OpenCV
- Edge detection (Canny or Sobel)
- Line plotting along the gradient

**Script:** `OB032_propagacion_lateral_desde_borde.py`. Explains inside how to run it and what it requires.  
**Parameters per result:** found in the metadata of each image (EXIF, *ImageDescription* field).

---

## 3. Procedure and variables

**Procedure:**

1. Read the photograph and smooth it with a Gaussian blur.
2. Detect edges using Canny (fine and selective) or Sobel (every high-gradient zone).
3. Discard edges with a gradient strength lower than a minimum threshold.
4. Choose at random, using a fixed seed, the percentage of emitting edges.
5. For each emitter, sample the color a few pixels behind the edge.
6. Plot a straight line from the edge in the chosen direction (horizontal, vertical, along the gradient, or parallel to the contour), with a length proportional to the modulator and an opacity that fades toward the end.
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
- Sampling distance for the source color
- Protected region and final blending with the original

**Uncontrolled / accidental variables:**

- Bundles of converging traces when many neighboring edges share the same orientation
- Radial halo around the head: the hair, as the zone of highest contrast, emits outward in all directions
- Traces that cross the entire image and leave the frame
- Veiling: the overlapping of many fine traces reveals the figure underneath as if through a weave
- Material differences depending on the origin of the color (dark traces from hair, light from the background, warm from skin)

---

## 4. Visual sequence

All steps originate from [[Input_005.jpeg.webp|Input 005.jpeg.webp]]. The order is chronological, and the parameters for each step are found in its image metadata.

Steps 01–02 test horizontal drag with short traces. Steps 03–06 switch to drag along the gradient with long traces and few emitters. Steps 07–17 sweep the detection threshold, the percentage of emitters, and the minimum length along that same direction.

### Initial image
![[Input_005.jpeg.webp|200]]

| | | |
| --- | --- | --- |
| Step 01<br>![[OB032_step01.jpeg.webp\|200]] | Step 02<br>![[OB032_step02.jpeg.webp\|200]] | Step 03<br>![[OB032_step03.jpeg.webp\|200]] |
| Step 04<br>![[OB032_step04.jpeg.webp\|200]] | Step 05<br>![[OB032_step05.jpeg.webp\|200]] | Step 06<br>![[OB032_step06.jpeg.webp\|200]] |
| Step 07<br>![[OB032_step07.jpeg.webp\|200]] | Step 08<br>![[OB032_step08.jpeg.webp\|200]] | Step 09<br>![[OB032_step09.jpeg.webp\|200]] |
| Step 10<br>![[OB032_step10.jpeg.webp\|200]] | Step 11<br>![[OB032_step11.jpeg.webp\|200]] | Step 12<br>![[OB032_step12.jpeg.webp\|200]] |
| Step 13<br>![[OB032_step13.jpeg.webp\|200]] | Step 14<br>![[OB032_step14.jpeg.webp\|200]] | Step 15<br>![[OB032_step15.jpeg.webp\|200]] |
| Step 16<br>![[OB032_step16.jpeg.webp\|200]] | Step 17<br>![[OB032_step17.jpeg.webp\|200]] |  |
---

## 5. Visual selection

### Crisis / threshold according to AI-assisted reading

### Step 16
![[OB032_step16.jpeg.webp]]



### Crisis / threshold according to my perception

### Step 09
![[OB032_step09.jpeg.webp]]

---

## 6. Crisis and formal-perceptual reading

**The operation affects the contour, figure-ground relationship, color, and legibility of the image:**

The operation acts precisely upon the place where the image separates the figure from the background. The contour is not erased: edge pixels do not overwrite themselves, so the drawing survives. What is lost is its containing function, because each edge becomes a vanishing point from which matter flows outward or flows inward.

With few emitters, the image reads as a photograph with lines superimposed: the two layers do not touch. With too many, the traces form a homogeneous texture that obscures the figure. In the intermediate zone, the traces overlap until they become a veil, and the face is read through its own displaced color. The hair, which is the zone of highest contrast, emits with greater force and becomes a radial halo: precisely the area that defined the boundary of the head is the first to lose its boundary.

---

## 7. Final evaluation and artistic reference

**Operation notes / what I learned:**  
The parameter that drives the reading is not the length of the traces but how many edges emit. With traces longer than 800 px, the detection threshold single-handedly decides whether the image remains stable (few threads) or collapses (a mass). The minimum length and the percentage of emitters are what allow it to remain at the intermediate point.

The filename generated by the script prior to cataloging did not include the detection thresholds, so different runs ended up with the same name. The actual parameters for each one were retrieved from the experimentation log and saved in the metadata of each step.

**Final_status:**  
Works:: [[SI|YES]]

**How it destroys the image:**  
Works_on:: [[Configurativo|Configurational]]

**Level and richness of crisis:**  
Crisis:: [[Media|Medium]]

**Decision:**  
Selection:: [[Combinable|Combinable]]

---

### Potential artistic reference

Reference:: [[Arnulf Rainer|Arnulf Rainer]], [[Kumi Yamashita|Kumi Yamashita]], 

**Possible works:**  
- [Arnulf Rainer - Face Farces 1969](https://www.google.com/search?q=Arnulf+Rainer+Face+Farces+1969&udm=2)

- [Kumi Yamashita — _Constellation_, 2004]()
