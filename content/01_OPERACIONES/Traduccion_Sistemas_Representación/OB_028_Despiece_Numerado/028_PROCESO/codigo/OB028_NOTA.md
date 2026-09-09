# DESPIECE NUMERADO

## 🎯 RÉGIMEN OPERATIVO
**Traducción de Sistemas de Representación**

La imagen se traduce al "sistema de manual técnico explodido". Detecta componentes visuales, los separa en una axonometría explotada (desplazados desde un centro imaginario), y agrega líneas de guía y numeración. Como un despiece de máquina pero de la fotografía original.

---

**Estado:** En experimentación — SIN catalogar (sin `OB_0XX` aún).

## Familia

No pertenece a familias exploradas. Es una traducción a sistema técnico único.

## Qué hace

Segmenta la imagen en componentes detectando contornos. Cada componente se numera y se desplaza radialmente desde el centro de la imagen. Se agregan líneas de guía conectando cada pieza con su origen. El resultado: una "vista explotada" técnica de la escena.

## Crisis buscada

**Traducción de Representación:** la imagen se convierte del "sistema visual continuo" al "sistema de diagrama técnico desarmado". Información se pierde: continuidad espacial, unidad de la escena.

**Zona de fricción:** el contenido sigue siendo reconocible (se ven los componentes) pero su lectura queda **suspendida**: no está ni armado ni completamente destruido. Requiere un esfuerzo mental para rearmar la escena original. Las líneas técnicas compiten con la legibilidad de la imagen.

**Si la explosión es suave:** casi no se ve, demasiado estable.
**Si es extrema:** se vuelve abstracto, técnico, ilegible como fotografía.
**Ideal:** separación notoria que exija rearme mental.

## Parámetros que se iteran

- **NUM_COMPONENTES** (3–30): cuántas partes se detectan y numeran.
  Bajo = pocas piezas grandes, fácil de rearmar.
  Alto = muchas pequeñas, difícil de seguir.

- **DISTANCIA_EXPLOSION** (10–150 px): cuánto se separan las piezas del centro.
  Bajo = sutilmente separadas.
  Alto = extremadamente explodidas, casi abstracto.

- **MOSTRAR_LINEAS_GUIA** (True/False): si se dibujan líneas conectivas.
  True = más "técnico", como manual.
  False = despiece sin guías, más ambiguo.

## Cómo se registra

Cada corrida:
1. Genera un archivo con nombre único: `<input>_despiece_<parámetros>_<timestamp>_<variante>.<ext>`
2. Registra cuántos componentes se detectaron.
3. Agrega un bloque de evaluación a este archivo (`NOTA.md`).
4. Kurt completa: lectura perceptiva (checkbox), qué pasa con forma/continuidad/estructura,
   y decisión (repetir, intensificar, etc.).

---

## Bitácora por corrida

### Corrida 20260907_211111_571358

| Parámetro | Valor |
|---|---|
| Input | `Input_003.jpeg` (3024×4032) |
| NUM_COMPONENTES | 8 |
| DISTANCIA_EXPLOSION | 60 |
| MOSTRAR_LINEAS_GUIA | True |
| Componentes detectados | 8 |

Salidas:
- `resultados/Input_003_despiece_comp8_exp60_lineassi_20260907_211111_571358_despiece.jpeg`

**Lectura perceptiva** (marcá una):
- [ ] Demasiado estable — componentes casi sin separación, fácil de rearmar
- [ ] Destruida demasiado rápido — despiece tan extremo que es abstracto, ilegible
- [ ] Zona de fricción — despiece visible pero requiere rearme mental, lectura suspendida

**Qué pasa con:** forma · contorno · continuidad de la escena · legibilidad · estructura técnica
>

**Decisión:** repetir · intensificar (subir `DISTANCIA_EXPLOSION`, más `NUM_COMPONENTES`) · detener · descartar · (hibridar — más adelante)
>

---

### Corrida 20260907_211221_618734

