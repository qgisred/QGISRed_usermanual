# Element Explorer

The **Element Explorer** is a floating panel (dock) that QGISRed maintains as a single instance. It groups two related functionalities into separate tabs: searching for elements by ID and viewing the properties of the selected element on the map.

<figure><img src="../assets/images/consultas/element-explorer.png" alt="Element Explorer panel with the two tabs Find Elements and Properties"><figcaption><p>Element Explorer panel with the two tabs Find Elements and Properties</p></figcaption></figure>
*Element Explorer panel: Find Elements tab (left) and Properties tab (right).*

The **Find elements by ID** and **Element properties** buttons in the Queries bar open this same panel and activate the corresponding tab. Switching tabs within the panel does not close any functionality.

---

## Find Elements Tab — Search by ID

**Queries Bar → Find elements by ID…**

Locates any element on the network by writing its ID and highlights it on the map.

### Searchable items

- Pipes, Junctions, Demands, Reservoirs, Tanks, Pumps, Valves, Sources

### Process

1. Activate **Find elements by ID**. The panel opens or is brought to the front.
2. Select the element type from the layer dropdown.
3. Type the ID in the text field and press **Find** or Enter.
4. QGISRed centers the map on the element and highlights it. The result appears on the panel with a light yellow background.

### Multiple search

Separate multiple IDs with a comma or semicolon to highlight them all simultaneously.

### If the ID does not exist

The panel displays a warning and the map does not change.

---

## Properties tab — Element properties

**Queries bar → Element properties…**

Activates an interactive identification tool: when you click on any element on the map, the panel shows all its attributes in the Properties tab.

### Process

1. Activate **Element properties**. The cursor changes to identification mode.
2. Click on any element on the network.
3. The panel shows the fields of the clicked element. You can continue clicking on other elements without deactivating the tool.

### Information displayed

Attributes are organized by element type. For a typical **pipe**:

| Field | Description |
|-------|-------------|
| `Id` | Unique identifier |
| `Length` | Length (m) |
| `Diameter` | Diameter (mm) |
| `Roughness` | Roughness coefficient |
| `Material` | Materials |
| `InstallYear` | Year of installation |
| `Status` | Status (Open / Closed / CV) |
| `Tag` | Free label |

For **nodes** `Elevation`, `Demand`, `Pattern`, `InitQuality`, etc. are shown. Each item type has its own set of fields.

If the project has simulation results loaded, the panel adds a section with the calculated values ​​(pressure, flow, velocity...) for the active period in the results viewer. The simulated time is indicated by the prefix **Time:** followed by the bold value in the format `HH:MM:SS`.

> ⚠️ **Conditional quality fields.** The `Quality` field only appears when the project quality model is not *None*. The `ReactRate` field is only visible when the quality model is *Chemical*; remains hidden for *None*, *Age* and *Trace* models. These fields are only displayed when the project's quality model supports them.

### Usage Notes

- Deactivating the button returns the cursor to the standard QGIS navigation mode.
- If you click in an area without elements, the panel retains the last selection.
- The background of the panel has a light yellow tint to differentiate it from the rest of QGIS panels.
- Clicks on layers that do not belong to the active QGISRed project (background layers, external auxiliary layers, etc.) are ignored: the panel does not update its content.

### ID field resolution per layer

QGISRed automatically resolves the **identifier field name** of each network layer using the internal function `getIdFieldName(layer)`. This allows the plugin to correctly detect the ID on layers with different naming conventions:

| Layer type | Typical ID field |
|--------------|-----------------|
| Pipes | `PipeID` |
| Junctions | `JunctionID` |
| Tanks | `TankID` |
| Reservoirs | `ReservoirID` |
| Pumps | `PumpID` |
| Valves | `ValveID` |

If your project uses custom naming conventions, automatic resolution prevents search or identification errors. There is no need to configure anything manually: the scanner detects the correct field when activated on any layer of the network.

### Additional field aliases automatically recognized

The panel automatically recognizes the following field aliases and presents them with correct labels, units, and decimals without any additional configuration:

| Alias ​​| Description |
|-------|-------------|
| `DemPattID` | Demand pattern in nodes; is suppressed when multiple requests are active and is grouped correctly |
| `HedPattID` | Pump height curve pattern |
| `QualPattID` | Quality pattern in fonts |
| `NodeID` | Node identifier in derived layers |
| `NodeType` | Node type |
| `LinkID` | Link identifier in derived layers |
| `LinkType` | Link type |

> ℹ️ Recognition is automatic: the browser detects the correct alias when activated on any layer of the network, without the need to configure anything manually.
