# 🧭 A interface QGISRed

QGISRed integra-se ao QGIS como um conjunto de **barras de ferramentas especializadas**. Cada barra agrupa as ferramentas de uma etapa do fluxo de trabalho: gerenciamento de projetos, edição de rede, verificação, simulação, etc.

<figure><img src="../assets/images/guia-rapida/barra-principal.png" alt="Barra principal QGISRed com os botões suspensos de cada barra de ferramentas"><figcaption><p>Barra principal QGISRed com os botões suspensos de cada barra de ferramentas</p></figcaption></figure>
*Barra principal QGISRed: cada botão suspenso ativa/desativa uma barra de ferramentas.*

---

## A barra principal

Quando você instala o plugin, uma **barra principal** aparece no QGIS com um botão suspenso para cada barra de ferramentas secundária. Clicar em qualquer um desses botões mostra ou oculta a barra correspondente. Além disso, o menu suspenso de cada botão lista diretamente todas as ações daquela barra de ferramentas, permitindo que sejam executadas sem ter a barra visível.

À direita da barra principal há um **indicador de unidades** (por exemplo `LPS | D-W`) que mostra as unidades de fluxo e a fórmula de perda de carga para o projeto ativo.

## Barras de ferramentas

QGISRed inclui **8 barras de ferramentas** organizadas por área de trabalho:

| Barra | Função principal |
|-------|------------------|
| **Geral** | Criar, abrir e importar projetos |
| **Projeto** | Configuração, Camadas e Backup |
| **Edição** | Desenhar e editar a rede hidráulica |
| **Depurar** | Verifique a qualidade e consistência do modelo |
| **Ferramentas** | Ferramentas de cálculo e gerenciamento de dados |
| **Consultas** | Consultar, filtrar e visualizar informação |
| **Análise** | Simular e explorar resultados |
| **Gêmeo Digital** | Conexões, válvulas de corte e sensores |

> 💡 **DICA**: Ative apenas as barras necessárias a qualquer momento para manter o espaço de trabalho arrumado. O status de visibilidade de cada barra é salvo automaticamente entre as sessões.

## O projeto QGISRed

Todos os dados da rede são armazenados em uma pasta do projeto como arquivos **SHP + DBF**. O nome da rede (por exemplo `MiRed`) é o prefixo comum de todos esses arquivos (`MiRed_Pipes.shp`, `MiRed_Junctions.shp`, etc.).

QGISRed não funciona com o arquivo QGIS `.qgz` como fonte da verdade: a fonte da verdade são sempre os arquivos SHP do projeto. O `.qgz` é opcional e é usado para salvar a aparência visual (estilos, camadas visíveis, etc.).

---

Confira [Resumo da barra de ferramentas](toolbars.md) para ver o que cada ferramenta faz ou vá direto para [Fluxo de trabalho típico](flujo-de-trabajo.md) se quiser começar o mais rápido possível.
