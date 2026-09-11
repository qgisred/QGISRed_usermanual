# 📜 Journal des modifications

Restez à jour avec les dernières améliorations de QGISRed.

### Version 0.19

**Interface utilisateur** :

* Regroupement d'options informatives telles que Actualités, Incidents, Manuel, Évaluation, Abonnements et À propos... dans une nouvelle entrée Info dans le menu principal.
* Déplacement du menu Requêtes derrière le menu Outils, dans la barre de menu principale.
* Incorporation d'une marque et d'un préfixe dans le titre de tous les panels QGISRed pour les différencier des autres.
* Incorporation d'une icône d'avertissement dans les couches qui peuvent devenir obsolètes lorsque des modifications sont apportées aux données.

**Chef de projet** :

* Vous pouvez désormais modifier indépendamment le nom du projet QGISRed et le nom du fichier qui héberge les informations cartographiques (qgz).
* Lors du déplacement d'un projet, vous pouvez déplacer les données et le fichier cartographique (qgz) ensemble ou indépendamment vers des dossiers différents.
* L'option permettant de faire une sauvegarde du projet a été supprimée et a été remplacée par l'option Exporter le projet, avec plus d'alternatives.
* Lors de l'export d'un projet, vous pouvez choisir les groupes de couches QGISRed et les couches extérieures au projet (cartographies, MDT, etc.) à copier, parmi celles présentes dans le panneau des couches. Tout cela est enregistré dans un seul fichier .zip.
* Pour exporter le fichier map qgz, il doit se trouver dans le même dossier du projet ou à un niveau supérieur. Les informations cartographiques doivent se trouver dans des dossiers parallèles au dossier du projet.
* Lors de l'importation d'un projet QGISRed, toutes les informations précédemment exportées sont restaurées dans un nouveau dossier, en conservant la structure de tous les fichiers.

**Import de formes** :

* Possibilité de sélectionner les canalisations candidates pour connecter les connexions qui partent des points de consommation importés.

**Tableaux des matériaux** :

* Déclaration d'une table de matériaux par défaut différente pour chacune des quatre langues prises en charge.
* Nouvelles options dans la boîte de dialogue d'édition des tables de matériaux, pour copier, charger et éditer de nouvelles tables au niveau global, avant de créer un projet ou depuis celui-ci.
* Nouvelles options pour choisir la table de matériaux souhaitée lors de la création d'un nouveau projet ou de l'importation de fichiers de forme pour la première fois.

**Gestion des couches** :

* Création d'un nouveau groupe de calques appelé AuxiliaryLayers pour héberger des thèmes complémentaires aux thèmes de base.
* Création d'un sous-groupe au sein du groupe des Couches Auxiliaires, appelé Constructeur de Demandes, pour héberger ses propres thématiques : secteurs, demandes spécifiques et liens.
* Ajout d'un nouvel onglet au Gestionnaire de Couches pour créer, supprimer, charger ou télécharger des couches auxiliaires liées au Constructeur de Demandes.

**Édition graphique** :

* Le fait de taper sur une pompe, une vanne ou un tuyau bascule désormais uniquement entre les états ouvert et fermé.
* Pour basculer entre l'état actif ou fermé d'une vanne, ou déclarer un CV sur un tuyau, maintenez la touche Ctrl enfoncée lorsque vous cliquez avec la baguette.
* Lors de l'insertion d'une pompe ou d'une vanne dans une section inférieure à la séparation établie entre les nœuds extrêmes, celles-ci sont maintenues et ne bougent plus.
* Lors du déplacement d'un nœud, aucun calque n'est laissé ouvert, évitant ainsi les conflits avec d'autres outils d'édition.
* Révision de l'outil d'édition de sommets pour le rendre plus convivial.
* Lors de la division d'un tuyau en un point intermédiaire, l'Id est divisé en ajoutant un suffixe numérique. L'identifiant d'origine peut être récupéré si les sections sont fusionnées dans le sens opposé à celui dans lequel les nœuds intermédiaires ont été créés.
* Lorsque deux tuyaux en série ne peuvent être joints en éliminant le nœud intermédiaire, la cause est signalée.
* Révision de l'outil de fusion ou de séparation des nœuds, permettant une plus grande séparation entre eux.
* La création d'une connexion en T prolonge désormais la dernière section de la branche jusqu'à ce qu'elle croise le tuyau principal.
* Révision des outils d'annulation T et des croix, supprimant certaines restrictions et standardisant les actions de la souris.

**Modification des propriétés de groupe** :

* Nouvelle option de menu Modifier pour modifier les propriétés des éléments du groupe.
* Présélection graphique des éléments à modifier avec de multiples outils de sélection.
* Application de filtres pour restreindre les éléments à modifier, selon le type de propriété.
* Option pour afficher les éléments qui vont être modifiés sur la carte.
* Plusieurs options pour modifier la propriété choisie, en différenciant si la propriété est numérique, textuelle ou énumérée.
* Prévisualisez dans la table attributaire les modifications apportées avant de les consolider.

