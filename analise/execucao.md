# Execução e Opções

As três primeiras ações na barra Análise controlam o ciclo de simulação: configurar opções do mecanismo, iniciar a simulação e revisar o relatório de status.

---

## Opções de análise…

**Barra de análise → Opções de análise…**

Abre a caixa de diálogo Opções do mecanismo EPANET. Permite configurar todos os parâmetros que controlam a forma como é realizada a simulação hidráulica e de qualidade.

<figure><img src="../assets/images/analisis/analysis-options.png" alt="Caixa de diálogo Opções de análise com guias de configuração do mecanismo EPANET"><figcaption><p>Caixa de diálogo Opções de análise com guias de configuração do mecanismo EPANET</p></figcaption></figure>
*Caixa de diálogo Opções de análise: configuração completa do motor EPANET.*

### Parâmetros configuráveis ​​

| Grupo | Parâmetros principais |
|-------|------------------------|
| **Hidráulica** | Unidades de fluxo (LPS, GPM, CMH…), fórmula de perda de carga (H-W / D-W / CM), viscosidade, gravidade específica |
| **Qualidade** | Tipo de análise de qualidade (nenhuma, cloro, idade da água, vestígios de origem), coeficientes de reacção |
| **Tempos** | Duração total da simulação, etapa de tempo hidráulico, etapa de qualidade, etapa de relatório, hora de início |
| **Energia** | Preço da electricidade, eficiência global das bombas |
| **Geral** | Modo PDA (Pressure Dependent Analysis): ativa a demanda local dependente da pressão |

> A Tabela de Materiais do Projeto armazena a rugosidade em unidades D-W (mm). Se você alterar a fórmula hidráulica aqui, o QGISRed oferecerá a conversão automática dos coeficientes de rugosidade existentes.

---

## Executar modelo

**Barra de análise → Executar modelo**

Inicie a simulação EPANET com as opções configuradas e carregue os resultados no painel de resultados.

### Processo

1. QGISRed valida o projeto (camadas ativas, nenhuma camada sendo editada).
2. Chame o motor EPANET através do kit de ferramentas QGISRed.
3. Ao terminar, ele abre automaticamente o encaixe Resultados à direita da tela e carrega os dados calculados.
4. O mapa atualiza a simbologia da camada com os valores do primeiro instante de tempo disponível.

Se a simulação detectar problemas (pressões negativas, nós desconectados, bombas em cavitação), o relatório de status os registra em nível de alerta.

### Opções de diálogo de progresso

A caixa de diálogo de progresso inclui um botão **Pausar** (ícone ‖). Quando pressionado, a simulação para no final do intervalo de tempo atual e o ícone muda para ▶. Pressionar novamente retoma a execução. O botão desaparece assim que a simulação for concluída.

A caixa de diálogo também inclui a caixa de seleção **"Não mostrar esta janela de progresso novamente"**. Se você marcá-la e a simulação terminar com êxito, as execuções subsequentes iniciarão o cálculo diretamente, sem exibir a caixa de diálogo.

> ⚠️ **Exceção para grandes redes**: se o produto (número de nós: junções + tanques + reservatórios) × (número de instantes de cálculo = Duração / intervalo de tempo hidráulico) exceder **500.000**, a caixa de diálogo de progresso é sempre mostrada nessa execução, mesmo que a caixa "Não mostrar esta janela de progresso novamente" esteja marcada em uma execução anterior. Além disso, nesse caso, a própria caixa fica oculta da caixa de diálogo, uma vez que a preferência salva permanece ineficaz durante aquela grande rede.

> Para reativar a caixa de diálogo de progresso em redes que não excedem esse limite, vá para **Propriedades do Projeto** e desmarque a opção *"Não mostrar janela de progresso ao executar a simulação"*.

> ⚠️ Quando a janela de progresso está oculta, o cursor do sistema muda para um cursor de espera em todos os aplicativos enquanto a simulação está em andamento. O cursor é restaurado automaticamente após a conclusão do cálculo.

### Mensagens de status durante a execução

A caixa de diálogo de progresso informa sobre as diferentes fases do cálculo:

- **Salvando resultados…**: indica que os resultados estão sendo gravados no disco após a conclusão do cálculo hidráulico.
- Se os arquivos de resultado (`.out`, `.hyd`) estiverem **bloqueados por outra aplicação** (por exemplo, EPANET Desktop aberto com o mesmo projeto), o plugin detecta isso e notifica o usuário com um aviso específico.

### Tratamento de erros

- Se o EPANET devolver um erro durante o cálculo, o conteúdo do relatório (`.rpt`) é automaticamente apresentado no registo de incidentes sem necessidade de procurá-lo manualmente.
- Exceções inesperadas durante o processo também são capturadas e exibidas no log, evitando falhas silenciosas.

---

## Navegador de resultados

**Barra de análise → Navegador de resultados**

Abre o painel de resultados se já existir uma simulação anterior para o projeto ativo, sem simular novamente. Se não houver resultados, inicia a simulação automaticamente.

Equivale a **Executar modelo** mas priorizando os resultados já calculados: se o arquivo `.out` existe e corresponde ao projeto atual, ele os carrega diretamente. Útil para reabrir o visualizador após fechá-lo sem perder os resultados.

---

## Relatório de status

**Barra de análise → Relatório de status**

Abre o painel de resultados diretamente na aba **Relatório de Status**, que exibe o relatório de texto gerado pelo motor EPANET após a conclusão da simulação.

O relatório inclui:

- Balanço geral de massa da rede.
- Lista de nós com pressão negativa ou fora de faixa.
- Avisos de bombas operando fora de sua curva.
- Estado de convergência do cálculo hidráulico em cada etapa.
- Resumo das reações de qualidade (caso a qualidade tenha sido simulada).

> O relatório de status é o primeiro lugar a ser consultado quando uma simulação produz resultados inesperados ou não converge.
