# Demand Sector Builder

**Tools Bar → Demand Sector Builder…**

The **Demand Sector Builder** is a modal dialog that allows you to create and manage multiple **named sectorizations** of the network

<figure><img src="../assets/images/herramientas/constructor-sectores.png" alt="Demand Sector Builder dialog with list of sectorizations and topic settings"><figcaption><p>Demand Sector Builder dialog with list of sectorizations and topic settings</p></figcaption></figure>
*Demand Sector Builder: list of sectorizations (left panel), detection parameters and topics to generate (right panel).*, each with its own demand sectors. Each sectorization groups the nodes of the network into zones according to the topology and limits defined by the user, and generates the necessary auxiliary layers for use in the Nodal Demand Builder or for water balance analysis.

---

## Key concepts

| Concept | Description |
|----------|-------------|
| **Sectorization** | Named set of sectors that covers the entire network. There can be multiple sectorizations in the same project. |
| **Sector** | Subset of nodes and links delimited by boundaries. Each node belongs to exactly one sector within a sectorization. |
| **Theme** | Type of geometric layer that represents the sectors. The Builder can generate up to 6 topic types for each sectorization. |
| **Border** | Element or set of elements that delimits two adjacent sectors (border pipes, valves, flowmeters). |

---

## Create and manage sectorizations

### List of sectorizations

The left pane of the dialog shows all the project slices. Each entry has:
- Editable name.
- Add (＋) and Delete (✕) buttons.

### Add a sectorization

1. Press **＋** in the list of sectors.
2. Enter a friendly name (e.g., `Sectorizacion_2024`, `Zonas_Presion`).
3. Configure the detection parameters and the topics to generate.
4. Press **Build** to run the analysis.

Sectorizations are stored in the project's auxiliary layers under the group **Auxiliary Layers > DemandSectors**.

---

## Sector detection

The Builder detects the sectors using a **BFS** (breadth search) algorithm that runs through the network topology starting from the marked border elements.

### Border types

| Type | Description |
|------|-------------|
| **Pipes** | Pipes marked as border; the flow through them delimits sectors |
| **Isolation Valves** | Isolation valves in the network |
| **Meters** | Flowmeters (delimit water balance sectors) |

The selection of which type of element acts as a border is configured using checkboxes in the dialog. Multiple types can be activated simultaneously.

### Geometric tolerance

The Builder uses a tolerance of **0.01 map units** to verify geometric agreement between nodes and boundary elements. Nodes that do not exactly match the network but are within this range are considered connected.

---

## Topics generated

For each sectorization, the Builder can generate up to **6 topic types**:

| Theme | Geometry | Description |
|------|-----------|-------------|
| **Frontiers** | Lines | Border elements between adjacent sectors |
| **Links** | Lines | Pipes and internal links of each sector |
| **Nodes** | Points | Network nodes with the `SectorId` field assigned |
| **Polygons** | Polygons | Convex geometric envelope of each sector |
| **MultiLinks** | Multiline | All links in a sector merged into a single geometry per sector |
| **MultiNodes** | Multipoint | All nodes of a sector merged into a single geometry per sector |

The themes to be generated are selected individually with checkboxes before clicking **Build**. At least one topic must be active.

---

## Integrity validations

Before generating the sectors, the Builder runs **7 integrity checks**:

1. The network has at least one node.
2. There are border elements of the selected type.
3. There are no isolated nodes (no connectivity).
4. The border elements have the necessary fields assigned.
5. There are no empty sectors (no nodes).
6. Each node belongs to exactly one sector.
7. The generated polygons do not overlap.

If any validation fails, the dialog displays a descriptive error message and does not generate the layers.

---

## Result in the project

The layers for each sectorization are created within the **Auxiliary Layers > DemandSectors > [sectorization name]** group in the QGIS layers panel. Each Nodes type layer includes the `SectorId` field that can be used directly in the **Nodal Demand Builder** to assign patterns or efficiencies by sector.

### Use in Nodal Demand Builder

A sectorization generated with the Demand Sector Builder can be selected in the Nodal Demand Builder using the **"Use project sectors theme"** option, avoiding the need to import an external SHP. See [Demands and scenarios](demandas-escenarios.md) for more details.

---

## Typical workflow

1. **Define borders**: in the Pipes (or Meters) layer, mark as a border the elements that delimit the sectors (field `IsFrontier` or equivalent, or by selection).
2. **Open the Builder**: Tools → Demand Sector Builder.
3. **Create sectorization**: press ＋, name it and select the topics to generate.
4. **Run**: Press **Build**. The layers appear in Auxiliary Layers > DemandSectors.
5. **Use in Nodal Demand Builder**: In the sector patterns or efficiencies section, choose the new sectorization as the project theme.
