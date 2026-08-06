# 🧬 Digital Twin

La barra **Digital Twin** añade al modelo hidráulico los elementos de infraestructura que conectan la red con el usuario final y con los sistemas de monitorización en campo: acometidas, válvulas de corte, medidores y sensores. Estos elementos no forman parte del modelo EPANET estrictamente pero enriquecen el gemelo digital con información operacional y de telelectura.

<figure><img src="../assets/images/gemelo-digital/barra-digital-twin.png" alt="Barra de herramientas Digital Twin de QGISRed"><figcaption><p>Barra de herramientas Digital Twin de QGISRed</p></figcaption></figure>
*Barra Digital Twin: acometidas, válvulas de corte, medidores y carga de datos de campo.*

---

## Herramientas de la barra Digital Twin

### Grupo 1 — Elementos de red

| # | Herramienta | Función |
|---|-------------|---------|
| 1 | **Add service connection** | Dibuja una acometida desde la tubería principal hasta el punto de suministro del cliente |
| 2 | **Add isolation valve** | Añade una válvula de corte haciendo clic sobre una tubería |
| 3 | **Add meter** (desplegable) | Coloca un medidor o sensor sobre una tubería. 11 tipos disponibles |

### Grupo 2 — Datos operacionales

| # | Herramienta | Función |
|---|-------------|---------|
| 4 | **Load meter readings…** | Carga lecturas de contadores inteligentes y las asocia a las acometidas del proyecto |
| 5 | **Set pipe's initial status from isolation valves** | Propaga el estado de apertura/cierre de las válvulas de corte al campo `InitStatus` de las tuberías afectadas |
| 6 | **Load field data…** | Importa datos de campo SCADA y los asocia a los medidores del proyecto |

### Grupo 3 — Integración en el modelo

| # | Herramienta | Función |
|---|-------------|---------|
| 7 | **Convert service connections into pipes/nodes** | Convierte las acometidas en nudos puntuales o en tuberías del modelo EPANET |

---

## En esta sección

* [Acometidas y Válvulas de Corte](acometidas.md) — dibujo de acometidas, válvulas de corte y conversión al modelo hidráulico
* [Sensores y Medidores](sensores.md) — tipos de medidores, carga de lecturas y datos de campo
