```dataview
LIST
FROM "01_OPERACIONES/Transformacion_Algoritmica"
WHERE contains(file.outlinks, this.file.link)
SORT file.name ASC
```

