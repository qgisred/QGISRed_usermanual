# 🗂️ Gestión de Proyectos

Las barras **General** y **Project** cubren todo el ciclo de vida de un proyecto QGISRed: crearlo, abrirlo, configurarlo y mantenerlo.

![Barra de herramientas General y Project de QGISRed](../assets/images/image14.png)
*Barras General (izquierda) y Project (derecha) de QGISRed.*

---

## Estructura de un proyecto QGISRed

Un proyecto QGISRed es una **carpeta** que contiene un conjunto de archivos con el mismo prefijo (el nombre de la red). Por ejemplo, para una red llamada `RedUrbana`:

```
RedUrbana/
├── RedUrbana_Junctions.shp/.dbf/.shx/.prj
├── RedUrbana_Pipes.shp/.dbf/.shx/.prj
├── RedUrbana_Tanks.shp/.dbf/.shx/.prj
├── RedUrbana_Reservoirs.shp/.dbf/.shx/.prj
├── RedUrbana_Valves.shp/.dbf/.shx/.prj
├── RedUrbana_Pumps.shp/.dbf/.shx/.prj
├── RedUrbana_Options.dbf
├── RedUrbana_Title.dbf
├── Issues/
├── Queries/
└── Results/
```

> ⚠️ **IMPORTANTE**: Nunca muevas, renombres o borres manualmente estos archivos desde el explorador de Windows. Usa siempre las herramientas de QGISRed (Renombrar, Borrar del Gestor de proyectos) para garantizar la coherencia del conjunto.

## En esta sección

* [Gestor de proyectos](gestor-proyectos.md) — historial, clonar, renombrar
* [Crear proyecto](crear-proyecto.md) — proyecto nuevo desde cero
* [Abrir e importar](abrir-importar.md) — abrir existente o importar desde `.inp`
* [Gestor de capas y leyenda](capas-y-leyenda.md) — visibilidad, recuperación y simbología
* [Configuración del proyecto](configuracion.md) — opciones EPANET, valores por defecto, materiales
* [Guardar y copia de seguridad](guardar-backup.md) — guardar el mapa, backup y cierre
