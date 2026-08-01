# Resumo da barra de ferramentas

Uma visão geral de tudo o que o QGISRed pode fazer, organizado por barra de ferramentas.

---

## 🗂️ Geral — Gerenciamento de Projetos

Ponto de entrada para qualquer sessão de trabalho. A partir daqui você cria, abre ou importa projetos.

| Ferramenta | O que isso faz |
|-------------|----------|
| **Gerente de Projeto** | Lista de projetos recentes, clonar, renomear, excluir |
| **Projeto aberto** | Abra um projeto existente indicando nome e pasta |
| **Criar projeto** | Gere a estrutura do arquivo SHP para uma nova rede |
| **Importar projeto** | Criar um projeto a partir de um arquivo EPANET `.inp` ou de PCHs externas |

---

## 📋 Projeto — Configurações e camadas

Ferramentas abertas de gerenciamento de projetos.

| Ferramenta | O que isso faz |
|-------------|----------|
| **Resumo** | Mostra a quantidade de elementos de cada tipo na rede |
| **Adicionar dados por importação** | Importe elementos adicionais para o projeto já aberto |
| **Gerenciador de camadas** | Controla quais camadas estão ativas; recuperar camadas excluídas acidentalmente |
| **Editor de legendas** | Personalize a simbologia de qualquer camada do projeto |
| **Opções de Projeto** | Configurar opções do EPANET: unidades, fórmula de perda, qualidade |
| **Valores padrão** | Define prefixos de ID, tolerâncias geométricas e valores hidráulicos iniciais |
| **Tabela de materiais** | Gerenciar a lista de materiais com sua rugosidade inicial e incrementos de idade |
| **Salvar mapa** | Salve o projeto QGIS (`.qgz`) |
| **Fechar projeto** | Feche o projeto atual |

> 💡 A exportação do projeto (ZIP portátil) não está mais nesta barra: é feita a partir do botão **Exportar** do Gerenciador de Projetos (ver [Salvar, exportar e fechar projeto](../projeto-ativo/salvar-exportar-fechar.md)).

---

## ✏️ Edição — Criação e edição de redes

Ferramentas para desenhar e modificar a topologia da rede diretamente no mapa.

| Ferramenta | O que isso faz |
|-------------|----------|
| **Adicionar tubo** | Desenhe um cano; cria automaticamente nós extremos |
| **Adicionar RNV** | Converte um nó existente em RNV (Tank) |
| **Adicionar RNF** | Converte um nó existente em RNF (Reservoir) |
| **Inserir válvula** | Divida um tubo e insira uma válvula |
| **Inserir bomba** | Divida um tubo e insira uma bomba |
| **Selecionar elementos** | Seleção múltipla de nós e linhas |
| **Mover nós** | Mova um nó arrastando-o; mantém conectividade |
| **Editar vértices** | Adicionar, mover ou excluir vértices intermediários de um tubo |
| **Link reverso** | Alterar a direção do fluxo de referência em tubulações/válvulas/bombas |
| **Dividir / Unir tubos** | Divida um tubo em um ponto ou junte dois tubos consecutivos |
| **Dividir/Mesclar nós** | Separe um nó em dois ou mescle nós sobrepostos |
| **Criar/Reverter T** | Criar ou interromper uma conexão em T sobre um tubo existente |
| **Criar/reverter crossover** | Gerenciar cruzamentos entre tubulações sobrepostas geograficamente |
| **Mover válvula/bomba** | Reposicionar uma válvula ou bomba em outro tubo |
| **Alterar status** | Modifica o estado inicial (Aberto/Fechado/CV) de tubulações, válvulas e bombas |
| **Excluir itens** | Excluir elementos selecionados e reconstruir a conectividade |
| **Editar propriedades** | Abra o formulário de atributos de um elemento |
| **Padrões e curvas** | Gerenciar curvas de demanda, eficiência e fluxo de cabeça |
| **Controles e regras** | Definir controles simples e regras baseadas em condições |

---

## 🐛 Debug — Verificação e depuração

Ferramentas para garantir a integridade topológica e de atributos do modelo.

