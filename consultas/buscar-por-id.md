# Buscar Elemento por ID

**Barra Queries → Find elements by ID…**

Abre el panel **Element Explorer** en la pestaña de búsqueda por identificador. Permite localizar cualquier elemento de la red escribiendo su ID y resaltarlo en el mapa sin necesidad de desplazarse manualmente.

![Panel Element Explorer con la pestaña Find Elements activa](../assets/images/consultas/element-explorer-find.png)
*Panel Element Explorer: búsqueda de elementos por ID con resultados resaltados en el mapa.*

---

## El panel Element Explorer

Element Explorer es un panel flotante (dock) que QGISRed mantiene como instancia única. Una vez abierto permanece disponible mientras el proyecto esté activo. Contiene dos secciones principales accesibles desde sus pestañas:

- **Find Elements** — búsqueda por ID (esta página)
- **Element Properties** — propiedades del elemento seleccionado en el mapa (página siguiente)

---

## Búsqueda por ID

### Elementos que se pueden buscar

La búsqueda abarca todas las capas activas del proyecto:

- Pipes (tuberías)
- Junctions (nudos de demanda)
- Demands (demandas múltiples)
- Reservoirs (embalses)
- Tanks (depósitos)
- Pumps (bombas)
- Valves (válvulas)
- Sources (fuentes)

### Proceso

1. Activa **Find elements by ID** en la barra Queries. El panel Element Explorer se abre o se lleva al frente si ya estaba visible.
2. Selecciona el tipo de elemento en el desplegable de capa.
3. Escribe el ID del elemento en el campo de texto.
4. Pulsa **Find** o tecla Intro.
5. QGISRed centra el mapa en el elemento encontrado y lo resalta. El resultado aparece en la pestaña de resultados con fondo amarillo claro.

### Búsqueda múltiple

Puedes buscar varios IDs en la misma consulta separándolos por coma o punto y coma. Todos los elementos encontrados quedan resaltados simultáneamente en el mapa y listados en el panel de resultados.

### Si el ID no existe

Si el ID introducido no corresponde a ningún elemento de la capa seleccionada, el panel muestra un mensaje de advertencia. El mapa no cambia.

---

## Notas de uso

- El botón **Find elements by ID** es de tipo *checkable*: al activarlo abre el panel; al desactivarlo lo oculta.
- El panel Element Explorer es compartido con la herramienta **Element properties**. Cambiar de pestaña dentro del panel no cierra ninguna funcionalidad.
