# Manipulação Geométrica e Topológica

As ferramentas do segundo grupo da barra Edição permitem modificar a geometria e a topologia da rede sem interromper a conectividade. QGISRed mantém a consistência entre a geometria espacial e os dados do modelo em todos os momentos.

> Todas as ferramentas desta página que são ativadas clicando no mapa (Mover nós, Inverter elementos, Mesclar/Dissolver junções, Criar/Remover conexões T, Criar/Remover cruzamentos...) resolvem o clique contra o elemento **mais próximo** dentro da tolerância configurada, e não contra o primeiro que encontrarem — importante quando há vários nós muito próximos uns dos outros.

---

## Seleção múltipla (selecione vários elementos)

**Barra de edição → Selecionar vários elementos**

Ferramenta de seleção simultânea em diversas camadas. Ative-o e desenhe um retângulo no mapa: todos os elementos de todas as camadas do projeto que se enquadram na área são selecionados.

A seleção é usada como **entrada** para outras ferramentas: Reverter elementos e Excluir elementos operam nos elementos selecionados, se houver algum, ou solicitam que você clique no mapa, se não houver seleção anterior.

> Para desmarcar, pressione o botão novamente ou use `Ctrl+Shift+A` (desmarcação global do QGIS).

---

## Mover nós (Mover nós)

**Barra de edição → Mover nós**

Move um ou mais nós (Junções, RNVs, RNFs) arrastando consigo **todos os elementos lineares conectados** (tubos, válvulas, bombas). A rede permanece conectada após o movimento.

<figure><img src="../assets/images/edicion/move-nodes.png" alt="Mova um nó e seus tubos conectados no mapa"><figcaption><p>Mova um nó e seus tubos conectados no mapa</p></figcaption></figure>
*Quando você arrasta um nó, todos os tubos conectados seguem o movimento.*

### Como usar

1. Ative a ferramenta.
2. Clique no nó que deseja mover (ou em uma área de nó na camada Junções).
3. Arraste para a nova posição.
4. Solte o botão do mouse para confirmar.

> Esta ferramenta **não** move vértices de tubos intermediários. Para isso, use **Editar vértices do link**.

---

## Editar vértices do link

**Barra de edição → Editar vértices do link**

Permite ajustar o layout visual de tubos e outros elementos lineares manipulando seus vértices intermediários. Isso não afeta os nós finais ou a topologia.

### Operações disponíveis

| Ação | Gesto |
|--------|-------|
| **Mover vértice** | Clique em um vértice existente (círculo azul) e arraste-o |
| **Adicionar vértice** | Clique no segmento entre dois vértices para inserir um novo |
| **Excluir vértice** | Clique com o botão direito em um vértice para excluí-lo |

---

## Elementos reversos (elementos reversos)

**Edição Barra → Inverter elementos**

Inverte a **orientação** de tubulações e conexões de serviço. A orientação determina a direção positiva do fluxo nos resultados da simulação.

### Duas maneiras de usar

1. **Sobre seleção**: Selecione um ou mais tubos com a ferramenta de seleção múltipla e pressione Reverter. Todos eles invertem sua orientação.
2. **Por clique**: Sem seleção prévia, pressione Reverter e clique no tubo que deseja reverter.

> A inversão afeta apenas a convenção de sinais da vazão nos resultados. Não modifica o comportamento hidráulico na simulação (o EPANET calcula sempre a direção real do fluxo, independente da orientação armazenada).

---

## Dividir/juntar tubos

**Edição Barra → Dividir/Unir tubos**

Clique em um tubo para **dividi-lo** no ponto indicado: QGISRed cria uma nova junção naquele ponto e duas seções com o mesmo diâmetro, material e atributos InstallYear do original.

Para **unir** dois tubos, clique no nó intermediário que eles compartilham: se esse nó tiver exatamente dois tubos conectados e o diâmetro, material, coeficiente de rugosidade e propriedades InstallYear forem iguais, o QGISRed os mescla em uma única seção e elimina o nó.

<figure><img src="../assets/images/edicion/split-pipe.png" alt="Dividir um tubo: um nó intermediário e duas seções são criados"><figcaption><p>Dividir um tubo: um nó intermediário e duas seções são criados</p></figcaption></figure>
*Clique em P-5 cria o nó J-42 e divide o tubo em P-5 e P-45.*

> Se os dois tubos tiverem diâmetro, material, coeficiente de rugosidade ou ano de instalação diferentes, a conexão não é feita e o plugin mostra um aviso.

---

## Mesclar/Dissolver junções

**Edição Barra → Mesclar/Dissolver junções**

Esta ferramenta funciona com **dois cliques**:

- **Um único clique** (clique e sem segundo ponto): **Separa** o nó indicado em tantos nós independentes quantos forem os tubos conectados a ele — você precisa de pelo menos dois tubos conectados ao nó, caso contrário o QGISRed avisa que não há nada para dissolver. Útil quando um nó agrupa vários tubos que não deveriam estar conectados topologicamente.
- **Dois cliques** (origem → destino): **Mescla** o nó de origem com o nó de destino. Todos os pipes conectados ao nó de origem são reconectados ao nó de destino. O nó de origem desaparece. Se os dois nós escolhidos já forem as duas extremidades do mesmo tubo, a fusão não é realizada (criaria um loop) e o QGISRed exibe um aviso.

