# Gestionnaire de couches et légende

---

## Gestionnaire de couches

**Barre de projet → Gestionnaire de calques** (Gestionnaire de calques)

Contrôle quelles couches de projet sont actives dans QGIS, vous permet de recréer les éléments de base manquants et gère les couches auxiliaires dans Demands Builder. La boîte de dialogue organise son contenu en trois onglets : **Éléments de base**, **Digital Twin** et **Couches auxiliaires**.

<figure><img src="../assets/images/proyecto/gestor-capas.png" alt="Boîte de dialogue Gestionnaire de couches QGISRed"><figcaption><p>Boîte de dialogue Gestionnaire de couches QGISRed</p></figcaption></figure>
<!-- TODO : Capture obsolète, boîte de dialogue déplacée des sections empilées vers les onglets (voir commits 12d9ee7 et 11c29ed) -->
*Gestionnaire de calques : liste de tous les calques du projet avec leur état de chargement.*

Au dessus des onglets le champ **CRS** est toujours visible, avec le système de coordonnées du projet et un bouton ****** pour le modifier.

### Éléments de base et onglets Digital Twin

- **Éléments de base** regroupe les 6 éléments de base d'EPANET (Tuyaux, Jonctions, Réservoirs, Vannes, Pompes) plus les couches complémentaires Demandes et Sources Multiples.
- **Digital Twin** rassemble les couches du jumeau numérique : connexions de service, vannes d'isolement et compteurs.

Pour chaque élément, la ligne affiche l'une des deux choses suivantes selon que son fichier existe ou non sur le disque :

- **Box cochée/décochée** → le shapefile existe déjà ; La case à cocher décide si la couche est chargée et visible dans QGIS. Vous pouvez en cocher ou décocher sans affecter les données.
- **Bouton "Créer un calque `<Elemento>`"** → le shapefile n'existe pas encore ; le bouton le crée vide (avec la structure de champ correcte) et l'ouvre automatiquement. Une fois créée, la ligne affiche désormais la boîte.

> ⚠️ Pipes est l'exception : dès qu'elle est chargée, son carton est verrouillé. C'est la couche qui contient le reste du réseau, elle ne peut donc pas être téléchargée à partir d'ici sans télécharger au préalable le reste du projet.

> 💡 Lorsque vous appuyez sur **Accepter**, la boîte de dialogue n'agit que sur ce qui a changé : un élément qui a déjà été marqué et qui reste marqué n'est pas fermé et rouvert, il conserve donc son style, sa visibilité et la sélection que vous aviez faite sur le canevas. La modification du CRS est l'exception : comme il réécrit tous les fichiers de formes, il ferme et rouvre tout ce qui est géré par la boîte de dialogue.

### Récupérer un calque supprimé

Si vous avez accidentellement supprimé une couche de la légende QGIS (ou son fichier SHP sur le disque), le gestionnaire de couches vous permet de la **recréer vide** : lorsque vous ouvrez la boîte de dialogue, cette couche n'affiche plus la case cochée, mais plutôt le bouton **Créer une couche `<Elemento>`** décrit ci-dessus. Appuyez dessus et QGISRed crée le SHP vide avec la structure de champ correcte et le charge dans QGIS.

> ⚠️ La récréation crée le calque vide. Les données qui s'y trouvaient (si le SHP a été effacé du disque) ne peuvent être récupérées que si vous disposez d'une copie de sauvegarde.

### Avis de couche obsolète

En plus de l'icône d'avertissement de couche supprimée, la légende QGIS peut afficher un deuxième type d'icône d'avertissement (⚠) sur les couches qui **existent** mais dont le contenu est peut-être devenu obsolète.

QGISRed surveille en arrière-plan (vérifiant toutes les 5 secondes) les couches dérivées suspendues aux dossiers du projet **Issues**, **Queries** et **Results**, dont le nom de fichier commence par `<Red>_`. Si le fichier d'entrée le plus récent du réseau (Tuyaux, Jonctions, etc.) a été modifié après la génération de l'une de ces couches dérivées, cette couche reçoit l'icône d'avertissement avec le message :

> "La couche est peut-être obsolète — les entrées ont changé depuis la dernière génération"

