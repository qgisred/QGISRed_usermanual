# 🧬 Digital Twin

The **Digital Twin** bus adds to the hydraulic model the infrastructure elements that connect the network with the end user and with the field monitoring systems: connections, shut-off valves, meters and sensors. These elements are not strictly part of the EPANET model but enrich the digital twin with operational and remote reading information.

\*Digital Twin Bar: connections, shut-off valves, meters and field data loading.\*

***

## Digital Twin Bar Tools

### Group 1 — Network elements

| # | Tool                       | Function                                                            |
| - | -------------------------- | ------------------------------------------------------------------- |
| 1 | **Add service connection** | Draw a connection from the main pipe to the customer's supply point |
| 2 | **Add isolation valve**    | Add a shut-off valve by clicking on a pipe                          |
| 3 | **Add meter** (dropdown)   | Place a meter or sensor on a pipe. 11 types available               |

### Group 2 — Operational data

| # | Tool                                                | Function                                                                                                |
| - | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| 4 | **Load meter readings…**                            | Load smart meter readings and associate them with the project connections                               |
| 5 | **Set pipe's initial status from isolation valves** | Propagates the open/close status of the shut-off valves to the `InitStatus` field of the affected pipes |
| 6 | **Load field data…**                                | Import SCADA field data and associate it with the project meters                                        |

### Group 3 — Integration into the model

| # | Tool                                             | Function                                                           |
| - | ------------------------------------------------ | ------------------------------------------------------------------ |
| 7 | **Convert service connections into pipes/nodes** | Converts connections into point nodes or pipes of the EPANET model |

***

## In this section

* [Connections and Shut-Off Valves](service-connections.md) — drawing of connections, shut-off valves and conversion to the hydraulic model
* [Sensors and Meters](sensors.md) — meter types, loading readings and field data
