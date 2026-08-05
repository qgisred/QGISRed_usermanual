# Salvar, exportar e fechar projeto

---

## Salve o mapa do projeto

**Barra do projeto → Salvar mapa** (Salvar mapa do projeto)

Salva o arquivo QGIS (`.qgz`) que contém as configurações visuais do projeto: camadas carregadas, estilos, visibilidade do grupo, enquadramento do mapa, etc.

### Primeira vez

Se o projeto QGIS ainda não tiver um arquivo `.qgz`, o plugin abre a caixa de diálogo padrão do QGIS **"Salvar como"** sugerindo automaticamente a pasta do projeto QGISRed e o nome da rede como o nome do arquivo:

```
{CarpetaProyecto}/{NombreRed}.qgz
```

### Mais tarde salva

Se já existir um `.qgz`, ele o substitui diretamente (equivalente a `Ctrl+S` no QGIS).

> 💡 **Recomendação**: salve o `.qgz` na mesma pasta das PCHs do projeto. Assim, se você copiar a pasta para outro computador, o arquivo `.qgz` encontrará os SHPs sem a necessidade de reconfigurar caminhos.

> ⚠️ Salvar o `.qgz` **não salva dados da rede**. Os dados (diâmetros, dimensões, demandas...) são salvos automaticamente no SHP+DBF quando o QGISRed os modifica. O `.qgz` salva apenas a apresentação visual.

---

## Exporte o projeto

**Gerente de Projeto → Exportar**

> ⚠️ Este botão **não está mais** na barra **Projeto**: o antigo botão _Backup do projeto_ foi removido e não tem substituto nessa barra. A exportação agora é feita a partir de [Gestor de projeto](../gestao-projetos/gestor-projetos.md) — selecione o projeto na lista (não é necessário mantê-lo aberto) e pressione **Exportar**.

Gera um arquivo ZIP portátil com o projeto: o SHP/DBF da rede, o mapa QGIS (`.qgz`) se existir, e opcionalmente os grupos de conteúdo e dados complementares (cartografia de fundo, MDT, ortofotos...) que esse `.qgz` referencia.

### Antes de exportar

Se o projeto que você exporta é aquele que você abriu no QGIS e seu `.qgz` possui alterações não salvas, o QGISRed pergunta primeiro:

> _"O projeto QGIS possui alterações não salvas. Deseja salvá-lo antes de exportar?"_

- **Sim**: salve o `.qgz` e exporte a versão recém-salva.
- **Não**: exporta o `.qgz` como estava no último save (alterações pendentes não viajam no ZIP).
- **Cancelar**: a caixa de diálogo de exportação não abre.

### A caixa de diálogo de exportação

<figure><img src="../assets/images/proyecto/exportar-proyecto.png" alt="Caixa de diálogo de exportação de projeto do QGISRed"><figcaption><p>Caixa de diálogo de exportação de projeto do QGISRed</p></figcaption></figure>

| Campo | Função |
|-------|---------|
| **Nome do arquivo:** | Nome ZIP (sem extensão); por padrão, o nome da rede |
| **Pasta:** | Pasta de destino; por padrão, a pasta Downloads do usuário |
| **Conteúdo** | Grupos opcionais a incluir (ver abaixo) |
| **Dados complementares** | Dados externos referenciados por `.qgz`, selecionáveis ​​um por um |
| **Abra a pasta que contém quando terminar** | Abra o explorador de arquivos na pasta de destino quando terminar (habilitado por padrão) |

### O que está sempre incluído

- A PCH+DBF+PRJ da rede na raiz da pasta do projeto (Tubulações, Junções, Válvulas, Bombas, RNVs, RNFs, Demandas, Fontes...) e os arquivos de opções e metadados (`_Options.dbf`, `_Title.dbf`).
- O arquivo de mapa `.qgz`, se o QGISRed o encontrar na pasta do projeto ou em sua pasta pai. Se não houver nenhum `.qgz` salvo, a caixa de diálogo avisa que a exibição do mapa não será exportada.

### O que está incluído opcionalmente

Quatro grupos de conteúdo, cada um com sua própria caixa na seção **Conteúdo** (marcada por padrão se o grupo possui dados desta rede; se vazia, a caixa fica desabilitada):

| Caixa | Conteúdo |
|---------|-----------|
| **Resultados** | Resultados da simulação salvos em `Results/` |
| **Problemas** | Incidentes detectados por verificações, em `Issues/` |
| **Consultas** | Consultas salvas, em `Queries/` |
| **Camadas Auxiliares** | Camadas auxiliares (por exemplo, do Construtor de consumos nodais), em `Auxiliary Layers/` |

Se `.qgz` fizer referência a dados complementares, a caixa de diálogo adicionará uma tabela **Dados complementares** com uma linha por camada (nome, localização e estado), cada uma com sua própria caixa de seleção — para que você possa deixar de fora, por exemplo, um MDT de vários GB sem abrir mão do resto.

### O que não está incluído

- Grupos de conteúdo que você deixa desmarcados.
- Os dados complementares que estão fora da pasta do projeto e de sua pasta pai: a caixa de diálogo os marca como _"Não exportáveis"_ e avisa antes de exportar. Para incluí-los, mova-os com o explorador de arquivos para a pasta do projeto (ou próximo a ela) e reabra o projeto para que o QGISRed os vincule novamente.
- Camadas de fundo remotas (serviços WMS, XYZ, bancos de dados): não há nada para copiar, portanto nunca bloqueiam a exportação ou aparecem na tabela.

> ⚠️ Se você deixar de fora um grupo de conteúdo ou camada complementar que `.qgz` ainda está usando, o QGISRed avisa antes de exportar. Pressione **OK** uma segunda vez se quiser continuar mesmo assim.

### Onde está salvo

```
{CarpetaDestino}/{NombreArchivo}.zip
```

Por padrão, `{CarpetaDestino}` é a pasta de downloads do usuário e `{NombreArchivo}` é o nome da rede, mas ambos são editáveis ​​na caixa de diálogo. Se já existir um ZIP com esse nome, o QGISRed pergunta se você deseja substituí-lo.

Após a conclusão, QGISRed mostra o caminho completo do ZIP criado na barra de mensagens.

> 💡 **Práticas recomendadas**: Exporte o projeto antes de operações que modificam muitos elementos de uma vez (importações em massa, alterações de CRS, conversões de rugosidade) e antes de atualizar a versão do plugin. Para recuperar um projeto exportado, use **Importar projeto → aba "Projeto QGISRed"** — veja [Abrir e importar projetos](../gestao-projetos/abrir-importar.md).

---

## Fechar projeto

**Barra do projeto → Fechar projeto** (Fechar projeto)

Feche o projeto QGISRed atual e limpe a sessão QGIS: exclua todas as camadas carregadas e restaure o estado inicial.

É equivalente a usar _Projeto → Novo_ no menu QGIS.

> ⚠️ Se houver alterações não salvas no arquivo `.qgz`, o QGIS perguntará se você deseja salvá-las antes de fechar.

---

## Resumo: o que cada opção economiza

| Operação | O que mantém | Onde |
|-----------|-----------|-------|
| Ferramentas de edição | Atributos e geometria | SHP/DBF em disco, imediatamente |
| Salvar mapa | Estilos, camadas visíveis, enquadramento | Arquivo `.qgz` |
| Exportar projeto (Gerente de Projeto → Exportar) | Rede SHP/DBF, `.qgz` e, opcionalmente, dados suplementares e grupos de conteúdo | Arquivo `.zip` na pasta de sua preferência |
