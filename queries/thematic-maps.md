# Thematic Maps

**Queries Bar → Thematic maps…**

Opens the **Thematic Maps** dialog, which generates layers that color pipes and nodes by intervals of a hydraulic attribute. Unlike other QGISRed dialogs, you don't have to choose a "field and confirm": each available attribute has its own box, and you can check as many at once as you want — each one generates its own layer, and they all live on the map simultaneously.

<!-- TODO: capture pending — Thematic Maps dialog with Pipes and Knots boxes -->

---

## Active elements: pipes and nodes

In the current version, **Thematic Maps works on the Pipes and Junctions layers**. The options for other types of elements (valves, pumps, tanks, reservoirs) are present in the interface but are automatically hidden because they are not yet implemented. The groups **Service connections**, **Isolation valves** and **Meters** are visible, but their only checkbox ("Temporary") is also not operational yet — do not check it.

---

## Process

1. Open **Thematic maps** from the Queries bar.
2. Check the boxes of the attributes you want to represent (you can check several pipes and nodes at the same time).
3. Press **Accept**. QGISRed creates a layer for each checked box, within the **Queries → Thematic Maps** group of the QGIS layers panel.
4. To remove an already generated map, reopen the dialog, uncheck its box and press **Accept** — QGISRed deletes that specific layer without touching the rest. The boxes on the already generated maps appear pre-marked.

> 💡 You can have multiple thematic maps open at once (e.g. Pipe Material and Year of Installation along with Node Base Demand) — each is a separate layer, they do not replace each other as was the case before.

---

## Available fields for pipes

| Field | Description |
|-------|-------------|
| `Diameter` | Pipe diameter |
| `Length` | Length |
| `Material` | Pipe material, colored with QGISRed's fixed palette (see table below) |
| `Roughness` | Roughness coefficient — classes and style file depend on the **pressure loss formula** active in the project (Hazen-Williams, Colebrook-White or Darcy-Weisbach) |
| `Age` | Age, calculated from the year of installation; classes are labeled with "yrs" suffix |
| `Installation Year` | Year of installation |

> The **Age** and **Installation Year** maps add three columns together to the layer's attribute table: the raw installation date (`InstalDate`), the extracted year (`InstYear`), and the calculated age (`Age`) — seeing them all at once is useful even if you've only marked one of the two maps.

---

## Available fields for nodes

| Field | Description |
|-------|-------------|
| `Elevation` | Knot level. Classes are automatically calculated from the actual project values ​​(there are no standard ranges) — the legend shows the cuts with the project length unit (e.g. "< 120 m", "120 < 180 m", ">= 180 m"). |
| `Total Base Demand` | Total base demand of the node. The circles are **sized proportionally** to the demand (non-linear, so that very large values ​​do not visually dominate the map), in classes also calculated from the actual data, labeled on the project's active flow unit. If the node has multiple demand categories (see [Demands and scenarios](../tools/demands-and-scenarios.md)), the layer reflects the aggregate sum; nodes with zero demand are not shown. |

---

## Material palette

The **Material** map colors each pipe based on the value of its `Material` field, comparing it (case insensitive) against the abbreviation or name in this fixed table — a material that does not appear here receives a random color instead:

| Abbreviated | Materials | Abbreviated | Materials |
|--------|----------|--------|----------|
| FG | Gray Cast Iron | Pb | Lead |
| FD | Ductile Casting | PVC | Polyvinyl Chloride |
| ACE | Steel | PE | Polyethylene |
| STAINLESS STEEL | Stainless Steel | PVC-O | Oriented PVC |
| FC | Fiber cement | PVC-R | Rigid PVC |
| AGal | Galvanized Steel | Cu | Copper |
| HCCC | Concrete with sheet metal jacket | PE-AD | High Density Polyethylene |
| HSCC | Concrete without sheet metal jacket | PE-BD | Low Density Polyethylene |
| HAr | Reinforced Concrete | PE-MD | Medium Density Polyethylene |
| HPr | Prestressed Concrete | GRP | Fiberglass Reinforced Polyester |

> This color table only applies to the **default** style that QGISRed comes with. If you save your own Material legend from the legend editor (see [Overview and layer management](../active-project/layers-and-legend.md)), your colors take precedence over this palette when you regenerate the map.

---

## Outdated map notice

If you change the project's **units**, **head loss formula** or **flow units** after generating a thematic map that depends on them (Diameter, Length, Roughness, Base Demand...), QGISRed marks that layer with a warning icon ⚠ in the layers panel — the same icon it already uses to warn of outdated simulation results.

- Mouse over the icon to see the reason.
- Click on the icon to rebuild that layer with the current configuration, without having to reopen the dialog.

---

## Result on the map

Each checked box generates its own layer (for example `Pipe Materials`, `Junction Elevations`) within the **Queries → Thematic Maps** group. The layers are read-only and update themselves when you edit the source pipe or node (there is no need to regenerate the map by hand after a specific change) — the legend of each one also shows how many elements each class has.

If you check and confirm an already generated box again, QGISRed replaces that specific layer with the new configuration, without touching the rest of the active maps.

---

## Usage Notes

- The generation of thematic maps does not modify any model data; it only creates new layers with the corresponding symbology.
- To remove a map, uncheck it in the dialog (see "Process" above) or delete its layer directly from the QGIS layers panel.
- The **Total Base Demand** map requires nodes with assigned demand to exist; If the project has no demands loaded, the layer is generated empty.
