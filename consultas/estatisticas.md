# Estatísticas

**Barra de consultas → Estatísticas…**

Abre o painel **Estatísticas**, que calcula e exibe a distribuição estatística de qualquer atributo numérico ou categórico na rede, com suporte para classificação automática, segunda classificação cruzada e representação gráfica.

> **ℹ️ Nota:** O painel Estatísticas abre **encaixado** na janela principal do QGIS e respeita os painéis já agrupados em abas. Seus controles também se adaptam a larguras estreitas de painéis, sem serem cortados na borda direita.

<figure><img src="../assets/images/consultas/statistics-panel.png" alt="Painel de estatísticas com histograma de diâmetros de tubos"><figcaption><p>Painel de estatísticas com histograma de diâmetros de tubos</p></figcaption></figure>
*Painel de Estatísticas: histograma de diâmetros de tubos com classificação por intervalos.*

---

## Estrutura do painel

O painel Estatísticas está organizado em duas guias:

- **Setup**: define o que é analisado e como é classificado.
- **Relatório**: mostra o histograma e a tabela de resultados. Ele é ativado automaticamente após a execução da análise.

---

## Aba Configuração

### Tipo e propriedade do elemento

Selecione o tipo de elemento (Junções, Tubulações, Tanques...) e a propriedade a analisar. O seletor de propriedades exibe em uma **lista unificada** os campos de projeto (Diâmetro, Comprimento, Rugosidade...) e os campos de resultado da simulação (Pressão, Vazão, Velocidade...). Os campos de resultados aparecem com **fundo amarelo/creme** para diferenciá-los visualmente dos campos de design.

### Classificação principal

| Parâmetro | Descrição |
|-----------|-------------|
| **Campo** | Propriedade a ser classificada |
| **Método** | Como calcular os intervalos (ver tabela abaixo) |
| **Número de turmas** | Quantos grupos são gerados |

#### Métodos de classificação disponíveis

Os métodos a seguir estão disponíveis para a classificação principal e para a segunda classificação. O método padrão é **Pretty Breaks**.

| Método | Descrição |
|--------|-------------|
| **Jenks (pausas naturais)** | Minimiza a variação intraclasse. Ideal para distribuições não uniformes. |
| **Pausas bonitas** | Limites de intervalo "redondos". Preferível para apresentações. *(Padrão)* |
| **Contagem igual** | Cada classe contém o mesmo número de elementos. |
| **Intervalo fixo** | Todos os intervalos têm a mesma amplitude. |
| **Manual** | O usuário define diretamente os limites de cada intervalo. |

> **ℹ️ Nota:** Quando todos os valores são idênticos ou muito semelhantes, os endpoints de classe duplicados são recolhidos mostrando um único valor em vez de "100,0 - 100,0".

> **ℹ️ Nota — Campos sem dados úteis:** Caso o campo escolhido para classificar não possua nenhum valor calculado, o painel não apresenta mensagem de erro: gera diretamente uma única classe **NULL** que agrupa todos os elementos sem valor. Se o campo tiver valores, mas todos forem iguais (incluindo o caso em que todos são zero), uma única classe será gerada com esse valor, assim como no caso anterior de endpoints recolhidos. Em ambos os casos o histograma e a tabela são gerados normalmente, sem interromper a análise.

> **ℹ️ Nota:** Ao analisar um campo de resultado de simulação dinâmica, os **limites de classe são calculados uma vez** considerando todos os instantes de tempo simultaneamente. À medida que a etapa de simulação avança, a contagem de elementos por barra varia, mas os limites permanecem constantes, permitindo **comparar distribuições entre instantes de tempo** com total consistência.

### Pré-filtragem

Antes de calcular, você pode limitar o conjunto de elementos com uma condição em qualquer campo:

- **campos numéricos**: `>=`, `<=`, `=`, `>`, `<`, `≠`, `Range`
- **lista** campos: `=`
- **texto** campos: `=`, `≠`, `ILIKE`, `NOT ILIKE`, `LIKE`, `NOT LIKE`
- Selecione **Sem filtro** para incluir todos os elementos sem restrições.

O campo **Valor** inclui um botão **(×)** limpar: quando pressionado, limpa o texto inserido e não deixa nenhuma seleção ativa, facilitando a troca rápida do filtro.

Quando o atributo de filtro é um campo de resultado de simulação, o combo exibe o mesmo **fundo amarelo/creme** usado para esses campos no seletor de propriedades.

> **ℹ️ Nota — Fluxo:** Ao filtrar no campo `Flow` com valor numérico escrito, o valor é sempre interpretado como **valor absoluto**, pelo que não é necessário saber o sinal que o EPANET atribui internamente ao fluxo.

### Restringir à seleção ativa

A caixa de seleção **Apenas elementos selecionados** limita a análise aos elementos atualmente selecionados no mapa. A seleção é avaliada conjuntamente entre a camada **Entradas** e sua camada **Resultados** correspondente: se o elemento for selecionado em qualquer camada do mesmo tipo (por exemplo, `Pipes` em Entradas e seu tema de resultados do pipeline), ele será incluído no cálculo.

> ⚠️ Se você ativar a caixa e nenhum elemento estiver selecionado em nenhuma das camadas, o painel exibe um aviso e não executa a análise.

