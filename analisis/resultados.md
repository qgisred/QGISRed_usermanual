# Visor de Resultados

Una vez completada la simulación, QGISRed ofrece dos herramientas complementarias para explorar los resultados: el **panel de resultados** (Results dock), que controla la visualización sobre el mapa, y el **panel de series temporales** (Time series dock), que muestra la evolución de cualquier variable a lo largo del tiempo para elementos individuales.

---

## Panel de resultados (Results dock)

El Results dock se ancla en la zona derecha de la pantalla. Contiene **tres pestañas**:

- **Results**: visualización interactiva sobre el mapa con selección de variable, navegación temporal y opciones de mapa.
- **Report**: informe de texto del motor EPANET.
- **Appearance**: configuración completa del aspecto visual de los resultados en el mapa.

<figure><img src="../assets/images/analisis/results-dock.png" alt="Panel de resultados con selector de variable y barra de tiempo"><figcaption><p>Panel de resultados con selector de variable y barra de tiempo</p></figcaption></figure>
*Results dock: selección de variable, modo de estadística y navegación por instantes de tiempo.*
<!-- TODO: captura desactualizada tras añadir el botón Constant playback rate junto al slider de velocidad -->

---

### Pestaña Results

#### Grupo Timing

Muestra el instante de tiempo actual en formato `HH:MM:SS` (o en formato am/pm si está activo). Incluye botones para alternar entre formato civil y formato de tiempo transcurrido.

Cuando está activo un modo de estadística (Maximum, Minimum…), el área de tiempo muestra el nombre y la descripción de la estadística en lugar del reloj.

#### Navegación temporal (Time controls)

| Control | Descripción |
|---------|-------------|
| **Slider de tiempo** | Desliza por los instantes del informe. |
| **Combo de instantes** (`cbTimes`) | Lista desplegable con todos los instantes disponibles. |
| **Botones de avance/retroceso** | Siguiente, anterior, inicio, fin. |
| **Play / Play backward** | Animación automática hacia adelante o atrás. |
| **Slider de velocidad** | Controla la velocidad relativa de la animación (1–10). Se oculta cuando **Constant playback rate** está activo. |
| **Constant playback rate** | Botón conmutable junto al slider de velocidad. Al activarlo, el slider se sustituye por el campo **"1h in: N sec"**: N son los segundos reales que tarda en reproducirse una hora de tiempo simulado (1–3600), de modo que la velocidad de reproducción es constante respecto al tiempo simulado incluso si el paso entre instantes no es uniforme. Al desactivarlo, vuelve a usarse el slider de velocidad relativa. El estado y el valor se guardan en el proyecto. |
| **Loop** | Repite la animación en bucle. |

> 💡 Al cambiar de instante de tiempo, activar o desactivar un modo de estadística, modificar los decimales en la pestaña Appearance, o cargar todos los resultados de golpe, QGISRed relee y reformatea los valores. Si la operación tarda (redes grandes con muchos elementos), aparece un aviso superpuesto y centrado sobre el mapa: **"Reading results… NN%"**. En operaciones rápidas no llega a mostrarse, para evitar parpadeos.

#### Reported Times y Statistics

Dos combos situados bajo los controles de tiempo:

| Combo | Descripción |
|-------|-------------|
| **Reported Times** (`cbResultTimes`) | Filtra qué instantes se muestran: Single Period, Step times o All calculation times. |
| **Statistics** (`cbStatistics`) | Aplica una estadística sobre todos los períodos: Maximum, Minimum, Range, Average, StdDev, Warning. Cuando está activo, el reloj se sustituye por el nombre de la estadística. |

> 💡 En los modos **Maximum** y **Minimum**, las etiquetas del mapa muestran el valor junto con el instante de ocurrencia en el formato `valor (@ HH:MM:SS)`. Al situar el cursor sobre un elemento del mapa, el tooltip incluye una línea adicional `@ HH:MM:SS` con el instante exacto en que se produjo ese máximo o mínimo.

> 💡 Con cualquier modo de estadística activo, el tooltip antepone al valor la abreviatura de la estadística mostrada: **Max**, **Min**, **Avg** (Average), **Rng** (Range) o **Std** (StdDev). Por ejemplo, `Max 45.2` en lugar de simplemente `45.2`.

#### Grupo Mapping — Nodes

