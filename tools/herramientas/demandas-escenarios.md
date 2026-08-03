# Demandas y escenarios

Las tres herramientas del segundo grupo de la barra Tools gestionan la asignación masiva de demandas, los escenarios de simulación y la identificación de segmentos de aislamiento operacional.

***

## Nodal demand builder…

**Barra Tools → Nodal demand builder…**

Asigna consumos a los nudos de la red de forma masiva a partir de capas SHP externas cargadas en QGIS. Es la herramienta principal para integrar datos de facturación, censos de usuarios o estimaciones por polígono en el modelo EPANET.

\*Nodal demand builder: capas de origen detectadas automáticamente, configuración de campos y método de distribución.\*

### Fuentes de datos soportadas

| Tipo de geometría | Método de asignación                                                                                      |
| ----------------- | --------------------------------------------------------------------------------------------------------- |
| **Puntos**        | Cada punto se asigna al nudo más cercano. El valor de demanda se lee de un campo configurable de la capa. |
| **Polígonos**     | La demanda total del polígono se reparte entre todos los nudos que caen dentro de él.                     |
| **Líneas**        | La demanda de cada tramo se distribuye entre los nudos más cercanos a lo largo del eje.                   |

### Proceso

1. Carga en QGIS la capa SHP externa con los datos de consumo antes de abrir el gestor.
2. Activa **Nodal demand builder**. El diálogo detecta y lista automáticamente las capas externas.
3. Configura para cada capa:
   * **Campo de demanda**: columna con el valor de consumo.
   * **Campo de categoría**: para crear demandas múltiples por tipo de usuario (residencial, industrial, etc.).
   * **Campo de patrón**: ID del patrón de demanda a aplicar (opcional).
4. Opcionalmente selecciona nudos en el mapa para limitar la asignación a esa zona.
5. Confirma. QGISRed escribe los valores en `Junctions` o en `{Red}_MultipleDemands.shp` si hay categorías.

### Restricción a candidatos seleccionados

El diálogo ofrece dos opciones de restricción que pueden combinarse:

| Opción                                                 | Efecto                                                                                                                                                                                                                |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Restrict demand candidates to selected**             | Solo se consideran como candidatos a recibir demanda los **nudos (Junctions) actualmente seleccionados** en el mapa. Los demás nudos se ignoran aunque caigan dentro de la zona de influencia de un punto de consumo. |
| **Restrict service connection candidates to selected** | Solo se consideran como puntos de servicio candidatos las **acometidas (Service Connections) actualmente seleccionadas** en el mapa. Útil para reasignar demanda a acometidas concretas sin afectar al resto.         |

Ambas opciones son independientes y pueden activarse simultáneamente.

### Unidades de demanda personalizadas

Por defecto, el Builder interpreta los valores de demanda en las unidades de caudal del proyecto. Si los datos de origen usan unidades distintas, activa **Custom demand units** e introduce:

* **Units label**: etiqueta descriptiva de las unidades de origen (p. ej., `m³/mes`).
* **Conversion factor**: factor multiplicador para convertir a las unidades del proyecto (p. ej., si el proyecto usa L/s y los datos vienen en m³/mes: `1000 / 86400 / 30 ≈ 0.000386`).

El Builder aplica el factor automáticamente a todos los valores de consumo antes de asignarlos a los nudos.

### Resultado en el mapa

La capa resultante se muestra con colores por categoría y etiquetas con el valor de demanda. Los nudos sin categoría asignada aparecen en naranja bajo el grupo **Uncategorized**.

> 💡 Las capas auxiliares del Demand Builder (ConsumptionPoints, DemandLinks, Sectors…) también se pueden crear vacías desde el Gestor de Capas, sin necesidad de ejecutar antes un análisis (ver [Resumen y gestión de capas](../../proyecto/proyecto-activo/capas-y-leyenda.md)).

### Limpieza de demandas

El gestor permite borrar demandas existentes antes de asignar las nuevas:

* **Borrar demandas de nudos seleccionados**: elimina valores de `Demand` y entradas de `MultipleDemands`.
* **Eliminar patrones huérfanos**: elimina patrones que ya no estén referenciados por ningún nudo.

### Asignación de demanda desde capa de tramos

Cuando se usa una capa de tramos (geometría de línea) para distribuir demandas mediante el campo `%Dem`, los registros sin ese campo relleno reciben automáticamente el porcentaje restante hasta completar el 100 %, distribuido de forma proporcional entre ellos.

### Patrones por sectores

La sección de patrones por sectores permite asignar un patrón de demanda a cada sector de la red. Dispone de **dos modos excluyentes**:

