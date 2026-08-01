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

---

### Version 0.18 (avril 2026)
**Version QGIS** : 3.28-4.99

*Cette version a été financée par [Banque interaméricaine de développement (BID)](https://www.iadb.org/es) via le contrat C-RG-T4041-P001.*

**Actualités** :
* Améliorations du gestionnaire de projet. Nouveaux boutons pour déplacer et exporter des projets et nouvelles options pour renommer les projets.
* Identification de toutes les couches gérées par QGISRed à l'aide de leur propre identifiant, plutôt que par nom, ce qui permet de travailler en plusieurs langues.
* Examen des symboles cartographiques, des étiquettes et des avis associés à toutes les couches gérées par QGISRed.
* Meilleure intégration de l'éditeur de propriétés des éléments, conservation des propriétés des couches et actualisation des données dans toutes les fenêtres concernées, y compris la table attributaire.
* Stockage du style de toutes les couches gérées par QGISRed dans des fichiers .qml à trois niveaux : par défaut, niveau utilisateur et niveau projet.
* Stockage dans son propre tableau de toutes les grandeurs gérées par QGISRed, précisant les unités et décimales à afficher dans les différents systèmes d'unités et selon les cas.
* Création de votre propre éditeur de légendes pour personnaliser les plages ou classes, les couleurs et les tailles de toutes les légendes gérées par QGISRed.
* Assistants pour personnaliser automatiquement les légendes.
* Ajout d'un nouveau menu et d'une nouvelle barre d'outils pour héberger les nouvelles options visant à interroger les données et les résultats.
* Réorganisation des couches du groupe Requêtes, et stockage des fichiers shp correspondants dans la structure des dossiers du projet.
* Nouvel outil pour localiser n'importe quel élément sur la carte grâce à son identifiant et identifier les éléments connectés, avec la possibilité de naviguer à travers eux.
* Nouveau panneau pour observer les données et les résultats de tout élément de réseau sélectionné. Synchronisation des résultats avec le moment actuel de la simulation.
* Nouvelle boîte de dialogue pour créer des cartes thématiques de certaines ampleurs associées aux différents types d'éléments gérés par QGISRed.
* Nouveau panneau pour localiser les éléments sur la carte qui répondent à certains critères par rapport aux données ou aux résultats. Synchronisation avec les résultats du moment actuel de la simulation.
* Amélioration du format dans lequel le fichier INP est exporté depuis QGISRed, similaire à celui qui serait exporté depuis EPANET Toolkit.
* Remplacement du moteur de calcul EPANET 2.2 par la nouvelle version 2.3, jusqu'à la plus récente révision 2.3.5.
* Lecture des résultats d'une simulation directement à partir des fichiers binaires EPANET pour une navigation plus rapide et plus agile.
* Incorporation du Status Report au panneau de résultats dans un nouvel onglet, toujours accessible.
* Exportation de tous les résultats de simulation vers un fichier CSV structuré.
* Nouvelle option pour afficher diverses statistiques sur les résultats tout au long de la période de simulation.
* Nouvelle fenêtre pour afficher la courbe d'évolution dans le temps de n'importe quelle ampleur d'un élément tout au long de la période de simulation. Possibilité de superposer plusieurs courbes pour une grandeur identique ou différente.
* Améliorations du Demand Builder pour des demandes spécifiques. Revue des algorithmes et chargement automatique des liens. Nouveau sujet pour les points de demande.
* Revue de l'outil d'identification des filières hydrauliques et de détection des consommations isolées.
* Revue de l'algorithme pour identifier les fermés. Détection de consommation isolée.
* Nouvelles options au niveau du projet pour transférer les demandes des connexions vers les nœuds. Classification des revendications par les employeurs.
* Compatibilité de la version 0.18 avec les nouvelles versions de QGIS 4.0.
* Traduction de tous les dialogues, panneaux, messages et noms de couches QGISRed en espagnol.
* Refonte de toutes les icônes gérées par QGISRed avec un aspect plus uniforme et agréable.
* Hébergement web du manuel provisoire de QGISRed en anglais et espagnol pour consultation en ligne via la plateforme collaborative GitBook.
* Mention à la Banque Interaméricaine de Développement (BID) pour le soutien financier de toutes les améliorations apportées dans cette version 0.18.

**Corrections**:
* Résolution d'un problème lors du chargement des données de champ liées au séparateur décimal.
* Correction d'une erreur qui empêchait l'annulation des demandes provenant de zones isolées.
* Limitation de la taille du champ Description, utilisé pour rendre compte des demandes des connexions chargées sur chaque nœud.

---

### Version 0.17 (janvier 2026)
**Version QGis** : 3.2-3.99

**Actualités** :
* Nouvel outil d'analyse fermé, avec plusieurs options.
* Afficher les résultats jusqu'à 13 états pour les tuyaux, les vannes et les pompes.
* Transfert d'états et de qualités pour enchaîner les simulations dans des périodes successives.
* Nouvelles options pour réinitialiser la rugosité, les altitudes et les diamètres dans le générateur de scénarios.
* Nouvelle option pour exporter et importer des scénarios au format Epanet.
* Nouvelles fonctionnalités dans le gestionnaire de projet (trier, exporter, supprimer et renommer).
* Nouveaux boutons pour ouvrir ou enregistrer des projets.
* Nouvelle option pour importer un projet QGISRed.
* Modifications des icônes et des noms dans certaines options de menu.
* Amélioration de la précision lors de l'écriture de valeurs numériques dans des formes.
* Amélioration du message lors du téléchargement des dépendances nécessaires.

**Corrections**:
* Correction d'une erreur lors de l'interpolation des dimensions lorsque le point tombe sur une des extrémités du maillage.
* Erreur corrigée lors de la répartition des demandes proportionnellement à la longueur des tuyaux.
* Correction d'une erreur lors du chargement des demandes d'une couche de secteurs.
* Correction d'une erreur lors de l'importation d'INP avec des sources sans modulation définie.
* Correction d'erreurs lors de l'importation d'INP liées aux horaires et aux règles temporaires.
* Correction d'une erreur lors de l'exportation d'INP avec des descriptions très longues.
* Erreur corrigée avec le symbole décimal dans les options du modèle PDA.


