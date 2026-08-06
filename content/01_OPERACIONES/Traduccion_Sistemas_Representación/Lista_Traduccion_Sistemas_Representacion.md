```dataview
LIST
FROM "01_OPERACIONES/Traduccion_Sistemas_Representación"
WHERE contains(file.outlinks, this.file.link)
SORT file.name ASC
```