**Cartes thématiques** :

* Incorporation de nouvelles cartographies thématiques liées aux canalisations : Année d'installation, âge et coefficient de rugosité selon formule de perte.
* Nouvelles cartes thématiques liées aux carrefours : Altitudes et Demande de Base Totale graduées par taille.
* Lors de la création de la carte des matériaux, chaque matériau se voit désormais attribuer sa propre couleur en fonction de son abréviation et de sa langue, qui est modifiable.
* Lorsqu'une carte thématique devient obsolète en raison d'un changement d'unités ou d'une formule de perte, une icône d'avertissement s'affiche et peut être mise à jour en cliquant dessus.

**Éditeur de légendes** :

* Améliorations des assistants pour créer automatiquement des plages, des tailles et des couleurs afin de définir la légende de tous les calques.
* Possibilité de modifier certains paramètres de style des thèmes de base du groupe Data.
* Incorporation à l'Éditeur de légendes QGISRed des couches créées par les Requêtes (cartes thématiques, secteurs hydrauliques, arbres, etc.).
* Ajout de calques de résultats à l'éditeur de légende pour personnaliser son style.
* Option pour enregistrer les légendes au niveau du projet ou au niveau de l'utilisateur pour les appliquer à de nouveaux projets.
* Possibilité de stocker des assistants permettant d'adapter la légende aux données, au lieu de sauvegarder une légende préconfigurée.
* Création d'une bibliothèque QGISRed de symboles, rampes et palettes de couleurs, accessible depuis l'éditeur de légende et modifiable depuis QGIS.

**Constructeur de Demandes** :

* Option pour consolider les paramètres importés liés à l'affectation des demandes par secteurs dans un thème QGISRed.
* Possibilité de répartir la demande globale ou par secteurs en fonction des diamètres qui convergent aux nœuds candidats.
* Possibilité de déclarer les consommations par sections linéaires ou par polygones, comme alternative aux consommations spécifiques.
* Option pour consolider les consommations spécifiques importées dans un thème QGISRed.
* Possibilité de gérer des sujets de consommation spécifiques et d'ajouter plusieurs demandes au même sujet.
* Reconnaissance de diverses unités lors de la déclaration de la consommation à importer.
* Option permettant d'attribuer des demandes spécifiques aux extrémités du tuyau le plus proche au lieu de rechercher directement les nœuds les plus proches.
* Possibilité de considérer ou non les extrémités des pompes et des vannes comme nœuds de demande possibles.
* Possibilité de répartir les demandes spécifiques en fonction des diamètres des canalisations qui convergent aux nœuds, ou en combinaison avec leur distance par rapport aux points de consommation.
* Notification des nœuds chargés qui se trouvent à plus d'une distance donnée des points de consommation.
* Possibilité d'éditer et de réutiliser les liens entre les points de consommation et les nœuds de demande.
* Affectation des demandes aux nœuds en fonction des connexions déclarées comme éléments du Jumeau Numérique.
* Différenciation des demandes de base par catégories, tant en consommation spécifique que par connexions, créant des demandes multiples aux nœuds.
* Possibilité de charger les demandes uniquement des secteurs, points de consommation ou connexions sélectionnés.
* Possibilité d'utiliser votre propre thème pour attribuer des performances et des modèles par secteur, importer leurs valeurs et les modifier.
* Possibilité d'appliquer les performances hydrauliques et d'attribuer des modèles de demande par catégories.
* Possibilité de réajuster les performances et modèles déclarés à un niveau par ceux imposés à un niveau supérieur (catégories -> secteurs -> global).

**Panneau de statistiques** :

* Nouvelle option dans le menu Requêtes pour effectuer tous types de statistiques avec les données et résultats du modèle.
* Évaluation des statistiques d'une grandeur, classées par plages ou classes de ladite grandeur ou d'une autre grandeur du même type d'élément.
* Possibilité d'utiliser une deuxième grandeur de classification pour créer des tableaux à double entrée.
* Possibilité d'appliquer des filtres sur les données de départ et de visualiser les éléments concernés par la requête sur la carte.
* Affichage des statistiques sous forme d'histogrammes ou via un tableau de valeurs exportable.
* Exportation de la configuration de la requête et son importation ultérieure.

**Requêtes de topologie** :

* Révision des outils Connectivité, Secteurs Hydrauliques et Arbres Graphiques : nouveaux noms, déplacement des couches, changements de style, etc.
* Nouveau sujet pour mettre en avant des demandes isolées dans les secteurs hydrauliques.
* Possibilité de créer et de gérer l'existence de plusieurs thèmes pour les Graphes en Arbre (maintenant appelés Arbres de Coût Minimal).

