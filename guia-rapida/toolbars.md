# Resumen de Barras de Herramientas

Una visión de conjunto de todo lo que QGISRed puede hacer, organizado por toolbar.

---

## 🗂️ General — Gestión de proyectos

Punto de entrada para cualquier sesión de trabajo. Desde aquí creas, abres o importas proyectos.

| Herramienta | Qué hace |
|-------------|----------|
| **Gestor de proyectos** | Lista de proyectos recientes, clonar, renombrar, borrar |
| **Abrir proyecto** | Abre un proyecto existente indicando nombre y carpeta |
| **Crear proyecto** | Genera la estructura de archivos SHP para una red nueva |
| **Importar proyecto** | Crea un proyecto a partir de un archivo `.inp` de EPANET o SHPs externos |

---

## 📋 Project — Configuración y capas

Herramientas de administración del proyecto abierto.

| Herramienta | Qué hace |
|-------------|----------|
| **Resumen** | Muestra el número de elementos de cada tipo en la red |
| **Añadir datos por importación** | Importa elementos adicionales al proyecto ya abierto |
| **Gestor de capas** | Controla qué capas están activas; recupera capas borradas accidentalmente |
| **Editor de leyenda** | Personaliza la simbología de cualquier capa del proyecto |
| **Opciones del proyecto** | Configura las opciones de EPANET: unidades, fórmula de pérdidas, calidad |
| **Valores por defecto** | Define prefijos de ID, tolerancias geométricas y valores hidráulicos iniciales |
| **Tabla de materiales** | Gestiona la lista de materiales con sus rugosidades iniciales e incrementos por edad |
| **Guardar mapa** | Guarda el proyecto QGIS (`.qgz`) |
| **Copia de seguridad** | Crea una copia de todos los archivos del proyecto en una subcarpeta con fecha |
| **Cerrar proyecto** | Cierra el proyecto actual |

---

## ✏️ Edition — Creación y edición de la red

Herramientas para dibujar y modificar la topología de la red directamente sobre el mapa.

| Herramienta | Qué hace |
|-------------|----------|
| **Añadir tubería** | Dibuja una tubería; crea automáticamente los nudos extremos |
| **Añadir depósito** | Convierte un nudo existente en depósito (Tank) |
| **Añadir embalse** | Convierte un nudo existente en embalse (Reservoir) |
| **Insertar válvula** | Divide una tubería e inserta una válvula |
| **Insertar bomba** | Divide una tubería e inserta una bomba |
| **Seleccionar elementos** | Selección múltiple de nudos y líneas |
| **Mover nudos** | Desplaza un nudo arrastrándolo; mantiene la conectividad |
| **Editar vértices** | Añade, mueve o borra vértices intermedios de una tubería |
| **Invertir enlace** | Cambia la dirección de flujo de referencia en tuberías/válvulas/bombas |
| **Partir / Unir tuberías** | Divide una tubería en un punto o une dos tuberías consecutivas |
| **Partir / Fusionar nudos** | Separa un nudo en dos o fusiona nudos superpuestos |
| **Crear / Revertir T** | Crea o deshace una conexión en T sobre una tubería existente |
| **Crear / Revertir cruce** | Gestiona cruces entre tuberías que se solapan geográficamente |
| **Mover válvula / bomba** | Reposiciona una válvula o bomba a otra tubería |
| **Cambiar estado** | Modifica el estado inicial (Abierto/Cerrado/CV) de tuberías, válvulas y bombas |
| **Eliminar elementos** | Borra elementos seleccionados y recompone la conectividad |
| **Editar propiedades** | Abre el formulario de atributos de un elemento |
| **Patrones y curvas** | Gestiona curvas de demanda, eficiencia y altura-caudal |
| **Controles y reglas** | Define controles simples y reglas basadas en condiciones |

---

## 🐛 Debug — Verificación y depuración

Herramientas para garantizar la integridad topológica y de atributos del modelo.