| Parámetro | Valor |
|---|---|
| Input | `Input_003.jpeg` (3024×4032) |
| NUM_COMPONENTES | 15 |
| DISTANCIA_EXPLOSION | 100 |
| MOSTRAR_LINEAS_GUIA | True |
| Componentes detectados | 15 |

Salidas:
- `resultados/Input_003_despiece_comp15_exp100_lineassi_20260907_211221_618734_despiece.jpeg`

**Lectura perceptiva** (marcá una):
- [ ] Demasiado estable — componentes casi sin separación, fácil de rearmar
- [ ] Destruida demasiado rápido — despiece tan extremo que es abstracto, ilegible
- [ ] Zona de fricción — despiece visible pero requiere rearme mental, lectura suspendida

**Qué pasa con:** forma · contorno · continuidad de la escena · legibilidad · estructura técnica
>

**Decisión:** repetir · intensificar (subir `DISTANCIA_EXPLOSION`, más `NUM_COMPONENTES`) · detener · descartar · (hibridar — más adelante)
>

---

### Corrida 20260907_211242_356420

| Parámetro | Valor |
|---|---|
| Input | `Input_003.jpeg` (3024×4032) |
| NUM_COMPONENTES | 15 |
| DISTANCIA_EXPLOSION | 100 |
| MOSTRAR_LINEAS_GUIA | True |
| Componentes detectados | 15 |

Salidas:
- `resultados/Input_003_despiece_comp15_exp100_lineassi_20260907_211242_356420_despiece.jpeg`

**Lectura perceptiva** (marcá una):
- [ ] Demasiado estable — componentes casi sin separación, fácil de rearmar
- [ ] Destruida demasiado rápido — despiece tan extremo que es abstracto, ilegible
- [ ] Zona de fricción — despiece visible pero requiere rearme mental, lectura suspendida

**Qué pasa con:** forma · contorno · continuidad de la escena · legibilidad · estructura técnica
>

**Decisión:** repetir · intensificar (subir `DISTANCIA_EXPLOSION`, más `NUM_COMPONENTES`) · detener · descartar · (hibridar — más adelante)
>

---

### Corrida 20260907_211341_921874

| Parámetro | Valor |
|---|---|
| Input | `input_001.jpg` (3024×4032) |
| NUM_COMPONENTES | 15 |
| DISTANCIA_EXPLOSION | 100 |
| MOSTRAR_LINEAS_GUIA | True |
| Componentes detectados | 15 |

Salidas:
- `resultados/input_001_despiece_comp15_exp100_lineassi_20260907_211341_921874_despiece.jpg`

**Lectura perceptiva** (marcá una):
- [ ] Demasiado estable — componentes casi sin separación, fácil de rearmar
- [ ] Destruida demasiado rápido — despiece tan extremo que es abstracto, ilegible
- [ ] Zona de fricción — despiece visible pero requiere rearme mental, lectura suspendida

**Qué pasa con:** forma · contorno · continuidad de la escena · legibilidad · estructura técnica
>

**Decisión:** repetir · intensificar (subir `DISTANCIA_EXPLOSION`, más `NUM_COMPONENTES`) · detener · descartar · (hibridar — más adelante)
>

---

### Corrida 20260907_211443_802429

| Parámetro | Valor |
|---|---|
| Input | `input_001.jpg` (3024×4032) |
| NUM_COMPONENTES | 30 |
| DISTANCIA_EXPLOSION | 100150 |
| MOSTRAR_LINEAS_GUIA | True |
| Componentes detectados | 30 |

Salidas:
- `resultados/input_001_despiece_comp30_exp100150_lineassi_20260907_211443_802429_despiece.jpg`

**Lectura perceptiva** (marcá una):
- [ ] Demasiado estable — componentes casi sin separación, fácil de rearmar
- [ ] Destruida demasiado rápido — despiece tan extremo que es abstracto, ilegible
- [ ] Zona de fricción — despiece visible pero requiere rearme mental, lectura suspendida

**Qué pasa con:** forma · contorno · continuidad de la escena · legibilidad · estructura técnica
>

