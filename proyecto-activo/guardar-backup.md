# Guardar, exportar y cerrar proyecto

***

## Guardar el mapa de proyecto

**Barra Project → Guardar mapa** (Save project map)

Guarda el archivo QGIS (`.qgz`) que contiene la configuración visual del proyecto: capas cargadas, estilos, visibilidad de grupos, encuadre del mapa, etc.

### Primera vez

Si el proyecto QGIS no tiene todavía un archivo `.qgz`, el plugin abre el diálogo estándar de QGIS **"Guardar como"** sugiriendo automáticamente la carpeta del proyecto QGISRed y el nombre de la red como nombre de archivo:

```
{CarpetaProyecto}/{NombreRed}.qgz
```

### Guardados posteriores

Si ya existe un `.qgz`, lo sobreescribe directamente (equivalente a `Ctrl+S` en QGIS).

> 💡 **Recomendación**: guarda el `.qgz` en la misma carpeta que los SHP del proyecto. Así, si copias la carpeta a otro equipo, el archivo `.qgz` encontrará los SHP sin necesidad de reconfigurar rutas.

> ⚠️ Guardar el `.qgz` **no guarda los datos de la red**. Los datos (diámetros, cotas, demandas…) se guardan automáticamente en los SHP+DBF en el momento en que QGISRed los modifica. El `.qgz` solo guarda la presentación visual.

***

## Exportar el proyecto

**Gestor de proyectos → Export**

> ⚠️ Este botón ya **no** está en la barra **Project**: el antiguo botón _Project backup_ se ha eliminado y no tiene sustituto en esa barra. La exportación ahora se hace desde el [Gestor de proyectos](../gestion-proyectos/gestor-proyectos.md) — selecciona el proyecto en la lista (no hace falta tenerlo abierto) y pulsa **Export**.

Genera un archivo ZIP portable con el proyecto: los SHP/DBF de la red, el mapa de QGIS (`.qgz`) si existe, y opcionalmente los grupos de contenido y los datos complementarios (cartografía de fondo, MDT, ortofotos…) que ese `.qgz` referencia.

### Antes de exportar

Si el proyecto que exportas es el que tienes abierto en QGIS y su `.qgz` tiene cambios sin guardar, QGISRed pregunta primero:

> _"The QGIS project has unsaved changes. Do you want to save it before exporting?"_

* **Yes**: guarda el `.qgz` y exporta esa versión recién guardada.
* **No**: exporta el `.qgz` tal como estaba en el último guardado (los cambios pendientes no viajan en el ZIP).
* **Cancel**: no se abre el diálogo de exportación.

### El diálogo de exportación

| Campo                                        | Función                                                                                 |
| -------------------------------------------- | --------------------------------------------------------------------------------------- |
| **File name:**                               | Nombre del ZIP (sin extensión); por defecto, el nombre de la red                        |
| **Folder:**                                  | Carpeta destino; por defecto, la carpeta de Descargas del usuario                       |
| **Content**                                  | Grupos opcionales a incluir (ver más abajo)                                             |
| **Complementary data**                       | Datos externos referenciados por el `.qgz`, seleccionables uno a uno                    |
| **Open the containing folder when finished** | Abre el explorador de archivos en la carpeta destino al terminar (activado por defecto) |

### Qué se incluye siempre

* Los SHP+DBF+PRJ propios de la red en la raíz de la carpeta del proyecto (Pipes, Junctions, Valves, Pumps, Tanks, Reservoirs, Demands, Sources…) y los ficheros de opciones y metadatos (`_Options.dbf`, `_Title.dbf`).
* El archivo `.qgz` del mapa, si QGISRed lo encuentra en la carpeta del proyecto o en su carpeta padre. Si no hay ningún `.qgz` guardado, el diálogo avisa de que la presentación visual del mapa no se exportará.

### Qué se incluye opcionalmente

Cuatro grupos de contenido, cada uno con su propia casilla en el apartado **Content** (marcada por defecto si el grupo tiene datos de esta red; si está vacío, la casilla aparece deshabilitada):

| Casilla              | Contenido                                                                                   |
| -------------------- | ------------------------------------------------------------------------------------------- |
| **Results**          | Resultados de simulaciones guardados en `Results/`                                          |
| **Issues**           | Incidencias detectadas por las verificaciones, en `Issues/`                                 |
| **Queries**          | Consultas guardadas, en `Queries/`                                                          |
| **Auxiliary Layers** | Capas auxiliares (por ejemplo, del Constructor de demandas nodales), en `Auxiliary Layers/` |

Si el `.qgz` referencia datos complementarios, el diálogo añade una tabla **Complementary data** con una fila por capa (nombre, ubicación y estado), cada una con su propia casilla — así puedes dejar fuera, por ejemplo, un MDT de varios GB sin renunciar al resto.

### Qué no se incluye

* Los grupos de contenido que dejes desmarcados.
* Los datos complementarios que están fuera de la carpeta del proyecto y de su carpeta padre: el diálogo los marca como _"Not exportable"_ y avisa antes de exportar. Para incluirlos, muévelos con el explorador de archivos a la carpeta del proyecto (o junto a ella) y vuelve a abrir el proyecto para que QGISRed los reenlace.
* Las capas de fondo remotas (servicios WMS, XYZ, bases de datos): no hay nada que copiar, así que nunca bloquean la exportación ni aparecen en la tabla.

> ⚠️ Si dejas fuera un grupo de contenido o una capa complementaria que el `.qgz` sigue usando, QGISRed te avisa antes de exportar. Pulsa **OK** una segunda vez si quieres continuar de todas formas.

### Dónde se guarda

```
{CarpetaDestino}/{NombreArchivo}.zip
```

Por defecto `{CarpetaDestino}` es la carpeta de Descargas del usuario y `{NombreArchivo}` es el nombre de la red, pero ambos son editables en el diálogo. Si ya existe un ZIP con ese nombre, QGISRed pregunta si quieres sobrescribirlo.

Al finalizar, QGISRed muestra en la barra de mensajes la ruta completa del ZIP creado.

> 💡 **Buenas prácticas**: exporta el proyecto antes de operaciones que modifiquen muchos elementos a la vez (importaciones masivas, cambios de CRS, conversiones de rugosidad) y antes de actualizar la versión del plugin. Para recuperar un proyecto exportado, usa **Importar proyecto → pestaña "QGISRed project"** — ver [Abrir e importar proyectos](../gestion-proyectos/abrir-importar.md).

***

## Cerrar proyecto

**Barra Project → Cerrar proyecto** (Close project)

Cierra el proyecto actual de QGISRed y limpia la sesión de QGIS: elimina todas las capas cargadas y restablece el estado inicial.

Es equivalente a usar _Proyecto → Nuevo_ en el menú de QGIS.

> ⚠️ Si hay cambios no guardados en el archivo `.qgz`, QGIS preguntará si deseas guardarlos antes de cerrar.

***

## Resumen: qué guarda cada opción

| Operación                                        | Qué guarda                                                                              | Dónde                                   |
| ------------------------------------------------ | --------------------------------------------------------------------------------------- | --------------------------------------- |
| Herramientas de edición                          | Atributos y geometría                                                                   | SHP/DBF en disco, inmediatamente        |
| Guardar mapa                                     | Estilos, capas visibles, encuadre                                                       | Archivo `.qgz`                          |
| Exportar proyecto (Gestor de proyectos → Export) | SHP/DBF de la red, `.qgz` y, opcionalmente, grupos de contenido y datos complementarios | Archivo `.zip` en la carpeta que elijas |
