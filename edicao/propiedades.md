# Propriedades do elemento

**Barra de edição → Editar propriedades do elemento…**

A caixa de diálogo de propriedades é a ferramenta central para visualizar e editar todos os atributos de qualquer elemento da rede. Funciona como um formulário inteligente que carrega os dados do elemento clicado e permite navegar entre os elementos sem fechá-lo.

<figure><img src="../assets/images/edicion/propiedades-elemento.png" alt="Caixa de diálogo de propriedades de um tubo com todos os seus campos"><figcaption><p>Caixa de diálogo de propriedades de um tubo com todos os seus campos</p></figcaption></figure>
*Diálogo de propriedades: atributos do elemento, navegador de elementos conectados e botão de centralização.*

---

## Como abrir a caixa de diálogo

1. Ative a ferramenta pressionando o botão **Editar propriedades do elemento…** (ícone de lápis/editar).
2. Clique em qualquer elemento da rede no mapa: tubulação, nó, válvula, bomba, tanque ou reservatório.
3. A caixa de diálogo é aberta mostrando todos os atributos do elemento selecionado.

> A ferramenta permanece ativa enquanto o botão for pressionado. Você pode clicar em diferentes elementos sem ativá-los novamente.

---

## Campos de tubulação

| Campo | Descrição |
|-------|-------------|
| **ID** | Identificador exclusivo de tubo |
| **Comprimento** | Comprimento calculado automaticamente a partir da geometria (m ou pés) |
| **Diâmetro** | Diâmetro interno (mm ou polegadas) |
| **Rugosidade** | Rugosidade para a fórmula de perda de carga configurada |
| **Perda Menor** | Coeficiente de perda menor (0 se não aplicável) |
| **Status de inicialização** | Estado inicial: Aberto, Fechado ou CV (Válvula de Retenção) |
| **Material** | Código do material (referenciado na Tabela de Materiais) |
| **Ano de instalação** | Ano de instalação (formato `YYYY`), utilizado para calcular a rugosidade ao envelhecimento |
| **Coeff em Massa** | Coeficiente de reacção em massa (para modelos de qualidade do tipo químico) |
| **WallCoef** | Coeficiente de reação da parede (para modelos de qualidade do tipo químico) |

---

## Campos de nós (junções)

| Campo | Descrição |
|-------|-------------|
| **ID** | Identificador único de nó |
| **Elevação** | Altura do nó (m ou pés) |
| **Demanda** | Demanda base (em unidades de fluxo do projeto) |
| **Padrão** | ID do padrão de demanda aplicado |
| **EmissorCoeff** | Coeficiente do emissor (para modelar fugas dependentes da pressão) |
| **Qualidade inicial** | Concentração ou idade inicial da água (apenas se o modelo de qualidade estiver activo) |

### Múltiplas demandas

Os nós podem ter mais de uma demanda (categorias de usuários: residencial, industrial, etc.). Caso o projeto possua a camada opcional `{Red}_MultipleDemands.shp`, a caixa de diálogo mostra uma seção adicional onde é possível adicionar, editar e excluir demandas por categoria:

| Campo | Descrição |
|-------|-------------|
| **Demanda** | Valor de demanda para esta categoria |
| **Padrão** | Padrão de demanda específico da categoria |
| **Nome** | Etiqueta da categoria (informativa) |

---

## Campos de tanques

| Campo | Descrição |
|-------|-------------|
| **ID** | Identificador único |
| **Elevação** | Nível inferior do tanque |
| **Nível de inicialização** | Nível inicial de água no fundo |
| **Nível mínimo** | Nível operacional mínimo |
| **Nível Máximo** | Nível operacional máximo |
| **Diâmetro** | Diâmetro do reservatório (0 se utilizar curva de volume) |
| **VolMín** | Volume mínimo (m³) |
| **VolCurva** | ID da curva de volume (para geometria não cilíndrica) |
| **Modelo misto** | Modelo de mixagem: MIXED, 2COMP, FIFO, LIFO |
| **Fração Misturada** | Fração do primeiro compartimento (modelo 2COMP) |

---

## Campos de reservatório

| Campo | Descrição |
|-------|-------------|
| **ID** | Identificador único |
| **Cabeça** | Cabeça piezométrica fixa (m ou pés) |
| **Padrão** | Padrão de variação de carga ao longo do tempo |

---

## Campos de válvula (Válvulas)

| Campo | Descrição |
|-------|-------------|
| **ID** | Identificador único |
| **Diâmetro** | Diâmetro (mm ou polegadas) |
| **Tipo** | Tipo de válvula: PRV, PSV, PBV, FCV, TCV, GPV |
| **Configuração** | Ponto de regulação de regulação (pressão, caudal ou perda de pressão dependendo do tipo) |
| **Perda Menor** | Coeficiente de perda menor |
| **Status de inicialização** | Estado inicial: Aberto, Fechado, Ativo |

---

## Campos de Bombas (Bombas)

| Campo | Descrição |
|-------|-------------|
| **ID** | Identificador único |
| **Curva** | ID da curva H-Q da bomba |
| **Velocidade** | Fator de velocidade de giro (1,0 = nominal) |
| **Padrão** | Padrão de variação de velocidade |
| **Poder** | Potência constante (alternativa à curva H-Q) |
| **Curva de Eficiência** | ID da curva de eficiência (para análise energética) |
| **PreçoEnergia** | Preço específico da energia para esta bomba |
| **Padrão de Preço** | Padrão de variação do preço da energia |
| **Status de inicialização** | Estado inicial: Aberto ou Fechado |

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
| **Ano de instalação** | Tubos | Ano de instalação para cálculo da rugosidade devido ao envelhecimento |
| **EstáAtivo** | Vários | Habilitar/desabilitar o elemento no Digital Twin |
| **Etiqueta** | Todos | Tag grátis (equivalente ao campo EPANET TAG) |
