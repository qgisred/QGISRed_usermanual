# Perfis Longitudinais

**Barra de análise → Perfil longitudinal…**

O perfil longitudinal mostra a evolução de uma variável hidráulica ao longo de um caminho definido interativamente sobre a rede. O eixo X representa a distância acumulada desde o nó inicial do percurso; no eixo Y, o valor da variável selecionada em cada nó do caminho. É possível abrir vários painéis de perfil simultaneamente, cada um com seu próprio caminho, variáveis ​​e configurações independentes.

> **Pré-requisito**: Uma simulação EPANET deve ter sido executada antes de abrir o perfil. Se nenhum resultado estiver disponível, o plugin exibe a mensagem _"Execute uma simulação primeiro para construir um perfil longitudinal."_

> 📝 O plugin detecta automaticamente se os resultados vêm do formato padrão EPANET ou do formato `.hyd` estendido QGISRed; nenhum ajuste manual é necessário.

<figure><img src="../assets/images/analisis/perfil-longitudinal-dock.png" alt="Doca de perfil longitudinal com rota desenhada no mapa e gráfico de pressão"><figcaption><p>Doca de perfil longitudinal com rota desenhada no mapa e gráfico de pressão</p></figcaption></figure>
*Perfil longitudinal: percurso destacado em vermelho no mapa (esquerda) e gráfico de altura piezométrica + elevação do terreno (direita).*

---

## Múltiplas janelas de perfil

O plugin permite que você mantenha vários docks de perfil abertos ao mesmo tempo. Cada dock funciona de forma totalmente independente: possui seu próprio caminho, suas próprias variáveis ​​selecionadas e suas próprias configurações de gráfico.

- O botão **Novo Painel** na barra de ferramentas cria um encaixe adicional numerado sequencialmente (_Perfil 2_, _Perfil 3_, etc.).
- O painel ativo – aquele que recebe as interações do mapa – é visualmente diferenciado dos demais.
- Abrir o perfil no menu Análise reutiliza o primeiro painel se já estiver aberto; caso contrário, crie um novo.

---

## Abrir e construir perfil

1. Ative **Perfil longitudinal** na barra Análise. O encaixe do perfil é aberto na área inferior do QGIS.
2. O modo **Pick** é ativado automaticamente; O cursor muda para o ícone do perfil.
3. Clique em um nó da rede (Entroncamentos, Tanques, Reservatórios) para definir o primeiro nó de referência.
4. Clique em outro nó: o plugin calcula o **caminho topológico mínimo** entre os dois nós e desenha o perfil.
5. Cada clique adicional estende o caminho concatenando o caminho do último nó para o novo.

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

| Botão | Modo | Função |
|-------|------|---------|
| Escolha | **Escolha** | Ativa o mapa para adicionar nós de referência ao final do caminho a cada clique |
| Adicionar nó | **Adicionar nó** | Converte um nó intermediário existente no caminho em um nó de referência; também se aplica a ramais |
| Remover nó | **Remover nó** | Remove um nó de referência da travessia (os nós finais não podem ser removidos); também se aplica a filiais |
| Mover nó | **Mover nó** | Realoca um nó de referência: primeiro clique na posição atual, depois clique na nova posição; também se aplica a ramificações e verifica conflitos com caminhos existentes |
| Filial | **Filial** | Adicione uma ramificação lateral (veja a seção [Filiais](#ramas)) |

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
| **Símbolos** | Mostra simbologia dos elementos (nó, tanque, reservatório, bomba, válvula) e setas de direção do fluxo na curva |
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

O modo **Ramal** permite adicionar ramais laterais que compartilham o mesmo gráfico da rota principal.

1. Ative o modo Filial.
2. Clique em um nó já pertencente ao caminho principal ou em uma ramificação existente: esse nó define o ponto de ramificação e sua posição no eixo X.
3. Faça cliques sucessivos para estender a ramificação para outros nós.

Cada ramo é desenhado com uma cor diferente da paleta. As distâncias dos ramos são calculadas a partir do ponto de ramificação, de modo que ambas as curvas compartilhem a mesma origem X naquele ponto. Quando a variável selecionada é **Cabeça + Elevação**, os ramos também mostram sua própria curva de elevação do terreno próxima à linha piezométrica.

> ⚠️ **Restrições de integridade do curso**
>
> - Uma ramificação não pode reutilizar links ou nós que já pertencem ao caminho principal ou a outra ramificação, exceto o nó da ramificação de origem. Se tentada, a operação é rejeitada com uma mensagem de erro.
> - O nó de origem de uma ramificação não pode ser removido da travessia principal enquanto a ramificação estiver ativa. Para eliminá-lo, é necessário primeiro aparar o galho desde a extremidade mais distante.
> - O modo **Mover nó** também verifica conflitos com caminhos existentes antes de aplicar a alteração.
> - Qualquer operação de edição (Adicionar, Remover, Mover) será desfeita silenciosamente se o caminho recalculado resultante for inválido.

Os modos **Adicionar nó**, **Remover nó** e **Mover nó** funcionam tanto no caminho principal quanto nos caminhos de ramificação.

As ramificações podem ser excluídas diretamente da **legenda do gráfico**, sem a necessidade de usar o botão Limpar.

O botão **Limpar** exclui o caminho principal e todas as ramificações.

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
- Mover o mouse sobre o **mapa** enquanto o modo Seleção de perfil está ativo move o cursor do gráfico para o nó correspondente.

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
