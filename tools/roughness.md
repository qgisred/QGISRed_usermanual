# Roughness Management and Conversion

One of the powers of QGISRed is the dynamic management of roughness based on the material and age of the infrastructure.

### Calculation by Age and Material
The plugin estimates the roughness coefficient by crossing the **Installation Date** and **Material** of the pipe with the **Materials Table** of the project.

1. Find the material in the table to obtain the initial roughness ($\epsilon_0$).
2. Calculate the current age (years since installation).
3. Apply the configured annual roughness increase.

### Conversion between Formulas
QGISRed allows you to convert roughness coefficients automatically when you change the project's head loss formula:

* **Darcy-Weisbach (D-W)** $\leftrightarrow$ **Hazen-Williams (H-W)**
* **Darcy-Weisbach (D-W)** $\leftrightarrow$ **Chezy-Manning (C-M)**

> ❗ **IMPORTANT**:
> By changing the formula in **Hydraulic Options**, the plugin will ask you if you want to perform the mass conversion of all existing roughnesses to maintain the physical consistency of the model.

### Table of Materials
You can set the base coefficients to `Project > Materials Table`. It is essential to use the correct acronyms (e.g. `PVC-O`, `PEAD`) for effective linking.