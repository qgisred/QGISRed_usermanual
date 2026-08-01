# Versões Anteriores

Aqui você pode verificar o histórico detalhado de alterações das versões anteriores do QGISRed.

### Versão 0.16
**Versões do QGis**: 3.2-3.99

**Recursos**:
* Novas opções no gerenciador de demandas nodais para declarar consumos para toda a rede ou por zonas.
* Possibilidade de exportar, editar e reimportar os links entre consumos específicos e nós.
* Novas opções para importar/exportar/excluir cenários de demanda por categorias.
* Novas ferramentas no gestor de demandas nodais para considerar a eficiência hídrica ou atribuir padrões de consumo por setores.
* Novo Gerenciador de Cenários para armazenar e recuperar vários parâmetros do modelo em massa.
* Cálculo automático do comprimento do tubo a partir das coordenadas do vértice.
* Conclusão automática do layout da conexão usando uma seção perpendicular ao tubo mais próximo ou uma ligação ao nó mais próximo.
* Possibilidade de traçar automaticamente conexões de comprimento predefinido a partir de um ponto de um tubo ou nó.
* Nova opção para refletir a correria com a ferramenta de investimento.
* Nova opção para importar conexões como pontos, criando perpendiculares às tubulações ou conexões aos nós mais próximos.
* Novo campo IsActive nas conexões para definir se está operacional ou não.
* Verificação do ponto de contato de uma conexão com tubo ou nó em ambas as extremidades.
* Antes de calcular a setorização hidráulica, agora é transmitido o estado das válvulas manuais.
* Na exportação para o INP o coeficiente de perdas das válvulas de corte é transmitido às tubulações.
* Declaração, edição e eliminação de contadores de vários tipos, como novos elementos do Digital Twin.
* Editar, ler e salvar os sinais associados aos medidores.
* Nova caixa de diálogo para leitura dos dados do campo e exportação para CSV daqueles correspondentes ao intervalo de simulação.
* Nova opção de exportação de dados de campo, juntamente com o arquivo INP.
* Novos campos na caixa de diálogo de importação para importar mais informações do item.
* Nova opção para mostrar nos temas auxiliares os elementos com incidente durante a importação.
* Novos botões e novo controle deslizante no painel de resultados.
* Melhorias nos rótulos para exibição dos resultados.
* Novo tipo de resultado para exibir o Status das linhas.
* Melhorias nas pesquisas do editor de imóveis.
* Dropdown com caminhos executáveis ​​do EPANET ao exportar INP para abertura automática.
* Classificando padrões por tipo ao importar INP.
* Novo aviso quando o Id de algum elemento é preenchido automaticamente.
* Alterações na ordem da barra de ferramentas, nomes e ícones e estilos visuais.
* Novo link para o site QGISRed na janela de informações.

**Correções**:
* Corrigida a leitura e edição da curva Id nas válvulas GPV.
* Corrigido erro ao atribuir valores padrão na importação de coeficientes de reação.
* Corrigido erro e mensagem na leitura de fontes poluidoras em RNVs e RNFs.
* Corrigido problema com ferramentas de seleção específicas.
* Corrigido erro na criação em massa de conexões T.
* Corrigidos erros na seleção múltipla e de polígonos com diferentes CRS.
* Corrigido bug com ajuste no QGIS 3.26.

---

### Versão 0.15
**Versões do QGis**: 3.2-3.99

**Recursos**:
* Gerenciamento manual de válvulas (importação, criação, exclusão, edição de propriedades, interação com o estado das tubulações...).
* Nova ferramenta para alteração do estado de elementos lineares e válvulas manuais.
* Nova simbolização de tubulações, bombas, válvulas de regulação e manuais de acordo com seu estado.
* Cancelamento de demandas isoladas por fechamento de tubulações ou válvulas sobrepostas durante simulações.
* Atribuição de demandas aos nós com base em setores de demanda e demandas específicas, com diversas opções.
* Melhorias na janela de edição de propriedades (seleção múltipla, elementos conectados, elementos visitados, elemento centralizado selecionado).
* Revisão e ampliação de opções de análises (hidráulica, qualidade, tempos e energia).
* Incorporação dos novos parâmetros Epanet 2.2 às formas (transbordamento de RNV, demandas dependentes de pressão).
* Botões/menus da barra de ferramentas principal em destaque.
* O idioma padrão e único é o inglês (por enquanto).
* Melhor edição de regras (com horários e horários).

**Correções**:
* Corrigido erro ao escrever valores de demanda com mais de 4 dígitos.
* Corrigido bug com rótulos de tempo para seleção de resultados.
* Corrigido erro ao converter números em interpolação de dimensão.
* Corrigidos erros de leitura, escrita e ordem das regras.
* Corrigido erro com regras utilizando vírgula como separador decimal.
* Corrigido problema na atribuição da projeção do projeto.
* Corrigido erro ao editar propriedades trabalhando com camadas raster.

---

### Versão 0.14
**Versões do QGis**: 3.2-3.99

