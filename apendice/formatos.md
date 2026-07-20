# Formatos e gerenciamento de DBF

Referência para usuários que editam dados do projeto diretamente nas tabelas de atributos do QGIS ou a partir de ferramentas externas, sem passar pelas caixas de diálogo do QGISRed.

---

## Formato da data

O campo `InstalDate` da camada `Pipes` armazena a data de instalação como uma string de texto no formato:

```
yyyyMMdd
```

| Componente | Descrição | Exemplo |
|------------|-------------|---------|
| `yyyy` | Ano (4 dígitos) | `2023` |
| `MM` | Mês (2 dígitos, com zero à esquerda) | `07` |
| `dd` | Dia (2 dígitos, com zero à esquerda) | `15` |

**Exemplo correto**: `20230715` (15 de julho de 2023)

Se o valor não seguir esse formato exato, a ferramenta **Verificar datas de instalação do tubo** (barra de depuração) sinalizará isso como um problema e a ferramenta **Definir coeficientes de rugosidade** (barra de ferramentas) não será capaz de calcular a rugosidade de envelhecimento desse tubo.

---

## Padrões e Curvas (DBF)

Os padrões e curvas de demanda (H-Q, eficiência, volume) são armazenados em tabelas DBF separadas. Se você editá-los diretamente fora do QGIS:

- **Separador decimal**: Sempre use o **ponto** (`.`), independentemente da localidade do sistema. Vírgulas como separador decimal causam erros de leitura.
- **Campo de ordem**: cada tabela possui um campo de ordem numérica (`Order` ou similar) que determina a sequência dos pontos ou fatores dentro da série. Não altere este campo nem deixe lacunas na numeração.

---

## Regras

As regras de controle são armazenadas como registros individuais na tabela DBF de regras. Cada regra ocupa várias linhas (uma por linha lógica: IF, AND, OR, THEN, ELSE). Se você visualizar a tabela fora do gerenciador de regras QGISRed, classifique as linhas por estas duas colunas nesta ordem para que as regras sejam legíveis:

1. **`RuleOrder`** — agrupa todas as linhas da mesma regra.
2. **`LineOrder`** — define a ordem lógica das condições dentro de cada regra.

O campo **`Name`** armazena um rótulo descritivo visível no gerenciador de regras. Não afeta a simulação e pode ficar vazio.
