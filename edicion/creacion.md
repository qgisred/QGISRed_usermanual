# Creación de Elementos

Las cinco primeras herramientas de la barra Edition permiten añadir elementos a la red. Todas activan un **modo de edición interactivo**: el cursor cambia y el plugin espera una acción sobre el mapa. Para cancelar sin crear nada, pulsa de nuevo el mismo botón o presiona `Esc`.

---

## Añadir tubería (Add pipe)

**Barra Edition → Add pipe**

Modo de dibujo lineal: cada clic añade un vértice a la tubería. La herramienta permanece activa hasta que termines el trazado.

![Herramienta Add pipe en acción sobre el mapa de QGIS](../assets/images/edicion/add-pipe.png)
*Dibujando una tubería: la línea roja provisional sigue el cursor hasta el siguiente clic.*

### Proceso

1. Activa la herramienta. El cursor cambia a modo dibujo.
2. Haz clic para fijar el **punto inicial**. QGISRed crea automáticamente un nudo (Junction) en ese punto si no existe ninguno en el radio de tolerancia.
3. Haz clic para añadir **vértices intermedios** (puntos de quiebre del trazado).
4. Haz **doble clic** o pulsa el **botón derecho** para finalizar la tubería. QGISRed crea un segundo nudo en el punto final.

### Qué crea QGISRed al confirmar

- Un registro en `{Red}_Pipes.shp` con la geometría dibujada.
- Hasta dos nudos nuevos en `{Red}_Junctions.shp` (uno por extremo), si no existía ya un nudo dentro de la tolerancia configurada.
- Los valores de diámetro, rugosidad y demanda se toman de los **Valores por defecto** del proyecto.

### Conectar a elementos existentes

Si el punto inicial o final cae dentro de la tolerancia de un nudo, válvula, bomba, depósito o embalse existente, la nueva tubería **se conecta a ese elemento** en lugar de crear un nudo nuevo.

> El ajuste al nudo más cercano usa la tolerancia configurada en **Barra Project → Valores por defecto → Tolerancia de nudo**. Puedes revisar o cambiarla antes de dibujar redes densas.

---

## Añadir depósito (Add tank)

**Barra Edition → Add tank**

Coloca un depósito de almacenamiento (Tank) en el mapa. Los depósitos tienen nivel variable y participan en la simulación hidráulica.

### Proceso

1. Activa la herramienta. El cursor muestra el icono de depósito.
2. Haz clic sobre un **nudo existente** o sobre un punto vacío del mapa.
   - Si haces clic sobre un nudo existente, ese nudo se **convierte** en Tank.
   - Si haces clic en un punto vacío, QGISRed crea un Tank nuevo (sin conexión inicial; necesitarás conectarlo con una tubería).
3. QGISRed abre el diálogo de propiedades del nuevo depósito para que introduzcas los datos (cota de fondo, nivel inicial, nivel mínimo, nivel máximo, diámetro).

### Parámetros principales del depósito

| Parámetro | Descripción |
|-----------|-------------|
| **Elevation** | Cota del fondo del depósito (m o ft) |
| **InitLevel** | Nivel inicial del agua por encima del fondo |
| **MinLevel** | Nivel mínimo de operación |
| **MaxLevel** | Nivel máximo de operación |
| **Diameter** | Diámetro del depósito (para sección circular); si usa curva de volumen, poner 0 |
| **MinVol** | Volumen mínimo (opcional) |
| **VolCurve** | ID de la curva de volumen (para geometría no cilíndrica) |

---

## Añadir embalse (Add reservoir)

**Barra Edition → Add reservoir**

Coloca un embalse o punto de alimentación externo (Reservoir). A diferencia del Tank, el Reservoir tiene **nivel fijo** (carga piezométrica constante) y representa una fuente de agua de capacidad ilimitada.

El proceso es idéntico al del depósito. Los parámetros son más simples:

| Parámetro | Descripción |
|-----------|-------------|
| **Head** | Carga piezométrica fija (cota del nivel libre del agua, m o ft) |
| **Pattern** | Patrón de variación de carga a lo largo del tiempo (opcional) |

> Usa embalses para representar puntos de entrega de agua en alta (conexiones con sistemas externos) o puntos de suministro de caudal constante.

---

## Insertar válvula en tubería (Insert valve in pipe)

**Barra Edition → Insert valve in pipe**

Inserta una válvula dentro de una tubería existente. La tubería original se **divide en dos tramos** que quedan conectados a través de la válvula.

![Resultado de insertar una válvula: la tubería original queda dividida en dos](../assets/images/edicion/insert-valve.png)
*La tubería P-12 original queda dividida en P-12 y P-13, con la válvula V-1 entre ellas.*

### Proceso

1. Activa la herramienta. El cursor cambia al icono de válvula.
2. Haz clic sobre la tubería donde quieres insertar la válvula.
3. QGISRed determina el punto exacto de inserción (proyección del clic sobre el eje de la tubería) y:
   - Crea un nudo en ese punto.
   - Divide la tubería original en dos tramos con los mismos atributos de diámetro y material.
   - Crea la válvula entre los dos nuevos extremos.
4. Se abre el diálogo de propiedades para configurar el tipo y ajuste de la válvula.

### Tipos de válvula disponibles

| Tipo | Nombre | Función |
|------|--------|---------|
| **PRV** | Pressure Reducing Valve | Reduce la presión aguas abajo al valor de consigna |
| **PSV** | Pressure Sustaining Valve | Mantiene la presión aguas arriba al valor de consigna |
| **PBV** | Pressure Breaker Valve | Produce una pérdida de carga fija |
| **FCV** | Flow Control Valve | Limita el caudal al valor de consigna |
| **TCV** | Throttle Control Valve | Simula una válvula parcialmente cerrada mediante un coeficiente de pérdidas |
| **GPV** | General Purpose Valve | Pérdida de carga definida por una curva personalizada |

---

## Insertar bomba en tubería (Insert pump in pipe)

**Barra Edition → Insert pump in pipe**

Inserta una bomba en una tubería existente, dividiéndola exactamente igual que con válvulas.

### Proceso

1. Activa la herramienta y haz clic sobre la tubería.
2. QGISRed divide la tubería y crea la bomba entre los dos tramos resultantes.
3. Se abre el diálogo de propiedades para configurar la curva H-Q y la velocidad inicial.

### Parámetros de la bomba

| Parámetro | Descripción |
|-----------|-------------|
| **Curve** | ID de la curva H-Q (obligatorio para simular) |
| **Speed** | Factor de velocidad inicial (1.0 = velocidad nominal) |
| **Pattern** | Patrón de variación de velocidad |
| **Power** | Potencia constante (alternativa a la curva H-Q) |

> Si la bomba necesita una curva de eficiencia para el cálculo de energía, defínela en el **Editor de patrones y curvas** y referencíala desde las propiedades de la bomba.
