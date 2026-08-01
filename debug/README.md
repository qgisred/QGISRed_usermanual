# ✅ Depurar

A barra **Debug** agrupa as ferramentas de verificação e depuração do modelo. O seu objectivo é detectar e corrigir erros topológicos, inconsistências de atributos e problemas de conectividade **antes de iniciar a simulação**, evitando assim erros de difícil diagnóstico no EPANET.

<figure><img src="../assets/images/debug/barra-debug.png" alt="Barra de ferramentas de depuração QGISRed"><figcaption><p>Barra de ferramentas de depuração QGISRed</p></figcaption></figure>
*Barra de depuração: validação de dados, depuração topológica, revisão de atributos e setores hidráulicos.*

---

## Ferramentas da barra de depuração

### Grupo 1 — Topologia e coerência

| # | Ferramenta | Função |
|---|-------------|---------|
| 1 | **Verificar && confirmar dados** | Valida todos os dados do modelo e sinaliza elementos com erros |
| 2 | **Remover elementos sobrepostos** | Detectar e remover nós ou tubos duplicados na mesma posição |
| 3 | **Simplifique os vértices do link** | Elimina vértices intermediários alinhados em trechos retos |
| 4 | **Junte-se a pipes consecutivos** | Unir tubos adjacentes com diâmetro, material e ano idênticos |
| 5 | **Criar conexões T** | Detecta nós finais em tubos e cria a junção topológica |
| 6 | **Verifique a conectividade** | Identifica áreas isoladas de fontes de abastecimento |
| — | *Excluir subzonas isoladas* | (Subopção) Elimina subzonas com menos tubagens do que o limite definido |

### Grupo 2 — Verificação de atributos

| # | Ferramenta | Função |
|---|-------------|---------|
| 7 | **Verifique os comprimentos dos tubos** | Compare comprimentos de atributos versus geometria e aponta diferenças |
| 8 | **Verificar diâmetros** | Detecta diâmetros fora da faixa usual do projeto |
| 9 | **Verifique os materiais dos tubos** | Detecta materiais indefinidos na tabela de materiais do projeto |
| 10 | **Verifique as datas de instalação da tubulação** | Detectar datas de instalação formatadas incorretamente ou inconsistentes |

### Grupo 3 — Setores hidráulicos

| # | Ferramenta | Função |
|---|-------------|---------|
| 11 | **Verificar setores hidráulicos** | Classifica as áreas da rede de acordo com a sua capacidade de oferta (tipos A–D) |

---

## Nesta seção

* [Topologia e conectividade](topologia.md) — commit, sobreposição, simplificação, junção, conexões T, conectividade
* [Verificação de atributos](atributos.md) — comprimentos, diâmetros, materiais, datas de instalação
* [Setores hidráulicos](setores-hidraulicos.md) — classificação dos setores tipo A, B, C e D
