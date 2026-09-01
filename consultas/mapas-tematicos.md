# Mapas Temáticos

**Barra Queries → Thematic maps…**

Abre el diálogo de **Thematic Maps**, que genera capas que colorean tuberías y nudos por intervalos de un atributo hidráulico. A diferencia de otros diálogos de QGISRed, no hay que elegir "un campo y confirmar": cada atributo disponible tiene su propia casilla, y puedes marcar tantas a la vez como quieras — cada una genera su propia capa, y todas conviven en el mapa simultáneamente.

<!-- TODO: captura pendiente — diálogo Thematic Maps con las casillas de Tuberías y Nudos -->

---

## Elementos activos: tuberías y nudos

En la versión actual, **Thematic Maps trabaja sobre las capas Pipes (tuberías) y Junctions (nudos)**. Las opciones de otros tipos de elementos (válvulas, bombas, depósitos, embalses) están presentes en la interfaz pero se ocultan automáticamente porque aún no están implementadas. Los grupos **Service connections**, **Isolation valves** y **Meters** sí son visibles, pero su única casilla ("Temporary") tampoco está operativa todavía — no la marques.

---

## Proceso

1. Abre **Thematic maps** desde la barra Queries.
2. Marca las casillas de los atributos que quieras representar (puedes marcar varios de tuberías y de nudos a la vez).
3. Pulsa **Accept**. QGISRed crea una capa por cada casilla marcada, dentro del grupo **Queries → Thematic Maps** del panel de capas de QGIS.
4. Para quitar un mapa ya generado, vuelve a abrir el diálogo, desmarca su casilla y pulsa **Accept** — QGISRed elimina esa capa concreta sin tocar el resto. Las casillas de los mapas ya generados aparecen premarcadas.

> 💡 Puedes tener varios mapas temáticos abiertos a la vez (por ejemplo, Material y Año de Instalación de tuberías junto con Demanda Base de nudos) — cada uno es una capa independiente, no se sustituyen entre sí como ocurría antes.

---

## Campos disponibles para tuberías

| Campo | Descripción |
|-------|-------------|
| `Diameter` | Diámetro de la tubería |
| `Length` | Longitud |
| `Material` | Material de la tubería, coloreado con la paleta fija de QGISRed (ver tabla más abajo) |
| `Roughness` | Coeficiente de rugosidad — las clases y el fichero de estilo dependen de la **fórmula de pérdida de carga** activa en el proyecto (Hazen-Williams, Colebrook-White o Darcy-Weisbach) |
| `Age` | Antigüedad, calculada a partir del año de instalación; las clases se etiquetan con sufijo "yrs" |
| `Installation Year` | Año de instalación |

> Los mapas de **Age** e **Installation Year** añaden a la tabla de atributos de la capa tres columnas juntas: la fecha de instalación en bruto (`InstalDate`), el año extraído (`InstYear`) y la antigüedad calculada (`Age`) — verlas todas a la vez es útil aunque solo hayas marcado uno de los dos mapas.

---

## Campos disponibles para nudos

| Campo | Descripción |
|-------|-------------|
| `Elevation` | Cota del nudo. Las clases se calculan automáticamente a partir de los valores reales del proyecto (no hay rangos estándar) — la leyenda muestra los cortes con la unidad de longitud del proyecto (p. ej. "< 120 m", "120 < 180 m", ">= 180 m"). |
| `Total Base Demand` | Demanda base total del nudo. Los círculos tienen **tamaño proporcional** a la demanda (no lineal, para que los valores muy grandes no dominen visualmente el mapa), en clases calculadas también a partir de los datos reales, con la etiqueta en la unidad de caudal activa del proyecto. Si el nudo tiene varias categorías de demanda (ver [Demandas y escenarios](../herramientas/demandas-escenarios.md)), la capa refleja la suma agregada; los nudos con demanda cero no se muestran. |

---

## Paleta de materiales

El mapa de **Material** colorea cada tubería según el valor de su campo `Material`, comparándolo (sin distinguir mayúsculas/minúsculas) contra la abreviatura o el nombre de esta tabla fija — un material que no aparezca aquí recibe un color aleatorio en su lugar:

| Abrev. | Material | Abrev. | Material |
|--------|----------|--------|----------|
| FG | Fundición Gris | Pb | Plomo |
| FD | Fundición Dúctil | PVC | Policloruro de Vinilo |
| ACE | Acero | PE | Polietileno |
| INOX | Acero Inoxidable | PVC-O | PVC Orientado |
| FC | Fibrocemento | PVC-R | PVC Rígido |
| AGal | Acero Galvanizado | Cu | Cobre |
| HCCC | Hormigón con camisa de chapa | PE-AD | Polietileno Alta Densidad |
| HSCC | Hormigón sin camisa de chapa | PE-BD | Polietileno Baja Densidad |
| HAr | Hormigón Armado | PE-MD | Polietileno Media Densidad |
| HPr | Hormigón Pretensado | PRFV | Poliéster Reforzado con Fibra de Vidrio |

> Esta tabla de colores solo se aplica al estilo **por defecto** que trae QGISRed. Si guardas tu propia leyenda de Material desde el editor de leyendas (ver [Resumen y gestión de capas](../proyecto-activo/capas-y-leyenda.md)), tus colores prevalecen sobre esta paleta al volver a generar el mapa.

---

## Aviso de mapa desactualizado

Si cambias las **unidades**, la **fórmula de pérdida de carga** o las **unidades de caudal** del proyecto después de generar un mapa temático que dependa de ellas (Diámetro, Longitud, Rugosidad, Demanda Base…), QGISRed marca esa capa con un icono de aviso ⚠ en el panel de capas — el mismo icono que ya usa para avisar de resultados de simulación desactualizados.

- Pasa el ratón sobre el icono para ver el motivo.
- Haz clic sobre el icono para reconstruir esa capa con la configuración actual, sin tener que reabrir el diálogo.

---

## Resultado en el mapa

Cada casilla marcada genera su propia capa (por ejemplo `Pipe Materials`, `Junction Elevations`) dentro del grupo **Queries → Thematic Maps**. Las capas son de solo lectura y se actualizan solas cuando editas la tubería o el nudo de origen (no hace falta regenerar el mapa a mano tras un cambio puntual) — la leyenda de cada una muestra además cuántos elementos tiene cada clase.

Si vuelves a marcar y confirmar una casilla ya generada, QGISRed reemplaza esa capa concreta con la nueva configuración, sin tocar el resto de mapas activos.

---

## Notas de uso

- La generación de mapas temáticos no modifica ningún dato del modelo; solo crea capas nuevas con la simbología correspondiente.
- Para quitar un mapa, desmárcalo en el diálogo (ver "Proceso" más arriba) o elimina su capa directamente desde el panel de capas de QGIS.
- El mapa de **Total Base Demand** necesita que existan nudos con demanda asignada; si el proyecto no tiene demandas cargadas, la capa se genera vacía.
