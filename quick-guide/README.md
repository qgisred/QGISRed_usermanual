# ⚡ Quick Guide

QGISRed integrates into QGIS as a set of **specialized toolbars**. Each bar groups the tools of a stage of the workflow: project management, network editing, verification, simulation, etc.

\*QGISRed main bar: each dropdown button activates/deactivates a toolbar.\*

***

## The main bar

When you install the plugin, a **main bar** appears in QGIS with a drop-down button for each secondary toolbar. Clicking on any of these buttons shows or hides the corresponding bar. In addition, the drop-down menu for each button directly lists all the actions of that toolbar, allowing them to be executed without having the bar visible.

To the right of the main bar is a **units indicator** (for example `LPS | D-W`) that shows the flow units and head loss formula for the active project.

## Toolbars

QGISRed includes **8 toolbars** organized by work area:

| Bar              | Main function                                   |
| ---------------- | ----------------------------------------------- |
| **General**      | Create, open and import projects                |
| **Project**      | Configuration, Layers and Backup                |
| **Edition**      | Draw and edit the hydraulic network             |
| **Debug**        | Verify the quality and consistency of the model |
| **Tools**        | Calculation and data management tools           |
| **Queries**      | Consult, filter and view information            |
| **Analysis**     | Simulate and explore results                    |
| **Digital Twin** | Connections, shut-off valves and sensors        |

> 💡 **TIP**: Activate only the bars you need at any given time to keep the workspace tidy. The visibility status of each bar is automatically saved between sessions.

## The QGISRed project

All network data is stored in a project folder as **SHP + DBF** files. The network name (for example `MiRed`) is the common prefix of all those files (`MiRed_Pipes.shp`, `MiRed_Junctions.shp`, etc.).

QGISRed does not work with the QGIS `.qgz` file as a source of truth: the source of truth is always the project's SHP files. The `.qgz` is optional and is used to save the visual appearance (styles, visible layers, etc.).

***

Check out [Toolbar Summary](toolbars.md) to see what each tool does, or jump straight to [Typical workflow](workflow.md) if you want to get started as soon as possible.
