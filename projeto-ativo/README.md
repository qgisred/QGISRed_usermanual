# 📋 Projeto

A barra **Projeto** agrupa as ferramentas de administração do projeto que já está aberto no QGISRed. Todos os seus botões requerem um projeto válido carregado; Caso não haja nenhum, o plugin avisará com a mensagem _"Nenhum projeto válido foi aberto"_.

<figure><img src="../assets/images/proyecto/barra-project.png" alt="Barra de ferramentas do projeto QGISRed com seus nove botões"><figcaption><p>Barra de ferramentas do projeto QGISRed com seus nove botões</p></figcaption></figure>
*Barra de Projetos: ferramentas ativas de gerenciamento de projetos.*

<!-- TODO: captura de tela desatualizada após remoção do botão "Backup do projeto" (commit 7b2415f) -->

---

## Botões da barra de projeto

| # | Ferramenta | Função |
|---|-------------|---------|
| 1 | **Resumo** | Número de elementos de cada tipo na rede |
| 2 | **Adicionar dados por importação** | Importe elementos adicionais para o projeto aberto |
| 3 | **Gerenciador de camadas** | Controlar a visibilidade da camada e recuperar camadas excluídas |
| 4 | **Editor de legendas** | Personalize a simbologia das camadas |
| — | *(separador)* | |
| 5 | **Opções de Projeto** | Parâmetros EPANET: unidades, fórmula, qualidade, tempos, energia |
| 6 | **Valores padrão** | Prefixos de identificação, tolerâncias e valores hidráulicos iniciais |
| 7 | **Tabela de materiais** | Taxas de rugosidade e envelhecimento por material |
| — | *(separador)* | |
| 8 | **Salvar mapa** | Salve o arquivo QGIS `.qgz` |
| 9 | **Fechar projeto** | Feche o projeto e limpe a sessão QGIS |

> 💡 O antigo botão **Backup** (_Backup do projeto_) foi removido desta barra sem substituição direta. Para exportar o projeto para um ZIP portátil, use o botão **Exportar** em [Gestor de projeto](../gestao-projetos/gestor-projetos.md) — veja [Salvar, exportar e fechar projeto](salvar-exportar-fechar.md).

## Nesta seção

* [Visão geral e gerenciamento de camadas](camadas-e-legenda.md) — visibilidade, recuperação e legenda da camada
* [Configurações do Projeto](configuracao-do-projeto.md) — Opções do EPANET, valores padrão, materiais
* [Salvar, exportar e fechar projeto](salvar-exportar-fechar.md) — salve o mapa, exporte para ZIP e feche
