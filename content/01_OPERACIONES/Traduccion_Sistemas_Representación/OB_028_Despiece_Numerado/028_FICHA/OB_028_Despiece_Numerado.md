# OB_028_Despiece_Numerado

## Estado
Estado:: [[En revisión]]

---

## 1. Datos de la operación

**Número interno:** OB_028  
**Régimen operativo:** [[Lista_Traduccion_Sistemas_Representacion]]  
**Imagen de origen:** Fotografía digital

**Descripción operativa:**  
Una fotografía digital se segmenta en regiones y se traduce al lenguaje visual de un despiece técnico. Cada región conserva sus píxeles fotográficos, pero pasa a funcionar como una pieza separada y potencialmente identificable mediante contornos, líneas de montaje, marcas y numeración.

La mediación es algorítmica, pero el régimen principal es de traducción: la imagen deja de presentarse como una superficie fotográfica continua y comienza a leerse como un diagrama de componentes.

---

## 2. Herramientas

**Herramientas / medio:**

- Python
- OpenCV
- NumPy
- scikit-image, segmentación SLIC

**Script:** [[OB028_despiece_numerado.py]]  
**Dependencias:** [[requirements.txt]]  
**Nota de pruebas:** [[OB028_NOTA.md]]  
**Parámetros por resultado:** [[OB028_PARAMETROS_RESULTADOS.txt]]

---

## 3. Procedimiento y variables

**Procedimiento:**

1. Reducir proporcionalmente la imagen para acelerar el procesamiento.
2. Segmentar la fotografía en regiones visuales.
3. Extraer los píxeles correspondientes a cada región.
4. Calcular una dirección y una distancia de desplazamiento para cada pieza.
5. Distribuir las piezas en direcciones y capas cuantizadas.
6. Incorporar opcionalmente contornos, líneas, puntos de origen y numeración.
7. Recortar el espacio exterior sobrante sin eliminar piezas.

**Variables controladas:**

- Cantidad aproximada de piezas
- Compactación y suavizado de la segmentación
- Distancia y variación de la explosión
- Cantidad de direcciones y capas
- Presencia de imagen fantasma
- Líneas guía, contornos, marcas y numeración
- Tamaño máximo de procesamiento

**Variables no controladas / accidentales:**

- Forma concreta de las regiones detectadas
- Vacíos producidos entre piezas
- Cruces y acumulaciones entre piezas y líneas
- Grado de reconocimiento local de cada fragmento
- Reconstrucción mental que realiza quien observa

---

## 4. Secuencia visual

### Imagen inicial
![[Input_003.jpeg|200]]

### Step 01
![[OB028_step01.jpg.webp|200]]

### Step 02
![[OB028_step02.jpg.webp|200]]

### Step 03
![[OB028_step03.jpg.webp|200]]

### Step 04
![[OB028_step04.jpg.webp|200]]

### Step 05
![[OB028_step05.jpg.webp|200]]

### Step 06
![[OB028_step06.jpg.webp|200]]

### Step 07
![[OB028_step07.jpg.webp|200]]

### Step 08
![[OB028_step08.jpg.webp|200]]

### Step 09
![[OB028_step09.jpg.webp|200]]

### Step 10
![[OB028_step10.jpg.webp|200]]

### Step 11
![[OB028_step11.jpg.webp|200]]

### Step 12
![[OB028_step12.jpg.webp|200]]

### Step 13
![[OB028_step13.jpg.webp|200]]

### Step 14
![[OB028_step14.jpg.webp|200]]

### Step 15
![[OB028_step15.jpg.webp|200]]

### Step 16
![[OB028_step16.jpg.webp|200]]

---

## 5. Selección visual

### Crisis / umbral según lectura asistida por IA / ChatGPT

Pendiente de revisión de la secuencia completa.

### Crisis / umbral según mi percepción

Pendiente de selección.

---

## 6. Crisis y lectura formal-perceptiva

**La operación afecta la continuidad, la posición, la relación entre parte y totalidad, el reconocimiento y la lectura del soporte:**

Las piezas siguen siendo fotográficas y conservan información reconocible de la imagen técnica original, pero dejan de ocupar una superficie continua. La escena oscila entre fotografía y esquema de montaje: puede reconstruirse mentalmente, aunque su unidad queda subordinada a la lectura de componentes separados, numerados y desplazados.

La crisis aparece cuando las partes todavía permiten reconocer la procedencia fotográfica, pero el conjunto se percibe primero como inventario, diagrama o manual técnico.

---

## 7. Evaluación final y referente artístico

**Notas de la operación / qué aprendí:**  
El algoritmo no constituye por sí solo el régimen de la operación. La segmentación y el desplazamiento son medios para traducir una fotografía raster al sistema de representación de un despiece técnico numerado.

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