| Herramienta | Qué hace |
|-------------|----------|
| **Consolidar y revisar datos** | Verifica y consolida todos los atributos; genera un informe de incidencias |
| **Eliminar elementos superpuestos** | Detecta y borra tuberías o nudos duplicados en la misma posición |
| **Simplificar vértices de enlace** | Elimina vértices redundantes en tramos rectos |
| **Unir tuberías consecutivas** | Fusiona tuberías contiguas con igual diámetro, material y año de instalación |
| **Crear conexiones en T** | Crea nudos de conexión donde tuberías se cruzan sin nudo común |
| **Verificar conectividad** | Analiza la conectividad de la red e identifica zonas aisladas |
| **Eliminar zonas aisladas** | Borra subzonas sin conexión a ninguna fuente de presión |
| **Verificar longitudes** | Detecta tuberías demasiado cortas o largas respecto a los umbrales definidos |
| **Verificar diámetros** | Revisa que los diámetros estén dentro de rangos válidos |
| **Verificar materiales** | Detecta tuberías sin material asignado |
| **Verificar fechas** | Comprueba coherencia en las fechas de instalación |
| **Sectores hidráulicos** | Calcula y visualiza los sectores de la red (H-Q, H-nQ, nH-Q, nH-nQ) según su relación con fuentes y nudos de demanda |

---

## 🔧 Tools — Herramientas de cálculo

Utilidades para automatizar tareas de preparación y gestión del modelo.

| Herramienta | Qué hace |
|-------------|----------|
| **Calcular longitudes** | Recalcula las longitudes de las tuberías a partir de su geometría |
| **Interpolar cotas** | Asigna cotas a los nudos a partir de un MDT en formato `.asc` |
| **Asignar rugosidades** | Calcula el coeficiente de rugosidad a partir del material y la antigüedad |
| **Convertir rugosidades** | Transforma los coeficientes de rugosidad entre fórmulas (D-W ↔ H-W ↔ C-M) |
| **Gestor de demandas** | Distribuye consumos entre nudos desde polígonos de área o puntos georeferenciados |
| **Constructor de escenarios** | Exporta e importa en bloque parámetros del modelo (rugosidades, demandas, cotas, estados, calidades) para gestionar variantes sin duplicar proyectos |
| **Segmentos aislados** | Calcula los segmentos que quedarían aislados al cerrar cada válvula de corte |
| **Sectores de demanda** | Genera sectores basados en la demanda y patrones de consumo |
| **Árbol de mínimo coste** | Calcula el árbol de expansión de mínima resistencia hidráulica desde un nudo origen seleccionado |

---

## 🔍 Queries — Consultas

Herramientas de consulta e inspección del modelo sin modificar sus datos.

| Herramienta | Qué hace |
|-------------|----------|
| **Buscar elemento por ID** | Localiza y selecciona cualquier elemento a partir de su identificador |
| **Propiedades del elemento** | Muestra todas las propiedades de un elemento al hacer clic sobre él |
| **Mapas temáticos** | Genera capas de visualización temática por cualquier atributo numérico |
| **Consultas por propiedades** | Filtra elementos que cumplen condiciones sobre sus atributos |
| **Estadísticas** | Calcula estadísticas descriptivas de cualquier campo numérico |

---

## 📊 Analysis — Simulación y resultados

Herramientas para ejecutar la simulación hidráulica y explorar los resultados.

| Herramienta | Qué hace |
|-------------|----------|
| **Ejecutar modelo** | Lanza la simulación EPANET y carga los resultados como capas |
| **Visor de resultados** | Abre el panel lateral para explorar variables en el tiempo |
| **Informe de estado** | Muestra el informe de texto generado por EPANET |
| **Opciones de análisis** | Configura hidráulica, calidad, tiempos y energía |
| **Series temporales** | Representa gráficamente la evolución temporal de un elemento |
| **Exportar resultados** | Exporta todos los resultados a archivos CSV |
| **Exportar a INP** | Genera un archivo `.inp` compatible con EPANET |

---

## 🧬 Digital Twin — Gemelo Digital

Elementos avanzados para representar la infraestructura real de la red.

| Herramienta | Qué hace |
|-------------|----------|
| **Añadir acometida** | Crea una conexión de servicio desde la red hasta un punto de consumo |
| **Añadir válvula de corte** | Incorpora válvulas manuales de seccionamiento a la red |
| **Añadir medidor** (submenú) | Añade distintos tipos de sensores: caudalímetro, manómetro, contador, nivel, calidad, energía, estado, apertura, tacómetro |
| **Cargar lecturas** | Importa lecturas reales de sensores para calibración o comparación |
| **Estado inicial desde válvulas** | Aplica el estado real de las válvulas de corte como estado inicial del modelo |
| **Cargar datos de campo** | Importa datos georeferenciados de campañas de aforo |
| **Convertir acometidas** | Transforma las acometidas en tuberías y nudos de demanda del modelo |
