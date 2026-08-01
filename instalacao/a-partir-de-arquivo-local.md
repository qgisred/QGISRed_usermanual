# Instalação do ZIP Local

Use este método quando precisar instalar uma versão específica do plugin que não está no repositório ou quando seu computador não tiver acesso à Internet no momento da instalação.

---

## Obtenha o arquivo ZIP

Baixe o arquivo `QGISRed.zip` de:

- O repositório oficial de plugins do QGIS (seção de versões anteriores).
- O repositório GitHub do projeto.
- Um arquivo compartilhado pela equipe de desenvolvimento.

---

## Passo a passo

1. Abra o QGIS.
2. Vá para o menu **Plugins → Gerenciar e instalar plugins…**
3. Selecione a guia **Instalar do ZIP**.
4. Clique no botão `…` e selecione o arquivo `QGISRed.zip`.
5. Clique em **Instalar plug-in**.

<figure><img src="../assets/images/instalacion/instalar-desde-zip.png" alt="Instalação do ZIP"><figcaption><p>Guia "Instalar do ZIP" do gerenciador de plugins QGIS.</p></figcaption></figure>

---

## Aviso de segurança

O QGIS exibirá um aviso indicando que o plugin não vem do repositório oficial. Isso é normal para qualquer instalação de arquivo local. Pressione **Sim** para continuar com a instalação.

---

## Notas

- Se você já possui uma versão anterior do QGISRed instalada, a instalação a partir do ZIP a substitui. Os projetos existentes não são afetados.
- **dependências** não estão incluídas no plugin ZIP. Eles são baixados separadamente na primeira vez que você usa o plugin, assim como na instalação do repositório. Se o seu computador não tiver conexão com a Internet, consulte a seção [Gerenciamento de dependências](dependencias.md) para ver como instalá-los manualmente.
- Esta instalação **não recebe atualizações automáticas**. Para atualizar você terá que repetir o processo com o ZIP da nova versão.