| Modo                                         | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Import patterns from a sector theme**      | Selecciona la capa de polígonos con los sectores desde un combo desplegable que lista las capas de polígono ya cargadas en QGIS (o impórtala con el botón `...` si aún no está cargada). Después elige los campos **Sector Id (optional)**, **Id demand pattern** y **Priority (optional)** desde los combos correspondientes. El campo de Id de sector es opcional: si no se identifica, QGISRed genera identificadores internos automáticamente. Opcionalmente, guarda el resultado como capa interna del proyecto con el botón **Import and save**. Una vez guardado, esta opción queda bloqueada. |
| **Use patterns from a project sector theme** | Selecciona una capa de sectores ya cargada en el proyecto. Se muestra un listado con los sectores y, junto a cada uno, un combo **editable** para elegir el patrón: puedes seleccionar un patrón existente de la lista o escribir directamente el Id de un patrón nuevo. Los nudos sin sector se agrupan en un sector extra.                                                                                                                                                                                                                                                                          |

### Eficiencia por sectores

La sección de eficiencia hidráulica por sectores también presenta **dos modos excluyentes**:

| Modo                                             | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Import efficiencies from a sector theme**      | Selecciona la capa de polígonos con los sectores desde un combo desplegable que lista las capas de polígono ya cargadas en QGIS (o impórtala con el botón `...`), y elige los campos **Sector Id (optional)**, **Efficiency** y **Priority (optional)**. El campo de Id de sector es opcional. Opcionalmente, guarda el resultado como capa interna del proyecto con el botón **Import and save**. Una vez guardado, la opción de importar queda bloqueada. |
| **Use efficiencies from a project sector theme** | Selecciona una capa de sectores existente; el plugin identifica automáticamente los campos de eficiencia.                                                                                                                                                                                                                                                                                                                                                   |

#### Correcciones de eficiencia y patrones

Tras definir las eficiencias por sectores, el gestor ofrece opciones adicionales de corrección:

* **Corregir eficiencias de categorías para cumplir la eficiencia de sectores**: ajusta proporcionalmente las eficiencias de cada categoría de demanda para que la eficiencia resultante en cada sector coincida con el objetivo declarado. Excluyente con la corrección hacia eficiencia global.
* **Corregir patrones de sectores para cumplir el patrón global**: tras asignar patrones por sectores, corrige esos patrones para que su combinación cumpla con el patrón global previamente declarado. Las opciones de corrección se desglosan por ámbito del patrón (global o por categoría).

### Capa de acometidas aisladas con demanda

Al ejecutar el análisis de segmentos aislados o de sectores hidráulicos, el plugin genera una capa adicional con las **acometidas que tienen demanda asignada pero pertenecen a sectores hidráulicos aislados** (sin suministro). Esta capa se representa con marcadores circulares de contorno rojo e incluye los campos `Id`, `BaseDemand` y `Category`.

***

## Scenario builder…

**Barra Tools → Scenario builder…**

Exporta e importa en bloque parámetros del modelo, creando "fotografías" del estado de la red que pueden restaurarse en cualquier momento. Es la herramienta para gestionar variantes del modelo sin duplicar proyectos.

### Parámetros que gestiona

| Parámetro       | Descripción                                       |
| --------------- | ------------------------------------------------- |
| **Roughness**   | Coeficientes de rugosidad de todas las tuberías   |
| **InitStatus**  | Estados de apertura/cierre de tuberías y válvulas |
| **Demands**     | Demandas base de todos los nudos                  |
| **InitQuality** | Calidades iniciales de nudos y tuberías           |
| **Elevations**  | Cotas de nudos, depósitos y embalses              |

### Flujo de trabajo típico

1. Construye el modelo en el estado actual (año base).
2. Exporta el escenario base con **Scenario builder → Exportar**.
3. Modifica el modelo para el horizonte futuro (nuevas demandas, tuberías envejecidas, etc.).
4. Exporta el escenario futuro con otro nombre.
5. Para comparar o restaurar, usa **Scenario builder → Importar** y selecciona el escenario deseado.

Los archivos de escenario se guardan como CSV en la carpeta del proyecto.

***

## Isolated segments…

**Barra Tools → Isolated segments…**

Responde a la pregunta operacional: **"¿Qué válvulas debo cerrar para reparar esta tubería, y qué usuarios quedarán sin servicio?"**

\*En rojo la tubería a reparar, en amarillo las válvulas a cerrar y en azul la zona sin servicio.\*

### Proceso

1. Activa la herramienta y haz clic sobre la tubería a reparar o aislar.
2. QGISRed calcula el **segmento mínimo** que quedaría aislado al cerrar las válvulas manuales más cercanas e identifica los afectados colaterales.
3. El resultado se muestra en el mapa:
   * **Tubería objetivo**: en rojo.
   * **Válvulas a cerrar**: en amarillo.
   * **Zona sin servicio** (afectados colaterales): en azul.
4. Puedes hacer clic en más tuberías dentro de la misma sesión para acumular el análisis.

Se genera la capa auxiliar `IsolatedSegments` con toda la información. No modifica el modelo.
