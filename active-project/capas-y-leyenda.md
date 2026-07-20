# Layer Manager and Legend

---

## Layer Manager

**Project bar → Layer manager** (Layer manager)

Controls which project layers are active in QGIS and allows you to recover layers that have been accidentally deleted.

<figure><img src="../assets/images/proyecto/gestor-capas.png" alt="QGISRed Layer Manager Dialog"><figcaption><p>QGISRed Layer Manager Dialog</p></figcaption></figure>
*Layer manager: list of all the layers in the project with their loading status.*

### Base layers (Inputs)

Shows the 6 base elements of EPANET plus the optional layers (Multiple Demands, Sources, Service Connections, Isolation Valves, Meters). For each one, indicate whether it is loaded in QGIS or not.

- **Box checked** → the layer is loaded and visible in the QGIS legend.
- **Unchecked box** → the layer exists on disk but is not loaded.

You can check or uncheck any layer to upload or download it without affecting the data.

### Recover a deleted layer

If you have accidentally deleted a layer from the QGIS legend (or its SHP file on disk), the Layer Manager allows you to **recreate it empty**:

1. Select the missing layer (it will appear with a warning icon).
2. Press **Recover** (or the equivalent button depending on the version).
3. QGISRed creates the empty SHP with the correct field structure and loads it into QGIS.

> ⚠️ Recovery creates the empty layer. The data that was on it (if the SHP was erased from the disk) cannot be recovered unless you have a backup copy.

### Model Summary (Summary)

**Project bar → Summary**

Generate a quick report with the number of elements of each type present in the project:

```
Junctions: 1 243
Pipes: 1 876
Tanks: 3
Reservoirs: 2
Valves: 47
Pumps: 8
```

Useful to verify that the import was complete or to document the size of the model.

---

## Legend Editor

**Project bar → Legend editor** (Legend editor)

Opens a floating panel that allows you to customize the **symbology** of the project layers without having to navigate through the QGIS layer properties menu.

<figure><img src="../assets/images/proyecto/editor-leyenda.png" alt="QGISRed Legend Editor Panel"><figcaption><p>QGISRed Legend Editor Panel</p></figcaption></figure>
*Legend Editor panel: predefined styles and customization of colors and sizes.*

### Predefined styles

QGISRed includes predefined QML styles for each element type, adapted to the project's system of units (SI/US). The editor allows you to apply these styles with a single click:

- Style by **material** (color coding by pipe material)
- Style by **diameter** (color scale proportional to diameter)
- Style by **length**
- **base** style (standard QGISRed colors)

### Manual customization

For each layer you can adjust:
- Fill and border color for point elements
- Color and line thickness for pipes
- Symbol size

The changes are saved in the QGIS project file `.qgz`. If you don't have the `.qgz` saved, the custom styles will be lost when you close QGIS.

> 💡 If you change the version of the plugin and the styles are reset when you open the project, it is normal: QGISRed detects the version change and applies the updated default styles. You can customize again from the Legend Editor.
