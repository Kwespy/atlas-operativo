```dataview
LIST
FROM "01_OPERACIONES/Captura_Materializacion"
WHERE contains(file.outlinks, this.file.link)
SORT file.name ASC
```

