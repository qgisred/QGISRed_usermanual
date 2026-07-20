# Perfiles Longitudinales

**Barra Analysis → Longitudinal profile…**

El perfil longitudinal muestra la evolución de una variable hidráulica a lo largo de un recorrido definido interactivamente sobre la red. El eje X representa la distancia acumulada desde el nodo inicial del recorrido; el eje Y, el valor de la variable seleccionada en cada nodo del camino.

> **Requisito previo**: debe haberse ejecutado una simulación EPANET antes de abrir el perfil. Si no hay resultados disponibles, el plugin muestra el mensaje _"Run a simulation first to build a longitudinal profile."_

<figure><img src="../assets/images/analisis/perfil-longitudinal-dock.png" alt="Dock de perfil longitudinal con recorrido dibujado en el mapa y gráfico de presión"><figcaption><p>Dock de perfil longitudinal con recorrido dibujado en el mapa y gráfico de presión</p></figcaption></figure>
*Perfil longitudinal: recorrido resaltado en rojo en el mapa (izquierda) y gráfico de altura piezométrica + cota del terreno (derecha).*

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
| **Head** | Altura piezométrica en cada nodo |
| **Pressure** | Presión en cada nodo |
| **Quality** | Calidad del agua en cada nodo |
| **Accumulated head loss** | Pérdida de carga acumulada a lo largo del recorrido |

La variable por defecto es **Head**. Cuando se selecciona Head, el gráfico muestra **simultáneamente** la línea piezométrica (azul) y la cota del terreno (marrón), lo que permite ver de un vistazo si existe presión positiva en cada punto del recorrido.

El gráfico se actualiza automáticamente al cambiar el instante de tiempo en el Results dock.

---

## Barra de herramientas del dock

### Modos de edición del recorrido

| Botón | Modo | Función |
|-------|------|---------|
| Pick | **Pick** | Activa el mapa para añadir nodos de referencia al final del recorrido con cada clic |
| Add node | **Add node** | Convierte en nodo de referencia un nodo intermedio ya existente en el camino |
| Remove node | **Remove node** | Elimina un nodo de referencia del recorrido (los nodos extremos no se pueden eliminar) |
| Move node | **Move node** | Reubica un nodo de referencia: primer clic en la posición actual, segundo clic en la nueva posición |
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
| **Clear** | Borra el recorrido completo, las ramas y el resaltado del mapa |

---

## Envolvente Min/Max

Disponible para **Head**, **Pressure** y **Quality**. Muestra el rango histórico de variación de toda la simulación superpuesto sobre el perfil del instante actual.

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

Cada rama se dibuja con un color diferente de la paleta. Las distancias de la rama se calculan a partir del punto de bifurcación, de modo que ambas curvas comparten el mismo origen X en ese punto. El botón **Clear** elimina el recorrido principal y todas las ramas.

---

## Tooltip interactivo

Al mover el ratón sobre el gráfico, una línea vertical discontinua indica la posición del cursor. Sobre cada serie activa aparece un círculo de resaltado en el nodo más cercano y un cuadro de información con:

- ID del elemento
- Distancia acumulada desde el nodo inicial
- Valor de la variable para cada serie activa

---

## Personalización del gráfico

El diálogo **Chart options** (botón de ajuste en la barra) tiene cuatro pestañas. El botón **Apply** previsualiza los cambios en tiempo real sin cerrar el diálogo.

**Pestaña Axes**
Para cada eje (X = distancia, Y = variable):
- Título personalizado.
- Escala automática (activada por defecto) o rango fijo manual.
- Mostrar u ocultar cuadrícula.

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
