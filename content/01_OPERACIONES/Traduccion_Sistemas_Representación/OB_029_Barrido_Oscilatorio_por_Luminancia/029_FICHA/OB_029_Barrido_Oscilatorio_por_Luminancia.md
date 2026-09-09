# OB_029_Barrido_Oscilatorio_por_Luminancia

## Estado
Estado:: [[En revisión]]

---

## 1. Datos de la operación

**Número interno:** OB_029  
**Régimen operativo:** [[Lista_Traduccion_Sistemas_Representacion]]  
**Imagen de origen:** Fotografía digital

**Descripción operativa:**  
Una fotografía digital raster se convierte en una única trayectoria lineal que recorre el cuadro en serpentina. La luminancia de cada zona deja de expresarse como tono y pasa a controlar la amplitud y la frecuencia local de la oscilación.

Aunque el procedimiento se ejecuta mediante un algoritmo, el régimen principal es traducción: la matriz bidimensional de píxeles se vuelve una señal gráfica continua. La imagen ya no está compuesta por superficies de color, sino por el comportamiento de una línea.

---

## 2. Herramientas

**Herramientas / medio:**

- Python
- Pillow
- Muestreo de luminancia
- Dibujo de trayectoria raster

**Script:** [[OB029_barrido_oscilatorio_luminancia.py]]  
**Dependencias:** [[requirements.txt]]  
**Nota de pruebas:** [[OB029_NOTA.md]]  
**Parámetros por resultado:** [[OB029_PARAMETROS_RESULTADOS.txt]]

---

## 3. Procedimiento y variables

**Procedimiento:**

1. Leer la fotografía respetando su orientación técnica EXIF.
2. Reducirla temporalmente a una matriz de luminancia de menor resolución.
3. Recorrer la matriz fila por fila, alternando el sentido para construir una serpentina continua.
4. Convertir la oscuridad de cada muestra en amplitud y frecuencia de oscilación.
5. Dibujar todos los puntos como una sola línea sobre un fondo uniforme.
6. Mantener en el resultado las dimensiones originales de la imagen.

**Variables controladas:**

- Resolución horizontal de muestreo
- Amplitud máxima de oscilación
- Frecuencia base
- Frecuencia adicional producida por la oscuridad
- Grosor y color de línea
- Color de fondo

**Variables no controladas / accidentales:**

- Cruces entre filas contiguas
- Acumulación local de línea
- Aparición y desaparición de siluetas
- Lectura ambigua entre señal, trama y fotografía
- Formas producidas por la continuidad global del recorrido

---

## 4. Secuencia visual

La ficha utiliza únicamente los resultados históricos realizados con la imagen de la pelota. Las pruebas del árbol se conservan dentro de `029_PROCESO/resultados`, pero no forman parte de esta secuencia.

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

## 5. Selección visual

### Crisis / umbral según lectura asistida por IA / ChatGPT

Pendiente de elegir dentro de la secuencia de la pelota.

### Crisis / umbral según mi percepción

Pendiente de selección.

---

## 6. Crisis y lectura formal-perceptiva

**La operación afecta la superficie, el tono, el contorno, la figura-fondo, la legibilidad y el soporte de la imagen:**

La fotografía continúa siendo recuperable mediante densidades, cambios de amplitud y cruces de la línea, pero desaparece como superficie tonal continua. La crisis aparece cuando la pelota todavía emerge como volumen o silueta y, al mismo tiempo, la mirada reconoce primero una señal oscilatoria autónoma.

El soporte visual cambia de una matriz de píxeles a una trayectoria única: cada punto depende del anterior y la imagen completa queda subordinada a la continuidad temporal del barrido.

---

## 7. Evaluación final y referente artístico

**Notas de la operación / qué aprendí:**  
La luminancia puede conservar información figurativa sin representarse como gris. Al traducirse a movimiento lineal, la imagen se aproxima simultáneamente a una gráfica, una señal y un dibujo continuo.

**Estado_final:**  
Funciona:: [[SI]]

**Cómo destruye la imagen:**  
Trabaja_en_lo:: [[Formal]]

**Nivel y riqueza de crisis:**  
Crisis:: [[Pendiente]]

**Decisión:**  
Seleccion:: [[Revisar]]

---

### Referente artístico posible

Referente:: [[Pendiente]]
