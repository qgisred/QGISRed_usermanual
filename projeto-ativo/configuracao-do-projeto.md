# Configuração do Projeto

A barra **Projeto** agrupa três caixas de diálogo de configuração que afetam o comportamento hidráulico do modelo e os valores padrão com os quais novos elementos são criados.

---

## Opções de Projeto

**Barra do projeto → Opções do projeto** (Configurações do projeto)

Abre a caixa de diálogo principal de opções do EPANET. É equivalente à seção `[OPTIONS]` do arquivo `.inp`.

<figure><img src="../assets/images/proyecto/opciones-proyecto.png" alt="Caixa de diálogo de opções do projeto: guias Hidráulica, Qualidade, Tempo e Energia"><figcaption><p>Caixa de diálogo de opções do projeto: guias Hidráulica, Qualidade, Tempo e Energia</p></figcaption></figure>
*Caixa de diálogo Opções do Projeto com suas quatro guias.*

### Aba Hidráulica

| Campo | Descrição |
|-------|-------------|
| **Unidades de fluxo** | Define o sistema de unidades do projeto. As unidades métricas (LPS, LPM, MLD, CMH, CMD) correspondem ao SI; galões e pés cúbicos (CFS, GPM, MGD, IMGD, AFD) em EUA |
| **Fórmula de perda de carga** | Darcy-Weisbach (DW), Hazen-Williams (HW) ou Chezy-Manning (CM) |
| **Gravidade específica** | Peso específico do fluido em relação à água pura (1,0 para água padrão) |
| **Viscosidade relativa** | Factor na viscosidade cinemática da água a 20 °C |
| **Precisão** | Critério de convergência do solucionador hidráulico |
| **Modelo de demanda** | DDA (Demand Driven) ou PDA (Pressure Driven) — no PDA, a demanda é reduzida se a pressão cair abaixo de um limite |
| **Pressão mínima/nominal** | Limiares para o modelo PDA |
| **Máx. iterações / proporção** | Parâmetros de convergência do solucionador |

> 💡 Alterar as **unidades de fluxo** não converte os valores já inseridos. Se a rede estiver configurada para LPS e você mudar para GPM, todos os valores de demanda, fluxo e comprimento precisarão ser atualizados manualmente.

### Guia Qualidade

| Campo | Descrição |
|-------|-------------|
| **Tipo de análise de qualidade** | Nenhum (não simula qualidade), Químico (reagente), Idade (idade da água), Traço (traçador) |
| **Etiqueta do reagente** | Nome do produto modelado (por exemplo, "Cloro") — aparecerá nos resultados |
| **Nó traçador** | Para análise do tipo de rastreamento, ID do nó de origem do rastreador |
| **Unidades de concentração** | mg/L ou μg/L |
| **Difusividade** | Coeficiente de difusão molecular relativo (1,0 para cloro em água) |
| **Tolerância** | Critério de convergência para o solucionador de qualidade |

### Guia Tempos

| Campo | Descrição |
|-------|-------------|
| **Duração da simulação** | Tempo total de simulação. Formato `HH:MM:SS` ou em horas (por exemplo, `24:00:00`) |
| **Etapa de tempo hidráulico** | Intervalo de cálculo hidráulico (normalmente 1 h) |
| **Passe de tempo de qualidade** | Intervalo de cálculo da qualidade (normalmente 5 min) |
| **Etapa de tempo do relatório** | Frequência com que os resultados são salvos (determina a quantidade de momentos disponíveis no Viewer) |
| **Hora de início da simulação** | Tempo de relógio correspondente ao instante 0 da simulação |
| **Tipo de estatístico** | Nenhum (todos os instantes), Média, Mínimo, Máximo, Faixa |

> 💡 Uma **etapa de relatório** de 1 hora em uma simulação de 24 horas gera 25 instantes de resultado (0h a 24h). Etapas mais curtas aumentam a resolução temporal, mas também o tamanho dos arquivos de resultados.

### Guia Energia

Permite definir o custo energético das bombas para análise de consumo:

