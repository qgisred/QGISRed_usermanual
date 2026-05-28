# Requisitos del Sistema

Antes de instalar QGISRed, verifica que tu equipo cumple los siguientes requisitos.

---

## Sistema operativo

**Windows 10 o superior** (x86 o x64).

QGISRed no está disponible para Linux ni macOS. El motor de cálculo utiliza DLLs compiladas en .NET que requieren el entorno Windows.

---

## QGIS

**Versión 3.28 o superior**, incluyendo la serie 4.x.

### Cómo verificar tu versión de QGIS

Ve a **Ayuda → Acerca de QGIS**. La versión aparece en la primera línea del diálogo.

Si tu versión es anterior a 3.28, descarga la versión LTR (Long Term Release) más reciente desde [qgis.org](https://qgis.org/download/).

> Las versiones anteriores a 3.28 ya no son compatibles con el plugin desde QGISRed 0.18. Si necesitas trabajar con una versión antigua de QGIS, usa QGISRed 0.17 o anterior.

---

## .NET Framework

**Versión 4.8**.

### Cómo verificar si está instalado

1. Abre el **Panel de control → Programas → Programas y características**.
2. Haz clic en **Activar o desactivar las características de Windows**.
3. Busca **.NET Framework 4.8** en la lista. Si aparece marcado, ya está instalado.

En Windows 10 versión 1903 o superior, .NET Framework 4.8 viene preinstalado. En versiones anteriores o en Windows Server, puede ser necesario descargarlo e instalarlo manualmente desde Microsoft.

---

## Conexión a internet

Necesaria **la primera vez** que se usa el plugin, para descargar las GISRed libraries (las DLLs del motor de cálculo). Las descargas posteriores (actualizaciones del plugin) también requieren conexión.

Una vez instaladas las dependencias, QGISRed puede funcionar **sin conexión a internet**.
