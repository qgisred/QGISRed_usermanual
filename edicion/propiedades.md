# Propiedades de Elementos

**Barra Edition → Edit element properties…**

El diálogo de propiedades es la herramienta central para ver y editar todos los atributos de cualquier elemento de la red. Funciona como un formulario inteligente que carga los datos del elemento pulsado y permite navegar entre elementos sin cerrarlo.

![Diálogo de propiedades de una tubería con todos sus campos](../assets/images/edicion/propiedades-elemento.png)
*Diálogo de propiedades: atributos del elemento, navegador de elementos conectados y botón de centrado.*

---

## Cómo abrir el diálogo

1. Activa la herramienta pulsando el botón **Edit element properties…** (icono de lápiz/editar).
2. Haz clic sobre cualquier elemento de la red en el mapa: tubería, nudo, válvula, bomba, depósito o embalse.
3. El diálogo se abre mostrando todos los atributos del elemento seleccionado.

> La herramienta permanece activa mientras el botón esté pulsado. Puedes ir haciendo clic sobre diferentes elementos sin volver a activarla.

---

## Campos de las tuberías (Pipes)

| Campo | Descripción |
|-------|-------------|
| **ID** | Identificador único de la tubería |
| **Length** | Longitud calculada automáticamente a partir de la geometría (m o ft) |
| **Diameter** | Diámetro interior (mm o pulgadas) |
| **Roughness** | Rugosidad para la fórmula de pérdida de carga configurada |
| **MinorLoss** | Coeficiente de pérdidas menores (0 si no aplica) |
| **InitStatus** | Estado inicial: Open, Closed o CV (Check Valve) |
| **Material** | Código del material (referenciado en la Tabla de materiales) |
| **InstallYear** | Año de instalación (formato `YYYY`), usado para calcular la rugosidad por envejecimiento |
| **BulkCoeff** | Coeficiente de reacción en masa (para modelos de calidad de tipo Chemical) |
| **WallCoeff** | Coeficiente de reacción en pared (para modelos de calidad de tipo Chemical) |

---

## Campos de los nudos (Junctions)

| Campo | Descripción |
|-------|-------------|
| **ID** | Identificador único del nudo |
| **Elevation** | Cota del nudo (m o ft) |
| **Demand** | Demanda base (en las unidades de caudal del proyecto) |
| **Pattern** | ID del patrón de demanda aplicado |
| **EmitterCoeff** | Coeficiente de emisor (para modelar fugas dependientes de presión) |
| **InitQuality** | Concentración o edad del agua inicial (solo si el modelo de calidad está activo) |

### Demandas múltiples

Los nudos pueden tener más de una demanda (categorías de usuario: residencial, industrial, etc.). Si el proyecto tiene la capa opcional `{Red}_MultipleDemands.shp`, el diálogo muestra un apartado adicional donde puedes añadir, editar y eliminar demandas por categoría:

| Campo | Descripción |
|-------|-------------|
| **Demand** | Valor de demanda para esta categoría |
| **Pattern** | Patrón de demanda específico de la categoría |
| **Name** | Etiqueta de la categoría (informativa) |

---

## Campos de los depósitos (Tanks)

| Campo | Descripción |
|-------|-------------|
| **ID** | Identificador único |
| **Elevation** | Cota del fondo del depósito |
| **InitLevel** | Nivel inicial del agua sobre el fondo |
| **MinLevel** | Nivel mínimo operativo |
| **MaxLevel** | Nivel máximo operativo |
| **Diameter** | Diámetro del depósito (0 si usa curva de volumen) |
| **MinVol** | Volumen mínimo (m³) |
| **VolCurve** | ID de la curva de volumen (para geometría no cilíndrica) |
| **MixModel** | Modelo de mezcla: MIXED, 2COMP, FIFO, LIFO |
| **MixFraction** | Fracción del primer compartimento (modelo 2COMP) |

---

## Campos de los embalses (Reservoirs)

| Campo | Descripción |
|-------|-------------|
| **ID** | Identificador único |
| **Head** | Carga piezométrica fija (m o ft) |
| **Pattern** | Patrón de variación de carga a lo largo del tiempo |

---

## Campos de las válvulas (Valves)

| Campo | Descripción |
|-------|-------------|
| **ID** | Identificador único |
| **Diameter** | Diámetro (mm o pulgadas) |
| **Type** | Tipo de válvula: PRV, PSV, PBV, FCV, TCV, GPV |
| **Setting** | Consigna de regulación (presión, caudal o pérdida de carga según el tipo) |
| **MinorLoss** | Coeficiente de pérdidas menores |
| **InitStatus** | Estado inicial: Open, Closed, Active |

---

## Campos de las bombas (Pumps)

| Campo | Descripción |
|-------|-------------|
| **ID** | Identificador único |
| **Curve** | ID de la curva H-Q de la bomba |
| **Speed** | Factor de velocidad de giro (1.0 = nominal) |
| **Pattern** | Patrón de variación de velocidad |
| **Power** | Potencia constante (alternativa a la curva H-Q) |
| **EfficiencyCurve** | ID de la curva de eficiencia (para análisis de energía) |
| **EnergyPrice** | Precio de la energía específico para esta bomba |
| **PricePattern** | Patrón de variación de precio de energía |
| **InitStatus** | Estado inicial: Open o Closed |

---

## Navegación entre elementos

El diálogo incluye un **navegador** (Browser) que permite:

- **Ir a elemento conectado**: lista los nudos y elementos conectados al elemento actual para saltar a ellos.
- **Historial**: botones Anterior / Siguiente para volver a elementos visitados anteriormente sin cerrar el diálogo.
- **Centrar en mapa**: botón para desplazar el mapa al elemento actualmente mostrado.

> Al navegar a otro elemento desde el diálogo, QGISRed guarda los cambios del elemento anterior antes de cargar el nuevo. No es necesario pulsar "Aceptar" explícitamente tras cada modificación.

---

## Campos exclusivos de QGISRed

Estos campos no forman parte del estándar EPANET pero son usados por el plugin:

| Campo | Capa | Descripción |
|-------|------|-------------|
| **Material** | Pipes | Código de material referenciado en la Tabla de materiales |
| **InstallYear** | Pipes | Año de instalación para cálculo de rugosidad por envejecimiento |
| **IsActive** | Varios | Habilita/deshabilita el elemento en el Gemelo Digital |
| **Tag** | Todos | Etiqueta libre (equivalente al campo TAG de EPANET) |
