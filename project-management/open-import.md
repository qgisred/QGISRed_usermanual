# Open and Import Projects

QGISRed offers three ways to start working with an existing network:

| Option | When to use it |
|--------|---------------|
| **Open project** | The project has already been created with QGISRed and its SHP files are on disk |
| **Import project** | You have an EPANET `.inp` file, external SHPs without QGISRed structure, or a ZIP previously exported with QGISRed |
| **Add data by import** | You already have an open project and want to incorporate additional data |

---

## Open project

**General Bar → Open project**

Opens an existing QGISRed project (previously created with the plugin) that does not appear in the Project Manager, or that was moved from a folder.

<figure><img src="../assets/images/general/abrir-proyecto.png" alt="Project opening dialog"><figcaption><p>Project opening dialog</p></figcaption></figure>
*Opening dialog: enter the network name and select the folder.*

### Process

1. Enter the **network name** exactly as it appears in the SHP files prefix (without extension).
2. Select the **folder** where the files are.
3. QGISRed verifies that `{nombre}_Pipes.shp` exists in that folder and loads all the project layers.

### What happens when you open

- The layer group **Inputs** is loaded with the 6 base SHPs plus any auxiliary layers (multiple requests, sources, etc.).
- If the project has results from previous simulations, the **Results** group is also loaded.
- The project options (`_Options.dbf`) are read and the units indicator in the main bar is updated.
- If the visual styles (QML) have changed with respect to the version of the plugin with which it was saved, they are automatically updated.

> 💡 The quickest way to open a known project is to **double click** on the [Project manager](project-manager.md). The "Open Project" option is for projects that do not appear in that list.

---

## Import project

**General Bar → Import project**

Convert external data into a QGISRed project, or recover a previously exported one. Supports three input formats:

### Import from EPANET (`.inp`) {#import-from-epanet}

The most common case: you have an existing EPANET model and you want to work with it in QGISRed.

<figure><img src="../assets/images/general/importar-inp.png" alt="EPANET INP File Import Dialog"><figcaption><p>EPANET INP File Import Dialog</p></figcaption></figure>
*Import dialog: selection of .inp file, network name and destination folder.*

1. Select the file `.inp`.
2. Indicates the **name of the network** that the QGISRed project will have (it may be different from the internal name of the INP).
3. Choose the **destination folder** where the SHPs will be created.
4. QGISRed converts all elements (nodes, pipes, valves, pumps, curves, patterns, controls...) to the SHP+DBF structure.

> ⚠️ The coordinates of `.inp` must be in the same CRS that you will use in QGISRed. The plugin does not reproject during import.

**What is imported:**
- All network elements (junctions, pipes, tanks, reservoirs, valves, pumps)
- Curves (H-Q, efficiency, volume, pressure loss)
- Demand patterns
- Simple controls and rules
- Simulation options (units, formula, times, energy, quality)
- Multiple demands per node


### Import from external SHPs

If you have SHP layers with the geometry of the network but without the internal structure of QGISRed, the importer allows you to map the attribute columns of each layer to the fields expected by the plugin.

For each element type you can select the corresponding SHP layer and assign its fields to the model attributes. Automatically recognized fields (if the name matches) are preselected:

**Pipes** — mappable fields: ID, Length, Diameter, Roughness, Minor loss coeff., **Material**, Installation date, Initial status, Bulk reaction coeff., Wall reaction coeff., Tag, Description.

**Services** — mappable fields: ID, Length, Diameter, Roughness, **Material**, Base demand, Pattern, Active, Installation date, Tag, Description.

> If the connection layer is **points** (each connection is hooked to the nearest main pipe, instead of already having its own layout), two optional restrictions appear to decide which pipes each connection can be hooked to — combinable with each other:
> - **Only pipes with diameters below this value are candidates** (in the project diameter units).
> - **Only pipes currently selected in the Pipes layer are candidates** — only available if you already have pipes selected in the map before opening the importer; The box shows how many are selected.
>
> A connection that does not find any candidate pipes within those constraints is not imported, and QGISRed indicates this in the import summary.

The other elements (valves, pumps, tanks, reservoirs, nodes, isolation valves, meters) have their own sets of mappable fields.

When the import creates a new project, the **materials catalog** (same as when creating a project from scratch) and basic EPANET parameters (units and pressure drop formula) are also requested. If imported over an existing project, these parameters are ignored.

> 💡 The **Material** field of pipes and connections is crossed with the project's materials catalog to automatically estimate the roughness based on the age of the pipe.

### Import an exported QGISRed project (ZIP) {#import-zip}

Retrieves a project packaged with the **Export** button from [Project manager](project-manager.md) — see [Save, export and close project](../active-project/save-export-close.md). It also recognizes ZIPs generated by previous versions of the plugin, even if they do not have the internal manifest of the current exports.

<figure><img src="../assets/images/general/importar-proyecto-qgisred.png" alt="QGISRed project tab of the import dialog"><figcaption><p>QGISRed project tab of the import dialog</p></figcaption></figure>

1. In the **QGISRed project** tab, press the **...** button next to **ZIP file:** and select the `.zip` file.
2. QGISRed inspects the ZIP content without extracting it yet and displays a summary under the field:
- **Project:** name of the network containing the ZIP (replaces any name you entered before; the project name field is hidden in this tab).
- If the ZIP includes the QGIS map, indicate the file `.qgz`/`.qgs`; If it is not included, it warns that only the data will be imported.
- If the ZIP includes complementary data (background cartography, MDT, etc.), indicate how many elements and their total size.
3. If the ZIP includes complementary data, the **Import the complementary data included in the ZIP file** box appears, checked by default. Uncheck it if you don't want to bring them.
4. The **Automatically create a subfolder for this project** checkbox decides whether the project is placed in a subfolder with the network name within the destination folder:
- If the ZIP already contains its own project folder (it was exported along with supporting data in sister folders), QGISRed automatically unchecks and disables this box — nesting it in another folder would break the relative paths to that data.
- Otherwise, you can freely check or uncheck it.
5. Press **Import From Project**.

If the ZIP is not a valid QGISRed project, QGISRed indicates this without actually importing anything:

| Situation | Message |
|-----------|---------|
| The ZIP does not contain a recognizable QGISRed project | _"ZIP file does not contain a valid QGISRed project"_ |
| The ZIP was generated with a newer version of QGISRed than the one installed | _"This ZIP file was created with a newer version of QGISRed. Please update the plugin."_ |
| The ZIP contains unsafe file paths | _"The ZIP file contains unsafe file paths and will not be imported."_ |

> ⚠️ If a project with the same name (or files with the same name) already exists in the destination folder, QGISRed asks for confirmation before overwriting them.

> 💡 If the ZIP includes the QGIS map but you decide not to import the complementary data, QGISRed warns that some background layers will not be available and lets QGIS ask you to locate them.

---

## Add data by import

**Project bar → Add data by import**

Available only when there is a project already open. It allows you to enrich the project with additional data without closing what is loaded.

Typical use cases:
- Incorporate a new network zone designed in a separate `.inp`.
- Add demands for a new database.
- Integrate data from a sector imported from another system.

The process is the same as importing, but the imported items are **added** to the existing project instead of creating a new one. QGISRed verifies that there are no ID conflicts before incorporating the data.

---

## Considerations when changing equipment

If you copy the project folder to another computer:

1. Use **Upload** in Project Manager to add it to local history.
2. If the project has a `.qgz` saved, open it from QGIS normally — QGISRed will recognize it automatically.
3. If the `.qgz` is not there or the paths have changed, use **Open Project** to load it from the SHPs directly.
