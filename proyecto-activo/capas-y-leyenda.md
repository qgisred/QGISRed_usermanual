# Gestor de Capas y Leyenda

---

## Gestor de capas

**Barra Project → Gestor de capas** (Layer manager)

Controla qué capas del proyecto están activas en QGIS y permite recuperar capas que se hayan eliminado accidentalmente.

<figure><img src="../assets/images/proyecto/gestor-capas.png" alt="Diálogo del Gestor de capas de QGISRed"><figcaption><p>Diálogo del Gestor de capas de QGISRed</p></figcaption></figure>
*Gestor de capas: lista de todas las capas del proyecto con su estado de carga.*

### Capas base (Inputs)

Muestra los 6 elementos base de EPANET más las capas opcionales (Multiple Demands, Sources, Service Connections, Isolation Valves, Meters). Para cada una indica si está cargada en QGIS o no.

- **Casilla marcada** → la capa está cargada y visible en la leyenda de QGIS.
- **Casilla desmarcada** → la capa existe en disco pero no está cargada.

Puedes marcar o desmarcar cualquier capa para cargarla o descargarla sin afectar los datos.

### Recuperar una capa borrada

Si has borrado accidentalmente una capa de la leyenda de QGIS (o su archivo SHP en disco), el Gestor de capas permite **recrearla vacía**:

1. Selecciona la capa que falta (aparecerá con un icono de advertencia).
2. Pulsa **Recuperar** (o el botón equivalente según la versión).
3. QGISRed crea el SHP vacío con la estructura de campos correcta y lo carga en QGIS.

> ⚠️ La recuperación crea la capa vacía. Los datos que estuvieran en ella (si el SHP fue borrado del disco) no se pueden recuperar a menos que tengas una copia de seguridad.

### Resumen del modelo (Summary)

**Barra Project → Resumen**

Genera un informe rápido con el número de elementos de cada tipo presentes en el proyecto:

```
Junctions: 1 243
Pipes: 1 876
Tanks: 3
Reservoirs: 2
Valves: 47
Pumps: 8
```

Útil para verificar que la importación fue completa o para documentar el tamaño del modelo.

---

## Editor de leyenda

**Barra Project → Editor de leyenda** (Legend editor)

Abre un panel flotante que permite personalizar la **simbología** de las capas del proyecto sin necesidad de navegar por el menú de propiedades de capa de QGIS.

<figure><img src="../assets/images/proyecto/editor-leyenda.png" alt="Panel del Editor de leyenda de QGISRed"><figcaption><p>Panel del Editor de leyenda de QGISRed</p></figcaption></figure>
*Panel del Editor de leyenda: estilos predefinidos y personalización de colores y tamaños.*

### Estilos predefinidos

QGISRed incluye estilos QML predefinidos para cada tipo de elemento, adaptados al sistema de unidades del proyecto (SI/US). El editor permite aplicar estos estilos con un solo clic:

- Estilo por **material** (codificación de colores por material de tubería)
- Estilo por **diámetro** (escala de colores proporcional al diámetro)
- Estilo por **longitud**
- Estilo **base** (colores estándar de QGISRed)

### Personalización manual

Para cada capa puedes ajustar:
- Color de relleno y borde para elementos puntuales
- Color y grosor de línea para tuberías
- Tamaño de los símbolos

Los cambios se guardan en el archivo `.qgz` del proyecto QGIS. Si no tienes el `.qgz` guardado, los estilos personalizados se perderán al cerrar QGIS.

> 💡 Si cambias la versión del plugin y los estilos se reinician al abrir el proyecto, es normal: QGISRed detecta el cambio de versión y aplica los estilos por defecto actualizados. Puedes volver a personalizar desde el Editor de leyenda.
