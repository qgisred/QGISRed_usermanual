# Typical Workflow

This is the usual path to build, verify and simulate a distribution network with QGISRed.

---

## Step 1 — Create or open the project

Use the **General** bar to get started:

- **New project from scratch**: _Create project_ → choose name, folder and reference system. QGISRed automatically generates the 6 base SHPs (Junctions, Pipes, Tanks, Reservoirs, Valves, Pumps).
- **Existing project**: _Project manager_ → double click on the project in the recent list.
- **From an EPANET file**: _Import project_ → select the `.inp`. QGISRed converts it to SHP and opens it.

## Step 2 — Configure project options

From the **Project** bar, access _Project Options_ to define:
- **Flow units** (LPS, GPM, CMH…)
- **Head loss formula** (D-W, H-W, C-M)
- **Quality Model** (None, Chlorine, Age, Tracer)

The indicator on the main bar (`LPS | D-W`) always reflects the active values.

## Step 3 — Build the network

Activate the **Edition** bar and draw the network on the map:

1. Start with the **pipes** — the extreme nodes create themselves.
2. Add **tanks and reservoirs** by clicking on existing nodes.
3. Insert **valves and pumps** by clicking on a pipe.
4. Edit the **properties** of each element (diameter, roughness, dimension, demand...).

> 💡 You can import existing geometry (infrastructure SHP, background orthophoto) and plot the network on top of it.

## Step 4 — Check model quality

Before simulating, use the **Debug** bar:

1. **Consolidate and review data** — detects incomplete or inconsistent attributes.
2. **Verify connectivity** — identifies isolated areas without a pressure source.
3. **Hydraulic sectors** — check the power supply to each sector.

Correct any problems noted in the incident report before continuing.

## Step 5 — Prepare demand data

From the **Tools** bar:

- **Interpolate elevations** if the nodes do not have elevations assigned.
- **Assign roughness** based on material and installation date.
- **Demand manager** to distribute consumption.

## Step 6 — Simulate

From the **Analysis** bar:

1. _Analysis options_ — check the duration and time step.
2. _Run model_ — the simulation can take from one second to several minutes depending on the size of the network.
3. When finished, QGISRed automatically loads the result layers and opens the **Results Viewer**.

## Step 7 — Explore results

In the side panel of the Results Viewer:

- Select which **variable** to show in nodes (Pressure, Demand, Quality) and in pipes (Flow, Velocity, Unit Loss...).
- Move the **time slider** to see the evolution throughout the simulated period.
- Activate **Map Notices** to read values ​​when you mouse over any element.
- Use **Time Series** to graph the evolution of a specific point.

## Step 8 — Save

- _Save Map_ saves the QGIS project (`.qgz`) with the visible layers and styles.
- _Export project_ (from the Project Manager) generates a portable ZIP of the project.

---

> ❗ **IMPORTANT**: QGISRed does not modify the layers while they are in **Edit Mode** of QGIS. Be sure to commit (`Ctrl+S` on the layer) or discard your changes before using any plugin tools.
