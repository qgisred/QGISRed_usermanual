# Patterns and Curves

**Edition bar → Edit patterns and curves…**

The patterns and curves editor centralizes the management of temporal and functional data that control the dynamic behavior of the model: how demand varies throughout the day, how a pump behaves according to its flow rate, or what is the volume of an irregular tank.

<figure><img src="../assets/images/edicion/editor-curvas.png" alt="QGISRed Pattern and Curve Editor"><figcaption><p>QGISRed Pattern and Curve Editor</p></figcaption></figure>
*Pattern and curve editor: list of elements on the left, graph and data table on the right.*

---

## Demand Patterns

A pattern defines how you multiply a node's base demand (or other parameter) at each simulation time interval.

### Structure of a pattern

Each pattern has:
- A unique **ID** (referenced from the nodes or pumps).
- A list of **multiplier factors**, one per time interval.
- The **time step of the pattern** is defined in the simulation options; If the pattern has fewer factors than simulation intervals, the values ​​are repeated cyclically.

### Example

A pattern of 24 time factors for a 24-h simulation:

```
ID: DomResidential
Factores: 0.4  0.3  0.3  0.3  0.4  0.7  1.1  1.3  1.2  1.0  0.9  0.9
          1.0  1.1  1.0  0.9  1.0  1.2  1.3  1.2  1.0  0.8  0.6  0.4
```

The node with base demand 2.0 L/s and pattern `DomResidential` consumes 0.8 L/s at 0 h (2.0 × 0.4) and 2.6 L/s at 7 h (2.0 × 1.3).

### Editing in dialog

1. Select an existing pattern from the list or press **New** to create one.
2. Enter the factors in the table (one row per interval).
3. The graph updates in real time.
4. You can **import factors from CSV** (a column of numeric values) using the import button.

---

## Behavior curves

The curves relate two physical quantities. EPANET uses four types:

### Pump H-Q curve

It relates the **Manometric Height** (Head, Y axis) to the **Flow** (Flow, X axis). Defines the working point of the pump at nominal speed.

| Number of points | Adjustment method |
|--------------|-----------------|
| 1 point | QGISRed fits the EPANET standard curve: H₀ = 133% of point, given Q₀, Hmax = 0 to 2×Q₀ |
| 3 points | Second degree polynomial fit passing through the three points |
| N points | Linear interpolation between points (free curve) |

> The H-Q curve must have **negative slope** (higher head at lower flow). EPANET will warn if the curve has a positive slope in any section.

### Efficiency curve

Relates **Efficiency** (%) to **Flow** (Flow). It is used for energy consumption analysis. If not defined, EPANET uses the overall project efficiency.

### Volume curve

Relates the **Level** of the tank (m or ft, X axis) to the **Volume** stored (m³ or gallons, Y axis). Necessary for tanks with non-cylindrical geometry (conical basins, irregularly shaped tanks).

### GPV head loss curve

For **GPV** (General Purpose Valve) type valves, relate the **Head loss** (m or ft) to the **Flow** (Flow). It allows modeling any hydraulic control device for which the characteristic curve is known.

---

## Create and edit curves

1. Select the type of curve in the upper selector.
2. Choose an existing curve from the list or press **New**.
3. Enter the pairs of points (X, Y) in the table.
4. The graph shows the resulting curve with the corresponding interpolation or adjustment.
5. Press **OK** to save. The curves are stored in `{Red}_Options.dbf`.

> To reference a curve from a pump or tank, copy its exact **ID** into the corresponding field of the element properties dialog.