| Control | Descripción |
|---------|-------------|
| **Combo Nodes** (`cbNodes`) | Propiedad a visualizar en nudos: Pressure, Head, Demand, Quality. |
| **Show Node Labels** | Muestra etiquetas con el Id y el valor sobre cada nudo en el mapa. |
| **Show Node Histogram** | Abre un histograma integrado en el dock con la distribución del valor actual en nudos. |
| **Show Node Evolution** | Abre un mini-gráfico integrado con la evolución temporal del nudo seleccionado en el mapa. |

> 💡 Cuando se selecciona una variable en el combo **Nodes**, aparece junto al encabezado del grupo una etiqueta con el nombre de la variable en negrita y su unidad entre paréntesis (por ejemplo, **Presión** (m)).

#### Grupo Mapping — Links

| Control | Descripción |
|---------|-------------|
| **Combo Links** (`cbLinks`) | Propiedad a visualizar en tuberías/válvulas/bombas: Flow, Velocity, HeadLoss, UnitHdLoss, FricFactor, Status, ReactRate, Quality. |
| **Show Link Labels** | Muestra etiquetas con el Id y el valor sobre cada tubería. |
| **Show Flow Directions** | Añade flechas de sentido de flujo sobre las tuberías. |
| **Show Link Histogram** | Histograma integrado en el dock con la distribución del valor actual en tuberías. |
| **Show Link Evolution** | Mini-gráfico integrado con la evolución temporal de la tubería seleccionada en el mapa. |

> 💡 Del mismo modo, cuando se selecciona una variable en el combo **Links**, aparece junto al encabezado del grupo una etiqueta con el nombre de la variable en negrita y su unidad entre paréntesis (por ejemplo, **Velocidad** (m/s)).

> ⚠️ Cuando la variable de **Links** es **Status**, las etiquetas de texto se simplifican: los ~13 estados internos que puede devolver EPANET se agrupan en solo dos textos, **"Closed"** (incluye "Temp Closed") y **"Active"** (incluye "Active (Rev Pump)"). Los enlaces con cualquier estado **"Open*"** no muestran ninguna etiqueta, para no saturar el mapa con la mayoría de las tuberías (que suelen estar abiertas). No es un error si, con Status activo, la mayor parte de las tuberías aparecen sin etiqueta.

> El botón **Appearance** (icono en la cabecera del grupo Nodes) lleva directamente a la pestaña Appearance sin necesidad de navegar por las pestañas.

---

### Pestaña Report

Muestra el informe de texto generado por el motor EPANET al finalizar la simulación. Incluye:

- Balance de masa general de la red.
- Lista de nudos con presión negativa o fuera de rango.
- Advertencias de bombas operando fuera de su curva.
- Estado de convergencia del cálculo hidráulico en cada paso.
- Resumen de reacciones de calidad (si se simuló calidad).
- En caso de error, el contenido completo del informe se muestra automáticamente aquí.

> El informe de estado es el primer lugar donde mirar cuando una simulación produce resultados inesperados o no converge.

---

### Pestaña Appearance

Concentra todas las opciones de presentación visual de los resultados en el mapa. Los ajustes se guardan automáticamente en `{Red}_Results_Config.cfg` dentro de la carpeta `Results/` del proyecto y se restauran en la siguiente sesión.

> 💡 Cada control numérico de la pestaña Appearance dispone de un pequeño botón ↺ individual que restaura únicamente ese campo a su valor por defecto, sin afectar al resto de ajustes.

> ⚠️ Los controles del grupo **Nodes** se deshabilitan automáticamente cuando el combo Nodes está en «None», y lo mismo ocurre para **Links**. Además, el control **Decimals** queda deshabilitado cuando la variable activa es **Status** (variable categórica sin decimales aplicables).

#### Map Labels

| Opción | Descripción |
|--------|-------------|
| **Font size (pt)** | Tamaño de la fuente de las etiquetas en el mapa (6–24 pt, por defecto 8). |
| **Nodes / Links decimals** | Número de decimales mostrados en las etiquetas de nudos y tuberías respectivamente (0–6). El control se etiqueta con el nombre de la variable activa en ese momento. |
| **Text color** | Color por defecto: nudos **#333333** (gris oscuro), tuberías **#0A143C** (azul marino). **Black**: texto negro siempre. **By range**: el color del texto sigue la paleta del rango de valores activo. Cuando **Show Node ID** o **Show Link ID** está activo, la línea del Id usa el color del propio elemento y la línea del valor usa el color del símbolo o rango. |
| **Background** | Color de fondo detrás de las etiquetas del mapa. Incluye un selector de color y un botón de borrado para eliminar el fondo. Junto al selector hay un icono de **candado**: abierto (por defecto), el fondo de las etiquetas es independiente del fondo del mapa; al cerrarlo, el selector y el botón de borrado se deshabilitan y el fondo de las etiquetas queda vinculado al color de **Map Background** (ver más abajo), de modo que cambiar ese color también cambia automáticamente el fondo de las etiquetas. |
| **Buffer** | Color de contorno (halo) alrededor del texto de las etiquetas, con su propio selector de color y botón de borrado. Es independiente del Background y nunca se vincula al Map Background. Sin color asignado (por defecto) no se dibuja ningún halo. |
| **Show Node ID** / **Show Link ID** | Dos casillas independientes: añaden el Id del nudo o de la tubería, respectivamente, en la primera línea de su etiqueta. |

