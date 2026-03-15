# Topology and Connectivity Verification

These tools ensure that the physical structure of your network is correct and that there are no errors that prevent the simulation.

### Topology Tools
* **Consolidate Data**: Fundamental process to ensure that all manual changes to attribute tables are correctly synchronized with the plugin's internal model.
* **Overlapping Elements**: Detect and eliminate pipes, nodes, valves or pumps that share exactly the same geographic location, avoiding redundancies.
* **Simplify Vertices**: Eliminates intermediate vertices in straight sections of pipes. This optimizes graphics performance and simplifies the model without altering its length.
* **Pipe Union**: Automatically merges sections of pipe that have identical diameter, material and year of installation, reducing model fragmentation.
* **Type T Connections**: Resolves situations where an end node coincides on the layout of a pipe, dividing it into two and establishing the real connection.

### Connectivity Analysis
This utility identifies which parts of the network are isolated from supply sources.
* **Subzone Detection**: The plugin groups elements into connected subnets.
* **Automatic Cleaning**: Offers the option to automatically eliminate those subzones that have a number of pipes lower than the threshold defined by the user (useful for cleaning topological "garbage" after an import from GIS).