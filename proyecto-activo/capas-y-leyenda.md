# Gestor de Capas y Leyenda

---

## Gestor de capas

**Barra Proyecto → Gestor de capas** (Layer manager)

Controla qué capas del proyecto están activas en QGIS, permite recrear elementos base que falten y gestiona las capas auxiliares del Constructor de demandas nodales. El diálogo organiza su contenido en tres pestañas: **Elementos básicos**, **Gemelo Digital** y **Capas auxiliares**.

<figure><img src="../assets/images/project/layer-manager.png" alt="Diálogo del Gestor de capas de QGISRed"><figcaption><p>Diálogo del Gestor de capas de QGISRed</p></figcaption></figure>
<!-- TODO: captura desactualizada, el diálogo pasó de secciones apiladas a pestañas (ver commits 12d9ee7 y 11c29ed) -->
*Gestor de capas: lista de todas las capas del proyecto con su estado de carga.*

Encima de las pestañas siempre está visible el campo **CRS**, con el sistema de coordenadas del proyecto y un botón **...** para cambiarlo.

### Pestañas Elementos básicos y Gemelo Digital

- **Elementos básicos** reúne los 6 elementos base de EPANET (Pipes, Junctions, Tanks, Reservoirs, Valves, Pumps) más las capas complementarias Multiple Demands y Sources.
- **Gemelo Digital** reúne las capas propias del gemelo digital: Service Connections, Isolation Valves y Meters.

Para cada elemento, la fila muestra una de estas dos cosas según exista o no su fichero en disco:

- **Casilla marcada/desmarcada** → el shapefile ya existe; la casilla decide si la capa está cargada y visible en QGIS. Puedes marcar o desmarcar cualquiera sin afectar a los datos.
- **Botón "Create `<Elemento>` Layer"** → el shapefile todavía no existe; el botón lo crea vacío (con la estructura de campos correcta) y lo abre automáticamente. Una vez creado, la fila pasa a mostrar la casilla.

> ⚠️ Pipes es la excepción: en cuanto está cargada, su casilla queda bloqueada. Es la capa que sostiene el resto de la red, así que no se puede descargar desde aquí sin descargar antes el resto del proyecto.

> 💡 Al pulsar **Aceptar**, el diálogo solo actúa sobre lo que ha cambiado: un elemento que ya estaba marcado y sigue marcado no se cierra y reabre, así que conserva su estilo, su visibilidad y la selección que tuvieras hecha en el lienzo. Cambiar el CRS es la excepción — como reescribe todos los shapefiles, cierra y reabre todo lo gestionado por el diálogo.

### Recuperar una capa borrada

Si has borrado accidentalmente una capa de la leyenda de QGIS (o su archivo SHP en disco), el Gestor de capas permite **recrearla vacía**: al abrir el diálogo, esa capa ya no muestra la casilla marcada, sino el botón **Create `<Elemento>` Layer** descrito arriba. Púlsalo y QGISRed crea el SHP vacío con la estructura de campos correcta y lo carga en QGIS.

> ⚠️ La recreación crea la capa vacía. Los datos que estuvieran en ella (si el SHP fue borrado del disco) no se pueden recuperar a menos que tengas una copia de seguridad.

### Aviso de capa desactualizada

Además del icono de aviso por capa borrada, la leyenda de QGIS puede mostrar un segundo tipo de icono de advertencia (⚠) sobre capas que **sí existen** pero cuyo contenido puede haber quedado obsoleto.

QGISRed vigila en segundo plano (comprobación cada 5 segundos) las capas derivadas que cuelgan de las carpetas del proyecto **Incidencias**, **Consultas** y **Resultados**, cuyo nombre de fichero empieza por `<Red>_`. Si el fichero de entrada más reciente de la red (Pipes, Junctions, etc.) se ha modificado después de que se generase alguna de esas capas derivadas, esa capa recibe el icono de aviso con el mensaje:

> "La capa puede estar obsoleta - los datos de entrada han cambiado desde que se generó"

