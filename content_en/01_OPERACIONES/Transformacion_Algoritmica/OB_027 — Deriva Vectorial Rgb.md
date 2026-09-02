---
title: "OB_027 — RGB Vector Drift"
atlas_direct: true
lang: en
---

## Status
Status::  [[Terminada|Terminada]]

---

## 1. Operation data

**Internal number:** OB_027
**Operational regime:** [[Lista_Transformacion_Algoritmica|Algorithmic Transformation List]]  
**Source image:** Digital Photograph

**Operational description:**  

Each pixel shifts along a trajectory determined by its chromatic information: the RGB proportion defines the direction, brightness determines the distance, and saturation modifies the curvature. The accumulation of these trajectories produces a progressive drift of the original image.

---

## 2. Tools

**Tools / medium:**  

- Python
- NumPy
- Pillow


---

## 3. Variables

**Controlled variables:**  

- Maximum displacement distance
- Number of trajectory steps
- Intensity of curvature and conservation of the original image

**Uncontrolled / accidental variables:**  

- Overlap and concentration of pixels during displacement
- Empty or sparsely dense areas produced by pixels leaving their original positions
- Emerging shapes, stains, and transitions determined by the particular chromatic distribution of the source image


---

## 4. Visual sequence

### Initial image
![[input_03.jpeg.webp|200]]

### Step 01
![[OB027_step01.png.webp|200]]

### Step 02
![[OB027_step02.png.webp|200]]

### Step 03
![[OB027_step03.png.webp|200]]

### Step 04
![[OB027_step04.png.webp|200]]

### Step 05
![[OB027_step05.png.webp|200]]

### Step 06
![[OB027_step06.png.webp|200]]

### Step 07
![[OB027_step07.png.webp|200]]

### Step 08
![[OB027_step08.png.webp|200]]

### Step 09
![[OB027_step09.png.webp|200]]

### Step 10
![[OB027_step10.png.webp|200]]

### Step 11
![[OB027_step11.png.webp|200]]

### Step 12
![[OB027_step12.png.webp|200]]



---

## 5. Visual selection

### Crisis / threshold according to AI-assisted reading / ChatGPT


### Step 07
![[OB027_step07.png.webp]]



### Crisis / threshold according to my perception


### Step 10
![[OB027_step10.png.webp]]


---

## 6. Crisis and formal-perceptual reading


**Where the crisis occurs and the operation affects the visual grammar of the image: shape, contour, color, figure/ground relationship, legibility, recognition, and support:**

Its contours begin to dissolve and blend into the background. Color remains as an indication of the figure, although it ceases to correspond to a defined form. The figure/ground separation becomes ambiguous, and the image oscillates between a recognizable landscape and dragged chromatic masses. The digital support begins to become perceptible through the drift and accumulation of pixels.


---

## 7. Final evaluation and artistic reference


**Operation notes / what I learned:**  

This operation also feels [[organica|organic]] and [[pictorica|pictorial]], and it can be handled quite a bit. It is like passing a rag over the image.

**Final_status:** 
Works:: [[SI|SI]] 

**How it destroys the image:** 
Works_on:: [[Formal|Formal]] 

**Level and Richness of crisis:** 
Crisis::   [[Alta|Alta]]

**Decision:** 
Selection:: [[Combinable|Combinable]] / [[Guardar|Guardar]] 

---

### Potential artistic reference

Reference:: [[Gerhard Richter|Gerhard Richter]], [[Wilhelm Sasnal|Wilhelm Sasnal]], [[JMW Turner|JMW Turner]], [[James Whistler|James Whistler]], [[Claude Monet|Claude Monet]]

**Possible works:**  
- [Gerhard Richter - Apfelbaume Apple Trees 1987](https://www.google.com/search?q=Gerhard+Richter+Apfelbaume+Apple+Trees+1987&udm=2)

- [Wilhelm Sasnal - A forest](https://www.google.com/search?q=Wilhelm+Sasnal+a+forest&sca_esv=dce9e9559af1f0c3&udm=2&sxsrf=APpeQns-wz1UoJS5DwCoIbzS6F5RmEyl8g%3A1786612393995&ei=qYp9av2bPPSP9u8PpYXZmAc&biw=1680&bih=907&ved=0ahUKEwi9lOHooZ2WAxX0h_0HHaVCFnMQ4dUDCBE&uact=5&oq=Wilhelm+Sasnal+a+forest&gs_lp=Egtnd3Mtd2l6LWltZyIXV2lsaGVsbSBTYXNuYWwgYSBmb3Jlc3RI0B5Q_AhYlhtwAXgAkAEAmAGRA6ABtBKqAQkwLjQuNC4xLjG4AQPIAQD4AQGYAgOgAocFwgIHECMYyQIYJ8ICBRAAGIAEwgIEEAAYHsICBxAAGIAEGBPCAgYQABgeGBPCAggQABgeGBMYCsICBhAAGAgYHpgDAIgGAZIHBTAuMS4yoAf0E7IHBTAuMS4yuAeHBcIHBzAuMS4xLjHIBw6ACAE&sclient=gws-wiz-img)

- [JMW Turner - Snow Storm Steam Boat 1842](https://www.google.com/search?q=JMW+Turner+Snow+Storm+Steam+Boat+1842&udm=2)

- [James Whistler - nocturne in black and gold](https://search.brave.com/images?q=James+Whistler+-+nocturne+in+black+and+gold&source=web)

- [Claude Monet - Houses of Parliament Effect of Fog 1903](https://www.google.com/search?q=Claude+Monet+Houses+of+Parliament+Effect+of+Fog+1903&udm=2)
