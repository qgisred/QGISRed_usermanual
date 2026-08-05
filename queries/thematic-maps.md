# Thematic maps

**Queries Bar → Thematic maps…**

Opens the **Thematic Maps** dialog, which generates a visual representation of the network by coloring the pipes by intervals of any hydraulic attribute or simulation result.

\*Thematic Maps dialog: field selection, number of classes and color palette.\*

***

## Active element: pipes

In the current version, **Thematic Maps works exclusively on the Pipes layer**. Options for other types of elements (nodes, valves, pumps, tanks, reservoirs) are present in the interface but are automatically hidden because they are not yet implemented. When available, the dialog will display an element type selector.

***

## Process

1. Open **Thematic maps** from the Queries bar.
2. Select the **field to represent** in the drop-down menu (input attribute or simulation result).
3. Choose the **number of color classes**.
4. Select the **color palette** (single range gradient or bichromatic).
5. Set the **range** if you want to exclude extreme values.
6. Confirm. QGISRed generates layer `ThematicPipes` in the thematic layer group of the QGIS layers panel.

***

## Available fields for pipes

### Model input attributes

| Field         | Description           |
| ------------- | --------------------- |
| `Diameter`    | Pipe diameter (mm)    |
| `Length`      | Length (m)            |
| `Roughness`   | Roughness coefficient |
| `InstallYear` | Year of installation  |

### Simulation results

Available only if there are results loaded in the project:

| Field        | Description                        |
| ------------ | ---------------------------------- |
| `Flow`       | Flow rate (l/s or configured unit) |
| `Velocity`   | Velocity (m/s)                     |
| `HeadLoss`   | Head loss (m)                      |
| `UnitHdLoss` | Unit loss (m/km)                   |
| `FricFactor` | Friction factor                    |
| `ReactRate`  | Reaction rate (quality models)     |
| `Quality`    | Water quality                      |

***

## Result on the map

The tool generates the layer **`ThematicPipes`** within a group of QGISRed thematic layers. The color legend is displayed directly in the QGIS layers panel.

If you run Thematic Maps again, the old layer is replaced with the new settings.

***

## Usage Notes

* The generation of thematic maps does not modify any model data; only the symbology of the layer changes.
* To return to the standard symbology, remove the `ThematicPipes` layer from the layers panel or reload the default symbology from the QGIS layer properties.
* If the project does not have simulation results, the result fields do not appear in the dropdown.
