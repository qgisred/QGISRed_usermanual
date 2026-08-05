# Longitudinal Profiles

**Analysis bar → Longitudinal profile…**

The longitudinal profile shows the evolution of a hydraulic variable along an interactively defined path over the network. The X axis represents the accumulated distance from the initial node of the tour; the Y axis, the value of the selected variable at each node of the path. It is possible to have multiple profile panels open simultaneously, each with its own independent path, variables and settings.

> **Prerequisite**: An EPANET simulation must have been run before opening the profile. If no results are available, the plugin displays the message _"Run a simulation first to build a longitudinal profile."_

> 📝 The plugin automatically detects whether the results come from the EPANET standard format or the QGISRed extended `.hyd` format; no manual adjustment is necessary.

<figure><img src="../assets/images/analisis/perfil-longitudinal-dock.png" alt="Longitudinal profile dock with route drawn on the map and pressure graph"><figcaption><p>Longitudinal profile dock with route drawn on the map and pressure graph</p></figcaption></figure>
*Longitudinal profile: route highlighted in red on the map (left) and graph of piezometric height + terrain elevation (right).*
<!-- TODO: Deprecated capture — the Pick/Add node/Remove node/Move node/Branch buttons on the toolbar have been replaced with a single Edit Paths button + Help button -->

---

## Multiple profile windows

The plugin allows you to keep multiple profile docks open at the same time. Each dock works completely independently: it has its own path, its own selected variables and its own graph settings.

- The **New Panel** button on the toolbar creates an additional dock numbered sequentially (_Profile 2_, _Profile 3_, etc.).
- The active panel—the one that receives map interactions—is visually distinguished from the others.
- Opening the profile from the Analysis menu reuses the first panel if one is already open; otherwise create a new one.

---

## Open and build profile

1. Activate **Longitudinal profile** from the Analysis bar. The profile dock opens in the lower area of ​​QGIS.
2. The **Edit paths** button is automatically activated; the cursor changes to the pencil icon.
3. Click on a network node (Junctions, Tanks, Reservoirs) to set the first reference node.
4. Click on another node: the plugin calculates the **minimum topological path** between both nodes and draws the profile.
5. Each additional click extends the path by concatenating the path from the last node to the new one.
6. Right click (without node in progress) ends the editing route.

If two nodes are not connected in the network, the message _"Selected node is not connected to the previous one along the network."_

On the map, a **red line** is drawn over the path links and square **blue markers** are drawn over the reference nodes.

---

## Available variables

| Variable | Description |
|----------|-------------|
| **Elevation** | Terrain elevation — static, does not depend on the instant of time |
| **Head + Dimension** | Piezometric height and ground level together in the same graph |
| **Pressure** | Pressure in each node |
| **Quality** | Water quality at each node; the selector displays the project-specific quality name (for example, _Chlorine_) instead of the generic term _Quality_ |
| **Accumulated head loss** | Accumulated load loss along the route |

The default variable is **Head + Dimension**. When selected, the graph **simultaneously** shows the piezometric line (blue) and the terrain elevation (brown), allowing you to see at a glance whether positive pressure exists at each point along the route.

The graph updates automatically when the time instant changes in the Results dock.

> 📝 When time instants are available, the graph title displays **"Longitudinal profiles at HH:MM:SS"**. For static results **"Longitudinal profiles"** appears simply.

> 📝 Axis labels include the project unit in square brackets (e.g. _Head [m]_, _Pressure [bar]_, _Distance [m]_). The value table headers also show the units.

### Secondary axis

To the right of the main variable selector is the **2nd axis** combo. Allows you to superimpose a second variable on the **right Y-axis** of the graph, with its own independent scale.

