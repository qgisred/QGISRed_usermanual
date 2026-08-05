# Perfis Longitudinais

**Barra de análise → Perfil longitudinal…**

O perfil longitudinal mostra a evolução de uma variável hidráulica ao longo de um caminho definido interativamente sobre a rede. O eixo X representa a distância acumulada desde o nó inicial do percurso; no eixo Y, o valor da variável selecionada em cada nó do caminho. É possível abrir vários painéis de perfil simultaneamente, cada um com seu próprio caminho, variáveis ​​e configurações independentes.

> **Pré-requisito**: Uma simulação EPANET deve ter sido executada antes de abrir o perfil. Se nenhum resultado estiver disponível, o plugin exibe a mensagem _"Execute uma simulação primeiro para construir um perfil longitudinal."_

> 📝 O plugin detecta automaticamente se os resultados vêm do formato padrão EPANET ou do formato `.hyd` estendido QGISRed; nenhum ajuste manual é necessário.

<figure><img src="../assets/images/analisis/perfil-longitudinal-dock.png" alt="Doca de perfil longitudinal com rota desenhada no mapa e gráfico de pressão"><figcaption><p>Doca de perfil longitudinal com rota desenhada no mapa e gráfico de pressão</p></figcaption></figure>
*Perfil longitudinal: percurso destacado em vermelho no mapa (esquerda) e gráfico de altura piezométrica + elevação do terreno (direita).*
<!-- TODO: Captura obsoleta — os botões Selecionar/Adicionar nó/Remover nó/Mover nó/Ramificação na barra de ferramentas foram substituídos por um único botão Editar trajetos + botão Ajuda -->

---

## Múltiplas janelas de perfil

O plugin permite que você mantenha vários docks de perfil abertos ao mesmo tempo. Cada dock funciona de forma totalmente independente: possui seu próprio caminho, suas próprias variáveis ​​selecionadas e suas próprias configurações de gráfico.

- O botão **Novo Painel** na barra de ferramentas cria um encaixe adicional numerado sequencialmente (_Perfil 2_, _Perfil 3_, etc.).
- O painel ativo – aquele que recebe as interações do mapa – é visualmente diferenciado dos demais.
- Abrir o perfil no menu Análise reutiliza o primeiro painel se já estiver aberto; caso contrário, crie um novo.

---

## Abrir e construir perfil

1. Ative **Perfil longitudinal** na barra Análise. O encaixe do perfil é aberto na área inferior do QGIS.
2. O botão **Editar trajetos** é ativado automaticamente; o cursor muda para o ícone de lápis.
3. Clique em um nó da rede (Entroncamentos, RNVs, RNFs) para definir o primeiro nó de referência.
4. Clique em outro nó: o plugin calcula o **caminho topológico mínimo** entre os dois nós e desenha o perfil.
5. Cada clique adicional estende o caminho concatenando o caminho do último nó para o novo.
6. Clicar com o botão direito (sem nó em andamento) finaliza a rota de edição.

Se dois nós não estiverem conectados na rede, a mensagem _"O nó selecionado não está conectado ao anterior ao longo da rede."_

No mapa, uma **linha vermelha** é desenhada sobre os links do caminho e **marcadores azuis** quadrados são desenhados sobre os nós de referência.

---

## Variáveis ​​disponíveis

| Variável | Descrição |
|----------|-------------|
| **Elevação** | Elevação do terreno — estática, não depende do instante do tempo |
| **Cabeça + Dimensão** | Altura piezométrica e nível do solo juntos no mesmo gráfico |
| **Pressão** | Pressão em cada nó |
| **Qualidade** | Qualidade da água em cada nó; o seletor exibe o nome da qualidade específica do projeto (por exemplo, _Cloro_) em vez do termo genérico _Qualidade_ |
| **Perda de carga acumulada** | Perda de carga acumulada ao longo do percurso |

A variável padrão é **Cabeçalho + Dimensão**. Quando selecionado, o gráfico **simultaneamente** mostra a linha piezométrica (azul) e a elevação do terreno (marrom), permitindo ver rapidamente se existe pressão positiva em cada ponto ao longo da rota.

