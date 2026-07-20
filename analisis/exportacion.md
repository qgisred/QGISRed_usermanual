# Exportación del Modelo

La barra Analysis ofrece dos vías de exportación: el modelo completo como archivo EPANET `.inp`, y los resultados de simulación como tablas CSV.

---

## Export model to INP…

**Barra Analysis → Export model to INP…**

Exporta el modelo completo al formato estándar **INP** de EPANET. Útil para compartir el modelo con otros usuarios, ejecutarlo en la interfaz gráfica de EPANET o integrarlo con herramientas de terceros.

<figure><img src="../assets/images/analisis/export-inp-dialog.png" alt="Diálogo de exportación al formato INP"><figcaption><p>Diálogo de exportación al formato INP</p></figcaption></figure>
*Diálogo Export to INP: ruta de destino, exportación de datos de campo y apertura automática en EPANET.*

### Opciones del diálogo

| Opción | Descripción |
|--------|-------------|
| **INP file** | Ruta completa del archivo `.inp` a generar. Usa el botón `…` para navegar. |
| **Export field data files** | Exporta también los archivos auxiliares de datos de campo asociados al modelo. |
| **Open INP file with EPANET** | Si está activo, abre el `.inp` en EPANET al finalizar la exportación. |
| **Epanet path** | Ejecutable de EPANET detectado en el sistema. El desplegable muestra todas las versiones instaladas. |
| **Specific Epanet path** | Ruta manual a un ejecutable de EPANET no detectado automáticamente. |

Pulsa **Export to INP** para generar el archivo con la configuración elegida.

---

## Export results to CSV…

**Barra Analysis → Export results to CSV…**

Exporta los resultados de la última simulación a dos archivos CSV: uno para nudos y otro para tuberías. Es el método estándar para llevar los resultados a Excel, Python, R u otras herramientas de análisis externo.

> Solo disponible si existe un archivo `.out` de simulación para el escenario activo.

### Opciones del diálogo

| Opción | Descripción |
|--------|-------------|
| **Nodes CSV** | Ruta del archivo de salida para los resultados de nudos. Por defecto `{Red}_{Escenario}_Nodes.csv` en la carpeta `Results/`. |
| **Links CSV** | Ruta del archivo de salida para los resultados de tuberías. Por defecto `{Red}_{Escenario}_Links.csv`. |
| **List separator** | Separador de campos (detectado automáticamente del sistema regional; habitual `;` en locales europeas). |
| **Decimal separator** | Separador decimal (detectado del sistema; habitual `,` en locales europeas). |

### Contenido de los archivos

**Nodes CSV** — una fila por instante de tiempo por nudo, con columnas:

`Time | ID | Pressure | Head | Demand | Quality`

**Links CSV** — una fila por instante de tiempo por tubería/válvula/bomba, con columnas:

`Time | ID | Status | Flow | Velocity | HeadLoss | UnitHdLoss | FricFactor | ReactRate | Quality`

> Los separadores se adaptan a la configuración regional del sistema operativo para que el archivo se abra correctamente en Excel sin necesidad de conversión.
