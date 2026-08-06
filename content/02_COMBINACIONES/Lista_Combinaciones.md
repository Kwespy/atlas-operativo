```dataview
LIST
FROM "02_COMBINACIONES"
WHERE contains(file.outlinks, this.file.link)
SORT file.name ASC
```
