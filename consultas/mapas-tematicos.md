# Mapas Temáticos

**Barra Queries → Thematic maps…**

Abre el diálogo de **Thematic Maps**, que genera una representación visual de la red coloreando las tuberías por intervalos de cualquier atributo hidráulico o de resultado de simulación.

<figure><img src="../assets/images/consultas/thematic-maps-dialog.png" alt="Diálogo de Thematic Maps con selector de campo y rango de colores"><figcaption><p>Diálogo de Thematic Maps con selector de campo y rango de colores</p></figcaption></figure>
*Diálogo Thematic Maps: selección de campo, número de clases y paleta de color.*

---

## Elemento activo: tuberías

En la versión actual, **Thematic Maps trabaja exclusivamente sobre la capa Pipes (tuberías)**. Las opciones de otros tipos de elementos (nudos, válvulas, bombas, depósitos, embalses) están presentes en la interfaz pero se ocultan automáticamente porque aún no están implementadas. Cuando estén disponibles, el diálogo mostrará un selector de tipo de elemento.

---

## Proceso

1. Abre **Thematic maps** desde la barra Queries.
2. Selecciona el **campo a representar** en el desplegable (atributo de entrada o resultado de simulación).
3. Elige el **número de clases** de color.
4. Selecciona la **paleta de color** (degradado de una sola gama o bicromático).
5. Configura el **rango** si quieres excluir valores extremos.
6. Confirma. QGISRed genera la capa `ThematicPipes` en el grupo de capas temáticas del panel de capas de QGIS.

---

## Campos disponibles para tuberías

### Atributos de entrada del modelo

| Campo | Descripción |
|-------|-------------|
| `Diameter` | Diámetro de la tubería (mm) |
| `Length` | Longitud (m) |
| `Roughness` | Coeficiente de rugosidad |
| `InstallYear` | Año de instalación |

### Resultados de simulación

Disponibles solo si hay resultados cargados en el proyecto:

| Campo | Descripción |
|-------|-------------|
| `Flow` | Caudal (l/s o unidad configurada) |
| `Velocity` | Velocidad (m/s) |
| `HeadLoss` | Pérdida de carga (m) |
| `UnitHdLoss` | Pérdida unitaria (m/km) |
| `FricFactor` | Factor de fricción |
| `ReactRate` | Tasa de reacción (modelos de calidad) |
| `Quality` | Calidad del agua |

---

## Resultado en el mapa

La herramienta genera la capa **`ThematicPipes`** dentro de un grupo de capas temáticas de QGISRed. La leyenda de colores se muestra directamente en el panel de capas de QGIS.

Si ejecutas Thematic Maps de nuevo, la capa anterior se reemplaza con la nueva configuración.

---

## Notas de uso

- La generación de mapas temáticos no modifica ningún dato del modelo; solo cambia la simbología de la capa.
- Para volver a la simbología estándar, elimina la capa `ThematicPipes` del panel de capas o recarga la simbología predeterminada desde las propiedades de capa de QGIS.
- Si el proyecto no tiene resultados de simulación, los campos de resultado no aparecen en el desplegable.
