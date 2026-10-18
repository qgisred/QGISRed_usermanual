# Consultas de Propriedade

**Barra de consultas → Consultas por propriedades…**

Abre o painel **Consultas por Propriedades**, ferramenta de filtragem que destaca no mapa todos os elementos que atendem a uma ou mais condições em seus atributos. É a maneira mais rápida de encontrar, por exemplo, todos os tubos com diâmetro inferior a 80 mm, todos os nós com pressão abaixo de um limite ou todas as válvulas em estado fechado.

<figure><img src="../assets/images/queries/queries-by-properties.png" alt="Painel Consultas por Propriedades com condições configuradas e resultado destacado em magenta"><figcaption><p>Painel Consultas por Propriedades com condições configuradas e resultado destacado em magenta</p></figcaption></figure>
*Consultas por Painel de Propriedades: condições configuradas nos atributos do pipe. Os itens que atendem à condição são destacados em magenta no mapa.*

---

## Interface do painel

O painel tem uma cor de identificação **roxo** (`#7B1FA2`) em seu cabeçalho para distingui-lo do resto dos painéis QGISRed. Contém:

- **Seletor de tipo de elemento**: Tubulações, Junções, RNVs, RNFs, Bombas, Válvulas
- **Modo de critério**: duas opções, **One Criterion** (uma única condição ativa) e **Multiple Criteria** (lista de condições combináveis, veja abaixo)
- **Área de condições**: uma ou mais linhas com campo, operador e valor
- **Botão Executar**: aplica a consulta e destaca o resultado
- **Botão Limpar**: remove o destaque do mapa
- **Painel de Estatísticas**: seletor de propriedade e tabela com os resultados numéricos da consulta (veja abaixo)
- **Rótulo de tempo**: Quando os resultados da simulação são carregados, exibe o instante ativo com o prefixo "Tempo:" seguido do valor em negrito no formato `HH:MM:SS`. O rótulo de estatísticas do resultado também é mostrado em negrito.

---

## Tipos de condições

O operador disponível para cada campo depende do tipo de dados:

### Campos numéricos

| Operador | Significado |
|----------|-------------|
| `All` | Sem filtro (todos os valores) |
| `>=` | Maior ou igual a |
| `<=` | Menor ou igual a |
| `=` | Igual a |
| `>` | Maior que |
| `<` | Menos que |
| `≠` | Além de |
| `Range` | Entre dois valores (intervalo fechado) |

### Listar campos (enumerados)

Campos como `Status` que possuem um conjunto finito de valores possíveis:

| Operador | Significado |
|----------|-------------|
| `All` | Sem filtro |
| `=` | Igual ao valor selecionado |

> ℹ️ Para `Type`/`ValveType` em válvulas, o seletor de valor exibe o nome extenso descritivo do tipo (por exemplo, "Redutora de Pressão" para PRV) em vez do código EPANET.

### Campos de texto livres

Campos como `Tag` ou `Id`:

| Operador | Significado |
|----------|-------------|
| `All` | Sem filtro |
| `=` | Exatamente o mesmo |
| `≠` | Diferente |
| `ILIKE` | Contém (sem distinção entre maiúsculas e minúsculas) |
| `NOT ILIKE` | Não contém (não diferencia maiúsculas de minúsculas) |
| `LIKE` | Contém (diferencia maiúsculas de minúsculas) |
| `NOT LIKE` | Não contém (diferencia maiúsculas de minúsculas) |

---

## Processo

1. Abra **Consultas por propriedades** na barra de Consultas.
2. Selecione o **tipo de item** que você deseja filtrar.
3. Adicione uma ou mais condições: escolha o campo, o operador e escreva o valor.
4. Pressione **Executar**. QGISRed avalia a consulta e destaca em **magenta** os elementos que a atendem — no modo Multiple Criteria, segundo a lógica de inclusão/exclusão explicada abaixo.
5. Os itens destacados permanecem visíveis enquanto o painel está ativo. Pressione **Limpar** para remover o destaque.

---

## Modo de critério único ou múltiplo

O botão **One Criterion** limita o painel a uma única condição ativa por vez: alterar o campo, o operador ou o valor substitui a condição anterior. É o modo mais simples para consultas pontuais.

O botão **Multiple Criteria** abre uma lista de condições independentes que podem ser combinadas entre si:

- **Add**: adiciona a condição configurada acima à lista, marcada como condição de **inclusão** (`+`).
- **Subtract**: adiciona a condição configurada acima à lista, marcada como condição de **exclusão** (`-`).
- Cada linha da lista pode ser **reordenada** (setas para cima/baixo), **editada** (clique duplo ou botão de edição), **excluída**, ou **ativada/desativada** temporariamente sem excluí-la (botão "Enable/disable selected criterion") para testar combinações sem perder as condições já definidas.

