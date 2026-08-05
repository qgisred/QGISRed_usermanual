# Property Inquiries

**Queries bar → Queries by properties…**

Opens the **Queries by Properties** panel, a filtering tool that highlights on the map all elements that meet one or more conditions on their attributes. It is the fastest way to find, for example, all pipes with a diameter less than 80 mm, all nodes with pressure below a threshold, or all valves in a closed state.

<figure><img src="../assets/images/consultas/queries-by-properties.png" alt="Queries by Properties panel with configured conditions and result highlighted in magenta"><figcaption><p>Queries by Properties panel with configured conditions and result highlighted in magenta</p></figcaption></figure>
*Queries by Properties Panel: conditions configured on pipe attributes. Items that meet the condition are highlighted in magenta on the map.*

---

## Dashboard interface

The panel has an identifying color **purple** (`#7B1FA2`) in its header to distinguish it from the rest of the QGISRed panels. Contains:

- **Element type selector**: Pipes, Junctions, Tanks, Reservoirs, Pumps, Valves
- **Conditions area**: one or more rows with field, operator and value
- **Run button**: applies the query and highlights the result
- **Clear Button**: removes the map highlight
- **Time label**: When simulation results are loaded, displays the active instant with the prefix "Time:" followed by the bold value in `HH:MM:SS` format. The statistics label for the result is also shown in bold.

---

## Types of conditions

The operator available for each field depends on the data type:

### Numeric fields

| Operator | Meaning |
|----------|-------------|
| `All` | No filter (all values) |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |
| `=` | Equals |
| `>` | Greater than |
| `<` | Less than |
| `≠` | Other than |
| `Range` | Between two values ​​(closed interval) |

### List fields (enumerated)

Fields like `Status` that have a finite set of possible values:

| Operator | Meaning |
|----------|-------------|
| `All` | No filter |
| `=` | Equal to selected value |

> ℹ️ For `Type`/`ValveType` on valves, the value selector shows the type's long descriptive name (e.g. "Pressure Reducing" for PRV) instead of the EPANET code.

### Free text fields

Fields like `Tag` or `Id`:

| Operator | Meaning |
|----------|-------------|
| `All` | No filter |
| `=` | Exact same |
| `≠` | Different |
| `ILIKE` | Contains (case-insensitive) |
| `NOT ILIKE` | Does not contain (case-insensitive) |
| `LIKE` | Contains (case sensitive) |
| `NOT LIKE` | Does not contain (case sensitive) |

---

## Process

1. Open **Queries by properties** from the Queries bar.
2. Select the **item type** you want to filter on.
3. Add one or more conditions: choose the field, the operator and write the value.
4. Press **Run**. QGISRed evaluates the query and highlights in **magenta** all the elements that meet all the conditions simultaneously (AND logic).
5. Highlighted items remain visible while the panel is active. Press **Clear** to remove the highlight.

---

## Combination of conditions

All active conditions are combined with **AND** logic: an element is only highlighted if it meets **all** conditions at once. For an OR logic (any of the conditions), it runs separate queries with a single criterion at a time.

---

## Simulation results

If the project has simulation results loaded, the result fields (pressure, flow, velocity...) also appear in the field selector, allowing you to filter, for example, pipes with a velocity less than 0.5 m/s or nodes with negative pressure.

> ⚠️ **Conditional quality fields.** The result fields `Quality` and `ReactRate` only appear when the project's quality model allows it: `Quality` is hidden with *None* model and `ReactRate` is only visible with *Chemical* model. Static quality fields (`BulkCoeff`, `WallCoeff`, `ReactCoef`, `IniQuality`) are hidden when the quality model is *None*, *Age*, or *Trace*.

---

## Usage Notes

- The query does not modify any model data or create new layers: it only changes the temporal symbology.
- Magenta highlighting is visible on any map background.
- When you close the panel, the highlight disappears and the symbology returns to the previous state.

## ID field resolution

The panel uses the same automatic identifier field resolution logic as the Element Explorer (`getIdFieldName(layer)`). Query fields by ID (`PipeID`, `TankID`, etc.) are automatically detected based on the layer type, so queries on the `Id` field work correctly regardless of the actual name of the field in the project shapefile. See [Element Explorer](element-explorer.md) for more details.

The aliases `PumpCurvID`, `BaseDem` and `SourceQual` are automatically recognized as numeric type fields for pumps, demands and sources respectively. The data type of each field (numeric, list or free text) is determined automatically from the element's schema, without the need for manual configuration.
