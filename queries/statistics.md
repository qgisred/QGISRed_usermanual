# Statistics

**Queries Bar → Statistics…**

Opens the **Statistics** panel, which calculates and displays the statistical distribution of any numerical or categorical attribute in the network, with support for automatic classification, second cross-classification, and graphical representation.

> **ℹ️ Note:** The Statistics panel opens **docked** in the main QGIS window and respects the panels already grouped into tabs. Its controls also adapt to narrow panel widths, without being cut off on the right edge.

<figure><img src="../assets/images/consultas/statistics-panel.png" alt="Statistics panel with histogram of pipe diameters"><figcaption><p>Statistics panel with histogram of pipe diameters</p></figcaption></figure>
*Statistics Panel: histogram of pipe diameters with classification by intervals.*

---

## Panel structure

The Statistics panel is organized into two tabs:

- **Setup**: defines what is analyzed and how it is classified.
- **Report**: shows the histogram and results table. It is activated automatically after running the analysis.

---

## Configuration Tab

### Element type and property

Select the type of element (Junctions, Pipes, Tanks...) and the property to analyze. The property selector displays in a **unified list** both the design fields (Diameter, Length, Roughness...) and the simulation result fields (Pressure, Flow Rate, Velocity...). Result fields appear with **yellow/cream background** to visually differentiate them from design fields.

### Main classification

| Parameter | Description |
|-----------|-------------|
| **Field** | Property to sort by |
| **Method** | How to calculate the intervals (see table below) |
| **Number of classes** | How many groups are generated |

#### Available sorting methods

The following methods are available for both the main sort and the second sort. The default method is **Pretty Breaks**.

| Method | Description |
|--------|-------------|
| **Jenks (Natural Breaks)** | Minimizes intra-class variance. Ideal for non-uniform distributions. |
| **Pretty Breaks** | "Round" interval boundaries. Preferable for presentations. *(Default)* |
| **Equal Count** | Each class contains the same number of elements. |
| **Fixed Interval** | All intervals have the same amplitude. |
| **Manual** | The user directly defines the limits of each interval. |

> **ℹ️ Note:** When all values ​​are identical or very similar, duplicate class endpoints are collapsed showing a single value instead of "100.0 - 100.0".

> **ℹ️ Note — Fields without useful data:** If the field chosen to classify does not have any calculated value, the panel does not show an error message: it directly generates a single class **NULL** that groups all elements without value. If the field has values ​​but they are all equal (including the case where they are all zero), a single class is generated with that value, just as in the previous case of collapsed endpoints. In both cases the histogram and table are generated normally, without interrupting the analysis.

> **ℹ️ Note:** When analyzing a dynamic simulation result field, the **class limits are calculated once** considering all time instants simultaneously. As the simulation step progresses, the count of elements per bar varies, but the limits remain constant, allowing **to compare distributions between time instants** with complete consistency.

### Pre-filtering

Before calculating, you can limit the set of elements with a condition on any field:

- **numeric** fields: `>=`, `<=`, `=`, `>`, `<`, `≠`, `Range`
- **list** fields: `=`
- **text** fields: `=`, `≠`, `ILIKE`, `NOT ILIKE`, `LIKE`, `NOT LIKE`
- Select **No Filter** to include all elements without restriction.

The **Value** field includes a **(×)** clear button: when pressed, it clears the entered text and leaves no active selection, making it easy to change the filter quickly.

When the filter attribute is a simulation result field, the combo displays the same **yellow/cream background** that is used for these fields in the property selector.

> **ℹ️ Note — Flow:** When filtering on the `Flow` field with a written numerical value, the value is always interpreted as **absolute value**, so it is not necessary to know the sign that EPANET internally assigns to the flow.

### Restrict to active selection

The **Only selected elements** checkbox limits the analysis to the elements currently selected on the map. The selection is evaluated jointly between the **Inputs** layer and its corresponding **Results** layer: if the element is selected in either layer of the same type (for example, `Pipes` in Inputs and its pipeline results theme), it is included in the calculation.

> ⚠️ If you activate the box and no element is selected in either layer, the panel displays a warning and does not run the analysis.

