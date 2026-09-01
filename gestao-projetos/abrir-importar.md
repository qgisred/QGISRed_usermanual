# Abrir e Importar Projetos

QGISRed oferece três maneiras de começar a trabalhar com uma rede existente:

| Opção | Quando usar |
|--------|---------------|
| **Projeto aberto** | O projeto já foi criado com QGISRed e seus arquivos SHP estão em disco |
| **Importar projeto** | Você possui um arquivo EPANET `.inp`, SHPs externos sem estrutura QGISRed ou um ZIP previamente exportado com QGISRed |
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

> 💡 A maneira mais rápida de abrir um projeto conhecido é **clicar duas vezes** em [Gestor de projeto](gestor-projetos.md). A opção “Abrir Projeto” é para projetos que não aparecem nessa lista.

---

## Importar projeto

**Barra Geral → Importar projeto**

Converta dados externos em um projeto QGISRed ou recupere um projeto exportado anteriormente. Suporta três formatos de entrada:

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
- Todos os elementos da rede (junções, tubagens, RNVs, RNFs, válvulas, bombas)
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

> Se a camada de conexão for **pontos** (cada conexão é conectada ao tubo principal mais próximo, em vez de já ter seu próprio layout), duas restrições opcionais aparecem para decidir a quais tubos cada conexão pode ser conectada — combináveis ​​entre si:
> - **Somente tubos com diâmetros abaixo deste valor são candidatos** (nas unidades de diâmetro do projeto).
> - **Apenas os tubos atualmente selecionados na camada Tubulações são candidatos** — disponível apenas se você já tiver tubos selecionados no mapa antes de abrir o importador; A caixa mostra quantos estão selecionados.
>
> Uma conexão que não encontra nenhum cano candidato dentro dessas restrições não é importada e o QGISRed indica isso no resumo de importação.

Os demais elementos (válvulas, bombas, RNVs, RNFs, nós, válvulas de isolamento, medidores) possuem seus próprios conjuntos de campos mapeáveis.

Quando a importação cria um novo projeto, também são solicitados o **catálogo de materiais** (igual ao criar um projeto do zero) e os parâmetros básicos do EPANET (unidades e fórmula de queda de pressão). Se importados sobre um projeto existente, esses parâmetros serão ignorados.

> 💡 O campo **Material** de tubos e conexões é cruzado com o catálogo de materiais do projeto para estimar automaticamente a rugosidade com base na idade do tubo.

### Importe um projeto QGISRed exportado (ZIP) {#import-zip}

Recupera um projeto empacotado com o botão **Exportar** de [Gestor de projeto](gestor-projetos.md) — veja [Salvar, exportar e fechar projeto](../projeto-ativo/salvar-exportar-fechar.md). Também reconhece ZIPs gerados por versões anteriores do plugin, mesmo que não possuam o manifesto interno das exportações atuais.

<figure><img src="../assets/images/general/importar-proyecto-qgisred.png" alt="Aba QGISRed project da caixa de diálogo de importação"><figcaption><p>Aba QGISRed project da caixa de diálogo de importação</p></figcaption></figure>

1. Na aba **Projeto QGISRed**, pressione o botão **...** próximo a **Arquivo ZIP:** e selecione o arquivo `.zip`.
2. QGISRed inspeciona o conteúdo ZIP sem extraí-lo ainda e exibe um resumo no campo:
- **Projeto:** nome da rede que contém o ZIP (substitui qualquer nome digitado anteriormente; o campo do nome do projeto fica oculto nesta aba).
- Se o ZIP incluir o mapa QGIS, indicar o arquivo `.qgz`/`.qgs`; Caso não esteja incluído avisa que apenas os dados serão importados.
- Se o ZIP incluir dados complementares (cartografia de fundo, MDT, etc.), indicar quantos elementos e seu tamanho total.
3. Caso o ZIP inclua dados complementares, será exibida a caixa **Importar os dados complementares incluídos no arquivo ZIP**, marcada por padrão. Desmarque se não quiser trazê-los.
4. A caixa de seleção **Criar automaticamente uma subpasta para este projeto** decide se o projeto será colocado em uma subpasta com o nome da rede dentro da pasta de destino:
- Se o ZIP já contém sua própria pasta de projeto (foi exportado junto com os dados de suporte em pastas irmãs), o QGISRed desmarca e desabilita automaticamente esta caixa - aninhá-lo em outra pasta quebraria os caminhos relativos para esses dados.
- Caso contrário, você pode marcá-lo ou desmarcá-lo livremente.
5. Pressione **Importar do projeto**.

Se o ZIP não for um projeto QGISRed válido, o QGISRed indica isso sem realmente importar nada:

| Situação | Mensagem |
|-----------|---------|
| O ZIP não contém um projeto QGISRed reconhecível | _"O arquivo ZIP não contém um projeto QGISRed válido"_ |
| O ZIP foi gerado com uma versão do QGISRed mais recente que a instalada | _"Este arquivo ZIP foi criado com uma versão mais recente do QGISRed. Atualize o plugin."_ |
| O ZIP contém caminhos de arquivo não seguros | _"O arquivo ZIP contém caminhos de arquivo não seguros e não será importado."_ |

> ⚠️ Se já existir um projeto com o mesmo nome (ou arquivos com o mesmo nome) na pasta de destino, o QGISRed pede confirmação antes de sobrescrevê-los.

> 💡 Se o ZIP incluir o mapa QGIS, mas você decidir não importar os dados complementares, o QGISRed avisa que algumas camadas de fundo não estarão disponíveis e permite que o QGIS solicite que você as localize.

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
