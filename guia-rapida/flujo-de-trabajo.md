# Flujo de Trabajo Típico

Este es el recorrido habitual para construir, verificar y simular una red de distribución con QGISRed.

---

## Paso 1 — Crear o abrir el proyecto

Usa la barra **General** para empezar:

- **Proyecto nuevo desde cero**: _Crear proyecto_ → elige nombre, carpeta y sistema de referencia. QGISRed genera automáticamente los 6 SHP base (Junctions, Pipes, Tanks, Reservoirs, Valves, Pumps).
- **Proyecto existente**: _Gestor de proyectos_ → doble clic sobre el proyecto en la lista de recientes.
- **Desde un archivo EPANET**: _Importar proyecto_ → selecciona el `.inp`. QGISRed lo convierte a SHP y lo abre.

## Paso 2 — Configurar las opciones del proyecto

Desde la barra **Project**, accede a _Opciones del proyecto_ para definir:
- **Unidades de caudal** (LPS, GPM, CMH…)
- **Fórmula de pérdida de carga** (D-W, H-W, C-M)
- **Modelo de calidad** (Ninguno, Cloro, Edad, Trazador)

El indicador en la barra principal (`LPS | D-W`) siempre refleja los valores activos.

## Paso 3 — Construir la red

Activa la barra **Edition** y dibuja la red sobre el mapa:

1. Comienza con las **tuberías** — los nudos extremos se crean solos.
2. Añade **depósitos y embalses** pulsando sobre nudos existentes.
3. Inserta **válvulas y bombas** haciendo clic sobre una tubería.
4. Edita las **propiedades** de cada elemento (diámetro, rugosidad, cota, demanda…).

> 💡 Puedes importar geometría existente (SHP de infraestructura, ortofoto de fondo) y trazar la red encima.

## Paso 4 — Verificar la calidad del modelo

Antes de simular, usa la barra **Debug**:

1. **Consolidar y revisar datos** — detecta atributos incompletos o incoherentes.
2. **Verificar conectividad** — identifica zonas aisladas sin fuente de presión.
3. **Sectores hidráulicos** — comprueba la alimentación de cada sector.

Corrige los problemas que señale el informe de incidencias antes de continuar.

## Paso 5 — Preparar los datos de demanda

Desde la barra **Tools**:

- **Interpolar cotas** si los nudos no tienen cota asignada.
- **Asignar rugosidades** a partir de material y fecha de instalación.
- **Gestor de demandas** para distribuir los consumos.

## Paso 6 — Simular

Desde la barra **Analysis**:

1. _Opciones de análisis_ — revisa la duración y el paso de tiempo.
2. _Ejecutar modelo_ — la simulación puede tardar desde un segundo hasta varios minutos según el tamaño de la red.
3. Al terminar, QGISRed carga automáticamente las capas de resultado y abre el **Visor de Resultados**.

## Paso 7 — Explorar resultados

En el panel lateral del Visor de Resultados:

- Selecciona qué **variable** mostrar en nudos (Presión, Demanda, Calidad) y en tuberías (Caudal, Velocidad, Pérdida Unitaria…).
- Mueve el **deslizador de tiempo** para ver la evolución a lo largo del periodo simulado.
- Activa **Avisos de mapa** para leer valores al pasar el ratón sobre cualquier elemento.
- Usa **Series temporales** para graficar la evolución de un punto concreto.

## Paso 8 — Guardar

- _Guardar mapa_ guarda el proyecto QGIS (`.qgz`) con las capas visibles y los estilos.
- _Exportar proyecto_ (desde el Gestor de proyectos) genera un ZIP portable del proyecto.

---

> ❗ **IMPORTANTE**: QGISRed no modifica las capas mientras estén en **Modo Edición** de QGIS. Asegúrate de confirmar (`Ctrl+S` en la capa) o descartar los cambios antes de usar cualquier herramienta del plugin.
