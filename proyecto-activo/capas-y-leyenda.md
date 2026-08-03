# Resumen y gestión de capas

***

## Gestor de capas

**Barra Project → Gestor de capas** (Layer manager)

Controla qué capas del proyecto están activas en QGIS, permite recrear elementos base que falten y gestiona las capas auxiliares del Demands Builder. El diálogo organiza su contenido en tres pestañas: **Basic elements**, **Digital Twin** y **Auxiliary layers**.

\*Gestor de capas: lista de todas las capas del proyecto con su estado de carga.\*

Encima de las pestañas siempre está visible el campo **CRS**, con el sistema de coordenadas del proyecto y un botón **...** para cambiarlo.

### Pestañas Basic elements y Digital Twin

* **Basic elements** reúne los 6 elementos base de EPANET (Pipes, Junctions, Tanks, Reservoirs, Valves, Pumps) más las capas complementarias Multiple Demands y Sources.
* **Digital Twin** reúne las capas propias del gemelo digital: Service Connections, Isolation Valves y Meters.

Para cada elemento, la fila muestra una de estas dos cosas según exista o no su fichero en disco:

* **Casilla marcada/desmarcada** → el shapefile ya existe; la casilla decide si la capa está cargada y visible en QGIS. Puedes marcar o desmarcar cualquiera sin afectar a los datos.
* **Botón "Create `<Elemento>` Layer"** → el shapefile todavía no existe; el botón lo crea vacío (con la estructura de campos correcta) y lo abre automáticamente. Una vez creado, la fila pasa a mostrar la casilla.

> ⚠️ Pipes es la excepción: en cuanto está cargada, su casilla queda bloqueada. Es la capa que sostiene el resto de la red, así que no se puede descargar desde aquí sin descargar antes el resto del proyecto.

> 💡 Al pulsar **Accept**, el diálogo solo actúa sobre lo que ha cambiado: un elemento que ya estaba marcado y sigue marcado no se cierra y reabre, así que conserva su estilo, su visibilidad y la selección que tuvieras hecha en el lienzo. Cambiar el CRS es la excepción — como reescribe todos los shapefiles, cierra y reabre todo lo gestionado por el diálogo.

### Recuperar una capa borrada

Si has borrado accidentalmente una capa de la leyenda de QGIS (o su archivo SHP en disco), el Gestor de capas permite **recrearla vacía**: al abrir el diálogo, esa capa ya no muestra la casilla marcada, sino el botón **Create `<Elemento>` Layer** descrito arriba. Púlsalo y QGISRed crea el SHP vacío con la estructura de campos correcta y lo carga en QGIS.

> ⚠️ La recreación crea la capa vacía. Los datos que estuvieran en ella (si el SHP fue borrado del disco) no se pueden recuperar a menos que tengas una copia de seguridad.

### Aviso de capa desactualizada

Además del icono de aviso por capa borrada, la leyenda de QGIS puede mostrar un segundo tipo de icono de advertencia (⚠) sobre capas que **sí existen** pero cuyo contenido puede haber quedado obsoleto.

QGISRed vigila en segundo plano (comprobación cada 5 segundos) las capas derivadas que cuelgan de las carpetas del proyecto **Issues**, **Queries** y **Results**, cuyo nombre de fichero empieza por `<Red>_`. Si el fichero de entrada más reciente de la red (Pipes, Junctions, etc.) se ha modificado después de que se generase alguna de esas capas derivadas, esa capa recibe el icono de aviso con el mensaje:

> "Layer may be outdated — inputs have changed since last generation"

* El icono es solo informativo: no tiene ninguna acción asociada al hacer clic sobre él.
* Para resolver el aviso hay que **regenerar la capa**, es decir, volver a lanzar el análisis o la consulta que la creó (Isolated Segments, Hydraulic Sectors, una consulta por propiedades, etc.).
* Las capas auxiliares del Demands Builder (Consumption Points, Demand Links, Sectors) quedan explícitamente excluidas de esta vigilancia: son datos propios que tú importas o creas, no algo que QGISRed recalcule a partir de la red, así que editar un input no las invalida.

> 💡 Este aviso es distinto del icono que aparece cuando una capa ha sido borrada (ver "Recuperar una capa borrada" arriba): aquí la capa sigue existiendo y cargada, simplemente puede que su contenido ya no refleje el estado actual de la red.

### Pestaña Auxiliary layers: capas del Demands Builder

La pestaña **Auxiliary layers** contiene el grupo **Demand Builder**, desde donde se crean y gestionan las capas vacías de trabajo que usa la herramienta de asignación de demandas a nudos (Nodal Demand Builder): **Consumption Points**, **Demand Links** y **Sectors**.

Cada fila de la tabla es un **tema** (theme) — puedes tener varios temas del mismo tipo, por ejemplo un `Sectors` distinto por cada campaña de sectorización de demanda. La tabla muestra tres columnas:

