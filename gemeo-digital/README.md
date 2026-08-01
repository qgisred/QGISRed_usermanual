# 🧬Gêmeo Digital

O barramento **Digital Twin** agrega ao modelo hidráulico os elementos de infraestrutura que conectam a rede ao usuário final e aos sistemas de monitoramento de campo: conexões, válvulas de corte, medidores e sensores. Estes elementos não fazem parte estritamente do modelo EPANET, mas enriquecem o gémeo digital com informação operacional e de leitura remota.

<figure><img src="../assets/images/gemelo-digital/barra-digital-twin.png" alt="Barra de ferramentas digital dupla QGISRed"><figcaption><p>Barra de ferramentas digital dupla QGISRed</p></figcaption></figure>
*Digital Twin Bar: conexões, válvulas de corte, medidores e carregamento de dados de campo.*

---

## Ferramentas de barra dupla digital

### Grupo 1 — Elementos da rede

| # | Ferramenta | Função |
|---|-------------|---------|
| 1 | **Adicionar conexão de serviço** | Fazer uma ligação entre a tubagem principal e o ponto de abastecimento do cliente |
| 2 | **Adicionar válvula de isolamento** | Adicione uma válvula de corte clicando em um tubo |
| 3 | **Adicionar medidor** (menu suspenso) | Coloque um medidor ou sensor em um tubo. 11 tipos disponíveis |

### Grupo 2 — Dados operacionais

| # | Ferramenta | Função |
|---|-------------|---------|
| 4 | **Leituras do medidor de carga…** | Carregar leituras de medidores inteligentes e associá-las às conexões do projeto |
| 5 | **Defina o status inicial do tubo a partir das válvulas de isolamento** | Propaga o estado aberto/fechado das válvulas de corte para o campo `InitStatus` das tubulações afetadas |
| 6 | **Carregar dados do campo…** | Importe dados de campo SCADA e associe-os aos medidores do projeto |

### Grupo 3 — Integração no modelo

| # | Ferramenta | Função |
|---|-------------|---------|
| 7 | **Converter conexões de serviço em tubos/nós** | Converte ligações em nós pontuais ou tubos do modelo EPANET |

---

## Nesta seção

* [Conexões e Válvulas de Corte](ramais.md) — desenho de ligações, válvulas de corte e conversão para modelo hidráulico
* [Sensores e Medidores](sensores.md) — tipos de medidores, leituras de carregamento e dados de campo
