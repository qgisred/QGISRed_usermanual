# Versions précédentes

Ici, vous pouvez consulter l'historique détaillé des modifications des versions précédentes de QGISRed.

### Version 0.16
**Version QGis** : 3.2-3.99

**Caractéristiques** :
* Nouvelles options dans le gestionnaire de demandes nodales pour déclarer les consommations pour l'ensemble du réseau ou par zones.
* Possibilité d'exporter, d'éditer et de réimporter les liens entre consommations spécifiques et nœuds.
* Nouvelles options pour importer/exporter/supprimer des scénarios de demande par catégories.
* Nouveaux outils dans le gestionnaire de demandes nodales pour prendre en compte l'efficacité de l'eau ou attribuer des courbes de modulation de consommation par secteurs.
* Nouveau gestionnaire de scénarios pour stocker et récupérer divers paramètres de modèle en masse.
* Calcul automatique de la longueur du tuyau à partir des coordonnées du sommet.
* Complétion automatique du tracé de raccordement à l'aide d'une section perpendiculaire au tuyau le plus proche ou d'un lien vers le nœud le plus proche.
* Possibilité de tracer automatiquement des connexions de longueur prédéfinie à partir d'un point sur un tuyau ou un nœud.
* Nouvelle option pour refléter une ruée vers l'outil d'investissement.
* Nouvelle option pour importer des connexions sous forme de points, créant des perpendiculaires aux tuyaux ou des connexions aux nœuds les plus proches.
* Nouveau champ IsActive dans les connexions pour définir s'il est opérationnel ou non.
* Vérification du point de contact d'un raccordement avec un tuyau ou un nœud aux deux extrémités.
* Avant de calculer la sectorisation hydraulique, l'état des vannes manuelles est maintenant transmis.
* Lors de l'export vers l'INP, le coefficient de perte des vannes d'arrêt est transmis aux canalisations.
* Déclaration, édition et suppression de compteurs de différents types, comme nouveaux éléments du Digital Twin.
* Edition, lecture et sauvegarde des signaux associés aux compteurs.
* Nouvelle boîte de dialogue pour lire les données de terrain et exporter au format CSV celles correspondant à l'intervalle de simulation.
* Nouvelle option pour exporter les données de terrain, ainsi que le fichier INP.
* Nouveaux champs dans la boîte de dialogue d'importation pour importer plus d'informations sur les éléments.
* Nouvelle option pour afficher dans les thèmes auxiliaires les éléments avec un incident lors de l'import.
* Nouveaux boutons et nouveau curseur dans le panneau des résultats.
* Améliorations des étiquettes pour afficher les résultats.
* Nouveau type de résultat pour afficher l'état des lignes.
* Améliorations des recherches depuis l'éditeur de propriétés.
* Liste déroulante avec les chemins exécutables EPANET lors de l'exportation d'INP pour une ouverture automatique.
* Tri des modulations par type lors de l'importation d'INP.
* Nouvel avertissement lorsque l'identifiant d'un élément est complété automatiquement.
* Modifications de l'ordre de la barre d'outils, des noms, des icônes et des styles visuels.
* Nouveau lien vers le site QGISRed dans la fenêtre d'information.

**Corrections**:
* Correction de la lecture et de l'édition de la courbe Id dans les vannes GPV.
* Erreur corrigée lors de l'attribution de valeurs par défaut lors de l'importation des coefficients de réaction.
* Erreur et message corrigés lors de la lecture des sources polluantes dans les réservoirs et bâches.
* Correction d'un problème avec des outils de sélection spécifiques.
* Correction d'une erreur dans la création en masse de connexions T.
* Correction d'erreurs dans la sélection multiple et polygonale avec différents CRS.
* Correction d'un bug avec la capture dans QGIS 3.26.

---

### Version 0.15
**Version QGis** : 3.2-3.99

**Caractéristiques** :
* Gestion manuelle des vannes (importation, création, suppression, édition des propriétés, interaction avec l'état des canalisations...).
* Nouvel outil pour changer l'état des éléments linéaires et des vannes manuelles.
* Nouvelle symbolisation des canalisations, pompes, vannes de régulation et manuels selon leur statut.
* Annulation des demandes isolées dues à la fermeture de canalisations ou de vannes superposées lors des simulations.
* Affectation des demandes aux nœuds en fonction des secteurs de demande et des demandes spécifiques, avec diverses options.
* Améliorations dans la fenêtre d'édition des propriétés (sélection multiple, éléments connectés, éléments visités, élément sélectionné au centre).
* Revue et élargissement des options d'analyse (hydraulique, qualité, temps et énergie).
* Intégration des nouveaux paramètres Epanet 2.2 aux formulaires (débordement de cuve, demandes dépendant de la pression).
* Boutons/menus de la barre d'outils principale en surbrillance.
* La langue par défaut et unique est l'anglais (pour l'instant).
* Amélioration de l'édition des règles (avec heures et heures).

**Corrections**:
* Correction d'une erreur lors de l'écriture des valeurs de demande avec plus de 4 chiffres.
* Correction d'un bug avec les étiquettes de temps pour la sélection des résultats.
* Erreur corrigée lors de la conversion des nombres en interpolation dimensionnelle.
* Correction d'erreurs de lecture, d'écriture et d'ordre des règles.
* Correction d'une erreur avec les règles utilisant la virgule comme séparateur décimal.
* Correction d'un problème lors de l'attribution de la projection du projet.
* Correction d'une erreur lors de la modification des propriétés en utilisant des couches raster.

---

### Version 0.14
**Version QGis** : 3.2-3.99

