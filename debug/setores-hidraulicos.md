# Setores Hidráulicos

**Barra de depuração → Verifique os setores hidráulicos**

A ferramenta de setores hidráulicos varre a rede usando um algoritmo BFS (pesquisa em largura) de todas as fontes de abastecimento e classifica cada sub-rede conectada de acordo com se possui ou não uma fonte hidráulica (H) e se tem ou não demanda (Q). O resultado é despejado em camadas SHP e em um relatório CSV.

<figure><img src="../assets/images/debug/sectores-hidraulicos.png" alt="Mapa dos setores hidráulicos: áreas coloridas por tipo H-Q, H-nQ, nH-Q e nH-nQ"><figcaption><p>Mapa dos setores hidráulicos: áreas coloridas por tipo H-Q, H-nQ, nH-Q e nH-nQ</p></figcaption></figure>
*Setores hidráulicos: cada cor representa um tipo de classificação. Os setores nH-Q (sem fonte com demanda) aparecem em vermelho.*

---

## Classificação do setor

A ferramenta atribui a cada setor um destes quatro tipos. Estas são as **tags reais** que aparecem na camada SHP e no relatório CSV:

| Etiqueta | Fonte (H) | Demanda (Q) | Significado |
|----------|-----------|-------------|-------------|
| **H-Q** | ✅ Sim | ✅ Sim | Setor funcional: possui fonte de oferta e nós com demanda. Pode ser simulado corretamente. |
| **H-nQ** | ✅ Sim | ❌Não | Setor latente: possui fonte mas não possui nós com demanda > 0. Pode ser simulado mas sem fluxo real. |
| **nH-Q** | ❌Não | ✅ Sim | **Setor crítico**: nós com demanda mas sem fonte conectada. O EPANET não convergirá. |
| **nH-nQ** | ❌Não | ❌ Não | Setor passivo: nem fonte nem demanda. Não causa erro na simulação mas está desconectado. |

> **H** = presença de pelo menos um RNV ou RNF no setor.
> **Q** = presença de pelo menos um entroncamento com demanda base > 0.
> **n** = negação (ausência dessa condição).

Há também um pseudosetor especial chamado **ClosedLinks** que agrupa pipes com status `Closed` que estão fora de qualquer setor conectado. Não conta no número total de setores do relatório.

---

## Resultados gerados

A ferramenta produz três saídas que são adicionadas automaticamente ao projeto:

| Saída | Tipo | Conteúdo |
|--------|------|-----------|
| `HydraulicSectors` | Camada PCH | Geometria de todos os elementos coloridos por tipo de setor |
| `HydraulicSectors_IsolatedDemands` | Camada PCH | Nós e conexões do tipo **nH-Q** com demanda isolada |
| `{Red}_HydraulicSectors_Report.csv` | CSV | Tabela com ID do setor, número de elementos e classificação |

O CSV tem o formato:
```
SectorID; NumElements; Classification
S1; 1 243; H-Q
S2; 47; H-nQ
S3; 12; nH-Q
S4; 3; nH-nQ
```

---

## Como interpretar cada tipo

### HQ – Funcional

Estado correto. Cada setor que será simulado deve ser H-Q. Uma rede adequadamente construída terá um único grande setor H-Q (ou vários se houver setorização hidráulica real com válvulas fechadas entre eles).

### H-nQ — Latente

Existe uma fonte conectada, mas todos os nós desse setor têm demanda = 0. Causas comuns:

- Zona de rede importada sem dados de demanda atribuídos ainda.
- Bypass ou reserva de ramal sem consumidores (pode estar correto por design).

No primeiro caso, as demandas devem ser atribuídas antes que a simulação seja realista.

### nH-Q — Crítico (o mais importante para corrigir)

É o único tipo que impede a simulação. Existem nós com demanda que não possuem nenhum caminho para um RNV ou RNF.

**Causas frequentes:**
- Falta uma conduta que deveria ligar este sector à rede principal.
- Existe uma válvula fechada entre este setor e a fonte (operacionalmente correto, mas deve ser modelada desta forma propositalmente).
- Erro topológico: o tubo de conexão existe visualmente, mas há uma quebra de conectividade — detectada com **Verificar conectividade**.

A camada `HydraulicSectors_IsolatedDemands` mostra exatamente quais nós e conexões possuem demanda sem fonte, facilitando a localização do problema.

### nH-nQ — Passivo

Fragmentos desconectados sem consumo. Geralmente são restos importados ou ramificações incompletas do projeto. Eles não causam erro de simulação, mas sujam o modelo. Se eles não fizerem parte do layout, exclua-os com **Excluir elementos** ou a opção **Excluir subzonas isoladas** de **Verificar conectividade**.

---

## Fluxo de trabalho recomendado

Antes de simular pela primeira vez ou após importar uma nova rede:

1. **Verificar e confirmar dados** — garante que a topologia e os atributos básicos sejam consistentes.
2. **Remover elementos sobrepostos** — elimina nós e tubos duplicados que poderiam gerar setores artificiais.
3. **Verificar conectividade** — identifica zonas isoladas visualmente e, se houver "lixo" topológico, usa **Excluir subzonas isoladas**.
4. **Verifique os setores hidráulicos** — obtenha a classificação completa. Anote quantos setores nH-Q existem.
5. **Corrigir setores nH-Q** — adicionar tubos ou corrigir erros topológicos até que desapareçam.
6. Execute novamente **Verifique os setores hidráulicos** — confirme se todos os setores são H-Q, H-nQ ou nH-nQ (sem nH-Q).

> Somente quando não há setores **nH-Q** a simulação EPANET pode ser executada sem erros de convergência.
