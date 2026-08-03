# Estadísticas

**Barra Queries → Statistics…**

Abre el panel **Statistics**, que calcula y visualiza la distribución estadística de cualquier atributo numérico o categórico de la red, con soporte para clasificación automática, segunda clasificación cruzada y representación gráfica.

> **ℹ️ Nota:** El panel Statistics se abre **acoplado** en la ventana principal de QGIS y respeta los paneles ya agrupados en pestañas. Sus controles se adaptan también a anchos de panel estrechos, sin recortarse en el borde derecho.

\*Panel Statistics: histograma de diámetros de tuberías con clasificación por intervalos.\*

***

## Estructura del panel

El panel Statistics se organiza en dos pestañas:

* **Configuración (Setup)**: define qué se analiza y cómo se clasifica.
* **Informe (Report)**: muestra el histograma y la tabla de resultados. Se activa automáticamente tras ejecutar el análisis.

***

## Pestaña Configuración (Setup)

### Tipo de elemento y propiedad

Selecciona el tipo de elemento (Junctions, Pipes, Tanks…) y la propiedad a analizar. El selector de propiedad muestra en una **lista unificada** tanto los campos de diseño (Diámetro, Longitud, Rugosidad…) como los campos de resultado de simulación (Presión, Caudal, Velocidad…). Los campos de resultado aparecen con **fondo amarillo/crema** para diferenciarlos visualmente de los campos de diseño.

### Clasificación principal

| Parámetro            | Descripción                                            |
| -------------------- | ------------------------------------------------------ |
| **Campo**            | Propiedad por la que clasificar                        |
| **Método**           | Forma de calcular los intervalos (ver tabla siguiente) |
| **Número de clases** | Cuántos grupos se generan                              |

#### Métodos de clasificación disponibles

Los métodos siguientes están disponibles tanto para la clasificación principal como para la segunda clasificación. El método por defecto es **Pretty Breaks**.

| Método                     | Descripción                                                                      |
| -------------------------- | -------------------------------------------------------------------------------- |
| **Jenks (Natural Breaks)** | Minimiza la varianza intra-clase. Idóneo para distribuciones no uniformes.       |
| **Pretty Breaks**          | Límites de intervalo "redondos". Preferible para presentaciones. _(Por defecto)_ |
| **Equal Count**            | Cada clase contiene el mismo número de elementos.                                |
| **Fixed Interval**         | Todos los intervalos tienen la misma amplitud.                                   |
| **Manual**                 | El usuario define directamente los límites de cada intervalo.                    |

> **ℹ️ Nota:** Cuando todos los valores son idénticos o muy similares, los extremos de clase duplicados se colapsan mostrando un único valor en lugar de "100.0 - 100.0".

> **ℹ️ Nota — Campos sin datos útiles:** Si el campo elegido para clasificar no tiene ningún valor calculado, el panel no muestra un aviso de error: genera directamente una única clase **NULL** que agrupa todos los elementos sin valor. Si el campo tiene valores pero todos son iguales (incluido el caso de que todos sean cero), se genera una única clase con ese valor, igual que en el caso anterior de extremos colapsados. En ambos casos el histograma y la tabla se generan con normalidad, sin interrumpir el análisis.

> **ℹ️ Nota:** Cuando se analiza un campo de resultado de simulación dinámico, los **límites de clase se calculan una vez** considerando todos los instantes de tiempo simultáneamente. Al avanzar el paso de simulación, el recuento de elementos por barra varía, pero los límites permanecen constantes, lo que permite **comparar distribuciones entre instantes de tiempo** con total coherencia.

### Filtrado previo

Antes de calcular, puedes acotar el conjunto de elementos con una condición sobre cualquier campo:

* Campos **numéricos**: `>=`, `<=`, `=`, `>`, `<`, `≠`, `Range`
* Campos **de lista**: `=`
* Campos **de texto**: `=`, `≠`, `ILIKE`, `NOT ILIKE`, `LIKE`, `NOT LIKE`
* Selecciona **No Filter** para incluir todos los elementos sin restricción.

El campo **Valor** incluye un botón de borrado **(×)**: al pulsarlo, limpia el texto introducido y deja sin selección activa, facilitando cambiar el filtro rápidamente.

Cuando el atributo de filtro es un campo de resultado de simulación, el combo muestra el mismo **fondo amarillo/crema** que se usa para estos campos en el selector de propiedad.

> **ℹ️ Nota — Caudal:** Al filtrar por el campo `Flow` con un valor numérico escrito, el valor se interpreta siempre como **valor absoluto**, por lo que no es necesario conocer el signo que EPANET asigna internamente al caudal.

### Restringir a la selección activa

La casilla **Only selected elements** limita el análisis a los elementos actualmente seleccionados en el mapa. La selección se evalúa de forma conjunta entre la capa de **Inputs** y su correspondiente capa de **Results**: si el elemento está seleccionado en cualquiera de las dos capas del mismo tipo (por ejemplo, `Pipes` en Inputs y su tema de resultados de tuberías), se incluye en el cálculo.

> ⚠️ Si activas la casilla y no hay ningún elemento seleccionado en ninguna de las dos capas, el panel muestra un aviso y no ejecuta el análisis.

Mientras la casilla está activa, tanto el histograma como la tabla muestran una nota indicando que hay un filtro de selección (y, si además hay un filtro de atributo activo, ambos se combinan en el mismo texto).

#### Vista previa en el mapa

