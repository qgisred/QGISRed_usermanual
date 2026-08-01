# ✏️ Edição

A barra **Edição** contém todas as ferramentas para construir e editar a rede diretamente no mapa QGIS. Trabalhe nas camadas do projeto ativo sem precisar abrir tabelas de atributos ou arquivos externos.

<figure><img src="../assets/images/edicion/barra-edition.png" alt="Barra de ferramentas da edição QGISRed"><figcaption><p>Barra de ferramentas da edição QGISRed</p></figcaption></figure>
*Bar Edition: criação de elementos, edição geométrica e topológica, propriedades e dados de operação.*

> Todos os botões requerem o upload de um projeto válido. Se não houver nenhum, o plugin exibe _"Nenhum projeto válido está aberto"_.

---

## Ferramentas da barra de edição

### Grupo 1 — Criação de elementos

| # | Ferramenta | Função |
|---|-------------|---------|
| 1 | **Adicionar tubo** | Desenhe tubos clicando no mapa; cria nós automaticamente nas pontas |
| 2 | **Adicionar RNV** | Coloque um RNV (Tank) em um nó existente |
| 3 | **Adicionar RNF** | Coloque um RNF ou ponto de alimentação (Reservoir) em um nó existente |
| 4 | **Insira a válvula no tubo** | Insira uma válvula em um tubo existente, dividindo-o |
| 5 | **Insira a bomba no tubo** | Insira uma bomba em um tubo existente, dividindo-o |

### Grupo 2 — Edição geométrica e topológica

| # | Ferramenta | Função |
|---|-------------|---------|
| 6 | **Selecione vários elementos** | Seleção multicamadas por área retangular no mapa |
| 7 | **Mover nós** | Mova nós arrastando todos os elementos conectados |
| 8 | **Editar vértices do link** | Adicionar, mover e excluir vértices de tubos intermediários |
| 9 | **Elementos reversos** | Inverte a direção de orientação de tubulações ou conexões de serviço |
| 10 | **Dividir/juntar tubos** | Dividir um tubo no ponto indicado ou unir duas seções adjacentes |
| 11 | **Mesclar/Dissolver junções** | Mesclar dois nós em um ou separar um nó em vários |
| 12 | **Criar/Remover conexões T** | Criar ou excluir uma junta em T entre um nó e uma tubulação próxima |
| 13 | **Criar/Remover cruzamentos** | Cria ou exclui uma junção (nó compartilhado) entre tubos que se cruzam |
| 14 | **Mover válvulas/bombas** | Mover uma válvula ou bomba de um tubo para outro |
| 15 | **Alterar status do elemento** | Alterna o status Aberto/Fechado de tubos e válvulas |
| 16 | **Excluir elementos** | Exclua o item destacado ou itens selecionados |

### Grupo 3 — Propriedades e dados de funcionamento

| # | Ferramenta | Função |
|---|-------------|---------|
| 17 | **Editar propriedades do elemento…** | Abre a caixa de diálogo de propriedades do elemento clicado |
| 18 | **Editar padrões e curvas…** | Editor de padrões de demanda e curvas de bombas/RNVs |
| 19 | **Editar controles…** | Editor de controles simples e regras de operação |

---

## Nesta seção

* [Criação de elementos](criacao.md) — tubulações, RNVs, RNFs, válvulas, bombas
* [Manipulação geométrica e topológica](manipulacao.md) — mover, dividir, reverter, cruzar, excluir
* [Propriedades do elemento](propriedades.md) — caixa de diálogo de edição com navegador integrado
* [Padrões e curvas](curvas.md) — padrões de demanda, curvas H-Q, eficiência e volume
* [Controles e regras](controles.md) — controles simples e regras operacionais automáticas
