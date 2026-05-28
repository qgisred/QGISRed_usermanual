# Estadísticas

**Barra Queries → Statistics…**

Abre el panel **Statistics**, que calcula y visualiza la distribución estadística de cualquier atributo numérico o categórico de la red, con soporte para clasificación automática y representación como histograma.

> **Nota**: Esta herramienta está en desarrollo activo. Las funcionalidades descritas aquí corresponden a lo implementado actualmente; algunas opciones pueden variar o ampliarse en versiones futuras.

![Panel Statistics con histograma de diámetros de tuberías](../assets/images/consultas/statistics-panel.png)
*Panel Statistics: histograma de diámetros de tuberías con clasificación por intervalos.*

---

## Campos disponibles

### Campos categóricos

Los siguientes campos se tratan como categorías (valores discretos, sin operaciones de media o percentil):

| Campo | Descripción |
|-------|-------------|
| `Material` | Material de la tubería |
| `Type` | Tipo de elemento |
| `Status` | Estado operacional (Open / Closed / CV) |
| `InstalDate` | Fecha de instalación |
| `Tag` | Etiqueta libre |

Para campos categóricos, la estadística muestra el recuento de elementos por cada valor distinto.

### Campos numéricos de entrada

Cualquier campo numérico del modelo: `Diameter`, `Length`, `Roughness`, `Elevation`, `Demand`, `InstallYear`, etc.

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

## Métodos de clasificación

Para campos numéricos, el panel permite elegir cómo se agrupan los valores en intervalos:

| Método | Descripción |
|--------|-------------|
| **Jenks** | Minimiza la varianza dentro de cada clase (Natural Breaks). Agrupa mejor valores con distribución no uniforme. |
| **Pretty Breaks** | Genera intervalos con límites "redondos" fáciles de leer. Preferible para presentaciones. |
| **Manual** | El usuario define directamente los límites de cada intervalo. |

El número de clases es configurable en todos los métodos.

---

## Filtrado previo

Antes de calcular la estadística, puedes aplicar condiciones de filtrado sobre el campo analizado:

- Para campos **numéricos**: `>=`, `<=`, `=`, `>`, `<`, `≠`, `Range`
- Para campos **de lista**: `=`
- Para campos **de texto**: `=`, `≠`, `ILIKE`, `NOT ILIKE`, `LIKE`, `NOT LIKE`

El filtro limita el conjunto de elementos incluidos en el cálculo estadístico.

---

## Histograma

El panel muestra un **histograma** de la distribución del campo seleccionado. El eje X representa los intervalos de valor y el eje Y el número de elementos en cada intervalo.

Para campos categóricos, el histograma muestra barras por categoría en lugar de intervalos numéricos.

---

## Notas de uso

- El panel Statistics no modifica ningún dato del modelo.
- Puedes mantener el panel abierto mientras navegas por el mapa o cambias parámetros de simulación; actualiza el cálculo al pulsar de nuevo el botón de ejecutar.
- La integración completa con resultados de simulación por período de tiempo (series temporales) está prevista para versiones futuras.