La sección Filters incluye dos elementos adicionales para explorar el filtro antes de ejecutar el análisis completo:

* **Casilla "Vista previa en el mapa"**: cuando está marcada, los elementos que cumplen la condición de filtro se resaltan en **naranja** sobre el lienzo del mapa. La vista previa se actualiza automáticamente al cambiar cualquier parámetro del filtro.
* **Contador de coincidencias** (p. ej. _"43 elementos coinciden"_): visible siempre que la sección Filtros esté desplegada, incluso antes de ejecutar el análisis.

Los resaltes se eliminan automáticamente al cerrar el panel o al contraer la sección Filtros.

### Segunda clasificación _(opcional)_

Un grupo colapsable —contraído por defecto— permite definir un **segundo criterio de clasificación** sobre el mismo conjunto de elementos. Al desplegarlo, se configuran:

| Parámetro            | Descripción                                                                 |
| -------------------- | --------------------------------------------------------------------------- |
| **Campo**            | Segunda propiedad de clasificación                                          |
| **Método**           | Jenks (Natural Breaks), Pretty Breaks, Equal Count, Fixed Interval o Manual |
| **Número de clases** | Grupos de la segunda clasificación                                          |

Cuando la segunda clasificación está activa, la tabla de resultados se convierte en una **matriz cruzada**: las filas representan los grupos de la primera clasificación y las columnas los grupos de la segunda.

> **ℹ️ Nota:** Al cambiar el tipo de elemento y volver al anterior, la configuración de la segunda clasificación (método, número de clases, intervalos, valores manuales) se **recupera automáticamente**.

***

## Pestaña Informe (Report)

La pestaña Report se divide en dos marcos: **Histograma** y **Tabla**.

### Histograma

El histograma muestra la distribución de la propiedad analizada:

* **Selector de estadístico**: elige qué se representa en el eje Y: Count (recuento), Sum, Avg, Min, Max o StdD.
* **Botón expandir**: abre el histograma en una **ventana flotante independiente**, útil para tener el panel de configuración y el gráfico visibles a la vez.
* El **título del gráfico** incluye el estadístico seleccionado como prefijo y las unidades del campo. Por ejemplo: _"Avg Presión (mca) por Diámetros (mm) para Material PVC"_.
* Para campos categóricos, el histograma muestra barras por categoría en lugar de intervalos numéricos.

### Tabla de resultados

La tabla muestra los mismos datos en formato tabular:

* Los valores se formatean con los decimales correspondientes a cada campo según el CSV de unidades del proyecto.
* Los números enteros se muestran sin decimales.
* El **título de la tabla** refleja siempre las dos dimensiones de clasificación activas, incluyendo las unidades de cada campo.
* La **fila de exportación** incluye un selector de estadístico para elegir qué valor se vuelca al exportar a CSV (Count, Sum, Avg…).
* La exportación a CSV incluye los **valores de los puntos de corte manuales** de ambas clasificaciones (principal y segunda), con los encabezados de columna acompañados de las unidades entre paréntesis.
* Cuando la segunda clasificación está activa, la tabla se convierte en una **matriz cruzada** con columnas adicionales para cada grupo de la segunda clasificación.

***

## Campos disponibles

### Campos categóricos

Los siguientes campos se tratan como categorías (valores discretos):

| Campo        | Descripción                                     |
| ------------ | ----------------------------------------------- |
| `Material`   | Material de la tubería                          |
| `Type`       | Tipo de elemento                                |
| `ValveType`  | Tipo de válvula                                 |
| `MeterType`  | Tipo de contador                                |
| `SourceType` | Tipo de fuente                                  |
| `IniStatus`  | Estado operacional inicial (Open / Closed / CV) |
| `InstalDate` | Fecha de instalación                            |
| `InstDate`   | Fecha de instalación                            |
| `Tag`        | Etiqueta libre                                  |

### Campos numéricos de entrada

Cualquier campo numérico del modelo: `Diameter`, `Length`, `Roughness`, `Elevation`, `BaseDem`, etc.

### Campos de resultado de simulación

Disponibles solo si hay resultados cargados:

**Nudos:**

| Campo      | Descripción             |
| ---------- | ----------------------- |
| `Pressure` | Presión (m.c.a.)        |
| `Head`     | Altura piezométrica (m) |
| `Demand`   | Demanda calculada (l/s) |
| `Quality`  | Calidad del agua        |

**Tuberías:**

| Campo        | Descripción             |
| ------------ | ----------------------- |
| `Status`     | Estado en simulación    |
| `Flow`       | Caudal (l/s)            |
| `Velocity`   | Velocidad (m/s)         |
| `HeadLoss`   | Pérdida de carga (m)    |
| `UnitHdLoss` | Pérdida unitaria (m/km) |
| `FricFactor` | Factor de fricción      |
| `ReactRate`  | Tasa de reacción        |
| `Quality`    | Calidad del agua        |

> **⚠️ Nota:** Los campos `Velocity`, `UnitHdLoss`, `FricFactor` y `ReactRate` no están disponibles cuando el tipo de elemento seleccionado es **Pumps** (bombas) o **Valves** (válvulas); son exclusivos de tuberías.

***

## Notas de uso

* El panel Statistics no modifica ningún dato del modelo.
* Puedes mantener el panel abierto mientras navegas por el mapa o cambias parámetros; actualiza el cálculo al pulsar de nuevo el botón de ejecutar.
* La segunda clasificación está contraída por defecto; desplégala solo cuando necesites el análisis cruzado.
