# Consultas por propiedades

**Barra Queries → Queries by properties…**

Abre el panel **Queries by Properties**, una herramienta de filtrado que resalta en el mapa todos los elementos que cumplen una o varias condiciones sobre sus atributos. Es la forma más rápida de encontrar, por ejemplo, todas las tuberías con diámetro menor de 80 mm, todos los nudos con presión por debajo de un umbral, o todas las válvulas en estado cerrado.

\*Panel Queries by Properties: condiciones configuradas sobre atributos de tubería. Los elementos que cumplen la condición se resaltan en magenta en el mapa.\*

***

## Interfaz del panel

El panel tiene un color identificativo **morado** (`#7B1FA2`) en su cabecera para distinguirlo del resto de paneles de QGISRed. Contiene:

* **Selector de tipo de elemento**: Pipes, Junctions, Tanks, Reservoirs, Pumps, Valves
* **Área de condiciones**: una o varias filas con campo, operador y valor
* **Botón Ejecutar**: aplica la consulta y resalta el resultado
* **Botón Limpiar**: elimina el resaltado del mapa
* **Etiqueta de tiempo**: cuando hay resultados de simulación cargados, muestra el instante activo con el prefijo "Time:" seguido del valor en negrita en formato `HH:MM:SS`. La etiqueta de estadísticas del resultado se muestra igualmente en negrita.

***

## Tipos de condiciones

El operador disponible para cada campo depende del tipo de dato:

### Campos numéricos

| Operador | Significado                           |
| -------- | ------------------------------------- |
| `All`    | Sin filtro (todos los valores)        |
| `>=`     | Mayor o igual que                     |
| `<=`     | Menor o igual que                     |
| `=`      | Igual a                               |
| `>`      | Mayor que                             |
| `<`      | Menor que                             |
| `≠`      | Distinto de                           |
| `Range`  | Entre dos valores (intervalo cerrado) |

### Campos de lista (enumerados)

Campos como `Status` que tienen un conjunto finito de valores posibles:

| Operador | Significado                 |
| -------- | --------------------------- |
| `All`    | Sin filtro                  |
| `=`      | Igual al valor seleccionado |

### Campos de texto libre

Campos como `Tag` o `Id`:

| Operador    | Significado                                |
| ----------- | ------------------------------------------ |
| `All`       | Sin filtro                                 |
| `=`         | Igual exacto                               |
| `≠`         | Distinto                                   |
| `ILIKE`     | Contiene (sin distinción de mayúsculas)    |
| `NOT ILIKE` | No contiene (sin distinción de mayúsculas) |
| `LIKE`      | Contiene (con distinción de mayúsculas)    |
| `NOT LIKE`  | No contiene (con distinción de mayúsculas) |

***

## Proceso

1. Abre **Queries by properties** desde la barra Queries.
2. Selecciona el **tipo de elemento** sobre el que quieres filtrar.
3. Añade una o varias condiciones: elige el campo, el operador y escribe el valor.
4. Pulsa **Ejecutar**. QGISRed evalúa la consulta y resalta en **magenta** todos los elementos que cumplen todas las condiciones simultáneamente (lógica AND).
5. Los elementos resaltados permanecen visibles mientras el panel está activo. Pulsa **Limpiar** para eliminar el resaltado.

***

## Combinación de condiciones

Todas las condiciones activas se combinan con lógica **AND**: un elemento solo queda resaltado si cumple **todas** las condiciones a la vez. Para una lógica OR (cualquiera de las condiciones), ejecuta consultas separadas con un solo criterio cada vez.

***

## Resultados de simulación

Si el proyecto tiene resultados de simulación cargados, los campos de resultado (presión, caudal, velocidad…) también aparecen en el selector de campo, permitiendo filtrar, por ejemplo, tuberías con velocidad inferior a 0.5 m/s o nudos con presión negativa.

> ⚠️ **Campos de calidad condicionales.** Los campos de resultado `Quality` y `ReactRate` solo aparecen cuando el modelo de calidad del proyecto lo permite: `Quality` se oculta con modelo _None_ y `ReactRate` únicamente es visible con modelo _Chemical_. Los campos estáticos de calidad (`BulkCoeff`, `WallCoeff`, `ReactCoef`, `IniQuality`) se ocultan cuando el modelo de calidad es _None_, _Age_ o _Trace_.

***

## Notas de uso

* La consulta no modifica ningún dato del modelo ni crea capas nuevas: solo cambia la simbología temporal.
* El resaltado en magenta es visible sobre cualquier fondo de mapa.
* Al cerrar el panel, el resaltado desaparece y la simbología vuelve al estado anterior.

## Resolución del campo ID

El panel utiliza la misma lógica de resolución automática del campo identificador que el Element Explorer (`getIdFieldName(layer)`). Los campos de consulta por ID (`PipeID`, `TankID`, etc.) se detectan automáticamente según el tipo de capa, por lo que las consultas sobre el campo `Id` funcionan correctamente independientemente del nombre real del campo en el shapefile del proyecto. Ver [Element Explorer](explorador-elementos.md) para más detalles.

Los alias `PumpCurvID`, `BaseDem` y `SourceQual` se reconocen automáticamente como campos de tipo numérico para bombas, demandas y fuentes respectivamente. El tipo de dato de cada campo (numérico, lista o texto libre) se determina de forma automática a partir del esquema del elemento, sin necesidad de configuración manual.
