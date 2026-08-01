# Toolbar Summary

An overview of everything QGISRed can do, organized by toolbar.

---

## 🗂️ General — Project Management

Entry point for any work session. From here you create, open or import projects.

| Tool | What does it do |
|-------------|----------|
| **Project Manager** | Recent projects list, clone, rename, delete |
| **Open project** | Open an existing project indicating name and folder |
| **Create project** | Generate the SHP file structure for a new network |
| **Import project** | Create a project from an EPANET `.inp` file or external SHPs |

---

## 📋 Project — Settings and layers

Open project management tools.

| Tool | What does it do |
|-------------|----------|
| **Summary** | Shows the number of elements of each type in the network |
| **Add data by import** | Import additional elements to the already opened project |
| **Layer Manager** | Controls which layers are active; recover accidentally deleted layers |
| **Legend Editor** | Customize the symbology of any layer in the project |
| **Project Options** | Configure EPANET options: units, loss formula, quality |
| **Default values** | Defines ID prefixes, geometric tolerances and initial hydraulic values ​​|
| **Table of materials** | Manage the list of materials with their initial roughness and age increments |
| **Save map** | Save the QGIS project (`.qgz`) |
| **Close project** | Close the current project |

> 💡 The export of the project (ZIP portable) is no longer in this bar: it is done from the **Export** button of the Project Manager (see [Save, Export and Close Project](../active-project/save-export-close.md)).

---

## ✏️ Edition — Network creation and editing

Tools to draw and modify the network topology directly on the map.

| Tool | What does it do |
|-------------|----------|
| **Add Pipe** | Draw a pipe; automatically creates extreme knots |
| **Add tank** | Convert an existing node into a Tank |
| **Add reservoir** | Converts an existing node into a reservoir (Reservoir) |
| **Insert valve** | Split a pipe and insert a valve |
| **Insert pump** | Split a pipe and insert a pump |
| **Select elements** | Multiple selection of knots and lines |
| **Move knots** | Move a knot by dragging it; maintains connectivity |
| **Edit vertices** | Add, move or delete intermediate vertices of a pipe |
| **Reverse link** | Change the reference flow direction in pipes/valves/pumps |
| **Split / Join pipes** | Split a pipe at one point or join two consecutive pipes |
| **Split / Merge knots** | Separate a knot into two or merge overlapping knots |
| **Create / Revert T** | Create or break a tee connection over an existing pipe |
| **Create/Revert crossover** | Manage crossovers between geographically overlapping pipes |
| **Move valve / pump** | Reposition a valve or pump to another pipe |
| **Change status** | Modifies the initial state (Open/Closed/CV) of pipes, valves and pumps |
| **Delete items** | Delete selected elements and rebuild connectivity |
| **Edit properties** | Open the attributes form of an element |
| **Patterns and curves** | Manage demand, efficiency and head-flow curves |
| **Controls and rules** | Define simple controls and condition-based rules |

---

## 🐛 Debug — Verification and debugging

Tools to ensure the topological and attribute integrity of the model.

| Tool | What does it do |
|-------------|----------|
| **Consolidate and review data** | Verify and consolidate all attributes; generates an incident report |
| **Remove overlapping elements** | Detect and delete duplicate pipes or nodes in the same position |
| **Simplify link vertices** | Eliminates redundant vertices in straight sections |
| **Join consecutive pipes** | Merges adjacent pipes with the same diameter, material and year of installation |
| **Create T connections** | Create connection nodes where pipes intersect without a common knot |
| **Verify connectivity** | Analyze network connectivity and identify isolated areas |
| **Eliminate isolated areas** | Deletes subzones without connection to any pressure source |
| **Check lengths** | Detects pipes that are too short or long with respect to the defined thresholds |
| **Check diameters** | Check that the diameters are within valid ranges |
| **Check materials** | Detects pipes without assigned material |
| **Check dates** | Check consistency in installation dates |
| **Hydraulic sectors** | Calculates and visualizes the network sectors (H-Q, H-nQ, nH-Q, nH-nQ) according to their relationship with sources and demand nodes |

---

## 🔧 Tools — Calculation tools

Utilities to automate model preparation and management tasks.

| Tool | What does it do |
|-------------|----------|
| **Calculate lengths** | Recalculate the lengths of the pipes from their geometry |
| **Interpolate dimensions** | Assigns dimensions to the nodes from an MDT in `.asc` format |
| **Assign roughness** | Calculate the roughness coefficient based on the material and age |
| **Convert roughness** | Transform the roughness coefficients between formulas (D-W ↔ H-W ↔ C-M) |
| **Claim Manager** | Distribute consumption between nodes from area polygons or georeferenced points |
| **Scenario Builder** | Export and import model parameters (roughnesses, demands, dimensions, states, qualities) in bulk to manage variants without duplicating projects |
| **Isolated segments** | Calculate the segments that would be isolated when each shut-off valve is closed |
| **Demand sectors** | Generates sectors based on demand and consumption patterns |
| **Minimum cost tree** | Calculates the spanning tree of minimum hydraulic resistance from a selected source node |

---

## 🔍 Queries — Consultations

Model query and inspection tools without modifying its data.

| Tool | What does it do |
|-------------|----------|
| **Search item by ID** | Locate and select any element based on its identifier |
| **Element properties** | Shows all the properties of an element when you click on it |
| **Thematic maps** | Generate thematic display layers by any numeric attribute |
| **Property inquiries** | Filters elements that meet conditions on their attributes |
| **Statistics** | Calculates descriptive statistics of any numeric field |

---

## 📊 Analysis — Simulation and results

Tools to run hydraulic simulation and explore the results.

| Tool | What does it do |
|-------------|----------|
| **Run model** | Launch the EPANET simulation and load the results as layers |
| **Results viewer** | Open the side panel to explore variables over time |
| **Status Report** | Displays the text report generated by EPANET |
| **Analysis options** | Configure hydraulics, quality, times and energy |
| **Time series** | Graphically represents the temporal evolution of an element |
| **Export results** | Export all results to CSV files |
| **Export to INP** | Generates an EPANET compatible `.inp` file |

---

## 🧬 Digital Twin — Digital Twin

Advanced elements to represent the real network infrastructure.

| Tool | What does it do |
|-------------|----------|
| **Add connection** | Create a service connection from the network to a point of consumption |
| **Add shut-off valve** | Incorporates manual sectioning valves into the network |
| **Add meter** (submenu) | Add different types of sensors: flowmeter, pressure gauge, counter, level, quality, energy, status, opening, tachometer |
| **Load readings** | Import real sensor readings for calibration or comparison |
| **Initial state from valves** | Applies the real state of the shut-off valves as the initial state of the model |
| **Load field data** | Import georeferenced data from capacity campaigns |
| **Convert connections** | Transform the connections into pipes and demand nodes of the model |
