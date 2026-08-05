# Element Explorer

El **Element Explorer** es un panel flotante (dock) que QGISRed mantiene como instancia única. Agrupa dos funcionalidades relacionadas en sendas pestañas: búsqueda de elementos por ID y visualización de propiedades del elemento seleccionado en el mapa.

\*Panel Element Explorer: pestaña Find Elements (izquierda) y pestaña Properties (derecha).\*

Los botones **Find elements by ID** y **Element properties** de la barra Queries abren este mismo panel y activan la pestaña correspondiente. Cambiar de pestaña dentro del panel no cierra ninguna funcionalidad.

***

## Pestaña Find Elements — Buscar por ID

**Barra Queries → Find elements by ID…**

Localiza cualquier elemento de la red escribiendo su ID y lo resalta en el mapa.

### Elementos que se pueden buscar

* Pipes, Junctions, Demands, Reservoirs, Tanks, Pumps, Valves, Sources

### Proceso

1. Activa **Find elements by ID**. El panel se abre o se trae al frente.
2. Selecciona el tipo de elemento en el desplegable de capa.
3. Escribe el ID en el campo de texto y pulsa **Find** o Intro.
4. QGISRed centra el mapa en el elemento y lo resalta. El resultado aparece en el panel con fondo amarillo claro.

### Búsqueda múltiple

Separa varios IDs con coma o punto y coma para resaltarlos todos simultáneamente.

### Si el ID no existe

El panel muestra un aviso y el mapa no cambia.

***

## Pestaña Properties — Propiedades del elemento

**Barra Queries → Element properties…**

Activa una herramienta de identificación interactiva: al hacer clic sobre cualquier elemento del mapa, el panel muestra todos sus atributos en la pestaña Properties.

### Proceso

1. Activa **Element properties**. El cursor cambia a modo identificación.
2. Haz clic sobre cualquier elemento de la red.
3. El panel muestra los campos del elemento pulsado. Puedes seguir haciendo clic en otros elementos sin desactivar la herramienta.

### Información mostrada

Los atributos se organizan según el tipo de elemento. Para una **tubería** típica:

| Campo         | Descripción                 |
| ------------- | --------------------------- |
| `Id`          | Identificador único         |
| `Length`      | Longitud (m)                |
| `Diameter`    | Diámetro (mm)               |
| `Roughness`   | Coeficiente de rugosidad    |
| `Material`    | Material                    |
| `InstallYear` | Año de instalación          |
| `Status`      | Estado (Open / Closed / CV) |
| `Tag`         | Etiqueta libre              |

Para **nudos** se muestran `Elevation`, `Demand`, `Pattern`, `InitQuality`, etc. Cada tipo de elemento tiene su propio conjunto de campos.

Para **válvulas**, el campo `Type`/`ValveType` se muestra con su abreviatura en español (VRP, VSP, VRC, VCQ, VRG, VPG, VR) en lugar del código EPANET (PRV, PSV, PBV, FCV, TCV, GPV, CV).

Si el proyecto tiene resultados de simulación cargados, el panel añade una sección con los valores calculados (presión, caudal, velocidad…) para el período activo en el visor de resultados. El instante simulado se indica con el prefijo **Time:** seguido del valor en negrita en formato `HH:MM:SS`.

> ⚠️ **Campos de calidad condicionales.** El campo `Quality` solo aparece cuando el modelo de calidad del proyecto no es _None_. El campo `ReactRate` únicamente es visible cuando el modelo de calidad es _Chemical_; permanece oculto para los modelos _None_, _Age_ y _Trace_. Estos campos solo se muestran cuando el modelo de calidad del proyecto los soporta.

### Notas de uso

* Al desactivar el botón, el cursor vuelve al modo de navegación estándar de QGIS.
* Si haces clic en una zona sin elementos, el panel conserva la última selección.
* El fondo del panel tiene un tinte amarillo claro para diferenciarlo del resto de paneles de QGIS.
* Los clics sobre capas que no pertenecen al proyecto QGISRed activo (capas de fondo, capas auxiliares externas, etc.) son ignorados: el panel no actualiza su contenido.

### Resolución del campo ID por capa

QGISRed resuelve automáticamente el **nombre del campo identificador** de cada capa de la red mediante la función interna `getIdFieldName(layer)`. Esto permite que el plugin detecte correctamente el ID en capas con convenciones de nomenclatura distintas:

| Tipo de capa | Campo ID típico |
| ------------ | --------------- |
| Pipes        | `PipeID`        |
| Junctions    | `JunctionID`    |
| Tanks        | `TankID`        |
| Reservoirs   | `ReservoirID`   |
| Pumps        | `PumpID`        |
| Valves       | `ValveID`       |

Si el proyecto usa convenciones de nomenclatura personalizadas, la resolución automática evita errores de búsqueda o identificación. No es necesario configurar nada manualmente: el explorador detecta el campo correcto al activarse sobre cualquier capa de la red.

### Alias de campo adicionales reconocidos automáticamente

El panel reconoce automáticamente los siguientes alias de campo y los presenta con etiqueta, unidades y decimales correctos sin ninguna configuración adicional:

| Alias        | Descripción                                                                                            |
| ------------ | ------------------------------------------------------------------------------------------------------ |
| `DemPattID`  | Patrón de demanda en nudos; se suprime cuando hay demandas múltiples activas y se agrupa correctamente |
| `HedPattID`  | Patrón de curva de altura en bombas                                                                    |
| `QualPattID` | Patrón de calidad en fuentes                                                                           |
| `NodeID`     | Identificador de nudo en capas derivadas                                                               |
| `NodeType`   | Tipo de nudo                                                                                           |
| `LinkID`     | Identificador de enlace en capas derivadas                                                             |
| `LinkType`   | Tipo de enlace                                                                                         |

> ℹ️ El reconocimiento es automático: el explorador detecta el alias correcto al activarse sobre cualquier capa de la red, sin necesidad de configurar nada manualmente.
