# 📜 Registro de alterações

Mantenha-se atualizado com as últimas melhorias do QGISRed.

### Versão 0.19

**Notícias**:

* Reestruturação completa do painel Estatísticas: novas abas Setup/Relatório, histograma com janela flutuante e seletor de estatísticas no eixo Y, e segunda classificação cruzada com matriz de resultados.
* Novas opções de exibição no painel Resultados: tamanho proporcional ao valor em nós e tubulações e contorno preto opcional em marcadores de nós.
* Rótulos de mapa aprimorados: mostram o tipo e ID do item na primeira linha e o valor com unidades na segunda.
* Dicas de ferramentas do mapa visíveis em todas as camadas ativas gerenciadas pelo QGISRed, independentemente da camada selecionada na legenda.
* Evolução rápida do tempo diretamente do dock Resultados, sem a necessidade de abrir o painel Séries Temporais.
* Melhorias no painel Séries Temporais: novas magnitudes de tanques (Volume e TankSpill), cursor sincronizado com a tabela de valores, cópia da tabela com cabeçalho duplo (nome e unidade), exportação e importação da configuração do gráfico e suporte para múltiplas janelas simultâneas.
* Caixa de diálogo de progresso da simulação com opção de não ser mostrada novamente (configurável nas Propriedades do Projeto).
* Melhor tratamento de erros de simulação: o relatório EPANET é exibido automaticamente no log quando ocorre um erro e os erros não tratados são registrados em vez de falharem silenciosamente.
* Aviso específico quando os arquivos de resultados são bloqueados por outro aplicativo.
* Demand Builder: reestruturação da seção de padrões por setores com dois modos exclusivos (importar SHP externo / usar camada de projeto).
* Demand Builder: seção de eficiência do setor com dois modos de trabalho e novas opções para corrigir eficiências de categoria e padrões setoriais para atender aos objetivos globais.
* Demand Builder: distribuição automática de porcentagens de demanda faltantes nas camadas de seção.
* Nova camada de ligações isoladas com demanda diferente de zero gerada pela análise de segmentos hidráulicos.
* Árvore de distribuição: O nó raiz é identificado com `NodeType = "ROOT"` na camada de nós resultante.
* Renomeação de campos identificadores nas camadas SHP do projeto (por exemplo, `Id` → `JunctionID`, `PipeID`, etc.). Os projetos criados com versões anteriores permanecem compatíveis graças à tabela de nomes herdada.
* Categoria não atribuída renomeada de "Indefinido" para **"Não categorizado"** no Demand Builder e na legenda da camada.

---

### Versão 0.18 (abril de 2026)
**Versões do QGIS**: 3.28-4.99

