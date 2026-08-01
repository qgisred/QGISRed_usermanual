# Previous Versions

Here you can check the detailed change history of previous versions of QGISRed.

### Version 0.16
**QGis Versions**: 3.2-3.99

**Features**:
* New options in the nodal demands manager to declare consumption for the entire network or by zones.
* Possibility of exporting, editing and reimporting the links between specific consumption and nodes.
* New options to import/export/delete demand scenarios by categories.
* New tools in the nodal demands manager to consider water efficiency or assign consumption patterns by sectors.
* New Scenario Manager to store and retrieve various model parameters in bulk.
* Automatic calculation of pipe length from vertex coordinates.
* Automatic completion of the connection layout using a section perpendicular to the nearest pipe or a link to the nearest node.
* Possibility of automatically tracing connections of preset length from a point on a pipe or a node.
* New option to reflect a rush with the invest tool.
* New option to import connections as points, creating perpendiculars to the pipes or connections to the closest nodes.
* New IsActive field in connections to define whether it is operational or not.
* Verification of the contact point of a connection with a pipe or knot at both ends.
* Before calculating the hydraulic sectorization, the status of the manual valves is now transmitted.
* When exporting to INP the loss coefficient of the shut-off valves is transmitted to the pipes.
* Declaration, editing and deletion of meters of various types, as new elements of the Digital Twin.
* Editing, reading and saving the signals associated with the meters.
* New dialog to read field data and export to CSV those corresponding to the simulation interval.
* New option to export field data, together with the INP file.
* New fields in the import dialog to import more item information.
* New option to show in the auxiliary themes the elements with an incident during the import.
* New buttons and new slider in the results panel.
* Improvements in labels to display results.
* New type of result to display the Status of the lines.
* Improvements in searches from the property editor.
* Dropdown with EPANET executable paths when exporting INP for automatic opening.
* Sorting patterns by type when importing INP.
* New warning when the Id of some element is autocompleted.
* Changes to toolbar order, names and icons, and visual styles.
* New link to the QGISRed website in the info window.

**Corrections**:
* Corrected the reading and editing of the curve Id in GPV valves.
* Corrected error when assigning default values ​​when importing reaction coefficients.
* Corrected error and message when reading polluting sources in tanks and reservoirs.
* Corrected problem with specific selection tools.
* Fixed error in mass creation of T connections.
* Fixed errors in multiple and polygon selection with different CRS.
* Fixed bug with snapping in QGIS 3.26.

---

### Version 0.15
**QGis Versions**: 3.2-3.99

**Features**:
* Manual valve management (import, creation, deletion, editing properties, interaction with the status of the pipes...).
* New tool to change the state of linear elements and manual valves.
* New symbolization of pipes, pumps, regulation valves and manuals according to their status.
* Cancellation of isolated demands due to the closure of overlapping pipes or valves during simulations.
* Assignment of demands to nodes based on demand sectors and specific demands, with various options.
* Improvements in the properties editing window (multiple selection, connected elements, visited elements, center selected element).
* Review and expansion of analysis options (hydraulics, quality, times and energy).
* Incorporation of the new Epanet 2.2 parameters to the forms (tank overflow, pressure-dependent demands).
* Highlighted main toolbar buttons/menus.
* Default and only language is English (for now).
* Improved rules editing (with times and clocktimes).

**Corrections**:
* Fixed error when writing demand values ​​with more than 4 digits.
* Fixed bug with time labels for selecting results.
* Corrected error when converting numbers in dimension interpolation.
* Corrected errors with reading, writing and order of the rules.
* Fixed error with rules using comma as decimal separator.
* Corrected problem when assigning the project projection.
* Fixed error when editing properties working with raster layers.

---

### Version 0.14
**QGis Versions**: 3.2-3.99

**Features**:
* **Corrected serious error** when reading metadata from previous models that prevented working with them.
* Fixed error when installing the plugin without having previous dependencies.
* Fixed error with time format in simple control laws.
* User-defined decimal separator display.
* New tool to edit the geometry of the connections.
* The hydraulic option `demand multiplier` now supports decimals.
* Priority of Digital Twin elements when selecting objects.

