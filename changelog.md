# 📜 Changelog

Stay up to date with the latest QGISRed improvements.

### Version 0.19

**User Interface**:

* Grouping of informative options such as News, Incidents, Manual, Rating, Subscriptions and About... in a new Info entry in the main menu.
* Relocation of the Queries menu behind the Tools menu, in the main menu bar.
* Incorporation of a brand and a prefix in the title of all QGISRed panels to differentiate them from others.
* Incorporation of a warning icon in those layers that may become outdated when changes are made to the data.

**Project Manager**:

* Now you can independently change the name of the QGISRed project and the name of the file that houses the map information (qgz).
* When moving a project, you can move the data and the map file (qgz) together, or independently to different folders.
* The option to make a backup of the project has been removed, and has been replaced by the option to Export the project, with more alternatives.
* When exporting a project, you can choose the QGISRed layer groups and the layers outside the project (cartographies, MDT, etc.) to copy, among those present in the layers panel. All of this is saved in a single .zip file.
* To export the map qgz file, it must be in the same project folder or at a higher level. The cartographic information should be in folders parallel to the project folder.
* When importing a QGISRed project, all previously exported information is restored to a new folder, maintaining the structure of all files.

**Import of shapes**:

* Possibility of selecting the candidate pipes to connect the connections that start from the imported consumption points.

**Material tables**:

* Declaration of a different default material table for each of the four supported languages.
* New options in the materials table editing dialog, to copy, load and edit new tables at a global level, before creating a project or from within it.
* New options to choose the desired material table when creating a new project or importing shape files for the first time.

**Layer management**:

* Creation of a new group of layers called AuxiliaryLayers to host complementary themes to the basic themes.
* Creation of a subgroup within the group of Auxiliary Layers, called Demand Builder, to host its own topics: sectors, specific demands and links.
* Adding a new tab to the Layer Manager to create, delete, load or download auxiliary layers linked to the Demand Builder.

**Graphic edition**:

* Wand tapping on a pump, valve, or pipe now toggles only between open and closed states.
* To toggle between the active or closed state of a valve, or declare a CV on a pipe, hold the Ctrl key when wand-clicking.
* When inserting a pump or valve in a section smaller than the separation established between the extreme nodes, they are maintained and no longer move.
* When moving a node no layer is left open, avoiding conflicts with other editing tools.
* Revised the vertex editing tool to make it more user-friendly.
* When splitting a pipe at an intermediate point, the Id is split by adding a numerical suffix. The original Id can be recovered if the sections are merged in the opposite direction to which the intermediate nodes were created.
* When two pipes in series cannot be joined by eliminating the intermediate node, the cause is reported.
* Revised the tool for merging or separating nodes, allowing greater separation between them.
* Creating a T connection now extends the last section of the branch until it intersects with the main pipe.
* Revised the undo T and crosses tools, removing some restrictions and standardizing mouse actions.

**Group property editing**:

* New Edit menu option to edit the properties of group elements.
* Graphical preselection of the elements to modify with multiple selection tools.
* Application of filters to restrict the elements to modify, depending on the type of property.
* Option to display the elements that are going to be modified on the map.
* Multiple options to modify the chosen property, differentiating whether the property is numerical, text or enumerated.
* Preview in the attribute table of the changes made before consolidating them.

**Thematic maps**:

* Incorporation of new thematic maps linked to pipes: Year of installation, age, and roughness coefficient according to loss formula.
* New thematic maps linked to junctions: Elevations and Total Base Demand graduated by size.
* When creating the material map, each material is now assigned its own color based on its abbreviation and language, which is editable.
* When a thematic map becomes outdated due to a change in units or loss formula, a warning icon is displayed and can be updated by clicking on it.

**Legend Editor**:

* Improvements to wizards to automatically create ranges, sizes and colors to set the legend for all layers.
* Possibility of modifying some style parameters of the basic themes of the Data group.
* Incorporation to the QGISRed Legends Editor of the layers created by Queries (thematic maps, hydraulic sectors, trees, etc.).
* Added Results layers to the Legend Editor to customize its style.
* Option to save legends at the project level, or at the user level to apply them to new projects.
* Option to store wizards with which to adapt the legend to the data, instead of saving a preconfigured legend.
* Creation of a QGISRed library of symbols, ramps and color palettes, accessible from the Legend Editor and editable from QGIS.

**Demand Builder**:

* Option to consolidate the imported parameters related to the assignment of demands by sectors in a QGISRed theme.
* Option to distribute global demand or by sectors based on the diameters that converge at the candidate nodes.
* Option to declare consumption by linear sections or by polygons, as an alternative to specific consumption.
* Option to consolidate imported specific consumption in a QGISRed theme.
* Option to manage specific consumption topics and add several demands to the same topic.
* Recognition of various units when declaring the consumption to be imported.
* Option to assign specific demands to the ends of the nearest pipe instead of directly searching for the nearest nodes.
* Option to consider or not the ends of pumps and valves as possible demand nodes.
* Option to distribute specific demands based on the diameters of the pipes that converge at the nodes, or in combination with their distance from the consumption points.
* Notification of loaded nodes that are more than a given distance from consumption points.
* Possibility of editing and reusing links between consumption points and demand nodes.
* Assignment of demands to nodes based on connections declared as elements of the Digital Twin.
* Differentiation of base demands by categories, both in specific consumption and by connections, creating multiple demands at the nodes.
* Option to load demands only from the selected sectors, consumption points or connections.
* Option to use your own theme to assign efficiencies and patterns by sector, import their values and edit them.
* Option to apply hydraulic efficiencies and assign demand patterns by categories.
* Option to readjust efficiencies and patterns declared at one level using those imposed at a higher level (categories -> sectors -> global).

**Statistics panel**:

* New option in the Queries menu to perform all types of statistics with the model data and results.
* Evaluation of the statistics of a magnitude, classified by ranges or classes of said magnitude or another magnitude of the same type of element.
* Ability to use a second classification magnitude to create double entry tables.
* Possibility of applying filters on the starting data and viewing the elements affected by the query on the map.
* Display of statistics in histograms or through an exportable table of values.
* Export of the query configuration and its subsequent import.

**Topology queries**:

* Revised the Connectivity, Hydraulic Sectors and Tree Graphs tools: new names, relocation of layers, style changes, etc.
* New topic to highlight isolated demands in the hydraulic sectors.
* Possibility of creating and managing the existence of several themes for Tree Graphs (now called Minimum Cost Trees).

**Simulation**:

* New progress dialog to show the progress of hydraulic and quality calculations.
* The progress dialog can be paused to carefully observe the progress of the calculations.
* The progress dialog can be omitted for greater speed in calculations, except for networks with long processing times.

**Results panel**:

* Option to show all calculation moments in the results map and other panels in which time intervenes.
* Option to show the moment of the simulation in various formats: time elapsed since the beginning (in accumulated hours or grouped by days) or calendar time (in 24 hour or am/pm format).
* New button bar to perform animations at controlled speed or step by step.
* The variables chosen to display the results of nodes and lines are now highlighted and have their own color assigned.
* New tab with several options to improve the visualization of the results on the map, the symbology and the background color.
* New option to show in a histogram the distribution of the current variable of nodes or lines and their accumulated values, at the current moment.
* New option to show a simplified evolution curve of the current variable of nodes or lines, for the chosen element on the map.
* When rescuing the Results Panel, the options from the last action are preserved, instead of applying the default options.
* When the scenario data is changed, the result layers display a warning icon, which can be updated by clicking on it.

**Evolution graphs**:

* New buttons to navigate the evolution curves graph.
* New button with multiple options to customize the appearance of all the components of the graph.
* Adaptation of the time scale according to the options chosen in the Results Panel.
* Possibility of showing all time moments or only scheduled moments, as chosen in the Results Panel.
* Optional synchronization of the cursor with the current moment of the Results Panel.
* Incorporation of the evolution of the volume of a tank or the overflow flow, as new variables.
* Option to represent the evolution curves of some global variables for the entire system.
* New button to display in a table the numerical values of the passing points of the evolution curves and export their values to a CSV file.
* New button to export graphs as images.
* Option to save and recall evolution chart settings including template creation.
* Ability to create and keep open several evolution curve windows at the same time.

**Languages**:

* All QGISRed menu options, dialogs and messages are now also displayed in French and Brazilian Portuguese, when this language is chosen for the QGIS interface. Currently they are already shown in English and Spanish.

**Other changes**:

* All security controls verified and incidents related to code quality, reported by the QGIS Security Scan system, corrected.
* Checked version 0.19 code for compatibility with Qt6 and QGIS 4.xx.
* End of support for QGISRed libraries on 32-bit (x86) systems. From now on QGISRed will only work on 64-bit systems.
* Removed the minimize and maximize buttons in all dialogs built into the libraries.
* Revised the names of some fields in shape files, dbf tables and CSV files, for uniformity. All identifier fields now end with ID.
* Revised the property names displayed in all QGISRed dialogs, depending on the language, for uniformity.
* Revised the decimals shown in the topic attribute tables, depending on the units used.

**Bug fixes**:

* Review of possible situations when loading GISRed libraries to avoid repeated attempts.
* Review of the export format of INP files to avoid overlaps that caused reading errors.
* Corrected a bug that prevented creating new behavior curves.
* Checking that the identifiers of the elements, curves and patterns do not contain any blank space.
* Corrected an error that prevented consolidating the civil start time of the simulation.
