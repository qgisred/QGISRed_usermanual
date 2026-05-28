# Controles y Reglas

**Barra Edition → Edit controls…**

El editor de controles define la **lógica de operación** de la red: cuándo se abre una válvula, cuándo arranca una bomba, o qué secuencia de acciones desencadena un determinado estado del sistema. EPANET soporta dos niveles de control con distinta complejidad.

![Editor de controles y reglas de QGISRed](../assets/images/edicion/editor-controles.png)
*Editor de controles: pestañas Simple Controls y Rules, selector de elementos y condiciones.*

---

## Controles simples (Simple Controls)

Un control simple define una **acción única** que se ejecuta cuando se cumple una **condición única**. Son suficientes para la mayoría de automatismos básicos.

### Estructura

```
IF [elemento] [condición]  THEN [acción]
```

### Tipos de condición

| Tipo | Ejemplo de uso |
|------|---------------|
| **Nivel de depósito** | Si el nivel del Tank T-1 supera 4.5 m → cerrar bomba BM-1 |
| **Presión en nudo** | Si la presión en J-120 cae por debajo de 10 m → abrir válvula V-3 |
| **Tiempo de simulación** | A las 6 h de simulación → encender bomba BM-2 |
| **Reloj** | A las 23:00 (hora del reloj) → cerrar tubería P-55 |

### Acciones disponibles

| Acción | Aplica a |
|--------|---------|
| **OPEN** | Tuberías, válvulas, bombas |
| **CLOSED** | Tuberías, válvulas, bombas |
| **Setting = valor** | Válvulas (cambia la consigna de regulación) |
| **Speed = valor** | Bombas (cambia la velocidad relativa) |

### Ejemplo completo

```
; Arrancar bomba cuando el depósito esté bajo
IF TANK T-DEPOSITO1 LEVEL BELOW 1.5
THEN PUMP BM-ELEVADORA OPEN

; Parar bomba cuando el depósito esté lleno
IF TANK T-DEPOSITO1 LEVEL ABOVE 4.0
THEN PUMP BM-ELEVADORA CLOSED

; Encender bomba de refuerzo a hora punta
IF CLOCKTIME 7:00 AM
THEN PUMP BM-REFUERZO OPEN

IF CLOCKTIME 10:00 AM
THEN PUMP BM-REFUERZO CLOSED
```

---

## Reglas de operación (Rules)

Las reglas permiten combinar **múltiples condiciones** con operadores lógicos, así como definir acciones alternativas y prioridades. Son equivalentes a las `[RULES]` del archivo `.inp` de EPANET.

### Estructura general

```
RULE [ID]
IF   [condición 1]
AND  [condición 2]          (opcional)
OR   [condición alternativa] (opcional)
THEN [acción principal]
ELSE [acción alternativa]   (opcional)
PRIORITY [número]           (opcional)
```

### Operadores lógicos

| Operador | Uso |
|----------|-----|
| **AND** | Todas las condiciones deben cumplirse simultáneamente |
| **OR** | Basta con que se cumpla cualquiera de las condiciones |

### PRIORITY

Cuando dos reglas con condiciones contradictorias se activan al mismo tiempo, la que tiene **mayor número de prioridad** gana. El valor por defecto es 0.

### Ejemplo completo

```
RULE R-01
IF   TANK T-DEP1 LEVEL BELOW 2.0
AND  PUMP BM-ELEV STATUS = CLOSED
THEN PUMP BM-ELEV OPEN
PRIORITY 2

RULE R-02
IF   NODE J-SALIDARED PRESSURE BELOW 8.0
OR   TANK T-DEP1 LEVEL BELOW 1.0
THEN PUMP BM-REFUERZO OPEN
ELSE PUMP BM-REFUERZO CLOSED
PRIORITY 1
```

---

## Edición en QGISRed

El diálogo de QGISRed presenta las reglas en formato de texto editable directamente, equivalente a la sección `[CONTROLS]` y `[RULES]` del archivo `.inp`. Puedes:

- **Escribir** controles y reglas directamente en el área de texto.
- **Activar o desactivar** una regla poniéndole un `;` al inicio (convierte la línea en comentario).
- **Verificar la sintaxis** con el botón de validación antes de guardar.

> Los controles se exportan exactamente como aparecen al generar el `.inp` desde la barra Tools. Si la sintaxis es incorrecta, EPANET rechazará el archivo en la simulación.

---

## Consejos de modelado

- Para un sistema con bomba y depósito, define siempre **dos controles por bomba**: uno para arrancar (nivel bajo) y otro para parar (nivel alto). Sin el control de parada, la bomba funciona indefinidamente.
- Los controles simples son procesados **antes** que las reglas en cada paso de tiempo. Si tienes un control simple y una regla que actúan sobre el mismo elemento, el resultado puede ser contradictorio.
- El orden de los controles simples **no importa**; el de las reglas tampoco, porque la prioridad los ordena. Pero si dos reglas tienen la misma prioridad y condiciones contradictorias, el resultado es indeterminado.
- Evita crear bucles de control (regla A activa B, regla B desactiva A en el mismo paso de tiempo): EPANET puede no convergir.