**Recursos**:
* **Corrigido erro grave** ao ler metadados de modelos anteriores que impediam trabalhar com eles.
* Corrigido erro ao instalar o plugin sem possuir dependências anteriores.
* Corrigido erro com formato de hora em leis de controle simples.
* Exibição do separador decimal definido pelo usuário.
* Nova ferramenta para editar a geometria das conexões.
* A opção hidráulica `demand multiplier` agora suporta decimais.
* Prioridade dos elementos Digital Twin na seleção de objetos.

---

### Versão 0.13
**Versões do QGis**: 3.2-3.99

**Recursos**:
* Novo menu para agrupar ferramentas Digital Twin.
* Criação de conexões com ferramenta própria e integração em exclusão.
* Aba específica para edição de propriedades de conexão.
* Upload de leitura remota em diferentes formatos para conexões ou nós.
* Incorporação de curvas de modulação de conexão ao editor geral.
* Novo gerenciador de demandas para importação/exportação e exclusão seletiva.
* Tempos de acesso aprimorados a propriedades em grandes redes.
* Opcional abertura do INP no EPANET após exportação.
* Novas opções para definir unidades e fórmulas de perda de pressão do GIS.
* Formato de hora corrigido para permitir dias.
* Corrigida leitura de datas em metadados e diversos erros de importação de SHP.

---

### Versão 0.12
**Versões QGis**: 3.14-3.99

**Recursos**:
* Edição da tabela de rugosidade dos materiais para cálculo por material e idade.
* Nova importação e exportação de padrões/curvas em formato CSV.
* Importação de demandas base e IDs de curvas de CSV.
* Importação de conexões da SHP.
* Nova ferramenta para obtenção da árvore de resistência mínima.
* Atualização da biblioteca Epanet para **versão 2.2**.
* Melhorou a interface de conversão do coeficiente de rugosidade.
* Correções de bugs em resultados de qualidade e nós sem coordenadas.
* Inserção de válvulas/bombas evitando comprimentos negativos.

---

### Versão 0.11
**Versões do QGis**: 3.2-3.99

**Recursos**:
* Arquivo JSON local para projeções (.prj) sem internet.
* Leitura de formatos PUMPS herdados do Epanet 1.1.
* Novo instalador único (x86 e x64).
* Exibição de unidades e fórmula de perda na barra de status.
* Estimativa de rugosidade por idade/material compatível com diversas fórmulas.
* Ferramenta para criar cópia de segurança do projeto.
* Correções de bugs no QGIS 3.14.15 e formato AM/PM.

---

### Versão 0.10
**Versões do QGis**: 3.0-3.14.1

**Recursos**:
* Escrevendo cabeçalhos INP em inglês.
* Validação para evitar o mesmo nó final nas linhas.
* Simplificação de vértices duplicados em pontos iniciais.
* Unificação de metadados no arquivo `_Metadata.txt`.
*Aviso de novas versões disponíveis.
* Controle de visibilidade da camada usando `LayerManagement`.
* Separação entre Importar (sem projeto) e Adicionar (com projeto).
* Tolerância espacial ao adicionar dados de PCHs.
* Manual inclui formato ASCII para interpolação e classificação de setores hidráulicos.

---

### Versão 0.9
**Versões QGis**: 3.0-3.99

**Recursos**:
* Novo logotipo QGISRed.
* Criação ágil de tubulações, RNVs e RNFs com ancoragem.
* Edição de caminho (mover, criar, excluir vértices).
* Inversão de orientação de linha.
* Ferramentas para dividir/unir tubos e nós.
* Criando/desfazendo conexões T e crossovers.
*Deslocamento de válvulas e bombas.
* Seleção múltipla (Ctrl adiciona, Shift remove) e exclusão por polígono.
* Acesso aos últimos resultados sem simular novamente.

---

### Versão 0.8
**Versões QGis**: 3.0-3.99

**Recursos**:
* Edição de propriedades através de uma janela de diálogo com um navegador.
* Inserção/remoção inteligente de válvulas e bombas em tubulações.
* Edição do layout movendo nós e elementos coincidentes.
* Suporte para 5 categorias de ferramentas.
* Diálogos para opções de cálculo e valores padrão.
* Verificação de IDs repetidos.
* Ocultando tabelas de dados na legenda.
* Visualização de resultados utilizando rótulos fixos.

---

### Versão 0.7
**Versões QGis**: 3.0-3.99

**Recursos**:
* Tabela resumo do modelo.
* Gerenciador de Curvas de Modulação (Padrões): editar, criar, clonar, exportar/importar.
* Behavior Curve Manager: suporte para 1 ou 3 pontos com equação aproximada.
* Gerenciador de controles simples e interativos.
* Gerenciador de regras: combinação interativa de condições OR/AND.

---

### Versão 0.6
**Versões QGis**: 2.0-3.99

**Recursos**:
* Gerenciamento de projetos (abrir, criar, importar, clonar, excluir).
* Criação de camadas vetoriais SHP para elementos base EPANET.
* Importação de dados do INP ou PCHs.
* Validação de modelo e relatório de bugs.
* Exportação para INP com abertura automática opcional.
* Simulação com EPANET Toolkit.
* Ferramentas de layout (eliminação de sobreposições, conectividade, setores).
