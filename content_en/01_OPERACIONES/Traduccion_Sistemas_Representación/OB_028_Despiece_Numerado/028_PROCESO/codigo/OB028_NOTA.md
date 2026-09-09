---
lang: en
---

# NUMBERED EXPLODED VIEW

## 🎯 OPERATIONAL REGIME
**Representation Systems Translation**

The image is translated into the "exploded technical manual system". It detects visual components, separates them into an exploded axonometry (displaced from an imaginary center), and adds guide lines and numbering. Like a machine parts diagram, but of the original photograph.

---

**Status:** In experimentation — UNcataloged (without `OB_0XX` yet).

## Family

Does not belong to explored families. It is a translation to a single technical system.

## What it does

Segments the image into components by detecting contours. Each component is numbered and displaced radially from the center of the image. Guide lines are added connecting each piece to its origin. The result: a technical "exploded view" of the scene.

## Targeted crisis

**Representation Translation:** the image is converted from the "continuous visual system" to the "disassembled technical diagram system". Information is lost: spatial continuity, scene unity.

**Friction zone:** the content remains recognizable (components are visible) but its reading remains **suspended**: it is neither assembled nor completely destroyed. It requires mental effort to reassemble the original scene. The technical lines compete with the legibility of the image.

**If the explosion is mild:** barely visible, too stable.
**If it is extreme:** becomes abstract, technical, unreadable as a photograph.
**Ideal:** noticeable separation that demands mental reassembly.

## Iterated parameters

- **NUM_COMPONENTES** (3–30): how many parts are detected and numbered.
  Low = few large parts, easy to reassemble.
  High = many small ones, difficult to follow.

- **DISTANCIA_EXPLOSION** (10–150 px): how far the parts separate from the center.
  Low = subtly separated.
  High = extremely exploded, almost abstract.

- **MOSTRAR_LINEAS_GUIA** (True/False): whether connective lines are drawn.
  True = more "technical", like a manual.
  False = exploded view without guides, more ambiguous.

## How it is recorded

Each run:
1. Generates a file with a unique name: `<input>_despiece_<parámetros>_<timestamp>_<variante>.<ext>`
2. Records how many components were detected.
3. Adds an evaluation block to this file (`NOTA.md`).
4. Kurt fills in: perceptual reading (checkbox), what happens to form/continuity/structure,
   and decision (repeat, intensify, etc.).

---

## Log by run

### Run 20260907_211111_571358

| Parameter | Value |
|---|---|
| Input | `Input_003.jpeg` (3024×4032) |
| NUM_COMPONENTES | 8 |
| DISTANCIA_EXPLOSION | 60 |
| MOSTRAR_LINEAS_GUIA | True |
| Components detected | 8 |

Outputs:
- `resultados/Input_003_despiece_comp8_exp60_lineassi_20260907_211111_571358_despiece.jpeg`

**Perceptual reading** (check one):
- [ ] Too stable — components with almost no separation, easy to reassemble
- [ ] Destroyed too quickly — exploded view so extreme that it is abstract, unreadable
- [ ] Friction zone — exploded view visible but requires mental reassembly, reading suspended

**What happens to:** form · contour · scene continuity · legibility · technical structure
>

**Decision:** repeat · intensify (raise `DISTANCIA_EXPLOSION`, more `NUM_COMPONENTES`) · stop · discard · (hybridize — later)
>

---

### Run 20260907_211221_618734

| Parameter | Value |
|---|---|
| Input | `Input_003.jpeg` (3024×4032) |
| NUM_COMPONENTES | 15 |
| DISTANCIA_EXPLOSION | 100 |
| MOSTRAR_LINEAS_GUIA | True |
| Components detected | 15 |

Outputs:
- `resultados/Input_003_despiece_comp15_exp100_lineassi_20260907_211221_618734_despiece.jpeg`

**Perceptual reading** (check one):
- [ ] Too stable — components with almost no separation, easy to reassemble
- [ ] Destroyed too quickly — exploded view so extreme that it is abstract, unreadable
- [ ] Friction zone — exploded view visible but requires mental reassembly, reading suspended

**What happens to:** form · contour · scene continuity · legibility · technical structure
>

**Decision:** repeat · intensify (raise `DISTANCIA_EXPLOSION`, more `NUM_COMPONENTES`) · stop · discard · (hybridize — later)
>

