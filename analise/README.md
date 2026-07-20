# 🧪Análise

A barra **Análise** agrupa as ferramentas de simulação hidráulica, visualização de resultados e exportação do modelo. É a barra que fecha o ciclo de trabalho: uma vez definido, verificado e calibrado o modelo, esta barra é utilizada para executar o EPANET, explorar os resultados no mapa e exportar para outros formatos.

> Antes de simular é aconselhável ter passado o [topologia e verificações de atributos](../debug/README.md) para evitar erros de convergência.

<figure><img src="../assets/images/analisis/barra-analysis.png" alt="Barra de ferramentas de análise QGISRed"><figcaption><p>Barra de ferramentas de análise QGISRed</p></figcaption></figure>
*Barra de análise: simulação, visualizador de resultados, séries temporais e exportação.*

---

## Ferramentas da barra de análise

| # | Ferramenta | Função |
|---|-------------|---------|
| 1 | **Executar modelo** | Execute a simulação EPANET e carregue os resultados no mapa |
| — | **Navegador de resultados** | Abra o painel de resultados com os dados da última simulação |
| — | **Relatório de status** | Abra o painel de resultados na guia do relatório de status |
| 2 | **Opções de análise…** | Configurar parâmetros do motor EPANET (unidades, fórmula, tempos, qualidade) |
| 3 | **Série temporal…** | Ative a ferramenta de gráficos de evolução temporal por elemento |
| 4 | **Exportar resultados para CSV…** | Exportar resultados de simulação para arquivos CSV separados para nós e tubulações |
| 5 | **Modelo de exportação para INP…** | Exportar o modelo completo para o EPANET `.inp` |

*O modelo de execução, o navegador de resultados e o relatório de status compartilham um botão suspenso na barra.*

---

## Nesta seção

* [Execução e Opções](ejecucion.md) — simulação, opções de motor e acesso ao relatório de status
* [Visualizador de resultados](resultados.md) — painel de resultados, navegação temporal e séries temporais
* [Exportação de modelo](exportacion.md) — exportação para INP e CSV dos resultados
