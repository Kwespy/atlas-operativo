---
title: "OB_025 — Saturacion vecindad rgb"
atlas_direct: true
lang: en
---

## Status
Status::  [[Terminada|Finished]]

---

## 1. Operation Data

**Internal number:** OB_000 + OB_000
**Operational regime:** [[Lista_Combinaciones|Combinations List]]  
**Source image:** Digital Photography

**Operational description:**  
The script groups neighboring pixels with similar RGB values and increases their saturation according to the size and presence of each group, progressively driving the image toward a crisis of legibility.

---

## 2. Tools

**Tools / medium:**  
- Python
- NumPy
- Pillow / OpenCV


---

## 3. Variables

**Controlled variables:**  
- Number of divisions or RGB bins.
- Minimum size of pixel groups.
- Saturation intensity and degree of unification between similar colors.

**Uncontrolled / accidental variables:**  

The initial color distribution and proximity between pixels in the source image, which determines which groups are formed and where the zones of highest saturation appear.


---

## 4. Visual Sequence

### Initial image
![[input_03.jpeg.webp]]

### Step 01
![[OB025_step01.jpg.webp|200]]

### Step 02
![[OB025_step02.jpg.webp|200]]

### Step 03
![[OB025_step03.jpg.webp|200]]

### Step 04
![[OB025_step04.jpg.webp|200]]

### Step 05
![[OB025_step05.jpg.webp|200]]

### Step 06
![[OB025_step06.jpg.webp|200]]

### Step 07
![[OB025_step07.jpg.webp|200]]

### Step 08
![[OB025_step08.jpg.webp|200]]

### Step 09
![[OB025_step09.jpg.webp|200]]

### Step 10
![[OB025_step10.jpg.webp|200]]

### Step 11
![[OB025_step11.jpg.webp|200]]

### Step 12
![[OB025_step12.jpg.webp|200]]

### Step 13
![[OB025_step13.jpg.webp|200]]

### Step 14
![[OB025_step14.jpg.webp|200]]

### Step 15
![[OB025_step15.jpg.webp|200]]

### Step 16
![[OB025_step16.jpg.webp|200]]

### Step 17
![[OB025_step17.jpg.webp|200]]

### Step 18
![[OB025_step18.jpg.webp|200]]

### Step 19
![[OB025_step19.jpg.webp|200]]

### Step 20
![[OB025_step20.jpg.webp|200]]

### Step 21
![[OB025_step21.jpg.webp|200]]

### Step 22
![[OB025_step22.jpg.webp|200]]

### Step 23
![[OB025_step23.jpg.webp|200]]

### Step 24
![[OB025_step24.jpg.webp|200]]

### Step 25
![[OB025_step25.jpg.webp|200]]

---

## 5. Visual Selection

### Crisis / threshold according to AI-assisted reading / ChatGPT


### Step 15
![[OB025_step15.jpg.webp]]



### Crisis / threshold according to my perception


### Step 07
![[OB025_step07.jpg.webp]]

### Step 23
![[OB025_step23.jpg.webp]]




---

## 6. Crisis and Formal-Perceptual Reading


**Where the crisis occurs and the operation affects the visual grammar of the image: shape, contour, color, figure/ground relationship, legibility, recognition, and support:**

Saturation begins to dominate over the original information: contours weaken, certain figure and ground areas become confused, and the landscape remains at an intermediate point between recognition and abstraction. **Color** is the main element causing the loss of legibility, while the digital support remains unchanged.


---

## 7. Final Evaluation and Artistic Reference


**Operation notes / what I learned:**  

This operation yields a pictorial result and does not feel like a fully digital operation.
A script can be built following a logic and it can be articulated to be more complex and have a more complex logic as well.


**Final_status:** 
Works:: [[SI|YES]] 

**How it destroys the image:** 
Works_on::  [[Formal|Formal]] 

**Level and Richness of crisis:** 
Crisis::  [[Alta|High]]

**Decision:** 
Selection:: [[Combinable|Combinable]] / [[Guardar|Save]] / [[Tesis|Thesis]]

---

### Potential Artistic Reference

Reference:: [[Vincent van Gogh|Vincent van Gogh]], [[Andre Derain|Andre Derain]], [[Maurice de Vlaminck|Maurice de Vlaminck]], [[Ernst Ludwig Kirchner|Ernst Ludwig Kirchner]], [[Daniel Richter|Daniel Richter]],

**Possible works:**  
- [Vincent van Gogh - The Olive Trees. ](https://www.google.com/search?q=Vincent+van+Gogh.+The+Olive+Trees.+Saint+R%C3%A9my&sca_esv=0ab4c29f2e17ee32&udm=2&biw=1274&bih=892&sxsrf=APpeQnvnlWvshezjNKuhM0WYLOMXWM1W7g%3A1786550174533&ei=npd8auiCIKC8xc8PgvXDaQ&ved=0ahUKEwjoyZqEupuWAxUgXvEDHYL6MA0Q4dUDCBE&uact=5&oq=Vincent+van+Gogh.+The+Olive+Trees.+Saint+R%C3%A9my&gs_lp=Egtnd3Mtd2l6LWltZyIuVmluY2VudCB2YW4gR29naC4gVGhlIE9saXZlIFRyZWVzLiBTYWludCBSw6lteTIEEAAYHkjtL1ChDVieLnAFeACQAQCYAXSgAcACqgEDMS4yuAEDyAEA-AEB-AECmAIHoAL1AcICBxAjGMkCGCfCAgoQABiABBiKBRhDwgIGEAAYBxgewgIFEAAYgASYAwCIBgGSBwM2LjGgB8EHsgcDMS4xuAfaAcIHBTEuMC42yAccgAgB&sclient=gws-wiz-img)

- [Andre Derain - Mountains at Collioure 1905](https://www.google.com/search?q=Andre+Derain+Mountains+at+Collioure+1905&udm=2)

- [Maurice de Vlaminck - The Seine at Chatou 1906](https://www.google.com/search?q=Maurice+de+Vlaminck+The+Seine+at+Chatou+1906&udm=2)

- [Ernst Ludwig Kirchner - Winter Moonlit Night](https://www.google.com/search?q=Ernst+Ludwig+Kirchner+Winter+Moonlit+Night&udm=2)

- [Daniel Richter - Tarifa 2001](https://www.google.com/search?q=Daniel+Richter+Tarifa+2001&udm=2)
