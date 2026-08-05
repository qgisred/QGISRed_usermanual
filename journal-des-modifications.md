# 📜 Journal des modifications

Restez à jour avec les dernières améliorations de QGISRed.

### Version 0.19

**Actualités** :

* Restructuration complète du panneau Statistiques : nouveaux onglets Configuration/Rapport, histogramme avec fenêtre flottante et sélecteur de statistiques sur l'axe Y, et deuxième classification croisée avec matrice de résultats.
* Nouvelles options d'affichage dans le panneau Résultats : taille proportionnelle à la valeur dans les nœuds et les tuyaux, et contour noir en option dans les marqueurs de nœuds.
* Étiquettes de carte améliorées : affichez le type et l'identifiant de l'élément sur la première ligne et la valeur avec les unités sur la seconde.
* Infobulles cartographiques visibles sur toutes les couches actives gérées par QGISRed, quelle que soit la couche sélectionnée dans la légende.
* Evolution temporelle rapide directement depuis le dock Résultats, sans avoir à ouvrir le panneau Time Series.
* Améliorations du panneau Time Series : nouvelles grandeurs de réservoir (Volume et TankSpill), curseur synchronisé avec le tableau de valeurs, copie du tableau avec double en-tête (nom et unité), export et import de la configuration graphique et prise en charge de plusieurs fenêtres simultanées.
* Boîte de dialogue de progression de la simulation avec option pour ne plus s'afficher (configurable à partir des propriétés du projet).
* Gestion améliorée des erreurs de simulation : le rapport EPANET est automatiquement affiché dans le journal lorsqu'une erreur se produit, et les erreurs non gérées sont enregistrées au lieu d'échouer silencieusement.
* Avis spécifique lorsque les fichiers de résultats sont verrouillés par une autre application.
* Demand Builder : restructuration de la section des patterns par secteurs avec deux modes exclusifs (import SHP externe / utilisation couche projet).
* Demand Builder : section sur l'efficacité sectorielle avec deux modes de travail et de nouvelles options pour corriger l'efficacité des catégories et les modulations sectorielles afin d'atteindre les objectifs globaux.
* Demand Builder : répartition automatique des pourcentages de demande manquants dans les couches de sections.
* Nouvelle couche de connexions isolées avec demande non nulle générée par l'analyse des segments hydrauliques.
* Arbre de distribution : le nœud racine est identifié par `NodeType = "ROOT"` dans la couche de nœuds résultante.
* Renommer les champs d'identification dans les couches SHP du projet (par exemple `Id` → `JunctionID`, `PipeID`, etc.). Les projets créés avec les versions précédentes restent compatibles grâce à la table de noms héritée.
* Catégorie non attribuée renommée de « Non défini » à **« Non classé »** dans le générateur de demandes et la légende des couches.

