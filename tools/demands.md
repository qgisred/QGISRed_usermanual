# Nodal Demand Management

QGISRed offers powerful tools to distribute water consumption realistically over the network.

### Assignment Methods
* **By Sectors (Polygons)**: Distributes a known total demand in a geographic area among all the nodes contained in said polygon.
* **By Proximity (Points)**: Assigns individual consumption (for example, from a geo-referenced billing database) to the nearest demand node.

### Mass Import and Export
The plugin uses a simple exchange format to manage thousands of requests:

| Field | Description |
| :--- | :--- |
| **IdJunction** | Node identifier in QGISRed. |
| **Base Demand** | Numerical value of consumption. |
| **IdPattern** | (Optional) Identifier of the associated modulation curve. |

* **Format**: CSV file separated by semicolon (`;`) or comma (`,`).
* **Selective Deletion**: Allows you to delete demands for selected nodes and, optionally, clear modulation curves that are no longer used.

---
> 💡 **TIP**:
> You can export the current status of all demands to CSV, edit them in Excel and re-import them to make bulk changes externally.