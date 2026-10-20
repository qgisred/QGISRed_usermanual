# ✅ Depuración

La barra **Depuración** agrupa las herramientas de verificación y depuración del modelo. Su objetivo es detectar y corregir errores topológicos, inconsistencias de atributos y problemas de conectividad **antes de lanzar la simulación**, evitando así errores difíciles de diagnosticar en EPANET.

<figure><img src="../assets/images/debug/toolbar.png" alt="Barra de herramientas Debug de QGISRed"><figcaption><p>Barra de herramientas Debug de QGISRed</p></figcaption></figure>
*Barra Debug: validación de datos, depuración topológica, revisión de atributos y sectores hidráulicos.*

---

## Herramientas de la barra Debug

### Grupo 1 — Topología y coherencia

| # | Herramienta | Función |
|---|-------------|---------|
| 1 | **Comprobar y confirmar datos** | Valida todos los datos del modelo y señala los elementos con errores |
| 2 | **Eliminar elementos superpuestos** | Detecta y elimina nodos o tuberías duplicados en la misma posición |
| 3 | **Simplificar vértices de líneas** | Elimina vértices intermedios alineados en tramos rectos |
| 4 | **Join consecutive pipes** | Fusiona tuberías adyacentes con idéntico diámetro, material y año |
| 5 | **Crear conexiones en T** | Detecta nudos de extremo sobre tuberías y crea la unión topológica |
| 6 | **Comprobar conectividad** | Identifica zonas aisladas de las fuentes de suministro |
| — | *Delete isolated subzones* | (Sub-opción) Elimina subzonas con menos tuberías que el umbral definido |

### Grupo 2 — Verificación de atributos

| # | Herramienta | Función |
|---|-------------|---------|
| 7 | **Comprobar longitudes de tuberías** | Compara longitudes de atributo vs. geometría y señala diferencias |
| 8 | **Comprobar diámetros** | Detecta diámetros fuera del rango habitual del proyecto |
| 9 | **Comprobar materiales de tuberías** | Detecta materiales no definidos en la tabla de materiales del proyecto |
| 10 | **Comprobar fechas de instalación de tuberías** | Detecta fechas de instalación con formato incorrecto o inconsistentes |

### Grupo 3 — Sectores hidráulicos

| # | Herramienta | Función |
|---|-------------|---------|
| 11 | **Comprobar sectores hidráulicos** | Clasifica las zonas de la red según su capacidad de suministro (tipos A–D) |

---

## En esta sección

* [Topología y conectividad](topologia.md) — commit, overlapping, simplify, join, T-connections, conectividad
* [Verificación de atributos](atributos.md) — longitudes, diámetros, materiales, fechas de instalación
* [Sectores hidráulicos](sectores.md) — clasificación de sectores tipo A, B, C y D
