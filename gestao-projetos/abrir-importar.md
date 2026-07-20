# Abrir e Importar Projetos

QGISRed oferece três maneiras de começar a trabalhar com uma rede existente:

| Opção | Quando usar |
|--------|---------------|
| **Projeto aberto** | O projeto já foi criado com QGISRed e seus arquivos SHP estão em disco |
| **Importar projeto** | Você possui um arquivo EPANET `.inp` ou SHPs externos sem estrutura QGISRed |
| **Adicionar dados por importação** | Você já tem um projeto aberto e deseja incorporar dados adicionais |

---

## Abrir projeto

**Barra Geral → Abrir projeto**

Abre um projeto QGISRed existente (criado anteriormente com o plugin) que não aparece no Gerenciador de Projetos ou que foi movido de uma pasta.

<figure><img src="../assets/images/general/abrir-proyecto.png" alt="Caixa de diálogo de abertura do projeto"><figcaption><p>Caixa de diálogo de abertura do projeto</p></figcaption></figure>
*Caixa de diálogo de abertura: insira o nome da rede e selecione a pasta.*

### Processo

1. Digite o **nome da rede** exatamente como aparece no prefixo dos arquivos SHP (sem extensão).
2. Selecione a **pasta** onde estão os arquivos.
3. QGISRed verifica se `{nombre}_Pipes.shp` existe nessa pasta e carrega todas as camadas do projeto.

### O que acontece quando você abre

- O grupo de camadas **Inputs** é carregado com os 6 SHPs base mais quaisquer camadas auxiliares (múltiplas solicitações, fontes, etc.).
- Caso o projeto possua resultados de simulações anteriores, o grupo **Resultados** também é carregado.
- As opções do projeto (`_Options.dbf`) são lidas e o indicador de unidades na barra principal é atualizado.
- Se os estilos visuais (QML) foram alterados em relação à versão do plugin com o qual foi salvo, eles são atualizados automaticamente.

> 💡 A maneira mais rápida de abrir um projeto conhecido é **clicar duas vezes** em [Gestor de projeto](gestor-proyectos.md). A opção “Abrir Projeto” é para projetos que não aparecem nessa lista.

---

## Importar projeto

**Barra Geral → Importar projeto**

Converte dados externos em um projeto QGISRed. Suporta dois formatos de entrada:

### Importar do EPANET (`.inp`) {#importar-do-epanet}

O caso mais comum: você possui um modelo EPANET existente e deseja trabalhar com ele no QGISRed.

<figure><img src="../assets/images/general/importar-inp.png" alt="Caixa de diálogo de importação de arquivo EPANET INP"><figcaption><p>Caixa de diálogo de importação de arquivo EPANET INP</p></figcaption></figure>
*Caixa de diálogo de importação: seleção do arquivo .inp, nome da rede e pasta de destino.*

1. Selecione o arquivo `.inp`.
2. Indica o **nome da rede** que o projeto QGISRed terá (pode ser diferente do nome interno do INP).
3. Escolha a **pasta de destino** onde serão criadas as PCHs.
4. QGISRed converte todos os elementos (nós, tubos, válvulas, bombas, curvas, padrões, controles...) para a estrutura SHP+DBF.

> ⚠️ As coordenadas de `.inp` devem estar no mesmo CRS que você usará no QGISRed. O plugin não reprojeta durante a importação.

**O que é importado:**
- Todos os elementos da rede (junções, tubagens, tanques, reservatórios, válvulas, bombas)
- Curvas (H-Q, eficiência, volume, perda de pressão)
- Padrões de procura
- Controles e regras simples
- Opções de simulação (unidades, fórmula, tempos, energia, qualidade)
- Múltiplas demandas por nó


### Importação de PCHs externas

Caso você possua camadas SHP com a geometria da rede mas sem a estrutura interna do QGISRed, o importador permite mapear as colunas de atributos de cada camada para os campos esperados pelo plugin.

Para cada tipo de elemento você pode selecionar a camada SHP correspondente e atribuir seus campos aos atributos do modelo. Os campos reconhecidos automaticamente (se o nome corresponder) são pré-selecionados:

**Tubos** — campos mapeáveis: ID, Comprimento, Diâmetro, Rugosidade, Coeff. perdas, **Material**, Data de instalação, Estado inicial, Coef. reação em massa, Coef. reação da parede, Tag, Descrição.

**Serviços** — campos mapeáveis: ID, Comprimento, Diâmetro, Rugosidade, **Material**, Demanda base, Padrão, Ativo, Data de instalação, Tag, Descrição.

Os demais elementos (válvulas, bombas, tanques, reservatórios, nós, válvulas de isolamento, medidores) possuem seus próprios conjuntos de campos mapeáveis.

Quando a importação cria um novo projeto, também são solicitados o **catálogo de materiais** (igual ao criar um projeto do zero) e os parâmetros básicos do EPANET (unidades e fórmula de queda de pressão). Se importados sobre um projeto existente, esses parâmetros serão ignorados.

> 💡 O campo **Material** de tubos e conexões é cruzado com o catálogo de materiais do projeto para estimar automaticamente a rugosidade com base na idade do tubo.

---

## Adicionar dados por importação

**Barra do projeto → Adicionar dados por importação**

Disponível apenas quando já existe um projeto aberto. Permite enriquecer o projeto com dados adicionais sem fechar o que está carregado.

Casos de uso típicos:
- Incorporar uma nova zona de rede projetada em um `.inp` separado.
- Adicionar demandas para um novo banco de dados.
- Integrar dados de um setor importado de outro sistema.

O processo é o mesmo da importação, mas os itens importados são **adicionados** ao projeto existente em vez de criar um novo. QGISRed verifica se não há conflitos de ID antes de incorporar os dados.

---

## Considerações na troca de equipamento

Se você copiar a pasta do projeto para outro computador:

1. Use **Upload** no Project Manager para adicioná-lo ao histórico local.
2. Se o projeto tiver um `.qgz` salvo, abra-o normalmente no QGIS — o QGISRed o reconhecerá automaticamente.
3. Se `.qgz` não estiver lá ou os caminhos foram alterados, use **Open Project** para carregá-lo diretamente das PCHs.
