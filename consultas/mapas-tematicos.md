# Mapas Temáticos

**Barra de Consultas → Mapas temáticos…**

Abre a caixa de diálogo **Mapas Temáticos**, que gera camadas que colorem tubulações e nós por intervalos de um atributo hidráulico. Ao contrário de outras caixas de diálogo QGISRed, você não precisa escolher um "campo e confirmar": cada atributo disponível tem sua própria caixa, e você pode marcar quantos quiser de uma vez - cada um gera sua própria camada, e todos eles vivem no mapa simultaneamente.

<!-- TODO: captura pendente — Diálogo de Mapas Temáticos com caixas de Tubos e Nós -->

---

## Elementos ativos: tubos e nós

Na versão atual, **Mapas Temáticos funcionam nas camadas de Tubulações e Junções**. As opções de outros tipos de elementos (válvulas, bombas, tanques, reservatórios) estão presentes na interface, mas ficam automaticamente ocultadas por ainda não estarem implementadas. Os grupos **Conexões de serviço**, **Válvulas de isolamento** e **Medidores** estão visíveis, mas sua única caixa de seleção ("Temporário") também não está operacional ainda - não marque.

---

## Processo

1. Abra **Mapas temáticos** na barra de consultas.
2. Marque as caixas dos atributos que deseja representar (você pode marcar vários pipes e nós ao mesmo tempo).
3. Pressione **Aceitar**. QGISRed cria uma camada para cada caixa marcada, dentro do grupo **Consultas → Mapas Temáticos** do painel de camadas do QGIS.
4. Para remover um mapa já gerado, reabra a caixa de diálogo, desmarque sua caixa e pressione **Aceitar** — QGISRed exclui aquela camada específica sem tocar no resto. As caixas nos mapas já gerados aparecem pré-marcadas.

> 💡 Você pode ter vários mapas temáticos abertos ao mesmo tempo (por exemplo, Material do tubo e Ano de instalação junto com a demanda base do nó) — cada um é uma camada separada, eles não se substituem como acontecia antes.

---

## Campos disponíveis para pipes

| Campo | Descrição |
|-------|-------------|
| `Diameter` | Diâmetro do tubo |
| `Length` | Comprimento |
| `Material` | Material do tubo, colorido com a paleta fixa do QGISRed (ver tabela abaixo) |
| `Roughness` | Coeficiente de rugosidade — classes e arquivo de estilo dependem da **fórmula de perda de pressão** ativa no projeto (Hazen-Williams, Colebrook-White ou Darcy-Weisbach) |
| `Age` | Idade, calculada a partir do ano de instalação; as classes são rotuladas com o sufixo "anos" |
| `Installation Year` | Ano de instalação |

> Os mapas **Idade** e **Ano de instalação** adicionam três colunas à tabela de atributos da camada: a data de instalação bruta (`InstalDate`), o ano extraído (`InstYear`) e a idade calculada (`Age`) — vê-los todos de uma vez é útil mesmo se você tiver marcado apenas um dos dois mapas.

---

## Campos disponíveis para nós

| Campo | Descrição |
|-------|-------------|
| `Elevation` | Nível do nó. As classes são calculadas automaticamente a partir dos valores reais do projeto (não há intervalos padrão) — a legenda mostra os cortes com a unidade de comprimento do projeto (por exemplo, "< 120 m", "120 < 180 m", ">= 180 m"). |
| `Total Base Demand` | Demanda base total do nó. Os círculos são **dimensionados proporcionalmente** à demanda (não lineares, para que valores muito grandes não dominem visualmente o mapa), em classes também calculadas a partir dos dados reais, rotuladas na unidade de fluxo ativo do projeto. Se o nó tiver múltiplas categorias de demanda (ver [Demandas e cenários](../ferramentas/demandas-e-cenarios.md)), a camada reflete a soma agregada; nós com demanda zero não são mostrados. |

---

## Paleta de materiais

O mapa **Material** colore cada tubo com base no valor de seu campo `Material`, comparando-o (sem distinção entre maiúsculas e minúsculas) com a abreviatura ou nome nesta tabela fixa — um material que não aparece aqui recebe uma cor aleatória:

| Abreviado | Materiais | Abreviado | Materiais |
|--------|----------|--------|----------|
| FG | Ferro Fundido Cinzento | Pb | Liderar |
| FD | Fundição Dúctil | PVC | Cloreto de polivinila |
| ÁS | Aço | EP | Polietileno |
| AÇO INOX | Aço Inoxidável | PVC-O | PVC Orientado |
| FC | Fibrocimento | PVC-R | PVC rígido |
| AGal | Aço Galvanizado | Cu | Cobre |
| HCCC | Concreto com revestimento em chapa | PE-AD | Polietileno de Alta Densidade |
| HSCC | Concreto sem revestimento de chapa | PE-BD | Polietileno de Baixa Densidade |
| HA | Concreto Armado | PE-MD | Polietileno de Média Densidade |
| HPr | Concreto protendido | PRFV | Poliéster Reforçado com Fibra de Vidro |

> Esta tabela de cores se aplica apenas ao estilo **padrão** que vem com o QGISRed. Se você salvar sua própria legenda de Material no editor de legendas (consulte [Visão geral e gerenciamento de camadas](../projeto-ativo/camadas-e-legenda.md)), suas cores terão precedência sobre esta paleta quando você regenerar o mapa.

---

## Aviso de mapa desatualizado

Se você alterar as **unidades**, **fórmula de perda de carga** ou **unidades de fluxo** após gerar um mapa temático que depende delas (Diâmetro, Comprimento, Rugosidade, Demanda Base...), o QGISRed marca essa camada com um ícone de aviso ⚠ no painel de camadas - o mesmo ícone que já usa para avisar sobre resultados de simulação desatualizados.

- Passe o mouse sobre o ícone para ver o motivo.
- Clique no ícone para reconstruir aquela camada com a configuração atual, sem precisar reabrir a caixa de diálogo.

---

## Resultado no mapa

Cada caixa marcada gera sua própria camada (por exemplo `Pipe Materials`, `Junction Elevations`) dentro do grupo **Consultas → Mapas Temáticos**. As camadas são somente leitura e se atualizam quando você edita o pipe ou nó de origem (não há necessidade de regenerar o mapa manualmente após uma alteração específica) — a legenda de cada uma também mostra quantos elementos cada classe possui.

Se você marcar e confirmar novamente uma caixa já gerada, o QGISRed substitui essa camada específica pela nova configuração, sem tocar no restante dos mapas ativos.

---

## Notas de uso

- A geração de mapas temáticos não modifica nenhum dado do modelo; apenas cria novas camadas com a simbologia correspondente.
- Para remover um mapa, desmarque-o na caixa de diálogo (veja "Processar" acima) ou exclua sua camada diretamente do painel de camadas do QGIS.
- O mapa **Demanda Base Total** requer a existência de nós com demanda atribuída; Caso o projeto não possua demandas carregadas, a camada é gerada vazia.
