# Project Configuration

The **Project** bar groups three configuration dialogs that affect the hydraulic behavior of the model and the default values ​​with which new elements are created.

---

## Project Options

**Project bar → Project options** (Project settings)

Opens the main EPANET options dialog. It is equivalent to section `[OPTIONS]` of file `.inp`.

<figure><img src="../assets/images/proyecto/opciones-proyecto.png" alt="Project options dialog: Hydraulics, Quality, Time and Energy tabs"><figcaption><p>Project options dialog: Hydraulics, Quality, Time and Energy tabs</p></figcaption></figure>
*Project Options dialog with its four tabs.*

### Hydraulic Tab

| Field | Description |
|-------|-------------|
| **Flow units** | Defines the system of units of the project. Metric units (LPS, LPM, MLD, CMH, CMD) correspond to SI; gallons and cubic feet (CFS, GPM, MGD, IMGD, AFD) to US |
| **Head loss formula** | Darcy-Weisbach (D-W), Hazen-Williams (H-W) or Chezy-Manning (C-M) |
| **Specific gravity** | Specific weight of the fluid with respect to pure water (1.0 for standard water) |
| **Relative viscosity** | Factor on the kinematic viscosity of water at 20 °C |
| **Precision** | Convergence criterion of the hydraulic solver |
| **Demand model** | DDA (Demand Driven) or PDA (Pressure Driven) — in PDA, demand is reduced if the pressure drops below a threshold |
| **Minimum / nominal pressure** | Thresholds for the PDA model |
| **Max. iterations / ratio** | Solver convergence parameters |

> 💡 Changing the **flow units** does not convert the values ​​already entered. If the network is set to LPS and you switch to GPM, all demand, flow, and length values ​​will need to be updated manually.

### Quality Tab

| Field | Description |
|-------|-------------|
| **Type of quality analysis** | None (does not simulate quality), Chemical (reagent), Age (water age), Trace (tracer) |
| **Reagent label** | Name of the modeled product (e.g. "Chlorine") — will appear in the results |
| **Tracer node** | For Trace type analysis, tracer source node ID |
| **Concentration units** | mg/L or μg/L |
| **Diffusivity** | Relative molecular diffusion coefficient (1.0 for chlorine in water) |
| **Tolerance** | Convergence criterion for the quality solver |

### Times Tab

| Field | Description |
|-------|-------------|
| **Simulation duration** | Total simulation time. Format `HH:MM:SS` or in hours (e.g. `24:00:00`) |
| **Hydraulic time step** | Hydraulic calculation interval (typically 1 h) |
| **Quality time pass** | Quality calculation interval (typically 5 min) |
| **Report time step** | How often results are saved (determines the number of moments available in the Viewer) |
| **Simulation start time** | Clock time corresponding to instant 0 of the simulation |
| **Type of statistician** | None (all instants), Average, Minimum, Maximum, Range |

> 💡 A 1-h **reporting step** in a 24-h simulation generates 25 result instants (0 h to 24 h). Shorter steps increase the temporal resolution but also the size of the result files.

### Energy Tab

Allows you to define the energy cost of the pumps for consumption analysis:

| Field | Description |
|-------|-------------|
| **Global price** | Cost per kWh (in defined currency) |
| **Price pattern** | Temporal pattern of electricity price variation |
| **Overall efficiency** | Average efficiency of the pumps (if they do not have individual efficiency curve) |

---

## Default values

**Project bar → Default values** (Default values)

Defines the values ​​that are automatically assigned to new elements when they are created with the editing tools.

<figure><img src="../assets/images/proyecto/valores-defecto.png" alt="Defaults dialog with sections for nodes, pipes and prefixes"><figcaption><p>Defaults dialog with sections for nodes, pipes and prefixes</p></figcaption></figure>
*Default values ​​dialog: initial parameters for each element type.*

### ID Prefixes

Each item type has a configurable prefix that is used when automatically generating the ID of new items:

| Element | Default prefix | Example of generated ID |
|----------|---------------------|------------------------|
| Junction | J | J-1, J-2… |
| Pipe | P | P-1, P-2… |
| Tank | T | T-1, T-2… |
| Reservoir | R | R-1, R-2… |
| Valve | V | V-1, V-2… |
| Pump | BM | BM-1, BM-2… |

The prefixes are configurable. The starting number can also be set.

### Initial hydraulic values ​​

| Field | Description |
|-------|-------------|
| **Default diameter** | Diameter (mm or inches) assigned to the new pipes |
| **Default roughness** | Roughness coefficient according to the active formula |
| **Default elevation** | Elevation (m or ft) assigned to the new nodes |
| **Default base demand** | Initial demand of the new demand nodes |
| **Default pump speed** | Initial relative speed factor for pumps |

### Geometric tolerances

| Field | Description |
|-------|-------------|
| **Node Tolerance** | Maximum distance (m or ft) to consider two points to be the same node |
| **Minimum length for division** | Minimum length of the resulting sections when dividing a pipe |
| **Maximum length for division** | Maximum length of the resulting sections when dividing a pipe |

---

## Materials table

**Project bar → Materials table** (Materials table)

Manage the list of materials available for pipes and their aging properties.

<figure><img src="../assets/images/proyecto/tabla-materiales.png" alt="Table of materials: code, name, initial roughness and annual increase"><figcaption><p>Table of materials: code, name, initial roughness and annual increase</p></figcaption></figure>
*Table of materials with initial roughness and increase per year.*

### Table fields

| Field | Description |
|-------|-------------|
| **Code** | Material abbreviation (e.g. PVC, DI, AC) |
| **Name** | Full name (e.g. "Ductile Iron", "Asbestos Cement") |
| **Initial roughness** | D-W roughness coefficient (mm) at installation date |
| **Annual increase** | Increase in roughness per year of age (mm/year) |

### Use with the "Assign Roughness" tool

When you use the **Assign Roughnesses** tool from the Tools bar, QGISRed searches this table for the material of each pipe and calculates:

```
Rugosidad = Rugosidad_inicial + (Año_actual - Año_instalación) × Incremento_anual
```

> 💡 You can add custom materials. The materials defined here are also available when creating new pipes from the Edition bar.

### Materials included by default

QGISRed includes a predefined material table with the most common ones (CI, DI, AC, PVC, PE, HDPE...). You can edit or extend them according to the characteristics of your system.

### Save and reuse tables between projects

The materials table is specific to each project, but can be shared with other projects by saving it as a **global** table (stored in the user profile, outside of any project). The dialog, opened with an active project, offers these buttons:

| Button | Action |
|-------|--------|
| **Copy as global** | Saves a copy of the current table as a **new** global table, asking for a name. If a global table with that name already exists, ask for confirmation before overwriting it. |
| **Load materials** | Replaces the project materials table with a previously saved global table. |
| **Reset default materials** | Restores the predefined QGISRed table (depending on the interface language), discarding the project materials. |

> 💡 If you open **Table of Materials** without any active QGISRed project, the dialog works as an independent global table manager: you can choose between the already saved tables, delete them and use the **Save as global** button, which saves the changes **over the selected global table** (unlike **Copy as global**, which always creates a new table with another name).
