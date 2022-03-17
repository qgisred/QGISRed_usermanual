# Old versions

### Version 0.14

_QGis versions_: 3.2-3.99

_Features_:

* Fixed major bug when reading metadata from previous models that prevented working with them
* Fixed error when installing the plugin without previously having the necessary dependencies
* Fixed error with the time format in simple control laws
* Display of user-defined decimal separator in the different windows of the plugin
* New tool for editing the geometry of the service connections
* The hydraulic option _Demand multiplier_ now supports a value with decimal places
* Prioritization of DT elements when selecting objects for editing their properties or deleting them

### Version 0.13

_QGis versions_: 3.2-3.99

_Features_:

* New menu to group the tools for the management of Digital Twins.
* Specific button to create service connections and its integration on the global deletion tool.
* Specific tab for editing service connection properties
* Loading demands to service connections or model nodes from automatic meter readings (AMR) in different formats
* Integration of service connection demand patterns into the pattern editor dialog
* New demand manager to complete the import tool from file, with the selective export to file and deletion of the nodal base demands and patterns
* Improved access time to the element properties editor for large networks.
* Opening the INP file with EPANET when exporting it is now optional.
* New options for defining the units and the headloss formula when importing data from GIS
* The loss coefficient converter checks now for declared pipes before launching the converter
* Corrected the format of the time options to allow entering days in addition to hours, minutes and seconds.
* Removal of patterns on multiple demands is now limited to removed demands only
* Corrected date reading from metadata
* Fixed bug that prevented importing SHPs when selecting the same field for different properties
* Fixed bug that caused some SHP fields to be imported without being explicitly selected
* Translated into English some texts that were displayed only in Spanish
* Fixed bug in the graphical selection tools when the QGIS CRS is different from that of the QGISRed data
* Fixed SHPs import error when some feature does not have its geometry declared
* Fixed a display error in result layers

### Version 0.12

_QGis versions_: 3.14-3.99

_Features_:

* Editor of the roughness-material table for the estimation of roughness according to material and age
* New option to import and export patterns/curves in CSV format
* New tool to import base demands at junctions (single or multiple) and its Id patterns from CSV file
* Added import of service connections from SHP
* New tool to obtain the minimum spanning tree of the network
* Updated the Epanet library to version 2.2
* Improved the interface for converting roughness coefficients
* Fixed error when displaying quality results
* Refresh of current units and headloss formula in the status bar when loading a QGis project
* Projects imported from INP are now also displayed in the list of projects
* Fixed error when nodes have no coordinates
* Negative lengths are now avoided when inserting valves or pumps
* Fixed error to access Patterns when TimeStep Pattern is 0:00
* Service connections are now read correctly

### Version 0.11

_QGis versions_: 3.2-3.99

_Features_:

* Created a Json file to define the different projections (.prj file content) in case the Internet is not available
* Implemented the reading of the PUMPS section formats inherited from Epanet version 1.1
* New single installer for both architectures (x86 and x64)
* The units and headloss formula are displayed in the status bar.
* The estimation of roughness coefficients as a function of age and material support different headloss formulas and unit systems
* Conversion of roughness coefficients between different headloss formulas and unit systems
* Tool to create a project backup (manual restoration)
* Fixed error when loading the plugin in QGIS version 3.14.15
* Fixed error for not allowing to express the hours in a format other than AM/PM in the Controls section
* Fixed error when not being able to take the user information from Windows in some computers
* New blue color labels in results for line elements
* Fixed error when cloning the project and losing the metadata
* Fixed error when saving a result scenario and freezing the map
* New alphabetical order in the link and node lists in the Simple Controls

### Version 0.10

_QGis versions_: 3.0-3.14.1

_Features_:

* Fixed not correct behaviour in create/import tools when other layers are open.
* Headers of the INP sections written in English.
* Validation in element properties to prevent same final node in lines.
* Fixed error when importing tanks.
* Improved simplification of vertices to eliminate repetitions at the starting point.
* Fixed error writing the Times of Options.
* Metadata restructuring, now unified in the \*\_Metadata.txt file.
* Fixed error joining pipes with the same characteristics when they start and end in the same node.
* Check for new versions and notify the user.
* Fixed icons display in the legend for QGis version 3.12
* Fixed bug that prevented saving result styles.
* Fixed error in decimal symbol reading when the user uses the English format and changes the decimal symbol by comma.
* EditProject switches to LayerManagement to control visibility of layers and their creation.
* Now the projection is correctly saved in the PRJ file.
* New window with project options.
* Separation between Import (without project - INP or SHPs) and Add data (with project - only SHPs).
* Spatial tolerance when importing/adding data from SHPs.
* Manual includes ascii file format for elevation interpolation and classification of the 4 types of hydraulic sectors.
* Simplified 4 layers of meters in only 1.
* Fixed error when writing SHPs of issues in valves and pumps.
* Methods to assign roughness, check overlapping elements, aligned vertices, lengths, material, diameter or installation date now also for selected elements.
* Fixed error in very specific case when creating individual T-connections.
* New dependency management to avoid errors if they are in use.
* Some improvements on the features already offered in previous versions