- El icono es solo informativo: no tiene ninguna acción asociada al hacer clic sobre él.
- Para resolver el aviso hay que **regenerar la capa**, es decir, volver a lanzar el análisis o la consulta que la creó (Isolated Segments, Hydraulic Sectors, una consulta por propiedades, etc.).
- Las capas auxiliares del Constructor de demandas nodales (Consumption Points, Demand Links, Demand Sectors) quedan explícitamente excluidas de esta vigilancia: son datos propios que tú importas o creas, no algo que QGISRed recalcule a partir de la red, así que editar un input no las invalida.

> 💡 Este aviso es distinto del icono que aparece cuando una capa ha sido borrada (ver "Recuperar una capa borrada" arriba): aquí la capa sigue existiendo y cargada, simplemente puede que su contenido ya no refleje el estado actual de la red.

### Pestaña Capas auxiliares: capas del Constructor de demandas nodales

La pestaña **Capas auxiliares** contiene el grupo **Constructor Demandas**, desde donde se crean y gestionan las capas vacías de trabajo que usa la herramienta de asignación de demandas a nudos (Constructor de demandas nodales): **Consumos puntuales**, **Enlaces de demanda** y **Sectores de Demanda**.

<figure><img src="../assets/images/project/auxiliary-layers.png" alt="Pestaña Capas auxiliares del Gestor de capas de QGISRed"><figcaption><p>Pestaña Capas auxiliares del Gestor de capas de QGISRed</p></figcaption></figure>

Cada fila de la tabla es un **tema** (theme) — puedes tener varios temas del mismo tipo, por ejemplo un `Sectors` distinto por cada campaña de sectorización de demanda. La tabla muestra tres columnas:

- Casilla de carga (igual que en las otras pestañas: marcada = cargada en QGIS).
- **Tema** — nombre del tema, o "(por defecto)" para el que crea automáticamente el propio Constructor de demandas nodales.
- **Tipo** — Consumption Points / Demand Links / Demand Sectors.

Para crear un tema nuevo:

1. Pulsa **Crear tema auxiliar**.
2. En el diálogo **Nuevo tema auxiliar**, elige el **Tipo** (Consumption Points, Demand Links o Demand Sectors) y escribe un **Nombre**.
3. Pulsa **Aceptar**. QGISRed crea el shapefile vacío con los campos correspondientes y lo añade ya marcado y cargado a la tabla.

Para borrar un tema, selecciona su fila y pulsa **Eliminar tema auxiliar**; se te pedirá confirmación porque la operación borra también los ficheros del disco.

Cuando seleccionas un tema de tipo **Consumos puntuales**, aparece además un botón **…** (tooltip "Campos de demanda base") que abre el diálogo **Campos de demanda base**, donde se gestionan las columnas de demanda base del tema (todos los campos posteriores a `DemID` y `Category`):

- La lista muestra un campo por fila, con el nombre editable directamente (doble clic o tecla).
- **+** añade una fila nueva con un nombre libre sugerido (`BaseDem`, `BaseDem2`…); **-** borra la fila seleccionada. El tema siempre necesita al menos un campo de demanda base.
- Al pulsar **Aceptar**, QGISRed valida los nombres: no pueden quedar vacíos, no pueden superar 10 caracteres (límite del formato DBF), deben empezar por una letra y solo contener letras, números y guion bajo, y no puede haber dos campos con el mismo nombre (sin distinguir mayúsculas/minúsculas). Si algo no es válido, el diálogo no se cierra y muestra el motivo.
- Si algún campo existente se ha eliminado de la lista, antes de aplicar los cambios se pide confirmación explícita porque se borran también sus valores; renombrar un campo, en cambio, conserva los datos.

> 💡 Las capas que dejas marcadas en esta tabla se recuerdan al cerrar y reabrir el proyecto — incluidos los proyectos que no guardan un `.qgz` — igual que el resto de capas del proyecto.

> Para saber cómo se usan estas capas dentro del Constructor de demandas nodales (importar puntos de consumo, generar enlaces de demanda, agregar por sectores...), consulta [Demandas y escenarios](../herramientas/demandas-escenarios.md).

### Resumen del modelo (Summary)

**Barra Proyecto → Resumen**

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

---

## Editor de leyenda

**Barra Proyecto → Editor de leyenda** (Legend editor)

Abre un panel flotante que permite construir y personalizar la **simbología** de las capas del proyecto sin navegar por el menú de propiedades de capa de QGIS: tipo de leyenda, clasificación automática, tamaños, colores, opacidad y borde en capas de polígono, biblioteca de rampas/paletas propia, guardado/carga de estilos y reglas propias por tipo de elemento.

