# Sensors and Meters

The Digital Twin meters and sensors are elements that record physical magnitudes at specific points in the network. QGISRed stores them in the complementary layer `Meters` and uses them to load field data and compare it with the simulation results.

***

## Add meter (dropdown)

**Digital Twin Bar → Add meter**

Place a meter or sensor on a pipe by clicking on the installation point. The button drop-down menu allows you to choose the type before placing it; The last type used remains as the default action of the button.

\*Add meter drop-down: the 11 meter types available.\*

### Available meter types

| Type                       | Name on the bar            | Recorded magnitude                                |
| -------------------------- | -------------------------- | ------------------------------------------------- |
| **Automatic meter**        | Add automatic meter        | Type automatically determined by context          |
| **Manometer**              | Add manometer              | Pressure (m.c.a.)                                 |
| **Flowmeter**              | Add flowmeter              | Flow rate (l/s or configured unit)                |
| **Countermeter**           | Add countermeter           | Accumulated volume (water meter)                  |
| **Sensor level**           | Add level sensor           | Free sheet level in tank                          |
| **Differential manometer** | Add differential manometer | Pressure difference between two points            |
| **Quality sensor**         | Add quality sensor         | Chlorine concentration or other quality parameter |
| **Energy sensor**          | Add energy sensor          | Power or energy consumed (pumping groups)         |
| **Sensor status**          | Add sensor status          | Operational status of a pipe or valve             |
| **Valve opening**          | Add valve opening          | Degree of opening of a regulating valve           |
| **Tachometer**             | Add tachometer             | Speed ​​of rotation of a pump (rpm)               |

### Process

1. Choose the type of meter from the drop-down menu.
2. Click on the pipe at the installation point.
3. QGISRed calls `GISRed.AddMeter` with the selected type and updates layer `Meters`.

***

## Load meter readings…

**Digital Twin Bar → Load meter readings…**

Imports smart meter readings (smart metering) and associates them with the project connections. The readings enrich the model demands with actual consumption data rather than estimated demands.

### Supported import formats

| Format     | File structure                                                               |
| ---------- | ---------------------------------------------------------------------------- |
| **Table**  | First row: header with `Time; Id1; Id2; …`. Columns: one counter per column. |
| **Series** | One row per record: `Id; Time; Demand`. All counters in the same file.       |

Field separators are automatically detected from the regional system. The `Time` field accepts both absolute timestamps and offset in hours from the start of the simulation.

***

## Set pipe's initial status from isolation valves

**Digital Twin Bar → Set pipe's initial status from isolation valves**

Propagates the opening or closing state of the cut-off valves from the `IsolationValves` layer to the `InitStatus` field of the pipes that pass through each valve. Thus, the EPANET model collects the real state of the network without the need to manually modify each pipe.

### Requirement

The `IsolationValves.shp` layer must exist in the project directory. If it does not exist, the tool displays a warning and does not make any changes.

### When to use it

* Before simulating a specific operational scenario (for example, with a sector closed for maintenance).
* After updating the status of several cutoff valves on the map and before running **Run model**.

> This operation does modify the EPANET model (field `InitStatus` of `Pipes`). To return to the original state, use **Scenario builder** (Tools bar) if you had saved the base scenario before the operation.

***

## Load field data…

**Digital Twin Bar → Load field data…**

Imports field data from SCADA systems or data loggers and associates them with the meters of the `Meters` layer. The uploaded data is linked to each sensor for later comparison with the simulation results.

The dialog allows you to select the data file and configure the date/time format and field separator. QGISRed calls `GISRed.LoadScada` and updates the records of layer `Meters` with the imported time series.

### Typical usage

1. Export field sensor data from SCADA to a CSV or DAT file.
2. Run **Load field data** and select the file.
3. Run the simulation (**Run model**).
4. Visually compare the measured (field) and calculated (simulation) values ​​for each sensor in the **Time series** dock.
