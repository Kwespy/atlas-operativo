# OB_030_Desfase_Profundidad

## Estado
Estado:: [[Terminada]]

---

## 1. Datos de la operación

**Número interno:** OB_030  
**Régimen operativo:** [[Lista_Transformacion_Algoritmica]]  
**Imagen de origen:** Fotografía digital

**Descripción operativa:**  
Cada píxel se desplaza una distancia proporcional a su profundidad estimada, en una dirección fija. Es un paralaje falso: se finge que la fotografía tiene volumen y que la cámara se corre de costado, pero la profundidad no proviene de ninguna medición del espacio — se infiere de la propia imagen, de su luminancia o de dónde está enfocada.

Como los píxeles de igual profundidad se mueven juntos, con amplitudes grandes la imagen se pliega sobre sí misma y las iso-líneas del mapa quedan a la vista: aparecen bandas serpenteantes y anillos concéntricos, la fotografía reorganizada como un mapa de curvas de nivel.

El color no se altera en ningún momento: ningún valor cambia, solo cambia de sitio.

---

## 2. Herramientas

**Herramientas / medio:**

- Python
- NumPy
- OpenCV
- Estimación de profundidad por luminancia o por nitidez local
- Remapeo de coordenadas

**Script:** `OB030_desfase_profundidad.py`  
**Dependencias:** `requirements.txt`  
**Nota de pruebas:** `OB030_NOTA.md`  
**Parámetros por resultado:** `OB030_PARAMETROS_RESULTADOS.txt`

---

## 3. Procedimiento y variables

**Procedimiento:**

1. Leer la fotografía y convertirla a luminancia.
2. Construir un mapa de profundidad a partir de esa luminancia (lo claro se toma como lejano, siguiendo la neblina atmosférica) o del detalle local (lo enfocado se toma como cercano).
3. Desenfocar el mapa con un gaussiano, lo que define el tamaño de las bandas resultantes.
4. Opcionalmente cuantizar el mapa en escalones, para separar la imagen en láminas discretas.
5. Desplazar cada píxel una distancia proporcional a su profundidad, en una dirección fija.
6. Rellenar por reflexión lo que el desplazamiento deja fuera de cuadro.
7. Conservar las dimensiones originales de la imagen.

**Variables controladas:**

- Amplitud del desfase, como fracción del lado mayor
- Dirección del desplazamiento en grados
- Origen de la profundidad (luminancia, luminancia invertida, nitidez)
- Suavizado del mapa de profundidad (sigma)
- Cuantización del mapa en niveles
- Interpolación y modo de borde

**Variables no controladas / accidentales:**

- Aparición de anillos concéntricos donde el mapa tiene máximos locales
- Plegado de la imagen sobre sí misma
- Zonas que se vacían y se rellenan por reflexión
- Lectura ambigua entre fotografía y carta topográfica
- Colisión de materias distintas arrastradas a la misma banda

---

## 4. Secuencia visual

La ficha utiliza únicamente los resultados realizados con la imagen del árbol. Las pruebas de la pelota se conservan dentro de `030_PROCESO/resultados/PELOTA_fuera_de_secuencia`, pero no forman parte de esta secuencia.

Los steps 01–10 son el barrido histórico del 7 de agosto de 2026, de amplitud creciente. Los steps 11–13 corresponden al script reconstruido y llevan sus parámetros documentados.

| | | |
| --- | --- | --- |
| Step 01<br>![[OB030_step01.jpg.webp\|200]] | Step 02<br>![[OB030_step02.jpg.webp\|200]] | Step 03<br>![[OB030_step03.jpg.webp\|200]] |
| Step 04<br>![[OB030_step04.jpg.webp\|200]] | Step 05<br>![[OB030_step05.jpg.webp\|200]] | Step 06<br>![[OB030_step06.jpg.webp\|200]] |
| Step 07<br>![[OB030_step07.jpg.webp\|200]] | Step 08<br>![[OB030_step08.jpg.webp\|200]] | Step 09<br>![[OB030_step09.jpg.webp\|200]] |
| Step 10<br>![[OB030_step10.jpg.webp\|200]] | Step 11<br>![[OB030_step11.jpeg.webp\|200]] | Step 12<br>![[OB030_step12.jpeg.webp\|200]] |
| Step 13<br>![[OB030_step13.jpeg.webp\|200]] |  |  |
---

## 5. Selección visual

### Crisis / umbral según lectura asistida por IA / ChatGPT

### Step 05
![[OB030_step05.jpg.webp]]

### Crisis / umbral según mi percepción

### Step 06
![[OB030_step06.jpg.webp]]

---

## 6. Crisis y lectura formal-perceptiva

**La operación afecta la superficie, el tono, el contorno, la figura-fondo, la legibilidad y el soporte de la imagen:**

La organización general sobrevive: el cielo arriba, la masa del árbol en el centro, el suelo abajo, y los colores exactamente donde estaban, porque ningún valor de color se modifica. Lo que se pierde es la correspondencia entre la materia y lo que describe: cada zona se convierte en un tejido de bandas que ya no da cuenta de lo que había ahí.

La crisis aparece cuando el ojo lee un motivo y una carta topográfica al mismo tiempo y no puede decidir cuál de los dos está mirando. La imagen pasa a informar sobre su propia distribución de luz en lugar de informar sobre la escena: las bandas visibles son las iso-líneas del mapa de profundidad de esta fotografía en particular, y ninguna otra imagen produciría las mismas.

El contorno se erosiona sin borrarse: no desaparece, se estira y se pliega, y en los máximos locales del mapa se cierra sobre sí mismo formando anillos.

---

## 7. Evaluación final y referente artístico

**Notas de la operación / qué aprendí:**  
La profundidad puede fabricarse desde la propia imagen y funcionar igual como estructura de deformación. El resultado no depende de que la profundidad sea correcta, sino de que sea consistente: basta con que los píxeles de igual valor se muevan juntos para que aparezca la cartografía.

El script original de esta operación se perdió y tuvo que reconstruirse midiendo el campo de desplazamiento de las salidas históricas. Eso dejó una lección de método: sin el script y sin los parámetros en el nombre del archivo, un resultado no es reproducible aunque la imagen se conserve.

**Estado_final:**  
Funciona:: [[SI]]

**Cómo destruye la imagen:**  
Trabaja_en_lo:: [[Aparencial]]

**Nivel y riqueza de crisis:**  
Crisis:: [[Baja]]

**Decisión:**  
Seleccion:: [[Guardar]] [[Combinable]]

---

### Referente artístico posible

Referente:: [[Roberto Matta]], [[Vincent van Gogh]], [[Alex McAdoo]]

**Obras posibles:**  
- [Roberto Matta — _Invasion of the Night_](https://www.google.com/search?q=Roberto+Matta+Invasion+of+the+Night&udm=2#sv=CAMSURoyKhBlLW1FWjlNRE5GQjNEUVFNMg5tRVo5TURORkIzRFFRTToOZnp5Nk5zeHFRY0pKb00gBCoXCgFzEhBlLW1FWjlNRE5GQjNEUVFNGAEwARgHIKqm5ckKSggQAhgBIAIoAQ)

- [Vincent van Gogh — _La noche estrellada_](https://www.google.com/search?q=Vincent+van+Gogh+La+noche+estrellada&udm=2)

- [Alex McAdoo - Cowgill Ave](https://www.google.com/search?q=Alex+McAdoo+Cowgill+Ave&udm=2)