| Campo | Descrição |
|-------|-------------|
| **Preço global** | Custo por kWh (em moeda definida) |
| **Padrão de preço** | Padrão temporal de variação do preço da eletricidade |
| **Eficiência geral** | Eficiência média das bombas (caso não possuam curva de eficiência individual) |

---

## Valores padrão

**Barra do projeto → Valores padrão** (Valores padrão)

Define os valores que são atribuídos automaticamente aos novos elementos quando eles são criados com as ferramentas de edição.

<figure><img src="../assets/images/proyecto/valores-defecto.png" alt="Diálogo de padrões com seções para nós, tubulações e prefixos"><figcaption><p>Diálogo de padrões com seções para nós, tubulações e prefixos</p></figcaption></figure>
*Caixa de diálogo de valores padrão: parâmetros iniciais para cada tipo de elemento.*

### Prefixos de ID

Cada tipo de item possui um prefixo configurável que é utilizado na geração automática do ID de novos itens:

| Elemento | Prefixo padrão | Exemplo de ID gerado |
|----------|---------------------|------------------------|
| Junção | J | J-1, J-2… |
| Tubo | P | P-1, P-2… |
| RNV | T | T-1, T-2… |
| RNF | R | R-1, R-2… |
| Válvula | V | V-1, V-2… |
| Bomba | BM | BM-1, BM-2… |

Os prefixos são configuráveis. O número inicial também pode ser definido.

### Valores hidráulicos iniciais

| Campo | Descrição |
|-------|-------------|
| **Diâmetro padrão** | Diâmetro (mm ou polegadas) atribuído aos novos tubos |
| **Rugosidade padrão** | Coeficiente de rugosidade de acordo com a fórmula ativa |
| **Dimensão padrão** | Cota (m ou pés) atribuída aos novos nós |
| **Demanda base padrão** | Demanda inicial dos novos nós de demanda |
| **Velocidade padrão da bomba** | Fator de velocidade relativo inicial para bombas |

### Tolerâncias geométricas

| Campo | Descrição |
|-------|-------------|
| **Tolerância a nós** | Distância máxima (m ou pés) para considerar dois pontos como o mesmo nó |
| **Comprimento mínimo para divisão** | Comprimento mínimo das secções resultantes na divisão de um tubo |
| **Comprimento máximo para divisão** | Comprimento máximo das secções resultantes na divisão de um tubo |

---

## Tabela de materiais

**Barra do projeto → Tabela de materiais** (Tabela de materiais)

Gerencie a lista de materiais disponíveis para tubos e suas propriedades de envelhecimento.

<figure><img src="../assets/images/proyecto/tabla-materiales.png" alt="Tabela de materiais: código, nome, rugosidade inicial e acréscimo anual"><figcaption><p>Tabela de materiais: código, nome, rugosidade inicial e acréscimo anual</p></figcaption></figure>
*Tabela de materiais com rugosidade inicial e aumento por ano.*

### Campos da tabela

| Campo | Descrição |
|-------|-------------|
| **Abreviatura** | Código abreviado do material (por exemplo, PVC, DI, AC) |
| **Descrição** | Nome completo (por exemplo, "Ferro Dúctil", "Cimento de Amianto") |
| **Rugosidade inicial (mm)** | Coeficiente de rugosidade D-W na data de instalação |
| **Aumento anual (mm)** | Aumento da rugosidade por ano de idade |

> ⚠️ Não pode haver dois materiais com a mesma abreviatura — se houver, o QGISRed avisa e impede o salvamento até que você corrija o repetido.

### Excluir um material

Selecione uma linha e pressione **Del** para excluí-la. Se o material for atribuído a um tubo ou conexão, o QGISRed notifica quantos elementos o utilizam e pede confirmação antes de excluí-lo — se você aceitar, esses elementos ficam sem material atribuído.

### Use com a ferramenta "Atribuir Rugosidade"

Quando você usa a ferramenta **Assign Roughnesses** da barra de ferramentas, o QGISRed pesquisa nesta tabela o material de cada tubo e calcula:

```
Rugosidad = Rugosidad_inicial + (Año_actual - Año_instalación) × Incremento_anual
```

> 💡 Você pode adicionar materiais personalizados. Os materiais definidos aqui também estão disponíveis ao criar novos tubos na barra de edição.