**Caractéristiques** :
* **Erreur grave corrigée** lors de la lecture des métadonnées des modèles précédents qui empêchaient de travailler avec eux.
* Correction d'une erreur lors de l'installation du plugin sans avoir de dépendances précédentes.
* Correction d'une erreur avec le format de l'heure dans les lois de contrôle simples.
* Affichage du séparateur décimal défini par l'utilisateur.
* Nouvel outil pour éditer la géométrie des connexions.
* L'option hydraulique `demand multiplier` prend désormais en charge les décimales.
* Priorité des éléments Digital Twin lors de la sélection des objets.

---

### Version 0.13
**Version QGis** : 3.2-3.99

**Caractéristiques** :
* Nouveau menu pour regrouper les outils Digital Twin.
* Création de connexions avec propre outil et intégration en suppression.
* Onglet spécifique pour modifier les propriétés de connexion.
* Téléchargement de lectures à distance sous différents formats vers des connexions ou des nœuds.
* Incorporation des courbes de modulation de connexion à l'éditeur général.
* Nouveau gestionnaire de demandes pour l'import/export et la suppression sélective.
* Amélioration des temps d'accès aux propriétés sur les grands réseaux.
* Ouverture optionnelle d'INP dans EPANET après export.
* Nouvelles options pour définir les unités et les formules de perte de pression à partir du SIG.
* Format de l'heure corrigé pour autoriser les jours.
* Correction de lecture des dates dans les métadonnées et diverses erreurs d'import SHP.

---

### Version 0.12
**versions QGis** : 3.14-3.99

**Caractéristiques** :
* Edition du tableau matériaux-rugosité pour calcul en fonction du matériau et de l'âge.
* Nouvel import et export de modulations/courbes au format CSV.
* Importation des demandes de base et des identifiants de courbe à partir de CSV.
* Importation de connexions depuis SHP.
* Nouvel outil pour obtenir l'arbre de résistance minimale.
* Mise à jour de la bibliothèque Epanet vers **version 2.2**.
* Amélioration de l'interface de conversion du coefficient de rugosité.
* Corrections de bugs dans les résultats de qualité et les nœuds sans coordonnées.
* Insertion de vannes/pompes évitant les longueurs négatives.

---

### Version 0.11
**Version QGis** : 3.2-3.99

**Caractéristiques** :
* Fichier JSON local pour les projections (.prj) sans Internet.
* Lecture des formats PUMPS hérités d'Epanet 1.1.
* Nouveau programme d'installation unique (x86 et x64).
* Affichage des unités et de la formule de perte dans la barre d'état.
* Estimation de la rugosité par âge/matériau compatible avec diverses formules.
* Outil pour créer une copie de sauvegarde du projet.
* Corrections de bugs dans QGIS 3.14.15 et au format heure AM/PM.

---

### Version 0.10
**Version QGis** : 3.0-3.14.1

**Caractéristiques** :
* Rédaction des en-têtes INP en anglais.
* Validation pour éviter le même nœud final dans les lignes.
* Simplification des sommets dupliqués dans les points initiaux.
* Unification des métadonnées dans le fichier `_Metadata.txt`.
* Avis de nouvelles versions disponibles.
* Contrôle de la visibilité des couches à l'aide de `LayerManagement`.
* Séparation entre Import (sans projet) et Ajouter (avec projet).
* Tolérance spatiale lors de l'ajout de données provenant de SHP.
* Le manuel inclut le format ASCII pour l'interpolation et la classification des secteurs hydrauliques.

---

### Version 0.9
**versions QGis** : 3.0-3.99

**Caractéristiques** :
* Nouveau logo QGISRed.
* Création agile de canalisations, réservoirs et bâches avec ancrage.
* Édition de chemin (déplacer, créer, supprimer des sommets).
* Inversion d'orientation de ligne.
* Outils pour diviser/joindre des tuyaux et des nœuds.
* Création/annulation de connexions en T et de croisements.
* Déplacement de vannes et de pompes.
* Sélection multiple (Ctrl ajoute, Shift supprime) et suppression par polygone.
* Accès aux derniers résultats sans simuler à nouveau.

---

### Version 0.8
**versions QGis** : 3.0-3.99

**Caractéristiques** :
* Modification des propriétés via une fenêtre de dialogue avec un navigateur.
* Insertion/retrait intelligent des vannes et des pompes dans les canalisations.
* Modification de la mise en page en déplaçant les nœuds et les éléments coïncidents.
* Prise en charge de 5 catégories d'outils.
* Boîtes de dialogue pour les options de calcul et les valeurs par défaut.
* Vérification des identifiants répétés.
* Masquage des tableaux de données dans la légende.
* Visualisation des résultats à l'aide d'étiquettes fixes.

---

### Version 0.7
**versions QGis** : 3.0-3.99

**Caractéristiques** :
* Tableau récapitulatif du modèle.
* Gestionnaire de courbes de modulation (modulations) : éditer, créer, cloner, exporter/importer.
* Behaviour Curve Manager : prise en charge de 1 ou 3 points avec équation approximative.
* Gestionnaire de contrôles simple et interactif.
* Gestionnaire de règles : combinaison interactive de conditions OU/ET.

---

### Version 0.6
**versions QGis** : 2.0-3.99

**Caractéristiques** :
* Gestion de projet (ouvrir, créer, importer, cloner, supprimer).
* Création de couches vectorielles SHP pour les éléments de base EPANET.
* Importation de données depuis INP ou SHP.
* Validation du modèle et rapport de bugs.
* Exportation vers INP avec ouverture automatique en option.
* Simulation avec la boîte à outils EPANET.
* Outils d'agencement (élimination des chevauchements, connectivité, secteurs).
