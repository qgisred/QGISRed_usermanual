# Demands and Scenarios

The three tools in the second group of the Tools bar manage mass demand assignment, simulation scenarios, and identification of operational isolation segments.

---

## Nodal demand builder…

**Tools Bar → Nodal demand builder…**

Assign consumption to network nodes in bulk from external SHP layers loaded in QGIS. It is the main tool for integrating billing data, user censuses or polygon estimates into the EPANET model.

<figure><img src="../assets/images/herramientas/demand-builder.png" alt="Nodal demand builder dialog with source and assignment method options"><figcaption><p>Nodal demand builder dialog with source and assignment method options</p></figcaption></figure>
*Nodal demand builder: automatically detected source layers, field configuration and distribution method.*

### Supported data sources

| Geometry type | Assignment method |
|-------------------|----------------------|
| **Points** | Each point is assigned to the nearest node. The demand value is read from a configurable field in the layer. |
| **Polygons** | The total demand of the polygon is distributed among all the nodes that fall within it. |
| **Lines** | The demand for each section is distributed among the closest nodes along the axis. |

### Process

1. Load the external SHP layer with the consumption data into QGIS before opening the manager.
2. Activate **Nodal demand builder**. The dialog automatically detects and lists external layers.
3. Set for each layer:
- **Demand field**: column with the consumption value.
- **Category field**: to create multiple requests by type of user (residential, industrial, etc.).
- **Pattern field**: ID of the demand pattern to apply (optional).
4. Optionally select nodes on the map to limit the assignment to that area.
5. Confirm. QGISRed writes the values ​​to `Junctions` or `{Red}_MultipleDemands.shp` if there are categories.

### Restriction to selected candidates

The dialog offers two constraint options that can be combined:

| Option | Effect |
|--------|--------|
| **Restrict demand candidates to selected** | Only **nodes (Junctions) currently selected** on the map are considered as candidates to receive demand. The other nodes are ignored even if they fall within the influence zone of a consumption point. |
| **Restrict service connection candidates to selected** | Only currently selected Service Connections on the map are considered candidate service points. Useful for reallocating demand to specific connections without affecting the rest. |

Both options are independent and can be activated simultaneously.

### Custom Demand Units

By default, the Builder interprets demand values ​​in the project's flow units. If your source data uses different units, turn on **Custom demand units** and enter:

- **Units label**: descriptive label of the source units (e.g., `m³/mes`).
- **Conversion factor**: multiplier factor to convert to project units (e.g., if the project uses L/s and the data comes in m³/month: `1000 / 86400 / 30 ≈ 0.000386`).

The Builder automatically applies the factor to all consumption values ​​before assigning them to the nodes.

### Result on the map

The resulting layer is displayed with colors per category and labels with the demand value. Nodes with no assigned category appear in orange under the **Uncategorized** group.

> 💡 The auxiliary layers of the Demand Builder (ConsumptionPoints, DemandLinks, Sectors...) can also be created empty from the Layer Manager, without the need to first run an analysis (see [Overview and layer management](../active-project/capas-y-leyenda.md)).

### Lawsuit Cleanup

The manager allows you to delete existing demands before assigning new ones:
- **Delete demands from selected nodes**: eliminates values ​​of `Demand` and entries of `MultipleDemands`.
- **Delete orphan patterns**: delete patterns that are no longer referenced by any nodes.

### Demand assignment from segment layer

When a segment layer (line geometry) is used to distribute demands using the `%Dem` field, records without that field filled in automatically receive the remaining percentage up to 100%, distributed proportionally between them.

### Patterns by sectors

The sector patterns section allows you to assign a demand pattern to each sector of the network. It has **two exclusive modes**:

