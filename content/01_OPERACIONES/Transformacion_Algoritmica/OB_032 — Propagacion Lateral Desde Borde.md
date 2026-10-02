---
title: "OB_032 — Propagacion Lateral Desde Borde"
atlas_direct: true
---

# OB_032_Propagacion_Lateral_Desde_Borde

## Estado
Estado:: [[Terminada]]

---

## 1. Datos de la operación

**Número interno:** OB_032  
**Régimen operativo:** [[Lista_Transformacion_Algoritmica]]  
**Imagen de origen:** Fotografía digital — retrato frontal ([[Input_005.jpeg.webp]])

**Descripción operativa:**  
Cada píxel de borde deja de funcionar como límite y pasa a funcionar como fuente: emite una traza recta que copia color ya existente en la imagen, tomado unos píxeles detrás del filo, y lo arrastra hacia la región vecina. La longitud de la traza no es aleatoria: la fija la propia imagen, por la fuerza del gradiente, la luminancia o la saturación local. Solo un porcentaje de los bordes emite.

El contorno, que separaba la figura del fondo, se convierte en el origen de la invasión: el color de un lado del borde cruza al otro. El color nunca se inventa, solo se copia y se desplaza. El único azar es cuáles bordes emiten, y está fijado por una semilla.

**Familia:** arrastre direccional a partir de contornos detectados. El antecedente más cercano es el experimento `Propagacion_de_bordes`, que dilata el color desde los bordes de forma isotrópica, como una mancha que crece en todas direcciones. Aquí, en cambio, la propagación es direccional y de longitud variable: cada borde arrastra hacia un solo lado, según su gradiente.

---

## 2. Herramientas

**Herramientas / medio:**

- Python
- NumPy
- OpenCV
- Detección de bordes (Canny o Sobel)
- Trazado de líneas a lo largo del gradiente

**Script:** `OB032_propagacion_lateral_desde_borde.py`. Explica dentro cómo correrlo y qué necesita.  
**Parámetros por resultado:** están en los metadatos de cada imagen (EXIF, campo *ImageDescription*).

---

## 3. Procedimiento y variables

**Procedimiento:**

1. Leer la fotografía y suavizarla con un gaussiano.
2. Detectar bordes, con Canny (finos y selectivos) o con Sobel (toda zona de gradiente alto).
3. Descartar los bordes con fuerza de gradiente menor a un mínimo.
4. Elegir al azar, con semilla fija, el porcentaje de bordes que emite.
5. Para cada emisor, tomar el color unos píxeles detrás del filo.
6. Trazar una línea recta desde el borde en la dirección elegida (horizontal, vertical, a lo largo del gradiente o paralela al contorno), con una longitud proporcional al modulador y una opacidad que se apaga hacia el final.
7. Conservar las dimensiones originales de la imagen.

**Variables controladas:**

- Método de detección de bordes y umbrales
- Suavizado previo
- Fuerza mínima de borde
- Propiedad que decide la longitud (gradiente, luminancia, saturación)
- Dirección del arrastre
- Longitud mínima y máxima de la traza
- Opacidad y decaimiento de la traza
- Porcentaje de bordes que emiten
- Distancia de muestreo del color fuente
- Región protegida y mezcla final con el original

**Variables no controladas / accidentales:**

- Haces de trazas convergentes cuando muchos bordes vecinos tienen la misma orientación
- Aureola radial alrededor de la cabeza: el pelo, como zona de mayor contraste, emite hacia afuera en todas direcciones
- Trazas que atraviesan la imagen entera y salen del cuadro
- Veladura: la superposición de muchas trazas finas deja ver la figura debajo como a través de una trama
- Diferencias de materia según el origen del color (trazas oscuras del pelo, claras del fondo, cálidas de la piel)

---

## 4. Secuencia visual

Todos los steps provienen de [[Input_005.jpeg.webp]]. El orden es cronológico, y los parámetros de cada uno están en los metadatos de su imagen.

Los steps 01–02 prueban el arrastre horizontal con trazas cortas. Los steps 03–06 pasan al arrastre a lo largo del gradiente con trazas largas y pocos emisores. Los steps 07–17 barren el umbral de detección, el porcentaje de emisores y la longitud mínima sobre esa misma dirección.

### Imagen inicial
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

## 5. Selección visual

### Crisis / umbral según lectura asistida por IA

### Step 16
![[OB032_step16.jpeg.webp]]



### Crisis / umbral según mi percepción

### Step 09
![[OB032_step09.jpeg.webp]]

---

## 6. Crisis y lectura formal-perceptiva

**La operación afecta el contorno, la figura-fondo, el color y la legibilidad de la imagen:**

La operación trabaja exactamente sobre el lugar donde la imagen separa la figura del fondo. El contorno no se borra: los píxeles de borde no se pisan a sí mismos, así que el dibujo sobrevive. Lo que se pierde es su función de contener, porque cada borde se vuelve un punto de fuga desde el que la materia sale hacia afuera o entra hacia adentro.

Con pocos emisores, la imagen se lee como una fotografía con líneas encima: las dos capas no se tocan. Con demasiados, las trazas forman un peinado homogéneo que tapa la figura. En la zona intermedia, las trazas se superponen hasta volverse una veladura, y la cara se lee a través de su propio color desplazado. El pelo, que es la zona de mayor contraste, emite con más fuerza y se convierte en una aureola radial: justamente la zona que definía el borde de la cabeza es la primera que deja de tener borde.

---

## 7. Evaluación final y referente artístico

**Notas de la operación / qué aprendí:**  
El parámetro que mueve la lectura no es la longitud de las trazas sino cuántos bordes emiten. Con trazas de más de 800 px, el umbral de detección decide por sí solo si la imagen queda estable (pocos hilos) o colapsa (una masa). La longitud mínima y el porcentaje de emisores son los que permiten quedarse en el punto intermedio.

El nombre de archivo que generaba el script antes de catalogar no incluía los umbrales de detección, así que corridas distintas quedaron con el mismo nombre. Los parámetros reales de cada una se tomaron de la bitácora de experimentación y quedaron guardados en los metadatos de cada step.

**Estado_final:**  
Funciona:: [[SI]]

**Cómo destruye la imagen:**  
Trabaja_en_lo:: [[Configurativo]]

**Nivel y riqueza de crisis:**  
Crisis:: [[Media]]

**Decisión:**  
Seleccion:: [[Combinable]]

---

### Referente artístico posible

Referente:: [[Arnulf Rainer]], [[Kumi Yamashita]], 

**Obras posibles:**  
- [Arnulf Rainer - Face Farces 1969](https://www.google.com/search?q=Arnulf+Rainer+Face+Farces+1969&udm=2)

- [Kumi Yamashita — _Constellation_, 2004]()