#### Symbology

| Opción | Descripción |
|--------|-------------|
| **Hide border on junctions** | Oculta el borde/contorno de los marcadores de nudos (junctions). Activar esta opción elimina el contorno que rodea el símbolo del nudo. |
| **Proportional to value** | Escala el tamaño de los nudos y el grosor de las tuberías linealmente con el valor representado. No aplica al campo Status. |
| **Nodes factor** | Factor de escala base del tamaño de los marcadores de nudo (0.25–4.0, por defecto 1.0). |
| **Links factor** | Factor de escala base del grosor de las tuberías (0.25–4.0, por defecto 1.0). |
| **Arrows factor** | Factor de escala de las flechas de dirección de flujo (0.25–4.0, por defecto 1.0). |

#### Map Background

Permite fijar un color de fondo sólido para el lienzo del mapa mientras se visualizan resultados. El color se restaura al original al cerrarse el dock. El botón **×** elimina el color de fondo.

#### Reset all

Devuelve todos los parámetros de la pestaña Appearance a sus valores por defecto.

---

### Escenarios

El dock soporta múltiples escenarios de resultado. Cada escenario se identifica por un nombre (por defecto `Base`) y se almacena como archivos `.out` / `.hyd` en la subcarpeta `Results/` del proyecto. El nombre del escenario activo aparece en el título del panel.

---

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

> 💡 Las etiquetas del mapa para la variable **Flow** muestran siempre el valor absoluto (sin signo negativo), incluso en los modos de estadística Máximo y Mínimo. El sentido del flujo se indica mediante las flechas de dirección, no mediante el signo del valor.

---

## Series temporales (Time series…)

**Barra Analysis → Time series…**

Activa una herramienta de selección interactiva que dibuja la evolución temporal de cualquier propiedad de resultado para uno o varios elementos de la red.

<figure><img src="../assets/images/analisis/time-series-dock.png" alt="Panel Time series con curvas de presión de varios nudos"><figcaption><p>Panel Time series con curvas de presión de varios nudos</p></figcaption></figure>
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
| **Volume** | Volumen almacenado en m³ (o ft³ según las unidades del proyecto), calculado a partir de los binarios de resultado EPANET. |
| **TankSpill** | Caudal de desbordamiento. Solo es distinto de cero si el depósito tiene activada la opción de overflow en EPANET. |

### Variables globales de red

Además de los elementos individuales, el panel Time series permite añadir **series globales** que agregan valores sobre toda la red. Estas series no requieren hacer clic en el mapa: se añaden desde el menú de selección de variable del gráfico.

| Variable global | Descripción |
|-----------------|-------------|
| **TotalWaterSupply** | Caudal total suministrado por todos los embalses y fuentes de la red. |
| **TotalWaterDemand** | Demanda total consumida por todos los nudos de la red. |
| **AverageNodePressure** | Presión media de todos los nudos (excluye depósitos y embalses). |
| **TotalStoredVolume** | Volumen total almacenado sumando todos los depósitos de la red. |
| **TotalTankSpill** | Caudal total de desbordamiento sumando todos los depósitos de la red. |

### Configuración de curvas

Desde el panel Time series puedes ajustar para cada curva:

- Nombre en la leyenda.
- Color, estilo de línea (sólida, discontinua, punteada) y grosor.
- Marcadores: símbolo, tamaño, color, hueco.
- Mostrar valores en cada punto de la curva.
- Visibilidad (mostrar / ocultar sin borrar).

### Tabla de valores

La tabla de valores muestra los datos numéricos de todas las curvas activas. La **primera columna** (instante de tiempo) está **fija**: no desaparece al desplazar la tabla horizontalmente cuando hay muchas curvas. Esto facilita identificar en qué instante se encuentra cada fila sin necesidad de volver al principio.

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
