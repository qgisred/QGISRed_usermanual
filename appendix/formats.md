# Data Formats and DBF Files

For advanced users who prefer to edit data directly from QGIS tables or external files, the required technical formats are detailed here.

### Date Format
The `InstalDate` field in the pipes layer must strictly follow the format:
**`yyyyMMdd`**
* **yyyy**: Year (4 digits).
* **MM**: Month (2 digits, with leading zero if necessary).
* **dd**: Day (2 digits).
* *Example*: `20230715` for July 15, 2023.

### Pattern and Curve Management (DBF)
Pattern and curve data are stored in `.dbf` tables. When editing them manually keep in mind:
* **Order**: There is an order field that indicates the position of the factor within the series.
* **Separators**: If editing outside of QGIS, make sure to stay consistent with the decimal (dot) separator.

### Rules Management
Rules in attribute tables may appear out of order. To view them correctly, sort the table by these columns in this order:
1. **RuleOrder**: Groups all the lines of the same rule.
2. **LineOrder**: Defines the logical order of the conditions (IF, AND, OR, THEN, ELSE).

### "Name" field
QGISRed adds a `Name` column to the rules and controls. This field does not affect the simulation but allows you to visually identify the function of each line in the plugin form.