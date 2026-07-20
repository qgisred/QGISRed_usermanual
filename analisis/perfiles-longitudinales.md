# Perfiles Longitudinales

**Barra Analysis → Longitudinal profile…**

El perfil longitudinal muestra la evolución de una variable hidráulica a lo largo de un recorrido definido interactivamente sobre la red. El eje X representa la distancia acumulada desde el nodo inicial del recorrido; el eje Y, el valor de la variable seleccionada en cada nodo del camino. Es posible tener varios paneles de perfil abiertos simultáneamente, cada uno con su propio recorrido, variables y configuración independientes.

> **Requisito previo**: debe haberse ejecutado una simulación EPANET antes de abrir el perfil. Si no hay resultados disponibles, el plugin muestra el mensaje _"Run a simulation first to build a longitudinal profile."_

> 📝 El plugin detecta automáticamente si los resultados provienen del formato estándar de EPANET o del formato extendido `.hyd` de QGISRed; no es necesario ningún ajuste manual.

<figure><img src="../assets/images/analisis/perfil-longitudinal-dock.png" alt="Dock de perfil longitudinal con recorrido dibujado en el mapa y gráfico de presión"><figcaption><p>Dock de perfil longitudinal con recorrido dibujado en el mapa y gráfico de presión</p></figcaption></figure>
*Perfil longitudinal: recorrido resaltado en rojo en el mapa (izquierda) y gráfico de altura piezométrica + cota del terreno (derecha).*

---

## Múltiples ventanas de perfil

El plugin permite mantener varios docks de perfil abiertos al mismo tiempo. Cada dock funciona de manera completamente independiente: tiene su propio recorrido, sus propias variables seleccionadas y su propia configuración del gráfico.

- El botón **Nuevo panel** de la barra de herramientas crea un dock adicional numerado secuencialmente (_Profile 2_, _Profile 3_, etc.).
- El panel activo —el que recibe las interacciones del mapa— se distingue visualmente de los demás.
- Abrir el perfil desde el menú Analysis reutiliza el primer panel si ya existe alguno abierto; en caso contrario crea uno nuevo.

---

## Abrir y construir el perfil

1. Activa **Longitudinal profile** desde la barra Analysis. El dock de perfil se abre en la zona inferior de QGIS.
2. El modo **Pick** se activa automáticamente; el cursor cambia al icono de perfil.
3. Haz clic sobre un nudo de la red (Junctions, Tanks, Reservoirs) para fijar el primer nodo de referencia.
4. Haz clic sobre otro nudo: el plugin calcula el **camino mínimo topológico** entre ambos nudos y dibuja el perfil.
5. Cada clic adicional extiende el recorrido concatenando el camino desde el último nodo hasta el nuevo.

Si dos nudos no están conectados en la red, aparece el aviso _"Selected node is not connected to the previous one along the network."_

En el mapa se dibuja una **línea roja** sobre los enlaces del recorrido y **marcadores azules** cuadrados sobre los nodos de referencia.

---

## Variables disponibles

| Variable | Descripción |
|----------|-------------|
| **Elevation** | Cota del terreno — estático, no depende del instante de tiempo |
| **Cabeza + Cota** | Altura piezométrica y cota del terreno juntas en el mismo gráfico |
| **Pressure** | Presión en cada nodo |
| **Quality** | Calidad del agua en cada nodo; el selector muestra el nombre de calidad específico del proyecto (por ejemplo, _Cloro_) en lugar del término genérico _Calidad_ |
| **Accumulated head loss** | Pérdida de carga acumulada a lo largo del recorrido |

La variable por defecto es **Cabeza + Cota**. Cuando se selecciona, el gráfico muestra **simultáneamente** la línea piezométrica (azul) y la cota del terreno (marrón), lo que permite ver de un vistazo si existe presión positiva en cada punto del recorrido.

El gráfico se actualiza automáticamente al cambiar el instante de tiempo en el Results dock.

> 📝 Cuando hay instantes de tiempo disponibles, el título del gráfico muestra **"Perfiles longitudinales a las HH:MM:SS"**. Para resultados estáticos aparece simplemente **"Perfiles longitudinales"**.

> 📝 Las etiquetas de los ejes incluyen la unidad del proyecto entre corchetes (por ejemplo, _Cabeza [m]_, _Presión [bar]_, _Distancia [m]_). Las cabeceras de la tabla de valores también muestran las unidades.