---

### Run 20260907_211242_356420

| Parameter | Value |
|---|---|
| Input | `Input_003.jpeg` (3024×4032) |
| NUM_COMPONENTES | 15 |
| DISTANCIA_EXPLOSION | 100 |
| MOSTRAR_LINEAS_GUIA | True |
| Components detected | 15 |

Outputs:
- `resultados/Input_003_despiece_comp15_exp100_lineassi_20260907_211242_356420_despiece.jpeg`

**Perceptual reading** (check one):
- [ ] Too stable — components with almost no separation, easy to reassemble
- [ ] Destroyed too quickly — exploded view so extreme that it is abstract, unreadable
- [ ] Friction zone — exploded view visible but requires mental reassembly, reading suspended

**What happens to:** form · contour · scene continuity · legibility · technical structure
>

**Decision:** repeat · intensify (raise `DISTANCIA_EXPLOSION`, more `NUM_COMPONENTES`) · stop · discard · (hybridize — later)
>

---

### Run 20260907_211341_921874

| Parameter | Value |
|---|---|
| Input | `input_001.jpg` (3024×4032) |
| NUM_COMPONENTES | 15 |
| DISTANCIA_EXPLOSION | 100 |
| MOSTRAR_LINEAS_GUIA | True |
| Components detected | 15 |

Outputs:
- `resultados/input_001_despiece_comp15_exp100_lineassi_20260907_211341_921874_despiece.jpg`

**Perceptual reading** (check one):
- [ ] Too stable — components with almost no separation, easy to reassemble
- [ ] Destroyed too quickly — exploded view so extreme that it is abstract, unreadable
- [ ] Friction zone — exploded view visible but requires mental reassembly, reading suspended

**What happens to:** form · contour · scene continuity · legibility · technical structure
>

**Decision:** repeat · intensify (raise `DISTANCIA_EXPLOSION`, more `NUM_COMPONENTES`) · stop · discard · (hybridize — later)
>

---

### Run 20260907_211443_802429

| Parameter | Value |
|---|---|
| Input | `input_001.jpg` (3024×4032) |
| NUM_COMPONENTES | 30 |
| DISTANCIA_EXPLOSION | 100150 |
| MOSTRAR_LINEAS_GUIA | True |
| Components detected | 30 |

Outputs:
- `resultados/input_001_despiece_comp30_exp100150_lineassi_20260907_211443_802429_despiece.jpg`

**Perceptual reading** (check one):
- [ ] Too stable — components with almost no separation, easy to reassemble
- [ ] Destroyed too quickly — exploded view so extreme that it is abstract, unreadable
- [ ] Friction zone — exploded view visible but requires mental reassembly, reading suspended

**What happens to:** form · contour · scene continuity · legibility · technical structure
>

**Decision:** repeat · intensify (raise `DISTANCIA_EXPLOSION`, more `NUM_COMPONENTES`) · stop · discard · (hybridize — later)
>

---

### Run 20260907_211612_725797

| Parameter | Value |
|---|---|
| Input | `input_001.jpg` (3024×4032) |
| NUM_COMPONENTES | 30 |
| DISTANCIA_EXPLOSION | 200150 |
| MOSTRAR_LINEAS_GUIA | True |
| Components detected | 30 |

Outputs:
- `resultados/input_001_despiece_comp30_exp200150_lineassi_20260907_211612_725797_despiece.jpg`

**Perceptual reading** (check one):
- [ ] Too stable — components with almost no separation, easy to reassemble
- [ ] Destroyed too quickly — exploded view so extreme that it is abstract, unreadable
- [ ] Friction zone — exploded view visible but requires mental reassembly, reading suspended

**What happens to:** form · contour · scene continuity · legibility · technical structure
>

**Decision:** repeat · intensify (raise `DISTANCIA_EXPLOSION`, more `NUM_COMPONENTES`) · stop · discard · (hybridize — later)
>

---


### Run 20260907_212152_911909

| Parameter | Value |
|---|---|
| Input | `input_001.jpg` (3024×4032) |
| NUM_PIEZAS | 45 |
| COMPACTACION | 18.0 |
| DISTANCIA_EXPLOSION | 0.13 × diagonal |
| VARIACION_EXPLOSION | 0.45 |
| NUM_DIRECCIONES | 8 |
| NUM_CAPAS_EXPLOSION | 4 |
| OPACIDAD_FANTASMA | 0.0 |
| Pieces generated | 46 |

