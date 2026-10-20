# ✏️ Edición

La barra **Edición** contiene todas las herramientas para construir y editar la red directamente sobre el mapa de QGIS. Trabaja sobre las capas del proyecto activo sin necesidad de abrir tablas de atributos ni archivos externos.

<figure><img src="../assets/images/editing/toolbar.png" alt="Barra de herramientas Edition de QGISRed"><figcaption><p>Barra de herramientas Edition de QGISRed</p></figcaption></figure>
*Barra Edition: creación de elementos, edición geométrica y topológica, propiedades y datos de operación.*

> Todos los botones requieren un proyecto válido cargado. Si no hay ninguno, el plugin muestra _"No hay ningún proyecto válido abierto"_.

---

## Herramientas de la barra Edition

### Grupo 1 — Creación de elementos

| # | Herramienta | Función |
|---|-------------|---------|
| 1 | **Añadir tubería** | Dibuja tuberías haciendo clic en el mapa; crea nudos automáticamente en los extremos |
| 2 | **Añadir depósito** | Coloca un depósito (Tank) en un nudo existente |
| 3 | **Añadir embalse** | Coloca un embalse o punto de alimentación (Reservoir) en un nudo existente |
| 4 | **Insertar válvula en tubería** | Inserta una válvula dentro de una tubería existente, dividiéndola |
| 5 | **Insertar bomba en tubería** | Inserta una bomba dentro de una tubería existente, dividiéndola |

### Grupo 2 — Edición geométrica y topológica

| # | Herramienta | Función |
|---|-------------|---------|
| 6 | **Seleccionar múltiples elementos** | Selección multi-capa por área rectangular en el mapa |
| 7 | **Mover nudos** | Desplaza nudos arrastrando todos los elementos conectados |
| 8 | **Editar vértices de líneas** | Añade, mueve y elimina vértices intermedios de tuberías |
| 9 | **Invertir elementos** | Invierte el sentido de orientación de tuberías o conexiones de servicio |
| 10 | **Dividir/Unir tuberías** | Parte una tubería en el punto indicado o une dos tramos adyacentes |
| 11 | **Fusionar/Disolver uniones** | Fusiona dos nudos en uno o separa un nudo en varios |
| 12 | **Crear/Eliminar conexiones en T** | Crea o elimina una unión en T entre un nudo y una tubería cercana |
| 13 | **Crear/Eliminar cruces** | Crea o elimina un cruce (nudo compartido) entre tuberías que se intersectan |
| 14 | **Mover válvulas/bombas** | Mueve una válvula o bomba de una tubería a otra |
| 15 | **Cambiar estado de elementos** | Alterna el estado Open/Closed de tuberías y válvulas |
| 16 | **Eliminar elementos** | Elimina el elemento señalado o los elementos seleccionados |

### Grupo 3 — Propiedades y datos de operación

| # | Herramienta | Función |
|---|-------------|---------|
| 17 | **Edit element properties…** | Abre el diálogo de propiedades del elemento pulsado |
| 18 | **Edit patterns and curves…** | Editor de patrones de demanda y curvas de bombas/depósitos |
| 19 | **Edit controls…** | Editor de controles simples y reglas de operación |

---

## En esta sección

* [Creación de elementos](creacion.md) — tuberías, depósitos, embalses, válvulas, bombas
* [Manipulación geométrica y topológica](manipulacion.md) — mover, dividir, invertir, cruzar, borrar
* [Propiedades de elementos](propiedades.md) — diálogo de edición con navegador integrado
* [Patrones y curvas](curvas.md) — patrones de demanda, curvas H-Q, eficiencia y volumen
* [Controles y reglas](controles.md) — controles simples y reglas de operación automática
