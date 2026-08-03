# Acometidas y Válvulas de Corte

Las acometidas y las válvulas de corte son los dos elementos que conectan el modelo hidráulico con la realidad operacional de la red: las acometidas representan la conexión individual con cada cliente y las válvulas de corte permiten modelar el aislamiento de sectores sin necesidad de modificar la topología del modelo EPANET.

***

## Add service connection

**Barra Digital Twin → Add service connection**

Dibuja una acometida como polilínea desde la tubería principal hasta el punto de entrega del cliente. La acometida queda almacenada en la capa complementaria `ServiceConnections` del proyecto.

\*Dibujo de acometida: la línea parte de la tubería principal y llega al límite de parcela del cliente.\*

### Proceso

1. Activa **Add service connection**. El cursor cambia a modo de dibujo de línea.
2. Haz clic sobre la tubería principal en el punto de toma.
3. Haz clic en los puntos intermedios de la traza si la acometida no es recta.
4. Doble clic en el punto final (límite de parcela o contador) para completar el trazado.
5. QGISRed llama al motor C# (`GISRed.AddConnection`) y actualiza la capa `ServiceConnections`.

La acometida hereda automáticamente el nudo de conexión más cercano de la red principal. El campo `IsActive` de cada acometida permite activar o desactivar el suministro individualmente sin eliminar el elemento.

***

## Add isolation valve

**Barra Digital Twin → Add isolation valve**

Añade una válvula de corte manual sobre una tubería existente haciendo clic sobre ella. Las válvulas de corte se almacenan en la capa complementaria `IsolationValves` y no son elementos EPANET: no aparecen en la simulación pero sí en el análisis de segmentos aislados (**Isolated segments**, barra Tools).

### Proceso

1. Activa **Add isolation valve**.
2. Haz clic sobre la tubería en el punto donde quieres colocar la válvula.
3. QGISRed la inserta en la capa `IsolationValves` y la representa sobre el mapa.

### Relación con la simulación

Las válvulas de corte por sí solas no modifican el modelo EPANET. Para que su estado (abierta/cerrada) afecte a la simulación, usa la herramienta **Set pipe's initial status from isolation valves** del Grupo 2.

***

## Convert service connections into pipes/nodes

**Barra Digital Twin → Convert service connections into pipes/nodes**

Incorpora las acometidas dibujadas en `ServiceConnections` al modelo EPANET activo. Requiere que la capa `ServiceConnections` exista y contenga al menos una acometida.

### Opciones de conversión

Al ejecutar la herramienta aparece un diálogo con dos opciones:

| Opción       | Resultado en el modelo                                                                                                                                                          |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **As nodes** | Cada acometida se convierte en un nudo de demanda puntual en el punto de conexión con la tubería principal. La geometría de la acometida no entra en el modelo.                 |
| **As pipes** | Cada acometida se convierte en una tubería de pequeño diámetro que va desde el nudo de toma hasta un nuevo nudo final. Permite simular las pérdidas en la conexión del cliente. |

### Cuándo usar cada opción

* **As nodes**: cuando solo interesa incorporar la demanda del cliente al modelo sin simular las pérdidas internas de la acometida. Es la opción habitual para redes de distribución a escala de barrio o ciudad.
* **As pipes**: cuando se quiere simular redes de abonado con diámetros reales de acometida, o cuando la longitud de la acometida es significativa respecto a la red principal.

> Esta operación modifica el modelo EPANET (capa `Junctions` y/o `Pipes`). Guarda el proyecto antes de ejecutarla si quieres conservar el estado anterior.
