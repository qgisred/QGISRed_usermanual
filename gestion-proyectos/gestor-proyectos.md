# Gestor de proyectos

**Barra General → Gestor de proyectos** (o desde el menú QGISRed → General → Project manager)

El Gestor de proyectos es la ventana central de administración de QGISRed. Permite acceder a todos los proyectos conocidos sin necesidad de recordar dónde están almacenados.

\*Ventana del Gestor de proyectos: lista de proyectos recientes y operaciones disponibles.\*

***

## Lista de proyectos recientes

La ventana muestra todos los proyectos que han sido abiertos alguna vez en este equipo. Para cada proyecto se muestra el **nombre de la red** y la **ruta de la carpeta**.

* **Doble clic** sobre cualquier proyecto → lo abre directamente.
* Si hay un proyecto abierto con cambios sin guardar, QGISRed pedirá confirmación antes de cerrarlo.

## Operaciones disponibles

### Cargar (Load)

Permite añadir a la lista un proyecto que no aparece en el historial (por ejemplo, si el proyecto se creó en otro equipo y se ha copiado la carpeta).

1. Pulsa **Cargar**.
2. Introduce el **nombre de la red** (sin extensión, sin el prefijo de carpeta).
3. Selecciona la **carpeta del proyecto** con el explorador.
4. QGISRed verificará que existe el archivo `{nombre}_Pipes.shp` en esa carpeta antes de abrirlo.

### Clonar

Crea una copia completa del proyecto bajo un nombre diferente. Útil para crear variantes sin perder el original.

1. Selecciona el proyecto que quieres clonar.
2. Pulsa **Clonar**.
3. Introduce el nuevo nombre de la red.
4. Elige la carpeta destino (puede ser la misma carpeta si el nombre es distinto).

> 💡 La clonación copia todos los archivos SHP, DBF y los metadatos. Los resultados de simulación **no** se clonan para ahorrar espacio.

### Exportar

Empaqueta el proyecto seleccionado en un ZIP portable (SHP/DBF, `.qgz` y, opcionalmente, resultados, incidencias, consultas, capas auxiliares y datos complementarios). Es la única forma de exportar un proyecto: ya no existe un botón equivalente en la barra **Project**.

1. Selecciona el proyecto en la lista (no hace falta tenerlo abierto en QGIS).
2. Pulsa **Export**.
3. Completa el diálogo de exportación.

Ver el detalle completo del diálogo, qué se incluye y qué no, en [Guardar, exportar y cerrar proyecto](../proyecto-activo/guardar-backup.md#exportar-el-proyecto).

### Renombrar

Cambia el nombre de la red y actualiza automáticamente el nombre de **todos los archivos** del proyecto (SHP, DBF, PRJ, etc.). No es un simple cambio de nombre en la lista: mueve y renombra los ficheros en disco.

1. Selecciona el proyecto.
2. Pulsa **Renombrar**.
3. Introduce el nuevo nombre.

> ⚠️ Si tienes el proyecto abierto en QGIS, ciérralo antes de renombrarlo para evitar que QGIS mantenga bloqueos sobre los archivos.

### Borrar de la lista (Unload)

Elimina el proyecto del historial de recientes **sin borrar los archivos en disco**. El proyecto sigue existiendo en su carpeta y puede volver a añadirse con **Cargar**.

### Borrar del disco (Delete)

Elimina el proyecto del historial **y borra todos los archivos** del proyecto del disco. Esta operación es irreversible.

> ❗ QGISRed pedirá confirmación antes de borrar. Asegúrate de tener una copia de seguridad si necesitas recuperar el proyecto en el futuro.

### Abrir carpeta

Abre el explorador de Windows directamente en la carpeta del proyecto seleccionado.

***

## Cómo QGISRed identifica el proyecto activo

Cuando abres QGIS con un proyecto `.qgz` ya guardado, QGISRed reconoce automáticamente la red activa buscando en las capas cargadas cuál corresponde a `_Pipes.shp` y tiene la propiedad interna `qgisred_identifier`.

Si la capa de tuberías está cargada pero no tiene ese identificador (por ejemplo, porque se añadió manualmente sin pasar por QGISRed), el plugin avisará con el mensaje:

> _"Please, open the project from the QGISRed Project Manager"_

En ese caso, cierra las capas y usa el Gestor de proyectos para abrir el proyecto correctamente.
