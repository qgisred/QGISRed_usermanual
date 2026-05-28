# Topología y Conectividad

Las herramientas del primer grupo de la barra Debug detectan y corrigen los errores estructurales más frecuentes: elementos duplicados, vértices innecesarios, tuberías fragmentadas y zonas desconectadas. Es recomendable ejecutarlas en el orden en que aparecen en la barra antes de simular por primera vez.

---

## Check && commit data

**Barra Debug → Check && commit data**

Es la herramienta de validación principal. Recorre todos los elementos del proyecto, comprueba la coherencia de los datos (cotas, diámetros, IDs duplicados, referencias a curvas y patrones inexistentes, etc.) y **consolida los cambios pendientes**.

### Qué valida

- IDs duplicados en cualquier capa.
- Tuberías sin nudos extremos válidos (conectividad rota).
- Referencias a curvas o patrones que no existen en el proyecto.
- Valores obligatorios vacíos (diámetro nulo, cota vacía…).
- Coherencia interna del archivo `_Options.dbf`.

### Resultado

- Si todo es válido: mensaje _"Input data is valid"_ en verde.
- Si hay errores: lista de problemas con el ID y tipo de elemento afectado. Los elementos con error se seleccionan automáticamente en el mapa para facilitar su localización.

> Ejecuta **Check && commit data** siempre que hayas editado la tabla de atributos manualmente (fuera del diálogo de propiedades), ya que esos cambios no pasan por la validación automática del plugin.

---

## Remove overlapping elements

**Barra Debug → Remove overlapping elements**

Detecta elementos que comparten exactamente la misma posición geográfica: nudos sobre nudos, tuberías sobre tuberías o nudos sobre el extremo de otra capa.

### Cuándo aparecen duplicados

- Al importar desde un `.inp` con coordenadas redondeadas.
- Al combinar datos de distintas fuentes GIS.
- Al copiar-pegar elementos sin comprobar solapamiento.

### Funcionamiento

La herramienta opera sobre la selección actual o sobre toda la red si no hay selección. Elimina el elemento duplicado conservando el que tiene más conexiones o, en caso de empate, el de menor ID. Los atributos del elemento eliminado se descartan.

> Ejecuta esta herramienta **antes de Create T connections** y **antes de Check connectivity** para evitar falsos positivos de conectividad causados por nudos duplicados.

---

## Simplify link vertices

**Barra Debug → Simplify link vertices**

Elimina los vértices intermedios que están alineados (dentro de un umbral de tolerancia angular) con los segmentos adyacentes. Estos vértices no aportan información geométrica pero aumentan el tamaño del SHP y ralentizan el renderizado.

### Cuándo es útil

- Tras importar desde AutoCAD o SIG municipales donde las líneas tienen vértices cada pocos centímetros.
- Después de usar herramientas de suavizado externas que añaden puntos innecesarios.

### Qué conserva

Los vértices en puntos de quiebre real (cambio de dirección) no se eliminan. Solo se eliminan los que caen sobre la prolongación del segmento anterior, dentro del ángulo de tolerancia interna del plugin.

---

## Join consecutive pipes

**Barra Debug → Join consecutive pipes (= diameter, material and year)**

Fusiona tuberías adyacentes cuando comparten **los tres atributos**: diámetro, material y año de instalación. El nudo intermedio se elimina si no tiene demanda ni está conectado a otras capas.

### Resultado

Tuberías que antes estaban fragmentadas (por importación desde GIS, por divisiones anteriores o por diseño incremental) quedan fusionadas en un solo tramo. Esto:
- Reduce el número de elementos del modelo.
- Simplifica la tabla de atributos.
- Mejora el rendimiento de la simulación.

> Si el nudo intermedio tiene una demanda asignada distinta de cero, la tubería **no** se fusiona. QGISRed conserva el nudo para no perder datos de consumo.

---

## Create T connections

**Barra Debug → Create T connections**

Detecta automáticamente situaciones donde el extremo de una tubería (o un nudo de demanda) cae sobre el trazado de otra tubería, sin estar conectado a ella. En esos casos, el plugin divide la tubería y crea el nudo de unión.

### Problema que resuelve

Al digitalizar redes a mano, es frecuente que una derivación quede "flotando" sobre la tubería principal sin conectarse topológicamente. Visualmente parece correcto, pero en la simulación ese ramal no tiene conexión real. Esta herramienta lo detecta y lo soluciona automáticamente.

### Tolerancia

Usa la tolerancia de nudo configurada en **Barra Project → Valores por defecto**. Si el extremo de la tubería está a menos de esa distancia del eje de otra tubería, se considera una T a resolver.

---

## Check connectivity

**Barra Debug → Check connectivity** *(con sub-opción Delete isolated subzones)*

Analiza la conectividad de toda la red desde las fuentes de suministro (Reservoirs y Tanks). Identifica qué tuberías y nudos **no están conectados** a ninguna fuente.

![Resultado de Check connectivity: zonas aisladas coloreadas en rojo sobre el mapa](../assets/images/debug/check-connectivity.png)
*Zonas aisladas identificadas: en rojo los elementos sin conexión a ninguna fuente.*

### Opción 1: Check connectivity (solo visualización)

Colorea los elementos según su zona de conectividad. Los elementos sin conexión a ninguna fuente aparecen resaltados. No modifica la red.

### Opción 2: Delete isolated subzones

Abre un diálogo que pide el **número máximo de tuberías** de una subzona para eliminarla. Subzonas con ese número de tuberías o menos se eliminan automáticamente. Las de mayor tamaño se conservan aunque estén aisladas (pueden ser sectores válidos no conectados todavía).

Este umbral es útil para limpiar "basura" topológica — fragmentos de 1-3 tuberías que quedaron sueltos tras una importación.

> Ejecuta siempre **Remove overlapping elements** antes de **Check connectivity** para evitar que nudos duplicados generen falsos aislamientos.
