# 🔧Ferramentas

A barra **Ferramentas** agrupa as massivas ferramentas de processamento: cálculo automático de propriedades hidráulicas, atribuição de demandas de fontes externas, gerenciamento de cenários e análise topológica. Ao contrário das ferramentas de edição, estas atuam em toda a rede ou em grandes seleções, não elemento por elemento.

<figure><img src="../assets/images/herramientas/barra-tools.png" alt="Barra de ferramentas QGISRed Tools"><figcaption><p>Barra de ferramentas QGISRed Tools</p></figcaption></figure>
*Barra de ferramentas: propriedades hidráulicas, demandas e cenários, análise topológica.*

---

## Ferramentas da barra Ferramentas

### Grupo 1 — Propriedades hidráulicas

| # | Ferramenta | Função |
|---|-------------|---------|
| 1 | **Calcular automaticamente comprimentos de tubos** | Recalcular o comprimento de cada tubo a partir da sua geometria |
| 2 | **Interpolar elevação de arquivos .asc…** | Atribuir alturas aos nós interpolando a partir de um MDT em formato ASC |
| 3 | **Definir coeficientes de rugosidade (a partir de Material e Data)** | Calcular a rugosidade atual de cada tubo devido ao envelhecimento |
| 4 | **Converter coeficientes de rugosidade…** | Converter rugosidade entre as fórmulas HW, DW e CM |

### Grupo 2 — Demandas e cenários

| # | Ferramenta | Função |
|---|-------------|---------|
| 5 | **Construtor de demanda nodal…** | Atribuir demandas aos nós das camadas externas do SHP (pontos ou polígonos) |
| 6 | **Construtor de cenário…** | Exporte e importe parâmetros de modelo em massa para gerenciar cenários |
| 7 | **Segmentos isolados…** | Identificar quais válvulas fechar para isolar um trecho e quais áreas ficam sem serviço |

### Grupo 3 — Análise topológica

| # | Ferramenta | Função |
|---|-------------|---------|
| 8 | **Obter setores de demanda** | Gera setores de demanda delimitados por medidores de vazão |
| 9 | **Árvore de Custo Mínimo…** | Calcular a árvore de custo mínimo de um nó selecionado |

---

## Nesta seção

* [Propriedades hidráulicas](propiedades-hidraulicas.md) — comprimentos, elevações, rugosidade de envelhecimento e conversão entre fórmulas
* [Demandas e cenários](demandas-escenarios.md) — atribuição massiva de demandas, gestão de cenários e segmentos isolados
* [Setores de demanda e árvore](sectores-arbol.md) — setorização por medidores de vazão e árvore de custo mínimo
