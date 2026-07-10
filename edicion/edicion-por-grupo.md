# Edición por Grupo

**Barra Edition → Edit properties by group…**

La herramienta **Edit properties by group** permite modificar en bloque un atributo de múltiples elementos de la red. Combina un filtro opcional con una acción de edición y aplica el resultado a todos los elementos que cumplen la condición, acumulando los cambios en un buffer de edición de QGIS hasta que el usuario los confirma o descarta.

El diálogo es **no modal**: se puede seguir interactuando con el mapa mientras está abierto.

![Diálogo Edit properties by group con filtro y acción configurados](../assets/images/edicion/edicion-por-grupo.png)
*Diálogo de edición por grupo: filtro por campo numérico y acción Multiply by sobre tuberías.*

---

## Tipos de elementos disponibles

| Elemento | Descripción |
|----------|-------------|
| **Junctions** | Nudos de la red |
| **Multiple Demands** | Demandas múltiples por categoría |
| **Pipes** | Tuberías |
| **Tanks** | Depósitos |
| **Reservoirs** | Embalses |
| **Pumps** | Bombas |
| **Valves** | Válvulas |
| **Sources** | Fuentes de calidad |
| **Service Connections** | Acometidas |
| **Isolation Valves** | Válvulas de aislamiento |
| **Meters** | Caudalímetros |

---

## Filtro (sección "with… optional filter")

Limita los elementos afectados a los que cumplen una condición sobre un campo. Si se deja en `All`, la acción se aplica a todos los elementos del tipo seleccionado.

### Operadores disponibles por tipo de campo

| Tipo de campo | Operadores |
|---------------|------------|
| Numérico | All, `>=`, `<=`, `=`, `>`, `<`, `≠` |
| Lista de valores | All, `=` |
| Texto libre | All, `=`, `≠`, `ILIKE`, `NOT ILIKE`, `LIKE`, `NOT LIKE` |
| Fecha | All, `=` (selector de calendario) |

Cuando se elige un campo y un operador concreto, el desplegable de valor se rellena automáticamente con los valores únicos presentes en la capa. Para texto libre el campo de valor es editable.

### Preview en el mapa

El checkbox **Preview on map** resalta en **naranja** los elementos que cumplen el filtro activo, actualizándose en tiempo real al cambiar cualquier parámetro del filtro.

---

## Acción de edición (sección "Do…")

Define qué atributo modificar y con qué valor o transformación.

### Acciones para campos numéricos

| Acción | Fórmula |
|--------|---------|
| **Replace with** | `operando` |
| **Multiply by** | `valor_actual × operando` |
| **Add** | `valor_actual + operando` |
| **Subtract** | `valor_actual − operando` |
| **Divide by** | `valor_actual / operando` |
| **Clamp minimum to** | `max(valor_actual, operando)` |
| **Clamp maximum to** | `min(valor_actual, operando)` |

### Acciones para campos de texto

| Acción | Resultado |
|--------|-----------|
| **Set to** | Reemplaza el valor completo |
| **Prepend** | Antepone el texto al valor actual |
| **Append** | Añade el texto al final del valor actual |
| **Find and replace** | Búsqueda y reemplazo (distingue mayúsculas) |

### Acciones para campos enumerados

Solo **Replace with**, seleccionando el nuevo valor de una lista. Las opciones disponibles dependen del tipo de campo:

| Campo | Fuente de opciones |
|-------|--------------------|
| `InitStatus` | Lista fija de EPANET (Open, Closed, CV, Active…) |
| `Material` | Tabla de materiales del proyecto |
| `Curve` | Curvas del proyecto filtradas por tipo (pump, volume, efficiency, headloss) |
| `Pattern` | Patrones del proyecto filtrados por tipo (demand, quality, head, speed, price) |

### Campos de fecha

Acción **Set to**: la fecha se selecciona desde el combo de fechas existentes en la capa o mediante el botón de calendario.

---

## Ámbito de aplicación

- **Sin marcar** (por defecto): la acción afecta a todos los elementos del tipo elegido que cumplan el filtro.
- **Only selected features**: la acción afecta solo a los elementos actualmente **seleccionados en el mapa**. La selección puede realizarse antes de abrir el diálogo o mientras está abierto.

---

## Botones del diálogo

| Botón | Comportamiento |
|-------|----------------|
| **Apply** | Aplica los cambios al buffer de edición de QGIS sin guardar en disco. Puede llamarse varias veces para acumular cambios sobre distintos atributos. Los elementos modificados se seleccionan en el mapa y se abre su tabla de atributos como panel acoplable. |
| **Accept** | Muestra un resumen de todos los cambios pendientes en el buffer y, tras confirmación del usuario, los guarda en disco. Cierra el diálogo. |
| **Cancel** | Descarta **todos** los cambios acumulados en el buffer (rollback completo) y cierra el diálogo. |

> Los cambios solo se escriben a disco al pulsar **Accept**. Mientras se trabaja con **Apply**, los datos están en el buffer de edición de QGIS y pueden deshacerse en bloque con **Cancel** en cualquier momento.

---

## Tabla de atributos acoplada

Tras cada **Apply**, el diálogo abre la tabla de atributos de la capa afectada como panel acoplable con los elementos modificados ordenados al principio. Si se editan varias capas en sucesivos Apply, las tablas se apilan en un panel único con pestañas. Al cerrar el diálogo, todas las tablas abiertas por la herramienta se cierran.

---

## Ejemplos de uso

**Cambiar material a tuberías de un diámetro concreto**
Elemento: Pipes — Filtro: `Diameter = 200` — Do: `Material → Replace with → PVC`

**Incrementar el 10 % la rugosidad de tuberías de fundición**
Filtro: `Material = FD` — Do: `Roughness → Multiply by → 1.1`

**Cerrar todas las válvulas de aislamiento**
Elemento: Isolation Valves — Filtro: All — Do: `InitStatus → Replace with → CLOSED`

**Asignar patrón a un conjunto de nudos seleccionados**
Marcar "Only selected features" — Elemento: Junctions — Do: `Pattern → Replace with → PAT_RESIDENCIAL`

**Reemplazar texto en etiquetas**
Elemento: Junctions — Do: `Tag → Find and replace → Buscar: "SEC" / Reemplazar: "ZN"`
