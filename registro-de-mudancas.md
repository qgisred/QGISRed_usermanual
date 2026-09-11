# 📜 Registro de alterações

Mantenha-se atualizado com as últimas melhorias do QGISRed.

### Versão 0.19

**Interface do usuário**:

* Agrupamento de opções informativas como Notícias, Incidentes, Manual, Avaliação, Assinaturas e Sobre... em uma nova entrada de Informações no menu principal.
* Relocação do menu Consultas para trás do menu Ferramentas, na barra de menu principal.
* Incorporação de uma marca e um prefixo no título de todos os painéis QGISRed para diferenciá-los dos demais.
* Incorporação de um ícone de aviso nas camadas que podem ficar desatualizadas quando são feitas alterações nos dados.

**Gerente de Projeto**:

* Agora você pode alterar de forma independente o nome do projeto QGISRed e o nome do arquivo que contém as informações do mapa (qgz).
* Ao mover um projeto, você pode mover os dados e o arquivo de mapa (qgz) juntos ou independentemente para pastas diferentes.
* A opção de fazer backup do projeto foi removida, e substituída pela opção de Exportar o projeto, com mais alternativas.
* Ao exportar um projeto, você pode escolher os grupos de camadas QGISRed e as camadas externas ao projeto (cartografias, MDT, etc.) para copiar, entre aquelas presentes no painel de camadas. Tudo isso é salvo em um único arquivo .zip.
* Para exportar o arquivo qgz do mapa, ele deve estar na mesma pasta do projeto ou em um nível superior. As informações cartográficas deverão estar em pastas paralelas à pasta do projeto.
* Ao importar um projeto QGISRed, todas as informações exportadas anteriormente são restauradas para uma nova pasta, mantendo a estrutura de todos os arquivos.

**Importação de formas**:

* Possibilidade de selecionar as tubulações candidatas para conectar as conexões que partem dos pontos de consumo importados.

**Tabelas de materiais**:

* Declaração de uma tabela de materiais padrão diferente para cada um dos quatro idiomas suportados.
* Novas opções na caixa de diálogo de edição de tabelas de materiais, para copiar, carregar e editar novas tabelas em nível global, antes de criar um projeto ou dentro dele.
* Novas opções para escolher a tabela de materiais desejada ao criar um novo projeto ou importar arquivos de formas pela primeira vez.

**Gerenciamento de camadas**:

* Criação de um novo grupo de camadas denominado AuxiliaryLayers para hospedar temas complementares aos temas básicos.
* Criação de um subgrupo dentro do grupo de Camadas Auxiliares, denominado Construtor de Consumos, para hospedar temas próprios: setores, demandas específicas e links.
* Adicionando uma nova aba ao Gerenciador de Camadas para criar, excluir, carregar ou baixar camadas auxiliares vinculadas ao Construtor de Consumos.

**Edição gráfica**:

* Bater a varinha em uma bomba, válvula ou tubo agora alterna apenas entre os estados aberto e fechado.
* Para alternar entre o estado ativo ou fechado de uma válvula, ou declarar um CV em um tubo, segure a tecla Ctrl ao clicar com a varinha.
* Ao inserir uma bomba ou válvula em uma seção menor que a separação estabelecida entre os nós extremos, eles se mantêm e não se movem mais.
* Ao mover um nó nenhuma camada fica aberta, evitando conflitos com outras ferramentas de edição.
* Revisada a ferramenta de edição de vértices para torná-la mais fácil de usar.
* Ao dividir um tubo em um ponto intermediário, o Id é dividido adicionando um sufixo numérico. O Id original pode ser recuperado se as seções forem mescladas na direção oposta à qual os nós intermediários foram criados.
* Quando dois tubos em série não podem ser unidos eliminando o nó intermediário, a causa é informada.
* Revisada a ferramenta de mesclagem ou separação de nós, permitindo maior separação entre eles.
* A criação de uma conexão em T agora estende a última seção do ramal até que ela cruze com o tubo principal.
* Revisadas as ferramentas de desfazer T e cruzar, removendo algumas restrições e padronizando ações do mouse.

**Edição de propriedades de grupo**:

* Nova opção de menu Editar para editar as propriedades dos elementos do grupo.
* Pré-seleção gráfica dos elementos a serem modificados com múltiplas ferramentas de seleção.
* Aplicação de filtros para restringir os elementos a modificar, dependendo do tipo de imóvel.
* Opção para exibir os elementos que serão modificados no mapa.
* Múltiplas opções para modificar a propriedade escolhida, diferenciando se a propriedade é numérica, textual ou enumerada.
* Visualize na tabela de atributos as alterações realizadas antes de consolidá-las.

