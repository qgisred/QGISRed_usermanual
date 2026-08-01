# Gerente de Projetos

**Barra Geral → Gerente de Projeto** (ou no menu QGISRed → Geral → Gerente de Projeto)

O Gerenciador de Projetos é a janela de administração central do QGISRed. Permite acesso a todos os projetos conhecidos sem a necessidade de lembrar onde estão armazenados.

<figure><img src="../assets/images/general/gestor-proyectos.png" alt="Janela do Gerenciador de Projeto QGISRed"><figcaption><p>Janela do Gerenciador de Projeto QGISRed</p></figcaption></figure>
*Janela do Gerenciador de Projetos: lista de projetos recentes e operações disponíveis.*

---

## Lista de projetos recentes

A janela mostra todos os projetos que já foram abertos neste computador. Para cada projeto, o **nome da rede** e o **caminho da pasta** são exibidos.

- **Clique duas vezes** em qualquer projeto → abre-o diretamente.
- Se houver um projeto aberto com alterações não salvas, o QGISRed solicitará confirmação antes de fechá-lo.

## Operações disponíveis

### Carregar (Carregar)

Permite adicionar à lista um projeto que não aparece no histórico (por exemplo, se o projeto foi criado em outro computador e a pasta foi copiada).

1. Pressione **Carregar**.
2. Insira o **nome da rede** (sem extensão, sem prefixo de pasta).
3. Selecione a **pasta do projeto** com o explorer.
4. O QGISRed irá verificar se o arquivo `{nombre}_Pipes.shp` existe nessa pasta antes de abri-lo.

### Clonar

Crie uma cópia completa do projeto com um nome diferente. Útil para criar variantes sem perder o original.

1. Selecione o projeto que deseja clonar.
2. Pressione **Clonar**.
3. Insira o novo nome da rede.
4. Escolha a pasta de destino (pode ser a mesma pasta se o nome for diferente).

> 💡 A clonagem copia todos os arquivos SHP, DBF e metadados. Os resultados da simulação **não** são clonados para economizar espaço.

### Exportar

Empacota o projeto selecionado em um ZIP portátil (SHP/DBF, `.qgz` e, opcionalmente, resultados, problemas, consultas, camadas auxiliares e dados complementares). Esta é a única forma de exportar um projeto: não existe mais um botão equivalente na barra **Projeto**.

1. Selecione o projeto da lista (não é necessário abri-lo no QGIS).
2. Pressione **Exportar**.
3. Preencha a caixa de diálogo de exportação.

Veja todos os detalhes do diálogo, o que está incluído e o que não está, em [Salvar, exportar e fechar projeto](../projeto-ativo/guardar-backup.md#exportar-el-proyecto).

### Renomear

Renomeia a rede e atualiza automaticamente o nome de **todos os arquivos** do projeto (SHP, DBF, PRJ, etc.). Não é uma simples mudança de nome na lista: ela move e renomeia os arquivos no disco.

1. Selecione o projeto.
2. Pressione **Renomear**.
3. Insira o novo nome.

> ⚠️ Se você estiver com o projeto aberto no QGIS, feche-o antes de renomeá-lo para evitar que o QGIS mantenha bloqueios nos arquivos.

### Excluir da lista (Descarregar)

Remove o projeto do histórico recente **sem excluir arquivos do disco**. O projeto ainda existe na sua pasta e pode ser adicionado novamente com **Upload**.

### Excluir do disco (Excluir)

Exclua o projeto do histórico **e exclua todos os arquivos do projeto** do disco. Esta operação é irreversível.

> ❗ QGISRed pedirá confirmação antes de excluir. Certifique-se de ter um backup se precisar recuperar o projeto no futuro.

### Abrir pasta

Abra o Windows Explorer diretamente na pasta do projeto selecionado.

---

## Como o QGISRed identifica o projeto ativo

Quando você abre o QGIS com um projeto `.qgz` já salvo, o QGISRed reconhece automaticamente a rede ativa pesquisando as camadas carregadas para as quais uma corresponde a `_Pipes.shp` e possui a propriedade interna `qgisred_identifier`.

Se a camada de tubulação estiver carregada mas não possuir esse identificador (por exemplo, porque foi adicionada manualmente sem passar pelo QGISRed), o plugin avisará com a mensagem:

> _"Por favor, abra o projeto no QGISRed Project Manager"_

Nesse caso, feche as camadas e utilize o Gerenciador de Projetos para abrir o projeto corretamente.
