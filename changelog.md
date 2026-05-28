# 📜 Registro de Cambios (Changelog)

Mantente al día con las últimas mejoras de QGISRed.

### Versión 0.18 (Abril 2026)
**Versiones de QGIS**: 3.28-4.99

*Esta versión ha sido financiada por el [Banco Interamericano de Desarrollo (BID)](https://www.iadb.org/es) a través del contrato C-RG-T4041-P001.*

**Novedades**:
*   Mejoras en el Gestor de Proyectos: nuevos botones para mover y exportar proyectos, y nuevas opciones para renombrar proyectos.
*   Identificación de todas las capas gestionadas por QGISRed mediante un ID propio en lugar del nombre, lo que permite trabajar en varios idiomas.
*   Revisión de los símbolos de mapa, etiquetas y avisos asociados a todas las capas gestionadas por QGISRed.
*   Almacenamiento de los estilos de todas las capas en archivos `.qml` a tres niveles: por defecto, nivel de usuario y nivel de proyecto.
*   Incrustación de símbolos en los archivos de estilo `.qml` para evitar dependencias de ruta.
*   Revisión de todas las herramientas de edición gráfica para un funcionamiento más fluido y robusto.
*   Posibilidad de definir una cuadrícula de fondo para crear trazados de tuberías con geometría regular.
*   Al crear una nueva tubería, si uno de sus extremos solapa el trazado de una existente, se crea automáticamente una conexión en T.
*   El símbolo de demandas múltiples se ha sustituido por un doble círculo.
*   Cada herramienta de edición o interacción con el mapa tiene ahora su propio icono asociado al cursor, facilitando identificar la herramienta activa.
*   Mayor integración del editor de propiedades de elementos, manteniendo las propiedades de capa y actualizando los datos en todas las ventanas afectadas, incluida la tabla de atributos.
*   Almacenamiento en una tabla dedicada de todas las magnitudes gestionadas por QGISRed, especificando las unidades y decimales a mostrar según el sistema de unidades y el caso.
*   Nuevo Editor de Leyendas propio para personalizar rangos, clases, colores y tamaños de todas las leyendas gestionadas por QGISRed, con asistentes de configuración automática.
*   Reorganización de las capas del grupo Queries y almacenamiento de los archivos SHP correspondientes en las carpetas del proyecto.
*   Nueva barra de herramientas Queries con todas las opciones de consulta de datos y resultados.
*   Nueva herramienta para localizar cualquier elemento en el mapa por su ID e identificar sus elementos conectados con opción de navegación entre ellos.
*   Nuevo panel para visualizar datos y resultados de cualquier elemento de red seleccionado, sincronizado con el instante de simulación activo.
*   Nuevo diálogo para crear mapas temáticos de propiedades de los distintos tipos de elementos gestionados por QGISRed.
*   Nuevo panel para localizar en el mapa los elementos que cumplen criterios sobre datos o resultados, sincronizado con el instante de simulación activo.
*   Mejora del formato de exportación del archivo INP, equiparable al exportado por el Toolkit de EPANET.
*   Sustitución del motor de cálculo EPANET 2.2 por la nueva versión 2.3, hasta la revisión 2.3.5.
*   Incorporación del informe de estado (Status Report) al panel de resultados en una nueva pestaña siempre accesible.
*   Lectura de resultados de simulación directamente desde los archivos binarios de EPANET para una navegación más rápida y eficiente.
*   Exportación de todos los resultados de simulación a un archivo CSV estructurado.
*   Nueva opción para visualizar diversas estadísticas de los resultados a lo largo de todo el período de simulación.
*   Nueva ventana para mostrar curvas de evolución temporal de cualquier variable de un elemento. Posibilidad de superponer varias curvas de la misma o distinta magnitud.
*   Revisión del algoritmo de asignación de demandas puntuales en el Gestor de Demandas, con carga automática de la capa de enlaces y una nueva capa de puntos de demanda.
*   Revisión de la herramienta de identificación de sectores hidráulicos y detección de puntos de consumo aislados.
*   Revisión del algoritmo de identificación de segmentos aislados y detección de demandas aisladas.
*   Nuevas opciones de Gemelo Digital a nivel de proyecto para trasladar demandas de acometidas a nudos y clasificarlas por patrones.
*   Reescritura del código del plugin para evitar archivos de gran tamaño y mejorar la trazabilidad, el mantenimiento y la escalabilidad.
*   Compatibilidad de QGISRed 0.18 con las nuevas versiones de QGIS 4.0.
*   Traducción completa al español de todos los diálogos, paneles, mensajes y nombres de capa gestionados por QGISRed.
*   Rediseño de todos los iconos gestionados por QGISRed con una apariencia más uniforme y atractiva.
*   Manual de usuario provisional en inglés y español alojado en GitBook para consulta en línea.
*   Nuevo sistema de notificaciones para alertar a los usuarios sobre nuevas versiones, cursos, actualizaciones del manual, etc.

**Correcciones**:
*   Corregido error al cargar datos de campo relacionado con el separador decimal.
*   Corregido error que impedía cancelar la demanda de zonas aisladas.
*   Limitado el tamaño del campo `Description` usado para informar sobre las demandas de acometidas cargadas en cada nudo.
*   Corregido error por el que el final del informe de EPANET no aparecía en ciertos casos.
*   Corregido error al tener capas abiertas en varias aplicaciones simultáneamente (p. ej., dos ventanas de QGIS).

---

### Versión 0.17 (Enero 2026)
**Versiones de QGis**: 3.2-3.99 

**Novedades**:
*   Nueva herramienta de exploración de cerradas, con múltiples opciones.
*   Visualización en los resultados de hasta 13 estados para tuberías, válvulas y bombas.
*   Transferencia de estados y calidades para el encadenamiento de simulaciones en periodos sucesivos.
*   Nuevas opciones para resetear rugosidades, elevaciones y diámetros en el constructor de escenarios.
*   Nueva opción para exportar e importar escenarios con el formato de Epanet.
*   Nuevas funcionalidades en el gestor de proyectos (ordenar, exportar, borrar y renombrar).
*   Nuevos botones para abrir o guardar proyectos.
*   Nueva opción para importar un proyecto de QGISRed.
*   Cambios en iconos y nombres en algunas opciones de menú.
*   Ampliada la precisión al escribir valores numéricos en los shapes.
*   Mejora en el mensaje a la hora de descargar las dependencias necesarias.

**Correcciones**:
*   Corregido error al interpolar cotas cuando el punto cae en alguno de los extremos de la malla.
*   Corregido error al repartir las demandas en proporción a la longitud de las tuberías.
*   Corregido error al cargar demandas a partir de una capa de sectores.
*   Corregido error al importar INPs con sources sin patrón definido.
*   Corregidos errores al importar INP relacionados con los Times y las Rules temporales.
*   Corregido error al exportar INPs con descripciones muy largas.
*   Corregido error con el símbolo decimal en las opciones del modelo PDA.