Output:

- `resultados/input_001_despiece_piezas45_exp0p13_var0p45_dir8_capas4_20260907_212152_911909.jpg`

**Perceptual reading**:

- [ ] Too stable — the scene still appears first and the exploded view second
- [ ] Destroyed too quickly — only fragments appear with no possibility of reconstruction
- [ ] Friction zone — the pieces are recognizable but the scene demands mental reassembly

**What appears first when looking?**

- [ ] Photograph
- [ ] Technical exploded view
- [ ] Oscillates between both

**What happens to:**
continuity · figure/ground · position · object · fragment · recognition

>

**Decision:**

- [ ] lower explosion
- [ ] raise explosion
- [ ] lower pieces
- [ ] raise pieces
- [ ] modify segmentation
- [ ] stop
- [ ] discard

>

---



### Run 20260907_212459_593862

| Parameter | Value |
|---|---|
| Input | `Input_003.jpeg` (3024×4032) |
| NUM_PIEZAS | 45 |
| COMPACTACION | 18.0 |
| DISTANCIA_EXPLOSION | 0.13 × diagonal |
| VARIACION_EXPLOSION | 0.45 |
| NUM_DIRECCIONES | 8 |
| NUM_CAPAS_EXPLOSION | 4 |
| OPACIDAD_FANTASMA | 0.0 |
| Pieces generated | 26 |

Output:

- `resultados/Input_003_despiece_piezas45_exp0p13_var0p45_dir8_capas4_20260907_212459_593862.jpg`

**Perceptual reading**:

- [ ] Too stable — the scene still appears first and the exploded view second
- [ ] Destroyed too quickly — only fragments appear with no possibility of reconstruction
- [ ] Friction zone — the pieces are recognizable but the scene demands mental reassembly

**What appears first when looking?**

- [ ] Photograph
- [ ] Technical exploded view
- [ ] Oscillates between both

**What happens to:**
continuity · figure/ground · position · object · fragment · recognition

>

**Decision:**

- [ ] lower explosion
- [ ] raise explosion
- [ ] lower pieces
- [ ] raise pieces
- [ ] modify segmentation
- [ ] stop
- [ ] discard

>

---



### Run 20260907_212804_974846

| Parameter | Value |
|---|---|
| Input | `Input_003.jpeg` (3024×4032) |
| NUM_PIEZAS | 80 |
| COMPACTACION | 30.0 |
| DISTANCIA_EXPLOSION | 0.02 × diagonal |
| VARIACION_EXPLOSION | 0.1 |
| NUM_DIRECCIONES | 12 |
| NUM_CAPAS_EXPLOSION | 4 |
| OPACIDAD_FANTASMA | 0.0 |
| Pieces generated | 59 |

Output:

- `resultados/Input_003_despiece_piezas80_exp0p02_var0p1_dir12_capas4_20260907_212804_974846.jpg`

**Perceptual reading**:

- [ ] Too stable — the scene still appears first and the exploded view second
- [ ] Destroyed too quickly — only fragments appear with no possibility of reconstruction
- [ ] Friction zone — the pieces are recognizable but the scene demands mental reassembly

**What appears first when looking?**

- [ ] Photograph
- [ ] Technical exploded view
- [ ] Oscillates between both

**What happens to:**
continuity · figure/ground · position · object · fragment · recognition

>

**Decision:**

- [ ] lower explosion
- [ ] raise explosion
- [ ] lower pieces
- [ ] raise pieces
- [ ] modify segmentation
- [ ] stop
- [ ] discard

>

---



### Run 20260907_213239_430900

| Parameter | Value |
|---|---|
| Input | `Input_003.jpeg` (3024×4032) |
| NUM_PIEZAS | 200 |
| COMPACTACION | 5.0 |
| DISTANCIA_EXPLOSION | 0.12 × diagonal |
| VARIACION_EXPLOSION | 0.3 |
| NUM_DIRECCIONES | 20 |
| NUM_CAPAS_EXPLOSION | 5 |
| OPACIDAD_FANTASMA | 0.0 |
| Pieces generated | 26 |

Output:

- `resultados/Input_003_despiece_piezas200_exp0p12_var0p3_dir20_capas5_20260907_213239_430900.jpg`