---

### Version 0.13
**QGis Versions**: 3.2-3.99

**Features**:
* New menu to group Digital Twin tools.
* Creation of connections with own tool and integration in deletion.
* Specific tab to edit connection properties.
* Remote reading upload under different formats to connections or nodes.
* Incorporation of connection modulation curves to the general editor.
* New demand manager for import/export and selective deletion.
* Improved access times to properties on large networks.
* Optional opening of INP in EPANET after exporting.
* New options to define units and pressure loss formulas from GIS.
* Corrected time format to allow days.
* Corrected reading of dates in metadata and various SHP import errors.

---

### Version 0.12
**QGis versions**: 3.14-3.99

**Features**:
* Edition of the materials-roughness table for calculation according to material and age.
* New import and export of patterns/curves in CSV format.
* Import of base demands and curve IDs from CSV.
* Import of connections from SHP.
* New tool to obtain the tree of minimum resistance.
* Update of the Epanet library to **version 2.2**.
* Improved the roughness coefficient conversion interface.
* Bug fixes in quality results and knots without coordinates.
* Insertion of valves/pumps avoiding negative lengths.

---

### Version 0.11
**QGis Versions**: 3.2-3.99

**Features**:
* Local JSON file for projections (.prj) without internet.
* Reading PUMPS formats inherited from Epanet 1.1.
* New single installer (x86 and x64).
* Display of units and loss formula in status bar.
* Roughness estimation by age/material compatible with various formulas.
* Tool to create backup copy of the project.
* Bug fixes in QGIS 3.14.15 and AM/PM time format.

---

### Version 0.10
**QGis Versions**: 3.0-3.14.1

**Features**:
* Writing INP headers in English.
* Validation to prevent the same final knot in lines.
* Simplification of duplicate vertices in initial points.
* Unification of metadata in file `_Metadata.txt`.
* Notice of new versions available.
* Layer visibility control using `LayerManagement`.
* Separation between Import (without project) and Add (with project).
* Spatial tolerance when adding data from SHPs.
* Manual includes ASCII format for interpolation and classification of hydraulic sectors.

---

### Version 0.9
**QGis versions**: 3.0-3.99

**Features**:
* New QGISRed logo.
* Agile creation of pipes, tanks and reservoirs with anchoring.
* Path editing (move, create, delete vertices).
* Line orientation inversion.
* Tools for splitting/joining pipes and knots.
* Creating/undoing T-connections and crossovers.
* Displacement of valves and pumps.
* Multiple selection (Ctrl adds, Shift removes) and delete per polygon.
* Access to latest results without simulating again.

---

### Version 0.8
**QGis versions**: 3.0-3.99

**Features**:
* Editing properties through a dialog window with a browser.
* Intelligent insertion/removal of valves and pumps in pipelines.
* Editing the layout by moving nodes and coincident elements.
* Support for 5 tool categories.
* Dialogs for calculation options and default values.
* Verification of repeated IDs.
* Hiding data tables in the legend.
* Visualization of results using fixed labels.

---

### Version 0.7
**QGis versions**: 3.0-3.99

**Features**:
* Model summary table.
* Modulation Curves Manager (Patterns): edit, create, clone, export/import.
* Behavior Curve Manager: support for 1 or 3 points with approximate equation.
* Simple and Interactive Controls Manager.
* Rules Manager: interactive combination of OR/AND conditions.

---

### Version 0.6
**QGis versions**: 2.0-3.99

**Features**:
* Project management (open, create, import, clone, delete).
* Creation of SHP vector layers for EPANET base elements.
* Import of data from INP or SHPs.
* Model validation and bug reporting.
* Export to INP with optional automatic opening.
* Simulation with EPANET Toolkit.
* Layout tools (elimination of overlaps, connectivity, sectors).
