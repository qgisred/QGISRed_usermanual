# Crear proyecto

**Barra General → Crear proyecto** (o menú QGISRed → General → Create project)

Crea un proyecto QGISRed completamente nuevo desde cero, generando la estructura de archivos SHP necesaria para definir una red de distribución.

\*Diálogo de creación de proyecto: nombre, carpeta y sistema de referencia.\*

***

## Paso a paso

### 1. Nombre de la red

Introduce un nombre corto y sin espacios ni caracteres especiales (letras, números y guion bajo son seguros). Este nombre será el **prefijo** de todos los archivos del proyecto.

* ✅ Correcto: `RedUrbana`, `Red_Norte_2024`, `SectorA`
* ❌ Evitar: `Red Urbana`, `Réseau_Côte`, `Red/Norte`

### 2. Carpeta del proyecto

Selecciona o crea la carpeta donde se guardarán todos los archivos. Pueden convivir **varios proyectos en la misma carpeta** siempre que tengan nombres diferentes.

### 3. Sistema de Referencia de Coordenadas (CRS)

Selecciona el CRS apropiado para tu área de trabajo. QGISRed lo asignará a todos los archivos SHP del proyecto.

> 💡 Si vas a importar geometría de otras fuentes (ortofoto, catastro, etc.), usa el mismo CRS que esas fuentes o el más habitual en tu país para evitar reprojetciones.

### 4. Opciones iniciales de EPANET

En el mismo diálogo puedes configurar los parámetros básicos del modelo:

| Parámetro                       | Descripción                                                                              |
| ------------------------------- | ---------------------------------------------------------------------------------------- |
| **Unidades de caudal**          | LPS (litros/segundo), GPM, CMH, etc. Determina si el proyecto trabaja en sistema SI o US |
| **Fórmula de pérdida de carga** | Darcy-Weisbach (D-W), Hazen-Williams (H-W) o Chezy-Manning (C-M)                         |

Estos parámetros se pueden cambiar después desde _Opciones del proyecto_, pero es recomendable establecerlos desde el principio porque afectan a las unidades que se muestran en todas las propiedades de la red.

### 5. Catálogo de materiales

Selecciona el **catálogo de materiales** que se usará en el proyecto. Este catálogo es un archivo `.dbf` que define los materiales de tubería disponibles (nombre, coeficiente de rugosidad inicial e incremento por envejecimiento).

QGISRed busca los catálogos disponibles en las carpetas `materials` y `global_defaults` de `%APPDATA%\QGISRed\`. Si no hay ningún catálogo instalado, el desplegable aparecerá vacío y el proyecto se creará sin materiales predefinidos.

> El catálogo de materiales se usa para estimar automáticamente la rugosidad de las tuberías en función de su material y antigüedad, lo que facilita la calibración del modelo hidráulico.

***

## Archivos generados

Al confirmar la creación, QGISRed genera los siguientes archivos en la carpeta elegida y los carga automáticamente en QGIS:

| Archivo                | Contenido                                             |
| ---------------------- | ----------------------------------------------------- |
| `{Red}_Junctions.shp`  | Nudos de demanda                                      |
| `{Red}_Pipes.shp`      | Tuberías                                              |
| `{Red}_Tanks.shp`      | Depósitos                                             |
| `{Red}_Reservoirs.shp` | Embalses o puntos de alimentación                     |
| `{Red}_Valves.shp`     | Válvulas de regulación                                |
| `{Red}_Pumps.shp`      | Bombas                                                |
| `{Red}_Options.dbf`    | Opciones de EPANET (unidades, fórmula, calidad…)      |
| `{Red}_Title.dbf`      | Metadatos del proyecto (nombre del escenario, notas…) |

Todos se agrupan en la leyenda de QGIS bajo un grupo llamado **"{Red}" → "Inputs"**.

***

## Qué hacer a continuación

Una vez creado el proyecto, el siguiente paso es **construir la red** usando la barra de **Edition**. Consulta la sección [Edición y Modelado](../../edicion-y-modelado/edicion/) para ver cómo añadir tuberías, nudos y elementos especiales.

> 💡 Si ya tienes un archivo `.inp` de EPANET, es más rápido usar [Importar proyecto](abrir-importar.md#importar-desde-epanet) que crear desde cero.
