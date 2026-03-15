# Patterns and Curves

Manages the dynamic behavior of demands, pumps and tanks.

![Curves Icon](../assets/icons/curves.png)

### Modulation Curves (Patterns)
Defines how a parameter (usually demand) varies over time.
* **Types**: Volume, time or multiplying factors.
* **Edit**: You can add factors one by one or import entire series from CSV files.
* **Association**: In the demand node, make sure to put the pattern ID in the `IdPattern` field.

### Behavior Curves
Defines the physical relationship between two variables.
* **Pumps (Pump Curves)**: Relationship between Flow and Head. QGISRed allows you to define 1-point or 3-point curves, calculating the approximate equation automatically.
* **Deposits (Efficiency/Volume Curves)**: Relationship between level and volume for deposits with irregular shapes.