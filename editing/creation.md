# Element Creation

The first five tools on the Edition bar allow you to add elements to the network. They all activate an **interactive editing mode**: the cursor changes and the plugin waits for an action on the map. To cancel without creating anything, press the same button again or press `Esc`.

---

## Add pipe

**Edition bar → Add pipe**

Line drawing mode: Each click adds a vertex to the pipe. The tool remains active until you finish the layout.

<figure><img src="../assets/images/edicion/add-pipe.png" alt="Add pipe tool in action on the QGIS map"><figcaption><p>Add pipe tool in action on the QGIS map</p></figcaption></figure>
*Drawing a pipe: The temporary red line follows the cursor until the next click.*

### Process

1. Activate the tool. The cursor changes to drawing mode.
2. Click to set the **start point**. QGISRed automatically creates a junction at that point if none exists within the tolerance radius.
3. Click to add **intermediate vertices** (path break points).
4. **double click** or press the **right button** to finish the pipeline. QGISRed creates a second node at the end point.

### What QGISRed creates when confirming

- A record in `{Red}_Pipes.shp` with the geometry drawn.
- Up to two new nodes in `{Red}_Junctions.shp` (one per end), if a node did not already exist within the configured tolerance.
- The diameter, roughness and demand values ​​are taken from the **Default Values** of the project.

### Connect to existing elements

If the start or end point falls within the tolerance of an existing node, valve, pump, tank or reservoir, the new pipe **connects to that element** instead of creating a new node.

> Setting to the nearest node uses the tolerance configured in **Project Bar → Defaults → Node Tolerance**. You can review or change it before drawing dense networks.

---

## Add tank

**Edition bar → Add tank**

Place a Tank on the map. Tanks have a variable level and participate in the hydraulic simulation.

### Process

1. Activate the tool. The cursor shows the tank icon.
2. Click on an **existing node** or on an empty point on the map.
- If you click on an existing node, that node **becomes** a Tank.
- If you click on an empty point, QGISRed creates a new Tank (no initial connection; you will need to connect it with a pipe).
3. QGISRed opens the properties dialog of the new tank so you can enter the data (bottom elevation, initial level, minimum level, maximum level, diameter).

### Main tank parameters

| Parameter | Description |
|-----------|-------------|
| **Elevation** | Tank bottom elevation (m or ft) |
| **InitLevel** | Initial water level above bottom |
| **MinLevel** | Minimum operating level |
| **MaxLevel** | Maximum operating level |
| **Diameter** | Tank diameter (for circular section); if you use volume curve, put 0 |
| **MinVol** | Minimum volume (optional) |
| **VolCurve** | Volume curve ID (for non-cylindrical geometry) |

---

## Add reservoir

**Edition bar → Add reservoir**

Place an external reservoir or feeding point (Reservoir). Unlike the Tank, the Reservoir has **fixed level** (constant piezometric head) and represents a water source of unlimited capacity.

The process is identical to that of the tank. The parameters are simpler:

| Parameter | Description |
|-----------|-------------|
| **Head** | Fixed piezometric load (free water level elevation, m or ft) |
| **Pattern** | Load variation pattern over time (optional) |

> Use reservoirs to represent high water delivery points (connections with external systems) or constant flow supply points.

---

## Insert valve in pipe

**Edition bar → Insert valve in pipe**

Insert a valve into an existing pipe. The original pipe is **divided into two sections** that are connected through the valve.

<figure><img src="../assets/images/edicion/insert-valve.png" alt="Result of inserting a valve: the original pipe is divided into two"><figcaption><p>Result of inserting a valve: the original pipe is divided into two</p></figcaption></figure>
*The original P-12 pipe is divided into P-12 and P-13, with valve V-1 between them.*

### Process

1. Activate the tool. The cursor changes to the valve icon.
2. Click on the pipe where you want to insert the valve.
3. QGISRed determines the exact insertion point (projection of the click on the axis of the pipe) and:
- Create a node at that point.
- Divides the original pipe into two sections with the same diameter and material attributes.
- Create the valve between the two new ends.
4. The properties dialog opens to configure the valve type and setting.

### Available valve types

| Type | Name | Function |
|------|--------|---------|
| **PRV** | Pressure Reducing Valve | Reduces downstream pressure to setpoint |
| **PSV** | Pressure Sustaining Valve | Maintains upstream pressure at setpoint |
| **PBV** | Pressure Breaker Valve | Produces a fixed head loss |
| **FCV** | Flow Control Valve | Limits the flow to the setpoint |
| **TCV** | Throttle Control Valve | Simulates a partially closed valve using a loss coefficient |
| **GPV** | General Purpose Valve | Head loss defined by a custom curve |

---

## Insert pump in pipe

**Edition bar → Insert pump in pipe**

Insert a pump into an existing pipe, splitting it exactly the same as with valves.

### Process

1. Activate the tool and click on the pipe.
2. QGISRed divides the pipe and creates the pump between the two resulting sections.
3. The properties dialog opens to configure the H-Q curve and initial velocity.

### Pump parameters

| Parameter | Description |
|-----------|-------------|
| **Curve** | H-Q Curve ID (required to simulate) |
| **Speed** | Initial speed factor (1.0 = nominal speed) |
| **Pattern** | Speed ​​variation pattern |
| **Power** | Constant power (alternative to H-Q curve) |

> If the pump requires an efficiency curve for energy calculation, define it in the **Pattern and Curve Editor** and reference it from the pump properties.
