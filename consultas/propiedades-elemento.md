# Propiedades del Elemento

**Barra Queries → Element properties…**

Activa una herramienta de identificación interactiva: al hacer clic sobre cualquier elemento del mapa, el panel **Element Explorer** muestra en su pestaña *Properties* todos los atributos de ese elemento.

![Panel Element Explorer con la pestaña Properties mostrando atributos de una tubería](../assets/images/consultas/element-explorer-properties.png)
*Panel Element Explorer, pestaña Properties: atributos completos de la tubería seleccionada con clic.*

---

## Cómo funciona

1. Activa **Element properties** en la barra Queries. El cursor cambia a una herramienta de identificación.
2. Haz clic sobre cualquier elemento de la red en el mapa (tubería, nudo, válvula, bomba, depósito, embalse…).
3. El panel Element Explorer se abre automáticamente (o se trae al frente) y muestra en la pestaña *Properties* todos los campos del elemento pulsado.
4. Puedes seguir haciendo clic en otros elementos para actualizar el panel sin desactivar la herramienta.

---

## Información mostrada

El panel organiza los atributos por secciones según el tipo de elemento. Para una **tubería** típica se muestran:

| Campo | Descripción |
|-------|-------------|
| `Id` | Identificador único |
| `Length` | Longitud (m) |
| `Diameter` | Diámetro (mm) |
| `Roughness` | Coeficiente de rugosidad |
| `Material` | Material de la tubería |
| `InstallYear` | Año de instalación |
| `Status` | Estado (Open / Closed / CV) |
| `Tag` | Etiqueta libre |

Para **nudos** (`Junctions`) se muestran campos como `Elevation`, `Demand`, `Pattern`, `InitQuality`, etc. Cada tipo de elemento tiene su propio conjunto de campos.

Si el proyecto tiene **resultados de simulación** cargados, el panel añade una sección adicional con los valores calculados (presión, caudal, velocidad…) para el período activo en el visor de resultados.

---

## Relación con Find Elements

El panel Element Explorer es compartido entre **Find elements by ID** y **Element properties**. Ambas herramientas usan el mismo panel pero activan pestañas distintas. Puedes cambiar entre pestañas en cualquier momento sin desactivar ninguna herramienta.

---

## Notas de uso

- El botón **Element properties** es de tipo *checkable*. Al desactivarlo, el cursor vuelve al modo de navegación estándar de QGIS.
- Si haces clic en una zona sin elementos, el panel no se actualiza y conserva la última selección.
- El fondo del panel de resultados tiene un tinte amarillo claro para diferenciarlo visualmente del resto de paneles de QGIS.
