# Open and Import Projects

QGISRed offers three ways to start working with an existing network:

| Option | When to use it |
|--------|---------------|
| **Open project** | The project has already been created with QGISRed and its SHP files are on disk |
| **Import project** | You have an EPANET `.inp` file or external SHPs without QGISRed structure |
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

> 💡 The quickest way to open a known project is to **double click** on the [Project manager](gestor-proyectos.md). The "Open Project" option is for projects that do not appear in that list.

---

## Import project

**General Bar → Import project**

Converts external data into a QGISRed project. Supports two input formats:

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

**Pipes** — mappable fields: ID, Length, Diameter, Roughness, Coeff. losses, **Material**, Installation date, Initial state, Coeff. mass reaction, Coef. wall reaction, Tag, Description.

**Services** — mappable fields: ID, Length, Diameter, Roughness, **Material**, Base demand, Pattern, Active, Installation date, Tag, Description.

The other elements (valves, pumps, tanks, reservoirs, nodes, isolation valves, meters) have their own sets of mappable fields.

When the import creates a new project, the **materials catalog** (same as when creating a project from scratch) and basic EPANET parameters (units and pressure drop formula) are also requested. If imported over an existing project, these parameters are ignored.

> 💡 The **Material** field of pipes and connections is crossed with the project's materials catalog to automatically estimate the roughness based on the age of the pipe.

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
