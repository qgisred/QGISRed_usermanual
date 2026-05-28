# Ejecución y Opciones

Las tres primeras acciones de la barra Analysis controlan el ciclo de simulación: configurar las opciones del motor, lanzar la simulación y revisar el informe de estado.

---

## Analysis options…

**Barra Analysis → Analysis options…**

Abre el diálogo de opciones del motor EPANET. Permite configurar todos los parámetros que controlan cómo se realiza la simulación hidráulica y de calidad.

![Diálogo Analysis Options con pestañas de configuración del motor EPANET](../assets/images/analisis/analysis-options.png)
*Diálogo Analysis Options: configuración completa del motor EPANET.*

### Parámetros configurables

| Grupo | Parámetros principales |
|-------|------------------------|
| **Hydraulics** | Unidades de caudal (LPS, GPM, CMH…), fórmula de pérdida de carga (H-W / D-W / C-M), viscosidad, gravedad específica |
| **Quality** | Tipo de análisis de calidad (ninguno, cloro, edad del agua, traza de fuente), coeficientes de reacción |
| **Times** | Duración total de la simulación, paso de tiempo hidráulico, paso de tiempo de calidad, paso de informe, hora de inicio |
| **Energy** | Precio de la electricidad, eficiencia global de las bombas |
| **General** | Modo PDA (Pressure Dependent Analysis): activa la demanda dependiente de la presión local |

> La Tabla de materiales del proyecto almacena la rugosidad en unidades D-W (mm). Si cambias la fórmula hidráulica aquí, QGISRed te ofrecerá convertir automáticamente los coeficientes de rugosidad existentes.

---

## Run model

**Barra Analysis → Run model**

Lanza la simulación EPANET con las opciones configuradas y carga los resultados en el panel de resultados.

### Proceso

1. QGISRed valida el proyecto (capas activas, ninguna capa en edición).
2. Llama al motor EPANET a través del toolkit de QGISRed.
3. Al terminar, abre automáticamente el **panel de resultados** (Results dock) a la derecha de la pantalla y carga los datos calculados.
4. El mapa actualiza la simbología de las capas con los valores del primer instante de tiempo disponible.

Si la simulación detecta problemas (presiones negativas, nudos desconectados, bombas en cavitación), el informe de estado los registra con nivel de aviso.

---

## Results browser

**Barra Analysis → Results browser**

Abre el panel de resultados si ya existe una simulación previa para el proyecto activo, sin volver a simular. Si no hay resultados, lanza la simulación automáticamente.

Equivale a **Run model** pero priorizando los resultados ya calculados: si el archivo `.out` existe y corresponde al proyecto actual, los carga directamente. Útil para reabrir el visor tras cerrarlo sin perder los resultados.

---

## Status report

**Barra Analysis → Status report**

Abre el panel de resultados directamente en la pestaña **Status Report**, que muestra el informe de texto generado por el motor EPANET al finalizar la simulación.

El informe incluye:

- Balance de masa general de la red.
- Lista de nudos con presión negativa o fuera de rango.
- Advertencias de bombas operando fuera de su curva.
- Estado de convergencia del cálculo hidráulico en cada paso.
- Resumen de reacciones de calidad (si se simuló calidad).

> El informe de estado es el primer lugar donde mirar cuando una simulación produce resultados inesperados o no converge.