| Mode | Description |
|------|-------------|
| **Import patterns from a sector theme** | Select the polygon layer with the sectors from a drop-down combo that lists the polygon layers already loaded in QGIS (or import it with the `...` button if it is not already loaded). Then choose the **Sector Id (optional)**, **Id demand pattern** and **Priority (optional)** fields from the corresponding combos. The Sector Id field is optional: if not identified, QGISRed generates internal identifiers automatically. Optionally, save the result as an internal layer of the project with the **Import and save** button. Once saved, this option is locked. |
| **Use patterns from a project sector theme** | Select a slice layer already loaded in the project. A list is displayed with the sectors and, next to each one, an **editable** combo to choose the pattern: you can select an existing pattern from the list or directly write the Id of a new pattern. Nodes without a sector are grouped into an extra sector. |

### Efficiency by sectors

The hydraulic efficiency section by sectors also presents **two exclusive modes**:

| Mode | Description |
|------|-------------|
| **Import efficiencies from a sector theme** | Select the polygon layer with the sectors from a drop-down combo that lists the polygon layers already loaded in QGIS (or import it with the `...` button), and choose the **Sector Id (optional)**, **Efficiency** and **Priority (optional)** fields. The Sector ID field is optional. Optionally, save the result as an internal layer of the project with the **Import and save** button. Once saved, the import option is blocked. |
| **Use efficiencies from a project sector theme** | Select an existing slice layer; The plugin automatically identifies efficiency fields. |

#### Efficiency and pattern fixes

After defining the efficiencies by sectors, the manager offers additional correction options:

- **Correct category efficiencies to meet sector efficiency**: proportionally adjusts the efficiencies of each demand category so that the resulting efficiency in each sector matches the stated objective. Exclusive with the correction towards global efficiency.
- **Correct sector patterns to comply with the global pattern**: after assigning sector patterns, correct these patterns so that their combination complies with the previously declared global pattern. Remediation options are broken down by pattern scope (global or category).

### Layer of isolated connections with demand

When executing the analysis of isolated segments or hydraulic sectors, the plugin generates an additional layer with **connections that have assigned demand but belong to isolated hydraulic sectors** (without supply). This layer is represented by red outlined circular markers and includes the fields `Id`, `BaseDemand`, and `Category`.

---

## Scenario builder…

**Tools bar → Scenario builder…**

Bulk export and import model parameters, creating “snapshots” of the network state that can be restored at any time. It is the tool to manage model variants without duplicating projects.

### Parameters managed

| Parameter | Description |
|-----------|-------------|
| **Roughness** | Roughness coefficients of all pipes |
| **InitStatus** | Open/close states of pipes and valves |
| **Demands** | Base demands of all nodes |
| **InitQuality** | Initial qualities of nodes and pipes |
| **Elevations** | Levels of nodes, tanks and reservoirs |

### Typical workflow

1. Build the model in the current state (base year).
2. Export the base scenario with **Scenario builder → Export**.
3. Modify the model for the future horizon (new demands, aging pipes, etc.).
4. Export the future scenario with another name.
5. To compare or restore, use **Scenario builder → Import** and select the desired scenario.

The scenario files are saved as CSV in the project folder.

---

## Isolated segments…

**Tools Bar → Isolated segments…**

Answers the operational question: **"What valves should I close to repair this pipeline, and which users will be left without service?"**

<figure><img src="../assets/images/herramientas/isolated-segments.png" alt="Result of Isolated segments: affected pipe, shut-off valves and zone without service"><figcaption><p>Result of Isolated segments: affected pipe, shut-off valves and zone without service</p></figcaption></figure>
*In red the pipe to be repaired, in yellow the valves to close and in blue the area without service.*

### Process

1. Activate the tool and click on the pipe to be repaired or isolated.
2. QGISRed calculates the **minimum segment** that would be isolated when closing the closest manual valves and identifies the affected collaterals.
3. The result is displayed on the map:
- **Target pipe**: in red.
- **Valves to close**: in yellow.
- **Zone without service** (collateral affected people): in blue.
4. You can click on more pipes within the same session to accumulate the analysis.

The auxiliary layer `IsolatedSegments` is generated with all the information. Does not modify the model.