**Decisión:** repetir · intensificar (subir `DISTANCIA_EXPLOSION`, más `NUM_COMPONENTES`) · detener · descartar · (hibridar — más adelante)
>

---

### Corrida 20260907_211612_725797

| Parámetro | Valor |
|---|---|
| Input | `input_001.jpg` (3024×4032) |
| NUM_COMPONENTES | 30 |
| DISTANCIA_EXPLOSION | 200150 |
| MOSTRAR_LINEAS_GUIA | True |
| Componentes detectados | 30 |

Salidas:
- `resultados/input_001_despiece_comp30_exp200150_lineassi_20260907_211612_725797_despiece.jpg`

**Lectura perceptiva** (marcá una):
- [ ] Demasiado estable — componentes casi sin separación, fácil de rearmar
- [ ] Destruida demasiado rápido — despiece tan extremo que es abstracto, ilegible
- [ ] Zona de fricción — despiece visible pero requiere rearme mental, lectura suspendida

**Qué pasa con:** forma · contorno · continuidad de la escena · legibilidad · estructura técnica
>

**Decisión:** repetir · intensificar (subir `DISTANCIA_EXPLOSION`, más `NUM_COMPONENTES`) · detener · descartar · (hibridar — más adelante)
>

---


### Corrida 20260907_212152_911909

| Parámetro | Valor |
|---|---|
| Input | `input_001.jpg` (3024×4032) |
| NUM_PIEZAS | 45 |
| COMPACTACION | 18.0 |
| DISTANCIA_EXPLOSION | 0.13 × diagonal |
| VARIACION_EXPLOSION | 0.45 |
| NUM_DIRECCIONES | 8 |
| NUM_CAPAS_EXPLOSION | 4 |
| OPACIDAD_FANTASMA | 0.0 |
| Piezas generadas | 46 |

Salida:

- `resultados/input_001_despiece_piezas45_exp0p13_var0p45_dir8_capas4_20260907_212152_911909.jpg`

**Lectura perceptiva**:

- [ ] Demasiado estable — todavía aparece primero la escena y después el despiece
- [ ] Destruida demasiado rápido — solo aparecen fragmentos sin posibilidad de reconstrucción
- [ ] Zona de fricción — las piezas son reconocibles pero la escena exige rearme mental

**¿Qué aparece primero al mirar?**

- [ ] Fotografía
- [ ] Despiece técnico
- [ ] Oscila entre ambos

**Qué pasa con:**
continuidad · figura/fondo · posición · objeto · fragmento · reconocimiento

>

**Decisión:**

- [ ] bajar explosión
- [ ] subir explosión
- [ ] bajar piezas
- [ ] subir piezas
- [ ] modificar segmentación
- [ ] detener
- [ ] descartar

>

---



### Corrida 20260907_212459_593862

| Parámetro | Valor |
|---|---|
| Input | `Input_003.jpeg` (3024×4032) |
| NUM_PIEZAS | 45 |
| COMPACTACION | 18.0 |
| DISTANCIA_EXPLOSION | 0.13 × diagonal |
| VARIACION_EXPLOSION | 0.45 |
| NUM_DIRECCIONES | 8 |
| NUM_CAPAS_EXPLOSION | 4 |
| OPACIDAD_FANTASMA | 0.0 |
| Piezas generadas | 26 |

Salida:

- `resultados/Input_003_despiece_piezas45_exp0p13_var0p45_dir8_capas4_20260907_212459_593862.jpg`

**Lectura perceptiva**:

- [ ] Demasiado estable — todavía aparece primero la escena y después el despiece
- [ ] Destruida demasiado rápido — solo aparecen fragmentos sin posibilidad de reconstrucción
- [ ] Zona de fricción — las piezas son reconocibles pero la escena exige rearme mental

**¿Qué aparece primero al mirar?**

- [ ] Fotografía
- [ ] Despiece técnico
- [ ] Oscila entre ambos

**Qué pasa con:**
continuidad · figura/fondo · posición · objeto · fragmento · reconocimiento

>

**Decisión:**

