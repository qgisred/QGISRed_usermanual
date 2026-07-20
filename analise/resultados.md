# Visualizador de resultados

Assim que a simulação for concluída, o QGISRed oferece duas ferramentas complementares para explorar os resultados: o encaixe Resultados, que controla a exibição no mapa, e o encaixe Série temporal, que mostra a evolução de qualquer variável ao longo do tempo para elementos individuais.

---

## Base de resultados

O encaixe Resultados está ancorado na área direita da tela. Contém **três guias**:

- **Resultados**: visualização interativa no mapa com seleção de variáveis, navegação temporal e opções de mapa.
- **Relatório**: relatório de texto do motor EPANET.
- **Aparência**: configuração completa da aparência visual dos resultados no mapa.

<figure><img src="../assets/images/analisis/results-dock.png" alt="Painel de resultados com seletor de variáveis ​​e barra de tempo"><figcaption><p>Painel de resultados com seletor de variáveis ​​e barra de tempo</p></figcaption></figure>
*Dock de resultados: seleção de variáveis, modo estatístico e navegação por instantes de tempo.*

---

### Guia Resultados

#### Grupo de Tempo

Exibe o instante da hora atual no formato `HH:MM:SS` (ou no formato am/pm se ativo). Inclui botões para alternar entre o formato civil e o formato de tempo decorrido.

Quando um modo estatístico está ativo (Máximo, Mínimo...), a área de tempo mostra o nome e a descrição da estatística em vez do relógio.

#### Navegação temporal (controles de tempo)

| Controle | Descrição |
|---------|-------------|
| **Controle deslizante de tempo** | Percorra os momentos do relatório. |
| **Combo de momentos** (`cbTimes`) | Lista suspensa com todos os momentos disponíveis. |
| **Botões avançar/retroceder** | Próximo, anterior, início, fim. |
| **Reproduzir / Reproduzir para trás** | Animação automática para frente ou para trás. |
| **Controle deslizante de velocidade** | Controla a velocidade da animação (1–10). |
| **Circuito** | Repita a animação em loop. |

#### Tempos e estatísticas relatados

Dois combos localizados sob os controles de tempo:

| Combinação | Descrição |
|-------|-------------|
| **Tempos relatados** (`cbResultTimes`) | Filtre quais momentos são mostrados: Período único, Tempos de etapa ou Todos os tempos de cálculo. |
| **Estatísticas** (`cbStatistics`) | Aplica uma estatística em todos os períodos: Máximo, Mínimo, Faixa, Média, StdDev, Aviso. Quando ativo, o relógio é substituído pelo nome da estatística. |

> 💡 Nos modos **Máximo** e **Mínimo**, os rótulos do mapa mostram o valor junto com o horário de ocorrência no formato `valor (@ HH:MM:SS)`. Quando você coloca o cursor sobre um elemento do mapa, a dica de ferramenta inclui uma linha adicional `@ HH:MM:SS` com o momento exato em que ocorreu aquele máximo ou mínimo.

#### Grupo de Mapeamento — Nós

| Controle | Descrição |
|---------|-------------|
| **Nós de combinação** (`cbNodes`) | Propriedade a ser exibida nos nós: Pressão, Carga, Demanda, Qualidade. |
| **Mostrar rótulos de nós** | Exibe rótulos com o ID e o valor em cada nó no mapa. |
| **Mostrar histograma de nós** | Abre um histograma integrado no dock com a distribuição do valor atual em nós. |
| **Mostrar evolução do nó** | Abre um minigráfico integrado com a evolução temporal do nó selecionado no mapa. |

> 💡 Quando uma variável é selecionada no combo **Nodes**, um rótulo aparece próximo ao cabeçalho do grupo com o nome da variável em negrito e sua unidade entre parênteses (por exemplo, **Pressão** (m)).

#### Grupo de Mapeamento — Links

| Controle | Descrição |
|---------|-------------|
| **Links combinados** (`cbLinks`) | Propriedade a ser exibida em tubulações/válvulas/bombas: Fluxo, Velocidade, HeadLoss, UnitHdLoss, FricFactor, Status, ReactRate, Quality. |
| **Mostrar rótulos de link** | Exibe rótulos com o ID e o valor em cada tubo. |
| **Mostrar direções de fluxo** | Adicione setas de direção de fluxo nas tubulações. |
| **Mostrar histograma de links** | Histograma integrado ao dock com distribuição do valor atual em pipelines. |
| **Mostrar evolução do link** | Minigráfico integrado com a evolução temporal do pipeline selecionado no mapa. |

> 💡 Da mesma forma, quando uma variável é selecionada no combo **Links**, um rótulo aparece próximo ao cabeçalho do grupo com o nome da variável em negrito e sua unidade entre parênteses (por exemplo, **Velocidade** (m/s)).

> O botão **Aparência** (ícone no cabeçalho do grupo Nós) leva você diretamente para a aba Aparência sem precisar navegar pelas abas.