**Simulation** :

* Nouvelle boîte de dialogue de progression pour afficher la progression des calculs hydrauliques et de qualité.
* La boîte de dialogue de progression peut être mise en pause pour observer attentivement la progression des calculs.
* La boîte de dialogue de progression peut être omise pour une plus grande rapidité dans les calculs, sauf pour les réseaux avec des temps de traitement longs.

**Panneau des résultats** :

* Option pour afficher tous les moments de calcul dans la carte des résultats et dans d'autres panneaux dans lesquels le temps intervient.
* Option pour afficher le moment de la simulation sous différents formats : temps écoulé depuis le début (en heures accumulées ou regroupés par jours) ou heure calendaire (au format 24 heures ou am/pm).
* Nouvelle barre de boutons pour effectuer des animations à vitesse contrôlée ou étape par étape.
* Les variables choisies pour afficher les résultats des nœuds et des lignes sont désormais mises en surbrillance et ont leur propre couleur attribuée.
* Nouvel onglet avec plusieurs options pour améliorer la visualisation des résultats sur la carte, la symbologie et la couleur de fond.
* Nouvelle option pour afficher dans un histogramme la distribution de la variable actuelle des nœuds ou des lignes et leurs valeurs accumulées, au moment actuel.
* Nouvelle option pour afficher une courbe d'évolution simplifiée de la variable actuelle des nœuds ou des lignes, pour l'élément choisi sur la carte.
* Lors du sauvetage du panneau de résultats, les options de la dernière action sont conservées, au lieu d'appliquer les options par défaut.
* Lorsque les données du scénario sont modifiées, les couches de résultats affichent une icône d'avertissement, qui peut être mise à jour en cliquant dessus.

**Graphiques d'évolution** :

* Nouveaux boutons pour naviguer dans le graphique des courbes d'évolution.
* Nouveau bouton avec plusieurs options pour personnaliser l'apparence de tous les composants du graphique.
* Adaptation de l'échelle de temps selon les options choisies dans le Panel des Résultats.
* Possibilité d'afficher tous les moments horaires ou uniquement les moments programmés, comme choisi dans le panneau des résultats.
* Synchronisation facultative du curseur avec le moment actuel du panneau de résultats.
* Incorporation de l'évolution du volume d'un réservoir ou du débit de trop-plein, comme nouvelles variables.
* Option pour représenter les courbes d'évolution de certaines variables globales pour l'ensemble du système.
* Nouveau bouton pour afficher dans un tableau les valeurs numériques des points de passage des courbes d'évolution et exporter leurs valeurs vers un fichier CSV.
* Nouveau bouton pour exporter des graphiques sous forme d'images.
* Option pour enregistrer et rappeler les paramètres du graphique d'évolution, y compris la création de modèles.
* Possibilité de créer et de maintenir ouvertes plusieurs fenêtres de courbes d'évolution en même temps.

**Langues** :

* Toutes les options de menu, boîtes de dialogue et messages de QGISRed sont désormais également affichés en français et en portugais brésilien, lorsque cette langue est choisie pour l'interface QGIS. Actuellement, ils sont déjà diffusés en anglais et en espagnol.

**Autres changements** :

* Tous les contrôles de sécurité vérifiés et les incidents liés à la qualité du code, signalés par le système QGIS Security Scan, corrigés.
* Vérification du code de la version 0.19 pour la compatibilité avec Qt6 et QGIS 4.xx.
* Fin du support des bibliothèques QGISRed sur les systèmes 32 bits (x86). Désormais, QGISRed ne fonctionnera que sur les systèmes 64 bits.
* Suppression des boutons minimiser et agrandir dans toutes les boîtes de dialogue intégrées aux bibliothèques.
* Révision des noms de certains champs dans les fichiers de formes, les tables dbf et les fichiers CSV, pour plus d'uniformité. Tous les champs d'identifiant se terminent désormais par ID.
* Révision des noms de propriétés affichés dans toutes les boîtes de dialogue QGISRed, en fonction de la langue, pour plus d'uniformité.
* Révision des décimales affichées dans les tables attributaires des sujets, en fonction des unités utilisées.

**Corrections de bugs** :

* Examen des situations possibles lors du chargement des bibliothèques GISRed pour éviter les tentatives répétées.
* Révision du format d'export des fichiers INP pour éviter les chevauchements qui provoquaient des erreurs de lecture.
* Correction d'un bug qui empêchait la création de nouvelles courbes de comportement.
* Vérifier que les identifiants des éléments, courbes et motifs ne contiennent aucun espace vide.
* Correction d'une erreur qui empêchait la consolidation de l'heure de début civil de la simulation.