- [ ] bajar explosión
- [ ] subir explosión
- [ ] bajar piezas
- [ ] subir piezas
- [ ] modificar segmentación
- [ ] detener
- [ ] descartar

>

---



### Corrida 20260907_212804_974846

| Parámetro | Valor |
|---|---|
| Input | `Input_003.jpeg` (3024×4032) |
| NUM_PIEZAS | 80 |
| COMPACTACION | 30.0 |
| DISTANCIA_EXPLOSION | 0.02 × diagonal |
| VARIACION_EXPLOSION | 0.1 |
| NUM_DIRECCIONES | 12 |
| NUM_CAPAS_EXPLOSION | 4 |
| OPACIDAD_FANTASMA | 0.0 |
| Piezas generadas | 59 |

Salida:

- `resultados/Input_003_despiece_piezas80_exp0p02_var0p1_dir12_capas4_20260907_212804_974846.jpg`

**Lectura perceptiva**:

- [ ] Demasiado estable — todavía aparece primero la escena y después el despiece
- [ ] Destruida demasiado rápido — solo aparecen fragmentos sin posibilidad de reconstrucción
- [ ] Zona de fricción — las piezas son reconocibles pero la escena exige rearme mental

**¿Qué aparece primero al mirar?**

- [ ] Fotografía
- [ ] Despiece técnico
- [ ] Oscila entre ambos

**Qué pasa con:**
continuidad · figura/fondo · posición · objeto · fragmento · reconocimiento

>

**Decisión:**

- [ ] bajar explosión
- [ ] subir explosión
- [ ] bajar piezas
- [ ] subir piezas
- [ ] modificar segmentación
- [ ] detener
- [ ] descartar

>

---



### Corrida 20260907_213239_430900

| Parámetro | Valor |
|---|---|
| Input | `Input_003.jpeg` (3024×4032) |
| NUM_PIEZAS | 200 |
| COMPACTACION | 5.0 |
| DISTANCIA_EXPLOSION | 0.12 × diagonal |
| VARIACION_EXPLOSION | 0.3 |
| NUM_DIRECCIONES | 20 |
| NUM_CAPAS_EXPLOSION | 5 |
| OPACIDAD_FANTASMA | 0.0 |
| Piezas generadas | 26 |

Salida:

- `resultados/Input_003_despiece_piezas200_exp0p12_var0p3_dir20_capas5_20260907_213239_430900.jpg`

**Lectura perceptiva**:

- [ ] Demasiado estable — todavía aparece primero la escena y después el despiece
- [ ] Destruida demasiado rápido — solo aparecen fragmentos sin posibilidad de reconstrucción
- [ ] Zona de fricción — las piezas son reconocibles pero la escena exige rearme mental

**¿Qué aparece primero al mirar?**

- [ ] Fotografía
- [ ] Despiece técnico
- [ ] Oscila entre ambos

**Qué pasa con:**
continuidad · figura/fondo · posición · objeto · fragmento · reconocimiento

>

**Decisión:**

- [ ] bajar explosión
- [ ] subir explosión
- [ ] bajar piezas
- [ ] subir piezas
- [ ] modificar segmentación
- [ ] detener
- [ ] descartar

>

---



### Corrida 20260907_214300_116168

| Parámetro | Valor |
|---|---|
| Input | `Input_003.jpeg` (3024×4032) |
| NUM_PIEZAS | 100 |
| COMPACTACION | 30.0 |
| DISTANCIA_EXPLOSION | 0.18 × diagonal |
| VARIACION_EXPLOSION | 0.5 |
| NUM_DIRECCIONES | 12 |
| NUM_CAPAS_EXPLOSION | 5 |
| OPACIDAD_FANTASMA | 0.0 |
| Piezas generadas | 84 |

Salida:

- `resultados/Input_003_despiece_piezas100_exp0p18_var0p5_dir12_capas5_20260907_214300_116168.jpg`

**Lectura perceptiva**:

- [ ] Demasiado estable — todavía aparece primero la escena y después el despiece
- [ ] Destruida demasiado rápido — solo aparecen fragmentos sin posibilidad de reconstrucción
- [ ] Zona de fricción — las piezas son reconocibles pero la escena exige rearme mental

