# Consultas por Propiedades

**Barra Consultas → Consultas por propiedades…**

Abre el panel **Queries by Properties**, una herramienta de filtrado que resalta en el mapa todos los elementos que cumplen una o varias condiciones sobre sus atributos. Es la forma más rápida de encontrar, por ejemplo, todas las tuberías con diámetro menor de 80 mm, todos los nudos con presión por debajo de un umbral, o todas las válvulas en estado cerrado.

<figure><img src="../assets/images/queries/queries-by-properties.png" alt="Panel Queries by Properties con condiciones configuradas y resultado resaltado en magenta"><figcaption><p>Panel Queries by Properties con condiciones configuradas y resultado resaltado en magenta</p></figcaption></figure>
*Panel Queries by Properties: condiciones configuradas sobre atributos de tubería. Los elementos que cumplen la condición se resaltan en magenta en el mapa.*

---

## Interfaz del panel

El panel tiene un color identificativo **morado** (`#7B1FA2`) en su cabecera para distinguirlo del resto de paneles de QGISRed. Contiene:

- **Selector de tipo de elemento**: Pipes, Junctions, Tanks, Reservoirs, Pumps, Valves
- **Modo de criterio**: dos opciones, **Un criterio** (una sola condición activa) y **Múltiples criterios** (lista de condiciones combinables, ver más abajo)
- **Área de condiciones**: una o varias filas con campo, operador y valor
- **Botón Ejecutar**: aplica la consulta y resalta el resultado
- **Botón Limpiar**: elimina el resaltado del mapa
- **Panel de Estadísticas**: selector de propiedad y tabla con los resultados numéricos de la consulta (ver más abajo)
- **Etiqueta de tiempo**: cuando hay resultados de simulación cargados, muestra el instante activo con el prefijo "Instante:" seguido del valor en negrita en formato `HH:MM:SS`. La etiqueta de estadísticas del resultado se muestra igualmente en negrita.

---

## Tipos de condiciones

El operador disponible para cada campo depende del tipo de dato:

### Campos numéricos

| Operador | Significado |
|----------|-------------|
| `All` | Sin filtro (todos los valores) |
| `>=` | Mayor o igual que |
| `<=` | Menor o igual que |
| `=` | Igual a |
| `>` | Mayor que |
| `<` | Menor que |
| `≠` | Distinto de |
| `Range` | Entre dos valores (intervalo cerrado) |

### Campos de lista (enumerados)

Campos como `Status` que tienen un conjunto finito de valores posibles:

| Operador | Significado |
|----------|-------------|
| `All` | Sin filtro |
| `=` | Igual al valor seleccionado |

> ℹ️ Para `Type`/`ValveType` en válvulas, el selector de valor muestra el nombre largo del tipo en español (p. ej. "Reductora de Presión" para PRV) en lugar del código EPANET.

### Campos de texto libre

Campos como `Tag` o `Id`:

| Operador | Significado |
|----------|-------------|
| `All` | Sin filtro |
| `=` | Igual exacto |
| `≠` | Distinto |
| `ILIKE` | Contiene (sin distinción de mayúsculas) |
| `NOT ILIKE` | No contiene (sin distinción de mayúsculas) |
| `LIKE` | Contiene (con distinción de mayúsculas) |
| `NOT LIKE` | No contiene (con distinción de mayúsculas) |

---

## Proceso

1. Abre **Queries by properties** desde la barra Queries.
2. Selecciona el **tipo de elemento** sobre el que quieres filtrar.
3. Añade una o varias condiciones: elige el campo, el operador y escribe el valor.
4. Pulsa **Ejecutar**. QGISRed evalúa la consulta y resalta en **magenta** los elementos que la cumplen — en modo Multiple Criteria, según la lógica de inclusión/exclusión que se explica más abajo.
5. Los elementos resaltados permanecen visibles mientras el panel está activo. Pulsa **Limpiar** para eliminar el resaltado.

---

## Modo de criterio único o múltiple

El radio **Un criterio** limita el panel a una sola condición activa a la vez: cambiar el campo, el operador o el valor reemplaza la condición anterior. Es el modo más simple para consultas puntuales.

El radio **Múltiples criterios** abre una lista de condiciones independientes que se pueden combinar entre sí:

- **Añadir**: añade la condición configurada arriba a la lista, marcada como condición de **inclusión** (`+`).
- **Restar**: añade la condición configurada arriba a la lista, marcada como condición de **exclusión** (`-`).
- Cada fila de la lista se puede **reordenar** (flechas arriba/abajo), **editar** (doble clic o botón de edición), **eliminar**, o **activar/desactivar** temporalmente sin borrarla (botón "Habilitar/deshabilitar el criterio seleccionado") para probar combinaciones sin perder las condiciones ya definidas.

