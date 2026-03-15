# Model Export

QGISRed allows you to export the network model to the EPANET standard **INP** format. This feature is useful for sharing the model with other users, running it directly in the EPANET graphical interface, or integrating it with other hydraulic analysis tools.

To access the export, use the **Export to INP** option from the corresponding QGISRed menu.

### Export Options

When launching the export, the following dialog appears with the available options:

![Export dialog to INP format](assets/images/image69.png)

The options presented by the dialog are:

* **INP file**: Full path of the `.inp` file that will be generated. You can type it directly or use the `...` button to navigate to the desired folder.
* **Export field data files**: If this option is checked, the field data files (auxiliary files associated with the model) will also be exported.
* **Open INP file with EPANET**: If enabled, once the export is complete the INP file will automatically open in the EPANET application installed on your computer.
    * **Epanet path**: Path to the EPANET executable detected on the system. You can select a different version from the dropdown if you have several installed.
    * **Specific Epanet path**: Allows you to manually indicate the path to an EPANET executable that does not appear in the previous list.

Once the options are configured, press the **Export to INP** button to generate the file.