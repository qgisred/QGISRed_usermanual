# Results Viewer

Once the simulation is complete, QGISRed offers two complementary tools to explore the results: the Results dock, which controls the display on the map, and the Time series dock, which shows the evolution of any variable over time for individual elements.

---

## Results dock

The Results dock is anchored to the right area of ​​the screen. Contains **three tabs**:

- **Results**: interactive visualization on the map with variable selection, temporal navigation and map options.
- **Report**: EPANET engine text report.
- **Appearance**: complete configuration of the visual appearance of the results on the map.

<figure><img src="../assets/images/analisis/results-dock.png" alt="Results panel with variable selector and time bar"><figcaption><p>Results panel with variable selector and time bar</p></figcaption></figure>
*Results dock: variable selection, statistics mode and navigation by time instants.*
<!-- TODO: screenshot outdated after adding the Constant playback rate button next to the speed slider -->

---

### Results tab

#### Timing Group

Displays the current time instant in `HH:MM:SS` format (or in am/pm format if active). Includes buttons to toggle between civil format and elapsed time format.

When a stat mode is active (Maximum, Minimum...), the time area shows the name and description of the stat instead of the clock.

#### Temporal navigation (Time controls)

| Control | Description |
|---------|-------------|
| **Time Slider** | Scroll through the moments of the report. |
| **Combo of moments** (`cbTimes`) | Drop-down list with all available moments. |
| **Forward/backward buttons** | Next, previous, start, end. |
| **Play / Play backward** | Automatic forward or backward animation. |
| **Speed ​​slider** | Controls the relative speed of the animation (1–10). It is hidden when **Constant playback rate** is active. |
| **Constant playback rate** | Switchable button next to the speed slider. When activated, the slider is replaced by the field **"1h in: N sec"**: N are the actual seconds it takes to play an hour of simulated time (1–3600), so the playback speed is constant with respect to the simulated time even if the step between instants is not uniform. When you deactivate it, the relative speed slider is used again. The state and value are saved in the project. |
| **Loop** | Repeat the animation in a loop. |

> 💡 When you change the time instant, activate or deactivate a statistics mode, modify the decimals in the Appearance tab, or load all the results at once, QGISRed rereads and reformats the values. If the operation takes a while (large networks with many elements), a notice appears superimposed and centered on the map: **"Reading results… NN%"**. In quick operations it is not displayed, to avoid flickering.

#### Reported Times and Statistics

Two combos located under the time controls:

| Combo | Description |
|-------|-------------|
| **Reported Times** (`cbResultTimes`) | Filter which moments are shown: Single Period, Step times or All calculation times. |
| **Statistics** (`cbStatistics`) | Applies a statistic on all periods: Maximum, Minimum, Range, Average, StdDev, Warning. When active, the clock is replaced by the stat name. |

> 💡 In **Maximum** and **Minimum** modes, the map labels show the value along with the time of occurrence in the format `valor (@ HH:MM:SS)`. When you place the cursor over a map element, the tooltip includes an additional line `@ HH:MM:SS` with the exact moment in which that maximum or minimum occurred.

> 💡 With any stat mode active, the tooltip prepends the value with the abbreviation of the displayed statistic: **Max**, **Min**, **Avg** (Average), **Rng** (Range) or **Std** (StdDev). For example, `Max 45.2` instead of simply `45.2`.

#### Mapping Group — Nodes

| Control | Description |
|---------|-------------|
| **Combo Nodes** (`cbNodes`) | Property to display in nodes: Pressure, Head, Demand, Quality. |
| **Show Node Labels** | Displays labels with the ID and value on each node on the map. |
| **Show Node Histogram** | Opens a built-in histogram in the dock with the distribution of the current value in knots. |
| **Show Node Evolution** | Opens an integrated mini-graph with the temporal evolution of the selected node on the map. |

> 💡 When a variable is selected in the **Nodes** combo, a label appears next to the group header with the variable name in bold and its unit in parentheses (for example, **Pressure** (m)).

#### Mapping Group — Links

| Control | Description |
|---------|-------------|
| **Combo Links** (`cbLinks`) | Property to display in pipes/valves/pumps: Flow, Velocity, HeadLoss, UnitHdLoss, FricFactor, Status, ReactRate, Quality. |
| **Show Link Labels** | Displays labels with the ID and value on each pipe. |
| **Show Flow Directions** | Add flow direction arrows on the pipes. |
| **Show Link Histogram** | Histogram integrated into the dock with the distribution of the current value in pipes. |
| **Show Link Evolution** | Integrated mini-graph with the temporal evolution of the selected pipeline on the map. |