| Ferramenta | O que isso faz |
|-------------|----------|
| **Consolidar e revisar dados** | Verifique e consolide todos os atributos; gera um relatório de incidente |
| **Remover elementos sobrepostos** | Detectar e excluir tubos ou nós duplicados na mesma posição |
| **Simplifique os vértices do link** | Elimina vértices redundantes em trechos retos |
| **Junte-se a tubos consecutivos** | Mescla tubos adjacentes com mesmo diâmetro, material e ano de instalação |
| **Criar conexões T** | Criar nós de conexão onde os tubos se cruzam sem um nó comum |
| **Verifique a conectividade** | Analise a conectividade da rede e identifique áreas isoladas |
| **Eliminar áreas isoladas** | Exclui subzonas sem conexão com nenhuma fonte de pressão |
| **Verifique os comprimentos** | Detecta tubos muito curtos ou longos em relação aos limites definidos |
| **Verificar diâmetros** | Verifique se os diâmetros estão dentro dos limites válidos |
| **Verificar materiais** | Detecta tubos sem material atribuído |
| **Verificar datas** | Verifique a consistência nas datas de instalação |
| **Setores hidráulicos** | Calcula e visualiza os setores da rede (H-Q, H-nQ, nH-Q, nH-nQ) de acordo com sua relação com fontes e nós de demanda |

---

## 🔧 Ferramentas — Ferramentas de cálculo

Utilitários para automatizar tarefas de preparação e gerenciamento de modelos.

| Ferramenta | O que isso faz |
|-------------|----------|
| **Calcular comprimentos** | Recalcular os comprimentos dos tubos a partir da sua geometria |
| **Interpolar dimensões** | Atribui dimensões aos nós de um MDT no formato `.asc` |
| **Atribuir rugosidade** | Calcular o coeficiente de rugosidade em função do material e da idade |
| **Converter rugosidade** | Transforme os coeficientes de rugosidade entre as fórmulas (D-W ↔ H-W ↔ CM) |
| **Gerenciador de reclamações** | Distribuir consumo entre nós de polígonos de área ou pontos georreferenciados |
| **Construtor de cenário** | Exporte e importe parâmetros do modelo (rugosidades, demandas, dimensões, estados, qualidades) em massa para gerenciar variantes sem duplicar projetos |
| **Segmentos isolados** | Calcular os segmentos que seriam isolados quando cada válvula de corte fosse fechada |
| **Setores de demanda** | Gera setores com base em padrões de demanda e consumo |
| **Árvore de custo mínimo** | Calcula a árvore geradora de resistência hidráulica mínima de um nó de origem selecionado |

---

## 🔍 Consultas — Consultas

Ferramentas de consulta e inspeção de modelos sem modificar seus dados.

| Ferramenta | O que isso faz |
|-------------|----------|
| **Pesquisar item por ID** | Localize e selecione qualquer elemento com base em seu identificador |
| **Propriedades do elemento** | Mostra todas as propriedades de um elemento ao clicar nele |
| **Mapas temáticos** | Gere camadas de exibição temáticas por qualquer atributo numérico |
| **Consultas sobre imóveis** | Filtra elementos que atendem às condições de seus atributos |
| **Estatísticas** | Calcula estatísticas descritivas de qualquer campo numérico |

---

## 📊 Análise — Simulação e resultados

Ferramentas para executar simulação hidráulica e explorar os resultados.

| Ferramenta | O que isso faz |
|-------------|----------|
| **Executar modelo** | Inicie a simulação EPANET e carregue os resultados como camadas |
| **Visualizador de resultados** | Abra o painel lateral para explorar variáveis ​​ao longo do tempo |
| **Relatório de status** | Apresenta o relatório de texto gerado pelo EPANET |
| **Opções de análise** | Configurar hidráulica, qualidade, tempos e energia |
| **Série temporal** | Representa graficamente a evolução temporal de um elemento |
| **Exportar resultados** | Exporte todos os resultados para arquivos CSV |
| **Exportar para INP** | Gera um arquivo `.inp` compatível com EPANET |

---

## 🧬 Gêmeo Digital — Gêmeo Digital

Elementos avançados para representar a infraestrutura de rede real.

| Ferramenta | O que isso faz |
|-------------|----------|
| **Adicionar conexão** | Criar uma ligação de serviço da rede a um ponto de consumo |
| **Adicionar válvula de corte** | Incorpora válvulas seccionadoras manuais na rede |
| **Adicionar medidor** (submenu) | Adicione diferentes tipos de sensores: medidor de vazão, manômetro, contador, nível, qualidade, energia, status, abertura, tacômetro |
| **Carregar leituras** | Importe leituras reais de sensores para calibração ou comparação |
| **Estado inicial das válvulas** | Aplica o estado real das válvulas de corte como estado inicial do modelo |
| **Carregar dados do campo** | Importar dados georreferenciados de campanhas de capacidade |
| **Converter conexões** | Transformar as conexões em tubulações e nós de demanda do modelo |
