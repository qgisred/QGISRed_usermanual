# 🧭 La Interfaz de QGISRed

QGISRed se integra en QGIS como un conjunto de **barras de herramientas especializadas**. Cada barra agrupa las herramientas de una etapa del flujo de trabajo: gestión de proyectos, edición de la red, verificación, simulación, etc.

![Barra de herramientas principal de QGISRed con los botones desplegables de cada toolbar](../assets/images/image14.png)
*Barra principal de QGISRed: cada botón desplegable activa/desactiva una barra de herramientas.*

---

## La barra principal

Al instalar el plugin aparece en QGIS una **barra principal** con un botón desplegable por cada toolbar secundaria. Haciendo clic en cualquiera de esos botones se muestra u oculta la barra correspondiente. Además, el desplegable de cada botón lista directamente todas las acciones de esa toolbar, permitiendo ejecutarlas sin necesidad de tener la barra visible.

A la derecha de la barra principal hay un **indicador de unidades** (por ejemplo `LPS | D-W`) que muestra las unidades de caudal y la fórmula de pérdida de carga del proyecto activo.

## Las barras de herramientas

QGISRed incluye **8 barras de herramientas** organizadas por área de trabajo:

| Barra | Función principal |
|-------|------------------|
| **General** | Crear, abrir e importar proyectos |
| **Project** | Configuración, capas y copia de seguridad |
| **Edition** | Dibujar y editar la red hidráulica |
| **Debug** | Verificar la calidad y consistencia del modelo |
| **Tools** | Herramientas de cálculo y gestión de datos |
| **Queries** | Consultar, filtrar y visualizar la información |
| **Analysis** | Simular y explorar resultados |
| **Digital Twin** | Acometidas, válvulas de corte y sensores |

> 💡 **CONSEJO**: Activa solo las barras que necesites en cada momento para mantener el espacio de trabajo ordenado. El estado de visibilidad de cada barra se guarda automáticamente entre sesiones.

## El proyecto QGISRed

Todos los datos de la red se almacenan en una carpeta de proyecto como archivos **SHP + DBF**. El nombre de la red (por ejemplo `MiRed`) es el prefijo común de todos esos archivos (`MiRed_Pipes.shp`, `MiRed_Junctions.shp`, etc.).

QGISRed no trabaja con el archivo `.qgz` de QGIS como fuente de verdad: la fuente de verdad siempre son los archivos SHP del proyecto. El `.qgz` es opcional y sirve para guardar la apariencia visual (estilos, capas visibles, etc.).

---

Consulta el [Resumen de barras de herramientas](toolbars.md) para ver qué hace cada herramienta, o salta directamente al [Flujo de trabajo típico](flujo-de-trabajo.md) si quieres empezar cuanto antes.
