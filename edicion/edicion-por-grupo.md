# Edición por Grupo

**Barra Edition → Edit properties by group…**

La herramienta **Edit properties by group** permite modificar en bloque un atributo de múltiples elementos de la red. Combina un filtro opcional con una acción de edición y aplica el resultado a todos los elementos que cumplen la condición, acumulando los cambios en un buffer de edición de QGIS hasta que el usuario los confirma o descarta.

El diálogo es **no modal**: se puede seguir interactuando con el mapa mientras está abierto.

<figure><img src="../assets/images/edicion/edicion-por-grupo.png" alt="Diálogo Edit properties by group con filtro y acción configurados"><figcaption><p>Diálogo Edit properties by group con filtro y acción configurados</p></figcaption></figure>
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

> 🧪 **Campos de calidad química:** Los campos BulkCoeff y WallCoeff (tuberías) y ReactCoef e InitQuality (depósitos, embalses y nudos) solo aparecen en los selectores de campo cuando el modelo de calidad del proyecto está configurado como **Chemical**.

---

## Seleccionar elementos

La sección **Select Elements** del diálogo agrupa el filtro de campo, la previsualización en el mapa y el ámbito de aplicación.

### Filtro de campo

El desplegable de campo comienza con la opción **Sin filtro** (*No Filter*). Mientras se mantiene esa selección, los controles de operador y valor permanecen ocultos y la acción afecta a todos los elementos del tipo elegido.

Al seleccionar un campo concreto, aparecen los controles de operador y valor:

- El **operador** determina el tipo de comparación (véase tabla más abajo).
- El **valor** se rellena automáticamente con los valores únicos presentes en la capa. La lista incluye **NULL** como primera opción:
  - Operador `=` con NULL genera un filtro **IS NULL**.
  - Operador `≠` con NULL genera un filtro **IS NOT NULL**.
- El campo de valor dispone de un botón **×** para borrarlo rápidamente. Además, el campo es **editable**: el usuario puede escribir un valor personalizado que no figure en la lista desplegable.

#### Operadores disponibles por tipo de campo

| Tipo de campo | Operadores |
|---------------|------------|
| Numérico | `>=`, `<=`, `=`, `>`, `<`, `≠` |
| Lista de valores | `=` |
| Texto libre | `=`, `≠`, `ILIKE`, `NOT ILIKE`, `LIKE`, `NOT LIKE` |
| Fecha | `=` (selector de calendario) |

### Preview en el mapa

El checkbox **Preview on map** resalta en **naranja** los elementos que cumplen el filtro activo, actualizándose en tiempo real al cambiar cualquier parámetro del filtro. Junto a este checkbox se muestra el **número de elementos** que coinciden con el filtro en ese momento.

### Solo elementos seleccionados

Al marcar **Only selected features**, la acción afecta únicamente a los elementos que estén seleccionados en el mapa en el momento de pulsar **Apply**. La selección puede realizarse antes de abrir el diálogo o mientras está abierto.

Sin marcar (por defecto), la acción se aplica a todos los elementos del tipo elegido que cumplan el filtro.

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
| `ValveType` (solo Valves) | Lista fija de EPANET (PRV, PSV, PBV, FCV, TCV, GPV), mostrada en el combo con su nombre largo en español (p. ej. "Reductora de Presión" para PRV) |

### Campos de fecha

Acción **Set to**: la fecha se selecciona desde el combo de fechas existentes en la capa o mediante el botón de calendario.

---

## Botones del diálogo

| Botón | Comportamiento |
|-------|----------------|
| **Apply** | Muestra un diálogo de confirmación previo que detalla los cambios que se aplicarán temporalmente (tipo de elemento, campo y número de elementos afectados) y solicita confirmación antes de escribir al buffer de edición de QGIS. Puede llamarse varias veces para acumular cambios sobre distintos atributos. Los elementos modificados quedan seleccionados en el mapa y su tabla de atributos se abre o reactiva. |
| **Accept** | Muestra una confirmación simple y, tras aceptar, guarda en disco de forma permanente todos los cambios acumulados en el buffer. Cierra el diálogo; las tablas de atributos permanecen abiertas. |
| **Cancel** | Descarta **todos** los cambios acumulados en el buffer (rollback completo) y cierra el diálogo. Limpia la selección en el mapa, pero las tablas de atributos permanecen abiertas. |

> Los cambios solo se escriben a disco al pulsar **Accept**. Mientras se trabaja con **Apply**, los datos están en el buffer de edición de QGIS y pueden deshacerse en bloque con **Cancel** en cualquier momento.

---

## Tabla de atributos

Tras cada **Apply**, la herramienta abre o reactiva la tabla de atributos de la capa afectada —tanto si está acoplada como si está flotante— sin duplicarla. Los elementos modificados aparecen ordenados al principio. Si se editan varias capas en sucesivos **Apply**, cada tabla se gestiona de forma independiente.

Al pulsar **Cancel** o **Accept**, las tablas de atributos permanecen abiertas; únicamente se limpia la selección en el mapa.

---

## Actualización automática del diálogo

Cuando se añaden o eliminan capas mientras el diálogo está abierto, este se actualiza automáticamente y restaura las selecciones previas de tipo de elemento, campo y filtro. Si el proyecto se cierra o se carga un proyecto diferente, el diálogo se cierra de forma automática.

---

## Ejemplos de uso

**Cambiar material a tuberías de un diámetro concreto**
Elemento: Pipes — Filtro: `Diameter = 200` — Do: `Material → Replace with → PVC`

**Incrementar el 10 % la rugosidad de tuberías de fundición**
Filtro: `Material = FD` — Do: `Roughness → Multiply by → 1.1`

**Cerrar todas las válvulas de aislamiento**
Elemento: Isolation Valves — Filtro: Sin filtro — Do: `InitStatus → Replace with → CLOSED`

**Asignar patrón a un conjunto de nudos seleccionados**
Marcar "Only selected features" — Elemento: Junctions — Do: `Pattern → Replace with → PAT_RESIDENCIAL`

**Reemplazar texto en etiquetas**
Elemento: Junctions — Do: `Tag → Find and replace → Buscar: "SEC" / Reemplazar: "ZN"`
