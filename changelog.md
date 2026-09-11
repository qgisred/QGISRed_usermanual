# 📜 Registro de Cambios (Changelog)

Mantente al día con las últimas mejoras de QGISRed.

### Versión 0.19

**Interfaz de usuario**:

*   Agrupación de las opciones de tipo informativo como Novedades, Incidencias, Manual, Valoración, Suscripciones y Acerca de... en una nueva entrada Info del menú principal.
*   Reubicación del menú de Consultas tras el menú de Herramientas, en la barra del menú principal.
*   Incorporación de una marca y un prefijo en el título de todos los paneles de QGISRed para diferenciarlos de otros.
*   Incorporación de un icono de aviso en aquellas capas que pueden quedar desactualizadas al realizar cambios en los datos.

**Gestor de proyectos**:

*   Ahora se puede cambiar independientemente el nombre del proyecto de QGISRed y el nombre del fichero que aloja la información del mapa (qgz).
*   Al mover un proyecto, se pueden mover los datos y el fichero del mapa (qgz) conjuntamente, o de forma independiente a carpetas distintas.
*   Se ha eliminado la opción de hacer un backup del proyecto, y se ha sustituido por la opción de Exportar el proyecto, con más alternativas.
*   Al exportar un proyecto se pueden elegir los grupos de capas de QGISRed y las capas ajenas al proyecto (cartografías, MDT, etc.) a copiar, entre las presentes en el panel de capas. Todo ello se guarda en un único fichero .zip.
*   Para exportar el fichero qgz del mapa, debe estar en la misma carpeta del proyecto o en un nivel superior. La información cartográfica debe estar en carpetas paralelas a la carpeta del proyecto.
*   Al importar un proyecto de QGISRed se restaura en una nueva carpeta toda la información previamente exportada, manteniendo la estructura de todos los ficheros.

**Importación de shapes**:

*   Posibilidad de seleccionar las tuberías candidatas para conectar las acometidas que parten de los puntos de consumo importados.

**Tablas de materiales**:

*   Declaración de una tabla de materiales por defecto distinta para cada uno de los cuatro idiomas soportados.
*   Nuevas opciones en el diálogo de edición de la tabla de materiales, para copiar, cargar y editar nuevas tablas a nivel global, antes de crear un proyecto o desde dentro de él.
*   Nuevas opciones para elegir la tabla de materiales deseada al crear un nuevo proyecto o importar ficheros shape por primera vez.

**Gestión de capas**:

*   Creación de un nuevo grupo de capas denominado CapasAuxiliares para alojar temas complementarios a los temas básicos.
*   Creación de un subgrupo dentro del grupo de Capas Auxiliares, denominado Constructor de Demandas, para alojar sus temas propios: sectores, demandas puntuales y enlaces.
*   Incorporación de una nueva pestaña al Gestor de Capas para crear, borrar, cargar o descargar las capas auxiliares vinculadas al Constructor de Demandas.

**Edición gráfica**:

*   Pulsando con la varita sobre una bomba, válvula o tubería, ahora se alterna solo entre los estados abierto y cerrado.
*   Para alternar entre el estado activo o cerrado de una válvula, o declarar una CV en una tubería, mantener la tecla Ctrl al pulsar con la varita.
*   Al insertar una bomba o válvula en un tramo menor que la separación establecida entre los nudos extremos, éstos se mantienen y ya no se desplazan.
*   Al mover un nudo ya no se queda ninguna capa abierta, evitando conflictos con otras herramientas de edición.
*   Revisada la herramienta de edición de vértices para hacer más amigable su manejo.
*   Al partir una tubería por un punto intermedio, se desdobla el Id añadiendo un sufijo numérico. El Id original puede recuperarse si los tramos se funden en sentido inverso al que se crearon los nudos intermedios.
*   Cuando dos tuberías en serie no pueden unirse eliminando el nudo intermedio, se informa de la causa.
*   Revisada la herramienta de fundir o separar nudos, permitiendo mayor separación entre ellos.
*   Al crear una conexión en T ahora se prolonga el último tramo de la derivación hasta intersectar con la tubería principal.
*   Revisadas las herramientas de deshacer T y cruces, eliminando algunas restricciones y uniformando las acciones del ratón.

**Edición de propiedades en grupo**:

*   Nueva opción del menú Edit para editar las propiedades de los elementos en grupo.
*   Preselección gráfica de los elementos a modificar con las herramientas de selección múltiple.
*   Aplicación de filtros para restringir los elementos a modificar, según el tipo de propiedad.
*   Opción para visualizar en el mapa los elementos que van a ser modificados.
*   Múltiples opciones para modificar la propiedad elegida, diferenciando si la propiedad es numérica, de texto o enumerada.
*   Visualización previa en la tabla de atributos de los cambios realizados antes de consolidarlos.

