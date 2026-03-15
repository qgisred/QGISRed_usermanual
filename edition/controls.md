# Controls and Rules

Define the operating logic of your network (e.g. "if the tank is full, turn off the pump").

![Controls Icon](../assets/icons/controls.png)

### Simple Controls
Direct actions based on a single trigger:
* **Based on Level/Pressure**: If node X is < 10m, open valve Y.
* **Time Based**: At 08:00, turn on bomb Z.
* **Based on Clock**: Every Monday at 02:00, close pipe W.

### Complex Rules
They allow multiple conditions to be combined using logical operators:
* **Operators**: `IF`, `AND`, `OR`, `THEN`, `ELSE`, `PRIORITY`.
* **Interactive Interface**: Unlike classic EPANET, in QGISRed you build the rules by selecting elements and operators in drop-down menus, avoiding syntax errors in the text file.
* **Enabling**: You can disable specific rules without deleting them to test different operating scenarios.