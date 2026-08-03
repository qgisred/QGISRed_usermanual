#  de Sectores de Demanda

**Barra Tools → Demand Sector Builder…**

El **Demand Sector Builder** es un diálogo modal que permite crear y gestionar múltiples **sectorizaciones con nombre** de la red

\*Demand Sector Builder: lista de sectorizaciones (panel izquierdo), parámetros de detección y temas a generar (panel derecho).\*, cada una con sus propios sectores de demanda. Cada sectorización agrupa los nudos de la red en zonas según la topología y los límites definidos por el usuario, y genera las capas auxiliares necesarias para usarlas en el Nodal Demand Builder o para análisis de balance hídrico.

***

## Conceptos clave

| Concepto          | Descripción                                                                                                                       |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Sectorización** | Conjunto con nombre de sectores que cubre toda la red. Puede haber múltiples sectorizaciones en el mismo proyecto.                |
| **Sector**        | Subconjunto de nudos y enlaces delimitado por fronteras. Cada nudo pertenece exactamente a un sector dentro de una sectorización. |
| **Tema**          | Tipo de capa geométrica que representa los sectores. El Builder puede generar hasta 6 tipos de tema para cada sectorización.      |
| **Frontera**      | Elemento o conjunto de elementos que delimita dos sectores adyacentes (tuberías de frontera, válvulas, caudalímetros).            |

***

## Crear y gestionar sectorizaciones

### Lista de sectorizaciones

El panel izquierdo del diálogo muestra todas las sectorizaciones del proyecto. Cada entrada tiene:

* Nombre editable.
* Botones Añadir (＋) y Eliminar (✕).

### Añadir una sectorización

1. Pulsa **＋** en la lista de sectorizaciones.
2. Introduce un nombre descriptivo (p. ej., `Sectorizacion_2024`, `Zonas_Presion`).
3. Configura los parámetros de detección y los temas a generar.
4. Pulsa **Build** para ejecutar el análisis.

Las sectorizaciones se almacenan en las capas auxiliares del proyecto bajo el grupo **Auxiliary Layers > DemandSectors**.

***

## Detección de sectores

El Builder detecta los sectores mediante un **algoritmo BFS** (búsqueda en anchura) que recorre la topología de la red partiendo de los elementos frontera marcados.

### Tipos de frontera

| Tipo                 | Descripción                                                                   |
| -------------------- | ----------------------------------------------------------------------------- |
| **Pipes**            | Tuberías marcadas como frontera; el flujo a través de ellas delimita sectores |
| **Isolation Valves** | Válvulas de aislamiento en la red                                             |
| **Meters**           | Caudalímetros (delimitan sectores de balance hídrico)                         |

La selección de qué tipo de elemento actúa como frontera se configura mediante checkboxes en el diálogo. Pueden activarse varios tipos simultáneamente.

### Tolerancia geométrica

El Builder utiliza una tolerancia de **0.01 unidades de mapa** para verificar la coincidencia geométrica entre nodos y elementos de frontera. Los nodos que no coincidan exactamente con la red pero estén dentro de este margen se consideran conectados.

***

## Temas generados

Para cada sectorización, el Builder puede generar hasta **6 tipos de tema**:

| Tema           | Geometría  | Descripción                                                                 |
| -------------- | ---------- | --------------------------------------------------------------------------- |
| **Frontiers**  | Líneas     | Elementos frontera entre sectores adyacentes                                |
| **Links**      | Líneas     | Tuberías y enlaces interiores de cada sector                                |
| **Nodes**      | Puntos     | Nudos de la red con el campo `SectorId` asignado                            |
| **Polygons**   | Polígonos  | Envolvente geométrica convexa de cada sector                                |
| **MultiLinks** | Multilínea | Todos los enlaces de un sector fusionados en una única geometría por sector |
| **MultiNodes** | Multipunto | Todos los nudos de un sector fusionados en una única geometría por sector   |

Los temas a generar se seleccionan individualmente con checkboxes antes de pulsar **Build**. Al menos un tema debe estar activo.

***

## Validaciones de integridad

Antes de generar los sectores, el Builder ejecuta **7 comprobaciones de integridad**:

1. La red tiene al menos un nudo.
2. Existen elementos frontera del tipo seleccionado.
3. No hay nudos aislados (sin conectividad).
4. Los elementos frontera tienen asignados los campos necesarios.
5. No hay sectores vacíos (sin nudos).
6. Cada nudo pertenece a exactamente un sector.
7. Los polígonos generados no se solapan.

Si alguna validación falla, el diálogo muestra un mensaje de error descriptivo y no genera las capas.

***

## Resultado en el proyecto

Las capas de cada sectorización se crean dentro del grupo **Auxiliary Layers > DemandSectors > \[nombre de la sectorización]** en el panel de capas de QGIS. Cada capa de tipo Nodes incluye el campo `SectorId` que puede utilizarse directamente en el **Nodal Demand Builder** para asignar patrones o eficiencias por sector.

### Uso en el Nodal Demand Builder

Una sectorización generada con el Demand Sector Builder puede seleccionarse en el Nodal Demand Builder mediante la opción **"Usar tema de sectores del proyecto"**, evitando la necesidad de importar un SHP externo. Ver [Demandas y escenarios](demandas-escenarios.md) para más detalles.

***

## Flujo de trabajo típico

1. **Definir fronteras**: en la capa Pipes (o Meters), marca como frontera los elementos que delimitan los sectores (campo `IsFrontier` o equivalente, o mediante selección).
2. **Abrir el Builder**: Tools → Demand Sector Builder.
3. **Crear sectorización**: pulsa ＋, ponle nombre y selecciona los temas a generar.
4. **Ejecutar**: pulsa **Build**. Las capas aparecen en Auxiliary Layers > DemandSectors.
5. **Usar en Nodal Demand Builder**: en la sección de patrones o eficiencias por sectores, elige la nueva sectorización como tema del proyecto.
