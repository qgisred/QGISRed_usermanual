# Elevation Interpolation (Elevation)

QGISRed allows you to automatically assign elevation to all specific elements (nodes, reservoirs and reservoirs) using digital terrain models in ASCII format.

### MDT file format (ASCII)
The file must follow the standard ASCII raster mesh structure:



```text
NCOLS 100
NROWS 100
XLLCENTER 450000
YLLCENTER 4400000
CELLSIZE 5
NODATA_VALUE -9999
[Valores de elevación separados por espacios]
```



* **XLLCENTER/YLLCENTER**: Coordinates of the center of the lower left cell.
* **CELLSIZE**: Mesh resolution.
* **NODATA_VALUE**: Value to be ignored during interpolation.

### Application Rules
1. **Selectivity**: Only nodes that have the default elevation value (0 or the one configured in options) are interpolated.
2. **Preservation**: If a node already has a manually assigned or imported dimension, the plugin will respect that value and will not overwrite it.
3. **Coverage**: If an element falls outside the MDT mesh, an incident notice will be issued.