**Mapas temáticos**:

* Incorporação de novos mapas temáticos vinculados às tubulações: Ano de instalação, idade e coeficiente de rugosidade conforme fórmula de perda.
* Novos mapas temáticos vinculados aos entroncamentos: Elevações e Demanda Base Total graduados por tamanho.
* Ao criar o mapa de materiais, cada material agora recebe sua própria cor com base em sua abreviatura e idioma, que é editável.
* Quando um mapa temático fica desatualizado devido a uma mudança nas unidades ou na fórmula de perda, um ícone de aviso é exibido e pode ser atualizado clicando nele.

**Editor de legendas**:

* Melhorias nos assistentes para criar automaticamente intervalos, tamanhos e cores para definir a legenda para todas as camadas.
* Possibilidade de modificar alguns parâmetros de estilo dos temas básicos do grupo Dados.
* Incorporação ao Editor de Legendas do QGISRed das camadas criadas pelas Consultas (mapas temáticos, setores hidráulicos, árvores, etc.).
* Adicionadas camadas de resultados ao Editor de legendas para personalizar seu estilo.
* Opção para salvar legendas no nível do projeto ou no nível do usuário para aplicá-las a novos projetos.
* Opção de armazenar assistentes para adaptar a legenda aos dados, em vez de salvar uma legenda pré-configurada.
* Criação de uma biblioteca QGISRed de símbolos, rampas e paletas de cores, acessíveis no Editor de Legendas e editáveis ​​no QGIS.

**Construtor de Consumos**:

* Opção de consolidação dos parâmetros importados relativos à atribuição de demandas por setores em um tema QGISRed.
* Opção de distribuição da demanda global ou por setores com base nos diâmetros que convergem nos nós candidatos.
* Opção de declaração de consumo por trechos lineares ou por polígonos, como alternativa ao consumo específico.
* Opção de consolidação de consumos específicos importados em tema QGISRed.
* Opção de gerenciar temas de consumo específicos e agregar diversas demandas ao mesmo tema.
* Reconhecimento de diversas unidades na declaração do consumo a ser importado.
* Opção de atribuir demandas específicas às extremidades do tubo mais próximo em vez de procurar diretamente os nós mais próximos.
* Opção de considerar ou não as extremidades das bombas e válvulas como possíveis nós de demanda.
* Opção de distribuição de demandas específicas em função dos diâmetros das tubulações que convergem nos nós, ou em combinação com sua distância dos pontos de consumo.
* Notificação de nós carregados que estão a mais de uma determinada distância dos pontos de consumo.
* Possibilidade de edição e reaproveitamento de links entre pontos de consumo e nós de demanda.
* Atribuição de demandas aos nós com base nas conexões declaradas como elementos do Gêmeo Digital.
* Diferenciação das demandas base por categorias, tanto em consumo específico quanto por conexões, criando múltiplas demandas nos nós.
* Opção de carregar demandas apenas dos setores, pontos de consumo ou ligações selecionados.
* Opção de utilizar tema próprio para atribuir eficiências e padrões por setor, importar seus valores e editá-los.
* Opção de aplicar eficiências hidráulicas e atribuir padrões de demanda por categorias.
* Opção de reajustar eficiências e padrões declarados em um nível pelos impostos em outro nível superior (categorias -> setores -> globais).

**Painel de estatísticas**:

* Nova opção no menu Consultas para realizar todos os tipos de estatísticas com os dados e resultados do modelo.
* Avaliação das estatísticas de uma grandeza, classificadas por faixas ou classes dessa grandeza ou outra grandeza do mesmo tipo de elemento.
* Capacidade de usar uma segunda magnitude de classificação para criar tabelas de dupla entrada.
* Possibilidade de aplicar filtros nos dados iniciais e visualizar no mapa os elementos afetados pela consulta.
* Exibição de estatísticas em histogramas ou através de tabela de valores exportável.
* Exportação da configuração da consulta e sua posterior importação.

**Consultas de topologia**:

* Revisadas as ferramentas Conectividade, Setores Hidráulicos e Gráficos de Árvore: novos nomes, realocação de camadas, mudanças de estilo, etc.
* Novo tópico para destacar demandas isoladas nos setores hidráulicos.
* Possibilidade de criar e gerenciar a existência de diversos temas para Grafos em Árvore (agora chamados de Árvores de Custo Mínimo).

