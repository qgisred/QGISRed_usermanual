# 🗂️ General

The **General** bar is the entry point to any work session with QGISRed. It contains the four actions to manage the life cycle of projects: create them, open them, import them and manage the history.

<figure><img src="../assets/images/general/barra-general.png" alt="QGISRed General Toolbar with its four buttons"><figcaption><p>QGISRed General Toolbar with its four buttons</p></figcaption></figure>
*General Bar: Project Manager, Open, Create and Import.*

---

## What is a QGISRed project

A QGISRed project is a **folder** containing a set of SHP and DBF files with the same prefix (the name of the network). For example, for a network named `RedUrbana`:

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

> ⚠️ Never move, rename or delete these files manually from Windows Explorer. Always use QGISRed tools to ensure consistency of the set.

## In this section

* [Project manager](project-manager.md) — history, clone, rename, delete
* [Create project](create-project.md) — new project from scratch
* [Open and import](open-import.md) — open existing or import from `.inp`
