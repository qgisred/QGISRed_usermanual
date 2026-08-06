# 🧪 Analysis

La barra **Analysis** agrupa las herramientas de simulación hidráulica, visualización de resultados y exportación del modelo. Es la barra que cierra el ciclo de trabajo: una vez que el modelo está definido, verificado y calibrado, se usa esta barra para ejecutar EPANET, explorar los resultados en el mapa y exportar a otros formatos.

> Antes de simular es recomendable haber pasado las [verificaciones de topología y atributos](../verificaciones/README.md) para evitar errores de convergencia.

<figure><img src="../assets/images/analisis/barra-analysis.png" alt="Barra de herramientas Analysis de QGISRed"><figcaption><p>Barra de herramientas Analysis de QGISRed</p></figcaption></figure>
*Barra Analysis: simulación, visor de resultados, series temporales y exportación.*

---

## Herramientas de la barra Analysis

| # | Herramienta | Función |
|---|-------------|---------|
| 1 | **Run model** | Ejecuta la simulación EPANET y carga los resultados en el mapa |
| — | **Results browser** | Abre el panel de resultados con los datos de la última simulación |
| — | **Status report** | Abre el panel de resultados en la pestaña de informe de estado |
| 2 | **Analysis options…** | Configura los parámetros del motor EPANET (unidades, fórmula, tiempos, calidad) |
| 3 | **Time series…** | Activa la herramienta de gráficas de evolución temporal por elemento |
| 4 | **Export results to CSV…** | Exporta los resultados de simulación a archivos CSV separados para nudos y tuberías |
| 5 | **Export model to INP…** | Exporta el modelo completo al formato EPANET `.inp` |

*Run model, Results browser y Status report comparten un botón desplegable en la barra.*

---

## En esta sección

* [Ejecución y Opciones](ejecucion.md) — simulación, opciones del motor y acceso al informe de estado
* [Visor de Resultados](resultados.md) — panel de resultados, navegación temporal y series temporales
* [Exportación del Modelo](exportacion.md) — exportación a INP y a CSV de resultados
