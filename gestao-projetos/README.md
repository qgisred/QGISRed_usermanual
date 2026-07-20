# 🗂️ Geral

A barra **Geral** é o ponto de entrada para qualquer sessão de trabalho com QGISRed. Contém as quatro ações para gerenciar o ciclo de vida dos projetos: criá-los, abri-los, importá-los e gerenciar o histórico.

<figure><img src="../assets/images/general/barra-general.png" alt="Barra de ferramentas geral QGISRed com seus quatro botões"><figcaption><p>Barra de ferramentas geral QGISRed com seus quatro botões</p></figcaption></figure>
*Barra Geral: Gerenciador de Projetos, Abrir, Criar e Importar.*

---

## O que é um projeto QGISRed

Um projeto QGISRed é uma **pasta** contendo um conjunto de arquivos SHP e DBF com o mesmo prefixo (o nome da rede). Por exemplo, para uma rede chamada `RedUrbana`:

```
RedUrbana/
├── RedUrbana_Junctions.shp/.dbf/.shx/.prj
├── RedUrbana_Pipes.shp/.dbf/.shx/.prj
├── RedUrbana_Tanks.shp/.dbf/.shx/.prj
├── RedUrbana_Reservoirs.shp/.dbf/.shx/.prj
├── RedUrbana_Valves.shp/.dbf/.shx/.prj
├── RedUrbana_Pumps.shp/.dbf/.shx/.prj
├── RedUrbana_Options.dbf
├── RedUrbana_Title.dbf
├── Issues/
├── Queries/
└── Results/
```

> ⚠️ Nunca mova, renomeie ou exclua esses arquivos manualmente do Windows Explorer. Sempre use ferramentas QGISRed para garantir a consistência do conjunto.

## Nesta seção

* [Gestor de projeto](gestor-proyectos.md) — histórico, clonar, renomear, excluir
* [Criar projeto](crear-proyecto.md) — novo projeto do zero
* [Abrir e importar](abrir-importar.md) — abra existente ou importe de `.inp`
