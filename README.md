# Atlas Operativo

Atlas Operativo es un archivo de operaciones de transformación de la imagen. Cada operación documenta un procedimiento, sus variables, sus resultados y su relación con otros procesos.

## Fuentes del proyecto

- `ATLAS_OPERATIVO` es el vault canónico de Obsidian y la referencia editorial principal. Puede ordenarse, corregirse y reorganizarse siguiendo las reglas de conservación de este documento.
- `ATLAS_WEB_QUARTZ` contiene la versión pública preparada para su publicación web.
- El contenido español es la fuente de verdad.
- La versión inglesa se genera y actualiza antes de cada publicación.

## Regla de conservación

El material irremplazable tiene prioridad absoluta. Fotos, vídeos, audios, imágenes originales, scripts creativos, archivos de proyecto únicos y cualquier otro material difícil de recuperar no se elimina, sobreescribe ni mueve sin comprobar primero su identidad y su destino.

El texto Markdown y la documentación pueden corregirse, reorganizarse o regenerarse cuando exista una copia controlada o cuando Git permita recuperar el estado anterior. Aun así, no se debe borrar texto único si puede conservarse mediante una reorganización.

`ATLAS_OPERATIVO` puede ordenarse y modificarse porque es el proyecto canónico, pero todo cambio estructural debe conservar los materiales originales. Quartz se actualiza después a partir del Atlas Operativo ordenado.

Antes de eliminar cualquier archivo cuya recuperación o regeneración sea incierta, se debe consultar al propietario. Los duplicados demostrados, cachés, dependencias y archivos de prueba regenerables sí pueden eliminarse siguiendo el alcance autorizado.

## Estructura

- `content/`: contenido público en español.
- `content_en/`: traducción pública en inglés.
- `SOPORTE_TECNICO/`: únicamente archivos técnicos necesarios para mantener o publicar el sitio.
- `quartz.config.yaml`: configuración de Quartz.
- `Agents.md`: reglas para agentes y automatizaciones.
- `CONTRIBUTING.md`: normas para colaboradores.
- `CHANGELOG.md`: historial de cambios publicados.

## Flujo de publicación

1. Se ordena y revisa el contenido canónico en español en `ATLAS_OPERATIVO`.
2. Se comprueba que fotos, vídeos y demás materiales importantes siguen localizables.
3. Se prepara la copia española en Quartz.
4. Se genera o actualiza la traducción inglesa.
5. Se comprueban enlaces, imágenes, fichas e índices.
6. Se construye la web.
7. Se revisa el resultado y se publica.

## Incorporación de una operación nueva

Las operaciones se prueban primero sin número en `ATLAS_OPERATIVO/05_NO_CLASIFICADAS/`. Pasan al Atlas como `OB_NNN` solo cuando el autor lo confirma. El procedimiento completo está en `ATLAS_OPERATIVO/AGENTS.md`, sección "Paso de una operación no clasificada al Atlas". En resumen:

1. Se asigna el siguiente `OB_NNN` libre y el régimen.
2. Se copian las salidas a `NNN_PROCESO/resultados/` como `OBNNN_step01…`, en orden cronológico. Los parámetros de cada una quedan en los metadatos EXIF de la imagen.
3. `NNN_PROCESO/codigo/` guarda solo el script, adaptado a su nueva ubicación. Todo lo escrito va en la ficha (`NNN_FICHA/`).
4. Se actualizan los inventarios y se prueba el script desde su lugar definitivo.
5. Tras verificar la copia, se elimina el experimento de `05_NO_CLASIFICADAS`.
6. La operación queda `En revisión` hasta que el autor elige la imagen de crisis.

La operación llega a la web en la siguiente publicación, siguiendo el flujo anterior.

## Estado inicial

La organización documental comienza con la versión `v0.1.0`.
