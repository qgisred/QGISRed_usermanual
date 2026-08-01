# Padrões e Curvas

**Edição Barra → Editar padrões e curvas…**

O editor de padrões e curvas centraliza a gestão de dados temporais e funcionais que controlam o comportamento dinâmico do modelo: como a demanda varia ao longo do dia, como uma bomba se comporta de acordo com sua vazão ou qual o volume de um RNV irregular.

<figure><img src="../assets/images/edicion/editor-curvas.png" alt="Editor de padrões e curvas QGISRed"><figcaption><p>Editor de padrões e curvas QGISRed</p></figcaption></figure>
*Editor de padrões e curvas: lista de elementos à esquerda, gráfico e tabela de dados à direita.*

---

## Padrões de Demanda (Padrões)

Um padrão define como você multiplica a demanda base de um nó (ou outro parâmetro) em cada intervalo de tempo de simulação.

### Estrutura de um padrão

Cada padrão possui:
- Um **ID** exclusivo (referenciado nos nós ou bombas).
- Uma lista de **fatores multiplicadores**, um por intervalo de tempo.
- O **passo de tempo do padrão** é definido nas opções de simulação; Se o padrão tiver menos fatores que intervalos de simulação, os valores são repetidos ciclicamente.

### Exemplo

Um padrão de 24 fatores de tempo para uma simulação de 24 horas:

```
ID: DomResidential
Factores: 0.4  0.3  0.3  0.3  0.4  0.7  1.1  1.3  1.2  1.0  0.9  0.9
          1.0  1.1  1.0  0.9  1.0  1.2  1.3  1.2  1.0  0.8  0.6  0.4
```

O nó com demanda base 2,0 L/s e padrão `DomResidential` consome 0,8 L/s às 0 h (2,0 × 0,4) e 2,6 L/s às 7 h (2,0 × 1,3).

### Edição na caixa de diálogo

1. Selecione um padrão existente na lista ou pressione **Novo** para criar um.
2. Insira os fatores na tabela (uma linha por intervalo).
3. O gráfico é atualizado em tempo real.
4. Você pode **importar fatores de CSV** (uma coluna de valores numéricos) usando o botão de importação.

---

## Curvas de comportamento (Curvas)

As curvas relacionam duas grandezas físicas. O EPANET utiliza quatro tipos:

### Curva H-Q da bomba (curva da bomba)

Relaciona a **Altura Manométrica** (Cabeça, eixo Y) com o **Fluxo** (Fluxo, eixo X). Define o ponto de trabalho da bomba na velocidade nominal.

| Número de pontos | Método de ajuste |
|--------------|-----------------|
| 1 ponto | QGISRed ajusta-se à curva padrão EPANET: H₀ = 133% do ponto, dado Q₀, Hmax = 0 a 2×Q₀ |
| 3 pontos | Ajuste polinomial de segundo grau passando pelos três pontos |
| N pontos | Interpolação linear entre pontos (curva livre) |

> A curva H-Q deve ter **inclinação negativa** (altura manométrica maior com vazão menor). O EPANET avisará se a curva tiver inclinação positiva em algum trecho.

### Curva de eficiência (curva de eficiência)

Relaciona **Eficiência** (%) a **Fluxo** (Fluxo). É usado para análise de consumo de energia. Se não for definido, o EPANET utiliza a eficiência global do projecto.

### Curva de volume (curva de volume)

Relaciona o **Nível** do RNV (m ou pés, eixo X) ao **Volume** armazenado (m³ ou galões, eixo Y). Necessário para RNVs com geometria não cilíndrica (bacias cônicas, RNVs de formato irregular).

### Curva de perda de carga GPV (curva de perda de carga)

Para válvulas do tipo **GPV** (Válvula de Uso Geral), relacione a **Perda de carga** (m ou pés) ao **Fluxo** (Fluxo). Permite modelar qualquer dispositivo de controle hidráulico cuja curva característica seja conhecida.

---

## Criar e editar curvas

1. Selecione o tipo de curva no seletor superior.
2. Escolha uma curva existente na lista ou pressione **Novo**.
3. Insira os pares de pontos (X, Y) na tabela.
4. O gráfico mostra a curva resultante com a interpolação ou ajuste correspondente.
5. Pressione **OK** para salvar. As curvas são armazenadas em `{Red}_Options.dbf`.

> Para fazer referência a uma curva de uma bomba ou RNV, copie seu **ID** exato no campo correspondente da caixa de diálogo de propriedades do elemento.
