# Demandas y Escenarios

Las tres herramientas del segundo grupo de la barra Tools gestionan la asignación masiva de demandas, los escenarios de simulación y la identificación de segmentos de aislamiento operacional.

---

## Nodal demand builder…

**Barra Tools → Nodal demand builder…**

Asigna consumos a los nudos de la red de forma masiva a partir de capas SHP externas cargadas en QGIS. Es la herramienta principal para integrar datos de facturación, censos de usuarios o estimaciones por polígono en el modelo EPANET.

![Diálogo del Nodal demand builder con opciones de fuente y método de asignación](../assets/images/herramientas/demand-builder.png)
*Nodal demand builder: capas de origen detectadas automáticamente, configuración de campos y método de distribución.*

### Fuentes de datos soportadas

| Tipo de geometría | Método de asignación |
|-------------------|----------------------|
| **Puntos** | Cada punto se asigna al nudo más cercano. El valor de demanda se lee de un campo configurable de la capa. |
| **Polígonos** | La demanda total del polígono se reparte entre todos los nudos que caen dentro de él. |
| **Líneas** | La demanda de cada tramo se distribuye entre los nudos más cercanos a lo largo del eje. |

### Proceso

1. Carga en QGIS la capa SHP externa con los datos de consumo antes de abrir el gestor.
2. Activa **Nodal demand builder**. El diálogo detecta y lista automáticamente las capas externas.
3. Configura para cada capa:
   - **Campo de demanda**: columna con el valor de consumo.
   - **Campo de categoría**: para crear demandas múltiples por tipo de usuario (residencial, industrial, etc.).
   - **Campo de patrón**: ID del patrón de demanda a aplicar (opcional).
4. Opcionalmente selecciona nudos en el mapa para limitar la asignación a esa zona.
5. Confirma. QGISRed escribe los valores en `Junctions` o en `{Red}_MultipleDemands.shp` si hay categorías.

### Resultado en el mapa

La capa resultante se muestra con colores por categoría y etiquetas con el valor de demanda. Los nudos sin categoría aparecen en naranja (`Undefined`).

### Limpieza de demandas

El gestor permite borrar demandas existentes antes de asignar las nuevas:
- **Borrar demandas de nudos seleccionados**: elimina valores de `Demand` y entradas de `MultipleDemands`.
- **Eliminar patrones huérfanos**: elimina patrones que ya no estén referenciados por ningún nudo.

---

## Scenario builder…

**Barra Tools → Scenario builder…**

Exporta e importa en bloque parámetros del modelo, creando "fotografías" del estado de la red que pueden restaurarse en cualquier momento. Es la herramienta para gestionar variantes del modelo sin duplicar proyectos.

### Parámetros que gestiona

| Parámetro | Descripción |
|-----------|-------------|
| **Roughness** | Coeficientes de rugosidad de todas las tuberías |
| **InitStatus** | Estados de apertura/cierre de tuberías y válvulas |
| **Demands** | Demandas base de todos los nudos |
| **InitQuality** | Calidades iniciales de nudos y tuberías |
| **Elevations** | Cotas de nudos, depósitos y embalses |

### Flujo de trabajo típico

1. Construye el modelo en el estado actual (año base).
2. Exporta el escenario base con **Scenario builder → Exportar**.
3. Modifica el modelo para el horizonte futuro (nuevas demandas, tuberías envejecidas, etc.).
4. Exporta el escenario futuro con otro nombre.
5. Para comparar o restaurar, usa **Scenario builder → Importar** y selecciona el escenario deseado.

Los archivos de escenario se guardan como CSV en la carpeta del proyecto.

---

## Isolated segments…

**Barra Tools → Isolated segments…**

Responde a la pregunta operacional: **"¿Qué válvulas debo cerrar para reparar esta tubería, y qué usuarios quedarán sin servicio?"**

![Resultado de Isolated segments: tubería afectada, válvulas de corte y zona sin servicio](../assets/images/herramientas/isolated-segments.png)
*En rojo la tubería a reparar, en amarillo las válvulas a cerrar y en azul la zona sin servicio.*

### Proceso

1. Activa la herramienta y haz clic sobre la tubería a reparar o aislar.
2. QGISRed calcula el **segmento mínimo** que quedaría aislado al cerrar las válvulas manuales más cercanas e identifica los afectados colaterales.
3. El resultado se muestra en el mapa:
   - **Tubería objetivo**: en rojo.
   - **Válvulas a cerrar**: en amarillo.
   - **Zona sin servicio** (afectados colaterales): en azul.
4. Puedes hacer clic en más tuberías dentro de la misma sesión para acumular el análisis.

Se genera la capa auxiliar `IsolatedSegments` con toda la información. No modifica el modelo.
