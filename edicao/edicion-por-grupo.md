# Editar por grupo

**Barra de edição → Editar propriedades por grupo…**

A ferramenta **Editar propriedades por grupo** permite modificar um atributo de vários elementos de rede em massa. Combine um filtro opcional com uma ação de edição e aplique o resultado a todos os elementos que atendam à condição, acumulando as alterações em um buffer de edição do QGIS até que o usuário as confirme ou descarte.

A caixa de diálogo é **sem janela restrita**: você ainda pode interagir com o mapa enquanto ele estiver aberto.

<figure><img src="../assets/images/edicion/edicion-por-grupo.png" alt="Editar propriedades por caixa de diálogo de grupo com filtro e ação configurados"><figcaption><p>Editar propriedades por caixa de diálogo de grupo com filtro e ação configurados</p></figcaption></figure>
*Editar caixa de diálogo por grupo: filtrar por campo numérico e multiplicar por ação em tubos.*

---

## Tipos de itens disponíveis

| Elemento | Descrição |
|----------|-------------|
| **Junções** | Nós de rede |
| **Múltiplas Demandas** | Múltiplas reivindicações por categoria |
| **Tubos** | Tubos |
| **Tanques** | Depósitos |
| **Reservatórios** | Reservatórios |
| **Bombas** | Bombas |
| **Válvulas** | Válvulas |
| **Fontes** | Fontes de qualidade |
| **Conexões de serviço** | Juncos |
| **Válvulas de isolamento** | Válvulas de isolamento |
| **Metros** | Medidores de vazão |

> 🧪 **Campos de Qualidade Química:** Os campos BulkCoeff e WallCoeff (tubulações) e ReactCoef e InitQuality (reservatórios, reservatórios e nós) só aparecem nos seletores de campo quando o modelo de qualidade do projeto está definido como **Química**.

---

## Selecionar elementos

A seção **Selecionar elementos** da caixa de diálogo agrupa o filtro de campo, a visualização do mapa e o escopo.

### Filtro de campo

O menu suspenso do campo começa com a opção **Sem filtro**. Enquanto a seleção é mantida, os controles de operador e valor permanecem ocultos e a ação afeta todos os elementos do tipo escolhido.

Quando você seleciona um campo específico, os controles de operador e valor aparecem:

- O **operador** determina o tipo de comparação (ver tabela abaixo).
- O **valor** é preenchido automaticamente com os valores únicos presentes na camada. A lista inclui **NULL** como primeira opção:
- O operador `=` com NULL gera um filtro **IS NULL**.
- O operador `≠` com NULL gera um filtro **IS NOT NULL**.
- O campo de valor possui um botão **×** para excluí-lo rapidamente. Além disso, o campo é **editável**: o usuário pode inserir um valor personalizado que não esteja listado na lista suspensa.

#### Operadores disponíveis por tipo de campo

| Tipo de campo | Operadores |
|---------------|------------|
| Numérico | `>=`, `<=`, `=`, `>`, `<`, `≠` |
| Lista de valores | `=` |
| Texto livre | `=`, `≠`, `ILIKE`, `NOT ILIKE`, `LIKE`, `NOT LIKE` |
| Data | `=` (seletor de calendário) |

### Visualização no mapa

A caixa de seleção **Visualizar no mapa** destaca em **laranja** os elementos que atendem ao filtro ativo, atualizando em tempo real quando algum parâmetro do filtro for alterado. Ao lado desta caixa de seleção está o **número de elementos** que correspondem ao filtro naquele momento.

### Somente itens selecionados

Ao marcar **Apenas feições selecionadas**, a ação afeta apenas os elementos que estão selecionados no mapa no momento em que você pressiona **Aplicar**. A seleção pode ser feita antes de abrir a caixa de diálogo ou enquanto ela está aberta.

Desmarcada (padrão), a ação é aplicada a todos os elementos do tipo escolhido que atendem ao filtro.

---

## Editar ação (“Seção Fazer…”)

Define qual atributo modificar e com qual valor ou transformação.

### Ações para campos numéricos