O gráfico é atualizado automaticamente quando o instante da hora muda no encaixe Resultados.

> 📝 Quando instantes de tempo estão disponíveis, o título do gráfico exibe **"Perfis longitudinais em HH:MM:SS"**. Para resultados estáticos, **"Perfis longitudinais"** aparece de forma simples.

> 📝 Os rótulos dos eixos incluem a unidade do projeto entre colchetes (por exemplo, _Head [m]_, _Pressure [bar]_, _Distance [m]_). Os cabeçalhos da tabela de valores também mostram as unidades.

### Eixo secundário

À direita do seletor de variável principal está o combo **2º eixo**. Permite sobrepor uma segunda variável no **eixo Y direito** do gráfico, com sua própria escala independente.

- As variáveis ​​disponíveis no eixo secundário dependem da seleção principal.
- A curva do eixo secundário pode ser excluída diretamente da legenda do gráfico.
- O eixo Y direito tem suas próprias configurações de escala e rótulo, acessíveis em **Opções do gráfico → Eixos** (consulte [Personalização do gráfico](#personalización-del-gráfico)).

---

## Barra de ferramentas do Dock

### Modos de edição de tour

Todas as ações de edição são controladas a partir de um único botão de alternância, em vez de um botão separado por ação:

| Botão | Função |
|-------|---------|
| **Editar trajetos** (ícone de lápis, alternável) | Ative o modo de edição: clique com o botão esquerdo para traçar a rota nó por nó, clique com o botão direito em um nó para ver suas opções (ver [Atalhos do mouse](#atajos-de-ratón)). Quando desativado, mover o mouse sobre o caminho apenas o destaca e exibe informações, sem modificá-las. |
| **Ajuda** (ícone ⓘ) | Abre a caixa de diálogo **"Como editar trajetos"**, com um resumo de todas as ações de edição e atalhos do mouse disponíveis. |

> 📝 Adicionar um nó de etapa intermediária, excluí-lo, movê-lo ou criar uma ramificação não possui mais botão próprio na barra de ferramentas: eles são feitos com **Editar trajetos** ativo, usando o menu de contexto (clique com o botão direito) ou os atalhos do mouse descritos em [Atalhos do mouse](#atajos-de-ratón). Essas ações funcionam da mesma forma na rota principal e nos ramais.

### Navegação no gráfico

| Botão | Função |
|-------|---------|
| **Janela de zoom** | Desenhe um retângulo no gráfico para ampliar o eixo X |
| **Pão** | Arraste o gráfico horizontalmente; exclusivo com janela Zoom |
| **Aumentar/Diminuir o zoom** | Aumenta ou diminui o zoom no eixo X |
| **Ajuste** | Restaura a visualização completa do perfil |

A roda do mouse também amplia centralizando a posição do cursor.

### Opções de exibição

| Botão | Função |
|-------|---------|
| **Etiquetas** | Exibe o valor numérico da variável em cada nó de referência |
| **Símbolos** | Mostra simbologia dos elementos (nó, RNV, RNF, bomba, válvula) e setas de direção do fluxo na curva |
| **Envelope** | Abre um submenu para ativar o envelope Mín/Máx da simulação (ver seção [Envelope](#envolvente-minmax)) |
| **Opções de gráfico** | Abra a caixa de diálogo de personalização do gráfico |

### Tabela e exportação

| Botão | Função |
|-------|---------|
| **Tabela** | Mostrar ou ocultar a tabela de valores à esquerda do gráfico |
| **Exportar CSV** | Exportar tabela de valores para CSV com separadores regionais |
| **Exportar imagem** | Salve o gráfico como PNG ou SVG |
| **Exportar configuração** | Salve as configurações atuais do perfil em um arquivo `.cfg` (consulte a seção [Configurações de importação e exportação](#importar-y-exportar-configuración)) |
| **Configurações de importação** | Carregue uma configuração de perfil salva anteriormente de um arquivo `.cfg` |
| **Novo painel** | Crie um encaixe de perfil adicional numerado sequencialmente |
| **Limpar** | Limpa toda a rota, ramificações e destaques do mapa |

---

## Envelope Mín/Máx

Disponível para **Cabeça + Dimensão**, **Pressão** e **Qualidade**. Mostra a faixa histórica de variação de toda a simulação sobreposta ao perfil do momento atual.

| Modo | Descrição |
|------|-------------|
| **Desligado** | Sem envelope |
| **Somente faixa sombreada** | Área sombreada em laranja entre os valores máximos e mínimos históricos |
| **Apenas linhas limite** | Duas linhas tracejadas laranja marcando o máximo e o mínimo |
| **Banda e linhas** | Ambos sobrepostos |

Quando o envelope está ativo, a tabela de valores adiciona colunas com valor máximo, tempo máximo, valor mínimo e tempo mínimo para cada nó.

---

## Filiais

A ação **Criar ramificação** permite adicionar ramificações laterais que compartilham o mesmo gráfico com o caminho principal.

1. Com **Editar trajetos** ativo, clique com o botão direito em um nó já pertencente ao caminho principal ou uma ramificação existente e escolha **Criar ramificação** no menu de contexto (ou clique duas vezes com o botão direito diretamente sobre ele se for um nó interior com grau de conexão maior que 2; veja [Atalhos do mouse](#atajos-de-ratón)). Esse nó define o ponto de bifurcação e sua posição no eixo X.
2. Faça cliques sucessivos para estender a ramificação para outros nós.
3. Clique com o botão direito para finalizar a ramificação.

Cada ramo é desenhado com uma cor diferente da paleta. As distâncias dos ramos são calculadas a partir do ponto de ramificação, de modo que ambas as curvas compartilhem a mesma origem X naquele ponto. Quando a variável selecionada é **Cabeça + Elevação**, os ramos também mostram sua própria curva de elevação do terreno próxima à linha piezométrica.

> ⚠️ **Restrições de integridade do curso**
>
> - Uma ramificação não pode reutilizar links ou nós que já pertencem ao caminho principal ou a outra ramificação, exceto o nó da ramificação de origem. Se tentada, a operação é rejeitada com uma mensagem de erro.
> - O nó de origem de uma ramificação não pode ser removido da travessia principal enquanto a ramificação estiver ativa. Para eliminá-lo, é necessário primeiro aparar o galho desde a extremidade mais distante.
> - **Mover nó de passagem** também verifica conflitos com caminhos existentes antes de aplicar a alteração.
> - Qualquer operação de edição (declarar, excluir ou mover um nó de etapa) será desfeita silenciosamente se o caminho recalculado resultante for inválido.

Declarar, remover ou mover um nó de etapa (anteriormente **Adicionar nó**, **Remover nó** e **Mover nó**) funciona da mesma forma no caminho principal e nos caminhos de ramificação.

As ramificações podem ser excluídas diretamente da **legenda do gráfico**, sem a necessidade de usar o botão Limpar.

O botão **Limpar** exclui o caminho principal e todas as ramificações.

---

## Atalhos do mouse

Com **Editar trajetos** ativo, além de traçar o trajeto clique a clique, o mouse suporta diversos atalhos diretos que evitam passar pelo menu de contexto. Esses atalhos funcionam da mesma forma na rota principal e nos ramais.

- **Clique duas vezes com o botão esquerdo em um nó intermediário** da rota (que ainda não é um nó de passagem): declara-o como um nó de passagem (equivalente a **Declarar nó de passagem**).
- **Clique duas vezes com o botão esquerdo em um nó de passagem já declarado**: exclui-o e o caminho é recalculado (equivalente a **Excluir nó de passagem**).
- **Clique duas vezes com o botão direito em um nó extremo do caminho** (a origem ou o fim de um caminho, com conexão gratuita disponível): estende o caminho a partir desse ponto (equivalente a **Estender caminho**).
- **Clique duas vezes com o botão direito em um nó de passagem interior** com grau de conexão maior que 2 (e conexão livre disponível): inicie uma ramificação desse nó (equivalente a **Criar ramificação**).
- **Simples clique com o botão esquerdo em um nó de passagem**, sem nenhum percurso em andamento: inicia o movimento desse nó; o próximo clique marca o nó de destino (equivalente a **Mover nó de passagem**).
- **Clique único com o botão direito**: se houver um tour em andamento, finaliza-o; caso contrário, abre o menu de contexto com as ações disponíveis para o nó sob o cursor.

O menu de contexto (simples clique com o botão direito) oferece diferentes opções dependendo do nó indicado:

| Situação do nó | Opções de menu |
|---------------------|--------------------|
| Ainda não há rota | **Inicie um novo caminho aqui** |
| Nó intermédio da rota (ainda não é um nó de passagem) | **Declarar nó de passagem** |
| Nó da etapa de origem da rota principal | **Estender caminho**, **Criar branch** |
| Nó extremo de passagem (fim de percurso) | **Estender caminho**, **Criar ramificação**, **Mover nó de passagem**, **Excluir nó de passagem** |
| Nó de passagem interior do percurso | **Criar ramificação**, **Mover nó de passagem**, **Excluir nó de passagem** |
| Nó de ramificação (origem de uma ramificação) | **Criar filial** |

> 💡 O botão **Ajuda** na barra de ferramentas do dock (ícone ⓘ) abre a caixa de diálogo **"Como editar trajetos"** a qualquer momento, com as mesmas informações resumidas.

---

## Dica interativa

Ao passar o mouse sobre o gráfico, uma linha vertical tracejada indica a posição do cursor. Acima de cada série ativa aparece um círculo de destaque no nó mais próximo e uma caixa de informações com:

- ID do elemento
- Distância acumulada do nó inicial
- Valor da variável para cada série ativa

**Linhas de referência verticais** são desenhadas no gráfico na posição X de cada nó no caminho: linhas finas em azul claro para todos os nós e linhas mais grossas para nós de referência.

### Sincronização bidirecional com mapa

A interação entre o gráfico e o mapa é bidirecional e atualiza em tempo real:

- Quando você passa o mouse sobre o **gráfico**, o nó mais próximo é destacado na **tela do mapa** com um círculo laranja.
- Mover o mouse sobre o **mapa** enquanto **Editar trajetos** está ativo move o cursor do gráfico para o nó correspondente.

---

## Configuração de importação e exportação

Dois botões da barra de ferramentas permitem salvar e recuperar a configuração completa de um painel de perfil.

**Caminho padrão**: a mesma pasta dos resultados da simulação, com o nome `{salida}_Profile_Config.cfg`.

As configurações armazenadas incluem:

- Variável principal e variável do eixo secundário (se houver)
- Nós de referência do traçado principal
- Todas as filiais definidas
- Opções de exibição: símbolos, etiquetas, envelope
- Configuração de eixos (escala, rótulos, grade)
- Estilos de curva (cor, espessura, tipo de linha, marcadores)
- Texto de descrição livre associado ao painel

> 💡 O dock inclui um campo de texto livre (descrição ou comentário) que é salvo junto com a configuração e pode ser usado para identificar a análise ou anotar observações.

Ao **importar** uma configuração, o perfil é recalculado a partir dos nós armazenados. Caso algum nó não exista mais na rede, o plugin exibe um aviso e continua com os nós disponíveis.

---

## Personalização do gráfico

A caixa de diálogo **Opções de gráfico** (botão de configuração na barra) possui quatro guias. O botão **Aplicar** visualiza as alterações em tempo real sem fechar a caixa de diálogo.

**Guia Eixos**
Para cada eixo (X = distância, Y = variável):
- Título personalizado.
- Auto escalonamento (habilitado por padrão) ou intervalo fixo manual.
- Mostrar ou ocultar grade.

Quando uma variável está ativa no **eixo secundário**, um grupo adicional do **Eixo Y (direita)** aparece com suas próprias configurações de escala e rótulo, independente do eixo Y primário.

**Guia Curvas**
Para cada série ativa:
- Cor, estilo de linha (Sólido / Tracejado / Pontilhado) e espessura.
- Marcadores: mostrar/ocultar e tamanho.

**Guia Legenda**
- Mostrar/ocultar legenda.
- Posição (Esquerda/Centro/Direita), tamanho da fonte e tamanho do símbolo.
- Mostrar moldura e cor de fundo da legenda.

**Guia Geral**
- Cor de fundo da área do gráfico.
