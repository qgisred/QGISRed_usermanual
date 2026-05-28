# 🔧 Tools

La barra **Tools** agrupa las herramientas de procesamiento masivo: cálculo automático de propiedades hidráulicas, asignación de demandas desde fuentes externas, gestión de escenarios y análisis topológico. A diferencia de las herramientas de Edition, estas actúan sobre el conjunto de la red o sobre grandes selecciones, no elemento a elemento.

![Barra de herramientas Tools de QGISRed](../assets/images/herramientas/barra-tools.png)
*Barra Tools: propiedades hidráulicas, demandas y escenarios, análisis topológico.*

---

## Herramientas de la barra Tools

### Grupo 1 — Propiedades hidráulicas

| # | Herramienta | Función |
|---|-------------|---------|
| 1 | **Automatically calculate pipe lengths** | Recalcula la longitud de cada tubería a partir de su geometría |
| 2 | **Interpolate elevation from .asc files…** | Asigna cotas a los nudos interpolando desde un MDT en formato ASC |
| 3 | **Set roughness coefficients (from Material and Date)** | Calcula la rugosidad actual de cada tubería por envejecimiento |
| 4 | **Convert roughness coefficients…** | Convierte rugosidades entre fórmulas H-W, D-W y C-M |

### Grupo 2 — Demandas y escenarios

| # | Herramienta | Función |
|---|-------------|---------|
| 5 | **Nodal demand builder…** | Asigna demandas a nudos desde capas SHP externas (puntos o polígonos) |
| 6 | **Scenario builder…** | Exporta e importa en bloque parámetros del modelo para gestionar escenarios |
| 7 | **Isolated segments…** | Identifica qué válvulas cerrar para aislar un tramo y qué zonas quedan sin servicio |

### Grupo 3 — Análisis topológico

| # | Herramienta | Función |
|---|-------------|---------|
| 8 | **Obtain demand sectors** | Genera sectores de demanda delimitados por caudalímetros |
| 9 | **Minimum Cost Tree…** | Calcula el árbol de mínimo coste desde un nudo seleccionado |

---

## En esta sección

* [Longitudes y elevaciones](elevacion.md) — cálculo de longitudes y asignación de cotas desde MDT
* [Rugosidades](rugosidad.md) — asignación por envejecimiento y conversión entre fórmulas
* [Gestor de demandas](demandas.md) — asignación masiva de demandas desde capas externas
* [Escenarios y análisis](escenarios.md) — escenarios, segmentos aislados, sectores de demanda y árbol
