# Instalação do Repositório

É o método recomendado. Instale o QGISRed diretamente do repositório oficial do plugin QGIS e permita que você receba atualizações automáticas.

---

## Passo a passo

1. Abra o QGIS.
2. Vá para o menu **Plugins → Gerenciar e instalar plugins…**
3. Na guia **Todos**, digite `QGISRed` na caixa de pesquisa.
4. Selecione **QGISRed** na lista de resultados.
5. Clique em **Instalar plug-in**.

Quando terminar, a barra principal do QGISRed e o menu **QGISRed** aparecerão na barra de menu do QGIS.

---

## Primeira execução

Na primeira vez que você usa qualquer ferramenta de plug-in, o QGISRed detecta que as **dependências** não estão instaladas e exibe uma caixa de diálogo de instalação. Veja [Gerenciamento de dependências](dependencias.md) para detalhes.

---

## Atualizações automáticas

Ao iniciar o QGIS, o QGISRed verifica se uma nova versão está disponível. Caso exista, a janela de notícias do QGISRed abrirá automaticamente informando sobre a nova versão. Para atualizar a partir daí:

1. Vá para **Plugins → Gerenciar e instalar plug-ins…**
2. Abra a guia **Atualizável**.
3. Selecione **QGISRed** e clique em **Atualizar Plugin**.

> Você também pode ativar a atualização automática na aba **Configurações** do gerenciador de plugins.

---

## Solução de problemas

**QGISRed não aparece nos resultados da pesquisa**

O gerenciador de plugins precisa ter o repositório oficial do QGIS configurado. Vá para **Plugins → Gerenciar e instalar plug-ins… → Configurações** e verifique se o repositório `https://plugins.qgis.org/plugins/plugins.xml` está ativo.

**O botão "Instalar Plugin" está desabilitado**

Pode ser porque a versão instalada do QGIS é anterior à 3.28. Atualize o QGIS primeiro.