**¿Qué aparece primero al mirar?**

- [ ] Fotografía
- [ ] Despiece técnico
- [ ] Oscila entre ambos

**Qué pasa con:**
continuidad · figura/fondo · posición · objeto · fragmento · reconocimiento

>

**Decisión:**

- [ ] bajar explosión
- [ ] subir explosión
- [ ] bajar piezas
- [ ] subir piezas
- [ ] modificar segmentación
- [ ] detener
- [ ] descartar

>

---



### Corrida 20260907_215848_288246

| Parámetro | Valor |
|---|---|
| Input | `Input_003.jpeg` (900×1200) |
| NUM_PIEZAS | 300 |
| COMPACTACION | 40.0 |
| DISTANCIA_EXPLOSION | 0.02 × diagonal |
| VARIACION_EXPLOSION | 0.7 |
| NUM_DIRECCIONES | 22 |
| NUM_CAPAS_EXPLOSION | 10 |
| OPACIDAD_FANTASMA | 0.12 |
| Piezas generadas | 300 |

Salida:

- `resultados/Input_003_despiece_piezas300_exp0p02_var0p7_dir22_capas10_20260907_215848_288246.jpg`

**Lectura perceptiva**:

- [ ] Demasiado estable — todavía aparece primero la escena y después el despiece
- [ ] Destruida demasiado rápido — solo aparecen fragmentos sin posibilidad de reconstrucción
- [ ] Zona de fricción — las piezas son reconocibles pero la escena exige rearme mental

**¿Qué aparece primero al mirar?**

- [ ] Fotografía
- [ ] Despiece técnico
- [ ] Oscila entre ambos

**Qué pasa con:**
continuidad · figura/fondo · posición · objeto · fragmento · reconocimiento

>

**Decisión:**

- [ ] bajar explosión
- [ ] subir explosión
- [ ] bajar piezas
- [ ] subir piezas
- [ ] modificar segmentación
- [ ] detener
- [ ] descartar

>

---



### Corrida 20260907_220025_237094

| Parámetro | Valor |
|---|---|
| Input | `Input_003.jpeg` (900×1200) |
| NUM_PIEZAS | 300 |
| COMPACTACION | 40.0 |
| DISTANCIA_EXPLOSION | 0.02 × diagonal |
| VARIACION_EXPLOSION | 0.7 |
| NUM_DIRECCIONES | 22 |
| NUM_CAPAS_EXPLOSION | 10 |
| OPACIDAD_FANTASMA | 0.12 |
| Piezas generadas | 300 |

Salida:

- `resultados/Input_003_despiece_piezas300_exp0p02_var0p7_dir22_capas10_20260907_220025_237094.jpg`

**Lectura perceptiva**:

- [ ] Demasiado estable — todavía aparece primero la escena y después el despiece
- [ ] Destruida demasiado rápido — solo aparecen fragmentos sin posibilidad de reconstrucción
- [ ] Zona de fricción — las piezas son reconocibles pero la escena exige rearme mental

**¿Qué aparece primero al mirar?**

- [ ] Fotografía
- [ ] Despiece técnico
- [ ] Oscila entre ambos

**Qué pasa con:**
continuidad · figura/fondo · posición · objeto · fragmento · reconocimiento

>

**Decisión:**

- [ ] bajar explosión
- [ ] subir explosión
- [ ] bajar piezas
- [ ] subir piezas
- [ ] modificar segmentación
- [ ] detener
- [ ] descartar

>

---



### Corrida 20260907_220416_643374

| Parámetro | Valor |
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
| Piezas generadas | 300 |

Salida:

- `resultados/Input_003_despiece_piezas300_exp0p02_var0p7_dir22_capas10_20260907_220416_643374.jpg`

**Lectura perceptiva**:

- [ ] Demasiado estable — todavía aparece primero la escena y después el despiece
- [ ] Destruida demasiado rápido — solo aparecen fragmentos sin posibilidad de reconstrucción
- [ ] Zona de fricción — las piezas son reconocibles pero la escena exige rearme mental