* Casilla de carga (igual que en las otras pestañas: marcada = cargada en QGIS).
* **Theme** — nombre del tema, o "(default)" para el que crea automáticamente el propio Demands Manager.
* **Type** — Consumption Points / Demand Links / Sectors.

Para crear un tema nuevo:

1. Pulsa **Create Auxiliary Theme**.
2. En el diálogo **New auxiliary theme**, elige el **Type** (Consumption Points, Demand Links o Sectors) y escribe un **Name**.
3. Pulsa **Accept**. QGISRed crea el shapefile vacío con los campos correspondientes y lo añade ya marcado y cargado a la tabla.

Para borrar un tema, selecciona su fila y pulsa **Delete Auxiliary Theme**; se te pedirá confirmación porque la operación borra también los ficheros del disco.

> 💡 Las capas que dejas marcadas en esta tabla se recuerdan al cerrar y reabrir el proyecto — incluidos los proyectos que no guardan un `.qgz` — igual que el resto de capas del proyecto.

> Para saber cómo se usan estas capas dentro del Nodal Demand Builder (importar puntos de consumo, generar enlaces de demanda, agregar por sectores...), consulta [Demandas y escenarios](../herramientas/demandas-escenarios.md).

### Resumen del modelo (Summary)

**Barra Project → Resumen**

Genera un informe rápido con el número de elementos de cada tipo presentes en el proyecto:

```
Junctions: 1 243
Pipes: 1 876
Tanks: 3
Reservoirs: 2
Valves: 47
Pumps: 8
```

Útil para verificar que la importación fue completa o para documentar el tamaño del modelo.

***

## Editor de leyenda

**Barra Project → Editor de leyenda** (Legend editor)

Abre un panel flotante que permite construir y personalizar la **simbología** de las capas del proyecto sin navegar por el menú de propiedades de capa de QGIS: tipo de leyenda, clasificación automática, tamaños, colores, guardado/carga de estilos y reglas propias por tipo de elemento.

\*Panel del Editor de leyenda: estilos predefinidos y personalización de colores y tamaños.\*

### Elegir la capa

En la cabecera del diálogo:

* **Group** — grupo del árbol de capas sobre el que quieres trabajar (Inputs, Results, Queries y sus subgrupos...).
* **Map Layer** — capa concreta dentro de ese grupo. También puedes cambiar de capa seleccionándola directamente en el panel de capas de QGIS; el editor sigue la selección automáticamente.

### Tipo de leyenda y clasificación

El desplegable **Legend Type** ofrece, según el tipo de capa, entre **Single Symbol**, **Categorized** y **Graduated**. Solo aparecen las opciones que tienen sentido para esa capa (por ejemplo, una capa de resultados numéricos no ofrece Single Symbol).

> 💡 Para la capa **Meters** aparece además el desplegable **Meter Type**, que filtra la tabla y las reglas de color/tamaño a "All types" o a un tipo concreto de contador (los distintos iconos apilados en el símbolo de Meters).

La tabla central lista una fila por clase, con casilla de visibilidad, color, tamaño, valor/rango (o categoría) y etiqueta de leyenda:

* **Classes** (spinbox) fija el número de clases; el botón junto a él, **Classify All**, añade una clase por cada valor único de la capa (categórica) o reclasifica automáticamente el rango numérico según el modo elegido en **Intervals**.
* Los botones **+ / -** junto a Classes añaden o quitan clases: clic izquierdo añade una clase debajo de la selección, clic derecho la añade encima; en leyendas categóricas, doble clic añade una clase especial "Other values" que agrupa el resto de valores no clasificados.
* **Intervals** (`cbMode`) fija el método de clasificación automática para leyendas graduadas: Manual, Equal Interval, Fixed Interval, Quantile (Equal Count), Natural Breaks (Jenks), Standard Deviation y Pretty Breaks. Con **Fixed Interval** aparece el campo **Interval Range** para indicar el ancho de cada clase.
* Puedes editar el rango de una clase a mano haciendo **doble clic sobre su valor** (columna Value) para abrir un pequeño diálogo con los límites inferior y superior.
* **Up / Down** (flechas junto a la tabla) reordenan la clase seleccionada.

### Tamaños

El bloque **Sizes** controla el tamaño (grosor de línea o tamaño de símbolo puntual) de las clases:

* **Sizes** (`cbSizes`): Manual, Equal, Linear, Quadratic, Exponential o Proportional to Value.
* **Equal** usa un único campo **Value** para todas las clases.
* Linear/Quadratic/Exponential/Proportional to Value reparten el tamaño entre **Min** y **Max** según la curva elegida, con la casilla **Invert** para intercambiar qué extremo (menor o mayor valor) recibe el tamaño mínimo.

### Colores

El bloque **Colors** controla el color de cada clase:

