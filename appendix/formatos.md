# DBF Formats and Management

Reference for users who edit project data directly in the QGIS attribute tables or from external tools, without going through the QGISRed dialogs.

---

## Date format

Field `InstalDate` of layer `Pipes` stores the installation date as a text string in the format:

```
yyyyMMdd
```

| Component | Description | Example |
|------------|-------------|---------|
| `yyyy` | Year (4 digits) | `2023` |
| `MM` | Month (2 digits, with leading zero) | `07` |
| `dd` | Day (2 digits, with leading zero) | `15` |

**Correct example**: `20230715` (July 15, 2023)

If the value does not follow this exact format, the **Check pipe installation dates** tool (Debug bar) will flag it as an issue and the **Set roughness coefficients** tool (Tools bar) will not be able to calculate the aging roughness for that pipe.

---

## Patterns and Curves (DBF)

Demand patterns and curves (H-Q, efficiency, volume) are stored in separate DBF tables. If you edit them directly outside of QGIS:

- **Decimal separator**: Always use the **dot** (`.`), regardless of the system locale. Commas as a decimal separator cause reading errors.
- **Order field**: each table has a numerical order field (`Order` or similar) that determines the sequence of the points or factors within the series. Do not alter this field or leave gaps in the numbering.

---

## Rules

Control rules are stored as individual records in the rules DBF table. Each rule occupies several rows (one per logical line: IF, AND, OR, THEN, ELSE). If you view the table outside of the QGISRed rules manager, sort the rows by these two columns in this order so that the rules are readable:

1. **`RuleOrder`** — groups all the lines of the same rule.
2. **`LineOrder`** — defines the logical order of the conditions within each rule.

The **`Name`** field stores a descriptive label visible in the rules manager. It does not affect the simulation and can be left empty.
