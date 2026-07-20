# Gerenciador de camadas e legenda

---

## Gerenciador de camadas

**Barra de projeto → Gerenciador de camadas** (Gerenciador de camadas)

Controla quais camadas do projeto estão ativas no QGIS e permite recuperar camadas que foram excluídas acidentalmente.

<figure><img src="../assets/images/proyecto/gestor-capas.png" alt="Caixa de diálogo Gerenciador de camadas QGISRed"><figcaption><p>Caixa de diálogo Gerenciador de camadas QGISRed</p></figcaption></figure>
*Gerenciador de camadas: lista de todas as camadas do projeto com seu status de carregamento.*

### Camadas base (Entradas)

Mostra os 6 elementos base do EPANET mais as camadas opcionais (Múltiplas Demandas, Fontes, Conexões de Serviço, Válvulas de Isolamento, Medidores). Para cada um indique se está carregado no QGIS ou não.

- **Caixa marcada** → a camada é carregada e visível na legenda do QGIS.
- **Caixa desmarcada** → a camada existe no disco, mas não está carregada.

Você pode marcar ou desmarcar qualquer camada para fazer upload ou download sem afetar os dados.

### Recuperar uma camada excluída

Se você acidentalmente excluiu uma camada da legenda QGIS (ou seu arquivo SHP no disco), o Gerenciador de camadas permite **recriá-la vazia**:

1. Selecione a camada que falta (ela aparecerá com um ícone de aviso).
2. Pressione **Recuperar** (ou o botão equivalente dependendo da versão).
3. QGISRed cria o SHP vazio com a estrutura de campo correta e carrega-o no QGIS.

> ⚠️ A recuperação cria a camada vazia. Os dados que estavam nele (se o SHP foi apagado do disco) não podem ser recuperados a menos que você tenha uma cópia de backup.

### Resumo do modelo (Resumo)

**Barra do projeto → Resumo**

Gere um relatório rápido com a quantidade de elementos de cada tipo presentes no projeto:

```
Junctions: 1 243
Pipes: 1 876
Tanks: 3
Reservoirs: 2
Valves: 47
Pumps: 8
```

Útil para verificar se a importação foi concluída ou para documentar o tamanho do modelo.

---

## Editor de legenda

**Barra do projeto → Editor de legendas** (Editor de legendas)

Abre um painel flutuante que permite personalizar a **simbologia** das camadas do projeto sem ter que navegar pelo menu de propriedades da camada QGIS.

<figure><img src="../assets/images/proyecto/editor-leyenda.png" alt="Painel do Editor de Legenda QGISRed"><figcaption><p>Painel do Editor de Legenda QGISRed</p></figcaption></figure>
*Painel Editor de legendas: estilos predefinidos e personalização de cores e tamanhos.*

### Estilos predefinidos

QGISRed inclui estilos QML predefinidos para cada tipo de elemento, adaptados ao sistema de unidades do projeto (SI/US). O editor permite que você aplique estes estilos com um único clique:

- Estilo por **material** (codificação de cores por material do tubo)
- Estilo por **diâmetro** (escala de cores proporcional ao diâmetro)
- Estilo por **comprimento**
- Estilo **base** (cores QGISRed padrão)

### Personalização manual

Para cada camada você pode ajustar:
- Cor de preenchimento e borda para elementos pontuais
- Cor e espessura de linha para tubos
- Tamanho do símbolo

As alterações são salvas no arquivo de projeto QGIS `.qgz`. Se você não tiver o `.qgz` salvo, os estilos personalizados serão perdidos quando você fechar o QGIS.

> 💡 Se você alterar a versão do plugin e os estilos forem redefinidos ao abrir o projeto, é normal: QGISRed detecta a mudança de versão e aplica os estilos padrão atualizados. Você pode personalizar novamente no Editor de legendas.