**Perceptual reading**:

- [ ] Too stable — the scene still appears first and the exploded view second
- [ ] Destroyed too quickly — only fragments appear with no possibility of reconstruction
- [ ] Friction zone — the pieces are recognizable but the scene demands mental reassembly

**What appears first when looking?**

- [ ] Photograph
- [ ] Technical exploded view
- [ ] Oscillates between both

**What happens to:**
continuity · figure/ground · position · object · fragment · recognition

>

**Decision:**

- [ ] lower explosion
- [ ] raise explosion
- [ ] lower pieces
- [ ] raise pieces
- [ ] modify segmentation
- [ ] stop
- [ ] discard

>

---



### Run 20260907_214300_116168

| Parameter | Value |
|---|---|
| Input | `Input_003.jpeg` (3024×4032) |
| NUM_PIEZAS | 100 |
| COMPACTACION | 30.0 |
| DISTANCIA_EXPLOSION | 0.18 × diagonal |
| VARIACION_EXPLOSION | 0.5 |
| NUM_DIRECCIONES | 12 |
| NUM_CAPAS_EXPLOSION | 5 |
| OPACIDAD_FANTASMA | 0.0 |
| Pieces generated | 84 |

Output:

- `resultados/Input_003_despiece_piezas100_exp0p18_var0p5_dir12_capas5_20260907_214300_116168.jpg`

**Perceptual reading**:

- [ ] Too stable — the scene still appears first and the exploded view second
- [ ] Destroyed too quickly — only fragments appear with no possibility of reconstruction
- [ ] Friction zone — the pieces are recognizable but the scene demands mental reassembly

**What appears first when looking?**

- [ ] Photograph
- [ ] Technical exploded view
- [ ] Oscillates between both

**What happens to:**
continuity · figure/ground · position · object · fragment · recognition

>

**Decision:**

- [ ] lower explosion
- [ ] raise explosion
- [ ] lower pieces
- [ ] raise pieces
- [ ] modify segmentation
- [ ] stop
- [ ] discard

>

---



### Run 20260907_215848_288246

| Parameter | Value |
|---|---|
| Input | `Input_003.jpeg` (900×1200) |
| NUM_PIEZAS | 300 |
| COMPACTACION | 40.0 |
| DISTANCIA_EXPLOSION | 0.02 × diagonal |
| VARIACION_EXPLOSION | 0.7 |
| NUM_DIRECCIONES | 22 |
| NUM_CAPAS_EXPLOSION | 10 |
| OPACIDAD_FANTASMA | 0.12 |
| Pieces generated | 300 |

Output:

- `resultados/Input_003_despiece_piezas300_exp0p02_var0p7_dir22_capas10_20260907_215848_288246.jpg`

**Perceptual reading**:

- [ ] Too stable — the scene still appears first and the exploded view second
- [ ] Destroyed too quickly — only fragments appear with no possibility of reconstruction
- [ ] Friction zone — the pieces are recognizable but the scene demands mental reassembly

**What appears first when looking?**

- [ ] Photograph
- [ ] Technical exploded view
- [ ] Oscillates between both

**What happens to:**
continuity · figure/ground · position · object · fragment · recognition

>

**Decision:**

- [ ] lower explosion
- [ ] raise explosion
- [ ] lower pieces
- [ ] raise pieces
- [ ] modify segmentation
- [ ] stop
- [ ] discard

>

---



### Run 20260907_220025_237094

| Parameter | Value |
|---|---|
| Input | `Input_003.jpeg` (900×1200) |
| NUM_PIEZAS | 300 |
| COMPACTACION | 40.0 |
| DISTANCIA_EXPLOSION | 0.02 × diagonal |
| VARIACION_EXPLOSION | 0.7 |
| NUM_DIRECCIONES | 22 |
| NUM_CAPAS_EXPLOSION | 10 |
| OPACIDAD_FANTASMA | 0.12 |
| Pieces generated | 300 |

Output:

- `resultados/Input_003_despiece_piezas300_exp0p02_var0p7_dir22_capas10_20260907_220025_237094.jpg`

**Perceptual reading**:

- [ ] Too stable — the scene still appears first and the exploded view second
- [ ] Destroyed too quickly — only fragments appear with no possibility of reconstruction
- [ ] Friction zone — the pieces are recognizable but the scene demands mental reassembly

