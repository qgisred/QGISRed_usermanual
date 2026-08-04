# Versiones Anteriores

Aquí puedes consultar el historial detallado de cambios de las versiones previas de QGISRed.

### Versión 0.16
**Versiones de QGis**: 3.2-3.99 

**Características**:
*   Nuevas opciones en el gestor de demandas nodales para declarar el consumo para toda la red o por zonas.
*   Posibilidad de exportar, editar y reimportar los enlaces entre los consumos puntuales y los nudos.
*   Nuevas opciones para importar/exportar/eliminar escenarios de demanda por categorías.
*   Nuevas herramientas en el gestor de demandas nodales para considerar la eficiencia hídrica o asignar patrones de consumo por sectores.
*   Nuevo Gestor de Escenarios para almacenar y recuperar en bloque diversos parámetros del modelo.
*   Cálculo automático de la longitud de las tuberías a partir de las coordenadas de los vértices.
*   Completado automático del trazado de las acometidas mediante un tramo perpendicular a la tubería más próxima o un enlace al nudo más próximo.
*   Posibilidad de trazar automáticamente acometidas de longitud prefijada desde un punto de una tubería o un nudo.
*   Nueva opción para reflejar una acometida con la herramienta de invertir.
*   Nueva opción de importar acometidas como puntos, creando perpendiculares a las tuberías o conexiones a los nudos más próximos.
*   Nuevo campo IsActive en acometidas para definir si está operativa o no.
*   Verificación del punto de contacto de una acometida con alguna tubería o nudo por ambos extremos.
*   Antes de calcular la sectorización hidráulica se transmite ahora el estado de las válvulas manuales.
*   Al exportar a INP el coeficiente de pérdidas de las válvulas de corte se transmite a las tuberías.
*   Declaración, edición y borrado de medidores de diversos tipos, como nuevos elementos del Gemelo Digital.
*   Edición, lectura y guardado de las señales asociadas a los medidores.
*   Nuevo diálogo para leer los datos de campo y exportar a CSV aquellos correspondientes al intervalo de simulación.
*   Nueva opción para exportar los datos de campo, junto al fichero INP.
*   Nuevos campos en el diálogo de importación para importar más información de los elementos.
*   Nueva opción para mostrar en los temas auxiliares los elementos con alguna incidencia durante la importación.
*   Nuevos botones y nueva deslizadera en el panel de resultados.
*   Mejoras en las etiquetas para mostrar los resultados.
*   Nuevo tipo de resultado para visualizar el Status de las líneas.
*   Mejoras en las búsquedas desde el editor de propiedades.
*   Desplegable con rutas de ejecutables de EPANET al exportar INP para apertura automática.
*   Clasificación de patrones por tipo al importar INP.
*   Nuevo warning cuando se autocompleta el Id de algún elemento.
*   Cambios en el orden, nombres e iconos de la barra de herramientas y estilos visuales.
*   Nuevo enlace a la web de QGISRed en la ventana de info.

**Correcciones**:
*   Corregida la lectura y edición del Id de la curva en válvulas GPV.
*   Corregido error al asignar valores por defecto en la importación de coeficientes de reacción.
*   Corregido error y mensaje al leer fuentes contaminantes en depósitos y embalses.
*   Corregido problema con herramientas de selección puntual.
*   Corregido error en creación masiva de conexiones en T.
*   Corregidos errores en selección múltiple y por polígono con diferentes CRS.
*   Corregido error con snapping en QGIS 3.26.

---

### Versión 0.15
**Versiones de QGis**: 3.2-3.99 

**Características**:
*   Gestión de válvulas manuales (importación, creación, borrado, edición de propiedades, interacción con el estado de las tuberías...).
*   Nueva herramienta para cambiar el estado de los elementos lineales y válvulas manuales.
*   Nueva simbolización de tuberías, bombas, válvulas de regulación y manuales según su estado.
*   Anulación de las demandas aisladas por el cierre de tuberías o válvulas superpuestas durante las simulaciones.
*   Asignación de demandas a los nudos a partir de sectores de demanda y demandas puntuales, con diversas opciones.
*   Mejoras en la ventana de edición de propiedades (selección múltiple, elementos conectados, elementos visitados, centrar elemento seleccionado).
*   Revisión y ampliación de las opciones de análisis (hidráulicas, calidad, tiempos y energía).
*   Incorporación de los nuevos parámetros de Epanet 2.2 a los formularios (rebose depósitos, demandas dependientes de la presión).
*   Resaltados los botones/menús de la barra de herramientas principal.
*   Idioma por defecto y único el inglés (por ahora).
*   Mejora de la edición de rules (con times y clocktimes).

**Correcciones**:
*   Corregido error al escribir valores de demanda con más de 4 dígitos.
*   Corregido error con los labels de tiempo para seleccionar resultados.
*   Corregido error al convertir números en la interpolación de cotas.
*   Corregidos errores con la lectura, escritura y orden de las rules.
*   Corregido error con rules usando la coma como separador decimal.
*   Corregido problema al asignar la proyección del proyecto.
*   Corregido error al editar propiedades trabajando con capas ráster.

---

### Versión 0.14
**Versiones de QGis**: 3.2-3.99

