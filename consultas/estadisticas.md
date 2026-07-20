# Estadísticas

**Barra Queries → Statistics…**

Abre el panel **Statistics**, que calcula y visualiza la distribución estadística de cualquier atributo numérico o categórico de la red, con soporte para clasificación automática, segunda clasificación cruzada y representación gráfica.

<figure><img src="../assets/images/consultas/statistics-panel.png" alt="Panel Statistics con histograma de diámetros de tuberías"><figcaption><p>Panel Statistics con histograma de diámetros de tuberías</p></figcaption></figure>
*Panel Statistics: histograma de diámetros de tuberías con clasificación por intervalos.*

---

## Estructura del panel

El panel Statistics se organiza en dos pestañas:

- **Configuración (Setup)**: define qué se analiza y cómo se clasifica.
- **Informe (Report)**: muestra el histograma y la tabla de resultados. Se activa automáticamente tras ejecutar el análisis.

---

## Pestaña Configuración (Setup)

### Tipo de elemento y propiedad

Selecciona el tipo de elemento (Junctions, Pipes, Tanks…) y la propiedad a analizar. Las propiedades disponibles dependen del tipo seleccionado e incluyen atributos de diseño y, si hay resultados cargados, campos de simulación.

### Clasificación principal

| Parámetro | Descripción |
|-----------|-------------|
| **Campo** | Propiedad por la que clasificar |
| **Método** | Forma de calcular los intervalos (ver tabla siguiente) |
| **Número de clases** | Cuántos grupos se generan |

#### Métodos de clasificación disponibles

| Método | Descripción |
|--------|-------------|
| **Jenks** | Minimiza la varianza intra-clase (Natural Breaks). Idóneo para distribuciones no uniformes. |
| **Pretty Breaks** | Límites de intervalo "redondos". Preferible para presentaciones. |
| **Manual** | El usuario define directamente los límites de cada intervalo. |

### Filtrado previo

Antes de calcular, puedes acotar el conjunto de elementos con una condición sobre el campo analizado:

- Campos **numéricos**: `>=`, `<=`, `=`, `>`, `<`, `≠`, `Range`
- Campos **de lista**: `=`
- Campos **de texto**: `=`, `≠`, `ILIKE`, `NOT ILIKE`, `LIKE`, `NOT LIKE`
- Selecciona **No Filter** para incluir todos los elementos sin restricción.

### Segunda clasificación *(opcional)*

Un grupo colapsable —contraído por defecto— permite definir un **segundo criterio de clasificación** sobre el mismo conjunto de elementos. Al desplegarlo, se configuran:

| Parámetro | Descripción |
|-----------|-------------|
| **Campo** | Segunda propiedad de clasificación |
| **Método** | Equal Count, Fixed Interval, Manual o Categorized |
| **Número de clases** | Grupos de la segunda clasificación |

Cuando la segunda clasificación está activa, la tabla de resultados se convierte en una **matriz cruzada**: las filas representan los grupos de la primera clasificación y las columnas los grupos de la segunda.

---

## Pestaña Informe (Report)

La pestaña Report se divide en dos marcos: **Histograma** y **Tabla**.

### Histograma

El histograma muestra la distribución de la propiedad analizada:

- **Selector de estadístico**: elige qué se representa en el eje Y: Count (recuento), Sum, Avg, Min, Max o StdD.
- **Botón expandir**: abre el histograma en una **ventana flotante independiente**, útil para tener el panel de configuración y el gráfico visibles a la vez.
- El título del gráfico aparece dentro del propio área del gráfico, limitado a dos líneas.
- Para campos categóricos, el histograma muestra barras por categoría en lugar de intervalos numéricos.

### Tabla de resultados

La tabla muestra los mismos datos en formato tabular:

- Los valores se formatean con los decimales correspondientes a cada campo según el CSV de unidades del proyecto.
- Los números enteros se muestran sin decimales.
- La **fila de exportación** incluye un selector de estadístico para elegir qué valor se vuelca al exportar a CSV (Count, Sum, Avg…).
- Cuando la segunda clasificación está activa, la tabla se convierte en una **matriz cruzada** con columnas adicionales para cada grupo de la segunda clasificación.

---

## Campos disponibles

### Campos categóricos

Los siguientes campos se tratan como categorías (valores discretos):

| Campo | Descripción |
|-------|-------------|
| `Material` | Material de la tubería |
| `Type` | Tipo de elemento |
| `IniStatus` | Estado operacional inicial (Open / Closed / CV) |
| `InstalDate` | Fecha de instalación |
| `Tag` | Etiqueta libre |

### Campos numéricos de entrada

Cualquier campo numérico del modelo: `Diameter`, `Length`, `Roughness`, `Elevation`, `BaseDem`, etc.

### Campos de resultado de simulación

Disponibles solo si hay resultados cargados:

**Nudos:**

| Campo | Descripción |
|-------|-------------|
| `Pressure` | Presión (m.c.a.) |
| `Head` | Altura piezométrica (m) |
| `Demand` | Demanda calculada (l/s) |
| `Quality` | Calidad del agua |

**Tuberías:**

| Campo | Descripción |
|-------|-------------|
| `Status` | Estado en simulación |
| `Flow` | Caudal (l/s) |
| `Velocity` | Velocidad (m/s) |
| `HeadLoss` | Pérdida de carga (m) |
| `UnitHdLoss` | Pérdida unitaria (m/km) |
| `FricFactor` | Factor de fricción |
| `ReactRate` | Tasa de reacción |
| `Quality` | Calidad del agua |

---

## Notas de uso

- El panel Statistics no modifica ningún dato del modelo.
- Puedes mantener el panel abierto mientras navegas por el mapa o cambias parámetros; actualiza el cálculo al pulsar de nuevo el botón de ejecutar.
- La segunda clasificación está contraída por defecto; desplégala solo cuando necesites el análisis cruzado.
