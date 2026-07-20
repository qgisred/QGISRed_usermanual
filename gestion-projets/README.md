# 🗂️ Général

La barre **Général** est le point d'entrée de toute session de travail avec QGISRed. Il contient les quatre actions pour gérer le cycle de vie des projets : les créer, les ouvrir, les importer et gérer l'historique.

<figure><img src="../assets/images/general/barra-general.png" alt="Barre d'outils générale QGISRed avec ses quatre boutons"><figcaption><p>Barre d'outils générale QGISRed avec ses quatre boutons</p></figcaption></figure>
*Barre générale : Gestionnaire de projet, Ouvrir, Créer et Importer.*

---

## Qu'est-ce qu'un projet QGISRed

Un projet QGISRed est un **dossier** contenant un ensemble de fichiers SHP et DBF avec le même préfixe (le nom du réseau). Par exemple, pour un réseau nommé `RedUrbana` :

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

> ⚠️ Ne déplacez, renommez ou supprimez jamais ces fichiers manuellement depuis l'Explorateur Windows. Utilisez toujours les outils QGISRed pour garantir la cohérence de l'ensemble.

## Dans cette rubrique

* [Chef de projet](gestor-proyectos.md) — historique, cloner, renommer, supprimer
* [Créer un projet](crear-proyecto.md) — nouveau projet à partir de zéro
* [Ouvrir et importer](abrir-importar.md) — ouvrir un existant ou importer depuis `.inp`