**Mapas temáticos**:

*   Incorporación de nuevos mapas temáticos vinculados a las tuberías: Año de instalación, edad, y coeficiente de rugosidad según fórmula de pérdidas.
*   Nuevos mapas temáticos vinculados a las uniones: Elevaciones y Demanda base total graduada por tamaño.
*   Al confeccionar el mapa de materiales, ahora a cada material se le asigna un color propio en función de su abreviatura e idioma, el cual es editable.
*   Cuando un mapa temático queda desactualizado por un cambio de unidades o fórmula de pérdidas, se muestra un icono de advertencia, pudiendo actualizarlo pinchando en él.

**Editor de leyendas**:

*   Mejoras en los asistentes para crear automáticamente rangos, tamaños y colores para configurar la leyenda de todas las capas.
*   Posibilidad de modificar algunos parámetros de estilo de los temas básicos del grupo Datos.
*   Incorporación al Editor de Leyendas de QGISRed de las capas creadas por Consultas (mapas temáticos, sectores hidráulicos, árboles, etc.).
*   Incorporación de las capas de Resultados al Editor de Leyendas para personalizar su estilo.
*   Opción para guardar las leyendas a nivel de proyecto, o a nivel de usuario para aplicarlas en nuevos proyectos.
*   Opción para almacenar los asistentes con los cuales adaptar la leyenda a los datos, en lugar de guardar una leyenda preconfigurada.
*   Creación de una biblioteca de símbolos, rampas y paletas de colores propia de QGISRed, accesible desde el Editor de Leyendas y editable desde QGIS.

**Constructor de demandas**:

*   Opción para consolidar los parámetros importados relativos a la asignación de demandas por sectores en un tema propio de QGISRed.
*   Opción para repartir la demanda global o por sectores en base a los diámetros que confluyen en los nudos candidatos.
*   Opción para declarar los consumos por tramos lineales o por polígonos, como alternativa a los consumos puntuales.
*   Opción para consolidar los consumos puntuales importados en un tema propio de QGISRed.
*   Opción para gestionar los temas propios de consumos puntuales y agregar varias demandas al mismo tema.
*   Reconocimiento de diversas unidades a la hora de declarar los consumos a importar.
*   Opción para asignar las demandas puntuales a los extremos de la tubería más próxima en lugar de buscar directamente los nudos más próximos.
*   Opción para considerar o no los extremos de bombas y válvulas como posibles nudos de demanda.
*   Opción para distribuir las demandas puntuales en base a los diámetros de las tuberías que confluyen en los nudos, o en combinación con su distancia a los puntos de consumo.
*   Notificación de los nudos cargados que queden alejados más de una distancia dada de los puntos de consumo.
*   Posibilidad de editar y reutilizar los enlaces entre puntos de consumo y nudos de demanda.
*   Asignación de las demandas a los nudos a partir de las acometidas declaradas como elementos del Gemelo Digital.
*   Diferenciación de las demandas base por categorías, tanto en consumos puntuales como por acometidas, creando demandas múltiples en los nudos.
*   Opción para cargar las demandas solo de los sectores, puntos de consumo o acometidas seleccionados.
*   Opción de usar un tema propio para asignar rendimientos y patrones por sectores, importar sus valores y editarlos.
*   Opción para aplicar rendimientos hídricos y asignar patrones de demanda por categorías.
*   Opción para reajustar rendimientos y patrones declarados a un nivel por los impuestos a otro nivel superior (categorías -> sectores -> global).

**Panel de estadísticas**:

*   Nueva opción en el menú de Consultas para realizar todo tipo de estadísticas con los datos del modelo y los resultados.
*   Evaluación de las estadísticas de una magnitud, clasificadas por rangos o clases de dicha magnitud u otra magnitud del mismo tipo de elemento.
*   Posibilidad de usar una segunda magnitud de clasificación para crear tablas de doble entrada.
*   Posibilidad de aplicar filtros sobre los datos de partida y visualizar en el mapa los elementos afectados por la consulta.
*   Visualización de las estadísticas en histogramas o mediante una tabla de valores exportable.
*   Exportación de la configuración de la consulta y su posterior importación.

**Consultas de topología**:

*   Revisadas las herramientas de Conectividad, Sectores hidráulicos y Grafos en árbol: nuevos nombres, reubicación de las capas, cambios de estilo, etc.
*   Nuevo tema para resaltar las demandas aisladas en los Sectores hidráulicos.
*   Posibilidad de crear y gestionar la existencia de varios temas para los Grafos en árbol (ahora denominados Árboles de Mínimo Coste).