---

### Guia Relatório

Exibe o relatório de texto gerado pelo motor EPANET após a conclusão da simulação. Inclui:

- Balanço geral de massa da rede.
- Lista de nós com pressão negativa ou fora de faixa.
- Avisos de bombas operando fora de sua curva.
- Estado de convergência do cálculo hidráulico em cada etapa.
- Resumo das reações de qualidade (caso a qualidade tenha sido simulada).
- Em caso de erro, o conteúdo completo do relatório é exibido automaticamente aqui.

> O relatório de status é o primeiro lugar a ser consultado quando uma simulação produz resultados inesperados ou não converge.

---

### Aba Aparência

Concentra todas as opções de apresentação visual dos resultados no mapa. As configurações são salvas automaticamente em `{Red}_Results_Config.cfg` na pasta `Results/` do projeto e restauradas na próxima sessão.

> 💡 Cada controle numérico na aba Aparência possui um pequeno botão ↺ individual que restaura apenas aquele campo ao seu valor padrão, sem afetar o restante das configurações.

> ⚠️ Os controles do grupo **Nodes** são desativados automaticamente quando o combo Nodes é definido como "None", e o mesmo se aplica a **Links**. Além disso, o controle **Decimais** é desabilitado quando a variável ativa é **Status** (variável categórica sem decimais aplicáveis).

#### Etiquetas do mapa

| Opção | Descrição |
|--------|-------------|
| **Tamanho da fonte (pt)** | Tamanho da fonte dos rótulos no mapa (6–24 pt, padrão 8). |
| **Decimais de nós/links** | Número de decimais exibidos nos rótulos dos nós e tubulações, respectivamente (0–6). O controle é rotulado com o nome da variável atualmente ativa. |
| **Cor do texto** | Cor padrão: Nós **#333333** (cinza escuro), tubulação **#0A143C** (azul marinho). **Preto**: texto sempre preto. **Por intervalo**: A cor do texto segue a paleta do intervalo de valores ativo. Quando “Mostrar ID ao lado do valor” está ativo, a linha Id usa a cor do próprio elemento e a linha de valor usa a cor do símbolo ou intervalo. |
| **Antecedentes** | Cor de fundo atrás dos rótulos do mapa. Inclui um seletor de cores e um botão de exclusão para remover o fundo. |
| **Mostrar ID ao lado do valor** | Adicione o ID do elemento à primeira linha do rótulo. |

#### Simbologia

| Opção | Descrição |
|--------|-------------|
| **Ocultar borda nos cruzamentos** | Oculta a borda/contorno dos marcadores de junção. Ativar esta opção remove o contorno ao redor do símbolo do nó. |
| **Proporcional ao valor** | Dimensiona o tamanho dos nós e a espessura dos tubos linearmente com o valor representado. Não se aplica ao campo Status. |
| **Fator de nós** | Fator de escala base do tamanho do marcador de nó (0,25–4,0, padrão 1,0). |
| **Fator de links** | Fator de escala base da espessura do tubo (0,25–4,0, padrão 1,0). |
| **Fator de setas** | Fator de escala das setas de direção do fluxo (0,25–4,0, padrão 1,0). |

#### Plano de fundo do mapa

Permite definir uma cor de fundo sólida para a tela do mapa durante a visualização dos resultados. A cor é restaurada ao original quando o encaixe é fechado. O botão ****** remove a cor de fundo.

#### Redefinir tudo

Retorna todos os parâmetros da guia Aparência aos seus valores padrão.

---

### Cenários

O dock oferece suporte a vários cenários de resultados. Cada cenário é identificado por um nome (por padrão `Base`) e é armazenado como arquivos `.out` / `.hyd` na subpasta `Results/` do projeto. O nome do cenário ativo aparece no título do painel.

---

### Propriedades disponíveis

**Nós** (Junções, Tanques, Reservatórios):

| Propriedade | Descrição |
|-----------|-------------|
| `Pressure` | Pressão em m.c.a. |
| `Head` | Altura piezométrica em m |
| `Demand` | Demanda calculada |
| `Quality` | Qualidade da água (dependendo do tipo configurado nas opções de Análise) |

**Tubos, válvulas e bombas** (Links):

| Propriedade | Descrição |
|-----------|-------------|
| `Flow` | Caudal (com sinal ou sem sinal) |
| `Velocity` | Velocidade em m/s |
| `HeadLoss` | Perda de carga em m |
| `UnitHdLoss` | Perda unitária em m/km |
| `FricFactor` | Fator de atrito |
| `Status` | Status operacional (Aberto/Ativo/Fechado) |
| `ReactRate` | Taxa de reação (modelos de qualidade) |
| `Quality` | Qualidade da água |

> 💡 Os rótulos do mapa para a variável **Fluxo** sempre mostram o valor absoluto (sem sinal negativo), mesmo nos modos de estatística Máximo e Mínimo. A direção do fluxo é indicada pelas setas de direção e não pelo sinal de valor.

