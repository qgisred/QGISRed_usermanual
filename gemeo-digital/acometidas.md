# Conexões e Válvulas de Corte

As ligações e válvulas de corte são os dois elementos que ligam o modelo hidráulico à realidade operacional da rede: as ligações representam a ligação individual com cada cliente e as válvulas de corte permitem modelar o isolamento dos sectores sem necessidade de modificar a topologia do modelo EPANET.

---

## Adicionar conexão de serviço

**Digital Twin Bar → Adicionar conexão de serviço**

Desenha uma gota como uma polilinha do tubo principal até o ponto de entrega do cliente. A conexão é armazenada na camada complementar `ServiceConnections` do projeto.

<figure><img src="../assets/images/gemelo-digital/add-service-connection.png" alt="Ferramenta de desenho de conexão no mapa"><figcaption><p>Ferramenta de desenho de conexão no mapa</p></figcaption></figure>
*Desenho do serviço: a linha parte da tubulação principal e chega até o limite do terreno do cliente.*

### Processo

1. Ative **Adicionar conexão de serviço**. O cursor muda para o modo de desenho de linha.
2. Clique no tubo principal no ponto de entrada.
3. Clique nos pontos intermediários do traçado caso a conexão não seja reta.
4. Clique duas vezes no ponto final (limite do gráfico ou contador) para completar o layout.
5. QGISRed chama o mecanismo C# (`GISRed.AddConnection`) e atualiza a camada `ServiceConnections`.

A conexão herda automaticamente o nó de conexão mais próximo da rede principal. O campo `IsActive` de cada conexão permite ativar ou desativar a alimentação individualmente sem excluir o elemento.

---

## Adicionar válvula de isolamento

**Barra Dupla Digital → Adicionar válvula de isolamento**

Adicione uma válvula de corte manual a um tubo existente clicando nele. As válvulas de corte são armazenadas na camada complementar `IsolationValves` e não são elementos EPANET: não aparecem na simulação mas aparecem na análise de segmentos isolados (**Segmentos isolados**, barra de ferramentas).

### Processo

1. Ative **Adicionar válvula de isolamento**.
2. Clique no tubo no ponto onde deseja colocar a válvula.
3. QGISRed insere-o na camada `IsolationValves` e representa-o no mapa.

### Relação com simulação

As válvulas de corte por si só não modificam o modelo EPANET. Para que seu status (aberto/fechado) afete a simulação, utilize a ferramenta **Definir status inicial do tubo a partir de válvulas de isolamento** no Grupo 2.

---

## Converta conexões de serviço em pipes/nós

**Digital Twin Bar → Converta conexões de serviço em tubos/nós**

Incorpora as ligações traçadas em `ServiceConnections` ao modelo EPANET ativo. Requer que a camada `ServiceConnections` exista e contenha pelo menos uma conexão.

### Opções de conversão

Ao executar a ferramenta, uma caixa de diálogo aparece com duas opções:

| Opção | Resultado no modelo |
|--------|------------------------|
| **Como nós** | Cada conexão se torna um nó de demanda pontual no ponto de conexão com o pipeline principal. A geometria da conexão não entra no modelo. |
| **Como tubos** | Cada conexão se transforma em um tubo de pequeno diâmetro que vai do nó de captação até um novo nó final. Permite simular perdas na conexão do cliente. |

### Quando usar cada opção

- **Como nós**: quando o único interesse é incorporar a demanda do cliente ao modelo sem simular as perdas internas da conexão. É a opção usual para redes de distribuição em escala de bairro ou cidade.
- **Como tubos**: quando se deseja simular redes de assinantes com diâmetros de conexão reais, ou quando o comprimento da conexão é significativo em relação à rede principal.

> Esta operação modifica o modelo EPANET (camada `Junctions` e/ou `Pipes`). Salve o projeto antes de executá-lo se quiser manter o estado anterior.