**Simulación**:

*   Nuevo diálogo de progreso para mostrar el avance de los cálculos hidráulicos y de calidad.
*   El diálogo de progreso puede pausarse para observar detenidamente el avance de los cálculos.
*   El diálogo de progreso puede omitirse para mayor agilidad en los cálculos, salvo para redes con largos tiempos de procesamiento.

**Panel de resultados**:

*   Opción para mostrar todos los instantes de cálculo en el mapa de resultados y demás paneles en los que interviene el tiempo.
*   Opción para mostrar el instante de la simulación en diversos formatos: tiempo transcurrido desde el inicio (en horas acumuladas o agrupadas por días) o bien hora civil (en formato 24 h o am/pm).
*   Nueva barra de botones para realizar animaciones a velocidad controlada o paso a paso.
*   Las variables elegidas para mostrar los resultados de nudos y líneas son ahora resaltadas y tienen asignado un color propio.
*   Nueva pestaña con varias opciones para mejorar la visualización de los resultados en el mapa, la simbología y el color del fondo.
*   Nueva opción para mostrar en un histograma la distribución de la variable actual de nudos o líneas y sus valores acumulados, en el instante actual.
*   Nueva opción para mostrar una curva simplificada de evolución de la variable actual de nudos o líneas, para el elemento elegido en el mapa.
*   Al rescatar el Panel de Resultados se conservan las opciones de la última acción, en lugar de aplicar las opciones por defecto.
*   Cuando se cambian los datos del escenario, las capas de resultados muestran un icono de advertencia, pudiendo actualizarse pinchando en él.

**Gráficos de evolución**:

*   Nuevos botones para navegar en el gráfico de las curvas de evolución.
*   Nuevo botón con múltiples opciones para personalizar el aspecto de todos los componentes de la gráfica.
*   Adaptación de la escala de tiempos conforme a las opciones elegidas en el Panel de resultados.
*   Posibilidad de mostrar todos los instantes de tiempo o solo instantes pautados, según se elija en el Panel de resultados.
*   Sincronización opcional del cursor con el instante actual del Panel de resultados.
*   Incorporación de la evolución del volumen de un depósito o del caudal desbordado, como nuevas variables.
*   Opción para representar las curvas de evolución de algunas variables globales para todo el sistema.
*   Nuevo botón para mostrar en una tabla los valores numéricos de los puntos de paso de las curvas de evolución y exportar sus valores a un fichero CSV.
*   Nuevo botón para exportar las gráficas como imágenes.
*   Opción para guardar y recuperar la configuración de los gráficos de evolución, incluida la creación de plantillas.
*   Posibilidad de crear y mantener abiertas varias ventanas de curvas de evolución al mismo tiempo.

**Idiomas**:

*   Todas las opciones de menú, diálogos y mensajes de QGISRed se muestran ahora también en francés y en portugués brasileño, cuando se elige este idioma para la interfaz de QGIS. Actualmente ya se muestran en inglés y en español.

**Otros cambios**:

*   Verificados todos los controles de seguridad y corregidas las incidencias relativas a la calidad del código, notificadas por el sistema Security Scan de QGIS.
*   Revisada la compatibilidad del código de la versión 0.19 con Qt6 y QGIS 4.xx.
*   Fin del soporte para las librerías de QGISRed en sistemas de 32 bits (x86). En adelante QGISRed solo funcionará en sistemas de 64 bits.
*   Eliminados los botones de minimizar y maximizar en todos los diálogos incorporados en las librerías.
*   Revisados los nombres de algunos campos de los ficheros shape, tablas dbf y ficheros CSV, por uniformidad. Todos los campos de identificadores terminan ahora con ID.
*   Revisados los nombres de las propiedades mostrados en todos los diálogos de QGISRed, según el idioma, por uniformidad.
*   Revisados los decimales mostrados en las tablas de atributos de los temas, en función de las unidades empleadas.

**Corrección de errores**:

*   Revisión de las posibles situaciones al cargar las librerías de GISRed para evitar intentos repetidos.
*   Revisión del formato de exportación de los ficheros INP para evitar solapamientos que causaban errores de lectura.
*   Subsanado un error que impedía crear nuevas curvas de comportamiento.
*   Comprobación de que los identificativos de los elementos, curvas y patrones no contengan ningún espacio en blanco.
*   Subsanado un error que impedía consolidar la hora civil de inicio de la simulación.
