# Model Attribute Analysis

QGISRed allows you to massively audit the data entered in the elements to detect logical inconsistencies.

### Data Audit
* **Length Analysis**: Compares the length assigned in the attribute table (L) with the calculated geometric length (Euclidean). If the difference exceeds the user-defined percentage, the plugin issues a warning. Allows massive updating of the L value with the geometric data.
* **Diameter Analysis**: Identifies pipes whose diameters are outside the pre-established thresholds (minimum/maximum), helping to detect transcription errors.
* **Material Analysis**: Search for materials that are not defined in the official materials table of the project or that appear as "UNKNOWN".
* **Date Analysis**: Detects incorrect, poorly formatted installation dates or those that point to the future.

---
> 💡 **NOTE**:
> These verifications are essential before proceeding with the age-based roughness calculation, as they directly depend on the accuracy of the material and the date of installation.