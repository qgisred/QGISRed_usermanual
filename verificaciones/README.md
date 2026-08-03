# ✅ Debug

La barra **Debug** agrupa las herramientas de verificación y depuración del modelo. Su objetivo es detectar y corregir errores topológicos, inconsistencias de atributos y problemas de conectividad **antes de lanzar la simulación**, evitando así errores difíciles de diagnosticar en EPANET.

\*Barra Debug: validación de datos, depuración topológica, revisión de atributos y sectores hidráulicos.\*

***

## Herramientas de la barra Debug

### Grupo 1 — Topología y coherencia

| # | Herramienta                     | Función                                                                 |
| - | ------------------------------- | ----------------------------------------------------------------------- |
| 1 | **Check && commit data**        | Valida todos los datos del modelo y señala los elementos con errores    |
| 2 | **Remove overlapping elements** | Detecta y elimina nodos o tuberías duplicados en la misma posición      |
| 3 | **Simplify link vertices**      | Elimina vértices intermedios alineados en tramos rectos                 |
| 4 | **Join consecutive pipes**      | Fusiona tuberías adyacentes con idéntico diámetro, material y año       |
| 5 | **Create T connections**        | Detecta nudos de extremo sobre tuberías y crea la unión topológica      |
| 6 | **Check connectivity**          | Identifica zonas aisladas de las fuentes de suministro                  |
| — | _Delete isolated subzones_      | (Sub-opción) Elimina subzonas con menos tuberías que el umbral definido |

### Grupo 2 — Verificación de atributos

| #  | Herramienta                       | Función                                                                |
| -- | --------------------------------- | ---------------------------------------------------------------------- |
| 7  | **Check pipe lengths**            | Compara longitudes de atributo vs. geometría y señala diferencias      |
| 8  | **Check diameters**               | Detecta diámetros fuera del rango habitual del proyecto                |
| 9  | **Check pipe materials**          | Detecta materiales no definidos en la tabla de materiales del proyecto |
| 10 | **Check pipe installation dates** | Detecta fechas de instalación con formato incorrecto o inconsistentes  |

### Grupo 3 — Sectores hidráulicos

| #  | Herramienta                 | Función                                                                    |
| -- | --------------------------- | -------------------------------------------------------------------------- |
| 11 | **Check hydraulic sectors** | Clasifica las zonas de la red según su capacidad de suministro (tipos A–D) |

***

## En esta sección

* [Topología y conectividad](topologia.md) — commit, overlapping, simplify, join, T-connections, conectividad
* [Verificación de atributos](atributos.md) — longitudes, diámetros, materiales, fechas de instalación
* [Sectores hidráulicos](sectores.md) — clasificación de sectores tipo A, B, C y D