- L'icône est à titre informatif uniquement : aucune action n'est associée au clic dessus.
- Pour résoudre l'avertissement il faut **régénérer la couche**, c'est-à-dire relancer l'analyse ou la requête qui l'a créée (Segments Isolés, Secteurs Hydrauliques, une requête de propriétés, etc.).
- Les couches auxiliaires du Demands Builder (Points de consommation, Liens de demande, Secteurs) sont explicitement exclues de cette surveillance : ce sont vos propres données que vous importez ou créez, pas quelque chose que QGISRed recalcule à partir du réseau, donc la modification d'une entrée ne les invalide pas.

> 💡 Cet avis est différent de l'icône qui apparaît lorsqu'une couche a été supprimée (voir "Récupérer une couche supprimée" ci-dessus) : ici la couche existe toujours et est chargée, son contenu peut tout simplement ne plus refléter l'état actuel du réseau.

### Onglet Couches auxiliaires : Couches du générateur de demandes

L'onglet **Couches auxiliaires** contient le groupe **Demand Builder**, à partir duquel sont créées et gérées les couches de travail vides utilisées par l'outil d'affectation des demandes aux nœuds (Nodal Demand Builder) : **Points de consommation**, **Liens de demande** et **Secteurs**.

<!-- TODO : capture en attente — Onglet Calques auxiliaires du Layer Manager, avec la table des thèmes et les boutons Créer/Supprimer -->

Chaque ligne du tableau est un **thème** (thème) — vous pouvez avoir plusieurs thèmes du même type, par exemple un `Sectors` différent pour chaque campagne de sectorisation de la demande. Le tableau comporte trois colonnes :

- Boîte de téléchargement (identique aux autres onglets : cochée = téléchargée sur QGIS).
- **Thème** — nom du thème, ou "(par défaut)" pour lequel Demands Manager lui-même crée automatiquement.
- **Type** — Points de consommation / Liens de demande / Secteurs.

Pour créer un nouveau sujet :

1. Appuyez sur **Créer un thème auxiliaire**.
2. Dans la boîte de dialogue **Nouveau thème auxiliaire**, choisissez le **Type** (Points de consommation, Liens de demande ou Secteurs) et saisissez un **Nom**.
3. Appuyez sur **Accepter**. QGISRed crée le fichier de formes vide avec les champs correspondants et l'ajoute déjà marqué et chargé à la table.

Pour supprimer un thème, sélectionnez sa ligne et appuyez sur **Supprimer le thème auxiliaire** ; Une confirmation vous sera demandée car l'opération supprime également les fichiers présents sur le disque.

> 💡 Les calques que vous laissez marqués dans ce tableau sont mémorisés lors de la fermeture et de la réouverture du projet — y compris les projets qui n'enregistrent pas de `.qgz` — tout comme le reste des calques du projet.

> Pour savoir comment ces couches sont utilisées au sein du Nodal Demand Builder (importer des points de consommation, générer des liens de demande, agréger par secteurs...), voir [Exigences et scénarios](../outils/demandas-escenarios.md).

### Résumé du modèle (Résumé)

**Barre de projet → Résumé**

Générez un rapport rapide avec le nombre d'éléments de chaque type présents dans le projet :

```
Junctions: 1 243
Pipes: 1 876
Tanks: 3
Reservoirs: 2
Valves: 47
Pumps: 8
```

Utile pour vérifier que l'importation a été terminée ou pour documenter la taille du modèle.

---

## Éditeur de légende

**Barre de projet → Éditeur de légende** (Éditeur de légende)

Ouvre un panneau flottant qui vous permet de créer et de personnaliser la **symbologie** des couches du projet sans naviguer dans le menu des propriétés de la couche QGIS : type de légende, classification automatique, tailles, couleurs, styles d'enregistrement/chargement et règles propres par type d'élément.

<figure><img src="../assets/images/proyecto/editor-leyenda.png" alt="Panneau de l'éditeur de légende QGISRed"><figcaption><p>Panneau de l'éditeur de légende QGISRed</p></figcaption></figure>
<!-- TODO : capture d'écran obsolète, boîte de dialogue entièrement repensée (voir commit a3038c2 et suiv., 20-31 juillet 2026) -->
*Panneau Legend Editor : styles prédéfinis et personnalisation des couleurs et des tailles.*