<figure><img src="../assets/images/project/legend-editor.png" alt="Panel del Editor de leyenda de QGISRed"><figcaption><p>Panel del Editor de leyenda de QGISRed</p></figcaption></figure>
<!-- TODO: captura desactualizada, el diálogo se rediseñó por completo y ha seguido cambiando desde entonces (bloque de commits [Legends]/[Styles], sep-oct 2026) -->
*Panel del Editor de leyenda: estilos predefinidos y personalización de colores y tamaños.*

### Elegir la capa

En la cabecera del diálogo:

- **Grupo** — grupo del árbol de capas sobre el que quieres trabajar (Inputs, Results, Queries y sus subgrupos...).
- **Capa de Mapa** — capa concreta dentro de ese grupo. También puedes cambiar de capa seleccionándola directamente en el panel de capas de QGIS; el editor sigue la selección automáticamente.

### Selector de variante

Varias capas de entrada muestran un desplegable adicional que filtra la tabla y las reglas de color/tamaño/opacidad a un subconjunto de la capa en vez de a todos sus elementos a la vez:

| Capa | Desplegable | Opciones |
|---|---|---|
| Meters | **Tipo de medidor** | "Todos los tipos" o un tipo concreto de contador (los distintos iconos apilados en el símbolo) |
| Junctions | **Demanda** | "Todos", "Salidas (> 0)", "Entradas (< 0)" |
| Sources | **Tipo de fuente** | "Todos los tipos" o un tipo concreto de fuente |
| Service Connections | **Componente** | "Todos", "Línea", "Círculo de demanda" |
| Capas de enlace (Pipes y similares) | **Componente** | "Todos", "Línea", "Marcador" |
| Nodos del árbol de conectividad (Tree) | **Nudo** | "Todos", "Uniones", "Nudo raíz" |
| Capas con tipos de elemento propios | **Elemento** | "Todos" + un tipo por cada elemento posible de esa capa |

Mientras el selector esté en "Todos" (o no tenga variantes), el color/tamaño se aplica a todos los elementos a la vez salvo que la capa tenga reglas de estilo fijas (ver más abajo).

### Tipo de leyenda y clasificación

El desplegable **Tipo de leyenda** ofrece, según el tipo de capa, entre **Símbolo único**, **Categorizado** y **Graduado**. Solo aparecen las opciones que tienen sentido para esa capa (por ejemplo, una capa de resultados numéricos no ofrece Single Symbol); si la capa es de tipo Single Symbol sin clases, el panel avisa con el texto "Capa de símbolo único: sin clases de tamaño ni de color."

La tabla central lista una fila por clase, con casilla de visibilidad, color, tamaño, valor/rango (o categoría) y etiqueta de leyenda:

- **Clases** es editable solo cuando el modo de clasificación admite un número variable de clases (por ejemplo, no en modo Manual sobre una leyenda numérica ni en capas con leyenda fija); en el resto de casos aparece en gris, sin flechas, y no se puede teclear. El botón junto a él, **Añadir todos los valores** (antes "Classify All"), añade una clase por cada valor único de la capa (categórica) o reclasifica automáticamente el rango numérico según el modo elegido en **Intervalos**.
- El botón **+** junto a Classes añade una clase debajo de la selección con un solo clic; la flecha a su lado abre un menú con "Añadir clase encima de la selección" y, en leyendas categóricas, 'Add "Other values" class' (una clase especial que agrupa el resto de valores no clasificados). El botón **-** quita la clase seleccionada.
- **Intervalos** (`cbMode`) fija el método de clasificación automática para leyendas graduadas: Manual, Equal Interval, Fixed Interval, Quantile (Equal Count), Natural Breaks (Jenks), Standard Deviation y Pretty Breaks. Con **Intervalo Fijo** aparece el campo **Rango de Intervalos** para indicar el ancho de cada clase.
- Puedes editar el rango de una clase a mano haciendo **doble clic sobre su valor** (columna Value) para abrir un pequeño diálogo con los límites inferior y superior.
- **Up / Down** (flechas junto a la tabla) reordenan la clase seleccionada a mano. El desplegable **Orden de las clases** (None / Ascending / Descending), por encima de la tabla, reordena todas las clases por su valor automáticamente en el momento de aplicar la leyenda.