**What appears first when looking?**

- [ ] Photograph
- [ ] Technical exploded view
- [ ] Oscillates between both

**What happens to:**
continuity · figure/ground · position · object · fragment · recognition

>

**Decision:**

- [ ] lower explosion
- [ ] raise explosion
- [ ] lower pieces
- [ ] raise pieces
- [ ] modify segmentation
- [ ] stop
- [ ] discard

>

---



### Run 20260907_220416_643374

| Parameter | Value |
|---|---|
| Input | `Input_003.jpeg` (900×1200) |
| NUM_PIEZAS | 300 |
| COMPACTACION | 40.0 |
| DISTANCIA_EXPLOSION | 0.02 × diagonal |
| VARIACION_EXPLOSION | 0.7 |
| NUM_DIRECCIONES | 22 |
| NUM_CAPAS_EXPLOSION | 10 |
| RECORTAR_MARCO | True |
| OPACIDAD_FANTASMA | 0.12 |
| Pieces generated | 300 |

Output:

- `resultados/Input_003_despiece_piezas300_exp0p02_var0p7_dir22_capas10_20260907_220416_643374.jpg`

**Perceptual reading**:

- [ ] Too stable — the scene still appears first and the exploded view second
- [ ] Destroyed too quickly — only fragments appear with no possibility of reconstruction
- [ ] Friction zone — the pieces are recognizable but the scene demands mental reassembly

**What appears first when looking?**

- [ ] Photograph
- [ ] Technical exploded view
- [ ] Oscillates between both

**What happens to:**
continuity · figure/ground · position · object · fragment · recognition

>

**Decision:**

- [ ] lower explosion
- [ ] raise explosion
- [ ] lower pieces
- [ ] raise pieces
- [ ] modify segmentation
- [ ] stop
- [ ] discard

>

---



### Run 20260907_222404_211012

| Parameter | Value |
|---|---|
| Input | `Input_003.jpeg` (1125×1500) |
| NUM_PIEZAS | 400 |
| COMPACTACION | 10.0 |
| DISTANCIA_EXPLOSION | 0.3 × diagonal |
| VARIACION_EXPLOSION | 0.8 |
| NUM_DIRECCIONES | 32 |
| NUM_CAPAS_EXPLOSION | 15 |
| RECORTAR_MARCO | True |
| OPACIDAD_FANTASMA | 0.12 |
| Pieces generated | 349 |

Output:

- `resultados/Input_003_despiece_piezas400_exp0p3_var0p8_dir32_capas15_20260907_222404_211012.jpg`

**Perceptual reading**:

- [ ] Too stable — the scene still appears first and the exploded view second
- [ ] Destroyed too quickly — only fragments appear with no possibility of reconstruction
- [ ] Friction zone — the pieces are recognizable but the scene demands mental reassembly

**What appears first when looking?**

- [ ] Photograph
- [ ] Technical exploded view
- [ ] Oscillates between both

**What happens to:**
continuity · figure/ground · position · object · fragment · recognition

>

**Decision:**

- [ ] lower explosion
- [ ] raise explosion
- [ ] lower pieces
- [ ] raise pieces
- [ ] modify segmentation
- [ ] stop
- [ ] discard

>

---



### Run 20260907_222501_835556

| Parameter | Value |
|---|---|
| Input | `Input_003.jpeg` (1125×1500) |
| NUM_PIEZAS | 400 |
| COMPACTACION | 10.0 |
| DISTANCIA_EXPLOSION | 0.3 × diagonal |
| VARIACION_EXPLOSION | 0.1 |
| NUM_DIRECCIONES | 32 |
| NUM_CAPAS_EXPLOSION | 15 |
| RECORTAR_MARCO | True |
| OPACIDAD_FANTASMA | 0.12 |
| Pieces generated | 349 |

Output:

- `resultados/Input_003_despiece_piezas400_exp0p3_var0p1_dir32_capas15_20260907_222501_835556.jpg`

**Perceptual reading**:

- [ ] Too stable — the scene still appears first and the exploded view second
- [ ] Destroyed too quickly — only fragments appear with no possibility of reconstruction
- [ ] Friction zone — the pieces are recognizable but the scene demands mental reassembly

**What appears first when looking?**