**Simulação**:

* Nova caixa de diálogo de progresso para mostrar o progresso dos cálculos hidráulicos e de qualidade.
* A caixa de diálogo de progresso pode ser pausada para observar cuidadosamente o progresso dos cálculos.
* A caixa de diálogo de progresso pode ser omitida para maior velocidade nos cálculos, exceto para redes com longos tempos de processamento.

**Painel de resultados**:

* Opção de mostrar todos os momentos de cálculo no mapa de resultados e outros painéis em que o tempo intervém.
* Opção de mostrar o momento da simulação em vários formatos: tempo decorrido desde o início (em horas acumuladas ou agrupadas por dias) ou tempo de calendário (em formato 24 horas ou am/pm).
* Nova barra de botões para realizar animações em velocidade controlada ou passo a passo.
* As variáveis ​​escolhidas para exibir os resultados dos nós e linhas agora estão destacadas e possuem cor própria atribuída.
* Nova aba com diversas opções para melhorar a visualização dos resultados no mapa, a simbologia e a cor de fundo.
* Nova opção para mostrar em histograma a distribuição da variável atual de nós ou linhas e seus valores acumulados, no momento atual.
* Nova opção para mostrar uma curva de evolução simplificada da variável atual de nós ou linhas, para o elemento escolhido no mapa.
* Ao resgatar o Painel de Resultados, as opções da última ação são preservadas, ao invés de aplicar as opções padrão.
* Quando os dados do cenário são alterados, as camadas resultantes exibem um ícone de aviso, que pode ser atualizado clicando nele.

**Gráficos de evolução**:

* Novos botões para navegar no gráfico das curvas de evolução.
* Novo botão com múltiplas opções para personalizar a aparência de todos os componentes do gráfico.
* Adaptação da escala temporal de acordo com as opções escolhidas no Painel de Resultados.
* Possibilidade de mostrar todos os momentos ou apenas momentos agendados, conforme escolhido no Painel de Resultados.
* Sincronização opcional do cursor com o momento atual do Painel de Resultados.
* Incorporação da evolução do volume de um tanque ou da vazão de transbordamento, como novas variáveis.
* Opção de representar as curvas de evolução de algumas variáveis ​​globais para todo o sistema.
* Novo botão para exibir em tabela os valores numéricos dos pontos de passagem das curvas de evolução e exportar seus valores para um arquivo CSV.
* Novo botão para exportar gráficos como imagens.
* Opção para salvar e recuperar configurações do gráfico de evolução, incluindo criação de modelos.
* Capacidade de criar e manter abertas diversas janelas de curvas de evolução ao mesmo tempo.

**Idiomas**:

* Todas as opções de menu, caixas de diálogo e mensagens do QGISRed agora também são exibidas em francês e português do Brasil, quando este idioma é escolhido para a interface do QGIS. Atualmente já são exibidos em inglês e espanhol.

**Outras alterações**:

* Todos os controles de segurança verificados e incidentes relacionados à qualidade do código, reportados pelo sistema QGIS Security Scan, corrigidos.
* Código da versão 0.19 verificado para compatibilidade com Qt6 e QGIS 4.xx.
* Fim do suporte para bibliotecas QGISRed em sistemas de 32 bits (x86). A partir de agora o QGISRed funcionará apenas em sistemas de 64 bits.
* Removidos os botões minimizar e maximizar em todas as caixas de diálogo incorporadas às bibliotecas.
* Revisados ​​os nomes de alguns campos em arquivos shape, tabelas dbf e arquivos CSV, para uniformidade. Todos os campos de identificação agora terminam com ID.
* Revisados ​​os nomes das propriedades exibidos em todas as caixas de diálogo do QGISRed, dependendo do idioma, para uniformidade.
* Revisados ​​os decimais apresentados nas tabelas de atributos do tópico, dependendo das unidades utilizadas.

**Correções de bugs**:

* Revisão de possíveis situações ao carregar bibliotecas GISRed para evitar tentativas repetidas.
* Revisão do formato de exportação dos arquivos INP para evitar sobreposições que causassem erros de leitura.
* Corrigido bug que impedia a criação de novas curvas de comportamento.
* Verificando se os identificadores dos elementos, curvas e padrões não contêm espaços em branco.
* Corrigido erro que impedia a consolidação do horário de início civil da simulação.
