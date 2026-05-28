# Manipulación Geométrica y Topológica

Las herramientas del segundo grupo de la barra Edition permiten modificar la geometría y la topología de la red sin romper la conectividad. QGISRed mantiene la coherencia entre la geometría espacial y los datos del modelo en todo momento.

---

## Selección múltiple (Select multiple elements)

**Barra Edition → Select multiple elements**

Herramienta de selección simultánea sobre varias capas. Actívala y dibuja un rectángulo en el mapa: todos los elementos de todas las capas del proyecto que queden dentro del área quedan seleccionados.

La selección se usa como **entrada** para otras herramientas: Reverse elements y Delete elements operan sobre los elementos seleccionados si los hay, o piden que hagas clic en el mapa si no hay selección previa.

> Para deseleccionar, vuelve a pulsar el botón o usa `Ctrl+Shift+A` (deselección global de QGIS).

---

## Mover nudos (Move nodes)

**Barra Edition → Move nodes**

Desplaza uno o varios nudos (Junctions, Tanks, Reservoirs) arrastrando consigo **todos los elementos lineales conectados** (tuberías, válvulas, bombas). La red permanece conectada tras el movimiento.

![Mover un nudo y sus tuberías conectadas en el mapa](../assets/images/edicion/move-nodes.png)
*Al arrastrar un nudo, todas las tuberías conectadas siguen el desplazamiento.*

### Cómo usarla

1. Activa la herramienta.
2. Haz clic sobre el nudo que quieres mover (o sobre la zona de un nudo en la capa Junctions).
3. Arrastra hasta la nueva posición.
4. Suelta el botón del ratón para confirmar.

> Esta herramienta **no** mueve vértices intermedios de tuberías. Para eso, usa **Edit link vertices**.

---

## Editar vértices de enlace (Edit link vertices)

**Barra Edition → Edit link vertices**

Permite ajustar el trazado visual de tuberías y otros elementos lineales manipulando sus vértices intermedios. No afecta a los nudos extremos ni a la topología.

### Operaciones disponibles

| Acción | Gesto |
|--------|-------|
| **Mover vértice** | Haz clic sobre un vértice existente (círculo azul) y arrástralo |
| **Añadir vértice** | Haz clic en el segmento entre dos vértices para insertar uno nuevo |
| **Eliminar vértice** | Haz clic derecho sobre un vértice para eliminarlo |

---

## Invertir elementos (Reverse elements)

**Barra Edition → Reverse elements**

Invierte la **orientación** de tuberías y conexiones de servicio. La orientación determina el sentido positivo del flujo en los resultados de simulación.

### Dos formas de usarla

1. **Sobre selección**: Selecciona una o varias tuberías con la herramienta de selección múltiple y pulsa Reverse. Todas invierten su orientación.
2. **Por clic**: Sin selección previa, pulsa Reverse y haz clic sobre la tubería que quieres invertir.

> La inversión solo afecta a la convención de signo del caudal en los resultados. No modifica el comportamiento hidráulico en la simulación (EPANET calcula siempre el sentido real del flujo, independientemente de la orientación almacenada).

---

## Dividir/Unir tuberías (Split/Join pipes)

**Barra Edition → Split/Join pipes**

Haz clic sobre una tubería para **dividirla** en el punto indicado: QGISRed crea un nuevo nudo (Junction) en ese punto y dos tramos con los mismos atributos de diámetro, material e InstallYear que el original.

Para **unir** dos tuberías, haz clic sobre el nudo intermedio que comparten: si ese nudo tiene exactamente dos tuberías conectadas y las propiedades de diámetro, material e InstallYear son iguales, QGISRed los funde en un solo tramo y elimina el nudo.

![Dividir una tubería: se crea un nudo intermedio y dos tramos](../assets/images/edicion/split-pipe.png)
*Clic sobre P-5 crea el nudo J-42 y divide la tubería en P-5 y P-45.*

> Si las dos tuberías tienen diámetros o materiales distintos, la unión no se realiza y el plugin muestra un aviso.

---

## Fusionar/Separar nudos (Merge/Dissolve junctions)

**Barra Edition → Merge/Dissolve junctions**

Esta herramienta opera con **dos clics**:

