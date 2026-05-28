# Guardar y Copia de Seguridad

---

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

---

## Copia de seguridad

**Barra Project → Copia de seguridad** (Project backup)

Crea una copia completa de todos los archivos SHP, DBF y metadatos del proyecto en una subcarpeta con la fecha y hora actuales.

### Dónde se guarda

```
{CarpetaProyecto}/Backups/{NombreRed}_{YYYYMMDD_HHMMSS}/
```

Por ejemplo:
```
RedUrbana/Backups/RedUrbana_20241215_143022/
    RedUrbana_Junctions.shp
    RedUrbana_Pipes.shp
    RedUrbana_Options.dbf
    ...
```

Al finalizar, QGISRed muestra en la barra de mensajes la ruta completa de la copia creada.

### Qué se incluye en el backup

- Todos los archivos SHP+DBF+PRJ de la carpeta principal del proyecto
- Los archivos de opciones y metadatos (`_Options.dbf`, `_Title.dbf`)
- Las subcarpetas de datos auxiliares (Demands Builder, etc.)

### Qué no se incluye

- La carpeta `Results/` (los resultados de simulación pueden ser muy grandes y se pueden regenerar ejecutando de nuevo la simulación)
- La carpeta `Issues/` (se regenera al volver a ejecutar las verificaciones)
- El archivo `.qgz` (guárdalo manualmente con _Guardar mapa_ si quieres incluirlo)

> 💡 **Buenas prácticas**: realiza una copia de seguridad antes de operaciones que modifiquen muchos elementos a la vez (importaciones masivas, cambios de CRS, conversiones de rugosidad). También es recomendable antes de actualizar la versión del plugin.

---

## Cerrar proyecto

**Barra Project → Cerrar proyecto** (Close project)

Cierra el proyecto actual de QGISRed y limpia la sesión de QGIS: elimina todas las capas cargadas y restablece el estado inicial.

Es equivalente a usar _Proyecto → Nuevo_ en el menú de QGIS.

> ⚠️ Si hay cambios no guardados en el archivo `.qgz`, QGIS preguntará si deseas guardarlos antes de cerrar.

---

## Resumen: qué guarda cada opción

| Operación | Qué guarda | Dónde |
|-----------|-----------|-------|
| Herramientas de edición | Atributos y geometría | SHP/DBF en disco, inmediatamente |
| Guardar mapa | Estilos, capas visibles, encuadre | Archivo `.qgz` |
| Copia de seguridad | Todos los SHP/DBF del proyecto | Subcarpeta `Backups/` |