- The variables available in the secondary axis depend on the main selection.
- The secondary axis curve can be deleted directly from the chart legend.
- The right Y axis has its own scale and label settings, accessible in **Chart options → Axes** (see [Chart customization](#personalización-del-gráfico)).

---

## Dock toolbar

### Tour Edit Modes

All editing actions are controlled from a single toggle button, rather than a separate button per action:

| Button | Function |
|-------|---------|
| **Edit paths** (pencil icon, toggleable) | Activate editing mode: left click to trace the route node by node, right click on a node to see its options (see [Mouse shortcuts](#atajos-de-ratón)). When disabled, moving the mouse over the path only highlights it and displays information, without modifying it. |
| **Help** (ⓘ icon) | Opens the **"How to edit paths"** dialog, with a summary of all available editing actions and mouse shortcuts. |

> 📝 Adding an intermediate step node, deleting it, moving it or creating a branch no longer has its own button on the toolbar: they are done with **Edit paths** active, using the context menu (right click) or the mouse shortcuts described in [Mouse shortcuts](#atajos-de-ratón). These actions work the same on the main route and on the branches.

### Chart navigation

| Button | Function |
|-------|---------|
| **Zoom window** | Draw a rectangle on the graph to zoom in on the X axis |
| **Bread** | Drag the graph horizontally; exclusive with Zoom window |
| **Zoom in / Zoom out** | Zooms in or out on the X axis |
| **Fit** | Restores full profile view |

The mouse wheel also zooms by centering on the cursor position.

### Display Options

| Button | Function |
|-------|---------|
| **Labels** | Displays the numerical value of the variable over each reference node |
| **Symbols** | Shows element symbology (node, tank, reservoir, pump, valve) and flow direction arrows on the curve |
| **Envelope** | Opens a submenu to activate the Min/Max envelope of the simulation (see section [Envelope](#envolvente-minmax)) |
| **Chart options** | Open the chart customization dialog |

### Table and export

| Button | Function |
|-------|---------|
| **Table** | Show or hide the table of values ​​to the left of the chart |
| **Export CSV** | Export table of values ​​to CSV with regional separators |
| **Export image** | Save the graphic as PNG or SVG |
| **Export configuration** | Save the current profile settings to a file `.cfg` (see section [Import and export settings](#importar-y-exportar-configuración)) |
| **Import settings** | Load a previously saved profile configuration from a file `.cfg` |
| **New panel** | Create an additional sequentially numbered profile dock |
| **Clear** | Clears the entire route, branches and highlighting from the map |

---

## Min/Max Envelope

Available for **Head + Dimension**, **Pressure** and **Quality**. Shows the historical range of variation of the entire simulation superimposed on the profile of the current moment.

| Mode | Description |
|------|-------------|
| **Off** | Without envelope |
| **Shaded band only** | Orange shaded area between the historical high and low values ​​|
| **Boundary lines only** | Two orange dashed lines marking the maximum and minimum |
| **Band and lines** | Both superimposed |

When the envelope is active, the value table adds columns with the maximum value, maximum time, minimum value, and minimum time for each node.

---

## Branches

The **Create branch** action allows you to add lateral branches that share the same graph with the main path.

1. With **Edit paths** active, right-click on a node already belonging to the main path or an existing branch and choose **Create branch** from the context menu (or double right-click directly on it if it is an interior node with connection degree greater than 2; see [Mouse shortcuts](#atajos-de-ratón)). That node defines the bifurcation point and its position on the X axis.
2. Make successive clicks to extend the branch to other nodes.
3. Right click to finish the branch.

Each branch is drawn with a different color from the palette. The branch distances are calculated from the branch point, so that both curves share the same origin X at that point. When the selected variable is **Head + Elevation**, the branches also show their own elevation curve of the terrain next to the piezometric line.

> ⚠️ **Course integrity restrictions**
>
> - A branch cannot reuse links or nodes that already belong to the main path or another branch, except the origin branch node. If attempted, the operation is rejected with an error message.
> - The source node of a branch cannot be removed from the main traversal while the branch is active. To eliminate it, it is necessary to first trim the branch from its farthest end.
> - **Move pass node** also checks for conflicts with existing paths before applying the change.
> - Any edit operation (declare, delete, or move a step node) is silently undone if the resulting recalculated path is invalid.

Declaring, removing or moving a step node (previously **Add node**, **Remove node** and **Move node**) works the same on the main path as on the branch paths.

Branches can be deleted directly from the **chart legend**, without needing to use the Clear button.

The **Clear** button deletes the main path and all branches.

---

## Mouse shortcuts

With **Edit paths** active, in addition to tracing the path click by click, the mouse supports several direct shortcuts that avoid going through the context menu. These shortcuts work the same on the main route and on the branches.

- **Double left click on an intermediate node** of the route (one that is not yet a pass node): declares it as a pass node (equivalent to **Declare pass node**).
- **Double left click on an already declared pass node**: deletes it and the path is recalculated (equivalent to **Delete pass node**).
- **Double right click on an extreme path node** (the origin or end of a path, with free connection available): extends the path from that point (equivalent to **Extend path**).
- **Double right click on an interior passage node** with connection degree greater than 2 (and free connection available): start a branch from that node (equivalent to **Create branch**).
- **Simple left click on a passage node**, without any traversal in progress: starts the movement of that node; the next click marks the destination node (equivalent to **Move pass node**).
- **Single right click**: if there is a tour in progress, ends it; if not, it opens the context menu with the actions available for the node under the cursor.

The context menu (simple right click) offers different options depending on the indicated node:

| Node situation | Menu options |
|---------------------|--------------------|
| There is no route yet | **Start new path here** |
| Intermediate node of the route (not yet a passing node) | **Declare pass node** |
| Origin step node of the main route | **Extend path**, **Create branch** |
| Extreme passage node (end of a route) | **Extend path**, **Create branch**, **Move pass node**, **Delete pass node** |
| Interior passage node of the route | **Create branch**, **Move pass node**, **Delete pass node** |
| Branch node (origin of a branch) | **Create branch** |

> 💡 The **Help** button on the dock toolbar (ⓘ icon) opens the **"How to edit paths"** dialog at any time, with this same summary information.

---

## Interactive Tooltip

When you move the mouse over the graph, a dashed vertical line indicates the position of the cursor. Above each active series a highlight circle appears on the nearest node and an information box with:

- Element ID
- Accumulated distance from the initial node
- Value of the variable for each active series

**Vertical reference lines** are drawn on the graph at the X position of each node in the path: thin light blue lines for all nodes and thicker lines for reference nodes.

### Two-way sync with map

The interaction between the graph and the map is bidirectional and updates in real time:

- When you move your mouse over the **graph**, the closest node is highlighted on the **map canvas** with an orange circle.
- Moving the mouse over the **map** while **Edit paths** is active moves the graph cursor to the corresponding node.

---

## Import and export configuration

Two toolbar buttons allow you to save and recall the complete configuration of a profile panel.

**Default path**: the same folder as the simulation results, with the name `{salida}_Profile_Config.cfg`.

Stored settings include:

- Main variable and secondary axis variable (if any)
- Reference nodes of the main route
- All branches defined
- Display options: symbols, labels, envelope
- Axes configuration (scale, labels, grid)
- Curve styles (color, thickness, line type, markers)
- Free description text associated with the panel

> 💡 The dock includes a free text field (description or comment) that is saved along with the configuration and can be used to identify the analysis or note observations.

When **importing** a configuration, the profile is recalculated from the stored nodes. If any node no longer exists in the network, the plugin displays a warning and continues with the available nodes.

---

## Chart customization

The **Chart options** dialog (setting button on the bar) has four tabs. The **Apply** button previews changes in real time without closing the dialog.

**Axes Tab**
For each axis (X = distance, Y = variable):
- Custom title.
- Auto scaling (enabled by default) or manual fixed range.
- Show or hide grid.

When a variable is active on the **secondary axis**, an additional **Y Axis (right)** group appears with its own scale and label settings, independent of the primary Y axis.

**Curves Tab**
For each active series:
- Color, line style (Solid / Dashed / Dotted) and thickness.
- Bookmarks: show/hide and size.

**Legend Tab**
- Show/hide legend.
- Position (Left/Center/Right), font size and symbol size.
- Show frame and background color of the legend.

**General Tab**
- Background color of the chart area.
