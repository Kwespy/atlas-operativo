```dataview
LIST
FROM "01_OPERACIONES/Intervencion_Fisica"
WHERE contains(file.outlinks, this.file.link)
SORT file.name ASC
```