Casos de uso comuns:
- Mesclar dois nós muito próximos que foram separados durante a importação de `.inp`.
- Separe um nó numa junção onde os tubos não estejam realmente conectados.

### O que acontece com as propriedades do nó de origem ao mesclar

QGISRed não simplesmente descarta os dados do nó que desaparece — ele os combina com os do nó de destino:

| Propriedade | Comportamento |
|-----------|-----------------|
| **Demanda base** | Caso os dois nós tenham uma única demanda com o mesmo padrão, os fluxos base são adicionados. Em qualquer outro caso, as demandas do nó de origem são adicionadas como categorias adicionais do nó de destino (ver [Demandas e cenários](../ferramentas/demandas-e-cenarios.md)). |
| **Fonte de qualidade** | Se apenas um dos dois nós tiver uma fonte de qualidade, esse será mantido. Se ambos tiverem o mesmo tipo e padrão, suas intensidades são somadas. Se ambos o possuírem, mas com tipo ou padrão diferente, o do nó de destino é mantido e o de origem é descartado, com aviso. |
| **Coeficiente de emissor** | Os coeficientes dos dois nós são somados. |

---

## Criar/Remover conexões T

**Edição Barra → Criar/Remover conexões T**

Gerencia juntas em T: pontos onde um nó está muito próximo de um tubo, mas **não** conectado a ele.

### Crie um T

1. Clique no nó que deseja conectar.
2. Clique no tubo ao qual deve ser conectado.
3. QGISRed divide o tubo no ponto mais próximo do nó e conecta ambos com um tubo curto, ou move o nó para o tubo se a distância for menor que a tolerância.

### Excluir um T

Clique na conexão T existente. O QGISRed verifica se os dois tubos em cada lado do nó são na verdade **colineares** (formam uma linha reta, dentro de uma tolerância angular): se estiverem, remove o nó intermediário e restaura o tubo original; caso contrário, ele rejeita a operação e mostra o quanto o par mais alinhado se desvia daquela reta, para você saber se realmente era uma conexão em T ou uma junção/ramo real.

---

## Criar/Remover cruzamentos (Criar/Remover cruzamentos)

**Barra de edição → Criar/Remover cruzamentos**

Gerencia cruzamentos entre tubos que se cruzam no mapa:

- **Criar junção**: Clique no ponto de interseção entre duas tubulações que não possuem um nó compartilhado. QGISRed divide os dois tubos e cria um nó comum na interseção.
- **Excluir junção**: clique em um nó de junção que tenha exatamente quatro tubos conectados. QGISRed verifica se esses quatro tubos formam dois pares **colineares** (duas linhas retas que se cruzam, dentro de uma tolerância angular); Se a melhor correspondência possível se desviar ainda mais da tolerância, ela rejeitará a operação e exibirá o ângulo de desvio em vez de desfazer uma correspondência que não era realmente uma correspondência. Se a verificação for aprovada, retire o nó e substitua os dois tubos originais que passam por ele.

> Esta ferramenta não aplica snap para evitar falsos positivos. A tolerância de detecção de cruzamento usa o valor configurado em **Valores padrão**.

---

## Mover válvulas e bombas (Move válvulas/bombas)

**Edição Barra → Mover válvulas/bombas**

Move uma válvula ou bomba de um tubo para outro mantendo todas as suas propriedades (tipo, ajuste, curva...).

### Processo

1. Ative a ferramenta. O cursor pede o primeiro clique.
2. Clique no **tubo fonte** (aquele que contém a válvula/bomba atual).
3. Clique no **pipe de destino** (onde o elemento será inserido).
4. QGISRed remove o elemento da posição original, restaura o tubo original e o insere na nova posição.

---

## Alterar status do elemento

**Barra de edição → Alterar status do elemento**

Alterna o estado operacional (Aberto/Fechado) de tubulações e válvulas manuais sem abrir a caixa de diálogo de propriedades.

- **Clique único**: Alternar entre Aberto e Fechado.
- **Ctrl + Clique**: Percorre todos os estados disponíveis: Aberto → Fechado → CV (Válvula de retenção) → Aberto.

A camada **Válvulas de isolamento** também pode ser gerenciada com esta ferramenta se estiver carregada.

> O estado é armazenado no campo `InitStatus` da camada correspondente e exportado para o `.inp` do EPANET.

---

## Excluir elementos (Excluir elementos)

**Barra de edição → Excluir elementos**

Exclua um ou mais elementos do projeto. Funciona de duas maneiras:

1. **Sobre seleção**: selecione itens com a ferramenta de seleção múltipla e pressione Excluir. Todos os itens selecionados são removidos.
2. **Ao clicar**: Sem seleção, ative a ferramenta e clique no elemento a ser excluído.

### Comportamento ao excluir

| Situação | O que acontece |
|-----------|------------|
| Excluir um canal | O tubo é removido. Os nós finais permanecem se tiverem outras conexões; Eles são eliminados se ficarem isolados. |
| Remover um nó com tubos conectados | Todos os tubos conectados também são removidos. |
| Remova uma válvula ou bomba | As duas seções do tubo em que foi dividido são automaticamente mescladas em uma só. |
| Excluir um RNV ou RNF | O elemento é convertido em Junção ou removido se não tiver conexões. |

> A exclusão não pode ser desfeita com `Ctrl+Z`. QGISRed salva automaticamente o estado anterior do projeto na pasta temporária antes de executar a operação, mas a única maneira de recuperar os dados excluídos é usar um **backup** anterior.
