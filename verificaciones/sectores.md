# Sectores Hidráulicos

**Barra Debug → Check hydraulic sectors**

La herramienta de sectores hidráulicos recorre la red mediante un algoritmo BFS (búsqueda en anchura) desde todas las fuentes de suministro y clasifica cada subred conectada según si tiene o no fuente hidráulica (H) y si tiene o no demanda (Q). El resultado se vuelca en capas SHP y en un informe CSV.

<figure><img src="../assets/images/debug/sectores-hidraulicos.png" alt="Mapa de sectores hidráulicos: zonas coloreadas por tipo H-Q, H-nQ, nH-Q y nH-nQ"><figcaption><p>Mapa de sectores hidráulicos: zonas coloreadas por tipo H-Q, H-nQ, nH-Q y nH-nQ</p></figcaption></figure>
*Sectores hidráulicos: cada color representa un tipo de clasificación. Los sectores nH-Q (sin fuente con demanda) aparecen en rojo.*

---

## Clasificación de sectores

La herramienta asigna a cada sector uno de estos cuatro tipos. Estas son las **etiquetas reales** que aparecen en la capa SHP y en el informe CSV:

| Etiqueta | Fuente (H) | Demanda (Q) | Significado |
|----------|-----------|-------------|-------------|
| **H-Q** | ✅ Sí | ✅ Sí | Sector funcional: tiene fuente de suministro y nudos con demanda. Puede simularse correctamente. |
| **H-nQ** | ✅ Sí | ❌ No | Sector latente: tiene fuente pero ningún nudo con demanda > 0. Puede simularse pero sin flujo real. |
| **nH-Q** | ❌ No | ✅ Sí | **Sector crítico**: nudos con demanda pero sin ninguna fuente conectada. EPANET no convergirá. |
| **nH-nQ** | ❌ No | ❌ No | Sector pasivo: ni fuente ni demanda. No causa error en la simulación pero está desconectado. |

> **H** = presencia de al menos un Tank o Reservoir en el sector.  
> **Q** = presencia de al menos un Junction con demanda base > 0.  
> **n** = negación (ausencia de esa condición).

Existe además un pseudo-sector especial llamado **ClosedLinks** que agrupa las tuberías con estado `Closed` que quedan fuera de cualquier sector conectado. No cuenta en el total de sectores del informe.

---

## Salidas generadas

La herramienta produce tres salidas que se añaden automáticamente al proyecto:

| Salida | Tipo | Contenido |
|--------|------|-----------|
| `HydraulicSectors` | Capa SHP | Geometría de todos los elementos coloreados por tipo de sector |
| `HydraulicSectors_IsolatedDemands` | Capa SHP | Nudos y acometidas del tipo **nH-Q** con su demanda aislada |
| `{Red}_HydraulicSectors_Report.csv` | CSV | Tabla con ID de sector, número de elementos y clasificación |

El CSV tiene el formato:
```
SectorID; NumElements; Classification
S1; 1 243; H-Q
S2; 47; H-nQ
S3; 12; nH-Q
S4; 3; nH-nQ
```

---

## Cómo interpretar cada tipo

### H-Q — Funcional

Estado correcto. Todo sector que se vaya a simular debe ser H-Q. Una red correctamente construida tendrá un único sector H-Q grande (o varios si hay sectorización hidráulica real con válvulas cerradas entre ellos).

### H-nQ — Latente

Hay una fuente conectada pero todos los nudos de ese sector tienen demanda = 0. Causas habituales:

- Zona de la red importada sin datos de demanda asignados todavía.
- Bypass o ramal de reserva sin consumidores (puede ser correcto por diseño).

En el primer caso, hay que asignar demandas antes de que la simulación sea realista.

### nH-Q — Crítico (el más importante a corregir)

Es el único tipo que impide la simulación. Hay nudos con demanda que no tienen ningún camino hasta un Tank o Reservoir.

**Causas frecuentes:**
- Falta una tubería que debería enlazar este sector con la red principal.
- Hay una válvula cerrada entre este sector y la fuente (correcto operacionalmente, pero hay que modelarlo así a propósito).
- Error topológico: la tubería de conexión existe visualmente pero hay una rotura de conectividad — se detecta con **Check connectivity**.

La capa `HydraulicSectors_IsolatedDemands` muestra exactamente qué nudos y acometidas tienen demanda sin fuente, facilitando la localización del problema.

### nH-nQ — Pasivo

Fragmentos desconectados sin consumo. Suelen ser restos de importación o ramales de proyecto incompletos. No causan error de simulación, pero ensucian el modelo. Si no son parte del diseño, elimínalos con **Delete elements** o con la opción **Delete isolated subzones** de **Check connectivity**.

---

## Flujo de trabajo recomendado

Antes de simular por primera vez, o tras importar una red nueva:

1. **Check && commit data** — asegura que la topología básica y los atributos son coherentes.
2. **Remove overlapping elements** — elimina nudos y tuberías duplicadas que podrían generar sectores artificiales.
3. **Check connectivity** — identifica zonas aisladas visualmente y, si hay "basura" topológica, usa **Delete isolated subzones**.
4. **Check hydraulic sectors** — obtén la clasificación completa. Anota cuántos sectores nH-Q hay.
5. **Corregir los sectores nH-Q** — añade las tuberías o corrige los errores topológicos hasta que desaparezcan.
6. Vuelve a ejecutar **Check hydraulic sectors** — confirma que todos los sectores son H-Q, H-nQ o nH-nQ (ninguno nH-Q).

> Solo cuando no haya sectores **nH-Q** la simulación EPANET puede ejecutarse sin errores de convergencia.
