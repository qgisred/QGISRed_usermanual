# Criação de Elemento

As primeiras cinco ferramentas da barra de edição permitem adicionar elementos à rede. Todos eles ativam um **modo de edição interativo**: o cursor muda e o plugin aguarda uma ação no mapa. Para cancelar sem criar nada, pressione o mesmo botão novamente ou pressione `Esc`.

---

## Adicionar tubo

**Barra de edição → Adicionar pipe**

Modo de desenho de linha: Cada clique adiciona um vértice à tubulação. A ferramenta permanece ativa até você finalizar o layout.

<figure><img src="../assets/images/edicion/add-pipe.png" alt="Adicionar ferramenta de tubo em ação no mapa QGIS"><figcaption><p>Adicionar ferramenta de tubo em ação no mapa QGIS</p></figcaption></figure>
*Desenhando um cano: A linha vermelha temporária segue o cursor até o próximo clique.*

### Processo

1. Ative a ferramenta. O cursor muda para o modo de desenho.
2. Clique para definir o **ponto inicial**. QGISRed cria automaticamente uma junção nesse ponto se não existir nenhuma dentro do raio de tolerância.
3. Clique para adicionar **vértices intermediários** (pontos de quebra de caminho).
4. **clique duas vezes** ou pressione o **botão direito** para finalizar o pipeline. QGISRed cria um segundo nó no ponto final.

### O que o QGISRed cria ao confirmar

- Um registro em `{Red}_Pipes.shp` com a geometria desenhada.
- Até dois novos nós em `{Red}_Junctions.shp` (um por ponta), caso ainda não exista nó dentro da tolerância configurada.
- Os valores de diâmetro, rugosidade e demanda são retirados dos **Valores Padrão** do projeto.

### Conecte-se a elementos existentes

Se o ponto inicial ou final estiver dentro da tolerância de um nó, válvula, bomba, reservatório ou reservatório existente, o novo tubo **conecta-se a esse elemento** em vez de criar um novo nó.

> Definir para o nó mais próximo usa a tolerância configurada em **Barra de Projeto → Padrões → Tolerância de Nó**. Você pode revisá-lo ou alterá-lo antes de desenhar redes densas.

---

## Adicionar tanque (Adicionar tanque)

**Edição Barra → Adicionar tanque**

Coloque um tanque de armazenamento (tanque) no mapa. Os tanques possuem nível variável e participam da simulação hidráulica.

### Processo

1. Ative a ferramenta. O cursor mostra o ícone de depósito.
2. Clique em um **nó existente** ou em um ponto vazio no mapa.
- Se você clicar em um nó existente, esse nó **se tornará** um Tanque.
- Se você clicar em um ponto vazio, o QGISRed cria um novo Tanque (sem conexão inicial; você precisará conectá-lo com um tubo).
3. QGISRed abre a caixa de diálogo de propriedades do novo depósito para que você possa inserir os dados (elevação inferior, nível inicial, nível mínimo, nível máximo, diâmetro).

### Principais parâmetros do tanque

| Parâmetro | Descrição |
|-----------|-------------|
| **Elevation** | Elevação do fundo do tanque (m ou pés) |
| **InitLevel** | Nível inicial da água acima do fundo |
| **MinLevel** | Nível operacional mínimo |
| **MaxLevel** | Nível operacional máximo |
| **Diameter** | Diâmetro do tanque (para seção circular); se você usar curva de volume, coloque 0 |
| **MinVol** | Volume mínimo (opcional) |
| **VolCurve** | ID da curva de volume (para geometria não cilíndrica) |

---

## Adicionar reservatório (Adicionar reservatório)

**Barra de edição → Adicionar reservatório**

Coloque um reservatório externo ou ponto de alimentação (Reservatório). Ao contrário do Tanque, o Reservatório possui **nível fixo** (altura piezométrica constante) e representa uma fonte de água de capacidade ilimitada.

O processo é idêntico ao do depósito. Os parâmetros são mais simples:

| Parâmetro | Descrição |
|-----------|-------------|
| **Cabeça** | Carga piezométrica fixa (elevação do nível da água livre, m ou pés) |
| **Padrão** | Padrão de variação de carga ao longo do tempo (opcional) |

> Utilizar reservatórios para representar pontos de abastecimento de água elevados (ligações com sistemas externos) ou pontos de abastecimento de fluxo constante.

---

## Insira a válvula no tubo (Insira a válvula no tubo)

**Edição Barra → Insira a válvula na tubulação**

Insira uma válvula em um tubo existente. O tubo original é **dividido em duas seções** que são conectadas através da válvula.

<figure><img src="../assets/images/edicion/insert-valve.png" alt="Resultado da inserção de uma válvula: o tubo original é dividido em dois"><figcaption><p>Resultado da inserção de uma válvula: o tubo original é dividido em dois</p></figcaption></figure>
*O tubo P-12 original é dividido em P-12 e P-13, com a válvula V-1 entre eles.*

### Processo

1. Ative a ferramenta. O cursor muda para o ícone da válvula.
2. Clique no tubo onde deseja inserir a válvula.
3. QGISRed determina o ponto exato de inserção (projeção do clique no eixo do tubo) e:
- Crie um nó nesse ponto.
- Divide o tubo original em duas seções com o mesmo diâmetro e atributos de material.
- Crie a válvula entre as duas novas extremidades.
4. A caixa de diálogo de propriedades é aberta para configurar o tipo e a configuração da válvula.

### Tipos de válvulas disponíveis

| Tipo | Nome | Função |
|------|--------|---------|
| **PRV** | Válvula Redutora de Pressão | Reduz a pressão a jusante até o ponto de ajuste |
| **PSV** | Válvula de sustentação de pressão | Mantém a pressão a montante no ponto de ajuste |
| **PBV** | Válvula quebra-pressão | Produz uma perda de carga fixa |
| **FCV** | Válvula de controle de fluxo | Limita o fluxo ao setpoint |
| **TCV** | Válvula de controle do acelerador | Simula uma válvula parcialmente fechada usando um coeficiente de perda |
| **GPV** | Válvula de uso geral | Perda de carga definida por uma curva personalizada |

---

## Insira a bomba no tubo (Insira a bomba no tubo)

**Edição Barra → Insira a bomba na tubulação**

Insira uma bomba em um tubo existente, dividindo-o exatamente da mesma forma que acontece com as válvulas.

### Processo

1. Ative a ferramenta e clique no tubo.
2. QGISRed divide o tubo e cria a bomba entre as duas seções resultantes.
3. A caixa de diálogo de propriedades é aberta para configurar a curva H-Q e a velocidade inicial.

### Parâmetros da bomba

| Parâmetro | Descrição |
|-----------|-------------|
| **Curva** | ID da curva H-Q (obrigatório para simular) |
| **Velocidade** | Fator de velocidade inicial (1,0 = velocidade nominal) |
| **Pattern** | Padrão de variação de velocidade |
| **Power** | Potência constante (alternativa à curva H-Q) |

> Se a bomba exigir uma curva de eficiência para cálculo de energia, defina-a no **Editor de padrões e curvas** e faça referência a ela nas propriedades da bomba.
