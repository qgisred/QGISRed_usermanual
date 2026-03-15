# Hydraulic Sectors

This tool classifies isolated or connected subnetworks based on their supply and demand capacity. It is vital to identify why a part of the model is not receiving water.

### Sector Classification
For each identified sector, QGISRed classifies it into one of these 4 types:

| Type | Description | Supply Status |
| :--- | :--- | :--- |
| **TYPE A** | There is at least one source (reservoir/reservoir) and there are nodes with base demand. | ✅ **Functional**: Knots can be stocked. |
| **TYPE B** | There is a supply source, but there is no demand assigned to the nodes. | ⚠️ **Latent**: Installed capacity but no flow. |
| **TYPE C** | **There are no sources of supply**, but there are assigned demands. | ❌ **Critical Isolated**: There is no water to meet demand. |
| **TYPE D** | There are no sources of supply and there are no assigned demands. | ✅ **Passive**: Hydraulically compatible since it does not require flow. |

### Usefulness of Analysis
This preventive diagnosis allows detecting connectivity errors before launching a long simulation in EPANET, saving time in the diagnosis of "Disconnected Nodes".