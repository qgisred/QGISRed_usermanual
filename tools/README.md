# 🔧Tools

The **Tools** bar groups the massive processing tools: automatic calculation of hydraulic properties, assignment of demands from external sources, scenario management and topological analysis. Unlike the Edition tools, these act on the entire network or on large selections, not element by element.

<figure><img src="../assets/images/herramientas/barra-tools.png" alt="QGISRed Tools toolbar"><figcaption><p>QGISRed Tools toolbar</p></figcaption></figure>
*Tools bar: hydraulic properties, demands and scenarios, topological analysis.*

---

## Tools from the Tools bar

### Group 1 — Hydraulic properties

| # | Tool | Function |
|---|-------------|---------|
| 1 | **Automatically calculate pipe lengths** | Recalculate the length of each pipe from its geometry |
| 2 | **Interpolate elevation from .asc files…** | Assign heights to nodes by interpolating from an MDT in ASC format |
| 3 | **Set roughness coefficients (from Material and Date)** | Calculate the current roughness of each pipe due to aging |
| 4 | **Convert roughness coefficients…** | Convert roughness between H-W, D-W and C-M formulas |

### Group 2 — Demands and scenarios

| # | Tool | Function |
|---|-------------|---------|
| 5 | **Nodal demand builder…** | Assign demands to nodes from external SHP layers (points or polygons) |
| 6 | **Scenario builder…** | Export and import model parameters in bulk to manage scenarios |
| 7 | **Isolated segments…** | Identify which valves to close to isolate a section and which areas are left without service |

### Group 3 — Topological analysis

| # | Tool | Function |
|---|-------------|---------|
| 8 | **Obtain demand sectors** | Generates demand sectors delimited by flowmeters |
| 9 | **Minimum Cost Tree…** | Calculate the minimum cost tree from a selected node |

---

## In this section

* [Hydraulic properties](hydraulic-properties.md) — lengths, elevations, aging roughness and conversion between formulas
* [Demands and scenarios](demands-and-scenarios.md) — mass assignment of demands, management of scenarios and isolated segments
* [Demand sectors and tree](sectors-tree.md) — sectorization by flowmeters and minimum cost tree
