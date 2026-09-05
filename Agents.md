# Agents

## Alcance

Estas reglas se aplican a cualquier agente que trabaje en `ATLAS_WEB_QUARTZ`.

## Fuente canónica

`ATLAS_OPERATIVO` es el vault canónico de Obsidian. Se puede ordenar, corregir y reorganizar cuando sea necesario. Quartz debe actualizarse después a partir de esa versión canónica.

La prioridad de conservación es: fotos y vídeos originales, audios, imágenes únicas, archivos de proyecto difíciles de recuperar, scripts creativos y, después, texto Markdown. Un script que haya sido pensado o creado como parte de una operación es material creativo y no se elimina aunque técnicamente pudiera volver a escribirse. Los materiales irremplazables no se eliminan, sobreescriben ni mueven sin comprobación previa. El Markdown puede corregirse o regenerarse si existe una copia controlada o historial recuperable.

## Reglas editoriales

- El español es el idioma de trabajo y la referencia editorial.
- No inventar datos, fechas, herramientas, resultados ni imágenes.
- Si una ficha está incompleta, completar solo lo que esté respaldado por el material existente y marcar lo demás como pendiente de revisión.
- Señalar los errores conceptuales o las ambigüedades para revisión humana.
- Mantener el identificador `OB_###` de cada operación.
- Corregir ortografía, puntuación y consistencia cuando el sentido esté claro.
- Mantener todos los materiales originales importantes del Atlas Operativo, especialmente fotos, vídeos y scripts creativos.

## Quartz

- `content/` contiene la versión española publicada.
- `content_en/` contiene la versión inglesa publicada.
- La traducción inglesa debe actualizarse antes de cada publicación.
- No modificar manualmente la versión inglesa para resolver una diferencia de contenido: corregir primero el español y volver a traducir.
- No borrar archivos de Quartz salvo que sean duplicados, cachés, pruebas o soportes confirmados como innecesarios.
- No mover archivos o carpetas salvo que sea necesario para corregir la estructura.

## Fichas

Cada ficha debe conservar, cuando sea aplicable, su descripción, herramientas, procedimiento, variables, resultado, lectura conceptual, secuencia visual y archivos relacionados. Los campos desconocidos deben quedar claramente identificados, nunca rellenarse por suposición.

## Comprobaciones antes de publicar

- No hay identificadores duplicados.
- Las listas incluyen las operaciones existentes.
- Los enlaces internos apuntan a páginas válidas.
- Las imágenes y vídeos enlazados existen.
- No quedan marcadores accidentales como `OB___`, `OB_000`, `Pending`, `TODO` o listas vacías sin justificar.
- La versión inglesa corresponde a la versión española.
- El sitio se construye correctamente.

## Cambios destructivos

Antes de eliminar cualquier archivo cuya recuperación o regeneración sea incierta, presentar una lista exacta y esperar autorización. Los cambios destructivos autorizados en Quartz deben limitarse a archivos innecesarios y describirse en el `CHANGELOG.md`. Nunca eliminar fotos, vídeos ni scripts creativos sin confirmación explícita.
