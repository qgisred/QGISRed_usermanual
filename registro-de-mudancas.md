# 📜 Registro de alterações

Mantenha-se atualizado com as últimas melhorias do QGISRed.

### Versão 0.19

**Notícias**:

* Reestruturação completa do painel Estatísticas: novas abas Setup/Relatório, histograma com janela flutuante e seletor de estatísticas no eixo Y, e segunda classificação cruzada com matriz de resultados.
* Novas opções de exibição no painel Resultados: tamanho proporcional ao valor em nós e tubulações e contorno preto opcional em marcadores de nós.
* Rótulos de mapa aprimorados: mostram o tipo e ID do item na primeira linha e o valor com unidades na segunda.
* Dicas de ferramentas do mapa visíveis em todas as camadas ativas gerenciadas pelo QGISRed, independentemente da camada selecionada na legenda.
* Evolução rápida do tempo diretamente do dock Resultados, sem a necessidade de abrir o painel Séries Temporais.
* Melhorias no painel Séries Temporais: novas magnitudes de RNVs (Volume e TankSpill), cursor sincronizado com a tabela de valores, cópia da tabela com cabeçalho duplo (nome e unidade), exportação e importação da configuração do gráfico e suporte para múltiplas janelas simultâneas.
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

