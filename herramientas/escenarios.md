# Escenarios y Análisis

Las últimas cuatro herramientas de la barra Tools cubren funciones de análisis y gestión de escenarios: gestión de variantes del modelo, identificación de segmentos de aislamiento, sectorización por demanda y análisis de árbol de mínimo coste.

---

## Scenario builder…

**Barra Tools → Scenario builder…**

Permite exportar e importar en bloque un conjunto de parámetros del modelo, creando "fotografías" del estado de la red que pueden aplicarse de nuevo más adelante. Es la herramienta para gestionar variantes del modelo sin crear proyectos separados.

### Qué parámetros gestiona

| Parámetro | Descripción |
|-----------|-------------|
| **Roughness** | Coeficientes de rugosidad de todas las tuberías |
| **InitStatus** | Estados de apertura/cierre de tuberías y válvulas |
| **Demands** | Demandas base de todos los nudos |
| **InitQuality** | Calidades iniciales de nudos y tuberías |
| **Elevations** | Cotas de nudos, depósitos y embalses |

### Flujo de trabajo típico

1. Construye el modelo en el estado actual (año base).
2. Exporta el escenario base con **Scenario builder → Exportar**.
3. Modifica los parámetros del modelo para el horizonte futuro (nuevas demandas, tuberías envejecidas, estados de válvulas modificados…).
4. Exporta el escenario futuro con otro nombre.
5. Para comparar o restaurar, usa **Scenario builder → Importar** y selecciona el archivo de escenario deseado.

Los archivos de escenario se guardan en formato CSV en la carpeta del proyecto.

---

## Isolated segments…

**Barra Tools → Isolated segments…**

Responde a la pregunta operacional: **"¿Qué válvulas debo cerrar para reparar esta tubería, y qué usuarios quedarán sin servicio?"**

![Resultado de Isolated segments: tubería afectada y válvulas de corte resaltadas](../assets/images/herramientas/isolated-segments.png)
*Isolated segments: en rojo la tubería a reparar, en amarillo las válvulas a cerrar y en azul la zona sin servicio.*

### Proceso

1. Activa la herramienta. El cursor cambia a modo selección.
2. Haz clic sobre la tubería que necesita ser reparada o aislada.
3. QGISRed calcula el **segmento mínimo** que quedaría aislado al cerrar las válvulas manuales más cercanas:
   - Identifica todas las válvulas de corte (manuales o isolation valves) accesibles desde ese tramo.
   - Determina qué combinación de válvulas cierra el área mínima necesaria para aislar la avería.
4. El resultado se muestra en el mapa:
   - **Tubería objetivo**: resaltada en rojo.
   - **Válvulas a cerrar**: resaltadas en amarillo.
   - **Zona sin servicio** (afectados colaterales): nudos y tuberías en azul.
5. Puedes hacer clic en más tuberías para acumular el análisis (misma sesión de herramienta activa).

### Salida

Se genera una capa auxiliar `IsolatedSegments` con la información del segmento aislado. Esta capa es informativa y no modifica el modelo.

---

## Obtain demand sectors

**Barra Tools → Obtain demand sectors**

Genera una sectorización de la red basada en la presencia de **caudalímetros** (flow meters). Cada sector de demanda es la subred suministrada por un único caudalímetro, sin cruzar otros caudalímetros.

### Diferencia con los sectores hidráulicos

| Sectores hidráulicos (Debug) | Sectores de demanda (Tools) |
|------------------------------|------------------------------|
| Basados en fuentes (Tank/Reservoir) | Basados en caudalímetros |
| Responden a "¿de dónde viene el agua?" | Responden a "¿qué mide cada caudalímetro?" |
| Clasificación H-Q / nH-Q / etc. | Sin clasificación de tipo |
| Para diagnóstico antes de simular | Para análisis de balance hídrico |

### Uso

La herramienta no necesita configuración. Genera la capa `DemandSectors` en el mapa coloreando cada sector con un color diferente. Si la red no tiene caudalímetros cargados, el resultado es un único sector con toda la red.

---

## Minimum Cost Tree…

**Barra Tools → Minimum Cost Tree…**

Calcula el **árbol de expansión de mínimo coste** de la red desde un nudo seleccionado. Muestra el camino hidráulicamente más eficiente (menor resistencia acumulada) desde ese nudo hasta todos los demás puntos de la red.

### Proceso

1. Activa la herramienta.
2. Haz clic sobre el nudo de origen (por ejemplo, una fuente de suministro o un punto de entrega).
3. QGISRed calcula el árbol de mínima resistencia hidráulica y genera una capa con el resultado.

### Interpretación del resultado

El árbol resultante muestra qué camino seguiría el agua naturalmente desde el nudo de origen si no hubiera bucles en la red. Es útil para:
- Identificar tuberías que siempre trabajan en un único sentido de flujo.
- Detectar tuberías redundantes en la topología.
- Analizar la estructura de suministro en redes ramificadas o en condiciones de emergencia (con parte de la red cerrada).

La capa generada (`Tree`) se añade al proyecto con la distancia acumulada desde el origen etiquetada en cada tramo.