> 💡 Similarly, when a variable is selected in the **Links** combo, a label appears next to the group header with the variable name in bold and its unit in parentheses (for example, **Velocity** (m/s)).

> ⚠️ When the **Links** variable is **Status**, the text labels are simplified: the ~13 internal states that EPANET can return are grouped into just two texts, **"Closed"** (includes "Temp Closed") and **"Active"** (includes "Active (Rev Pump)"). Links with any state **"Open*"** do not show any labels, so as not to clutter the map with most of the pipes (which are usually open). It is not an error if, with Status active, most of the pipes appear without label.

> The **Appearance** button (icon in the header of the Nodes group) takes you directly to the Appearance tab without having to navigate through the tabs.

---

### Report Tab

Displays the text report generated by the EPANET engine upon completion of the simulation. Includes:

- General mass balance of the network.
- List of nodes with negative pressure or out of range.
- Warnings of pumps operating outside their curve.
- Convergence status of the hydraulic calculation in each step.
- Summary of quality reactions (if quality was simulated).
- In case of error, the full content of the report is automatically displayed here.

> The status report is the first place to look when a simulation produces unexpected results or does not converge.

---

### Appearance Tab

Concentrates all the options for visual presentation of the results on the map. Settings are automatically saved to `{Red}_Results_Config.cfg` within the project's `Results/` folder and restored in the next session.

> 💡 Each numerical control in the Appearance tab has a small individual ↺ button that restores only that field to its default value, without affecting the rest of the settings.

> ⚠️ The **Nodes** group controls are automatically disabled when the Nodes combo is set to "None", and the same is true for **Links**. Additionally, the **Decimals** control is disabled when the active variable is **Status** (categorical variable with no applicable decimals).

#### Map Labels

| Option | Description |
|--------|-------------|
| **Font size (pt)** | Font size of labels on the map (6–24 pt, default 8). |
| **Nodes / Links decimals** | Number of decimals displayed on node and pipe labels respectively (0–6). The control is labeled with the name of the currently active variable. |
| **Text color** | Default Color: Knots **#333333** (Dark Grey), Piping **#0A143C** (Navy Blue). **Black**: always black text. **By range**: The text color follows the palette of the active value range. When **Show Node ID** or **Show Link ID** is active, the Id line uses the color of the element itself and the value line uses the color of the symbol or range. |
| **Background** | Background color behind map labels. Includes a color picker and a delete button to remove the background. Next to the selector is a **lock** icon: open (by default), the labels background is independent of the map background; When you close it, the selector and clear button are disabled and the labels background is linked to the **Map Background** color (see below), so changing that color also automatically changes the labels background. |
| **Buffer** | Outline color (halo) around label text, with its own color picker and delete button. It is independent of the Background and is never linked to the Map Background. Without an assigned color (default) no halo is drawn. |
| **Show Node ID** / **Show Link ID** | Two independent boxes: add the ID of the node or the pipe, respectively, in the first line of its label. |

#### Symbology

| Option | Description |
|--------|-------------|
| **Hide border on junctions** | Hides the edge/outline of junction markers. Enabling this option removes the outline surrounding the knot symbol. |
| **Proportional to value** | Scales the size of the nodes and the thickness of the pipes linearly with the represented value. Does not apply to the Status field. |
| **Nodes factor** | Base scale factor of knot marker size (0.25–4.0, default 1.0). |
| **Links factor** | Pipe thickness base scaling factor (0.25–4.0, default 1.0). |
| **Arrows factor** | Flow direction arrows scale factor (0.25–4.0, default 1.0). |

#### Map Background

Allows you to set a solid background color for the map canvas while viewing results. The color is restored to the original when the dock is closed. The **×** button removes the background color.

#### Reset all

Returns all parameters on the Appearance tab to their default values.

---

### Scenarios

The dock supports multiple outcome scenarios. Each scenario is identified by a name (by default `Base`) and is stored as files `.out` / `.hyd` in the `Results/` subfolder of the project. The name of the active scenario appears in the panel title.

---

### Available properties

**Knots** (Junctions, Tanks, Reservoirs):

| Property | Description |
|-----------|-------------|
| `Pressure` | Pressure in m.c.a. |
| `Head` | Piezometric height in m |
| `Demand` | Calculated demand |
| `Quality` | Water quality (depending on the type configured in Analysis options) |

