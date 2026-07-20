# Create Project

**General Bar → Create project** (or QGISRed menu → General → Create project)

Create a completely new QGISRed project from scratch, generating the SHP file structure necessary to define a distribution network.

<figure><img src="../assets/images/general/crear-proyecto.png" alt="New project creation dialog"><figcaption><p>New project creation dialog</p></figcaption></figure>
*Project creation dialog: name, folder and reference system.*

---

## Step by step

### 1. Network name

Enter a short name without spaces or special characters (letters, numbers, and underscores are safe). This name will be the **prefix** of all files in the project.

- ✅ Correct: `RedUrbana`, `Red_Norte_2024`, `SectorA`
- ❌ Avoid: `Red Urbana`, `Réseau_Côte`, `Red/Norte`

### 2. Project folder

Select or create the folder where all files will be saved. **Several projects can coexist in the same folder** as long as they have different names.

### 3. Coordinate Reference System (CRS)

Select the appropriate CRS for your work area. QGISRed will assign it to all SHP files in the project.

> 💡 If you are going to import geometry from other sources (orthophoto, cadastre, etc.), use the same CRS as those sources or the most common one in your country to avoid reprojections.

### 4. EPANET Initial Options

In the same dialog you can configure the basic parameters of the model:

| Parameter | Description |
|-----------|-------------|
| **Flow units** | LPS (liters/second), GPM, CMH, etc. Determines if the project works in the SI or US system |
| **Head loss formula** | Darcy-Weisbach (D-W), Hazen-Williams (H-W) or Chezy-Manning (C-M) |

These parameters can be changed later from _Project Options_, but it is recommended to set them from the beginning because they affect which units are displayed in all network properties.

### 5. Materials catalog

Select the **materials catalog** that will be used in the project. This catalog is a `.dbf` file that defines the available pipe materials (name, initial roughness coefficient, and aging increment).

QGISRed looks for the catalogs available in the `materials` and `global_defaults` folders of `%APPDATA%\QGISRed\`. If there is no catalog installed, the dropdown will appear empty and the project will be created without predefined materials.

> The materials catalog is used to automatically estimate the roughness of pipes based on their material and age, making it easy to calibrate the hydraulic model.

---

## Generated files

Upon confirming the creation, QGISRed generates the following files in the chosen folder and automatically uploads them to QGIS:

| Archive | Content |
|---------|-----------|
| `{Red}_Junctions.shp` | Demand nodes |
| `{Red}_Pipes.shp` | Pipes |
| `{Red}_Tanks.shp` | Deposits |
| `{Red}_Reservoirs.shp` | Reservoirs or feeding points |
| `{Red}_Valves.shp` | Regulating valves |
| `{Red}_Pumps.shp` | Bombs |
| `{Red}_Options.dbf` | EPANET options (units, formula, quality...) |
| `{Red}_Title.dbf` | Project metadata (scenario name, notes…) |

They are all grouped together in the QGIS legend under a group called **"{Red}" → "Inputs"**.

---

## What to do next

Once the project is created, the next step is to **build the network** using the **Edition** bar. See section [Editing and Modeling](../editing/README.md) to see how to add pipes, nodes, and special elements.

> 💡 If you already have an EPANET `.inp` file, it's faster to use [Import project](abrir-importar.md#importar-desde-epanet) than creating from scratch.
