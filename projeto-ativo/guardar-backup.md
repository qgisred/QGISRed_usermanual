# Salvar e fazer backup

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

## Backup

**Barra do projeto → Backup** (Backup do projeto)

Cria uma cópia completa de todos os arquivos SHP, arquivos DBF e metadados do projeto em uma subpasta com a data e hora atuais.

### Onde está salvo

```
{CarpetaProyecto}/Backups/{NombreRed}_{YYYYMMDD_HHMMSS}/
```

Por exemplo:
```
RedUrbana/Backups/RedUrbana_20241215_143022/
    RedUrbana_Junctions.shp
    RedUrbana_Pipes.shp
    RedUrbana_Options.dbf
    ...
```

Após a conclusão, o QGISRed mostra o caminho completo da cópia criada na barra de mensagens.

### O que está incluído no backup

- Todos os arquivos SHP+DBF+PRJ na pasta principal do projeto
- As opções e arquivos de metadados (`_Options.dbf`, `_Title.dbf`)
- As subpastas de dados auxiliares (Demands Builder, etc.)

### O que não está incluído

- A pasta `Results/` (os resultados da simulação podem ser muito grandes e podem ser regenerados executando a simulação novamente)
- A pasta `Issues/` (regenerada ao reexecutar as verificações)
- O arquivo `.qgz` (salve-o manualmente com _Save Map_ se quiser incluí-lo)

> 💡 **Práticas recomendadas**: Faça um backup antes de operações que modificam muitos elementos de uma vez (importações em massa, alterações de CRS, conversões de rugosidade). Também é recomendado antes de atualizar a versão do plugin.

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
| Backup | Todas PCH/DBF do projeto | Subpasta `Backups/` |