**Pipes, valves and pumps** (Links):

| Property | Description |
|-----------|-------------|
| `Flow` | Flow rate (with sign or without sign) |
| `Velocity` | Speed ​​in m/s |
| `HeadLoss` | Head loss in m |
| `UnitHdLoss` | Unit loss in m/km |
| `FricFactor` | Friction factor |
| `Status` | Operational status (Open / Active / Closed) |
| `ReactRate` | Reaction rate (quality models) |
| `Quality` | Water quality |

> 💡 The map labels for the **Flow** variable always show the absolute value (without a negative sign), even in the Maximum and Minimum statistics modes. The direction of flow is indicated by the direction arrows, not by the value sign.

---

## Time series (Time series…)

**Analysis bar → Time series…**

Activates an interactive selection tool that plots the time evolution of any result property for one or more network elements.

<figure><img src="../assets/images/analisis/time-series-dock.png" alt="Panel Time series with multi-knot pressure curves"><figcaption><p>Panel Time series with multi-knot pressure curves</p></figcaption></figure>
*Panel Time series: time evolution of pressure in several nodes selected simultaneously.*

### Process

1. Activate **Time series** (checkable button). The Time series panel opens at the bottom of the screen.
2. Click on any element on the map (node, pipe, valve, pump, tank, reservoir).
3. The panel draws the time curve of the active property in the Results dock for that element.
4. The item is highlighted in blue on the map.

### Multiple selection

- **Shift + click** on another element: adds its curve to the graph without deleting the previous ones. Each curve receives a different color from the palette.
- **Shift + click** on an element already selected: removes it from the graph.
- **Click without Shift** with more than one active curve: asks for confirmation before clearing the selection.

### Property Selection

- By default, the active property is represented in the Results dock for the type of element clicked.
- **Right click** on an element: Opens a context menu to choose any other properties available for that element without changing the Results dock view.

### Additional properties for buckets

For the **Tank** element type, two additional quantities are available:

| Magnitude | Description |
|----------|-------------|
| **Volume** | Stored volume in m³ (or ft³ depending on project units), calculated from EPANET output binaries. |
| **TankSpill** | Overflow flow. It is only non-zero if the tank has the EPANET overflow option enabled. |

### Network global variables

In addition to individual elements, the Time series panel allows you to add **global series** that aggregate values ​​over the entire network. These series do not require clicking on the map: they are added from the graph's variable selection menu.

| Global variable | Description |
|-----------------|-------------|
| **TotalWaterSupply** | Total flow supplied by all reservoirs and sources in the network. |
| **TotalWaterDemand** | Total demand consumed by all nodes in the network. |
| **AverageNodePressure** | Average pressure of all nodes (excludes tanks and reservoirs). |
| **TotalStoredVolume** | Total stored volume adding all tanks in the network. |
| **TotalTankSpill** | Total overflow flow adding all the tanks in the network. |

### Curve configuration

From the Time series panel you can adjust for each curve:

- Name in the legend.
- Color, line style (solid, dashed, dotted) and thickness.
- Markers: symbol, size, color, space.
- Show values ​​at each point of the curve.
- Visibility (show/hide without deleting).

### Table of values ​​

The values ​​table displays the numerical data for all active curves. The **first column** (time instant) is **fixed**: it does not disappear when scrolling the table horizontally when there are many curves. This makes it easy to identify where each row is at without having to go back to the beginning.

### Synchronization with the value table

When you move the cursor over the chart, the corresponding row of the stock table is automatically highlighted in real time.

### Copy table to clipboard

The copy function generates **two header rows**: the first with the name of the element or magnitude and the second with the unit. Facilitates direct pasting into spreadsheets.

### Export and import chart settings

The **Export chart configuration** and **Import chart configuration** buttons save and retrieve the complete configuration of curves, axes and styles in a `.cfg` file. It is also possible to export the general template configuration (axes, styles) even if there are no curves loaded, and apply it when importing it on a new graph.

### Multiple chart windows

The **New chart window** button opens a new independent Time Series window. Each window has its own curve context, property and selected elements. You can keep several windows open simultaneously to compare different variables or areas of the network.

### Time format synchronization

The "Time of Day" column in the values ​​table automatically uses the same format (24h or am/pm) as the Results panel.

### Closing

When you turn off the **Time series** button or close the panel, the highlight disappears and the cursor returns to standard navigation mode.