### Version 0.9

_QGis versions_: 3.0-3.99

_Features_:

* A new logo for the QGISRed plugin
* Easy creation of pipes, reservoirs and tanks, with snapping tool
* Tool to create (add as you click), move or delete (right click) vertices of links
* Fixed valve/pump orientation when inserted into pipes
* Tool to reverse links (pipes, valves and pumps)
* Tool to split and join pipes
* Tool to join / separate nodes
* Tool to create / undo T connections
* Tool to create / undo pipe crossings
* Tool to move valves and pumps
* Multiple selection of elements from different layers in one step (Ctrl adds, and Shift removes)
* Deletion of all selected elements within a polygonal region
* Removed most of double buttons and replaced by a new option in the dialog window
* New button to access the latest results without running the model again
* Results menu can be expanded and compressed to allow coupling other QGIS windows
* Fixed error when working with long paths
* Some improvements on the features already offered in previous versions

### Version 0.8

_QGis versions_: 3.0-3.99

_Features_:

* Editing properties of the main elements through a dialog window, being able to navigate from it through the different elements contained in the model.
* Insertion/Elimination of valves and pumps in pipes. In the first case, by clicking on a point in the pipe, the pipe will be split or shortened (whichever the case may be) to introduce the new element. In the second case, by clicking on the valve or pump element, it will be eliminated by joining the adjacent pipes if possible.
* Editing the network layout, being able to move nodes of the model so that the rest of the connected elements also move accordingly.
* Rearrangement of all the buttons of the plugin in 5 categories to facilitate the handling of the different options.
* Correction of some bugs as control rules are read.
* Dialogs for editing analysis options and default values.
* Verification of repeated Ids during their generation.
* Hiding of legend data tables (Patterns, Curves, Controls, Rules, Options and Default Values).
* Changes in the results selection menu to show a single variable per node or per line. Reduction of refresh time.
* Option to visualize the value of the chosen parameter for each element by using static labels.
* Elimination of administrator permissions to install the necessary dependencies.
* Some improvements on the features already offered in previous versions.

### Version 0.7

_QGis versions_: 3.0-3.99

_Features_:

* Abstract report with the number of elements of each type, as well as the flow units, the pressure loss formula and if any quality parameter is modeled.
* Modulation Curves Manager: Allows you to edit, create, delete, clone, export and import new patterns. Adds the option to define the pattern type. It also indicates which elements are associated with that pattern. Finally, it includes the functionality of working with real values (depending on the base value associated with the pattern) or with a multiplier or factor (traditional form).
* Curves Manager: Allows you to edit, create, delete, clone, export and import new curves. For curves associated with pumps, in the case of 1 or 3 points, the equation of the approximate curve is specified. The elements associated with these curves are also specified.
* Simple Controls Manager: Allows editing, adding, deleting, cloning and ordering Simple control laws. It includes the option of being able to disable a control law.
* Rules Manager: Allows editing, adding, deleting, cloning and ordering Rules. It includes the option of being able to disable a Rule. You can combine different conditions through the OR and AND operators, as well as select the appropriate combined condition to apply to the Rule.
* In both Controls managers its definition is done interactively and not by typing text (traditional way).

### Version 0.6

_QGis versions_: 2.0-3.99

_Features_:

* Manage QGISRed projects. It is possible to open, create, import, clone or delete projects.
* Create or edit a QGISRed project. It allows to create vector layers (SHPs) of the basic elements that the EPANET software works with. If the user removes any of these SHPs, it is possible to recreate them.
* Data import from INP (EPANET) or SHPs files. In the first format you can import complete models developed with the popular EPANET software. Using SHPs, you can create or complete a model specifying for each type of element, the SHP from which you want to import information and which fields contain certain information needed for the model.
* Validation of the model, informing if there has been any error or warning when processing the information contained in the SHPs.
* Export to EPANET INP file, with the option to open this software once the file is generated.
* Simulation with the EPANET Toolkit to show the hydraulic and quality results.
* Plugin includes a set of tools associated with the layout (elimination of overlapped elements, simplification of aligned vertices, creation of T-type connections, pipe union with the same characteristics or analysis of network connectivity), with the properties of the elements (analysis of lengths, diameters, materials, installation dates, change of state of pipes or elevation interpolation), to add components (connections, hydrants, drains) or to sectorize (hydraulic sectors and demand sectors).
