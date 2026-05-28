# Longitudes y Elevaciones

Las dos primeras herramientas de la barra Tools calculan propiedades geométricas básicas — longitud y cota — de forma masiva a partir de fuentes de datos externas o de la propia geometría del SHP.

---

## Automatically calculate pipe lengths

**Barra Tools → Automatically calculate pipe lengths**

Recalcula el campo `Length` de cada tubería seleccionada (o de todas si no hay selección) utilizando la longitud geométrica real medida sobre los vértices del SHP en las unidades del CRS del proyecto.

### Cuándo usarla

- Tras mover vértices o nudos con las herramientas de Edition sin haber actualizado el atributo.
- Después de importar desde un `.inp` cuyas longitudes difieren de la geometría real (coordenadas en escala distinta o proyección diferente).
- Como paso previo a **Check pipe lengths** (Barra Debug) para dejar todos los valores sincronizados antes de la auditoría.

### Comportamiento

La herramienta sobreescribe el valor de `Length` con la longitud calculada. No pregunta confirmación ni filtra por tolerancia: actualiza todas las tuberías del ámbito de selección incondicionalmente.

> Usa siempre un CRS métrico proyectado (UTM, LCC, etc.). Si el proyecto usa coordenadas geográficas (grados decimales), la longitud calculada estará en grados, no en metros, y será inútil para la simulación.

---

## Interpolate elevation from .asc files…

**Barra Tools → Interpolate elevation from .asc files…**

Asigna la cota (campo `Elevation`) a los nudos, depósitos y embalses del proyecto interpolando su valor desde uno o varios Modelos Digitales del Terreno (MDT) en formato ASC.

![Selector de archivos ASC para interpolación de cotas](../assets/images/herramientas/interpolate-elevation.png)
*Selector de archivos MDT: puedes cargar varios archivos ASC para cubrir toda el área de la red.*

### Formato ASC soportado

```
ncols         500
nrows         400
xllcenter     450000.0
yllcenter     4400000.0
cellsize      5.0
nodata_value  -9999
230.4 231.1 231.8 ...
```

| Cabecera | Significado |
|----------|-------------|
| `ncols` / `nrows` | Número de columnas y filas de la malla |
| `xllcenter` / `yllcenter` | Coordenadas del centro de la celda inferior-izquierda |
| `cellsize` | Tamaño de celda en las unidades del CRS |
| `nodata_value` | Valor que el plugin ignora (celda sin dato) |

También se acepta `xllcorner` / `yllcorner` (esquina en lugar de centro de celda).

### Proceso de asignación

1. Abre el selector de archivos y elige uno o más archivos `.asc`. Puedes combinar varios MDT para cubrir el área completa de la red.
2. QGISRed proyecta la coordenada de cada nudo sobre la malla y obtiene la elevación por interpolación bilineal entre las cuatro celdas vecinas.
3. Solo se actualizan los nudos cuyo `Elevation` actual sea igual al valor por defecto configurado en **Valores por defecto** (típicamente 0). Los nudos con cota ya asignada manualmente no se modifican.
4. Los nudos que caen fuera de la extensión de todos los MDT cargados quedan marcados como incidencia en el panel de mensajes.

### Consejos

- El CRS del archivo ASC debe coincidir con el CRS del proyecto. Si no coinciden, las coordenadas no se proyectan y los nudos quedarán fuera de la malla.
- Para redes que abarcan varias hojas MDT, carga todos los archivos en un solo lanzamiento de la herramienta: el plugin los trata como un mosaico continuo.
- Tras la interpolación, revisa los nudos con cota = 0 o con incidencia registrada. Asígnales la cota manualmente si están en zona sin cobertura MDT.
