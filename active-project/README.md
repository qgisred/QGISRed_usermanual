# 📋 Project

The **Project** bar groups the administration tools of the project that is already open in QGISRed. All of your buttons require a valid project loaded; If there are none, the plugin will warn with the message _"No valid project is opened"_.

<figure><img src="../assets/images/proyecto/barra-project.png" alt="QGISRed Project toolbar with its nine buttons"><figcaption><p>QGISRed Project toolbar with its nine buttons</p></figcaption></figure>
*Project Bar: active project management tools.*

<!-- TODO: screenshot outdated after removal of "Project backup" button (commit 7b2415f) -->

---

## Project bar buttons

| # | Tool | Function |
|---|-------------|---------|
| 1 | **Summary** | Number of elements of each type in the network |
| 2 | **Add data by import** | Import additional elements to the open project |
| 3 | **Layer Manager** | Control layer visibility and recover deleted layers |
| 4 | **Legend Editor** | Customize the symbology of the layers |
| — | *(separator)* | |
| 5 | **Project Options** | EPANET parameters: units, formula, quality, times, energy |
| 6 | **Default values** | ID Prefixes, Tolerances and Initial Hydraulic Values ​​|
| 7 | **Table of materials** | Roughness and aging rates by material |
| — | *(separator)* | |
| 8 | **Save map** | Save the QGIS file `.qgz` |
| 9 | **Close project** | Close the project and clear the QGIS session |

> 💡 The old **Backup** button (_Project backup_) has been removed from this bar with no direct replacement. To export the project to a portable ZIP, use the **Export** button on [Project manager](../project-management/project-manager.md) — see [Save, export and close project](save-export-close.md).

## In this section

* [Overview and layer management](layers-and-legend.md) — layer visibility, recovery and legend
* [Project Settings](project-configuration.md) — EPANET options, default values, materials
* [Save, export and close project](save-export-close.md) — save map, export to ZIP and close
