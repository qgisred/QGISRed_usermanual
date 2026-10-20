# 🧬 Gemelo Digital

La barra **Gemelo Digital** añade al modelo hidráulico los elementos de infraestructura que conectan la red con el usuario final y con los sistemas de monitorización en campo: acometidas, válvulas de corte, medidores y sensores. Estos elementos no forman parte del modelo EPANET estrictamente pero enriquecen el gemelo digital con información operacional y de telelectura.

<figure><img src="../assets/images/digital-twin/toolbar.png" alt="Barra de herramientas Digital Twin de QGISRed"><figcaption><p>Barra de herramientas Digital Twin de QGISRed</p></figcaption></figure>
*Barra Digital Twin: acometidas, válvulas de corte, medidores y carga de datos de campo.*

---

## Herramientas de la barra Digital Twin

### Grupo 1 — Elementos de red

| # | Herramienta | Función |
|---|-------------|---------|
| 1 | **Añadir acometida** | Dibuja una acometida desde la tubería principal hasta el punto de suministro del cliente |
| 2 | **Añadir válvula de seccionamiento** | Añade una válvula de corte haciendo clic sobre una tubería |
| 3 | **Añadir medidor** (desplegable) | Coloca un medidor o sensor sobre una tubería. 11 tipos disponibles |

### Grupo 2 — Datos operacionales

| # | Herramienta | Función |
|---|-------------|---------|
| 4 | **Load meter readings…** | Carga lecturas de contadores inteligentes y las asocia a las acometidas del proyecto |
| 5 | **Establecer estado inicial de tuberías desde válvulas de seccionamiento** | Propaga el estado de apertura/cierre de las válvulas de corte al campo `InitStatus` de las tuberías afectadas |
| 6 | **Load field data…** | Importa datos de campo SCADA y los asocia a los medidores del proyecto |

### Grupo 3 — Integración en el modelo

| # | Herramienta | Función |
|---|-------------|---------|
| 7 | **Convertir acometidas en tuberías/nudos** | Convierte las acometidas en nudos puntuales o en tuberías del modelo EPANET |

---

## En esta sección

* [Acometidas y Válvulas de Corte](acometidas.md) — dibujo de acometidas, válvulas de corte y conversión al modelo hidráulico
* [Sensores y Medidores](sensores.md) — tipos de medidores, carga de lecturas y datos de campo