### Eje secundario

A la derecha del selector de variable principal se encuentra el combo **2nd axis**. Permite superponer una segunda variable sobre el **eje Y derecho** del gráfico, con su propia escala independiente.

- Las variables disponibles en el eje secundario dependen de la selección principal.
- La curva del eje secundario se puede eliminar directamente desde la leyenda del gráfico.
- El eje Y derecho tiene su propia configuración de escala y etiqueta, accesible en **Chart options → Axes** (véase [Personalización del gráfico](#personalización-del-gráfico)).

---

## Barra de herramientas del dock

### Modos de edición del recorrido

| Botón | Modo | Función |
|-------|------|---------|
| Pick | **Pick** | Activa el mapa para añadir nodos de referencia al final del recorrido con cada clic |
| Add node | **Add node** | Convierte en nodo de referencia un nodo intermedio ya existente en el camino; también aplica a recorridos de ramas |
| Remove node | **Remove node** | Elimina un nodo de referencia del recorrido (los nodos extremos no se pueden eliminar); también aplica a ramas |
| Move node | **Move node** | Reubica un nodo de referencia: primer clic en la posición actual, segundo clic en la nueva posición; también aplica a ramas y verifica conflictos con recorridos existentes |
| Branch | **Branch** | Añade una rama lateral (ver sección [Ramas](#ramas)) |

### Navegación del gráfico

| Botón | Función |
|-------|---------|
| **Zoom window** | Dibuja un rectángulo sobre el gráfico para hacer zoom en el eje X |
| **Pan** | Arrastra horizontalmente el gráfico; exclusivo con Zoom window |
| **Zoom in / Zoom out** | Amplía o reduce la vista en el eje X |
| **Fit** | Restaura la vista completa del perfil |

La rueda del ratón también hace zoom centrando en la posición del cursor.

### Opciones de visualización

| Botón | Función |
|-------|---------|
| **Labels** | Muestra el valor numérico de la variable sobre cada nodo de referencia |
| **Symbols** | Muestra simbología de elemento (nudo, depósito, embalse, bomba, válvula) y flechas de dirección de flujo sobre la curva |
| **Envelope** | Abre un submenú para activar la envolvente Min/Max de la simulación (ver sección [Envolvente](#envolvente-minmax)) |
| **Chart options** | Abre el diálogo de personalización del gráfico |

### Tabla y exportación

| Botón | Función |
|-------|---------|
| **Table** | Muestra u oculta la tabla de valores a la izquierda del gráfico |
| **Export CSV** | Exporta la tabla de valores a CSV con separadores regionales |
| **Export image** | Guarda el gráfico como PNG o SVG |
| **Exportar configuración** | Guarda la configuración actual del perfil en un archivo `.cfg` (ver sección [Importar y exportar configuración](#importar-y-exportar-configuración)) |
| **Importar configuración** | Carga una configuración de perfil previamente guardada desde un archivo `.cfg` |
| **Nuevo panel** | Crea un dock de perfil adicional numerado secuencialmente |
| **Clear** | Borra el recorrido completo, las ramas y el resaltado del mapa |

---

## Envolvente Min/Max

Disponible para **Cabeza + Cota**, **Pressure** y **Quality**. Muestra el rango histórico de variación de toda la simulación superpuesto sobre el perfil del instante actual.

| Modo | Descripción |
|------|-------------|
| **Off** | Sin envolvente |
| **Shaded band only** | Área sombreada en naranja entre los valores máximo y mínimo históricos |
| **Boundary lines only** | Dos líneas discontinuas naranjas que marcan el máximo y el mínimo |
| **Band and lines** | Ambos superpuestos |

Cuando la envolvente está activa, la tabla de valores añade columnas con el valor máximo, el instante de máximo, el valor mínimo y el instante de mínimo de cada nodo.

---

## Ramas

El modo **Branch** permite añadir derivaciones laterales que comparten el mismo gráfico con el recorrido principal.

1. Activa el modo Branch.
2. Haz clic sobre un nudo ya perteneciente al recorrido principal o a una rama existente: ese nudo define el punto de bifurcación y su posición en el eje X.
3. Haz clics sucesivos para extender la rama hacia otros nudos.

Cada rama se dibuja con un color diferente de la paleta. Las distancias de la rama se calculan a partir del punto de bifurcación, de modo que ambas curvas comparten el mismo origen X en ese punto. Cuando la variable seleccionada es **Cabeza + Cota**, las ramas también muestran su propia curva de cota del terreno junto a la línea piezométrica.

> ⚠️ **Restricciones de integridad del recorrido**
>
> - Una rama no puede reutilizar enlaces ni nodos que ya pertenezcan al recorrido principal o a otra rama, salvo el nodo de bifurcación de origen. Si se intenta, la operación es rechazada con un mensaje de error.
> - El nodo de origen de una rama no puede eliminarse del recorrido principal mientras la rama esté activa. Para eliminarlo es necesario recortar primero la rama desde su extremo más alejado.
> - El modo **Move node** comprueba también conflictos con los recorridos existentes antes de aplicar el cambio.
> - Cualquier operación de edición (Add, Remove, Move) se deshace silenciosamente si el recorrido recalculado resultante no es válido.

Los modos **Add node**, **Remove node** y **Move node** funcionan tanto sobre el recorrido principal como sobre los recorridos de las ramas.

Las ramas pueden eliminarse directamente desde la **leyenda del gráfico**, sin necesidad de usar el botón Clear.

El botón **Clear** elimina el recorrido principal y todas las ramas.

---

## Tooltip interactivo

Al mover el ratón sobre el gráfico, una línea vertical discontinua indica la posición del cursor. Sobre cada serie activa aparece un círculo de resaltado en el nodo más cercano y un cuadro de información con:

- ID del elemento
- Distancia acumulada desde el nodo inicial
- Valor de la variable para cada serie activa

En el gráfico se dibujan **líneas verticales de referencia** en la posición X de cada nodo del recorrido: líneas finas en azul claro para todos los nodos e líneas más gruesas para los nodos de referencia.

### Sincronización bidireccional con el mapa

La interacción entre el gráfico y el mapa es bidireccional y se actualiza en tiempo real:

- Al desplazar el ratón sobre el **gráfico**, el nodo más cercano queda resaltado en el **lienzo del mapa** con un círculo naranja.
- Al desplazar el ratón sobre el **mapa** mientras el modo Pick del perfil está activo, el cursor del gráfico se desplaza al nodo correspondiente.

---

## Importar y exportar configuración

Dos botones de la barra de herramientas permiten guardar y recuperar la configuración completa de un panel de perfil.

**Ruta por defecto**: la misma carpeta que los resultados de la simulación, con el nombre `{salida}_Profile_Config.cfg`.

La configuración almacenada incluye:

- Variable principal y variable del eje secundario (si existe)
- Nodos de referencia del recorrido principal
- Todas las ramas definidas
- Opciones de visualización: símbolos, etiquetas, envolvente
- Configuración de ejes (escala, etiquetas, cuadrícula)
- Estilos de curva (color, grosor, tipo de línea, marcadores)
- Texto de descripción libre asociado al panel

> 💡 El dock incluye un campo de texto libre (descripción o comentario) que se guarda junto con la configuración y puede usarse para identificar el análisis o anotar observaciones.

Al **importar** una configuración, el perfil se recalcula a partir de los nodos almacenados. Si algún nodo ya no existe en la red, el plugin muestra una advertencia y continúa con los nodos disponibles.

---

## Personalización del gráfico

El diálogo **Chart options** (botón de ajuste en la barra) tiene cuatro pestañas. El botón **Apply** previsualiza los cambios en tiempo real sin cerrar el diálogo.

**Pestaña Axes**
Para cada eje (X = distancia, Y = variable):
- Título personalizado.
- Escala automática (activada por defecto) o rango fijo manual.
- Mostrar u ocultar cuadrícula.

Cuando hay una variable activa en el **eje secundario**, aparece un grupo adicional **Eje Y (derecho)** con su propia configuración de escala y etiqueta, independiente del eje Y principal.

**Pestaña Curves**
Por cada serie activa:
- Color, estilo de línea (Solid / Dashed / Dotted) y grosor.
- Marcadores: mostrar/ocultar y tamaño.

**Pestaña Legend**
- Mostrar/ocultar leyenda.
- Posición (Left / Center / Right), tamaño de fuente y tamaño del símbolo.
- Mostrar marco y color de fondo de la leyenda.

**Pestaña General**
- Color de fondo del área del gráfico.