| Ação | Fórmula |
|--------|---------|
| **Substitua por** | `operando` |
| **Multiplicar por** | `valor_actual × operando` |
| **Adicionar** | `valor_actual + operando` |
| **Subtrair** | `valor_actual − operando` |
| **Dividir por** | `valor_actual / operando` |
| **Aperte o mínimo para** | `max(valor_actual, operando)` |
| **Aperte máximo para** | `min(valor_actual, operando)` |

### Ações para campos de texto

| Ação | Resultado |
|--------|-----------|
| **Definir como** | Substitui todo o valor |
| **Anexar** | Acrescenta o texto ao valor atual |
| **Anexar** | Adiciona o texto ao final do valor atual |
| **Localizar e substituir** | Pesquisar e substituir (diferencia maiúsculas de minúsculas) |

### Ações para campos enumerados

Basta **Substituir por**, selecionando o novo valor em uma lista. As opções disponíveis dependem do tipo de campo:

| Campo | Fonte de opções |
|-------|--------------------|
| `InitStatus` | Lista EPANET fixa (Aberta, Fechada, CV, Ativa…) |
| `Material` | Tabela de Materiais do Projeto |
| `Curve` | Curvas de projeto filtradas por tipo (bomba, volume, eficiência, perda de carga) |
| `Pattern` | Padrões de projetos filtrados por tipo (demanda, qualidade, cabeça, velocidade, preço) |

### Campos de data

**Definir como** ação: A data é selecionada na combinação de datas existente na camada ou por meio do botão de calendário.

---

## Botões de diálogo

| Botão | Comportamento |
|-------|----------------|
| **Inscreva-se** | Exibe uma caixa de diálogo de pré-comprometimento detalhando as alterações a serem aplicadas temporariamente (tipo de item, campo e número de itens afetados) e solicita confirmação antes de gravar no buffer de edição do QGIS. Pode ser chamado várias vezes para acumular alterações em diferentes atributos. Os elementos modificados são selecionados no mapa e sua tabela de atributos é aberta ou reativada. |
| **Aceitar** | Mostra uma confirmação simples e, após aceitar, salva permanentemente em disco todas as alterações acumuladas no buffer. Feche o diálogo; as tabelas de atributos permanecem abertas. |
| **Cancelar** | Descarta **todas** as alterações acumuladas no buffer (reversão completa) e fecha a caixa de diálogo. Limpa a seleção no mapa, mas as tabelas de atributos permanecem abertas. |

> As alterações só são gravadas no disco quando você pressiona **Aceitar**. Ao trabalhar com **Aplicar**, os dados estão no buffer de edição do QGIS e podem ser desfeitos em massa com **Cancelar** a qualquer momento.

---

## Tabela de atributos

Após cada **Aplicar**, a ferramenta abre ou reativa a tabela de atributos da camada afetada — esteja ela encaixada ou flutuante — sem duplicá-la. Os elementos modificados aparecem ordenados no início. Se várias camadas forem editadas em **Aplicar** sucessivas, cada tabela será gerenciada de forma independente.

Ao pressionar **Cancelar** ou **Aceitar**, as tabelas de atributos permanecem abertas; apenas a seleção no mapa é apagada.

---

## Atualização automática da caixa de diálogo

Quando camadas são adicionadas ou removidas enquanto a caixa de diálogo está aberta, ela atualiza e restaura automaticamente o tipo de elemento, campo e seleções de filtro anteriores. Se o projeto for fechado ou um projeto diferente for carregado, a caixa de diálogo fecha automaticamente.

---

## Exemplos de uso

**Alterar material para tubos de diâmetro específico**
Elemento: Tubos — Filtro: `Diameter = 200` — Do: `Material → Replace with → PVC`

**Aumentar a rugosidade dos tubos de ferro fundido em 10%**
Filtro: `Material = FD` — Faça: `Roughness → Multiply by → 1.1`

**Feche todas as válvulas de isolamento**
Elemento: Válvulas de Isolamento — Filtro: Sem Filtro — Do: `InitStatus → Replace with → CLOSED`

**Atribuir padrão a um conjunto de nós selecionado**
Marque "Apenas feições selecionadas" — Elemento: Junções — Do: `Pattern → Replace with → PAT_RESIDENCIAL`

**Substitua o texto nos rótulos**
Elemento: Junções — Do: `Tag → Find and replace → Buscar: "SEC" / Reemplazar: "ZN"`
