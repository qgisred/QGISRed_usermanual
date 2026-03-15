# Editing Properties

Accessing and modifying your element data is easy thanks to QGISRed's smart forms.

![Properties Icon](../assets/icons/properties.png)

### The Properties Dialog
When you select an element with this tool, an intuitive window opens that allows you to:
* **Modify attributes**: Change diameters, roughness, demands, etc.
* **Browser**: Quickly navigate to connected items or review recently visited items without closing the window.
* **Center element**: Button to visually locate the selected element on the map.

### Alternative Methods
1. **Attribute Table**: Open the layer table (Pipes, Junctions, etc.) and use the field calculator for bulk edits.
2. **QGIS Identifier**: If you activate "Auto open form" in the native QGIS identifier, the QGISRed form will open when clicked.

---

### QGISRed Specific Data
There are additional fields that are not in EPANET but are vital for the plugin:
* **Material**: The material of the pipe (use the acronym from the materials table).
* **InstalDate**: Installation date in `yyyyMMdd` format (e.g. 20240115).
* **IsActive**: In the Digital Twin, it allows you to enable or disable elements such as connections.