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

### Opciones de visualización

El dock de resultados incluye opciones adicionales para el aspecto de los elementos en el mapa:

| Opción | Descripción |
|--------|-------------|
| **Proportional to value** | Escala el tamaño de los nodos y el grosor de las tuberías linealmente con el valor representado. El slider de tamaño base controla el máximo. No aplica al campo Status. |
| **Black border on nodes** | Añade un contorno negro a los marcadores de nodos para mejorar su visibilidad sobre fondos complejos. |

### Etiquetas y tooltips en el mapa

Las etiquetas visibles sobre el mapa muestran el tipo traducido y el Id del elemento en la primera línea (ej. "Junction J-01"), y el valor con sus unidades en la segunda. Cuando se muestra una estadística temporal (Mín/Máx), también se indica el instante correspondiente.

El tooltip del mapa (al pasar el cursor sobre cualquier capa gestionada por QGISRed) muestra en negrita la variable seleccionada, el tipo y el Id del elemento, y el valor con su unidad según el CSV de unidades del proyecto. Los tooltips son visibles en **todas las capas activas**, independientemente de cuál esté seleccionada en la leyenda.

### Evolución temporal rápida

El dock de resultados incorpora dos checkboxes:

- **Show Node Evolution**: abre un mini-gráfico integrado con la curva temporal del nudo seleccionado en el mapa.
- **Show Link Evolution**: equivalente para tuberías, válvulas y bombas.

Son una alternativa rápida al dock completo de Series Temporales cuando solo se necesita ver la evolución de un único elemento.

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

### Propiedades adicionales para depósitos

Para el tipo de elemento **Tank** (depósito), están disponibles dos magnitudes adicionales:

| Magnitud | Descripción |
|----------|-------------|
| **Volume** | Volumen almacenado en m³ (o ft³ según las unidades del proyecto). |
| **TankSpill** | Caudal de desbordamiento. Solo es distinto de cero si el depósito tiene activada la opción de overflow en EPANET. |

### Configuración de curvas

Desde el panel Time series puedes ajustar para cada curva:

- Nombre en la leyenda.
- Color, estilo de línea (sólida, discontinua, punteada) y grosor.
- Marcadores: símbolo, tamaño, color, hueco.
- Mostrar valores en cada punto de la curva.
- Visibilidad (mostrar / ocultar sin borrar).

### Sincronización con la tabla de valores

Al mover el cursor sobre el gráfico, la fila correspondiente de la tabla de valores se resalta automáticamente en tiempo real.

### Copiar tabla al portapapeles

La función de copiar genera **dos filas de cabecera**: la primera con el nombre del elemento o magnitud y la segunda con la unidad. Facilita el pegado directo en hojas de cálculo.

### Exportar e importar configuración del gráfico

Los botones **Export chart configuration** e **Import chart configuration** guardan y recuperan la configuración completa de curvas, ejes y estilos en un archivo `.cfg`. También es posible exportar la configuración de la plantilla general (ejes, estilos) aunque no haya curvas cargadas, y aplicarla al importarla sobre un gráfico nuevo.

### Múltiples ventanas de gráfico

El botón **New chart window** abre una nueva ventana de Series Temporales independiente. Cada ventana tiene su propio contexto de curvas, propiedad y elementos seleccionados. Puedes mantener varias ventanas abiertas simultáneamente para comparar distintas variables o zonas de la red.

### Sincronización del formato horario

La columna "Hora del día" en la tabla de valores utiliza automáticamente el mismo formato (24 h o am/pm) que el panel de Resultados.

### Cierre

Al desactivar el botón **Time series** o cerrar el panel, el resaltado desaparece y el cursor vuelve al modo de navegación estándar.