Enquanto o checkbox estiver ativo, tanto o histograma quanto a tabela exibem uma nota indicando que existe um filtro de seleção (e, se também houver um filtro de atributos ativo, ambos são combinados no mesmo texto).

#### Visualização no mapa

A seção Filtros inclui dois itens adicionais para verificar o filtro antes de executar a verificação completa:

- **Caixa de seleção "Visualizar no mapa"**: quando marcada, os itens que atendem à condição de filtro são destacados em **laranja** na tela do mapa. A visualização é atualizada automaticamente quando você altera qualquer parâmetro de filtro.
- **Contador de correspondências** (ex. *"correspondência de 43 itens"*): visível sempre que a seção Filtros for exibida, mesmo antes de executar a análise.

Os realces são removidos automaticamente quando você fecha o painel ou recolhe a seção Filtros.

### Segunda classificação *(opcional)*

Um grupo recolhível (recolhido por padrão) permite definir um **segundo critério de classificação** no mesmo conjunto de elementos. Quando implantado, o seguinte é configurado:

| Parâmetro | Descrição |
|-----------|-------------|
| **Campo** | Propriedade de segunda classificação |
| **Método** | Jenks (quebras naturais), pausas bonitas, contagem igual, intervalo fixo ou manual |
| **Número de turmas** | Grupos de segunda classificação |

Quando a segunda ordenação está ativa, a tabela de resultados se torna uma **matriz cruzada**: as linhas representam os grupos da primeira ordenação e as colunas representam os grupos da segunda.

> **ℹ️ Nota:** Ao alterar o tipo de elemento e retornar ao anterior, as configurações da segunda classificação (método, número de classes, intervalos, valores manuais) são **recuperadas automaticamente**.

---

## Guia Relatório

A guia Relatório é dividida em dois quadros: **Histograma** e **Tabela**.

### Histograma

O histograma mostra a distribuição da propriedade analisada:

- **Seletor de estatísticas**: Escolha o que é representado no eixo Y: Contagem, Soma, Média, Mín, Máx ou StdD.
- **Botão Expandir**: abre o histograma em uma **janela flutuante separada**, útil para ter o painel de configurações e o gráfico visíveis ao mesmo tempo.
- O **título do gráfico** inclui a estatística selecionada como prefixo e as unidades do campo. Por exemplo: *"Pressão Média (mca) por Diâmetros (mm) para Material PVC"*.
- Para campos categóricos, o histograma exibe barras por categoria em vez de intervalos numéricos.

### Tabela de resultados

A tabela exibe os mesmos dados em formato tabular:

- Os valores são formatados com as casas decimais correspondentes a cada campo conforme o CSV das unidades do projeto.
- Os números inteiros são exibidos sem decimais.
- O **título da tabela** reflete sempre as duas dimensões de classificação ativas, incluindo as unidades de cada campo.
- A **linha de exportação** inclui um seletor de estatísticas para escolher qual valor será descartado ao exportar para CSV (Contagem, Soma, Média...).
- A exportação CSV inclui os **valores de ponto de interrupção manual** de ambas as classificações (principal e segunda), com os cabeçalhos das colunas acompanhados das unidades entre parênteses.
- Quando a segunda classificação está ativa, a tabela se torna uma **matriz cruzada** com colunas adicionais para cada grupo da segunda classificação.

---

## Campos disponíveis

### Campos categóricos

Os seguintes campos são tratados como categorias (valores discretos):

| Campo | Descrição |
|-------|-------------|
| `Material` | Material do tubo |
| `Type` | Tipo de elemento |
| `ValveType` | Tipo de válvula |
| `MeterType` | Tipo de contador |
| `SourceType` | Tipo de fonte |
| `IniStatus` | Situação operacional inicial (Aberto/Fechado/CV) |
| `InstalDate` | Data de instalação |
| `InstDate` | Data de instalação |
| `Tag` | Etiqueta grátis |

### Campos de entrada numéricos

Qualquer campo numérico no modelo: `Diameter`, `Length`, `Roughness`, `Elevation`, `BaseDem`, etc.

### Campos de resultado da simulação

Disponível apenas se os resultados forem carregados:

**Nós:**

| Campo | Descrição |
|-------|-------------|
| `Pressure` | Pressão (m.c.a.) |
| `Head` | Altura piezométrica (m) |
| `Demand` | Procura calculada (l/s) |
| `Quality` | Qualidade da água |

**Tubos:**

| Campo | Descrição |
|-------|-------------|
| `Status` | Estado em simulação |
| `Flow` | Caudal (l/s) |
| `Velocity` | Velocidade (m/s) |
| `HeadLoss` | Perda de carga (m) |
| `UnitHdLoss` | Perda unitária (m/km) |
| `FricFactor` | Fator de atrito |
| `ReactRate` | Taxa de reação |
| `Quality` | Qualidade da água |

> **⚠️ Nota:** Os campos `Velocity`, `UnitHdLoss`, `FricFactor` e `ReactRate` não estão disponíveis quando o tipo de elemento selecionado for **Bombas** ou **Válvulas**; Eles são exclusivos para tubos.

---

## Notas de uso

- O painel Estatísticas não modifica nenhum dado do modelo.
- Você pode manter o painel aberto enquanto navega no mapa ou altera parâmetros; atualiza o cálculo quando você pressiona o botão executar novamente.
- A segunda classificação é recolhida por padrão; implante-o somente quando precisar de análise cruzada.
