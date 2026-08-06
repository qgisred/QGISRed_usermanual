# ✅ Debug

The **Debug** bar groups together the model verification and debugging tools. Its objective is to detect and correct topological errors, attribute inconsistencies and connectivity problems **before launching the simulation**, thus avoiding errors that are difficult to diagnose in EPANET.

<figure><img src="../assets/images/debug/barra-debug.png" alt="QGISRed Debug Toolbar"><figcaption><p>QGISRed Debug Toolbar</p></figcaption></figure>
*Debug bar: data validation, topological debugging, review of attributes and hydraulic sectors.*

---

## Debug Bar Tools

### Group 1 — Topology and coherence

| # | Tool | Function |
|---|-------------|---------|
| 1 | **Check && commit data** | Validates all model data and flags elements with errors |
| 2 | **Remove overlapping elements** | Detect and remove duplicate nodes or pipes in the same position |
| 3 | **Simplify link vertices** | Eliminates intermediate vertices aligned in straight sections |
| 4 | **Join consecutive pipes** | Merge adjacent pipes with identical diameter, material and year |
| 5 | **Create T connections** | Detects end nodes on pipes and creates the topological join |
| 6 | **Check connectivity** | Identifies areas isolated from supply sources |
| — | *Delete isolated subzones* | (Sub-option) Eliminates subzones with fewer pipes than the defined threshold |

### Group 2 — Attribute verification

| # | Tool | Function |
|---|-------------|---------|
| 7 | **Check pipe lengths** | Compare attribute lengths vs. geometry and points out differences |
| 8 | **Check diameters** | Detects diameters outside the usual range of the project |
| 9 | **Check pipe materials** | Detects undefined materials in the project's materials table |
| 10 | **Check pipe installation dates** | Detect incorrectly formatted or inconsistent installation dates |

### Group 3 — Hydraulic sectors

| # | Tool | Function |
|---|-------------|---------|
| 11 | **Check hydraulic sectors** | Classifies the areas of the network according to their supply capacity (types A–D) |

---

## In this section

* [Topology and connectivity](topology.md) — commit, overlapping, simplification, join, T-connections, connectivity
* [Attribute verification](attributes.md) — lengths, diameters, materials, installation dates
* [Hydraulic sectors](hydraulic-sectors.md) — classification of sectors type A, B, C and D