Al pasar de **Múltiples criterios** a **Un criterio** con más de una condición en la lista, QGISRed pide confirmación: solo se conserva la primera, el resto se descarta.

### Lógica de combinación

Las condiciones de inclusión (`+`) se combinan entre sí con **OR**: un elemento se resalta si cumple **cualquiera** de ellas. Las condiciones de exclusión (`-`) se combinan entre sí con **AND** y el resultado se **resta** del anterior. En resumen:

> *(cualquier condición de inclusión)* **AND NOT** *(todas las condiciones de exclusión)*

Por ejemplo, para encontrar todas las tuberías de diámetro ≥ 300 mm que **no** sean de fundición: una condición `Diameter >= 300` marcada con **Añadir**, y una condición `Material = Cast Iron` marcada con **Restar**.

En modo **Un criterio** solo hay una condición, así que esta combinación no aplica.

---

## Resultados de simulación

Si el proyecto tiene resultados de simulación cargados, los campos de resultado (presión, caudal, velocidad…) también aparecen en el selector de campo, permitiendo filtrar, por ejemplo, tuberías con velocidad inferior a 0.5 m/s o nudos con presión negativa.

> ⚠️ **Campos de calidad condicionales.** Los campos de resultado `Quality` y `ReactRate` solo aparecen cuando el modelo de calidad del proyecto lo permite: `Quality` se oculta con modelo *None* y `ReactRate` únicamente es visible con modelo *Chemical*. Los campos estáticos de calidad (`BulkCoeff`, `WallCoeff`, `ReactCoef`, `IniQuality`) se ocultan cuando el modelo de calidad es *None*, *Age* o *Trace*.

---

## Tabla de Estadísticas

El panel calcula estadísticas numéricas sobre los elementos resaltados sin necesidad de exportar nada. Selecciona en el desplegable **Statistics of... for selected Elements** la propiedad a calcular — cualquier campo numérico del tipo de elemento activo, o una de las variables de resultado si hay simulación cargada — y la tabla se actualiza automáticamente.

Las columnas dependen del tipo de propiedad:

| Propiedad | Columnas |
|---|---|
| Campo de texto o lista | **Recuento** (número de elementos) |
| Campo numérico | **Recuento**, **Promedio**, **Mínimo**, **Máximo**, y **Suma** o **Desv. Típica** según la propiedad (caudales y demandas muestran la suma; el resto, la desviación típica) |
| **Ninguna** (sin propiedad) | solo **Recuento** |

En modo **Un criterio** la tabla muestra una única fila con el resultado de la condición activa. En modo **Múltiples criterios** con varias condiciones habilitadas, muestra una fila por cada condición (etiquetada `Cr1`, `Cr2`...) y una fila final **Todos** en amarillo con el resultado combinado (la misma lógica de inclusión/exclusión que el resaltado del mapa) — así se puede comparar cuántos elementos aporta cada condición por separado frente al total combinado.

## Exportar criterios y estadísticas

Los botones de exportación del panel (criterios de consulta y tabla de estadísticas) guardan por defecto en la subcarpeta `Queries/Queries by properties` del proyecto, en lugar de la carpeta raíz.

> 📝 Al exportar varios criterios combinados a texto o CSV, cada línea se numera como `Cr1:`, `Cr2:`... en vez de empezar directamente por el operador de la condición — así una hoja de cálculo no interpreta por error un criterio que empieza por `+` o `-` como una fórmula.

El CSV de estadísticas incluye, antes de la tabla de valores, unas líneas de cabecera con el proyecto, el escenario, el tipo de elemento, la consulta o consultas aplicadas y la magnitud exportada.

## Notas de uso

- La consulta no modifica ningún dato del modelo ni crea capas nuevas: solo cambia la simbología temporal.
- El resaltado en magenta es visible sobre cualquier fondo de mapa.
- Al cerrar el panel, el resaltado desaparece y la simbología vuelve al estado anterior.

## Resolución del campo ID

El panel utiliza la misma lógica de resolución automática del campo identificador que el Element Explorer (`getIdFieldName(layer)`). Los campos de consulta por ID (`PipeID`, `TankID`, etc.) se detectan automáticamente según el tipo de capa, por lo que las consultas sobre el campo `Id` funcionan correctamente independientemente del nombre real del campo en el shapefile del proyecto. Ver [Element Explorer](explorador-elementos.md) para más detalles.

Los alias `PumpCurvID`, `BaseDem` y `SourceQual` se reconocen automáticamente como campos de tipo numérico para bombas, demandas y fuentes respectivamente. El tipo de dato de cada campo (numérico, lista o texto libre) se determina de forma automática a partir del esquema del elemento, sin necesidad de configuración manual.
