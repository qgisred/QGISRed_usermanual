# Advanced Editing Tools

QGISRed offers precise tools to manipulate the geometry and state of your network without breaking the topology.

### Graphic Manipulation

#### Vertex Editing
Allows you to adjust the actual layout of pipes and other linear elements:
* **Move**: Drag any intermediate vertex.
* **Create**: Click anywhere on the stretch to add a break point.
* **Delete**: Right-click on a vertex to delete it.

#### Move Knots
This tool moves a node (Junction, Tank, Reservoir) and drags all the connected elements with it (pipes, valves, pumps) keeping the network together.

---

### Network Tools (Net Tools)

| Tool | Action |
| :--- | :--- |
| **Invest** | Changes the orientation of a line (affects the direction of positive flow). |
| **Split/Join Pipe** | Splits a pipe in two or joins two sections with identical properties (diameter, material, age). |
| **Split/Join Knot** | The joining process is two by two (origin -> destination). Split (right button) separates connected lines into individual nodes. |
| **T Connections** | Creates or breaks joins where a connectivity node 1 coincides on a pipe. |
| **Pipe Crossings** | Merge or separate pipes that intersect on the map. |
| **Move Valves/Pumps** | Moves an element from one pipe to another while maintaining its properties. |
| **Change Status** | Toggles the status (Open/Closed) of pipes and manual valves. |

> 💡 **NOTE**:
> If a pipe has a manual valve, the state change must be made on the valve, not on the pipe.