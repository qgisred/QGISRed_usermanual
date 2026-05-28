# 📜 Registro de Cambios (Changelog)

Mantente al día con las últimas mejoras de QGISRed.

### Versión 0.18 (Abril 2026)
**Versiones de QGIS**: 3.28-4.99

*Esta versión ha sido financiada por el [Banco Interamericano de Desarrollo (BID)](https://www.iadb.org/es) a través del contrato C-RG-T4041-P001.*

**Novedades**:
*   Mejoras en el Gestor de Proyectos. Nuevos botones para Mover y Exportar proyectos, y nuevas opciones para Renombrar proyectos.
*   Identificación de todas las capas gestionadas por QGISRed mediante un Id propio, en lugar de hacerlo por el nombre, lo que permite trabajar en varios idiomas.
*   Revisión de los símbolos, etiquetas y avisos del mapa asociados a todas las capas gestionadas por QGISRed.
*   Mayor integración del Editor de Propiedades de los Elementos, manteniendo las propiedades de las capas, y el refresco de los datos en todas las ventanas afectadas, incluida la tabla de atributos.
*   Almacenamiento del estilo de todas las capas gestionadas por QGISRed en ficheros .qml a tres niveles: por defecto, nivel de usuario y nivel de proyecto.
*   Almacenamiento en una tabla propia de todas las magnitudes manejadas por QGISRed, especificando las unidades y decimales a mostrar en los distintos sistemas de unidades y según la casuística.
*   Creación de un Editor de Leyendas propio para personalizar rangos o clases, colores y tamaños de todas las leyendas manejadas por QGISRed.
*   Asistentes para personalizar las leyendas automáticamente.
*   Adición de un nuevo menú y una nueva barra de herramientas para alojar las nuevas opciones orientadas a realizar consultas sobre datos y resultados.
*   Reorganización de las capas del grupo de Consultas, y del almacenamiento de los ficheros shp correspondientes en la estructura de carpetas del proyecto.
*   Nueva herramienta para localizar en el mapa cualquier elemento a través de su Id e identificar los elementos conectados, con la opción de navegar a través de los mismos.
*   Nuevo panel para observar los datos y resultados de cualquier elemento de la red seleccionado. Sincronización de los resultados con el instante actual de la simulación.
*   Nuevo diálogo para crear mapas temáticos de algunas magnitudes asociadas a los distintos tipos de elementos manejados por QGISRed.
*   Nuevo panel para localizar en el mapa los elementos que cumplen determinados criterios en relación a los datos o los resultados. Sincronización con los resultados para el instante actual de la simulación.
*   Mejora del formato en que se exporta el fichero INP desde QGISRed, similar al que se exportaría desde la Toolkit de EPANET.
*   Sustitución del motor de cálculo de EPANET 2.2 por la nueva versión 2.3, hasta la revisión más reciente 2.3.5.
*   Lectura de los resultados de una simulación directamente desde los ficheros binarios de EPANET para una navegación más rápida y ágil.
*   Incorporación del Informe de Estado al panel de resultados en una nueva pestaña, siempre accesible.
*   Exportación de todos los resultados de una simulación a un fichero CSV estructurado.
*   Nueva opción para mostrar diversas estadísticas sobre los resultados a lo largo de todo el periodo de simulación.
*   Nueva ventana para mostrar la curva de evolución en el tiempo de cualquier magnitud de un elemento a lo largo del periodo de simulación. Posibilidad de superponer varias curvas para la misma o distinta magnitud.
*   Mejoras en el Constructor de Demandas para las demandas puntuales. Revisión de los algoritmos y carga automática de los enlaces. Nuevo tema para los puntos de demanda.
*   Revisión de la herramienta de identificación de los sectores hidráulicos y detección de los consumos aislados.
*   Revisión del algoritmo para identificar cerradas. Detección de los consumos aislados.
*   Nuevas opciones a nivel de proyecto para trasladar las demandas de las acometidas a los nudos. Clasificación de las demandas por patrones.
*   Compatibilización de la versión 0.18 con las nuevas versiones de QGIS 4.0.
*   Traducción de todos los diálogos, paneles, mensajes y nombres de capas de QGISRed al idioma español.
*   Rediseño de todos los iconos manejados por QGISRed con un aspecto más uniforme y agradable.
*   Alojamiento en web del manual provisional de QGISRed en inglés y español para su consulta on-line a través de la plataforma colaborativa GitBook.
*   Mención al Banco Interamericano de Desarrollo (BID) por el soporte financiero a todas las mejoras realizadas en la presente versión 0.18.

**Correcciones**:
*   Resuelto un problema al cargar los datos de campo relacionado con el separador decimal.
*   Corregido un error que impedía cancelar las demandas de las zonas que quedan aisladas.
*   Limitación del tamaño del campo Descripción, usado para informar sobre las demandas de las acometidas cargadas a cada nudo.

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


