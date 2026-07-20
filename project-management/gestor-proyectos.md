# Project Manager

**General Bar → Project Manager** (or from the QGISRed menu → General → Project manager)

The Project Manager is the central administration window of QGISRed. Allows access to all known projects without having to remember where they are stored.

<figure><img src="../assets/images/general/gestor-proyectos.png" alt="QGISRed Project Manager Window"><figcaption><p>QGISRed Project Manager Window</p></figcaption></figure>
*Project Manager window: list of recent projects and available operations.*

---

## List of recent projects

The window shows all projects that have ever been opened on this computer. For each project the **network name** and **folder path** are displayed.

- **Double click** on any project → opens it directly.
- If there is an open project with unsaved changes, QGISRed will ask for confirmation before closing it.

## Available operations

### Load (Load)

Allows you to add a project that does not appear in the history to the list (for example, if the project was created on another computer and the folder was copied).

1. Press **Load**.
2. Enter the **network name** (no extension, no folder prefix).
3. Select the **project folder** with the explorer.
4. QGISRed will verify that the file `{nombre}_Pipes.shp` exists in that folder before opening it.

### Clone

Create a complete copy of the project under a different name. Useful for creating variants without losing the original.

1. Select the project you want to clone.
2. Press **Clone**.
3. Enter the new network name.
4. Choose the destination folder (it can be the same folder if the name is different).

> 💡 Cloning copies all SHP, DBF files and metadata. Simulation results are **not** cloned to save space.

### Rename

Renames the network and automatically updates the name of **all files** in the project (SHP, DBF, PRJ, etc.). It is not a simple name change in the list: it moves and renames the files on disk.

1. Select the project.
2. Press **Rename**.
3. Enter the new name.

> ⚠️ If you have the project open in QGIS, close it before renaming it to prevent QGIS from maintaining locks on the files.

### Delete from list (Unload)

Removes the project from recent history **without deleting files on disk**. The project still exists in your folder and can be added back with **Upload**.

### Delete from disk (Delete)

Delete the project from history **and delete all project files** from disk. This operation is irreversible.

> ❗ QGISRed will ask for confirmation before deleting. Make sure you have a backup if you need to recover the project in the future.

### Open folder

Open Windows Explorer directly to the selected project folder.

---

## How QGISRed identifies the active project

When you open QGIS with a `.qgz` project already saved, QGISRed automatically recognizes the active network by searching the loaded layers for which one corresponds to `_Pipes.shp` and has the internal property `qgisred_identifier`.

If the piping layer is loaded but does not have that identifier (for example, because it was added manually without going through QGISRed), the plugin will warn with the message:

> _"Please, open the project from the QGISRed Project Manager"_

In that case, close the layers and use the Project Manager to open the project correctly.