### Tamaños

El bloque **Tamaños** controla el tamaño de las clases, siempre en milímetros salvo la excepción de abajo:

- **Tamaños** (`cbSizes`): Manual, Equal, Linear, Quadratic, Exponential o Proportional to Value.
- **Igual** usa un único campo **Valor** para todas las clases.
- Linear/Quadratic/Exponential/Proportional to Value reparten el tamaño entre **Mínimo** y **Máximo** según la curva elegida, con la casilla **Invertir** para intercambiar qué extremo (menor o mayor valor) recibe el tamaño mínimo.

> 💡 En capas con leyenda de estado fija (ver "Reglas de estilo específicas" más abajo) o en una capa Single Symbol con el selector de variante en "Todos", la columna cambia de cabecera a **Tamaño (%)**: el valor ya no es un tamaño en mm sino un **porcentaje de los tamaños actuales** — 100 % deja cada elemento con el tamaño que ya tiene dibujado, y el ajuste escala todos a la vez en vez de fijar un tamaño absoluto por clase.

### Colores

El bloque **Colores** controla el color de cada clase. El desplegable **Colores** (`cbColors`) ofrece, además de Manual/Equal/Random, las rampas y paletas de la biblioteca agrupadas por tipo:

- **Manual** — cada clase mantiene el color que tenga puesto a mano.
- **Igual** — un único color (botón de color junto al desplegable) para todas las clases.
- **Aleatorio** — colores aleatorios distintos por clase, con el mismo criterio de "colores aleatorios barajados" (shuffle) que usa QGIS de forma nativa. El botón de refrescar junto al desplegable (visible solo en este modo) vuelve a barajar los colores sin cambiar nada más.
- **2 colors Ramps / 3 colors Ramps / > 3 colors Ramps** — rampas de color continuas, agrupadas por cuántos colores definen la rampa.
- **Paletas extendidas** — paleta categórica cuyos colores se reparten a lo largo del rango de clases conservando el primero y el último.
- **Paletas secuenciales** — paleta categórica cuyos colores se asignan en el orden en que están declarados en la paleta.
- **Paletas etiquetadas** — paleta categórica donde cada clase recibe el color cuya etiqueta coincide con su propio valor.

El propio editor **recomienda una opción** según el tipo de leyenda (Span Palettes para leyendas numéricas; Labeled Palettes si existe una paleta etiquetada que encaje con las categorías de la capa, o Sequential Palettes en cualquier otro caso categórico): esa opción aparece en negrita con el sufijo "(recommended)". Las opciones sin ninguna rampa/paleta de ese tipo en la biblioteca activa, o Labeled Palettes sobre una leyenda numérica, aparecen deshabilitadas con un tooltip explicando el motivo.

La casilla **Invertir** intercambia el sentido de la rampa/paleta elegida.

> 💡 Para la capa de nodos del árbol de conectividad (Tree), el color de la fila no tiñe el símbolo entero: edita solo el **color de trazo (stroke)** del círculo exterior del nodo, dejando la estrella y los iconos de elemento con su color propio.

### Biblioteca de rampas y paletas

Junto al desplegable Colors, **Biblioteca Símbolos** deja elegir de dónde salen las rampas y paletas que ofrece ese desplegable:

- **Usar valor por defecto** — la biblioteca que trae QGISRed de serie.
- **Usar propia** — tu propia biblioteca editable. Al seleccionarla aparece el botón **Editar propia**, que abre el gestor de estilos nativo de QGIS (Style Manager) sobre esa biblioteca para añadir, editar o borrar rampas, paletas y símbolos. Los cambios que hagas ahí se reflejan al momento en el desplegable Colors, incluso recalculando los colores ya aplicados si la rampa activa cambió.

### Opacidad y borde (capas de relleno)

En capas cuyo símbolo es un relleno de polígono (por ejemplo, Sectores Hidráulicos y de Demanda), el panel añade dos controles que se aplican **a la vez a todas las clases**, no clase por clase:

