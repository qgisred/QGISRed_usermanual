# Setores e Árvore de Demanda

As duas últimas ferramentas da barra Ferramentas realizam análises topológicas da rede: setorização por medidores de vazão e cálculo da árvore de custo mínimo a partir de um nó de origem.

---

## Obter setores de demanda

**Barra de Ferramentas → Obter setores de demanda**

Gera uma setorização da rede com base na presença de **medidores de vazão** (medidores de vazão). Cada setor de demanda é a sub-rede atendida por um único medidor de vazão, sem cruzar outros medidores de vazão.

### Diferença com setores hidráulicos

| | Setores hidráulicos (barra de depuração) | Setores de demanda (Barra Tools) |
|-|-------------------------------------|-----------------------------------|
| **Base** | Presença de Tanque ou Reservatório | Presença de medidores de vazão |
| **Pergunta** | De onde vem a água? | O que cada medidor de vazão mede? |
| **Classificação** | H-Q / H-nQ / nH-Q / nH-nQ | Nenhum tipo, apenas colorido por setor |
| **Usar** | Diagnóstico antes da simulação | Balanço hídrico por setor |

### Resultado

A ferramenta gera a camada `DemandSectors` no mapa, com cada setor em uma cor diferente. Se a rede não tiver medidores de vazão carregados, o resultado será um único setor que abrange toda a rede.

Nenhuma configuração necessária: inicia diretamente sem diálogo.

---

## Árvore de Custo Mínimo…

**Barra de Ferramentas → Árvore de Custo Mínimo…**

Calcula a **árvore geradora de custo mínimo** da rede a partir de um nó selecionado. Mostra o caminho hidraulicamente mais eficiente (menor resistência cumulativa) desse nó até todos os outros pontos acessíveis na rede.

### Processo

1. Ative a ferramenta.
2. Clique no nó de origem (por exemplo, uma fonte de abastecimento ou um ponto de abastecimento de água em alta).
3. O QGISRed calcula a árvore e gera a camada `Tree` no mapa, com a distância acumulada da origem rotulada em cada trecho.

### Interpretação do resultado

A árvore resultante mostra qual caminho a água seguiria a partir do nó fonte se a rede fosse puramente ramificada (sem loops). É útil para:

- Identifique tubos que funcionam sempre em uma única direção de fluxo.
- Detectar pipes redundantes na topologia (eles não aparecem na árvore porque existe um caminho mais curto).
- Analisar a estrutura de abastecimento em situação de emergência com parte da rede fechada.
- Planejar esquemas de setorização de pressão.

### ID do nó raiz

Na camada de nós gerada pela árvore, o nó de origem (raiz) é identificado com o valor **"ROOT"** no campo `NodeType`. Os restantes nós têm o seu tipo EPANET habitual (Junção, Tanque, Reservatório...). Isto permite criar regras de simbologia específicas para o nó raiz diretamente no QGIS.
