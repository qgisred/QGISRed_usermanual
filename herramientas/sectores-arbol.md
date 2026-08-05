# Sectores de Demanda y Árbol

Las dos últimas herramientas de la barra Tools realizan análisis topológicos sobre la red: sectorización por caudalímetros y cálculo del árbol de mínimo coste desde un nudo origen.

---

## Constructor de sectores de demanda…

**Barra Tools → Constructor de sectores de demanda…**

Genera una sectorización de la red basada en la presencia de **caudalímetros** (flow meters). Cada sector de demanda es la subred suministrada por un único caudalímetro, sin cruzar otros caudalímetros.

### Diferencia con los sectores hidráulicos

| | Sectores hidráulicos (Barra Debug) | Sectores de demanda (Barra Tools) |
|-|-------------------------------------|-----------------------------------|
| **Base** | Presencia de Tank o Reservoir | Presencia de caudalímetros |
| **Pregunta** | ¿De dónde viene el agua? | ¿Qué mide cada caudalímetro? |
| **Clasificación** | H-Q / H-nQ / nH-Q / nH-nQ | Sin tipo, solo coloreado por sector |
| **Uso** | Diagnóstico antes de simular | Balance hídrico por sector |

### Resultado

La herramienta genera la capa `DemandSectors` en el mapa, con cada sector en un color diferente. Si la red no tiene caudalímetros cargados, el resultado es un único sector que abarca toda la red.

No requiere configuración: se lanza directamente sin diálogo.

---

## Minimum Cost Tree…

**Barra Tools → Minimum Cost Tree…**

Calcula el **árbol de expansión de mínimo coste** de la red desde un nudo seleccionado. Muestra el camino hidráulicamente más eficiente (menor resistencia acumulada) desde ese nudo hasta todos los demás puntos alcanzables de la red.

### Proceso

1. Activa la herramienta.
2. Haz clic sobre el nudo de origen (por ejemplo, una fuente de suministro o un punto de entrega de agua en alta).
3. QGISRed calcula el árbol y genera la capa `Tree` en el mapa, con la distancia acumulada desde el origen etiquetada en cada tramo.

### Interpretación del resultado

El árbol resultante muestra qué camino seguiría el agua desde el nudo de origen si la red fuera puramente ramificada (sin bucles). Es útil para:

- Identificar tuberías que siempre trabajan en un único sentido de flujo.
- Detectar tuberías redundantes en la topología (no aparecen en el árbol porque hay un camino más corto).
- Analizar la estructura de suministro en condiciones de emergencia con parte de la red cerrada.
- Planificar esquemas de sectorización de presión.

### Identificación del nodo raíz

En la capa de nudos generada por el árbol, el nudo de origen (raíz) se identifica con el valor **"ROOT"** en el campo `NodeType`. El resto de nudos llevan su tipo EPANET habitual (Junction, Tank, Reservoir…). Esto permite crear reglas de simbología específicas para el nodo raíz directamente en QGIS.
