# Gestor de Demandas

**Barra Tools → Nodal demand builder…**

El gestor de demandas nodales permite asignar consumos a los nudos de la red de forma masiva a partir de capas SHP externas. Es la herramienta principal para integrar datos de facturación, censos de usuarios o estimaciones por polígono en el modelo EPANET.

![Diálogo del Nodal demand builder con opciones de fuente y método de asignación](../assets/images/herramientas/demand-builder.png)
*Nodal demand builder: selección de capas de origen, método de asignación y opciones de limpieza.*

---

## Fuentes de datos soportadas

El gestor acepta capas vectoriales SHP externas cargadas en QGIS que no pertenezcan al proyecto QGISRed:

| Tipo de geometría | Método de asignación |
|-------------------|----------------------|
| **Puntos** | Cada punto se asigna al nudo más cercano dentro de un radio de búsqueda. El valor de demanda se lee de un campo configurable de la capa. |
| **Polígonos** | La demanda total del polígono se reparte proporcionalmente entre todos los nudos que caen dentro de él (proporcional al número de nudos o al área de influencia de Voronoi de cada nudo). |
| **Líneas** | La demanda de cada tramo lineal se distribuye entre los nudos más cercanos a lo largo del eje de la línea. |

---

## Proceso de asignación

1. Carga en QGIS la capa SHP externa con los datos de consumo (antes de abrir el gestor).
2. Activa **Nodal demand builder**. El diálogo muestra automáticamente las capas externas detectadas.
3. Configura para cada capa:
   - **Campo de demanda**: columna del SHP que contiene el valor de consumo.
   - **Campo de categoría**: columna que identifica el tipo de usuario (residencial, industrial, etc.) — se usa para crear demandas múltiples por categoría.
   - **Campo de patrón**: columna con el ID del patrón de demanda a aplicar (opcional).
   - **Método de distribución**: por proximidad, por polígono o proporcional.
4. Opcionalmente, selecciona nudos concretos en el mapa para limitar la asignación a esa zona.
5. Confirma. QGISRed escribe los valores en la capa `Junctions` o en la capa de demandas múltiples si corresponde.

---

## Demandas múltiples por categoría

Si la capa externa tiene un campo de categoría, QGISRed crea una entrada separada en `{Red}_MultipleDemands.shp` por cada combinación nudo–categoría. Así un mismo nudo puede tener demanda residencial, comercial e industrial con patrones distintos.

---

## Resultado en la capa del mapa

Tras la asignación, la capa resultante del Demand Builder se muestra en el mapa con:
- **Colores por categoría** (una categoría = un color aleatorio persistente durante la sesión).
- **Etiquetas** con el valor de demanda asignado al nudo.
- Los nudos sin categoría asignada aparecen en **naranja** (etiqueta `Undefined`).

---

## Limpieza de demandas

El gestor incluye opciones para eliminar demandas existentes antes de asignar las nuevas:
- **Borrar demandas de nudos seleccionados**: elimina los valores del campo `Demand` y las entradas de `MultipleDemands` de los nudos seleccionados.
- **Eliminar patrones huérfanos**: después del borrado, elimina del proyecto los patrones que ya no estén referenciados por ningún nudo.

> Usa la limpieza selectiva cuando actualices los datos de consumo de una zona concreta sin afectar al resto del modelo. Para una carga completa desde cero, limpia toda la red antes de importar.
