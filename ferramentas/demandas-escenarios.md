# Demandas e Cenários

As três ferramentas do segundo grupo da barra de ferramentas gerenciam a atribuição de demanda em massa, cenários de simulação e identificação de segmentos de isolamento operacional.

---

## Construtor de demanda nodal…

**Barra de ferramentas → Construtor de demanda nodal…**

Atribua o consumo aos nós da rede em massa a partir de camadas externas do SHP carregadas no QGIS. É a principal ferramenta para integração de dados de faturação, censos de utilizadores ou estimativas de polígonos no modelo EPANET.

<figure><img src="../assets/images/herramientas/demand-builder.png" alt="Diálogo do construtor de demanda nodal com opções de método de origem e atribuição"><figcaption><p>Diálogo do construtor de demanda nodal com opções de método de origem e atribuição</p></figcaption></figure>
*Construtor de demanda nodal: camadas de origem detectadas automaticamente, configuração de campo e método de distribuição.*

### Fontes de dados suportadas

| Tipo de geometria | Método de atribuição |
|-------------------|----------------------|
| **Pontos** | Cada ponto é atribuído ao nó mais próximo. O valor da demanda é lido em um campo configurável na camada. |
| **Polígonos** | A demanda total do polígono é distribuída entre todos os nós que se enquadram nele. |
| **Linhas** | A demanda de cada seção é distribuída entre os nós mais próximos ao longo do eixo. |

### Processo

1. Carregue a camada externa do SHP com os dados de consumo no QGIS antes de abrir o gerenciador.
2. Ative o **Criador de demanda nodal**. A caixa de diálogo detecta e lista automaticamente as camadas externas.
3. Defina para cada camada:
- **Campo demanda**: coluna com o valor do consumo.
- **Campo categoria**: para criar múltiplas solicitações por tipo de usuário (residencial, industrial, etc.).
- **Campo padrão**: ID do padrão de demanda a ser aplicado (opcional).
4. Opcionalmente, selecione nós no mapa para limitar a atribuição a essa área.
5. Confirme. QGISRed grava os valores em `Junctions` ou `{Red}_MultipleDemands.shp` se houver categorias.

### Restrição a candidatos selecionados

A caixa de diálogo oferece duas opções de restrição que podem ser combinadas:

| Opção | Efeito |
|--------|--------|
| **Restringir candidatos de demanda a selecionados** | Apenas **nós (junções) atualmente selecionados** no mapa são considerados candidatos para receber demanda. Os outros nós são ignorados mesmo que estejam dentro da zona de influência de um ponto de consumo. |
| **Restringir candidatos de conexão de serviço aos selecionados** | Somente conexões de serviço atualmente selecionadas no mapa são consideradas pontos de serviço candidatos. Útil para realocar a demanda para conexões específicas sem afetar o restante. |

Ambas as opções são independentes e podem ser ativadas simultaneamente.

### Unidades de demanda personalizadas

Por padrão, o Builder interpreta os valores de demanda nas unidades de fluxo do projeto. Se seus dados de origem usarem unidades diferentes, ative **Unidades de demanda personalizadas** e insira:

- **Etiqueta das unidades**: etiqueta descritiva das unidades de origem (por exemplo, `m³/mes`).
- **Fator de conversão**: fator multiplicador para converter para unidades do projeto (ex.: se o projeto utilizar L/s e os dados vierem em m³/mês: `1000 / 86400 / 30 ≈ 0.000386`).

O Builder aplica automaticamente o fator a todos os valores de consumo antes de atribuí-los aos nós.

### Resultado no mapa

A camada resultante é exibida com cores por categoria e rótulos com o valor da demanda. Os nós sem categoria atribuída aparecem em laranja no grupo **Sem categoria**.

> 💡 As camadas auxiliares do Demand Builder (ConsumptionPoints, DemandLinks, Sectors...) também podem ser criadas vazias a partir do Layer Manager, sem a necessidade de primeiro executar uma análise (ver [Visão geral e gerenciamento de camadas](../projeto-ativo/capas-y-leyenda.md)).

### Limpeza de ações judiciais

O gerenciador permite excluir demandas existentes antes de atribuir novas:
- **Excluir demandas de nós selecionados**: elimina valores de `Demand` e entradas de `MultipleDemands`.
- **Excluir padrões órfãos**: exclui padrões que não são mais referenciados por nenhum nó.

### Atribuição de demanda da camada de segmento

Quando uma camada de segmento (geometria de linha) é utilizada para distribuir demandas utilizando o campo `%Dem`, os registros sem esse campo preenchido recebem automaticamente o percentual restante até 100%, distribuído proporcionalmente entre eles.

### Padrões por setores

A seção de padrões setoriais permite atribuir um padrão de demanda a cada setor da rede. Possui **dois modos exclusivos**:

| Modo | Descrição |
|------|-------------|
| **Importar padrões de um tema setorial** | Selecione a camada poligonal com os setores em uma combinação suspensa que lista as camadas poligonais já carregadas no QGIS (ou importe-a com o botão `...` se ainda não estiver carregada). Em seguida, escolha os campos **Sector Id (opcional)**, **Id demand pattern** e **Priority (optional)** dos combos correspondentes. O campo Sector Id é opcional: caso não seja identificado, o QGISRed gera identificadores internos automaticamente. Opcionalmente, salve o resultado como uma camada interna do projeto com o botão **Importar e salvar**. Depois de salva, esta opção fica bloqueada. |
| **Use padrões de um tema do setor de projeto** | Selecione uma camada de fatia já carregada no projeto. É exibida uma lista com os setores e, ao lado de cada um, um combo **editável** para escolher o padrão: você pode selecionar um padrão existente na lista ou escrever diretamente o Id de um novo padrão. Nós sem setor são agrupados em um setor extra. |

### Eficiência por setores

A seção de eficiência hidráulica por setores também apresenta **duas modalidades exclusivas**:

| Modo | Descrição |
|------|-------------|
| **Importar eficiências de um tema setorial** | Selecione a camada poligonal com os setores em uma combinação suspensa que lista as camadas poligonais já carregadas no QGIS (ou importe-a com o botão `...`) e escolha os campos **Sector Id (opcional)**, **Efficiency** e **Priority (opcional)**. O campo ID do setor é opcional. Opcionalmente, salve o resultado como uma camada interna do projeto com o botão **Importar e salvar**. Depois de salvo, a opção de importação é bloqueada. |
| **Usar eficiências de um tema do setor de projeto** | Selecione uma camada de fatia existente; O plugin identifica automaticamente os campos de eficiência. |

#### Eficiência e correções de padrões

Após definir as eficiências por setores, o gestor oferece opções adicionais de correção:

- **Corrigir eficiências de categoria para atender à eficiência do setor**: ajusta proporcionalmente as eficiências de cada categoria de demanda para que a eficiência resultante em cada setor corresponda ao objetivo declarado. Exclusivo com correção para eficiência global.
- **Corrigir padrões setoriais para atender ao padrão global**: após atribuir padrões setoriais, corrija esses padrões para que sua combinação esteja de acordo com o padrão global declarado anteriormente. As opções de correção são divididas por escopo do padrão (global ou categoria).

### Camada de conexões isoladas com demanda

Ao executar a análise de segmentos isolados ou setores hidráulicos, o plugin gera uma camada adicional com **conexões que possuem demanda atribuída mas pertencem a setores hidráulicos isolados** (sem oferta). Esta camada é representada por marcadores circulares contornados em vermelho e inclui os campos `Id`, `BaseDemand` e `Category`.

---

## Construtor de cenário…

**Barra de ferramentas → Construtor de cenário…**

Exporte e importe parâmetros do modelo em massa, criando “instantâneos” do estado da rede que podem ser restaurados a qualquer momento. É a ferramenta para gerenciar variantes de modelos sem duplicar projetos.

### Parâmetros gerenciados

| Parâmetro | Descrição |
|-----------|-------------|
| **Roughness** | Coeficientes de rugosidade de todos os tubos |
| **InitStatus** | Estados abertos/fechados de tubos e válvulas |
| **Demands** | Demandas básicas de todos os nós |
| **InitQuality** | Qualidades iniciais de nós e tubulações |
| **Elevations** | Níveis de nós, tanques e reservatórios |

### Fluxo de trabalho típico

1. Construa o modelo no estado atual (ano base).
2. Exporte o cenário base com **Construtor de cenários → Exportar**.
3. Modificar o modelo para o horizonte futuro (novas demandas, tubulações antigas, etc.).
4. Exporte o cenário futuro com outro nome.
5. Para comparar ou restaurar, use **Construtor de cenários → Importar** e selecione o cenário desejado.

Os arquivos do cenário são salvos como CSV na pasta do projeto.

---

## Segmentos isolados…

**Barra de ferramentas → Segmentos isolados…**

Responde à questão operacional: **"Quais válvulas devo fechar para reparar esta tubulação e quais usuários ficarão sem atendimento?"**

<figure><img src="../assets/images/herramientas/isolated-segments.png" alt="Resultado de segmentos isolados: tubulação afetada, válvulas de corte e zona sem serviço"><figcaption><p>Resultado de segmentos isolados: tubulação afetada, válvulas de corte e zona sem serviço</p></figcaption></figure>
*Em vermelho a tubulação a ser reparada, em amarelo as válvulas a fechar e em azul a área sem atendimento.*

### Processo

1. Ative a ferramenta e clique no tubo a ser reparado ou isolado.
2. O QGISRed calcula o **segmento mínimo** que seria isolado ao fechar as válvulas manuais mais próximas e identifica as colaterais afetadas.
3. O resultado é exibido no mapa:
- **Tubo alvo**: em vermelho.
- **Válvulas para fechar**: em amarelo.
- **Zona sem atendimento** (afetados colaterais): em azul.
4. Você pode clicar em mais pipes na mesma sessão para acumular a análise.

A camada auxiliar `IsolatedSegments` é gerada com todas as informações. Não modifica o modelo.
