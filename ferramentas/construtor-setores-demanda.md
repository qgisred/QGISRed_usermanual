# Construtor de setor de demanda

**Barra de ferramentas → Construtor de setor de demanda…**

O **Demand Sector Builder** é uma caixa de diálogo modal que permite criar e gerenciar múltiplas **setorizações nomeadas** da rede

<figure><img src="../assets/images/herramientas/constructor-sectores.png" alt="Caixa de diálogo Demand Sector Builder com lista de setorizações e configurações de tópico"><figcaption><p>Caixa de diálogo Demand Sector Builder com lista de setorizações e configurações de tópico</p></figcaption></figure>
*Demand Sector Builder: lista de setorizações (painel esquerdo), parâmetros de detecção e tópicos a serem gerados (painel direito).*, cada um com seus setores de demanda. Cada setorização agrupa os nós da rede em zonas de acordo com a topologia e limites definidos pelo usuário, e gera as camadas auxiliares necessárias para utilização no Nodal Demand Builder ou para análise de balanço hídrico.

---

## Conceitos-chave

| Conceito | Descrição |
|----------|-------------|
| **Setorização** | Conjunto nomeado de setores que cobre toda a rede. Pode haver múltiplas setorizações em um mesmo projeto. |
| **Setor** | Subconjunto de nós e links delimitados por limites. Cada nó pertence a exatamente um setor dentro de uma setorização. |
| **Tema** | Tipo de camada geométrica que representa os setores. O Builder pode gerar até 6 tipos de tópicos para cada setorização. |
| **Fronteira** | Elemento ou conjunto de elementos que delimita dois setores adjacentes (tubos de borda, válvulas, medidores de vazão). |

---

## Criar e gerenciar setorizações

### Lista de setorizações

O painel esquerdo da caixa de diálogo mostra todas as fatias do projeto. Cada entrada possui:
- Nome editável.
- Botões Adicionar (＋) e Excluir (✕).

### Adicione uma setorização

1. Pressione **+** na lista de setores.
2. Insira um nome amigável (por exemplo, `Sectorizacion_2024`, `Zonas_Presion`).
3. Configure os parâmetros de detecção e os tópicos a serem gerados.
4. Pressione **Build** para executar a análise.

As setorizações são armazenadas nas camadas auxiliares do projeto no grupo **Camadas Auxiliares > Setores de Demanda**.

---

## Detecção de setor

O Builder detecta os setores usando um algoritmo **BFS** (pesquisa ampla) que percorre a topologia da rede começando pelos elementos de borda marcados.

### Tipos de borda

| Tipo | Descrição |
|------|-------------|
| **Tubos** | Tubos marcados como borda; o fluxo através deles delimita setores |
| **Válvulas de isolamento** | Válvulas de isolamento na rede |
| **Metros** | Medidores de vazão (delimitam setores de balanço hídrico) |

A seleção de qual tipo de elemento atua como borda é configurada usando caixas de seleção na caixa de diálogo. Vários tipos podem ser ativados simultaneamente.

### Tolerância geométrica

O Construtor usa uma tolerância de **0,01 unidades de mapa** para verificar a concordância geométrica entre nós e elementos de limite. Os nós que não correspondem exatamente à rede, mas estão dentro deste intervalo, são considerados conectados.

---

## Tópicos gerados

Para cada setorização, o Builder pode gerar até **6 tipos de tópicos**:

| Tema | Geometria | Descrição |
|------|-----------|-------------|
| **Frontiers** | Linhas | Elementos de fronteira entre setores adjacentes |
| **Links** | Linhas | Tubulações e ligações internas de cada setor |
| **Nodes** | Pontos | Nós da rede com o campo `SectorId` atribuído |
| **Polygons** | Polígonos | Envelope geométrico convexo de cada setor |
| **MultiLinks** | Multilinha | Todos os links de um setor mesclados em uma única geometria por setor |
| **MultiNodes** | Multiponto | Todos os nós de um setor mesclados em uma única geometria por setor |

Os temas a serem gerados são selecionados individualmente com caixas de seleção antes de clicar em **Construir**. Pelo menos um tópico deve estar ativo.

---

## Validações de integridade

Antes de gerar os setores, o Builder executa **7 verificações de integridade**:

1. A rede possui pelo menos um nó.
2. Existem elementos de borda do tipo selecionado.
3. Não existem nós isolados (sem conectividade).
4. Os elementos de borda possuem os campos necessários atribuídos.
5. Não existem setores vazios (sem nós).
6. Cada nó pertence exatamente a um setor.
7. Os polígonos gerados não se sobrepõem.

Se alguma validação falhar, a caixa de diálogo exibirá uma mensagem de erro descritiva e não gerará as camadas.

---

## Resultado no projeto

As camadas para cada setorização são criadas dentro do grupo **Camadas Auxiliares > Setores de Demanda > [nome da setorização]** no painel de camadas do QGIS. Cada camada do tipo Nodes inclui o campo `SectorId` que pode ser usado diretamente no **Nodal Demand Builder** para atribuir padrões ou eficiências por setor.

### Uso no Construtor de Demanda Nodal

Uma setorização gerada com o Demand Sector Builder pode ser selecionada no Nodal Demand Builder através da opção **"Usar tema de setores do projeto"**, evitando a necessidade de importação de uma PCH externa. Veja [Demandas e cenários](demandas-e-cenarios.md) para mais detalhes.

---

## Fluxo de trabalho típico

1. **Definir bordas**: na camada Tubulações (ou Medidores), marque como borda os elementos que delimitam os setores (campo `IsFrontier` ou equivalente, ou por seleção).
2. **Abra o Construtor**: Ferramentas → Construtor do Setor de Demanda.
3. **Criar setorização**: pressione +, dê um nome e selecione os tópicos a serem gerados.
4. **Executar**: pressione **Construir**. As camadas aparecem em Camadas Auxiliares > Setores de Demanda.
5. **Uso no Nodal Demand Builder**: Na seção padrões setoriais ou eficiências, escolha a nova setorização como tema do projeto.