### Materiais incluídos por padrão

QGISRed inclui uma tabela de materiais predefinida com os mais comuns (CI, DI, AC, PVC, PE, HDPE...). Você pode editá-los ou ampliá-los de acordo com as características do seu sistema.

### Salvar e reutilizar tabelas entre projetos

A tabela de materiais é exclusiva para cada projeto, mas pode ser compartilhada com outros projetos salvando-a como uma tabela **global** (salva no perfil do usuário, fora de qualquer projeto — um `.dbf` por tabela).

**Com um projeto ativo** (janela "Materiais do Projeto"), a caixa de diálogo edita diretamente a tabela do projeto (sem menu suspenso) e oferece estes botões:

| Botão | Ação |
|-------|--------|
| **Salvar** | Fecha a caixa de diálogo e salva as alterações no projeto. |
| **Salvar como global** | Salva uma cópia da tabela atual como uma **nova** tabela global, solicitando um nome. Se já existir uma tabela global com esse nome, pede confirmação antes de substituí-la. |
| **Restaurar materiais padrão (idioma)** | Substitui a tabela do projeto pela predefinida QGISRed no idioma indicado entre parênteses (o da interface), descartando os materiais do projeto atual. |
| **Carregar Tabela de Materiais** | Substitui a tabela do projeto por outra, escolhida em uma caixa de diálogo separada que lista as tabelas globais salvas pelo usuário e as tabelas QGISRed predefinidas (marcadas como "(padrão)"). |
| **Cancelar** | Fecha a caixa de diálogo sem salvar as alterações. |

> ⚠️ Não pode haver dois materiais com a mesma abreviatura — se houver, o QGISRed avisa com uma mensagem vermelha embaixo da tabela e impede o salvamento até que você corrija o repetido. A mesma verificação se aplica ao pressionar “Salvar” e “Salvar como global”.

### Nenhum projeto ativo: gerenciador de tabelas global

Se você abrir **Tabela de Materiais** sem nenhum projeto QGISRed ativo (por exemplo, assim que você abrir o QGIS, antes de criar ou abrir um projeto), a caixa de diálogo será aberta como uma janela separada ("Tabelas Globais de Materiais") para gerenciar as tabelas globais salvas, com o rótulo **"Selecione a tabela global de materiais"** próximo a uma lista suspensa que lista todas as disponíveis:

- **Tabelas globais salvas** pelo usuário (criadas com "Salvar" ou "Salvar como..."), editáveis.
- As **tabelas predefinidas** de QGISRed por idioma, marcadas com o sufixo **"(padrão)"** — somente leitura: a grade não pode ser editada enquanto uma delas estiver selecionada.

Ao lado do menu suspenso há um botão **Excluir** que exclui a tabela global selecionada; ele está disponível apenas para suas próprias tabelas, não para tabelas predefinidas somente leitura.

Os botões abaixo mudam dependendo da tabela selecionada:

| Botão | Quando aparece | Ação |
|-------|-----------------|--------|
| **Salvar** | Somente com tabela própria selecionada (não predefinida) | Salva as alterações **na tabela já selecionada**, sem solicitar um novo nome — ao contrário de **Salvar como...**. |
| **Salvar como...** | Sempre | Solicita um novo nome e salva uma cópia como tabela global; se o nome já existir, pede confirmação antes de substituí-lo. Se for bem-sucedido, ele o adiciona ao menu suspenso e o seleciona em seguida. |
| **Restaurar materiais padrão (idioma)** | Somente com tabela própria selecionada (não predefinida) | Substitui o conteúdo da tabela atual pelo predefinido do idioma da interface. |
| **Cancelar** | Sempre | Fecha a janela. |

> ⚠️ Se você alterar tabelas no menu suspenso com alterações não salvas, o QGISRed perguntará se você deseja salvá-las antes de alterar (Sim/Não/Cancelar). Fechando a janela com "Cancelar" (ou com o X), por outro lado, nada é perguntado: como não há um botão final que confirme todas as alterações de uma vez (como há em um projeto ativo), aqui só é mantido o que você já salvou explicitamente com "Salvar" ou "Salvar como...".
