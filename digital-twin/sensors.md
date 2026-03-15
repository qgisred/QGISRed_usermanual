# Sensors and Telecontrol

Integrate the reality of your network by creating virtual sensors that link field data with the model.

### Types of Sensors
QGISRed allows you to declare:
* **Flow Sensors**: Linked to pipes or valves.
* **Pressure Sensors**: Linked to nodes or tanks.
* **Quality Meters**: To monitor chlorine concentrations or traces.

### Digital Twin Operations
* **Status Transmission**: Before simulating, the plugin can transmit the real state of the manual or cut-off valves so that the hydraulic model reflects the operational reality.
* **Field Synchronization**: Import of real-time (or historical) data from `.dat` files to compare the simulation results with the observed reality (Calibration).