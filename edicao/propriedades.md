# Propriedades do elemento

**Barra de edição → Editar propriedades do elemento…**

A caixa de diálogo de propriedades é a ferramenta central para visualizar e editar todos os atributos de qualquer elemento da rede. Funciona como um formulário inteligente que carrega os dados do elemento clicado e permite navegar entre os elementos sem fechá-lo.

<figure><img src="../assets/images/edicion/propiedades-elemento.png" alt="Caixa de diálogo de propriedades de um tubo com todos os seus campos"><figcaption><p>Caixa de diálogo de propriedades de um tubo com todos os seus campos</p></figcaption></figure>
*Diálogo de propriedades: atributos do elemento, navegador de elementos conectados e botão de centralização.*

---

## Como abrir a caixa de diálogo

1. Ative a ferramenta pressionando o botão **Editar propriedades do elemento…** (ícone de lápis/editar).
2. Clique em qualquer elemento da rede no mapa: tubulação, nó, válvula, bomba, RNV ou RNF.
3. A caixa de diálogo é aberta mostrando todos os atributos do elemento selecionado.

> A ferramenta permanece ativa enquanto o botão for pressionado. Você pode clicar em diferentes elementos sem ativá-los novamente.

---

## Campos de tubulação

| Campo | Descrição |
|-------|-------------|
| **ID** | Identificador exclusivo de tubo |
| **Length** | Comprimento calculado automaticamente a partir da geometria (m ou pés) |
| **Diameter** | Diâmetro interno (mm ou polegadas) |
| **Roughness Coeff** | Rugosidade para a fórmula de perda de carga configurada |
| **MinorLoss** | Coeficiente de perda menor (0 se não aplicável) |
| **InitStatus** | Estado inicial: Aberto, Fechado ou CV (Válvula de Retenção) |
| **Material** | Código do material (referenciado na Tabela de Materiais) |
| **InstallYear** | Ano de instalação (formato `YYYY`), utilizado para calcular a rugosidade ao envelhecimento |
| **BulkCoeff** | Coeficiente de reacção em massa (para modelos de qualidade do tipo químico) |
| **WallCoeff** | Coeficiente de reação da parede (para modelos de qualidade do tipo químico) |

---

## Campos de nós (junções)

| Campo | Descrição |
|-------|-------------|
| **ID** | Identificador único de nó |
| **Elevation** | Altura do nó (m ou pés) |
| **Demand** | Demanda base (em unidades de fluxo do projeto) |
| **Pattern** | ID do padrão de demanda aplicado |
| **EmitterCoeff** | Coeficiente do emissor (para modelar fugas dependentes da pressão) |
| **InitQuality** | Concentração ou idade inicial da água (apenas se o modelo de qualidade estiver activo) |

### Múltiplas demandas

Os nós podem ter mais de uma demanda (categorias de usuários: residencial, industrial, etc.). Caso o projeto possua a camada opcional `{Red}_MultipleDemands.shp`, a caixa de diálogo mostra uma seção adicional onde é possível adicionar, editar e excluir demandas por categoria:

| Campo | Descrição |
|-------|-------------|
| **Demand** | Valor de demanda para esta categoria |
| **Pattern** | Padrão de demanda específico da categoria |
| **Name** | Etiqueta da categoria (informativa) |

---

## Campos do RNV (Reservatório de Nível Variável)

| Campo | Descrição |
|-------|-------------|
| **ID** | Identificador único |
| **Elevation** | Nível inferior do RNV |
| **InitLevel** | Nível inicial de água no fundo |
| **MinLevel** | Nível operacional mínimo |
| **MaxLevel** | Nível operacional máximo |
| **Diameter** | Diâmetro do RNV (0 se utilizar curva de volume) |
| **MinVol** | Volume mínimo (m³) |
| **VolCurve** | ID da curva de volume (para geometria não cilíndrica) |
| **MixModel** | Modelo de mixagem: MIXED, 2COMP, FIFO, LIFO |
| **MixFraction** | Fração do primeiro compartimento (modelo 2COMP) |

---

## Campos do RNF (Reservatório de Nível Fixo)

| Campo | Descrição |
|-------|-------------|
| **ID** | Identificador único |
| **Head** | Cabeça piezométrica fixa (m ou pés) |
| **Pattern** | Padrão de variação de carga ao longo do tempo |

---

## Campos de válvula (Válvulas)

| Campo | Descrição |
|-------|-------------|
| **ID** | Identificador único |
| **Diameter** | Diâmetro (mm ou polegadas) |
| **Valve Type** | Tipo de válvula: PRV, PSV, PBV, FCV, TCV, GPV |
| **Setting** | Ponto de ajuste de regulação (pressão, vazão ou perda de carga dependendo do tipo) |
| **MinorLoss** | Coeficiente de perda menor |
| **InitStatus** | Estado inicial: Aberto, Fechado, Ativo |

---

## Campos de Bombas (Bombas)

| Campo | Descrição |
|-------|-------------|
| **ID** | Identificador único |
| **Curve** | ID da curva H-Q da bomba |
| **Speed** | Fator de velocidade de giro (1,0 = nominal) |
| **Pattern** | Padrão de variação de velocidade |
| **Power** | Potência constante (alternativa à curva H-Q) |
| **EfficiencyCurve** | ID da curva de eficiência (para análise energética) |
| **EnergyPrice** | Preço específico da energia para esta bomba |
| **PricePattern** | Padrão de variação do preço da energia |
| **InitStatus** | Estado inicial: Aberto ou Fechado |

---

## Navegação entre elementos

A caixa de diálogo inclui um **navegador** (Navegador) que permite:

- **Ir para o elemento conectado**: lista os nós e elementos conectados ao elemento atual para ir até eles.
- **Histórico**: botões Anterior/Próximo para retornar aos itens visitados anteriormente sem fechar a caixa de diálogo.
- **Centralizar no mapa**: botão para mover o mapa para o elemento exibido atualmente.

> Ao navegar para outro elemento da caixa de diálogo, QGISRed salva as alterações do elemento anterior antes de carregar o novo. Não é necessário clicar explicitamente em “Aceitar” após cada modificação.

---

## Campos exclusivos QGISRed

Estes campos não fazem parte do padrão EPANET mas são utilizados pelo plugin:

| Campo | Camada | Descrição |
|-------|------|-------------|
| **Material** | Tubos | Código do material referenciado na Tabela de Materiais |
| **InstallYear** | Tubos | Ano de instalação para cálculo da rugosidade devido ao envelhecimento |
| **IsActive** | Vários | Habilitar/desabilitar o elemento no Digital Twin |
| **Tag** | Todos | Tag grátis (equivalente ao campo EPANET TAG) |