*Esta versão foi financiada por [Banco Interamericano de Desenvolvimento (BID)](https://www.iadb.org/es) através do contrato C-RG-T4041-P001.*

**Notícias**:
* Melhorias no Gerente de Projetos. Novos botões para mover e exportar projetos e novas opções para renomear projetos.
* Identificação de todas as camadas gerenciadas pelo QGISRed utilizando Id próprio, ao invés de por nome, o que permite trabalhar em vários idiomas.
* Revisão dos símbolos do mapa, rótulos e avisos associados a todas as camadas gerenciadas pelo QGISRed.
* Maior integração do Element Properties Editor, mantendo as propriedades das camadas e atualizando os dados em todas as janelas afetadas, incluindo a tabela de atributos.
* Armazenamento do estilo de todas as camadas gerenciadas pelo QGISRed em arquivos .qml em três níveis: padrão, nível de usuário e nível de projeto.
* Armazenamento em tabela própria de todas as grandezas gerenciadas pelo QGISRed, especificando as unidades e decimais a serem exibidas nos diferentes sistemas de unidades e conforme o caso.
* Criação de seu próprio Editor de Legendas para personalizar intervalos ou classes, cores e tamanhos de todas as legendas gerenciadas pelo QGISRed.
* Assistentes para personalizar legendas automaticamente.
* Adição de um novo menu e uma nova barra de ferramentas para abrigar as novas opções voltadas à consulta de dados e resultados.
* Reorganização das camadas do grupo Consultas, e armazenamento dos arquivos shp correspondentes na estrutura de pastas do projeto.
* Nova ferramenta para localizar qualquer elemento do mapa através de seu Id e identificar elementos conectados, com opção de navegar por eles.
* Novo painel para observar os dados e resultados de qualquer elemento de rede selecionado. Sincronização dos resultados com o momento atual da simulação.
* Nova caixa de diálogo para criar mapas temáticos de algumas magnitudes associadas aos diferentes tipos de elementos gerenciados pelo QGISRed.
* Novo painel para localizar elementos no mapa que atendam a determinados critérios em relação a dados ou resultados. Sincronização com os resultados do momento atual da simulação.
* Melhoria do formato em que o arquivo INP é exportado do QGISRed, semelhante ao que seria exportado do EPANET Toolkit.
* Substituição do motor de cálculo EPANET 2.2 pela nova versão 2.3, até à mais recente revisão 2.3.5.
* Leitura dos resultados de uma simulação diretamente dos arquivos binários do EPANET para uma navegação mais rápida e ágil.
* Incorporação do Relatório de Status ao painel de resultados em uma nova aba, sempre acessível.
* Exportação de todos os resultados da simulação para um arquivo CSV estruturado.
* Nova opção para exibir diversas estatísticas sobre os resultados ao longo de todo o período de simulação.
* Nova janela para mostrar a curva de evolução ao longo do tempo de qualquer magnitude de um elemento ao longo do período de simulação. Possibilidade de sobrepor diversas curvas de igual ou diferente magnitude.
* Melhorias no Demand Builder para demandas específicas. Revisão de algoritmos e carregamento automático de links. Novo tópico para pontos de demanda.
* Revisão da ferramenta de identificação de setores hidráulicos e detecção de consumos isolados.
* Revisão do algoritmo para identificação de fechados. Detecção de consumo isolado.
* Novas opções em nível de projeto para transferir as demandas das conexões aos nós. Classificação das demandas dos empregadores.
* Compatibilidade da versão 0.18 com novas versões do QGIS 4.0.
* Tradução de todas as caixas de diálogo, painéis, mensagens e nomes de camadas do QGISRed para o espanhol.
* Redesenho de todos os ícones gerenciados pelo QGISRed com uma aparência mais uniforme e agradável.
* Hospedagem na Web do manual provisório QGISRed em inglês e espanhol para consulta online através da plataforma colaborativa GitBook.
* Menção ao Banco Interamericano de Desenvolvimento (BID) pelo apoio financeiro de todas as melhorias realizadas nesta versão 0.18.

**Correções**:
* Resolvido problema ao carregar dados de campo relacionados ao separador decimal.
* Corrigido erro que impedia o cancelamento de demandas de áreas isoladas.
* Limitação no tamanho do campo Descrição, utilizado para reportar as demandas das conexões carregadas em cada nó.

---

### Versão 0.17 (janeiro de 2026)
**Versões do QGis**: 3.2-3.99

**Notícias**:
* Nova ferramenta de verificação fechada, com múltiplas opções.
* Exiba resultados de até 13 estados para tubos, válvulas e bombas.
* Transferência de estados e qualidades para encadeamento de simulações em períodos sucessivos.
* Novas opções para zerar rugosidades, elevações e diâmetros no construtor de cenários.
* Nova opção de exportação e importação de cenários no formato Epanet.
* Novos recursos no gerenciador de projetos (classificar, exportar, excluir e renomear).
* Novos botões para abrir ou salvar projetos.
* Nova opção para importar um projeto QGISRed.
* Alterações nos ícones e nomes em algumas opções do menu.
* Melhor precisão ao escrever valores numéricos em formas.
* Melhoria na mensagem ao baixar as dependências necessárias.

**Correções**:
* Corrigido erro ao interpolar cotas quando o ponto incide em uma das extremidades da malha.
* Corrigido erro ao distribuir demandas proporcionalmente ao comprimento das tubulações.
* Corrigido erro ao carregar demandas de uma camada de setores.
* Corrigido erro ao importar INPs com fontes sem padrão definido.
* Corrigidos erros na importação de INP relacionados a Tempos e Regras Temporárias.
* Corrigido erro ao exportar INPs com descrições muito longas.
* Corrigido erro com símbolo decimal nas opções do modelo PDA.


