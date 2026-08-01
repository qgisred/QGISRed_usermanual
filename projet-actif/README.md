# 📋 Projet

La barre **Projet** regroupe les outils d'administration du projet déjà ouvert dans QGISRed. Tous vos boutons nécessitent un projet valide chargé ; S'il n'y en a pas, le plugin vous avertira avec le message _"Aucun projet valide n'est ouvert"_.

<figure><img src="../assets/images/proyecto/barra-project.png" alt="Barre d'outils du projet QGISRed avec ses neuf boutons"><figcaption><p>Barre d'outils du projet QGISRed avec ses neuf boutons</p></figcaption></figure>
*Barre de projet : outils de gestion de projet actifs.*

<!-- TODO : capture d'écran obsolète après suppression du bouton "Sauvegarde du projet" (commit 7b2415f) -->

---

## Boutons de la barre de projet

| # | Outil | Fonction |
|---|-------------|---------|
| 1 | **Résumé** | Nombre d'éléments de chaque type dans le réseau |
| 2 | **Ajouter des données par importation** | Importer des éléments supplémentaires dans le projet ouvert |
| 3 | **Gestionnaire de calques** | Contrôler la visibilité des couches et récupérer les couches supprimées |
| 4 | **Éditeur de légende** | Personnaliser la symbologie des couches |
| — | *(séparateur)* | |
| 5 | **Options du projet** | Paramètres EPANET : unités, formule, qualité, temps, énergie |
| 6 | **Valeurs par défaut** | Préfixes ID, tolérances et valeurs hydrauliques initiales |
| 7 | **Tableau des matériaux** | Rugosité et taux de vieillissement par matériau |
| — | *(séparateur)* | |
| 8 | **Enregistrer la carte** | Enregistrez le fichier QGIS `.qgz` |
| 9 | **Fermer le projet** | Fermez le projet et effacez la session QGIS |

> 💡 L'ancien bouton **Sauvegarde** (_Sauvegarde du projet_) a été supprimé de cette barre sans remplacement direct. Pour exporter le projet vers un ZIP portable, utilisez le bouton **Exporter** sur [Chef de projet](../gestion-projets/gestor-proyectos.md) — voir [Enregistrer, exporter et fermer le projet](guardar-backup.md).

## Dans cette rubrique

* [Présentation et gestion des couches](capas-y-leyenda.md) — visibilité, récupération et légende des couches
* [Paramètres du projet](configuracion.md) — Options EPANET, valeurs par défaut, matériaux
* [Enregistrer, exporter et fermer le projet](guardar-backup.md) — enregistrez la carte, exportez au format ZIP et fermez