**¿Qué aparece primero al mirar?**

- [ ] Fotografía
- [ ] Despiece técnico
- [ ] Oscila entre ambos

**Qué pasa con:**
continuidad · figura/fondo · posición · objeto · fragmento · reconocimiento

>

**Decisión:**

- [ ] bajar explosión
- [ ] subir explosión
- [ ] bajar piezas
- [ ] subir piezas
- [ ] modificar segmentación
- [ ] detener
- [ ] descartar

>

---



### Corrida 20260907_222404_211012

| Parámetro | Valor |
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
| Piezas generadas | 349 |

Salida:

- `resultados/Input_003_despiece_piezas400_exp0p3_var0p8_dir32_capas15_20260907_222404_211012.jpg`

**Lectura perceptiva**:

- [ ] Demasiado estable — todavía aparece primero la escena y después el despiece
- [ ] Destruida demasiado rápido — solo aparecen fragmentos sin posibilidad de reconstrucción
- [ ] Zona de fricción — las piezas son reconocibles pero la escena exige rearme mental

**¿Qué aparece primero al mirar?**

- [ ] Fotografía
- [ ] Despiece técnico
- [ ] Oscila entre ambos

**Qué pasa con:**
continuidad · figura/fondo · posición · objeto · fragmento · reconocimiento

>

**Decisión:**

- [ ] bajar explosión
- [ ] subir explosión
- [ ] bajar piezas
- [ ] subir piezas
- [ ] modificar segmentación
- [ ] detener
- [ ] descartar

>

---



### Corrida 20260907_222501_835556

| Parámetro | Valor |
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
| Piezas generadas | 349 |

Salida:

- `resultados/Input_003_despiece_piezas400_exp0p3_var0p1_dir32_capas15_20260907_222501_835556.jpg`

**Lectura perceptiva**:

- [ ] Demasiado estable — todavía aparece primero la escena y después el despiece
- [ ] Destruida demasiado rápido — solo aparecen fragmentos sin posibilidad de reconstrucción
- [ ] Zona de fricción — las piezas son reconocibles pero la escena exige rearme mental

**¿Qué aparece primero al mirar?**

- [ ] Fotografía
- [ ] Despiece técnico
- [ ] Oscila entre ambos

**Qué pasa con:**
continuidad · figura/fondo · posición · objeto · fragmento · reconocimiento

>

**Decisión:**

- [ ] bajar explosión
- [ ] subir explosión
- [ ] bajar piezas
- [ ] subir piezas
- [ ] modificar segmentación
- [ ] detener
- [ ] descartar

>

---



### Corrida 20260907_222600_660703

| Parámetro | Valor |
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
| Piezas generadas | 349 |

Salida:

- `resultados/Input_003_despiece_piezas400_exp0p18_var1p0_dir32_capas15_20260907_222600_660703.jpg`

**Lectura perceptiva**:

- [ ] Demasiado estable — todavía aparece primero la escena y después el despiece
- [ ] Destruida demasiado rápido — solo aparecen fragmentos sin posibilidad de reconstrucción
- [ ] Zona de fricción — las piezas son reconocibles pero la escena exige rearme mental

**¿Qué aparece primero al mirar?**

- [ ] Fotografía
- [ ] Despiece técnico
- [ ] Oscila entre ambos

**Qué pasa con:**
continuidad · figura/fondo · posición · objeto · fragmento · reconocimiento

>

**Decisión:**

- [ ] bajar explosión
- [ ] subir explosión
- [ ] bajar piezas
- [ ] subir piezas
- [ ] modificar segmentación
- [ ] detener
- [ ] descartar

>

---



### Corrida 20260907_222630_929997

| Parámetro | Valor |
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
| Piezas generadas | 349 |

Salida:

- `resultados/Input_003_despiece_piezas400_exp0p1_var1p0_dir32_capas15_20260907_222630_929997.jpg`

**Lectura perceptiva**:

