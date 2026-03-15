# Connections and Individual Demand Management

The QGISRed Digital Twin allows you to model the network down to the individual client level using connections.

### Connection Modeling
* **Geometric Drawing**: You can manually draw connections from the main pipe to the plot boundary.
* **Autocompletion**: Tool to automatically generate the section perpendicular to the nearest pipe from a supply point.
* **IsActive Field**: Allows you to quickly simulate the loss or outage of supply to specific users.

### Connection Conversion
The connections in QGISRed can be treated in two ways in the final hydraulic model:
1. **Point Node**: The demand is assigned directly to the connection node.
2. **Linear Section**: The connection becomes a small diameter pipe, allowing the pressure losses in the customer connection to be simulated.

### Remote reading (Smart Metering)
QGISRed supports smart meter data integration. The formats allowed to import time series are:
* **Table Format**: `Time; Id1; Id2; ...` (Columns per counter).
* **Series Format**: `Id; Time; Demand` (One record per row).

---
> 💡 **TIP**:
> You can export all the accumulated remote reading data to a single CSV file for external analysis.