Ao passar de **Multiple Criteria** para **One Criterion** com mais de uma condição na lista, o QGISRed pede confirmação: apenas a primeira é mantida, o restante é descartado.

### Lógica de combinação

As condições de inclusão (`+`) se combinam entre si com **OR**: um elemento é destacado se atender a **qualquer uma** delas. As condições de exclusão (`-`) se combinam entre si com **AND** e o resultado é **subtraído** do anterior. Resumindo:

> *(qualquer condição de inclusão)* **AND NOT** *(todas as condições de exclusão)*

Por exemplo, para encontrar todos os tubos com diâmetro ≥ 300 mm que **não** sejam de ferro fundido: uma condição `Diameter >= 300` marcada com **Add**, e uma condição `Material = Cast Iron` marcada com **Subtract**.

No modo **One Criterion** há apenas uma condição, portanto essa combinação não se aplica.

---

## Resultados da simulação

Caso o projeto possua resultados de simulação carregados, os campos de resultados (pressão, vazão, velocidade...) também aparecem no seletor de campos, permitindo filtrar, por exemplo, tubulações com velocidade inferior a 0,5 m/s ou nós com pressão negativa.

> ⚠️ **Campos de qualidade condicional.** Os campos de resultado `Quality` e `ReactRate` só aparecem quando o modelo de qualidade do projeto permite: `Quality` fica oculto com o modelo *None* e `ReactRate` só fica visível com o modelo *Chemical*. Os campos de qualidade estáticos (`BulkCoeff`, `WallCoeff`, `ReactCoef`, `IniQuality`) ficam ocultos quando o modelo de qualidade é *None*, *Age* ou *Trace*.

---

## Tabela de Estatísticas

O painel calcula estatísticas numéricas sobre os elementos destacados sem necessidade de exportar nada. Selecione no menu suspenso **Statistics of... for selected Elements** a propriedade a calcular — qualquer campo numérico do tipo de elemento ativo, ou uma das variáveis de resultado se houver simulação carregada — e a tabela é atualizada automaticamente.

As colunas dependem do tipo de propriedade:

| Propriedade | Colunas |
|---|---|
| Campo de texto ou lista | **Count** (número de elementos) |
| Campo numérico | **Count**, **Avg**, **Min**, **Max**, e **Sum** ou **StdD** de acordo com a propriedade (vazões e demandas mostram a soma; o restante, o desvio padrão) |
| **None** (sem propriedade) | apenas **Count** |

No modo **One Criterion** a tabela mostra uma única linha com o resultado da condição ativa. No modo **Multiple Criteria** com várias condições habilitadas, mostra uma linha para cada condição (rotulada `Cr1`, `Cr2`...) e uma linha final **All** em amarelo com o resultado combinado (a mesma lógica de inclusão/exclusão do destaque no mapa) — assim é possível comparar quantos elementos cada condição contribui isoladamente em relação ao total combinado.

## Exportar critérios e estatísticas

Os botões de exportação do painel (critérios de consulta e tabela de estatísticas) salvam por padrão na subpasta `Queries/Queries by properties` do projeto, em vez da pasta raiz.

> 📝 Ao exportar vários critérios combinados para texto ou CSV, cada linha é numerada como `Cr1:`, `Cr2:`... em vez de começar diretamente pelo operador da condição — assim uma planilha não interpreta por engano um critério que comece com `+` ou `-` como uma fórmula.

O CSV de estatísticas inclui, antes da tabela de valores, linhas de cabeçalho com o projeto, o cenário, o tipo de elemento, a consulta ou consultas aplicadas e a grandeza exportada.

## Notas de uso

- A consulta não modifica nenhum dado do modelo nem cria novas camadas: apenas altera a simbologia temporal.
- O destaque magenta é visível em qualquer plano de fundo do mapa.
- Ao fechar o painel, o destaque desaparece e a simbologia volta ao estado anterior.

## Resolução do campo ID

O painel usa a mesma lógica de resolução automática de campo de identificador que o Element Explorer (`getIdFieldName(layer)`). Os campos de consulta por ID (`PipeID`, `TankID`, etc.) são detectados automaticamente com base no tipo de camada, portanto as consultas no campo `Id` funcionam corretamente independentemente do nome real do campo no shapefile do projeto. Veja [Explorador de Elementos](explorador-elementos.md) para mais detalhes.

Os apelidos `PumpCurvID`, `BaseDem` e `SourceQual` são automaticamente reconhecidos como campos do tipo numérico para bombas, demandas e fontes, respectivamente. O tipo de dados de cada campo (numérico, lista ou texto livre) é determinado automaticamente a partir do esquema do elemento, sem necessidade de configuração manual.
