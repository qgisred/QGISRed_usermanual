# Abrir e Importar Proyectos

QGISRed ofrece tres vías para empezar a trabajar con una red existente:

| Opción | Cuándo usarla |
|--------|---------------|
| **Abrir proyecto** | El proyecto ya fue creado con QGISRed y sus archivos SHP están en disco |
| **Importar proyecto** | Tienes un archivo `.inp` de EPANET o SHPs externos sin estructura QGISRed |
| **Añadir datos por importación** | Ya tienes un proyecto abierto y quieres incorporar datos adicionales |

---

## Abrir proyecto

**Barra General → Abrir proyecto**

Abre un proyecto QGISRed existente (creado previamente con el plugin) que no aparece en el Gestor de proyectos, o que fue movido de carpeta.

<figure><img src="../assets/images/general/abrir-proyecto.png" alt="Diálogo de apertura de proyecto"><figcaption><p>Diálogo de apertura de proyecto</p></figcaption></figure>
*Diálogo de apertura: introduce el nombre de la red y selecciona la carpeta.*

### Proceso

1. Introduce el **nombre de la red** exactamente como aparece en el prefijo de los archivos SHP (sin extensión).
2. Selecciona la **carpeta** donde están los archivos.
3. QGISRed verifica que exista `{nombre}_Pipes.shp` en esa carpeta y carga todas las capas del proyecto.

### Qué ocurre al abrir

- Se carga el grupo de capas **Inputs** con los 6 SHP base más cualquier capa auxiliar (demandas múltiples, fuentes, etc.).
- Si el proyecto tiene resultados de simulaciones anteriores, se carga también el grupo **Results**.
- Se leen las opciones del proyecto (`_Options.dbf`) y se actualiza el indicador de unidades en la barra principal.
- Si los estilos visuales (QML) han cambiado respecto a la versión del plugin con que se guardó, se actualizan automáticamente.

> 💡 La forma más rápida de abrir un proyecto conocido es hacer **doble clic** en el [Gestor de proyectos](gestor-proyectos.md). La opción "Abrir proyecto" es para proyectos que no aparecen en esa lista.

---

## Importar proyecto

**Barra General → Importar proyecto**

Convierte datos externos en un proyecto QGISRed. Soporta dos formatos de entrada:

### Importar desde EPANET (`.inp`) {#importar-desde-epanet}

El caso más habitual: tienes un modelo EPANET existente y quieres trabajar con él en QGISRed.

<figure><img src="../assets/images/general/importar-inp.png" alt="Diálogo de importación desde archivo INP de EPANET"><figcaption><p>Diálogo de importación desde archivo INP de EPANET</p></figcaption></figure>
*Diálogo de importación: selección de archivo .inp, nombre de red y carpeta destino.*

1. Selecciona el archivo `.inp`.
2. Indica el **nombre de la red** que tendrá el proyecto QGISRed (puede ser diferente al nombre interno del INP).
3. Elige la **carpeta destino** donde se crearán los SHP.
4. QGISRed convierte todos los elementos (nudos, tuberías, válvulas, bombas, curvas, patrones, controles…) a la estructura SHP+DBF.

> ⚠️ Las coordenadas del `.inp` deben estar en el mismo CRS que usarás en QGISRed. El plugin no reproyecta durante la importación.

**Qué se importa:**
- Todos los elementos de red (junctions, pipes, tanks, reservoirs, valves, pumps)
- Curvas (H-Q, eficiencia, volumen, pérdida de carga)
- Patrones de demanda
- Controles simples y reglas
- Opciones de simulación (unidades, fórmula, tiempos, energía, calidad)
- Demandas múltiples por nudo


### Importar desde SHPs externos

Si dispones de capas SHP con la geometría de la red pero sin la estructura interna de QGISRed, el importador permite mapear las columnas de atributos de cada capa a los campos esperados por el plugin.

Para cada tipo de elemento puedes seleccionar la capa SHP correspondiente y asignar sus campos a los atributos del modelo. Los campos reconocidos automáticamente (si el nombre coincide) se preseleccionan:

**Tuberías** — campos mapeables: ID, Longitud, Diámetro, Rugosidad, Coef. pérdidas, **Material**, Fecha instalación, Estado inicial, Coef. reacción en masa, Coef. reacción en pared, Tag, Descripción.

**Acometidas** — campos mapeables: ID, Longitud, Diámetro, Rugosidad, **Material**, Demanda base, Patrón, Activa, Fecha instalación, Tag, Descripción.

Los demás elementos (válvulas, bombas, depósitos, embalses, nudos, válvulas de aislamiento, medidores) disponen de sus propios conjuntos de campos mapeables.

Cuando la importación crea un proyecto nuevo, también se solicita el **catálogo de materiales** (igual que al crear un proyecto desde cero) y los parámetros básicos de EPANET (unidades y fórmula de pérdida de carga). Si se importa sobre un proyecto ya existente, estos parámetros se omiten.

> 💡 El campo **Material** de tuberías y acometidas se cruza con el catálogo de materiales del proyecto para estimar automáticamente la rugosidad en función de la antigüedad de la tubería.

---

## Añadir datos por importación

**Barra Project → Añadir datos por importación**

Disponible solo cuando hay un proyecto ya abierto. Permite enriquecer el proyecto con datos adicionales sin cerrar lo que hay cargado.

Casos de uso típicos:
- Incorporar una zona nueva de red diseñada en un `.inp` separado.
- Añadir demandas de una nueva base de datos.
- Integrar datos de un sector importado de otro sistema.

El proceso es el mismo que el de importación, pero los elementos importados se **añaden** al proyecto existente en lugar de crear uno nuevo. QGISRed verifica que no haya conflictos de IDs antes de incorporar los datos.

---

## Consideraciones al cambiar de equipo

Si copias la carpeta del proyecto a otro equipo:

1. Usa **Cargar** en el Gestor de proyectos para añadirlo al historial local.
2. Si el proyecto tiene un `.qgz` guardado, ábrelo desde QGIS normalmente — QGISRed lo reconocerá automáticamente.
3. Si el `.qgz` no está o las rutas han cambiado, usa **Abrir proyecto** para cargarlo desde los SHP directamente.
