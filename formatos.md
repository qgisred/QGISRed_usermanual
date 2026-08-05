# 📂 Apéndice Técnico

Referencia para usuarios que editen los datos del proyecto directamente en las tablas de atributos de QGIS o desde herramientas externas, sin pasar por los diálogos de QGISRed.

***

## Formato de fechas

El campo `InstalDate` de la capa `Pipes` almacena la fecha de instalación como cadena de texto con el formato:

```
yyyyMMdd
```

| Componente | Descripción                       | Ejemplo |
| ---------- | --------------------------------- | ------- |
| `yyyy`     | Año (4 dígitos)                   | `2023`  |
| `MM`       | Mes (2 dígitos, con cero inicial) | `07`    |
| `dd`       | Día (2 dígitos, con cero inicial) | `15`    |

**Ejemplo correcto**: `20230715` (15 de julio de 2023)

Si el valor no sigue este formato exacto, la herramienta **Check pipe installation dates** (barra Debug) lo marcará como incidencia y la herramienta **Set roughness coefficients** (barra Tools) no podrá calcular la rugosidad por envejecimiento para esa tubería.

***

## Patrones y curvas (DBF)

Los patrones de demanda y las curvas (H-Q, eficiencia, volumen) se almacenan en tablas DBF independientes. Si los editas directamente fuera de QGIS:

* **Separador decimal**: usa siempre el **punto** (`.`), independientemente de la configuración regional del sistema. Las comas como separador decimal provocan errores de lectura.
* **Campo de orden**: cada tabla tiene un campo numérico de orden (`Order` o similar) que determina la secuencia de los puntos o factores dentro de la serie. No alteres este campo ni dejes huecos en la numeración.

***

## Reglas (Rules)

Las reglas de control se almacenan como registros individuales en la tabla DBF de reglas. Cada regla ocupa varias filas (una por línea lógica: IF, AND, OR, THEN, ELSE). Si visualizas la tabla fuera del gestor de reglas de QGISRed, ordena las filas por estas dos columnas en este orden para que las reglas sean legibles:

1. **`RuleOrder`** — agrupa todas las líneas de una misma regla.
2. **`LineOrder`** — define el orden lógico de las condiciones dentro de cada regla.

El campo **`Name`** almacena una etiqueta descriptiva visible en el gestor de reglas. No afecta a la simulación y puede dejarse vacío.
