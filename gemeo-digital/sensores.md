# Sensores e Medidores

Os medidores e sensores Digital Twin são elementos que registram magnitudes físicas em pontos específicos da rede. QGISRed os armazena na camada complementar `Meters` e os utiliza para carregar dados de campo e compará-los com os resultados da simulação.

---

## Adicionar medidor (menu suspenso)

**Barra Twin Digital → Adicionar medidor**

Coloque um medidor ou sensor em um tubo clicando no ponto de instalação. O menu suspenso do botão permite escolher o tipo antes de colocá-lo; O último tipo utilizado permanece como ação padrão do botão.

<figure><img src="../assets/images/gemelo-digital/add-meter-dropdown.png" alt="Menu suspenso de tipo de medidor na barra Digital Twin"><figcaption><p>Menu suspenso de tipo de medidor na barra Digital Twin</p></figcaption></figure>
*Adicionar menu suspenso de medidores: os 11 tipos de medidores disponíveis.*

### Tipos de medidores disponíveis

| Tipo | Nome na barra | Magnitude registada |
|------|--------------------|---------------------|
| **Medidor automático** | Adicionar medidor automático | Tipo determinado automaticamente pelo contexto |
| **Manômetro** | Adicionar manômetro | Pressão (m.c.a.) |
| **Medidor de vazão** | Adicionar medidor de vazão | Vazão (l/s ou unidade configurada) |
| **Contador** | Adicionar contador | Volume acumulado (medidor de água) |
| **Nível do sensor** | Adicionar sensor de nível | Nível de folha livre no RNV |
| **Manômetro diferencial** | Adicionar manômetro diferencial | Diferença de pressão entre dois pontos |
| **Sensor de qualidade** | Adicionar sensor de qualidade | Concentração de cloro ou outro parâmetro de qualidade |
| **Sensor de energia** | Adicionar sensor de energia | Potência ou energia consumida (grupos de bombagem) |
| **Status do sensor** | Adicionar status do sensor | Estado operacional de um tubo ou válvula |
| **Abertura da válvula** | Adicionar abertura de válvula | Grau de abertura de uma válvula reguladora |
| **Tacômetro** | Adicionar tacômetro | Velocidade de rotação de uma bomba (rpm) |

### Processo

1. Escolha o tipo de medidor no menu suspenso.
2. Clique no tubo no ponto de instalação.
3. QGISRed chama `GISRed.AddMeter` com o tipo selecionado e atualiza a camada `Meters`.

---

## Leituras do medidor de carga…

**Barra Dupla Digital → Leituras do medidor de carga…**

Importa leituras de medidores inteligentes (medição inteligente) e as associa às conexões do projeto. As leituras enriquecem as demandas do modelo com dados de consumo reais, em vez de demandas estimadas.

### Formatos de importação suportados

| Formato | Estrutura de arquivos |
|---------|------------------------|
| **Tabela** | Primeira linha: cabeçalho com `Time; Id1; Id2; …`. Colunas: um contador por coluna. |
| **Série** | Uma linha por registro: `Id; Time; Demand`. Todos os contadores no mesmo arquivo. |

Os separadores de campo são detectados automaticamente no sistema regional. O campo `Time` aceita carimbos de data/hora absolutos e deslocamento em horas desde o início da simulação.

---

## Definir o status inicial do tubo a partir das válvulas de isolamento

**Digital Twin Bar → Definir o status inicial do tubo a partir das válvulas de isolamento**

Propaga o estado de abertura ou fechamento das válvulas de corte da camada `IsolationValves` para o campo `InitStatus` dos tubos que passam por cada válvula. Assim, o modelo EPANET coleta o estado real da rede sem a necessidade de modificar manualmente cada tubulação.

### Requisito

A camada `IsolationValves.shp` deve existir no diretório do projeto. Caso não exista, a ferramenta exibe um aviso e não faz nenhuma alteração.

### Quando usar

- Antes de simular um cenário operacional específico (por exemplo, com setor fechado para manutenção).
- Depois de atualizar o status de diversas válvulas de corte no mapa e antes de executar **Executar modelo**.

> Esta operação modifica o modelo EPANET (campo `InitStatus` de `Pipes`). Para retornar ao estado original, use **Construtor de cenários** (barra de ferramentas) se você salvou o cenário base antes da operação.

---

## Carregar dados do campo…

**Barra Gêmea Digital → Carregar dados do campo…**

Importa dados de campo de sistemas SCADA ou data loggers e os associa aos medidores da camada `Meters`. Os dados carregados são vinculados a cada sensor para posterior comparação com os resultados da simulação.

A caixa de diálogo permite selecionar o arquivo de dados e configurar o formato de data/hora e o separador de campo. QGISRed chama `GISRed.LoadScada` e atualiza os registros da camada `Meters` com a série temporal importada.

### Uso típico

1. Exporte os dados do sensor de campo do SCADA para um arquivo CSV ou DAT.
2. Execute **Carregar dados do campo** e selecione o arquivo.
3. Execute a simulação (**Executar modelo**).
4. Compare visualmente os valores medidos (campo) e calculados (simulação) para cada sensor no dock **Série temporal**.
