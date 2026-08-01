# Topologia e Conectividade

As ferramentas do primeiro grupo da barra Debug detectam e corrigem os erros estruturais mais comuns: elementos duplicados, vértices desnecessários, tubos fragmentados e áreas desconectadas. É aconselhável executá-los na ordem em que aparecem na barra antes de simular pela primeira vez.

---

## Verifica && dados de commit

**Barra de depuração → Verificar && dados de confirmação**

É a principal ferramenta de validação. Percorre todos os elementos do projeto, verifica a consistência dos dados (dimensões, diâmetros, IDs duplicados, referências a curvas e padrões inexistentes, etc.) e **consolida alterações pendentes**.

### O que é válido

- IDs duplicados em qualquer camada.
- Tubulações sem nós finais válidos (conectividade quebrada).
- Referências a curvas ou padrões que não existem no projeto.
- Valores obrigatórios vazios (diâmetro nulo, dimensão vazia...).
- Consistência interna do arquivo `_Options.dbf`.

### Resultado

- Se tudo for válido: mensagem _"Dados de entrada são válidos"_ em verde.
- Se houver erros: lista de problemas com o ID e tipo do elemento afetado. Itens com erros são selecionados automaticamente no mapa para facilitar sua localização.

> Execute **Check && commit data** sempre que você tiver editado a tabela de atributos manualmente (fora da caixa de diálogo de propriedades), pois essas alterações não passam pela validação automática do plugin.

---

## Remover elementos sobrepostos

**Barra de depuração → Remover elementos sobrepostos**

Detecta elementos que compartilham exatamente a mesma posição geográfica: nós em nós, tubulações em tubulações ou nós no final de outra camada.

### Quando aparecem duplicatas

- Ao importar de um `.inp` com coordenadas arredondadas.
- Ao combinar dados de diferentes fontes GIS.
- Ao copiar e colar elementos sem verificar a sobreposição.

### Operação

A ferramenta opera na seleção atual ou em toda a rede se não houver seleção. Elimina o elemento duplicado, mantendo aquele com maior número de conexões ou, em caso de empate, aquele com menor ID. Os atributos do elemento removido são descartados.

> Execute esta ferramenta **antes de criar conexões T** e **antes de verificar a conectividade** para evitar falsos positivos de conectividade causados ​​por nós duplicados.

---

## Simplifique os vértices do link

**Barra de depuração → Simplificar vértices de link**

Remove vértices intermediários alinhados (dentro de um limite de tolerância angular) com segmentos adjacentes. Esses vértices não fornecem informações geométricas, mas aumentam o tamanho do SHP e retardam a renderização.

### Quando é útil

- Após importar do AutoCAD ou GIS municipal onde as linhas possuem vértices a cada poucos centímetros.
- Depois de usar ferramentas externas de suavização que adicionam pontos desnecessários.

### O que preserva

Os vértices nos pontos de quebra reais (mudança de direção) não são removidos. Somente são eliminados aqueles que caem na extensão do segmento anterior, dentro do ângulo de tolerância interna do plugin.

---

## Unir tubos consecutivos

**Barra de depuração → Unir tubos consecutivos (= diâmetro, material e ano)**

Mesclar tubos adjacentes quando eles compartilharem **todos os três atributos**: diâmetro, material e ano de instalação. O nó intermediário é removido se não estiver em demanda ou conectado a outras camadas.

### Resultado

Tubulações que foram previamente fragmentadas (por importação do GIS, por divisões anteriores ou por design incremental) são mescladas em uma única seção. Isto:
- Reduz o número de elementos do modelo.
- Simplifica a tabela de atributos.
- Melhora o desempenho da simulação.

> Se o nó intermediário tiver demanda atribuída diferente de zero, o pipeline **não** será mesclado. QGISRed preserva o nó para não perder dados de consumo.

---

## Criar conexões T

**Barra de depuração → Criar conexões T**

Detecta automaticamente situações em que a extremidade de uma tubulação (ou nó de demanda) cai no trajeto de outra tubulação, sem estar conectada a ela. Nesses casos, o plugin divide o pipe e cria o nó de união.

### Problema que resolve

Ao digitalizar redes manualmente, é comum que um ramal fique “flutuando” acima do principal sem se conectar topologicamente. Visualmente parece correto, mas na simulação esse ramo não tem conexão real. Esta ferramenta detecta e corrige automaticamente.

### Tolerância

Usa a tolerância de nó configurada em **Barra de Projeto → Valores Padrão**. Se a extremidade do tubo for menor que aquela distância do eixo de outro tubo, é considerado um T a ser resolvido.

---

## Verifique a conectividade

**Barra de depuração → Verifique a conectividade** *(com a subopção Excluir subzonas isoladas)*

Analisa a conectividade de toda a rede desde as fontes de abastecimento (RNFs e RNVs). Identifique quais tubos e nós **não estão conectados** a nenhuma fonte.

<figure><img src="../assets/images/debug/check-connectivity.png" alt="Verifique o resultado da conectividade: áreas isoladas coloridas em vermelho no mapa"><figcaption><p>Verifique o resultado da conectividade: áreas isoladas coloridas em vermelho no mapa</p></figcaption></figure>
*Áreas isoladas identificadas: em vermelho os elementos sem ligação com nenhuma fonte.*

### Opção 1: verificar a conectividade (somente exibição)

Pinte os elementos de acordo com sua zona de conectividade. Os itens não conectados a nenhuma fonte são destacados. Não modifica a rede.

### Opção 2: Excluir subzonas isoladas

Abre uma caixa de diálogo que solicita o **número máximo de tubos** em uma subzona para exclusão. Subzonas com esse número de tubos ou menos são excluídas automaticamente. Os maiores são preservados mesmo isolados (podem ser setores válidos ainda não conectados).

Este limite é útil para limpar "lixo" topológico - fragmentos de 1 a 3 tubos deixados soltos após uma importação.

> Sempre execute **Remover elementos sobrepostos** antes de **Verificar conectividade** para evitar que nós duplicados gerem falsos isolamentos.
