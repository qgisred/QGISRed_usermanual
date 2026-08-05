# 📜 Registro de Cambios (Changelog)

Mantente al día con las últimas mejoras de QGISRed.

### Versión 0.19

**Novedades**:

*   Reestructuración completa del panel de Estadísticas: nuevas pestañas Setup/Report, histograma con ventana flotante y selector de estadístico en el eje Y, y segunda clasificación cruzada con matriz de resultados.
*   Nuevas opciones de visualización en el panel de Resultados: tamaño proporcional al valor en nudos y tuberías, y contorno negro opcional en marcadores de nudo.
*   Etiquetas de mapa mejoradas: muestran tipo e Id del elemento en la primera línea y valor con unidades en la segunda.
*   Tooltips de mapa visibles en todas las capas activas gestionadas por QGISRed, independientemente de la capa seleccionada en la leyenda.
*   Evolución temporal rápida directamente desde el dock de Resultados, sin necesidad de abrir el panel de Series Temporales.
*   Mejoras en el panel de Series Temporales: nuevas magnitudes de depósito (Volume y TankSpill), cursor sincronizado con la tabla de valores, copia de tabla con doble cabecera (nombre y unidad), exportación e importación de la configuración del gráfico y soporte para múltiples ventanas simultáneas.
*   Diálogo de progreso de simulación con opción de no volver a mostrarse (configurable desde Propiedades del Proyecto).
*   Mejora en la gestión de errores de simulación: el informe EPANET se muestra automáticamente en el log al producirse un error, y los errores no controlados quedan registrados en lugar de fallar silenciosamente.
*   Aviso específico cuando los ficheros de resultados están bloqueados por otra aplicación.
*   Constructor de Demandas: reestructuración de la sección de patrones por sectores con dos modos excluyentes (importar SHP externo / usar capa del proyecto).
*   Constructor de Demandas: sección de eficiencia por sectores con dos modos de trabajo, y nuevas opciones para corregir eficiencias de categorías y patrones de sectores para cumplir objetivos globales.
*   Constructor de Demandas: distribución automática de porcentajes de demanda faltantes en capas de tramos.
*   Nueva capa de acometidas aisladas con demanda no nula generada al analizar segmentos hidráulicos.
*   Árbol de distribución: el nodo raíz se identifica con `NodeType = "ROOT"` en la capa de nudos resultante.
*   Renombrado de campos identificadores en las capas SHP del proyecto (ej. `Id` → `JunctionID`, `PipeID`, etc.). Los proyectos creados con versiones anteriores siguen siendo compatibles gracias a la tabla de nombres heredados.
*   Categoría sin asignar renombrada de "Undefined" a **"Uncategorized"** en el Constructor de Demandas y en la leyenda de capas.