While the checkbox is active, both the histogram and the table display a note indicating that there is a selection filter (and, if there is also an active attribute filter, both are combined in the same text).

#### Preview on map

The Filters section includes two additional items to scan the filter before running the full scan:

- **"Preview on map" checkbox**: When checked, items that meet the filter condition are highlighted in **orange** on the map canvas. The preview updates automatically when you change any filter parameter.
- **Match counter** (e.g. *"43 items match"*): visible whenever the Filters section is displayed, even before running the analysis.

Highlights are automatically removed when you close the panel or collapse the Filters section.

### Second classification *(optional)*

A collapsible group—collapsed by default—allows you to define a **second classification criterion** on the same set of elements. When deployed, the following are configured:

| Parameter | Description |
|-----------|-------------|
| **Field** | Second classification property |
| **Method** | Jenks (Natural Breaks), Pretty Breaks, Equal Count, Fixed Interval or Manual |
| **Number of classes** | Second classification groups |

When the second sort is active, the results table becomes a **cross matrix**: the rows represent the groups of the first sort and the columns represent the groups of the second.

> **ℹ️ Note:** When changing the element type and returning to the previous one, the second classification settings (method, number of classes, intervals, manual values) are **automatically recovered**.

---

## Report Tab

The Report tab is divided into two frames: **Histogram** and **Table**.

### Histogram

The histogram shows the distribution of the analyzed property:

- **Statistic selector**: Choose what is represented on the Y axis: Count, Sum, Avg, Min, Max or StdD.
- **Expand button**: opens the histogram in a **separate floating window**, useful for having the settings panel and the graph visible at the same time.
- The **chart title** includes the statistic selected as a prefix and the field units. For example: *"Avg Pressure (mca) by Diameters (mm) for PVC Material"*.
- For categorical fields, the histogram displays bars per category instead of numerical ranges.

### Results table

The table displays the same data in tabular format:

- The values ​​are formatted with the decimals corresponding to each field according to the CSV of project units.
- Whole numbers are displayed without decimals.
- The **table title** always reflects the two active classification dimensions, including the units of each field.
- The **export row** includes a statistics selector to choose which value is dumped when exporting to CSV (Count, Sum, Avg...).
- The CSV export includes the **manual breakpoint values** of both classifications (main and second), with the column headers accompanied by the units in parentheses.
- When the second sort is active, the table becomes a **cross matrix** with additional columns for each group of the second sort.

---

## Available fields

### Categorical fields

The following fields are treated as categories (discrete values):

| Field | Description |
|-------|-------------|
| `Material` | Pipe material |
| `Type` | Element type |
| `ValveType` | Valve type |
| `MeterType` | Counter type |
| `SourceType` | Font type |
| `IniStatus` | Initial operational status (Open / Closed / CV) |
| `InstalDate` | Installation date |
| `InstDate` | Installation date |
| `Tag` | Free label |

### Numeric input fields

Any numeric field in the model: `Diameter`, `Length`, `Roughness`, `Elevation`, `BaseDem`, etc.

### Simulation result fields

Available only if results are uploaded:

**Nodes:**

| Field | Description |
|-------|-------------|
| `Pressure` | Pressure (m.c.a.) |
| `Head` | Piezometric height (m) |
| `Demand` | Calculated demand (l/s) |
| `Quality` | Water quality |

**Pipes:**

| Field | Description |
|-------|-------------|
| `Status` | State in simulation |
| `Flow` | Flow rate (l/s) |
| `Velocity` | Velocity (m/s) |
| `HeadLoss` | Head loss (m) |
| `UnitHdLoss` | Unit loss (m/km) |
| `FricFactor` | Friction factor |
| `ReactRate` | Reaction rate |
| `Quality` | Water quality |

> **⚠️ Note:** Fields `Velocity`, `UnitHdLoss`, `FricFactor` and `ReactRate` are not available when the selected element type is **Pumps** or **Valves**; They are exclusive to pipes.

---

## Usage Notes

- The Statistics panel does not modify any data in the model.
- You can keep the panel open while you navigate the map or change parameters; updates the calculation when you press the run button again.
- The second classification is collapsed by default; deploy it only when you need cross-analysis.
