# Patrones y Curvas

**Barra Edition → Edit patterns and curves…**

El editor de patrones y curvas centraliza la gestión de los datos temporales y funcionales que controlan el comportamiento dinámico del modelo: cómo varía la demanda a lo largo del día, cómo se comporta una bomba según su caudal, o cuál es el volumen de un depósito irregular.

<figure><img src="../assets/images/edicion/editor-curvas.png" alt="Editor de patrones y curvas de QGISRed"><figcaption><p>Editor de patrones y curvas de QGISRed</p></figcaption></figure>
*Editor de patrones y curvas: lista de elementos a la izquierda, gráfico y tabla de datos a la derecha.*

---

## Patrones de demanda (Patterns)

Un patrón define cómo multiplica la demanda base de un nudo (u otro parámetro) en cada intervalo de tiempo de la simulación.

### Estructura de un patrón

Cada patrón tiene:
- Un **ID** único (referenciado desde los nudos o bombas).
- Una lista de **factores multiplicadores**, uno por intervalo de tiempo.
- El **paso de tiempo del patrón** se define en las opciones de simulación; si el patrón tiene menos factores que intervalos de simulación, los valores se repiten cíclicamente.

### Ejemplo

Un patrón de 24 factores horarios para una simulación de 24 h:

```
ID: DomResidential
Factores: 0.4  0.3  0.3  0.3  0.4  0.7  1.1  1.3  1.2  1.0  0.9  0.9
          1.0  1.1  1.0  0.9  1.0  1.2  1.3  1.2  1.0  0.8  0.6  0.4
```

El nudo con demanda base 2.0 L/s y patrón `DomResidential` consume 0.8 L/s a las 0 h (2.0 × 0.4) y 2.6 L/s a las 7 h (2.0 × 1.3).

### Edición en el diálogo

1. Selecciona un patrón existente en la lista o pulsa **Nuevo** para crear uno.
2. Introduce los factores en la tabla (una fila por intervalo).
3. El gráfico se actualiza en tiempo real.
4. Puedes **importar factores desde CSV** (una columna de valores numéricos) usando el botón de importación.

---

## Curvas de comportamiento (Curves)

Las curvas relacionan dos magnitudes físicas. EPANET usa cuatro tipos:

### Curva H-Q de bomba (Pump curve)

Relaciona la **Altura manométrica** (Head, eje Y) con el **Caudal** (Flow, eje X). Define el punto de trabajo de la bomba a velocidad nominal.

| Nº de puntos | Método de ajuste |
|--------------|-----------------|
| 1 punto | QGISRed ajusta la curva estándar de EPANET: H₀ = 133% del punto, Q₀ dado, Hmax = 0 a 2×Q₀ |
| 3 puntos | Ajuste polinomial de segundo grado pasando por los tres puntos |
| N puntos | Interpolación lineal entre puntos (curva libre) |

> La curva H-Q debe tener **pendiente negativa** (mayor cabeza a menor caudal). EPANET avisará si la curva tiene pendiente positiva en algún tramo.

### Curva de eficiencia (Efficiency curve)

Relaciona la **Eficiencia** (%) con el **Caudal** (Flow). Se usa para el análisis de consumo energético. Si no se define, EPANET usa la eficiencia global del proyecto.

### Curva de volumen (Volume curve)

Relaciona el **Nivel** del depósito (m o ft, eje X) con el **Volumen** almacenado (m³ o galones, eje Y). Necesaria para depósitos con geometría no cilíndrica (piletas cónicas, depósitos de forma irregular).

### Curva de pérdida de carga GPV (Head loss curve)

Para válvulas de tipo **GPV** (General Purpose Valve), relaciona la **Pérdida de carga** (m o ft) con el **Caudal** (Flow). Permite modelar cualquier dispositivo de control hidráulico para el que se conozca la curva característica.

---

## Crear y editar curvas

1. Selecciona el tipo de curva en el selector superior.
2. Elige una curva existente en la lista o pulsa **Nueva**.
3. Introduce los pares de puntos (X, Y) en la tabla.
4. El gráfico muestra la curva resultante con la interpolación o ajuste correspondiente.
5. Pulsa **Aceptar** para guardar. Las curvas se almacenan en `{Red}_Options.dbf`.

> Para referenciar una curva desde una bomba o depósito, copia su **ID** exacto en el campo correspondiente del diálogo de propiedades del elemento.
