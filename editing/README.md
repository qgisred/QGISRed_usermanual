# ✏️ Editing and Modeling

The **Edition** bar contains all the tools to build and edit the network directly on the QGIS map. Work on the layers of the active project without having to open attribute tables or external files.

\*Bar Edition: creation of elements, geometric and topological editing, properties and operation data.\*

> All buttons require a valid project uploaded. If there are none, the plugin displays _"No valid project is opened"_.

***

## Edition Bar Tools

### Group 1 — Creation of elements

| # | Tool                     | Function                                                                   |
| - | ------------------------ | -------------------------------------------------------------------------- |
| 1 | **Add pipe**             | Draw pipes by clicking on the map; automatically creates nodes at the ends |
| 2 | **Add tank**             | Place a Tank on an existing node                                           |
| 3 | **Add reservoir**        | Place a reservoir or feed point (Reservoir) at an existing node            |
| 4 | **Insert valve in pipe** | Insert a valve into an existing pipe, splitting it                         |
| 5 | **Insert pump in pipe**  | Insert a pump into an existing pipe, splitting it                          |

### Group 2 — Geometric and topological editing

| #  | Tool                            | Function                                                               |
| -- | ------------------------------- | ---------------------------------------------------------------------- |
| 6  | **Select multiple elements**    | Multi-layer selection by rectangular area on the map                   |
| 7  | **Move nodes**                  | Move nodes by dragging all connected elements                          |
| 8  | **Edit link vertices**          | Add, move and delete intermediate pipe vertices                        |
| 9  | **Reverse elements**            | Reverses the direction of orientation of pipes or service connections  |
| 10 | **Split/Join pipes**            | Split a pipe at the indicated point or join two adjacent sections      |
| 11 | **Merge/Dissolve junctions**    | Merge two nodes into one or separate one node into several             |
| 12 | **Create/Remove T connections** | Create or delete a T-joint between a node and a nearby pipe            |
| 13 | **Create/Remove crossings**     | Creates or deletes a junction (shared node) between intersecting pipes |
| 14 | **Move valves/pumps**           | Move a valve or pump from one pipe to another                          |
| 15 | **Change element status**       | Toggles the Open/Closed status of pipes and valves                     |
| 16 | **Delete elements**             | Delete the highlighted item or selected items                          |

### Group 3 — Properties and operation data

| #  | Tool                          | Function                                           |
| -- | ----------------------------- | -------------------------------------------------- |
| 17 | **Edit element properties…**  | Opens the properties dialog of the clicked element |
| 18 | **Edit patterns and curves…** | Demand Pattern and Pump/Tank Curve Editor          |
| 19 | **Edit controls…**            | Simple controls and operating rules editor         |

***

## In this section

* [Creation of elements](creation.md) — pipes, tanks, reservoirs, valves, pumps
* [Geometric and topological manipulation](manipulation.md) — move, split, reverse, cross, delete
* [Element properties](properties.md) — editing dialog with integrated browser
* [Patterns and curves](curves.md) — demand patterns, H-Q curves, efficiency and volume
* [Controls and rules](controls.md) — simple controls and automatic operating rules
