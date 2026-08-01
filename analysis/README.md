# 🧪Analysis

The **Analysis** bar groups the hydraulic simulation tools, visualization of results and export of the model. It is the bar that closes the work cycle: once the model is defined, verified and calibrated, this bar is used to run EPANET, explore the results on the map and export to other formats.

> Before simulating it is advisable to have passed the [topology and attribute checks](../debug/README.md) to avoid convergence errors.

<figure><img src="../assets/images/analisis/barra-analysis.png" alt="QGISRed Analysis Toolbar"><figcaption><p>QGISRed Analysis Toolbar</p></figcaption></figure>
*Analysis bar: simulation, results viewer, time series and export.*

---

## Analysis Bar Tools

| # | Tool | Function |
|---|-------------|---------|
| 1 | **Run model** | Run the EPANET simulation and load the results into the map |
| — | **Results browser** | Open the results panel with the data from the last simulation |
| — | **Status report** | Open the results panel in the status report tab |
| 2 | **Analysis options…** | Configure EPANET engine parameters (units, formula, times, quality) |
| 3 | **Time series…** | Activate the time evolution graphs tool by element |
| 4 | **Export results to CSV…** | Export simulation results to separate CSV files for nodes and pipes |
| 5 | **Export model to INP…** | Export the complete model to EPANET `.inp` |

*Run model, Results browser and Status report share a drop-down button in the bar.*

---

## In this section

* [Execution and Options](execution.md) — simulation, engine options and status report access
* [Results Viewer](results.md) — results panel, temporal navigation and time series
* [Model Export](export.md) — export to INP and CSV of results