- [ ] Demasiado estable — todavía aparece primero la escena y después el despiece
- [ ] Destruida demasiado rápido — solo aparecen fragmentos sin posibilidad de reconstrucción
- [ ] Zona de fricción — las piezas son reconocibles pero la escena exige rearme mental

**¿Qué aparece primero al mirar?**

- [ ] Fotografía
- [ ] Despiece técnico
- [ ] Oscila entre ambos

**Qué pasa con:**
continuidad · figura/fondo · posición · objeto · fragmento · reconocimiento

>

**Decisión:**

- [ ] bajar explosión
- [ ] subir explosión
- [ ] bajar piezas
- [ ] subir piezas
- [ ] modificar segmentación
- [ ] detener
- [ ] descartar

>

---



### Corrida 20260907_222658_033783

| Parámetro | Valor |
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
| Piezas generadas | 349 |

Salida:

- `resultados/Input_003_despiece_piezas400_exp0p05_var1p0_dir32_capas15_20260907_222658_033783.jpg`

**Lectura perceptiva**:

- [ ] Demasiado estable — todavía aparece primero la escena y después el despiece
- [ ] Destruida demasiado rápido — solo aparecen fragmentos sin posibilidad de reconstrucción
- [ ] Zona de fricción — las piezas son reconocibles pero la escena exige rearme mental

**¿Qué aparece primero al mirar?**

- [ ] Fotografía
- [ ] Despiece técnico
- [ ] Oscila entre ambos

**Qué pasa con:**
continuidad · figura/fondo · posición · objeto · fragmento · reconocimiento

>

**Decisión:**

- [ ] bajar explosión
- [ ] subir explosión
- [ ] bajar piezas
- [ ] subir piezas
- [ ] modificar segmentación
- [ ] detener
- [ ] descartar

>

---



### Corrida 20260907_222801_548980

| Parámetro | Valor |
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
| Piezas generadas | 349 |

Salida:

- `resultados/Input_003_despiece_piezas400_exp0p05_var1p0_dir32_capas15_20260907_222801_548980.jpg`

**Lectura perceptiva**:

- [ ] Demasiado estable — todavía aparece primero la escena y después el despiece
- [ ] Destruida demasiado rápido — solo aparecen fragmentos sin posibilidad de reconstrucción
- [ ] Zona de fricción — las piezas son reconocibles pero la escena exige rearme mental

**¿Qué aparece primero al mirar?**

- [ ] Fotografía
- [ ] Despiece técnico
- [ ] Oscila entre ambos

**Qué pasa con:**
continuidad · figura/fondo · posición · objeto · fragmento · reconocimiento

>

**Decisión:**

- [ ] bajar explosión
- [ ] subir explosión
- [ ] bajar piezas
- [ ] subir piezas
- [ ] modificar segmentación
- [ ] detener
- [ ] descartar

>

---



### Corrida 20260907_222908_479463

| Parámetro | Valor |
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
| Piezas generadas | 186 |

Salida:

- `resultados/Input_003_despiece_piezas500_exp0p05_var1p0_dir32_capas15_20260907_222908_479463.jpg`

**Lectura perceptiva**:

- [ ] Demasiado estable — todavía aparece primero la escena y después el despiece
- [ ] Destruida demasiado rápido — solo aparecen fragmentos sin posibilidad de reconstrucción
- [ ] Zona de fricción — las piezas son reconocibles pero la escena exige rearme mental

**¿Qué aparece primero al mirar?**

- [ ] Fotografía
- [ ] Despiece técnico
- [ ] Oscila entre ambos

**Qué pasa con:**
continuidad · figura/fondo · posición · objeto · fragmento · reconocimiento

>

**Decisión:**

- [ ] bajar explosión
- [ ] subir explosión
- [ ] bajar piezas
- [ ] subir piezas
- [ ] modificar segmentación
- [ ] detener
- [ ] descartar

>

---



### Corrida 20260907_223010_002964

| Parámetro | Valor |
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
| Piezas generadas | 186 |

Salida:

