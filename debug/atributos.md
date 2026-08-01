# Verificação de atributos

As quatro ferramentas do segundo grupo da barra Debug auditam os **dados alfanuméricos** dos tubos para detectar erros de transcrição, valores inconsistentes ou campos vazios que impediriam uma simulação correta ou o cálculo da rugosidade do envelhecimento.

Todos operam na seleção atual ou em toda a rede se não houver seleção anterior.

---

## Verifique os comprimentos dos tubos

**Barra de depuração → Verifique os comprimentos dos tubos**

Compara o **comprimento armazenado no atributo `Length`** de cada tubo com o **comprimento geométrico real** calculado a partir dos vértices do SHP.

### Diálogo de Tolerância

Ao ativar a ferramenta, uma caixa de diálogo é aberta onde você define:

| Campo | Descrição |
|-------|-------------|
| **Tolerância (%)** | Diferença percentual máxima aceitável entre o comprimento do atributo e o comprimento geométrico |
| **Duração da atualização** | Se marcada, substitui o valor do atributo pelo comprimento geométrico em todas as tubulações que excedem a tolerância |

### Quando diferenças aparecem

- Tubos importados de um `.inp` onde `Length` foi calculado com uma escala diferente.
- Tubulações cuja geometria foi modificada (vértices movidos) sem atualização do atributo.
- Redes em CRS projetado vs. geográficas: se as coordenadas de `.inp` estiverem em graus e usadas como metros, as longitudes estão incorretas.

> QGISRed calcula o comprimento geométrico sempre nas unidades CRS do projeto. Se o projeto utilizar coordenadas geográficas (graus), as longitudes estarão incorretas. Sempre use um CRS métrico projetado.

---

## Verifique os diâmetros

**Barra de depuração → Verifique os diâmetros**

Revise os diâmetros de todos os tubos selecionados (ou de toda a rede) e aponte aqueles que estão fora da faixa usual ou são zero.

### O que detecta

- Tubos com diâmetro **zero ou negativo** (erro de importação ou edição manual).
- Tubos com diâmetros estatisticamente atípicos em relação ao resto do modelo (valores extremamente altos ou baixos).
- Tubulações sem diâmetro atribuído (campo vazio).

### Resultado

As feições com diâmetros problemáticos são selecionadas no mapa e um resumo é exibido no painel de mensagens. Não modifica automaticamente nenhum valor: a correção deve ser feita manualmente a partir da caixa de diálogo de propriedades ou tabela de atributos.

---

## Verifique os materiais dos tubos

**Barra de depuração → Verifique os materiais do tubo**

Verifique se o valor do campo `Material` de cada tubo está definido na **Tabela de Materiais do Projeto** (Barra do Projeto → Tabela de Materiais).

### O que detecta

- Tubos vazios ou sem material.
- Tubulações com código de material que não existe na tabela do projeto (por exemplo, código herdado de outro sistema GIS).
- Tubos com valor `UNKNOWN` (valor padrão quando o material não é conhecido).

### Por que é importante

O material é essencial para a ferramenta **Atribuir Rugosidades** (Barra de Ferramentas), que calcula a rugosidade de envelhecimento com base no material e na data de instalação. Se o material for inválido, a rugosidade não poderá ser calculada.

---

## Verifique as datas de instalação da tubulação

**Barra de depuração → Verifique as datas de instalação dos tubos**

Verifica o campo das tubulações `InstallYear`, que armazena o ano de instalação em formato numérico (`YYYY`).

### O que detecta

| Problema | Descrição |
|----------|-------------|
| **Data vazia** | Campo `InstallYear` nulo ou zero |
| **Data futura** | Ano superior ao ano em curso |
| **Formato incorreto** | Valores não numéricos ou fora do intervalo razoável (antes de 1800 ou após o ano em curso) |

### Por que é importante

A data de instalação, combinada com o material, permite calcular a **rugosidade atual** de cada tubo usando a fórmula de envelhecimento:

```
Rugosidade = Rugosidade_inicial + (Ano_atual − InstallYear) × Aumento_anual
```

Se a data estiver incorreta, a rugosidade calculada estará errada e a simulação hidráulica produzirá resultados distantes da realidade.
