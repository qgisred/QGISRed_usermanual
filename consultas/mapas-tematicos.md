# Mapas Temáticos

**Barra de Consultas → Mapas temáticos…**

Abre a caixa de diálogo **Mapas Temáticos**, que gera uma representação visual da rede colorindo as tubulações por intervalos de qualquer atributo hidráulico ou resultado de simulação.

<figure><img src="../assets/images/consultas/thematic-maps-dialog.png" alt="Caixa de diálogo Mapas Temáticos com seletor de campo e faixa de cores"><figcaption><p>Caixa de diálogo Mapas Temáticos com seletor de campo e faixa de cores</p></figcaption></figure>
*Diálogo de Mapas Temáticos: seleção de campos, número de classes e paleta de cores.*

---

## Elemento ativo: pipes

Na versão atual, **Mapas Temáticos funciona exclusivamente na camada Tubulações**. Opções para outros tipos de elementos (nós, válvulas, bombas, RNVs, RNFs) estão presentes na interface, mas ficam automaticamente ocultados porque ainda não estão implementados. Quando disponível, a caixa de diálogo exibirá um seletor de tipo de elemento.

---

## Processo

1. Abra **Mapas temáticos** na barra de consultas.
2. Selecione o **campo a representar** no menu suspenso (atributo de entrada ou resultado da simulação).
3. Escolha o **número de classes de cores**.
4. Selecione a **paleta de cores** (gradiente de intervalo único ou bicromático).
5. Defina o **intervalo** se desejar excluir valores extremos.
6. Confirme. QGISRed gera a camada `ThematicPipes` no grupo de camadas temáticas do painel de camadas do QGIS.

---

## Campos disponíveis para pipes

### Atributos de entrada do modelo

| Campo | Descrição |
|-------|-------------|
| `Diameter` | Diâmetro do tubo (mm) |
| `Length` | Comprimento (m) |
| `Roughness` | Coeficiente de rugosidade |
| `InstallYear` | Ano de instalação |

### Resultados da simulação

Disponível somente se houver resultados carregados no projeto:

| Campo | Descrição |
|-------|-------------|
| `Flow` | Vazão (l/s ou unidade configurada) |
| `Velocity` | Velocidade (m/s) |
| `HeadLoss` | Perda de carga (m) |
| `UnitHdLoss` | Perda unitária (m/km) |
| `FricFactor` | Fator de atrito |
| `ReactRate` | Taxa de reação (modelos de qualidade) |
| `Quality` | Qualidade da água |

---

## Resultado no mapa

A ferramenta gera a camada **`ThematicPipes`** dentro de um grupo de camadas temáticas QGISRed. A legenda de cores é exibida diretamente no painel de camadas do QGIS.

Se você executar Mapas Temáticos novamente, a camada antiga será substituída pelas novas configurações.

---

## Notas de uso

- A geração de mapas temáticos não modifica nenhum dado do modelo; apenas a simbologia da camada muda.
- Para retornar à simbologia padrão, remova a camada `ThematicPipes` do painel de camadas ou recarregue a simbologia padrão nas propriedades da camada QGIS.
- Caso o projeto não possua resultados de simulação, os campos de resultados não aparecem no menu suspenso.