### Choisir le calque

Dans l'en-tête de la boîte de dialogue :

- **Groupe** — groupe de l'arborescence des couches sur laquelle vous souhaitez travailler (Entrées, Résultats, Requêtes et leurs sous-groupes...).
- **Map Layer** — couche spécifique au sein de ce groupe. Vous pouvez également modifier les calques en les sélectionnant directement dans le panneau des calques de QGIS ; l'éditeur suit automatiquement la sélection.

### Type de légende et classification

La liste déroulante **Type de légende** propose, selon le type de calque, entre **Symbole unique**, **Catégorisé** et **Gradué**. Seules les options pertinentes pour cette couche apparaissent (par exemple, une couche de résultats numériques n'offre pas de symbole unique).

> 💡 Pour le calque **Mètres**, le menu déroulant **Type de compteur** apparaît également, qui filtre le tableau et les règles de couleur/taille sur "Tous les types" ou sur un type spécifique de compteur (les différentes icônes empilées dans le symbole Mètres).

Le tableau central répertorie une ligne par classe, avec la case à cocher de visibilité, la couleur, la taille, la valeur/plage (ou catégorie) et l'étiquette de légende :

- **Classes** (spinbox) définit le nombre de classes ; Le bouton à côté, **Classifier tout**, ajoute une classe pour chaque valeur unique du calque (catégorique) ou reclasse automatiquement la plage numérique selon le mode choisi dans **Intervalles**.
- Les boutons **+ / -** à côté de Classes ajoutent ou suppriment des classes : le clic gauche ajoute une classe en dessous de la sélection, le clic droit l'ajoute au dessus ; Dans les légendes catégorielles, un double-clic ajoute une classe spéciale "Autres valeurs" qui regroupe le reste des valeurs non classées.
- **Intervalles** (`cbMode`) définit la méthode de classification automatique des légendes graduées : Manuel, Intervalle égal, Intervalle fixe, Quantile (Nombre égal), Ruptures naturelles (Jenks), Écart type et Jolies ruptures. Avec **Fixed Interval**, le champ **Interval Range** apparaît pour indiquer la largeur de chaque classe.
- Vous pouvez éditer manuellement la plage d'une classe en **double-cliquant sur sa valeur** (colonne Valeur) pour ouvrir une petite boîte de dialogue avec les limites inférieure et supérieure.
- **Haut / Bas** (flèches à côté du tableau) réorganise la classe sélectionnée.

### Tailles

Le bloc **Sizes** contrôle la taille (épaisseur de ligne ou taille du symbole ponctuel) des classes :

- **Tailles** (`cbSizes`) : Manuel, Égal, Linéaire, Quadratique, Exponentiel ou Proportionnel à la Valeur.
- **Equal** utilise un seul champ **Value** pour toutes les classes.
- Linéaire/Quadratique/Exponentiel/Proportionnel à la Valeur répartit la taille entre **Min** et **Max** selon la courbe choisie, avec la case **Inverser** pour échanger quelle extrémité (valeur inférieure ou supérieure) reçoit la taille minimale.

### Couleurs

Le bloc **Colors** contrôle la couleur de chaque classe :

- **Couleurs** (`cbColors`) : Manuel, Égal, Aléatoire, Rampe ou Palette.
- **Égal** applique une seule couleur (bouton de couleur à côté de la liste déroulante) à toutes les classes.
- **Random** génère différentes couleurs aléatoires par classe, avec les mêmes critères de « lecture aléatoire » que QGIS utilise nativement. Le bouton d'actualisation à côté de la liste déroulante (visible uniquement dans ce mode) remanie les couleurs sans rien changer d'autre.
- **Ramp** affiche, sur toute la largeur de la boîte de dialogue, le sélecteur de rampe de couleurs natif de QGIS pour choisir la rampe à appliquer aux classes ; Il comprend à la fois le catalogue QGIS standard et les propres rampes de QGISRed.
- **Palette** distribue les couleurs à l'aide d'une palette catégorielle au lieu d'une rampe continue.
- La case **Inverser** échange la direction de la rampe/girouette.

> 💡 Pour la couche de nœuds de l'arbre de connectivité (Tree), la couleur de la ligne ne colore pas l'intégralité du symbole : elle modifie uniquement la **couleur du trait** du cercle extérieur du nœud, laissant les icônes d'étoile et d'élément avec leur propre couleur.

### Règles de style spécifiques par type de calque

Les éléments d'entrée (Inputs) et certaines couches de requête comportent des règles de style avec des états fixes que la couleur/taille que vous choisissez respecte, au lieu de remplacer l'intégralité du symbole. Par exemple, les Tuyaux/Vannes/Pompes gardent l'état "fermé" en rouge et les Vannes actives en orange, peu importe ce qui se passe avec la couleur que vous choisissez pour le reste. Parmi les couches avec leurs propres règles :

- **Demandes Multiples** : la couleur choisie colore uniquement la branche "demande positive" du symbole (le marqueur intérieur), tout comme dans les Jonctions ; la demande négative et le reste du symbole conservent leurs couleurs fixes.
- **Vannes d'isolement** : la couleur choisie remplace uniquement l'état « ouvert, pas de perte de pression » ; Les couleurs de fermé (rouge), avec perte de charge (ambre) et non disponible (gris) sont définies par la légende elle-même et ne peuvent pas être modifiées à partir d'ici.
- **Mètres** : La couleur et la taille sont appliquées en fonction de ce que vous avez sélectionné dans **Type de compteur** — à tous les types de compteurs à la fois, ou uniquement au type choisi, sans toucher au reste des icônes empilées.
- **Service Connections** : la couleur choisie est appliquée au trait de connexion actif et à une version plus claire de la même couleur pour son remplissage ; Les autres États conservent leur propre couleur.
- **Connect_Links** (résultat de l'outil Connectivité, au sein des Requêtes) : contrairement aux précédents, il n'a pas de règles par état — la couleur et la taille sont appliquées directement au symbole, comme dans n'importe quel calque de Symbole Unique.

### Charger et enregistrer les styles

Les boutons **Charger** et **Enregistrer**, en bas de la boîte de dialogue, ouvrent chacun un menu :

**Charger**
- **Style par défaut** — récupère le style QGISRed par défaut pour ce type de couche.
- **Style global** — chargez un style que vous avez préalablement enregistré au niveau global (valable pour n'importe quel projet).
- **Style de projet** — charge un style enregistré dans ce projet.
- **Revenir à la légende originale** — récupère dans la boîte de dialogue la légende que le calque avait au moment de l'ouverture de l'éditeur (sans avoir besoin de fermer et de rouvrir la boîte de dialogue).

**Enregistrer**
- **To Global...** — enregistre la légende actuelle sous forme de style global, réutilisable dans n'importe quel projet.
- **To Project...** — enregistre la légende actuelle dans le dossier `layerStyles` de ce projet.

Lors de la sauvegarde, une petite boîte de dialogue vous permet de choisir si vous souhaitez sauvegarder la légende **telle que vue** ou une **stratégie** qui se régénère automatiquement au prochain chargement (en marquant les parties à conserver : la structure classe/gamme, les tailles et/ou les couleurs).

> ⚠️ **Load** et **Revert to Original Legend** mettent à jour uniquement l'aperçu du dialogue. La couche du projet ne change pas tant que vous n'appuyez pas sur **Appliquer** ou **Accepter**.

### Postuler, accepter et annuler

Les trois boutons du bas ont une sémantique d'aperçu très spécifique :

- **Appliquer** — applique les modifications affichées dans la boîte de dialogue au calque, sans fermer l'éditeur. Utile pour voir le résultat sur la toile pendant que vous continuez les réglages.
- **Accepter** — applique les modifications au calque et ferme la boîte de dialogue (équivalent à Appliquer + fermer).
- **Annuler** — ferme la boîte de dialogue et **restaure le calque à la légende qu'il avait lorsque vous l'avez sélectionné** dans cet éditeur, annulant également toutes les modifications que vous avez peut-être déjà appliquées avec Appliquer. Si des modifications ont été appliquées, QGISRed demande une confirmation avant de les ignorer.

> 💡 Puisque Annuler vous ramène toujours à l'état de départ (même si vous avez appuyé plusieurs fois sur Appliquer en essayant), c'est le moyen sûr de "recommencer" avec un calque sans avoir à reconstruire sa légende à la main.
