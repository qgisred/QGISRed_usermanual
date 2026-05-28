# Visor de Resultados

Una vez completada la simulación, QGISRed ofrece dos herramientas complementarias para explorar los resultados: el **panel de resultados** (Results dock), que controla la visualización sobre el mapa, y el **panel de series temporales** (Time series dock), que muestra la evolución de cualquier variable a lo largo del tiempo para elementos individuales.

---

## Panel de resultados (Results dock)

El Results dock se ancla en la zona derecha de la pantalla. Contiene dos pestañas:

- **Pestaña 0 — Resultados**: visualización interactiva sobre el mapa con selección de variable y navegación temporal.
- **Pestaña 1 — Status Report**: informe de texto del motor EPANET (accesible también desde **Status report** en la barra).

![Panel de resultados con selector de variable y barra de tiempo](../assets/images/analisis/results-dock.png)
*Results dock: selección de variable, modo de estadística y navegación por instantes de tiempo.*

### Propiedades disponibles

**Nudos** (Junctions, Tanks, Reservoirs):

| Propiedad | Descripción |
|-----------|-------------|
| `Pressure` | Presión en m.c.a. |
| `Head` | Altura piezométrica en m |
| `Demand` | Demanda calculada |
| `Quality` | Calidad del agua (según el tipo configurado en Analysis options) |

**Tuberías, válvulas y bombas** (Links):

| Propiedad | Descripción |
|-----------|-------------|
| `Flow` | Caudal (con signo o sin signo) |
| `Velocity` | Velocidad en m/s |
| `HeadLoss` | Pérdida de carga en m |
| `UnitHdLoss` | Pérdida unitaria en m/km |
| `FricFactor` | Factor de fricción |
| `Status` | Estado operacional (Open / Active / Closed) |
| `ReactRate` | Tasa de reacción (modelos de calidad) |
| `Quality` | Calidad del agua |

### Navegación temporal

El dock incluye una barra de tiempo con:

- **Slider** y **combo de instantes** (`cbTimes`): permiten saltar a cualquier período de la simulación.
- **Botones de avance/retroceso**: siguiente instante, instante anterior, ir al inicio, ir al final.

### Modos de tiempo

El selector `cbResultTimes` controla qué instantes se muestran:

| Modo | Comportamiento |
|------|----------------|
| **Single Period** | Un único instante de tiempo fijo |
| **Step times** | Avanza paso a paso por los instantes del informe |
| **All calculation times** | Incluye todos los pasos de cálculo internos del solver |

### Modos de estadística

El selector `cbStatistics` aplica una estadística sobre todos los períodos de la simulación en lugar de mostrar un instante concreto:

| Estadística | Significado |
|-------------|-------------|
| (Ninguna) | Valor en el instante seleccionado |
| **Maximum** | Valor máximo de toda la simulación |
| **Minimum** | Valor mínimo de toda la simulación |
| **Range** | Diferencia entre máximo y mínimo |
| **Average** | Valor medio de toda la simulación |
| **StdDev** | Desviación estándar |
| **Warning** | Marca los elementos que superan umbrales de aviso |

### Escenarios

El dock soporta múltiples escenarios de resultado. Cada escenario se identifica por un nombre (por defecto `Base`) y se almacena como archivos `.out` / `.hyd` en la subcarpeta `Results/` del proyecto. El nombre del escenario activo aparece en el título del panel.

---

## Series temporales (Time series…)

**Barra Analysis → Time series…**

Activa una herramienta de selección interactiva que dibuja la evolución temporal de cualquier propiedad de resultado para uno o varios elementos de la red.

![Panel Time series con curvas de presión de varios nudos](../assets/images/analisis/time-series-dock.png)
*Panel Time series: evolución temporal de la presión en varios nudos seleccionados simultáneamente.*

### Proceso

1. Activa **Time series** (botón checkable). El panel Time series se abre en la zona inferior de la pantalla.
2. Haz clic sobre cualquier elemento del mapa (nudo, tubería, válvula, bomba, depósito, embalse).
3. El panel dibuja la curva temporal de la propiedad activa en el Results dock para ese elemento.
4. El elemento queda resaltado en azul en el mapa.

### Selección múltiple

- **Shift + clic** sobre otro elemento: añade su curva al gráfico sin borrar las anteriores. Cada curva recibe un color diferente de la paleta.
- **Shift + clic** sobre un elemento ya seleccionado: lo elimina del gráfico.
- **Clic sin Shift** con más de una curva activa: pide confirmación antes de limpiar la selección.

### Selección de propiedad

- Por defecto se representa la propiedad activa en el Results dock para el tipo de elemento pulsado.
- **Clic derecho** sobre un elemento: abre un menú contextual para elegir cualquier otra propiedad disponible para ese elemento sin cambiar la vista del Results dock.

### Configuración de curvas

Desde el panel Time series puedes ajustar para cada curva:

- Nombre en la leyenda.
- Color, estilo de línea (sólida, discontinua, punteada) y grosor.
- Marcadores: símbolo, tamaño, color, hueco.
- Mostrar valores en cada punto de la curva.
- Visibilidad (mostrar / ocultar sin borrar).

### Cierre

Al desactivar el botón **Time series** o cerrar el panel, el resaltado desaparece y el cursor vuelve al modo de navegación estándar.
