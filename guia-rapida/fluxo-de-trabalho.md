# Fluxo de trabalho típico

Este é o caminho usual para construir, verificar e simular uma rede de distribuição com QGISRed.

---

## Passo 1 — Crie ou abra o projeto

Use a barra **Geral** para começar:

- **Novo projeto do zero**: _Criar projeto_ → escolha nome, pasta e sistema de referência. QGISRed gera automaticamente as 6 PCHs básicas (Junções, Tubulações, RNVs, RNFs, Válvulas, Bombas).
- **Projeto existente**: _Gerente de projeto_ → clique duas vezes no projeto na lista recente.
- **De um arquivo EPANET**: _Importar projeto_ → selecione `.inp`. QGISRed converte para SHP e abre.

## Passo 2 — Configurar opções do projeto

Na barra **Projeto**, acesse _Opções de Projeto_ para definir:
- **Unidades de fluxo** (LPS, GPM, CMH…)
- **Fórmula de perda de carga** (D-W, H-W, C-M)
- **Modelo de Qualidade** (Nenhum, Cloro, Idade, Marcador)

O indicador na barra principal (`LPS | D-W`) sempre reflete os valores ativos.

## Passo 3 — Construa a rede

Ative a barra **Edição** e desenhe a rede no mapa:

1. Comece com os **tubos** — os nós extremos se criam sozinhos.
2. Adicione **RNVs e RNFs** clicando nos nós existentes.
3. Insira **válvulas e bombas** clicando em um tubo.
4. Edite as **propriedades** de cada elemento (diâmetro, rugosidade, dimensão, demanda...).

> 💡 Você pode importar geometria existente (infraestrutura SHP, ortofoto de fundo) e plotar a rede em cima dela.

## Passo 4 — Verifique a qualidade do modelo

Antes de simular, use a barra **Debug**:

1. **Consolidar e revisar dados** — detecta atributos incompletos ou inconsistentes.
2. **Verifique a conectividade** — identifica áreas isoladas sem fonte de pressão.
3. **Setores hidráulicos** — verifique a alimentação de cada setor.

Corrija quaisquer problemas observados no relatório de incidente antes de continuar.

## Passo 5 — Preparar dados de demanda

Na barra **Ferramentas**:

- **Interpolar elevações** se os nós não possuem elevações atribuídas.
- **Atribuir rugosidade** com base no material e na data de instalação.
- **Gerenciador de demanda** para distribuição de consumo.

## Passo 6 — Simular

Na barra **Análise**:

1. _Opções de análise_ — verifique a duração e o intervalo de tempo.
2. _Modelo de execução_ — a simulação pode levar de um segundo a vários minutos dependendo do tamanho da rede.
3. Ao terminar, o QGISRed carrega automaticamente as camadas de resultados e abre o **Visualizador de resultados**.

## Passo 7 — Explorar os resultados

No painel lateral do Results Viewer:

- Selecione qual **variável** mostrar nos nós (Pressão, Demanda, Qualidade) e nas tubulações (Fluxo, Velocidade, Perda Unitária...).
- Mova o **controle deslizante de tempo** para ver a evolução ao longo do período simulado.
- Ative **Map Notices** para ler valores ao passar o mouse sobre qualquer elemento.
- Use **Séries Temporais** para representar graficamente a evolução de um ponto específico.

## Passo 8 — Salvar

- _Save Map_ salva o projeto QGIS (`.qgz`) com as camadas e estilos visíveis.
- _Exportar projeto_ (do Gerente de Projeto) gera um ZIP portátil do projeto.

---

> ❗ **IMPORTANTE**: QGISRed não modifica as camadas enquanto elas estão no **Modo de Edição** do QGIS. Certifique-se de confirmar (`Ctrl+S` na camada) ou descartar suas alterações antes de usar qualquer ferramenta de plugin.
