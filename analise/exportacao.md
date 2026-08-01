# Exportação de modelo

A barra Análise oferece dois caminhos de exportação: o modelo completo como um arquivo EPANET `.inp` e os resultados da simulação como tabelas CSV.

---

## Exportar modelo para INP…

**Barra de análise → Exportar modelo para INP…**

Exporta todo o modelo para o formato padrão EPANET **INP**. Útil para partilhar o modelo com outros utilizadores, executá-lo na interface gráfica do EPANET ou integrá-lo com ferramentas de terceiros.

<figure><img src="../assets/images/analisis/export-inp-dialog.png" alt="Caixa de diálogo Exportar para o formato INP"><figcaption><p>Caixa de diálogo Exportar para o formato INP</p></figcaption></figure>
*Caixa de diálogo Exportar para INP: rota de destino, exportação de dados de campo e abertura automática no EPANET.*

### Opções de diálogo

| Opção | Descrição |
|--------|-------------|
| **Arquivo INP** | Caminho completo do arquivo `.inp` a ser gerado. Use o botão `…` para navegar. |
| **Exportar arquivos de dados de campo** | Também exporta os arquivos de dados de campo auxiliares associados ao modelo. |
| **Abrir arquivo INP com EPANET** | Se ativo, abre o `.inp` no EPANET após a conclusão da exportação. |
| **Caminho Epanet** | Executável EPANET detectado no sistema. O menu suspenso mostra todas as versões instaladas. |
| **Caminho Epanet específico** | Caminho manual para um executável EPANET não detectado automaticamente. |

Pressione **Exportar para INP** para gerar o arquivo com a configuração escolhida.

> ℹ️ **Precisão decimal conforme valores padrão do projeto.** A quantidade de casas decimais utilizadas para cada campo do arquivo `.inp` gerado respeita a precisão configurada nos valores padrão do projeto, a mesma mostrada nos painéis Propriedades e Consultas. Nas versões anteriores era aplicado um formato fixo de 4 a 6 casas decimais independente da configuração do projeto.

---

## Exportar resultados para CSV…

**Barra de análise → Exportar resultados para CSV…**

Exporta os resultados da última simulação para dois arquivos CSV: um para nós e outro para tubulações. É o método padrão para obter resultados em Excel, Python, R ou outras ferramentas de análise externas.

> Disponível apenas se existir um arquivo de simulação `.out` para o cenário ativo.

### Opções de diálogo

| Opção | Descrição |
|--------|-------------|
| **Nós CSV** | Caminho do arquivo de saída para resultados de nós. Por padrão `{Red}_{Escenario}_Nodes.csv` na pasta `Results/`. |
| **Links CSV** | Caminho do arquivo de saída para resultados do pipeline. Por padrão `{Red}_{Escenario}_Links.csv`. |
| **Separador de lista** | Separador de campo (detectado automaticamente no sistema regional; comum `;` em instalações europeias). |
| **Separador decimal** | Separador decimal (detectado no sistema; comum `,` em locais europeus). |

### Conteúdo do arquivo

**Nós CSV** — uma linha por instante por nó, com colunas:

`Time | ID | Pressure | Head | Demand | Quality`

**Links CSV** — uma linha por instante de tempo por tubo/válvula/bomba, com colunas:

`Time | ID | Status | Flow | Velocity | HeadLoss | UnitHdLoss | FricFactor | ReactRate | Quality`

> Os separadores se adaptam à localidade do sistema operacional para que o arquivo abra corretamente no Excel sem a necessidade de conversão.
