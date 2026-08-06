# Connections and Shut-Off Valves

The connections and cut-off valves are the two elements that connect the hydraulic model with the operational reality of the network: the connections represent the individual connection with each client and the cut-off valves allow the isolation of sectors to be modeled without the need to modify the topology of the EPANET model.

---

## Add service connection

**Digital Twin Bar → Add service connection**

Draws a drop as a polyline from the main pipe to the customer's delivery point. The connection is stored in the complementary layer `ServiceConnections` of the project.

<figure><img src="../assets/images/gemelo-digital/add-service-connection.png" alt="Connection drawing tool on the map"><figcaption><p>Connection drawing tool on the map</p></figcaption></figure>
*Service drawing: the line starts from the main pipe and reaches the client's plot boundary.*

### Process

1. Activate **Add service connection**. The cursor changes to line drawing mode.
2. Click on the main pipe at the intake point.
3. Click on the intermediate points of the trace if the connection is not straight.
4. Double click on the end point (plot boundary or counter) to complete the layout.
5. QGISRed calls the C# engine (`GISRed.AddConnection`) and updates the `ServiceConnections` layer.

The connection automatically inherits the closest connection node from the main network. The `IsActive` field of each connection allows the supply to be activated or deactivated individually without deleting the element.

---

## Add isolation valve

**Digital Twin Bar → Add isolation valve**

Add a manual shutoff valve to an existing pipe by clicking on it. The cut-off valves are stored in the complementary layer `IsolationValves` and are not EPANET elements: they do not appear in the simulation but they do appear in the analysis of isolated segments (**Isolated segments**, Tools bar).

### Process

1. Activate **Add isolation valve**.
2. Click on the pipe at the point where you want to place the valve.
3. QGISRed inserts it into the `IsolationValves` layer and represents it on the map.

### Relationship to simulation

Shutoff valves alone do not modify the EPANET model. To have its status (open/closed) affect the simulation, use the **Set pipe's initial status from isolation valves** tool in Group 2.

---

## Convert service connections into pipes/nodes

**Digital Twin Bar → Convert service connections into pipes/nodes**

Incorporates the connections drawn in `ServiceConnections` to the active EPANET model. Requires that layer `ServiceConnections` exists and contains at least one connection.

### Conversion options

When you run the tool, a dialog appears with two options:

| Option | Result in the model |
|--------|------------------------|
| **As nodes** | Each connection becomes a point demand node at the connection point with the main pipeline. The geometry of the connection does not enter the model. |
| **As pipes** | Each connection becomes a small diameter pipe that goes from the intake node to a new final node. Allows you to simulate losses in the client connection. |

### When to use each option

- **As nodes**: when the only interest is to incorporate the customer's demand into the model without simulating the internal losses of the connection. It is the usual option for distribution networks at the neighborhood or city scale.
- **As pipes**: when you want to simulate subscriber networks with real connection diameters, or when the length of the connection is significant with respect to the main network.

> This operation modifies the EPANET model (layer `Junctions` and/or `Pipes`). Save the project before running it if you want to keep the previous state.
