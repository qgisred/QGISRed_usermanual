# Topology and Connectivity

The tools in the first group of the Debug bar detect and correct the most common structural errors: duplicate elements, unnecessary vertices, fragmented pipes and disconnected areas. It is advisable to run them in the order they appear on the bar before simulating for the first time.

---

## Check && commit data

**Debug bar → Check && commit data**

It is the main validation tool. It goes through all the elements of the project, checks the consistency of the data (dimensions, diameters, duplicate IDs, references to non-existent curves and patterns, etc.) and **consolidates pending changes**.

### What is valid

- Duplicate IDs on any layer.
- Pipes without valid end nodes (broken connectivity).
- References to curves or patterns that do not exist in the project.
- Empty mandatory values ​​(null diameter, empty dimension...).
- Internal consistency of file `_Options.dbf`.

### Result

- If everything is valid: message _"Input data is valid"_ in green.
- If there are errors: list of problems with the ID and type of the affected element. Items with errors are automatically selected on the map to make them easier to locate.

> Run **Check && commit data** whenever you have edited the attribute table manually (outside of the properties dialog), since those changes do not go through the plugin's automatic validation.

---

## Remove overlapping elements

**Debug bar → Remove overlapping elements**

Detects elements that share exactly the same geographic position: nodes on nodes, pipes on pipes, or nodes on the end of another layer.

### When duplicates appear

- When importing from a `.inp` with rounded coordinates.
- When combining data from different GIS sources.
- When copy-pasting elements without checking overlap.

### Operation

The tool operates on the current selection or on the entire network if there is no selection. Eliminates the duplicate element, keeping the one with the most connections or, in case of a tie, the one with the lowest ID. The attributes of the removed element are discarded.

> Run this tool **before Create T connections** and **before Check connectivity** to avoid false connectivity positives caused by duplicate nodes.

---

## Simplify link vertices

**Debug bar → Simplify link vertices**

Removes intermediate vertices that are aligned (within an angular tolerance threshold) with adjacent segments. These vertices do not provide geometric information but increase the size of the SHP and slow down the rendering.

### When is it useful

- After importing from AutoCAD or municipal GIS where the lines have vertices every few centimeters.
- After using external smoothing tools that add unnecessary points.

### What preserves

Vertices at actual break points (change of direction) are not removed. Only those that fall on the extension of the anterior segment, within the internal tolerance angle of the plugin, are eliminated.

---

## Join consecutive pipes

**Debug bar → Join consecutive pipes (= diameter, material and year)**

Merge adjacent pipes when they share **all three attributes**: diameter, material and year of installation. The intermediate node is removed if it is not in demand or connected to other layers.

### Result

Pipes that were previously fragmented (by import from GIS, by previous divisions or by incremental design) are merged into a single section. This:
- Reduces the number of elements in the model.
- Simplifies the attribute table.
- Improves simulation performance.

> If the intermediate node has non-zero assigned demand, the pipeline is **not** merged. QGISRed preserves the node so as not to lose consumption data.

---

## Create T connections

**Debug bar → Create T connections**

Automatically detects situations where the end of a pipe (or a demand node) falls on the route of another pipe, without being connected to it. In those cases, the plugin splits the pipe and creates the joining node.

### Problem it solves

When digitizing networks by hand, it is common for a branch to be left "floating" above the main without connecting topologically. Visually it seems correct, but in the simulation that branch has no real connection. This tool detects and fixes it automatically.

### Tolerance

Uses the node tolerance configured in **Project Bar → Default Values**. If the end of the pipe is less than that distance from the axis of another pipe, it is considered a tee to solve.

---

## Check connectivity

**Debug bar → Check connectivity** *(with Delete isolated subzones sub-option)*

Analyzes the connectivity of the entire network from the supply sources (Reservoirs and Tanks). Identify which pipes and nodes are **not connected** to any source.

<figure><img src="../assets/images/debug/check-connectivity.png" alt="Check connectivity result: isolated areas colored in red on the map"><figcaption><p>Check connectivity result: isolated areas colored in red on the map</p></figcaption></figure>
*Isolated areas identified: in red the elements without connection to any source.*

### Option 1: Check connectivity (display only)

Color the elements according to their connectivity zone. Items not connected to any source are highlighted. It does not modify the network.

### Option 2: Delete isolated subzones

Opens a dialog that asks for the **maximum number of pipes** in a subzone to delete. Subzones with that number of pipes or less are automatically deleted. The largest ones are preserved even if they are isolated (they may be valid sectors not yet connected).

This threshold is useful for cleaning up topological "junk" — fragments of 1-3 pipes left loose after an import.

> Always run **Remove overlapping elements** before **Check connectivity** to prevent duplicate nodes from generating false isolations.