- **Opacidad** (0–100 %) — opacidad del relleno; 100 % es sólido, 0 % invisible.
- **Borde** — modo del borde de cada clase: "Sin borde", "Negro", "Color del relleno" (el borde toma el mismo color que el relleno) o "Más oscuro que el relleno"; con cualquier opción salvo "Sin borde" aparece además el ancho del borde en mm.

### Reglas de estilo específicas por tipo de capa

Los elementos de entrada (Inputs) y algunas capas de consulta llevan reglas de estilo con estados fijos que el color/tamaño que elijas respeta, en lugar de sobrescribir el símbolo entero. Por ejemplo, Pipes/Valves/Pumps mantienen en rojo el estado "cerrada" y las Valves activas en naranja pase lo que pase con el color que elijas para el resto. Entre las capas con reglas propias:

- **Demandas múltiples**: el color elegido solo tiñe la rama de "demanda positiva" del símbolo (el marcador interior), igual que en Junctions; la demanda negativa y el resto del símbolo mantienen sus colores fijos.
- **Uniones**: con el selector **Demanda** en "Salidas (> 0)" o "Entradas (< 0)" puedes clasificar y colorear cada grupo de nudos por separado; las demandas negativas conservan siempre blanco en las leyendas automáticas por rango.
- **Válvulas de seccionamiento**: el color elegido solo sustituye al estado "abierta, sin pérdida de carga"; los colores de cerrada (rojo), con pérdida de carga (ámbar) y no disponible (gris) están fijados por la propia leyenda y no se pueden editar desde aquí.
- **Medidores**: el color y el tamaño se aplican según lo que tengas seleccionado en **Tipo de medidor** — a todos los tipos de contador a la vez, o solo al tipo elegido, sin tocar el resto de iconos apilados.
- **Acometidas**: el color elegido se aplica al trazo de la acometida activa y a una versión más clara del mismo color para su relleno; el resto de estados conserva su color propio.
- **Conect_Líneas** (resultado de la herramienta de Conectividad, dentro de Queries): a diferencia de las anteriores, no tiene reglas por estado — el color y el tamaño se aplican directamente sobre el símbolo, como en cualquier capa Single Symbol.

### Cargar y guardar estilos

Los botones **Cargar** y **Guardar**, en la parte inferior del diálogo, abren cada uno un menú:

**Cargar**
- **Estilo por defecto** — recupera el estilo por defecto de QGISRed para ese tipo de capa.
- **Estilo global** — carga un estilo que hayas guardado previamente a nivel global (válido para cualquier proyecto).
- **Estilo del proyecto** — carga un estilo guardado dentro de este proyecto.
- **Volver a la leyenda original** — recupera en el diálogo la leyenda que tenía la capa en el momento de abrir el editor (sin necesidad de cerrar y reabrir el diálogo).

**Guardar**
- **To Global...** — guarda la leyenda actual como estilo global, reutilizable en cualquier proyecto.
- **To Project...** — guarda la leyenda actual dentro de la carpeta `layerStyles` de este proyecto.

Al guardar, un pequeño diálogo te deja elegir si quieres guardar la leyenda **tal cual se ve** o una **estrategia** que se regenere automáticamente la próxima vez que la cargues (marcando qué partes conservar: la estructura de clases/intervalos, los tamaños y/o los colores).

> ⚠️ Tanto **Cargar** como **Volver a la leyenda original** solo actualizan la vista previa del diálogo. La capa del proyecto no cambia hasta que pulses **Aplicar** o **Aceptar**.

### Aplicar, Aceptar y Cancelar

Los tres botones inferiores tienen una semántica de vista previa muy concreta:

- **Aplicar** — aplica los cambios mostrados en el diálogo a la capa, sin cerrar el editor. Útil para ir viendo el resultado en el lienzo mientras sigues ajustando.
- **Aceptar** — aplica los cambios a la capa y cierra el diálogo (equivale a Apply + cerrar).
- **Cancelar** — cierra el diálogo y **restaura la capa a la leyenda que tenía cuando la seleccionaste** en este editor, deshaciendo también los cambios que ya hubieras aplicado con Apply. Si había cambios aplicados, QGISRed pide confirmación antes de descartarlos.

> 💡 Como Cancel siempre vuelve al estado de partida (aunque hayas pulsado Apply varias veces mientras probabas cosas), es la forma segura de "empezar de nuevo" con una capa sin tener que reconstruir su leyenda a mano.
