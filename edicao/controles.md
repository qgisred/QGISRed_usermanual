# Controles e Regras

**Barra de edição → Editar controles…**

O editor de controles define a **lógica operacional** da rede: quando uma válvula abre, quando uma bomba inicia ou qual sequência de ações aciona um determinado estado do sistema. O EPANET suporta dois níveis de controlo com complexidade diferente.

<figure><img src="../assets/images/edicion/editor-controles.png" alt="Editor de regras e controles QGISRed"><figcaption><p>Editor de regras e controles QGISRed</p></figcaption></figure>
*Editor de controles: guias simples de controles e regras, seletor de elementos e condições.*

---

## Controles Simples

Um controle simples define uma **ação única** que é executada quando uma **condição única** é atendida. Eles são suficientes para a maioria das automações básicas.

### Estrutura

```
IF [elemento] [condição]  THEN [ação]
```

### Tipos de condição

| Tipo | Exemplo de uso |
|------|---------------|
| **Nível do RNV** | Se o nível do RNV T-1 ultrapassar 4,5 m → fechar a bomba BM-1 |
| **Pressão do nó** | Se a pressão no J-120 cair abaixo de 10 m → abrir a válvula V-3 |
| **Tempo de simulação** | Às 6 horas de simulação → ligar a bomba BM-2 |
| **Relógio** | Às 23h (horário) → fechamento do gasoduto P-55 |

### Ações disponíveis

| Ação | Aplica-se a |
|--------|---------|
| **ABERTO** | Canos, válvulas, bombas |
| **FECHADO** | Canos, válvulas, bombas |
| **Configuração = valor** | Válvulas (altera o setpoint de regulação) |
| **Velocidade = valor** | Bombas (muda a velocidade relativa) |

### Exemplo completo

```
; Ligar bomba quando o RNV estiver baixo
IF TANK T-DEPOSITO1 LEVEL BELOW 1.5
THEN PUMP BM-ELEVADORA OPEN

; Parar bomba quando o RNV estiver cheio
IF TANK T-DEPOSITO1 LEVEL ABOVE 4.0
THEN PUMP BM-ELEVADORA CLOSED

; Ligar bomba de reforço no horário de pico
IF CLOCKTIME 7:00 AM
THEN PUMP BM-REFUERZO OPEN

IF CLOCKTIME 10:00 AM
THEN PUMP BM-REFUERZO CLOSED
```

---

## Regras de funcionamento (Regras)

As regras permitem combinar **múltiplas condições** com operadores lógicos, bem como definir ações e prioridades alternativas. São equivalentes ao `[RULES]` do arquivo EPANET `.inp`.

### Estrutura geral

```
RULE [ID]
IF   [condição 1]
AND  [condição 2]          (opcional)
OR   [condição alternativa] (opcional)
THEN [ação principal]
ELSE [ação alternativa]   (opcional)
PRIORITY [número]           (opcional)
```

### Operadores lógicos

| Operador | Uso |
|----------|-----|
| **E** | Todas as condições devem ser satisfeitas simultaneamente |
| **OU** | Basta que qualquer uma das condições seja cumprida |

### PRIORIDADE

Quando duas regras com condições conflitantes são ativadas ao mesmo tempo, aquela com o **número de prioridade mais alto** vence. O valor padrão é 0.

### Exemplo completo

```
RULE R-01
IF   TANK T-DEP1 LEVEL BELOW 2.0
AND  PUMP BM-ELEV STATUS = CLOSED
THEN PUMP BM-ELEV OPEN
PRIORITY 2

RULE R-02
IF   NODE J-SALIDARED PRESSURE BELOW 8.0
OR   TANK T-DEP1 LEVEL BELOW 1.0
THEN PUMP BM-REFUERZO OPEN
ELSE PUMP BM-REFUERZO CLOSED
PRIORITY 1
```

---

## Edição no QGISRed

A caixa de diálogo QGISRed apresenta as regras em formato de texto editável diretamente, equivalente à seção `[CONTROLS]` e `[RULES]` do arquivo `.inp`. Você pode:

- **Escreva** controles e regras diretamente na área de texto.
- **Ative ou desative** uma regra colocando um `;` no início (converte a linha em um comentário).
- **Verifique a sintaxe** com o botão de validação antes de salvar.

> Os controles são exportados exatamente como aparecem ao gerar o `.inp` na barra de ferramentas. Se a sintaxe estiver incorreta, o EPANET rejeitará o arquivo na simulação.

---

## Dicas de modelagem

- Para sistema com bomba e RNV, defina sempre **dois controles por bomba**: um para partida (nível baixo) e outro para parada (nível alto). Sem o controlo de paragem, a bomba funciona indefinidamente.
- Controles simples são processados ​​**antes** das regras em cada intervalo de tempo. Se você tiver um controle simples e uma regra que atue no mesmo elemento, o resultado pode ser contraditório.
- A ordem dos controles simples **não importa**; nem o das regras, porque a prioridade as ordena. Mas se duas regras têm a mesma prioridade e condições contraditórias, o resultado é indeterminado.
- Evite criar loops de controlo (a regra A activa B, a regra B desactiva A no mesmo intervalo de tempo): o EPANET pode não convergir.
