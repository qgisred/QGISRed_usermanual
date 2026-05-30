# Instalación desde Repositorio

Es el método recomendado. Instala QGISRed directamente desde el repositorio oficial de plugins de QGIS y permite recibir actualizaciones automáticas.

---

## Paso a paso

1. Abre QGIS.
2. Ve al menú **Complementos → Administrar e instalar complementos…**
3. En la pestaña **Todos**, escribe `QGISRed` en el cuadro de búsqueda.
4. Selecciona **QGISRed** en la lista de resultados.
5. Haz clic en **Instalar complemento**.

Al terminar, aparecerán en QGIS la barra principal de QGISRed y el menú **QGISRed** en la barra de menús.

---

## Primera ejecución

La primera vez que uses cualquier herramienta del plugin, QGISRed detecta que las **dependencias** no están instaladas y muestra un diálogo de instalación. Consulta [Gestión de dependencias](dependencias.md) para más detalles.

---

## Actualizaciones automáticas

Al arrancar QGIS, QGISRed comprueba si hay una nueva versión disponible. Si existe, se abrirá automáticamente la ventana de noticias de QGISRed informando de la nueva versión. Para actualizar desde ahí:

1. Ve a **Complementos → Administrar e instalar complementos…**
2. Abre la pestaña **Actualizables**.
3. Selecciona **QGISRed** y haz clic en **Actualizar complemento**.

> También puedes activar la actualización automática en la pestaña **Configuración** del gestor de complementos.

---

## Solución de problemas

**QGISRed no aparece en los resultados de búsqueda**

El gestor de complementos necesita tener configurado el repositorio oficial de QGIS. Ve a **Complementos → Administrar e instalar complementos… → Configuración** y verifica que el repositorio `https://plugins.qgis.org/plugins/plugins.xml` está activo.

**El botón "Instalar complemento" está desactivado**

Puede deberse a que la versión de QGIS instalada es anterior a 3.28. Actualiza QGIS primero.
