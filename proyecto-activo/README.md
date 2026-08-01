# 📋 Proyecto

La barra **Project** agrupa las herramientas de administración del proyecto que ya está abierto en QGISRed. Todos sus botones requieren un proyecto válido cargado; si no hay ninguno, el plugin avisará con el mensaje _"No valid project is opened"_.

<figure><img src="../assets/images/proyecto/barra-project.png" alt="Barra de herramientas Project de QGISRed con sus nueve botones"><figcaption><p>Barra de herramientas Project de QGISRed con sus nueve botones</p></figcaption></figure>
*Barra Project: herramientas de administración del proyecto activo.*

<!-- TODO: captura desactualizada tras la eliminación del botón "Project backup" (commit 7b2415f) -->

---

## Botones de la barra Project

| # | Herramienta | Función |
|---|-------------|---------|
| 1 | **Resumen** | Número de elementos de cada tipo en la red |
| 2 | **Añadir datos por importación** | Importa elementos adicionales al proyecto abierto |
| 3 | **Gestor de capas** | Controla la visibilidad de capas y recupera capas borradas |
| 4 | **Editor de leyenda** | Personaliza la simbología de las capas |
| — | *(separador)* | |
| 5 | **Opciones del proyecto** | Parámetros EPANET: unidades, fórmula, calidad, tiempos, energía |
| 6 | **Valores por defecto** | Prefijos de ID, tolerancias y valores hidráulicos iniciales |
| 7 | **Tabla de materiales** | Rugosidades y tasas de envejecimiento por material |
| — | *(separador)* | |
| 8 | **Guardar mapa** | Guarda el archivo `.qgz` de QGIS |
| 9 | **Cerrar proyecto** | Cierra el proyecto y limpia la sesión de QGIS |

> 💡 El antiguo botón **Copia de seguridad** (_Project backup_) se ha eliminado de esta barra sin sustituto directo. Para exportar el proyecto a un ZIP portable, usa el botón **Export** del [Gestor de proyectos](../gestion-proyectos/gestor-proyectos.md) — ver [Guardar, exportar y cerrar proyecto](guardar-backup.md).

## En esta sección

* [Resumen y gestión de capas](capas-y-leyenda.md) — visibilidad de capas, recuperación y leyenda
* [Configuración del proyecto](configuracion.md) — opciones EPANET, valores por defecto, materiales
* [Guardar, exportar y cerrar proyecto](guardar-backup.md) — guardar el mapa, exportar a ZIP y cerrar