- **Un solo clic** (clic y sin segundo punto): **Separa** el nudo indicado en tantos nudos independientes como tuberías tiene conectadas. Útil cuando un nudo agrupa varias tuberías que no deberían estar conectadas topológicamente.
- **Dos clics** (origen → destino): **Fusiona** el nudo origen con el nudo destino. Todas las tuberías conectadas al nudo origen se reconectan al nudo destino. El nudo origen desaparece.

Casos de uso habituales:
- Fusionar dos nudos muy próximos que quedaron separados al importar desde `.inp`.
- Separar un nudo en un cruce donde las tuberías realmente no están conectadas.

---

## Crear/Eliminar conexiones en T (Create/Remove T connections)

**Barra Edition → Create/Remove T connections**

Gestiona las uniones en T: puntos donde un nudo está muy próximo a una tubería pero **no** conectado a ella.

### Crear una T

1. Haz clic sobre el nudo que quieres conectar.
2. Haz clic sobre la tubería a la que debe conectarse.
3. QGISRed divide la tubería en el punto más cercano al nudo y conecta ambos con una tubería corta, o mueve el nudo hasta la tubería si la distancia es menor que la tolerancia.

### Eliminar una T

Haz clic sobre la conexión en T existente. QGISRed elimina el nudo intermedio y restaura la tubería original.

---

## Crear/Eliminar cruces (Create/Remove crossings)

**Barra Edition → Create/Remove crossings**

Gestiona los cruces entre tuberías que se intersectan en el mapa:

- **Crear cruce**: Haz clic en el punto de intersección entre dos tuberías que no tienen nudo compartido. QGISRed divide ambas tuberías y crea un nudo común en la intersección.
- **Eliminar cruce**: Haz clic sobre un nudo de cruce que tiene exactamente cuatro tuberías conectadas. QGISRed elimina el nudo y restituye las dos tuberías originales que pasan por encima.

> Esta herramienta no aplica snapping para evitar falsos positivos. La tolerancia de detección de cruce usa el valor configurado en **Valores por defecto**.

---

## Mover válvulas y bombas (Move valves/pumps)

**Barra Edition → Move valves/pumps**

Mueve una válvula o bomba de una tubería a otra manteniendo todas sus propiedades (tipo, ajuste, curva…).

### Proceso

1. Activa la herramienta. El cursor pide el primer clic.
2. Haz clic sobre la **tubería origen** (la que contiene la válvula/bomba actual).
3. Haz clic sobre la **tubería destino** (donde se insertará el elemento).
4. QGISRed elimina el elemento de la posición original, restaura la tubería original y lo inserta en la nueva posición.

---

## Cambiar estado de elemento (Change element status)

**Barra Edition → Change element status**

Alterna el estado operativo (Open/Closed) de tuberías y válvulas manuales sin abrir el diálogo de propiedades.

- **Clic simple**: Alterna entre Open y Closed.
- **Ctrl + Clic**: Ciclo por todos los estados disponibles: Open → Closed → CV (Check Valve) → Open.

La capa de **Isolation Valves** (válvulas de corte del gemelo digital) también puede gestionarse con esta herramienta si está cargada.

> El estado se almacena en el campo `InitStatus` de la capa correspondiente y se exporta al `.inp` de EPANET.

---

## Eliminar elementos (Delete elements)

**Barra Edition → Delete elements**

Elimina uno o varios elementos del proyecto. Funciona de dos modos:

1. **Sobre selección**: Selecciona elementos con la herramienta de selección múltiple y pulsa Delete. Se eliminan todos los elementos seleccionados.
2. **Por clic**: Sin selección, activa la herramienta y haz clic sobre el elemento a eliminar.

### Comportamiento al eliminar

| Situación | Qué ocurre |
|-----------|------------|
| Eliminar una tubería | Se elimina la tubería. Los nudos extremos permanecen si tienen otras conexiones; se eliminan si quedan aislados. |
| Eliminar un nudo con tuberías conectadas | Se eliminan también todas las tuberías conectadas. |
| Eliminar una válvula o bomba | Los dos tramos de tubería en que fue dividida se fusionan automáticamente en uno solo. |
| Eliminar un Tank o Reservoir | Se convierte el elemento en Junction o se elimina si no tiene conexiones. |

> La eliminación no se puede deshacer con `Ctrl+Z`. QGISRed guarda automáticamente el estado anterior del proyecto en la carpeta temporal antes de ejecutar la operación, pero la única forma de recuperar datos eliminados es usar una **copia de seguridad** previa.