- [ ] Photograph
- [ ] Technical exploded view
- [ ] Oscillates between both

**What happens to:**
continuity · figure/ground · position · object · fragment · recognition

>

**Decision:**

- [ ] lower explosion
- [ ] raise explosion
- [ ] lower pieces
- [ ] raise pieces
- [ ] modify segmentation
- [ ] stop
- [ ] discard

>

---



### Run 20260907_222600_660703

| Parameter | Value |
|---|---|
| Input | `Input_003.jpeg` (1125×1500) |
| NUM_PIEZAS | 400 |
| COMPACTACION | 10.0 |
| DISTANCIA_EXPLOSION | 0.18 × diagonal |
| VARIACION_EXPLOSION | 1.0 |
| NUM_DIRECCIONES | 32 |
| NUM_CAPAS_EXPLOSION | 15 |
| RECORTAR_MARCO | True |
| OPACIDAD_FANTASMA | 0.12 |
| Pieces generated | 349 |

Output:

- `resultados/Input_003_despiece_piezas400_exp0p18_var1p0_dir32_capas15_20260907_222600_660703.jpg`

**Perceptual reading**:

- [ ] Too stable — the scene still appears first and the exploded view second
- [ ] Destroyed too quickly — only fragments appear with no possibility of reconstruction
- [ ] Friction zone — the pieces are recognizable but the scene demands mental reassembly

**What appears first when looking?**

- [ ] Photograph
- [ ] Technical exploded view
- [ ] Oscillates between both

**What happens to:**
continuity · figure/ground · position · object · fragment · recognition

>

**Decision:**

- [ ] lower explosion
- [ ] raise explosion
- [ ] lower pieces
- [ ] raise pieces
- [ ] modify segmentation
- [ ] stop
- [ ] discard

>

---



### Run 20260907_222630_929997

| Parameter | Value |
|---|---|
| Input | `Input_003.jpeg` (1125×1500) |
| NUM_PIEZAS | 400 |
| COMPACTACION | 10.0 |
| DISTANCIA_EXPLOSION | 0.1 × diagonal |
| VARIACION_EXPLOSION | 1.0 |
| NUM_DIRECCIONES | 32 |
| NUM_CAPAS_EXPLOSION | 15 |
| RECORTAR_MARCO | True |
| OPACIDAD_FANTASMA | 0.12 |
| Pieces generated | 349 |

Output:

- `resultados/Input_003_despiece_piezas400_exp0p1_var1p0_dir32_capas15_20260907_222630_929997.jpg`

**Perceptual reading**:

- [ ] Too stable — the scene still appears first and the exploded view second
- [ ] Destroyed too quickly — only fragments appear with no possibility of reconstruction
- [ ] Friction zone — the pieces are recognizable but the scene demands mental reassembly

**What appears first when looking?**

- [ ] Photograph
- [ ] Technical exploded view
- [ ] Oscillates between both

**What happens to:**
continuity · figure/ground · position · object · fragment · recognition

>

**Decision:**

- [ ] lower explosion
- [ ] raise explosion
- [ ] lower pieces
- [ ] raise pieces
- [ ] modify segmentation
- [ ] stop
- [ ] discard

>

---



### Run 20260907_222658_033783

| Parameter | Value |
|---|---|
| Input | `Input_003.jpeg` (1125×1500) |
| NUM_PIEZAS | 400 |
| COMPACTACION | 10.0 |
| DISTANCIA_EXPLOSION | 0.05 × diagonal |
| VARIACION_EXPLOSION | 1.0 |
| NUM_DIRECCIONES | 32 |
| NUM_CAPAS_EXPLOSION | 15 |
| RECORTAR_MARCO | True |
| OPACIDAD_FANTASMA | 0.12 |
| Pieces generated | 349 |

Output:

- `resultados/Input_003_despiece_piezas400_exp0p05_var1p0_dir32_capas15_20260907_222658_033783.jpg`

**Perceptual reading**:

- [ ] Too stable — the scene still appears first and the exploded view second
- [ ] Destroyed too quickly — only fragments appear with no possibility of reconstruction
- [ ] Friction zone — the pieces are recognizable but the scene demands mental reassembly

**What appears first when looking?**

- [ ] Photograph
- [ ] Technical exploded view
- [ ] Oscillates between both

**What happens to:**
continuity · figure/ground · position · object · fragment · recognition

