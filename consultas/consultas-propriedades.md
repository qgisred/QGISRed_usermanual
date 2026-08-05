# Consultas de Propriedade

**Barra de consultas → Consultas por propriedades…**

Abre o painel **Consultas por Propriedades**, ferramenta de filtragem que destaca no mapa todos os elementos que atendem a uma ou mais condições em seus atributos. É a maneira mais rápida de encontrar, por exemplo, todos os tubos com diâmetro inferior a 80 mm, todos os nós com pressão abaixo de um limite ou todas as válvulas em estado fechado.

<figure><img src="../assets/images/consultas/queries-by-properties.png" alt="Painel Consultas por Propriedades com condições configuradas e resultado destacado em magenta"><figcaption><p>Painel Consultas por Propriedades com condições configuradas e resultado destacado em magenta</p></figcaption></figure>
*Consultas por Painel de Propriedades: condições configuradas nos atributos do pipe. Os itens que atendem à condição são destacados em magenta no mapa.*

---

## Interface do painel

O painel tem uma cor de identificação **roxo** (`#7B1FA2`) em seu cabeçalho para distingui-lo do resto dos painéis QGISRed. Contém:

- **Seletor de tipo de elemento**: Tubulações, Junções, RNVs, RNFs, Bombas, Válvulas
- **Área de condições**: uma ou mais linhas com campo, operador e valor
- **Botão Executar**: aplica a consulta e destaca o resultado
- **Botão Limpar**: remove o destaque do mapa
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
4. Pressione **Executar**. QGISRed avalia a consulta e destaca em **magenta** todos os elementos que atendem todas as condições simultaneamente (lógica AND).
5. Os itens destacados permanecem visíveis enquanto o painel está ativo. Pressione **Limpar** para remover o destaque.

---

## Combinação de condições

Todas as condições ativas são combinadas com a lógica **AND**: um elemento só é destacado se atender a **todas** condições de uma só vez. Para uma lógica OR (qualquer uma das condições), ela executa consultas separadas com um único critério por vez.

---

## Resultados da simulação

Caso o projeto possua resultados de simulação carregados, os campos de resultados (pressão, vazão, velocidade...) também aparecem no seletor de campos, permitindo filtrar, por exemplo, tubulações com velocidade inferior a 0,5 m/s ou nós com pressão negativa.

> ⚠️ **Campos de qualidade condicional.** Os campos de resultado `Quality` e `ReactRate` só aparecem quando o modelo de qualidade do projeto permite: `Quality` fica oculto com o modelo *None* e `ReactRate` só fica visível com o modelo *Chemical*. Os campos de qualidade estáticos (`BulkCoeff`, `WallCoeff`, `ReactCoef`, `IniQuality`) ficam ocultos quando o modelo de qualidade é *None*, *Age* ou *Trace*.

---

## Notas de uso

- A consulta não modifica nenhum dado do modelo nem cria novas camadas: apenas altera a simbologia temporal.
- O destaque magenta é visível em qualquer plano de fundo do mapa.
- Ao fechar o painel, o destaque desaparece e a simbologia volta ao estado anterior.

## Resolução do campo ID

O painel usa a mesma lógica de resolução automática de campo de identificador que o Element Explorer (`getIdFieldName(layer)`). Os campos de consulta por ID (`PipeID`, `TankID`, etc.) são detectados automaticamente com base no tipo de camada, portanto as consultas no campo `Id` funcionam corretamente independentemente do nome real do campo no shapefile do projeto. Veja [Explorador de Elementos](explorador-elementos.md) para mais detalhes.

Os apelidos `PumpCurvID`, `BaseDem` e `SourceQual` são automaticamente reconhecidos como campos do tipo numérico para bombas, demandas e fontes, respectivamente. O tipo de dados de cada campo (numérico, lista ou texto livre) é determinado automaticamente a partir do esquema do elemento, sem necessidade de configuração manual.
