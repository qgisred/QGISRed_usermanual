# Hydraulic properties

The first four tools in the Tools bar calculate or update hydraulic properties of pipes and nodes in bulk: length, elevation and roughness. They work on the current selection or on the entire network if there is no selection.

***

## Automatically calculate pipe lengths

**Tools bar → Automatically calculate pipe lengths**

Recalculates the `Length` field of each pipe using the actual geometric length measured over the SHP vertices in the project's CRS units.

### When to use it

* After moving vertices or nodes with the Edition tools without having updated the attribute.
* After importing from a `.inp` whose lengths differ from the real geometry (coordinates on a different scale or different projection).
* As a previous step to **Check pipe lengths** (Debug Bar) to leave all values ​​synchronized before the audit.

The tool overwrites the value of `Length` unconditionally on all pipes in the selection scope. It does not ask for confirmation or filter for tolerance.

> Always use a projected metric CRS (UTM, LCC, etc.). If the project uses geographic coordinates (decimal degrees), the calculated length will be in degrees, not meters, and will be useless for the simulation.

***

## Interpolate elevation from .asc files…

**Tools Bar → Interpolate elevation from .asc files…**

Assigns the elevation (field `Elevation`) to the nodes, tanks and reservoirs of the project by interpolating their value from one or more Digital Terrain Models (DTM) in ASC format.

\*MDT File Selector: You can upload multiple ASC files to cover the entire network area.\*

### ASC format supported

```
ncols         500
nrows         400
xllcenter     450000.0
yllcenter     4400000.0
cellsize      5.0
nodata_value  -9999
230.4 231.1 231.8 ...
```

| Header                    | Meaning                                                                                        |
| ------------------------- | ---------------------------------------------------------------------------------------------- |
| `ncols` / `nrows`         | Number of columns and rows in the mesh                                                         |
| `xllcenter` / `yllcenter` | Coordinates of the center of the bottom-left cell (`xllcorner` / `yllcorner` is also accepted) |
| `cellsize`                | Cell size in CRS units                                                                         |
| `nodata_value`            | Value that the plugin ignores (cell without data)                                              |

### Assignment process

1. Open the selector and choose one or more `.asc` files. You can combine multiple MDTs to cover the entire network area.
2. QGISRed projects the coordinate of each node onto the mesh and obtains the elevation by bilinear interpolation between the four neighboring cells.
3. Only nodes whose current `Elevation` is equal to the default value (typically 0) are updated. Nodes with an elevation already assigned manually are not modified.
4. Nodes that fall outside the range of all loaded MDTs are marked as an incident on the message board.

> The CRS of the ASC file must match the CRS of the project. If they do not match, the coordinates are not projected and the nodes will be outside the mesh.

***

## Set roughness coefficients (from Material and Date)

**Tools bar → Set roughness coefficients (from Material and Date)**

Calculates and assigns the current roughness coefficient of each pipe based on its material, its year of installation and the parameters of the project's **Materials Table**.

### Calculation formula

```
Rugosidad_actual = Rugosidad_inicial + (Año_actual − InstallYear) × Incremento_anual
```

Where `Rugosidad_inicial` and `Incremento_anual` are obtained from the Material Table row that matches the `Material` field of the pipe.

### Prerequisites

Before using this tool, verify with the Debug Bar that:

1. All pipes have a valid `Material` (**Check pipe materials**).
2. All pipes have a correct `InstallYear` (**Check pipe installation dates**).

If any of these fields are empty or invalid for a pipe, its roughness is not updated and is recorded as an issue.

Roughness is written in the units of the active project formula:

| Formula              | Roughness unit                                |
| -------------------- | --------------------------------------------- |
| Darcy-Weisbach (D-W) | mm (absolute wall roughness)                  |
| Hazen-Williams (H-W) | Dimensionless C coefficient (typical 100–150) |
| Chezy-Manning (C-M)  | Coefficient n (typical 0.010–0.020)           |

> The Material Table stores the initial roughness in D-W units (mm). If the project uses H-W or C-M, the calculated value is automatically converted to the active system.

***

## Convert roughness coefficients…

**Tools bar → Convert roughness coefficients…**

Converts the values ​​of the `Roughness` field of all pipes between the three pressure loss formulas. It is necessary when you change the hydraulic formula of the project and want the existing values ​​to maintain their physical meaning.

### Available conversions

| Origin               | Destination          |
| -------------------- | -------------------- |
| Hazen-Williams (H-W) | Darcy-Weisbach (D-W) |
| Darcy-Weisbach (D-W) | Hazen-Williams (H-W) |
| Chezy-Manning (C-M)  | Darcy-Weisbach (D-W) |
| Darcy-Weisbach (D-W) | Chezy-Manning (C-M)  |

When changing the hydraulic formula in **Project Options**, QGISRed detects the change and offers to run this tool automatically. If you reject at that time, you can launch it manually from here.

> The D-W ↔ H-W conversion uses the diameter and a reference flow rate to find the C that produces the same loss as the D-W roughness at that flow rate. The result may differ from a direct calibration because the three formulas are not mathematically equivalent for all flow regimes.
