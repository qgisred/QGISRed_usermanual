# Propriedades Hidráulicas

As primeiras quatro ferramentas na barra de ferramentas calculam ou atualizam as propriedades hidráulicas de tubulações e nós em massa: comprimento, elevação e rugosidade. Eles funcionam na seleção atual ou em toda a rede se não houver seleção.

---

## Calcula automaticamente comprimentos de tubos

**Barra de ferramentas → Calcular comprimentos de tubos automaticamente**

Recalcula o campo `Length` de cada tubulação usando o comprimento geométrico real medido sobre os vértices da PCH nas unidades CRS do projeto.

### Quando usar

- Após mover vértices ou nós com as ferramentas de edição sem ter atualizado o atributo.
- Após importar de um `.inp` cujos comprimentos diferem da geometria real (coordenadas em escala diferente ou projeção diferente).
- Como etapa anterior para **Verificar comprimentos de tubos** (Barra de depuração) para deixar todos os valores sincronizados antes da auditoria.

A ferramenta substitui o valor de `Length` incondicionalmente em todos os tubos no escopo de seleção. Não pede confirmação nem filtro de tolerância.

> Sempre use um CRS métrico projetado (UTM, LCC, etc.). Caso o projeto utilize coordenadas geográficas (graus decimais), o comprimento calculado será em graus, e não em metros, e será inútil para a simulação.

---

## Interpolar elevação de arquivos .asc…

**Barra de ferramentas → Interpolar elevação de arquivos .asc…**

Atribui a cota (campo `Elevation`) aos nós, RNVs e RNFs do projeto interpolando seu valor a partir de um ou mais Modelos Digitais de Terreno (MDT) em formato ASC.

<figure><img src="../assets/images/herramientas/interpolate-elevation.png" alt="Seletor de arquivo ASC para interpolação de dimensão"><figcaption><p>Seletor de arquivo ASC para interpolação de dimensão</p></figcaption></figure>
*Seletor de arquivo MDT: você pode fazer upload de vários arquivos ASC para cobrir toda a área da rede.*

### Formato ASC suportado

```
ncols         500
nrows         400
xllcenter     450000.0
yllcenter     4400000.0
cellsize      5.0
nodata_value  -9999
230.4 231.1 231.8 ...
```

| Cabeçalho | Significado |
|----------|-------------|
| `ncols` / `nrows` | Número de colunas e linhas da malha |
| `xllcenter` / `yllcenter` | Coordenadas do centro da célula inferior esquerda (`xllcorner` / `yllcorner` também é aceita) |
| `cellsize` | Tamanho das células em unidades CRS |
| `nodata_value` | Valor que o plugin ignora (célula sem dados) |

### Processo de atribuição

1. Abra o seletor e escolha um ou mais arquivos `.asc`. Você pode combinar vários MDTs para cobrir toda a área da rede.
2. O QGISRed projeta a coordenada de cada nó na malha e obtém a elevação por interpolação bilinear entre as quatro células vizinhas.
3. Somente nós cujo `Elevation` atual é igual ao valor padrão (normalmente 0) são atualizados. Nós com altura já atribuída manualmente não são modificados.
4. Os nós que estão fora do alcance de todos os MDTs carregados são marcados como um incidente no quadro de mensagens.

> O CRS do arquivo ASC deve corresponder ao CRS do projeto. Se não coincidirem, as coordenadas não serão projetadas e os nós ficarão fora da malha.

---

## Definir coeficientes de rugosidade (de Material e Data)

**Barra de ferramentas → Definir coeficientes de rugosidade (de Material e Data)**

Calcula e atribui o coeficiente de rugosidade atual de cada tubo com base no seu material, no seu ano de instalação e nos parâmetros da **Tabela de Materiais** do projeto.

### Fórmula de cálculo

```
Rugosidade_atual = Rugosidade_inicial + (Ano_atual − InstallYear) × Aumento_anual
```

Onde `Rugosidade_inicial` e `Aumento_anual` são obtidos da linha da Tabela de Materiais que corresponde ao campo `Material` do tubo.

### Pré-requisitos

Antes de usar esta ferramenta, verifique na Barra de Depuração se:
1. Todos os tubos têm um `Material` válido (**Verifique os materiais dos tubos**).
2. Todos os tubos têm um `InstallYear` correto (**Verifique as datas de instalação dos tubos**).

Se algum desses campos estiver vazio ou for inválido para uma tubulação, sua rugosidade não será atualizada e será registrada como um problema.

A rugosidade é escrita nas unidades da fórmula do projeto ativo:

| Fórmula | Unidade de rugosidade |
|---------|---------------------|
| Darcy-Weisbach (DW) | mm (rugosidade absoluta da parede) |
| Hazen-Williams (HW) | Coeficiente C adimensional (típico 100–150) |
| Chezy-Manning (CM) | Coeficiente n (típico 0,010–0,020) |

> A Tabela de Materiais armazena a rugosidade inicial em unidades D-W (mm). Se o projeto utilizar H-W ou C-M, o valor calculado é automaticamente convertido para o sistema ativo.

---

## Converter coeficientes de rugosidade…

**Barra de ferramentas → Converter coeficientes de rugosidade…**

Converte os valores do campo `Roughness` de todas as tubulações entre as três fórmulas de perda de pressão. É necessário quando você altera a fórmula hidráulica do projeto e deseja que os valores existentes mantenham seu significado físico.

### Conversões disponíveis

| Origem | Destino |
|--------|---------|
| Hazen-Williams (HW) | Darcy-Weisbach (DW) |
| Darcy-Weisbach (DW) | Hazen-Williams (HW) |
| Chezy-Manning (CM) | Darcy-Weisbach (DW) |
| Darcy-Weisbach (DW) | Chezy-Manning (CM) |

Ao alterar a fórmula hidráulica em **Opções do Projeto**, o QGISRed detecta a alteração e se oferece para executar esta ferramenta automaticamente. Se você rejeitar nesse momento, poderá iniciá-lo manualmente aqui.

> A conversão DW ↔ HW usa o diâmetro e uma vazão de referência para encontrar o C que produz a mesma perda que a rugosidade DW nessa vazão. O resultado pode diferir de uma calibração direta porque as três fórmulas não são matematicamente equivalentes para todos os regimes de fluxo.