>

**Decision:**

- [ ] lower explosion
- [ ] raise explosion
- [ ] lower pieces
- [ ] raise pieces
- [ ] modify segmentation
- [ ] stop
- [ ] discard

>

---



### Run 20260907_222801_548980

| Parameter | Value |
|---|---|
| Input | `Input_003.jpeg` (1125×1500) |
| NUM_PIEZAS | 400 |
| COMPACTACION | 10.0 |
| DISTANCIA_EXPLOSION | 0.05 × diagonal |
| VARIACION_EXPLOSION | 1.0 |
| NUM_DIRECCIONES | 32 |
| NUM_CAPAS_EXPLOSION | 15 |
| RECORTAR_MARCO | True |
| OPACIDAD_FANTASMA | 0.12 |
| Pieces generated | 349 |

Output:

- `resultados/Input_003_despiece_piezas400_exp0p05_var1p0_dir32_capas15_20260907_222801_548980.jpg`

**Perceptual reading**:

- [ ] Too stable — the scene still appears first and the exploded view second
- [ ] Destroyed too quickly — only fragments appear with no possibility of reconstruction
- [ ] Friction zone — the pieces are recognizable but the scene demands mental reassembly

**What appears first when looking?**

- [ ] Photograph
- [ ] Technical exploded view
- [ ] Oscillates between both

**What happens to:**
continuity · figure/ground · position · object · fragment · recognition

>

**Decision:**

- [ ] lower explosion
- [ ] raise explosion
- [ ] lower pieces
- [ ] raise pieces
- [ ] modify segmentation
- [ ] stop
- [ ] discard

>

---



### Run 20260907_222908_479463

| Parameter | Value |
|---|---|
| Input | `Input_003.jpeg` (1125×1500) |
| NUM_PIEZAS | 500 |
| COMPACTACION | 1.0 |
| DISTANCIA_EXPLOSION | 0.05 × diagonal |
| VARIACION_EXPLOSION | 1.0 |
| NUM_DIRECCIONES | 32 |
| NUM_CAPAS_EXPLOSION | 15 |
| RECORTAR_MARCO | True |
| OPACIDAD_FANTASMA | 0.12 |
| Pieces generated | 186 |

Output:

- `resultados/Input_003_despiece_piezas500_exp0p05_var1p0_dir32_capas15_20260907_222908_479463.jpg`

**Perceptual reading**:

- [ ] Too stable — the scene still appears first and the exploded view second
- [ ] Destroyed too quickly — only fragments appear with no possibility of reconstruction
- [ ] Friction zone — the pieces are recognizable but the scene demands mental reassembly

**What appears first when looking?**

- [ ] Photograph
- [ ] Technical exploded view
- [ ] Oscillates between both

**What happens to:**
continuity · figure/ground · position · object · fragment · recognition

>

**Decision:**

- [ ] lower explosion
- [ ] raise explosion
- [ ] lower pieces
- [ ] raise pieces
- [ ] modify segmentation
- [ ] stop
- [ ] discard

>

---



### Run 20260907_223010_002964

| Parameter | Value |
|---|---|
| Input | `Input_003.jpeg` (1125×1500) |
| NUM_PIEZAS | 500 |
| COMPACTACION | 1.0 |
| DISTANCIA_EXPLOSION | 0.05 × diagonal |
| VARIACION_EXPLOSION | 1.0 |
| NUM_DIRECCIONES | 32 |
| NUM_CAPAS_EXPLOSION | 15 |
| RECORTAR_MARCO | True |
| OPACIDAD_FANTASMA | 0.0 |
| Pieces generated | 186 |

Output:

- `resultados/Input_003_despiece_piezas500_exp0p05_var1p0_dir32_capas15_20260907_223010_002964.jpg`

**Perceptual reading**:

- [ ] Too stable — the scene still appears first and the exploded view second
- [ ] Destroyed too quickly — only fragments appear with no possibility of reconstruction
- [ ] Friction zone — the pieces are recognizable but the scene demands mental reassembly

**What appears first when looking?**

- [ ] Photograph
- [ ] Technical exploded view
- [ ] Oscillates between both

**What happens to:**
continuity · figure/ground · position · object · fragment · recognition

>

**Decision:**