**Características**:
*   **Corregido error grave** al leer metadatos de modelos anteriores que impedía trabajar con ellos.
*   Corregido error al instalar el plugin sin disponer de dependencias previas.
*   Corregido error con el formato de la hora en leyes de control simples.
*   Visualización del separador decimal definido por el usuario.
*   Nueva herramienta para editar la geometría de las acometidas.
*   La opción hidráulica `demand multiplier` admite ahora decimales.
*   Prioridad de los elementos del Gemelo Digital al seleccionar objetos.

---

### Versión 0.13
**Versiones de QGis**: 3.2-3.99

**Características**:
*   Nuevo menú para agrupar herramientas de Gemelos Digitales.
*   Creación de acometidas con herramienta propia e integración en borrado.
*   Ficha específica para editar propiedades de acometidas.
*   Carga de telelectura bajo diferentes formatos a acometidas o nudos.
*   Incorporación de curvas de modulación de acometidas al editor general.
*   Nuevo gestor de demandas para importación/exportación y borrado selectivo.
*   Mejora de tiempos de acceso a propiedades en redes de gran tamaño.
*   Apertura optativa de INP en EPANET tras exportar.
*   Nuevas opciones para definir unidades y fórmulas de pérdida de carga desde GIS.
*   Corregido formato de tiempo para permitir días.
*   Corregida lectura de fechas en metadatos y diversos errores de importación SHP.

---

### Versión 0.12
**Versiones de QGis**: 3.14-3.99

**Características**:
*   Edición de la tabla de materiales-rugosidad para cálculo según material y edad.
*   Nueva importación y exportación de patrones/curvas en formato CSV.
*   Importación de demandas base e IDs de curvas desde CSV.
*   Importación de acometidas desde SHP.
*   Nueva herramienta para obtener el árbol de mínima resistencia.
*   Actualización de la librería de Epanet a la **versión 2.2**.
*   Mejorada la interfaz de conversión de coeficientes de rugosidad.
*   Corrección de errores en resultados de calidad y nudos sin coordenadas.
*   Inserción de válvulas/bombas evitando longitudes negativas.

---

### Versión 0.11
**Versiones de QGis**: 3.2-3.99

**Características**:
*   Archivo JSON local para proyecciones (.prj) sin internet.
*   Lectura de formatos PUMPS heredados de Epanet 1.1.
*   Nuevo instalador único (x86 y x64).
*   Muestra de unidades y fórmula de pérdida en la barra de estado.
*   Estimación de rugosidad por edad/material compatible con varias fórmulas.
*   Herramienta para crear copia de seguridad del proyecto.
*   Corrección de errores en QGIS 3.14.15 y formato de horas AM/PM.

---

### Versión 0.10
**Versiones de QGis**: 3.0-3.14.1

**Características**:
*   Escritura de cabeceras INP en inglés.
*   Validación para impedir mismo nudo final en líneas.
*   Simplificación de vértices duplicados en puntos iniciales.
*   Unificación de metadatos en archivo `_Metadata.txt`.
*   Aviso de versiones nuevas disponible.
*   Control de visibilidad de capas mediante `LayerManagement`.
*   Separación entre Importar (sin proyecto) y Añadir (con proyecto).
*   Tolerancia espacial al añadir datos desde SHPs.
*   Manual incluye formato ASCII para interpolación y clasificación de sectores hidráulicos.

---

### Versión 0.9
**Versiones de QGis**: 3.0-3.99

**Características**:
*   Nuevo logo de QGISRed.
*   Creación ágil de tuberías, depósitos y embalses con anclaje.
*   Edición de trazado (mover, crear, borrar vértices).
*   Inversión de orientación de líneas.
*   Herramientas para dividir/unir tuberías y nudos.
*   Creación/deshacer conexiones en T y cruces.
*   Desplazamiento de válvulas y bombas.
*   Selección múltiple (Ctrl añade, Shift elimina) y borrado por polígono.
*   Acceso a últimos resultados sin simular de nuevo.

---

### Versión 0.8
**Versiones de QGis**: 3.0-3.99

**Características**:
*   Edición de propiedades mediante ventana de diálogo con navegador.
*   Inserción/Eliminación inteligente de válvulas y bombas en tuberías.
*   Edición del trazado moviendo nudos y elementos coincidentes.
*   Soporte para 5 categorías de herramientas.
*   Diálogos para opciones de cálculo y valores por defecto.
*   Verificación de IDs repetidos.
*   Ocultación de tablas de datos en la leyenda.
*   Visualización de resultados mediante etiquetas fijas.

---

### Versión 0.7
**Versiones de QGis**: 3.0-3.99

**Características**:
*   Tabla resumen del modelo.
*   Gestor de Curvas de modulación (Patterns): editar, crear, clonar, exportar/importar.
*   Gestor de Curvas de comportamiento: soporte para 1 o 3 puntos con ecuación aproximada.
*   Gestor de Controles Simples e Interactivos.
*   Gestor de Rules: combinación de condiciones OR/AND interactiva.

---

### Versión 0.6
**Versiones de QGis**: 2.0-3.99

**Características**:
*   Gestión de proyectos (abrir, crear, importar, clonar, borrar).
*   Creación de capas vectoriales SHP para elementos base de EPANET.
*   Importación de datos desde INP o SHPs.
*   Validación del modelo e informes de errores.
*   Exportación a INP con apertura automática opcional.
*   Simulación con Toolkit de EPANET.
*   Herramientas de trazado (eliminación de superpuestos, conectividad, sectores).
