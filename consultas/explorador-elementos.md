#ElementExplorer

O **Element Explorer** é um painel flutuante (dock) que o QGISRed mantém como uma única instância. Ele agrupa duas funcionalidades relacionadas em abas separadas: busca de elementos por ID e visualização das propriedades do elemento selecionado no mapa.

<figure><img src="../assets/images/consultas/element-explorer.png" alt="Painel Element Explorer com as duas guias Localizar Elementos e Propriedades"><figcaption><p>Painel Element Explorer com as duas guias Localizar Elementos e Propriedades</p></figcaption></figure>
*Painel Element Explorer: guia Localizar Elementos (esquerda) e guia Propriedades (direita).*

Os botões **Localizar elementos por ID** e **Propriedades do elemento** na barra de Consultas abrem este mesmo painel e ativam a aba correspondente. A troca de guias dentro do painel não fecha nenhuma funcionalidade.

---

## Guia Encontrar Elementos — Pesquise por ID

**Barra de consultas → Encontrar elementos por ID…**

Localiza qualquer elemento da rede escrevendo seu ID e destaca-o no mapa.

### Itens pesquisáveis ​​

- Tubulações, Junções, Demandas, Reservatórios, Tanques, Bombas, Válvulas, Fontes

### Processo

1. Ative **Encontrar elementos por ID**. O painel abre ou é trazido para frente.
2. Selecione o tipo de elemento no menu suspenso da camada.
3. Digite o ID no campo de texto e pressione **Localizar** ou Enter.
4. QGISRed centraliza o mapa no elemento e o destaca. O resultado aparece no painel com fundo amarelo claro.

### Pesquisa múltipla

Separe vários IDs com vírgula ou ponto e vírgula para destacá-los todos simultaneamente.

### Se o ID não existir

O painel exibe um aviso e o mapa não muda.

---

## Aba Propriedades — Propriedades do elemento

**Barra de consultas → Propriedades do elemento…**

Ativa uma ferramenta interativa de identificação: ao clicar em qualquer elemento do mapa, o painel mostra todos os seus atributos na aba Propriedades.

### Processo

1. Ative **Propriedades do elemento**. O cursor muda para o modo de identificação.
2. Clique em qualquer elemento da rede.
3. O painel mostra os campos do elemento clicado. Você pode continuar clicando em outros elementos sem desativar a ferramenta.

### Informações exibidas

Os atributos são organizados por tipo de elemento. Para um **tubo** típico:

| Campo | Descrição |
|-------|-------------|
| `Id` | Identificador único |
| `Length` | Comprimento (m) |
| `Diameter` | Diâmetro (mm) |
| `Roughness` | Coeficiente de rugosidade |
| `Material` | Materiais |
| `InstallYear` | Ano de instalação |
| `Status` | Status (Aberto/Fechado/CV) |
| `Tag` | Etiqueta grátis |

Para **nós** `Elevation`, `Demand`, `Pattern`, `InitQuality`, etc. Cada tipo de item possui seu próprio conjunto de campos.

Caso o projeto possua resultados de simulação carregados, o painel adiciona uma seção com os valores calculados (pressão, vazão, velocidade...) para o período ativo no visualizador de resultados. O tempo simulado é indicado pelo prefixo **Time:** seguido do valor em negrito no formato `HH:MM:SS`.

> ⚠️ **Campos de qualidade condicional.** O campo `Quality` só aparece quando o modelo de qualidade do projeto não é *Nenhum*. O campo `ReactRate` só fica visível quando o modelo de qualidade é *Químico*; permanece oculto para os modelos *None*, *Age* e *Trace*. Estes campos só são exibidos quando o modelo de qualidade do projeto os suporta.

### Notas de uso

- Desativar o botão retorna o cursor para o modo de navegação padrão do QGIS.
- Se clicar numa área sem elementos, o painel mantém a última seleção.
- O fundo do painel possui uma tonalidade amarelo claro para diferenciá-lo dos demais painéis QGIS.
- Os cliques em camadas que não pertencem ao projeto QGISRed ativo (camadas de fundo, camadas auxiliares externas, etc.) são ignorados: o painel não atualiza seu conteúdo.

### Resolução do campo ID por camada

QGISRed resolve automaticamente o **nome do campo identificador** de cada camada de rede usando a função interna `getIdFieldName(layer)`. Isso permite que o plugin detecte corretamente o ID em camadas com diferentes convenções de nomenclatura:

| Tipo de camada | Campo ID típico |
|--------------|-----------------|
| Tubos | `PipeID` |
| Junções | `JunctionID` |
| Tanques | `TankID` |
| Reservatórios | `ReservoirID` |
| Bombas | `PumpID` |
| Válvulas | `ValveID` |

Se o seu projeto usar convenções de nomenclatura personalizadas, a resolução automática evitará erros de pesquisa ou identificação. Não há necessidade de configurar nada manualmente: o scanner detecta o campo correto quando ativado em qualquer camada da rede.

### Aliases de campos adicionais reconhecidos automaticamente

O painel reconhece automaticamente os seguintes aliases de campo e os apresenta com rótulos, unidades e decimais corretos sem qualquer configuração adicional:

| Alias ​​| Descrição |
|-------|-------------|
| `DemPattID` | Padrão de demanda em nós; é suprimido quando múltiplas solicitações estão ativas e agrupadas corretamente |
| `HedPattID` | Padrão de curva de altura da bomba |
| `QualPattID` | Padrão de qualidade em fontes |
| `NodeID` | Identificador de nó em camadas derivadas |
| `NodeType` | Tipo de nó |
| `LinkID` | Identificador de link em camadas derivadas |
| `LinkType` | Tipo de vínculo |

> ℹ️ O reconhecimento é automático: o navegador detecta o alias correto quando ativado em qualquer camada da rede, sem a necessidade de configurar nada manualmente.