---

## Série temporal (Série temporal…)

**Barra de análise → Série temporal…**

Ativa uma ferramenta de seleção interativa que traça a evolução temporal de qualquer propriedade de resultado para um ou mais elementos da rede.

<figure><img src="../assets/images/analisis/time-series-dock.png" alt="Série temporal do painel com curvas de pressão multinó"><figcaption><p>Série temporal do painel com curvas de pressão multinó</p></figcaption></figure>
*Série temporal do painel: evolução temporal da pressão em vários nós selecionados simultaneamente.*

### Processo

1. Ative **Série temporal** (botão verificável). O painel Série temporal é aberto na parte inferior da tela.
2. Clique em qualquer elemento do mapa (nó, tubulação, válvula, bomba, tanque, reservatório).
3. O painel desenha a curva de tempo da propriedade ativa no encaixe Resultados para esse elemento.
4. O item fica destacado em azul no mapa.

### Seleção múltipla

- **Shift + clique** em outro elemento: adiciona sua curva ao gráfico sem excluir as anteriores. Cada curva recebe uma cor diferente da paleta.
- **Shift + clique** em um elemento já selecionado: remove-o do gráfico.
- **Clique sem Shift** com mais de uma curva ativa: pede confirmação antes de limpar a seleção.

### Seleção de Propriedade

- Por padrão, a propriedade ativa é representada na doca Resultados para o tipo de elemento clicado.
- **Clique com o botão direito** em um elemento: abre um menu de contexto para escolher quaisquer outras propriedades disponíveis para esse elemento sem alterar a visualização de encaixe Resultados.

### Propriedades adicionais para buckets

Para o tipo de elemento **Tank**, duas quantidades adicionais estão disponíveis:

| Magnitude | Descrição |
|----------|-------------|
| **Volume** | Volume armazenado em m³ (ou ft³ dependendo das unidades do projeto), calculado a partir dos binários de saída do EPANET. |
| **Derramamento de tanque** | Fluxo de transbordamento. Só é diferente de zero se o repositório tiver a opção de overflow do EPANET habilitada. |

### Variáveis ​​globais de rede

Além de elementos individuais, o painel Série temporal permite adicionar **séries globais** que agregam valores em toda a rede. Estas séries não requerem clique no mapa: elas são adicionadas a partir do menu de seleção de variáveis ​​do gráfico.

| Variável global | Descrição |
|-----------------|-------------|
| **Fornecimento total de água** | Vazão total fornecida por todos os reservatórios e fontes da rede. |
| **Demanda total de água** | Demanda total consumida por todos os nós da rede. |
| **AverageNodePressure** | Pressão média de todos os nós (excluindo tanques e reservatórios). |
| **TotalVolume Armazenado** | Volume total armazenado somando todos os depósitos da rede. |
| **TotalTankSpill** | Vazão total somando todos os tanques da rede. |

### Configuração da curva

No painel Série temporal você pode ajustar cada curva:

- Nome na legenda.
- Cor, estilo de linha (sólida, tracejada, pontilhada) e espessura.
- Marcadores: símbolo, tamanho, cor, espaço.
- Mostrar valores em cada ponto da curva.
- Visibilidade (mostrar/ocultar sem excluir).

### Tabela de valores

A tabela de valores exibe os dados numéricos de todas as curvas ativas. A **primeira coluna** (instante de tempo) é **fixa**: ela não desaparece ao rolar a tabela horizontalmente quando há muitas curvas. Isso torna mais fácil identificar onde cada linha está sem ter que voltar ao início.

### Sincronização com a tabela de valores

Ao mover o cursor sobre o gráfico, a linha correspondente da tabela de ações é automaticamente destacada em tempo real.

### Copiar tabela para a área de transferência

A função copy gera **duas linhas de cabeçalho**: a primeira com o nome do elemento ou magnitude e a segunda com a unidade. Facilita a colagem direta em planilhas.

### Exportar e importar configurações do gráfico

Os botões **Exportar configuração do gráfico** e **Importar configuração do gráfico** salvam e recuperam a configuração completa de curvas, eixos e estilos em um arquivo `.cfg`. Também é possível exportar a configuração geral do template (eixos, estilos) mesmo que não haja curvas carregadas, e aplicá-la na importação em um novo gráfico.

### Múltiplas janelas de gráfico

O botão **Nova janela de gráfico** abre uma nova janela independente de Série Temporal. Cada janela possui seu próprio contexto de curva, propriedade e elementos selecionados. Você pode manter várias janelas abertas simultaneamente para comparar diferentes variáveis ​​ou áreas da rede.

### Sincronização do formato de hora

A coluna “Hora do dia” na tabela de valores usa automaticamente o mesmo formato (24h ou am/pm) do painel Resultados.

### Fechamento

Ao desligar o botão **Série temporal** ou fechar o painel, o destaque desaparece e o cursor retorna ao modo de navegação padrão.