* **Colors** (`cbColors`): Manual, Equal, Random, Ramp o Palette.
* **Equal** aplica un único color (botón de color junto al desplegable) a todas las clases.
* **Random** genera colores aleatorios distintos por clase, con el mismo criterio de "colores aleatorios barajados" (shuffle) que usa QGIS de forma nativa. El botón de refrescar junto al desplegable (visible solo en este modo) vuelve a barajar los colores sin cambiar nada más.
* **Ramp** muestra, a todo lo ancho del diálogo, el selector nativo de rampa de color de QGIS para elegir la rampa a aplicar sobre las clases; incluye tanto el catálogo estándar de QGIS como rampas propias de QGISRed.
* **Palette** reparte los colores tomando una paleta categórica en vez de una rampa continua.
* La casilla **Invert** intercambia el sentido de la rampa/paleta.

> 💡 Para la capa de nodos del árbol de conectividad (Tree), el color de la fila no tiñe el símbolo entero: edita solo el **color de trazo (stroke)** del círculo exterior del nodo, dejando la estrella y los iconos de elemento con su color propio.

### Reglas de estilo específicas por tipo de capa

Los elementos de entrada (Inputs) y algunas capas de consulta llevan reglas de estilo con estados fijos que el color/tamaño que elijas respeta, en lugar de sobrescribir el símbolo entero. Por ejemplo, Pipes/Valves/Pumps mantienen en rojo el estado "cerrada" y las Valves activas en naranja pase lo que pase con el color que elijas para el resto. Entre las capas con reglas propias:

* **Multiple Demands**: el color elegido solo tiñe la rama de "demanda positiva" del símbolo (el marcador interior), igual que en Junctions; la demanda negativa y el resto del símbolo mantienen sus colores fijos.
* **Isolation Valves**: el color elegido solo sustituye al estado "abierta, sin pérdida de carga"; los colores de cerrada (rojo), con pérdida de carga (ámbar) y no disponible (gris) están fijados por la propia leyenda y no se pueden editar desde aquí.
* **Meters**: el color y el tamaño se aplican según lo que tengas seleccionado en **Meter Type** — a todos los tipos de contador a la vez, o solo al tipo elegido, sin tocar el resto de iconos apilados.
* **Service Connections**: el color elegido se aplica al trazo de la acometida activa y a una versión más clara del mismo color para su relleno; el resto de estados conserva su color propio.
* **Connect\_Links** (resultado de la herramienta de Conectividad, dentro de Queries): a diferencia de las anteriores, no tiene reglas por estado — el color y el tamaño se aplican directamente sobre el símbolo, como en cualquier capa Single Symbol.

### Cargar y guardar estilos

Los botones **Load** y **Save**, en la parte inferior del diálogo, abren cada uno un menú:

**Load**

* **Default Style** — recupera el estilo por defecto de QGISRed para ese tipo de capa.
* **Global Style** — carga un estilo que hayas guardado previamente a nivel global (válido para cualquier proyecto).
* **Project Style** — carga un estilo guardado dentro de este proyecto.
* **Revert to Original Legend** — recupera en el diálogo la leyenda que tenía la capa en el momento de abrir el editor (sin necesidad de cerrar y reabrir el diálogo).

**Save**

* **To Global...** — guarda la leyenda actual como estilo global, reutilizable en cualquier proyecto.
* **To Project...** — guarda la leyenda actual dentro de la carpeta `layerStyles` de este proyecto.

Al guardar, un pequeño diálogo te deja elegir si quieres guardar la leyenda **tal cual se ve** o una **estrategia** que se regenere automáticamente la próxima vez que la cargues (marcando qué partes conservar: la estructura de clases/intervalos, los tamaños y/o los colores).

> ⚠️ Tanto **Load** como **Revert to Original Legend** solo actualizan la vista previa del diálogo. La capa del proyecto no cambia hasta que pulses **Apply** o **Accept**.

### Aplicar, Aceptar y Cancelar

Los tres botones inferiores tienen una semántica de vista previa muy concreta:

* **Apply** — aplica los cambios mostrados en el diálogo a la capa, sin cerrar el editor. Útil para ir viendo el resultado en el lienzo mientras sigues ajustando.
* **Accept** — aplica los cambios a la capa y cierra el diálogo (equivale a Apply + cerrar).
* **Cancel** — cierra el diálogo y **restaura la capa a la leyenda que tenía cuando la seleccionaste** en este editor, deshaciendo también los cambios que ya hubieras aplicado con Apply. Si había cambios aplicados, QGISRed pide confirmación antes de descartarlos.

> 💡 Como Cancel siempre vuelve al estado de partida (aunque hayas pulsado Apply varias veces mientras probabas cosas), es la forma segura de "empezar de nuevo" con una capa sin tener que reconstruir su leyenda a mano.
