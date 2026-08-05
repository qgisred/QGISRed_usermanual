# Instalación desde ZIP local

Usa este método cuando necesites instalar una versión específica del plugin que no está en el repositorio, o cuando el equipo no tiene acceso a internet en el momento de la instalación.

***

## Obtener el archivo ZIP

Descarga el archivo `QGISRed.zip` desde:

* El repositorio oficial de QGIS Plugins (sección de versiones anteriores).
* El repositorio de GitHub del proyecto.
* Un archivo compartido por el equipo de desarrollo.

***

## Paso a paso

1. Abre QGIS.
2. Ve al menú **Complementos → Administrar e instalar complementos…**
3. Selecciona la pestaña **Instalar a partir de ZIP**.
4. Haz clic en el botón `…` y selecciona el archivo `QGISRed.zip`.
5. Haz clic en **Instalar complemento**.

<figure><img src="../.gitbook/assets/instalar-desde-zip.png" alt="Instalación desde ZIP"><figcaption><p>Pestaña "Instalar a partir de ZIP" del gestor de complementos de QGIS.</p></figcaption></figure>

***

## Aviso de seguridad

QGIS mostrará un aviso indicando que el complemento no procede del repositorio oficial. Esto es normal para cualquier instalación desde archivo local. Pulsa **Sí** para continuar con la instalación.

***

## Notas

* Si ya tienes una versión anterior de QGISRed instalada, la instalación desde ZIP la reemplaza. Los proyectos existentes no se ven afectados.
* Las **dependencias** no están incluidas en el ZIP del plugin. Se descargan por separado la primera vez que usas el plugin, igual que en la instalación desde repositorio. Si el equipo no tiene conexión a internet, consulta la sección [Gestión de dependencias](dependencias.md) para ver cómo instalarlas manualmente.
* Esta instalación **no recibe actualizaciones automáticas**. Para actualizar, tendrás que repetir el proceso con el ZIP de la versión nueva.