- `resultados/Input_003_despiece_piezas500_exp0p05_var1p0_dir32_capas15_20260907_223010_002964.jpg`

**Lectura perceptiva**:

- [ ] Demasiado estable — todavía aparece primero la escena y después el despiece
- [ ] Destruida demasiado rápido — solo aparecen fragmentos sin posibilidad de reconstrucción
- [ ] Zona de fricción — las piezas son reconocibles pero la escena exige rearme mental

**¿Qué aparece primero al mirar?**

- [ ] Fotografía
- [ ] Despiece técnico
- [ ] Oscila entre ambos

**Qué pasa con:**
continuidad · figura/fondo · posición · objeto · fragmento · reconocimiento

>

**Decisión:**

- [ ] bajar explosión
- [ ] subir explosión
- [ ] bajar piezas
- [ ] subir piezas
- [ ] modificar segmentación
- [ ] detener
- [ ] descartar

>

---



### Corrida 20260907_223155_159984

| Parámetro | Valor |
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
| Piezas generadas | 18 |

Salida:

- `resultados/Input_003_despiece_piezas50_exp0p07_var1p0_dir32_capas20_20260907_223155_159984.jpg`

**Lectura perceptiva**:

- [ ] Demasiado estable — todavía aparece primero la escena y después el despiece
- [ ] Destruida demasiado rápido — solo aparecen fragmentos sin posibilidad de reconstrucción
- [ ] Zona de fricción — las piezas son reconocibles pero la escena exige rearme mental

**¿Qué aparece primero al mirar?**

- [ ] Fotografía
- [ ] Despiece técnico
- [ ] Oscila entre ambos

**Qué pasa con:**
continuidad · figura/fondo · posición · objeto · fragmento · reconocimiento

>

**Decisión:**

- [ ] bajar explosión
- [ ] subir explosión
- [ ] bajar piezas
- [ ] subir piezas
- [ ] modificar segmentación
- [ ] detener
- [ ] descartar

>

---



### Corrida 20260907_223302_395316

| Parámetro | Valor |
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
| Piezas generadas | 18 |

Salida:

- `resultados/Input_003_despiece_piezas50_exp0p07_var1p0_dir32_capas20_20260907_223302_395316.jpg`

**Lectura perceptiva**:

- [ ] Demasiado estable — todavía aparece primero la escena y después el despiece
- [ ] Destruida demasiado rápido — solo aparecen fragmentos sin posibilidad de reconstrucción
- [ ] Zona de fricción — las piezas son reconocibles pero la escena exige rearme mental

**¿Qué aparece primero al mirar?**

- [ ] Fotografía
- [ ] Despiece técnico
- [ ] Oscila entre ambos

**Qué pasa con:**
continuidad · figura/fondo · posición · objeto · fragmento · reconocimiento

>

**Decisión:**

- [ ] bajar explosión
- [ ] subir explosión
- [ ] bajar piezas
- [ ] subir piezas
- [ ] modificar segmentación
- [ ] detener
- [ ] descartar

>

---



### Corrida 20260907_224433_482869

| Parámetro | Valor |
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
| Piezas generadas | 18 |

Salida:

- `resultados/OB028_input_despiece_piezas50_exp0p07_var1p0_dir32_capas20_20260907_224433_482869.jpg`

**Lectura perceptiva**:

- [ ] Demasiado estable — todavía aparece primero la escena y después el despiece
- [ ] Destruida demasiado rápido — solo aparecen fragmentos sin posibilidad de reconstrucción
- [ ] Zona de fricción — las piezas son reconocibles pero la escena exige rearme mental

**¿Qué aparece primero al mirar?**

- [ ] Fotografía
- [ ] Despiece técnico
- [ ] Oscila entre ambos

**Qué pasa con:**
continuidad · figura/fondo · posición · objeto · fragmento · reconocimiento

>

**Decisión:**

- [ ] bajar explosión
- [ ] subir explosión
- [ ] bajar piezas
- [ ] subir piezas
- [ ] modificar segmentación
- [ ] detener
- [ ] descartar

>

---