- [ ] lower explosion
- [ ] raise explosion
- [ ] lower pieces
- [ ] raise pieces
- [ ] modify segmentation
- [ ] stop
- [ ] discard

>

---



### Run 20260907_223155_159984

| Parameter | Value |
|---|---|
| Input | `Input_003.jpeg` (1125×1500) |
| NUM_PIEZAS | 50 |
| COMPACTACION | 1.0 |
| DISTANCIA_EXPLOSION | 0.07 × diagonal |
| VARIACION_EXPLOSION | 1.0 |
| NUM_DIRECCIONES | 32 |
| NUM_CAPAS_EXPLOSION | 20 |
| RECORTAR_MARCO | True |
| OPACIDAD_FANTASMA | 0.0 |
| Pieces generated | 18 |

Output:

- `resultados/Input_003_despiece_piezas50_exp0p07_var1p0_dir32_capas20_20260907_223155_159984.jpg`

**Perceptual reading**:

- [ ] Too stable — the scene still appears first and the exploded view second
- [ ] Destroyed too quickly — only fragments appear with no possibility of reconstruction
- [ ] Friction zone — the pieces are recognizable but the scene demands mental reassembly

**What appears first when looking?**

- [ ] Photograph
- [ ] Technical exploded view
- [ ] Oscillates between both

**What happens to:**
continuity · figure/ground · position · object · fragment · recognition

>

**Decision:**

- [ ] lower explosion
- [ ] raise explosion
- [ ] lower pieces
- [ ] raise pieces
- [ ] modify segmentation
- [ ] stop
- [ ] discard

>

---



### Run 20260907_223302_395316

| Parameter | Value |
|---|---|
| Input | `Input_003.jpeg` (1125×1500) |
| NUM_PIEZAS | 50 |
| COMPACTACION | 1.0 |
| DISTANCIA_EXPLOSION | 0.07 × diagonal |
| VARIACION_EXPLOSION | 1.0 |
| NUM_DIRECCIONES | 32 |
| NUM_CAPAS_EXPLOSION | 20 |
| RECORTAR_MARCO | True |
| OPACIDAD_FANTASMA | 0.0 |
| Pieces generated | 18 |

Output:

- `resultados/Input_003_despiece_piezas50_exp0p07_var1p0_dir32_capas20_20260907_223302_395316.jpg`

**Perceptual reading**:

- [ ] Too stable — the scene still appears first and the exploded view second
- [ ] Destroyed too quickly — only fragments appear with no possibility of reconstruction
- [ ] Friction zone — the pieces are recognizable but the scene demands mental reassembly

**What appears first when looking?**

- [ ] Photograph
- [ ] Technical exploded view
- [ ] Oscillates between both

**What happens to:**
continuity · figure/ground · position · object · fragment · recognition

>

**Decision:**

- [ ] lower explosion
- [ ] raise explosion
- [ ] lower pieces
- [ ] raise pieces
- [ ] modify segmentation
- [ ] stop
- [ ] discard

>

---



### Run 20260907_224433_482869

| Parameter | Value |
|---|---|
| Input | `OB028_input.jpg` (1125×1500) |
| NUM_PIEZAS | 50 |
| COMPACTACION | 1.0 |
| DISTANCIA_EXPLOSION | 0.07 × diagonal |
| VARIACION_EXPLOSION | 1.0 |
| NUM_DIRECCIONES | 32 |
| NUM_CAPAS_EXPLOSION | 20 |
| RECORTAR_MARCO | True |
| OPACIDAD_FANTASMA | 0.0 |
| Pieces generated | 18 |

Output:

- `resultados/OB028_input_despiece_piezas50_exp0p07_var1p0_dir32_capas20_20260907_224433_482869.jpg`

**Perceptual reading**:

- [ ] Too stable — the scene still appears first and the exploded view second
- [ ] Destroyed too quickly — only fragments appear with no possibility of reconstruction
- [ ] Friction zone — the pieces are recognizable but the scene demands mental reassembly

**What appears first when looking?**

- [ ] Photograph
- [ ] Technical exploded view
- [ ] Oscillates between both

**What happens to:**
continuity · figure/ground · position · object · fragment · recognition

>

**Decision:**

- [ ] lower explosion
- [ ] raise explosion
- [ ] lower pieces
- [ ] raise pieces
- [ ] modify segmentation
- [ ] stop
- [ ] discard

>

---
