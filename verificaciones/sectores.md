# Sectores Hidráulicos

**Barra Debug → Check hydraulic sectors**

La herramienta de sectores hidráulicos analiza cómo está conectada cada parte de la red respecto a las fuentes de suministro (Reservoirs y Tanks) y a los puntos de consumo (Junctions con demanda). El resultado es una capa de coloración que clasifica cada tubería y nudo en uno de cuatro tipos.

![Mapa de sectores hidráulicos: zonas coloreadas por tipo A, B, C y D](../assets/images/debug/sectores-hidraulicos.png)
*Sectores hidráulicos: cada color corresponde a un tipo. Los sectores tipo C (sin fuente) aparecen en rojo.*

---

## Tipos de sector

| Tipo | Fuente | Demanda | Estado | Significado |
|------|--------|---------|--------|-------------|
| **A** | ✅ Sí | ✅ Sí | Funcional | El sector tiene fuente y consumidores. Puede simularse. |
| **B** | ✅ Sí | ❌ No | Latente | El sector tiene fuente pero ningún nudo con demanda asignada. Puede simularse pero no produce flujo. |
| **C** | ❌ No | ✅ Sí | **Aislado crítico** | Hay nudos con demanda pero ninguna fuente. El sector no puede abastecerse: EPANET lo rechazará con error de convergencia. |
| **D** | ❌ No | ❌ No | Pasivo | Sin fuente ni demanda. Hidráulicamente compatible (no requiere flujo), pero está desconectado. |

---

## Cómo interpretar el resultado

### Sector tipo A — Funcional

Es el estado deseable. Todo sector que vaya a simular debe ser tipo A. Si el proyecto tiene varios sectores tipo A independientes (por ejemplo, sectores de presión separados por válvulas cerradas), cada uno se puede simular por separado pero en el mismo modelo EPANET todos deben poder resolverse.

### Sector tipo B — Latente

Indica que existe una fuente conectada pero no hay demandas en esa zona. Puede ser:
- Una zona de la red aún sin datos de demanda asignados (pendiente de completar).
- Un ramal de reserva o bypass sin nudos de consumo (correcto).

En el primer caso, debes asignar demandas antes de simular para obtener resultados realistas.

### Sector tipo C — Aislado crítico

Es el error más grave. Significa que hay nudos con demanda que no tienen ningún camino conectado a un Reservoir o Tank. EPANET no puede calcular la presión en estos nudos y el modelo fallará.

**Causas frecuentes:**
- Tubería que debería conectar este sector a una fuente falta o está desconectada.
- Válvula cerrada que bloquea el único camino a la fuente (si es por diseño, puede ser correcto en algunas condiciones de operación).
- Error topológico: el nudo visualmente parece conectado pero hay una ruptura de conectividad (verifica con **Check connectivity**).

### Sector tipo D — Pasivo

Fragmentos sin fuente ni demanda. Habitualmente son restos de tuberías importadas sin datos o ramales de proyecto aún incompletos. No causan error en la simulación, pero pueden enmascarar problemas reales. Considera eliminarlos si no forman parte del modelo definitivo.

---

## Flujo de trabajo recomendado

1. Ejecuta **Check && commit data** para asegurar que la topología básica es correcta.
2. Ejecuta **Check connectivity** para identificar zonas aisladas.
3. Ejecuta **Check hydraulic sectors** para clasificar las zonas.
4. Corrige todos los sectores tipo C antes de simular.
5. Decide si los sectores tipo D son intencionados o deben eliminarse.
6. Vuelve a ejecutar **Check hydraulic sectors** para confirmar que el modelo queda en estado correcto.

> La herramienta genera una capa auxiliar `HydraulicSectors` que se añade al grupo de capas del proyecto. Esta capa es informativa y no forma parte del modelo EPANET exportado.
