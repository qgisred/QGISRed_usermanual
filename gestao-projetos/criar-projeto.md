# Criar Projeto

**Barra Geral → Criar projeto** (ou menu QGISRed → Geral → Criar projeto)

Crie um projeto QGISRed completamente novo do zero, gerando a estrutura de arquivos SHP necessária para definir uma rede de distribuição.

<figure><img src="../assets/images/general/crear-proyecto.png" alt="Caixa de diálogo de criação de novo projeto"><figcaption><p>Caixa de diálogo de criação de novo projeto</p></figcaption></figure>
*Diálogo de criação de projeto: nome, pasta e sistema de referência.*

---

## Passo a passo

### 1. Nome da rede

Insira um nome curto sem espaços ou caracteres especiais (letras, números e sublinhados são seguros). Este nome será o **prefixo** de todos os arquivos do projeto.

- ✅ Correto: `RedUrbana`, `Red_Norte_2024`, `SectorA`
- ❌ Evite: `Red Urbana`, `Réseau_Côte`, `Red/Norte`

### 2. Pasta do projeto

Selecione ou crie a pasta onde todos os arquivos serão salvos. **Vários projetos podem coexistir na mesma pasta** desde que tenham nomes diferentes.

### 3. Sistema de Referência de Coordenadas (SRC)

Selecione o CRS apropriado para sua área de trabalho. QGISRed irá atribuí-lo a todos os arquivos SHP do projeto.

> 💡 Se você for importar geometria de outras fontes (ortofoto, cadastro, etc.), utilize o mesmo CRS dessas fontes ou o mais comum em seu país para evitar reprojeções.

### 4. Opções iniciais do EPANET

Na mesma caixa de diálogo você pode configurar os parâmetros básicos do modelo:

| Parâmetro | Descrição |
|-----------|-------------|
| **Unidades de fluxo** | LPS (litros/segundo), GPM, CMH, etc. Determina se o projeto funciona no sistema SI ou US |
| **Fórmula de perda de carga** | Darcy-Weisbach (DW), Hazen-Williams (HW) ou Chezy-Manning (CM) |

Estes parâmetros podem ser alterados posteriormente em _Opções do Projeto_, mas é recomendado defini-los desde o início porque afetam quais unidades serão exibidas em todas as propriedades da rede.

### 5. Catálogo de materiais

Selecione o **catálogo de materiais** que será utilizado no projeto. Este catálogo é um arquivo `.dbf` que define os materiais de tubulação disponíveis (nome, coeficiente de rugosidade inicial e incremento de envelhecimento).

QGISRed procura os catálogos disponíveis nas pastas `materials` e `global_defaults` de `%APPDATA%\QGISRed\`. Se não houver nenhum catálogo instalado, o menu suspenso aparecerá vazio e o projeto será criado sem materiais predefinidos.

> O catálogo de materiais permite estimar automaticamente a rugosidade dos tubos com base no seu material e idade, facilitando a calibração do modelo hidráulico.

---

## Arquivos gerados

Ao confirmar a criação, o QGISRed gera os seguintes arquivos na pasta escolhida e os carrega automaticamente no QGIS:

| Arquivo | Conteúdo |
|---------|-----------|
| `{Red}_Junctions.shp` | Nós de demanda |
| `{Red}_Pipes.shp` | Tubos |
| `{Red}_Tanks.shp` | Depósitos |
| `{Red}_Reservoirs.shp` | Reservatórios ou pontos de alimentação |
| `{Red}_Valves.shp` | Válvulas reguladoras |
| `{Red}_Pumps.shp` | Bombas |
| `{Red}_Options.dbf` | Opções EPANET (unidades, fórmula, qualidade...) |
| `{Red}_Title.dbf` | Metadados do projeto (nome do cenário, notas…) |

Eles estão todos agrupados na legenda do QGIS em um grupo chamado **"{Red}" → "Inputs"**.

---

## O que fazer a seguir

Depois que o projeto for criado, a próxima etapa é **construir a rede** usando a barra **Edição**. Consulte a seção [Edição e Modelagem](../edicao/README.md) para ver como adicionar tubos, nós e elementos especiais.

> 💡 Se você já possui um arquivo EPANET `.inp`, é mais rápido usar [Importar projeto](abrir-importar.md#importar-desde-epanet) do que criar do zero.
