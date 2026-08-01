# Profils longitudinaux

**Barre d'analyse → Profil longitudinal…**

Le profil longitudinal montre l'évolution d'une variable hydraulique le long d'un chemin défini de manière interactive sur le réseau. L'axe X représente la distance accumulée depuis le nœud initial du tour ; l'axe Y, la valeur de la variable sélectionnée à chaque nœud du chemin. Il est possible d'ouvrir simultanément plusieurs panneaux de profil, chacun avec son propre chemin, ses variables et ses paramètres indépendants.

> **Prérequis** : Une simulation EPANET doit avoir été exécutée avant l'ouverture du profil. Si aucun résultat n'est disponible, le plugin affiche le message _"Exécutez d'abord une simulation pour construire un profil longitudinal."_

> 📝 Le plugin détecte automatiquement si les résultats proviennent du format standard EPANET ou du format étendu `.hyd` de QGISRed ; aucun réglage manuel n'est nécessaire.

<figure><img src="../assets/images/analisis/perfil-longitudinal-dock.png" alt="Quai à profil longitudinal avec itinéraire tracé sur la carte et graphique de pression"><figcaption><p>Quai à profil longitudinal avec itinéraire tracé sur la carte et graphique de pression</p></figcaption></figure>
*Profil longitudinal : itinéraire surligné en rouge sur la carte (à gauche) et graphique hauteur piézométrique + altitude du terrain (à droite).*
<!-- TODO : capture d'écran obsolète — les boutons Choisir/Ajouter un nœud/Supprimer un nœud/Déplacer un nœud/Branche de la barre d'outils ont été remplacés par un seul bouton Modifier les trajectoires + bouton Aide -->

---

## Plusieurs fenêtres de profil

Le plugin vous permet de garder plusieurs docks de profils ouverts en même temps. Chaque dock fonctionne de manière totalement indépendante : il a son propre chemin, ses propres variables sélectionnées et ses propres paramètres graphiques.

- Le bouton **Nouveau panneau** de la barre d'outils crée un dock supplémentaire numéroté séquentiellement (_Profile 2_, _Profile 3_, etc.).
- Le panneau actif, celui qui reçoit les interactions cartographiques, se distingue visuellement des autres.
- L'ouverture du profil depuis le menu Analyse réutilise le premier panneau s'il en est un déjà ouvert ; sinon créez-en un nouveau.

---

## Ouvrir et créer un profil

1. Activez **Profil longitudinal** depuis la barre d'analyse. Le dock de profil s'ouvre dans la zone inférieure de QGIS.
2. Le bouton **Modifier les trajectoires** s'active automatiquement ; le curseur se transforme en icône en forme de crayon.
3. Cliquez sur un nœud du réseau (Jonctions, Réservoirs, Bâches) pour définir le premier nœud de référence.
4. Cliquez sur un autre nœud : le plugin calcule le **chemin topologique minimum** entre les deux nœuds et dessine le profil.
5. Chaque clic supplémentaire étend le chemin en concaténant le chemin du dernier nœud au nouveau.
6. Un clic droit (sans nœud en cours) termine l'édition du parcours.

Si deux nœuds ne sont pas connectés dans le réseau, le message _"Le nœud sélectionné n'est pas connecté au précédent le long du réseau."_

Sur la carte, une **ligne rouge** est tracée sur les liens du chemin et des **marqueurs bleus** carrés sont tracés sur les nœuds de référence.

---

## Variables disponibles

| Variables | Descriptif |
|----------|-------------|
| **Altitude** | Altitude du terrain — statique, ne dépend pas de l'instant |
| **Charge + Altitude** | Hauteur piézométrique et niveau du sol réunis dans le même graphique |
| **Pression** | Pression dans chaque nœud |
| **Qualité** | Qualité de l'eau à chaque nœud ; le sélecteur affiche le nom de qualité spécifique au projet (par exemple, _Chlorine_) au lieu du terme générique _Quality_ |
| **Perte de charge accumulée** | Perte de charge accumulée le long du parcours |

La variable par défaut est **Charge + Altitude**. Lorsqu'il est sélectionné, le graphique affiche **simultanément** la ligne piézométrique (bleue) et l'altitude du terrain (marron), vous permettant de voir en un coup d'œil si une pression positive existe à chaque point du parcours.

Le graphique se met à jour automatiquement lorsque l'heure instantanée change dans le dock Résultats.

> 📝 Lorsque des instants temporels sont disponibles, le titre du graphique affiche **"Profils longitudinaux à HH:MM:SS"**. Pour les résultats statiques, **"Profils longitudinaux"** apparaît simplement.

> 📝 Les étiquettes des axes incluent l'unité du projet entre crochets (par exemple _Charge [m]_, _Pression [bar]_, _Distance [m]_). Les en-têtes du tableau de valeurs indiquent également les unités.

### Axe secondaire

À droite du sélecteur de variable principal se trouve le combo **2ème axe**. Permet de superposer une deuxième variable sur l'**axe Y droit** du graphique, avec sa propre échelle indépendante.

- Les variables disponibles dans l'axe secondaire dépendent de la sélection principale.
- La courbe de l'axe secondaire peut être supprimée directement de la légende du graphique.
- L'axe Y droit a ses propres paramètres d'échelle et d'étiquette, accessibles dans **Options du graphique → Axes** (voir [Personnalisation du graphique](#personalización-del-gráfico)).

---

## Barre d'outils du Dock

### Modes d'édition de visite

Toutes les actions d'édition sont contrôlées à partir d'un seul bouton bascule, plutôt que d'un bouton séparé par action :

| Bouton | Fonction |
|-------|---------|
| **Modifier les trajectoires** (icône en forme de crayon, modifiable) | Activer le mode édition : clic gauche pour tracer l'itinéraire nœud par nœud, clic droit sur un nœud pour voir ses options (voir [Raccourcis souris](#atajos-de-ratón)). Lorsqu'il est désactivé, le passage de la souris sur le chemin ne fait que le mettre en évidence et afficher les informations, sans les modifier. |
| **Aide** (icône ⓘ) | Ouvre la boîte de dialogue **"Comment modifier les trajectoires"**, avec un résumé de toutes les actions d'édition et raccourcis de souris disponibles. |

> 📝 Ajouter un nœud d'étape intermédiaire, le supprimer, le déplacer ou créer une branche n'a plus son propre bouton dans la barre d'outils : ils se font avec **Editer les trajectoires** actif, à l'aide du menu contextuel (clic droit) ou des raccourcis souris décrits dans [Raccourcis souris](#atajos-de-ratón). Ces actions fonctionnent de la même manière sur la route principale et sur les embranchements.

### Navigation graphique

| Bouton | Fonction |
|-------|---------|
| **Fenêtre de zoom** | Dessinez un rectangle sur le graphique pour zoomer sur l'axe X |
| **Pain** | Faites glisser le graphique horizontalement ; exclusif avec fenêtre Zoom |
| **Zoom avant/Zoom arrière** | Effectue un zoom avant ou arrière sur l'axe X |
| **Ajustement** | Restaure la vue complète du profil |

La molette de la souris effectue également un zoom en se centrant sur la position du curseur.

### Options d'affichage

| Bouton | Fonction |
|-------|---------|
| **Étiquettes** | Affiche la valeur numérique de la variable sur chaque nœud de référence |
| **Symboles** | Affiche la symbologie des éléments (nœud, réservoir, bâche, pompe, vanne) et les flèches de direction d'écoulement sur la courbe |
| **Enveloppe** | Ouvre un sous-menu pour activer l'enveloppe Min/Max de la simulation (voir section [Enveloppe](#envolvente-minmax)) |
| **Options du graphique** | Ouvrez la boîte de dialogue de personnalisation du graphique |

### Tableau et export

| Bouton | Fonction |
|-------|---------|
| **Tableau** | Afficher ou masquer le tableau des valeurs à gauche du graphique |
| **Exporter CSV** | Exporter le tableau des valeurs au format CSV avec séparateurs régionaux |
| **Exporter l'image** | Enregistrez le graphique au format PNG ou SVG |
| **Exporter la configuration** | Enregistrez les paramètres de profil actuels dans un fichier `.cfg` (voir section [Paramètres d'importation et d'exportation](#importar-y-exportar-configuración)) |
| **Paramètres d'importation** | Charger une configuration de profil précédemment enregistrée à partir d'un fichier `.cfg` |
| **Nouveau panneau** | Créer un quai de profil supplémentaire numéroté séquentiellement |
| **Effacer** | Efface l'intégralité de l'itinéraire, les branches et la mise en évidence de la carte |

---

## Enveloppe Min/Max

Disponible pour **Charge + Altitude**, **Pression** et **Qualité**. Affiche la plage de variation historique de l'ensemble de la simulation superposée au profil du moment actuel.

| Mode | Descriptif |
|------|-------------|
| **Désactivé** | Sans enveloppe |
| **Bande ombrée uniquement** | Zone ombrée orange entre les valeurs historiques hautes et basses |
| **Lignes de démarcation uniquement** | Deux lignes pointillées orange marquant le maximum et le minimum |
| **Bande et lignes** | Les deux superposés |

Lorsque l'enveloppe est active, la table de valeurs ajoute des colonnes avec la valeur maximale, la durée maximale, la valeur minimale et la durée minimale pour chaque nœud.

---

## Succursales

L'action **Créer une branche** vous permet d'ajouter des branches latérales partageant le même graphique avec le chemin principal.

1. Avec **Modifier les trajectoires** actif, faites un clic droit sur un nœud appartenant déjà au chemin principal ou à une branche existante et choisissez **Créer une branche** dans le menu contextuel (ou double-cliquez avec le bouton droit directement dessus s'il s'agit d'un nœud intérieur avec un degré de connexion supérieur à 2 ; voir [Raccourcis souris](#atajos-de-ratón)). Ce nœud définit le point de bifurcation et sa position sur l'axe X.
2. Effectuez des clics successifs pour étendre la branche vers d'autres nœuds.
3. Faites un clic droit pour terminer la branche.

Chaque branche est dessinée avec une couleur différente de la palette. Les distances des branches sont calculées à partir du point de branchement, de sorte que les deux courbes partagent la même origine X en ce point. Lorsque la variable sélectionnée est **Charge + Altitude**, les branches affichent également leur propre courbe d'altitude du terrain à côté de la ligne piézométrique.

> ⚠️ **Restrictions d'intégrité du cours**
>
> - Une branche ne peut pas réutiliser des liens ou des nœuds appartenant déjà au chemin principal ou à une autre branche, à l'exception du nœud de branche d'origine. En cas de tentative, l'opération est rejetée avec un message d'erreur.
> - Le nœud source d'une branche ne peut pas être supprimé du parcours principal pendant que la branche est active. Pour l’éliminer, il faut d’abord couper la branche depuis son extrémité la plus éloignée.
> - **Move pass node** vérifie également les conflits avec les chemins existants avant d'appliquer la modification.
> - Toute opération d'édition (déclarer, supprimer ou déplacer un nœud d'étape) est annulée silencieusement si le chemin recalculé résultant n'est pas valide.

Déclarer, supprimer ou déplacer un nœud d'étape (auparavant **Ajouter un nœud**, **Supprimer un nœud** et **Déplacer un nœud**) fonctionne de la même manière sur le chemin principal que sur les chemins de branche.

Les branches peuvent être supprimées directement de la **légende du graphique**, sans avoir besoin d'utiliser le bouton Effacer.

Le bouton **Effacer** supprime le chemin principal et toutes les branches.

---

## Raccourcis souris

Avec **Modifier les trajectoires** actif, en plus de tracer le chemin clic par clic, la souris prend en charge plusieurs raccourcis directs qui évitent de passer par le menu contextuel. Ces raccourcis fonctionnent de la même manière sur le chemin principal et sur les branches.

- **Double clic gauche sur un nœud intermédiaire** de la route (celui qui n'est pas encore un nœud pass) : le déclare comme nœud pass (équivalent à **Déclarer un nœud pass**).
- **Double clic gauche sur un nœud pass déjà déclaré** : le supprime et le chemin est recalculé (équivalent à **Supprimer le nœud pass**).
- **Double clic droit sur un nœud de chemin extrême** (l'origine ou la fin d'un chemin, avec connexion gratuite disponible) : étend le chemin à partir de ce point (équivalent à **Extend path**).
- **Double clic droit sur un nœud de passage intérieur** avec un degré de connexion supérieur à 2 (et connexion gratuite disponible) : démarrez une branche à partir de ce nœud (équivalent à **Créer une branche**).
- **Simple clic gauche sur un nœud de passage**, sans aucun parcours en cours : démarre le mouvement de ce nœud ; le clic suivant marque le nœud de destination (équivalent à **Move pass node**).
- **Un simple clic droit** : s'il y a une visite en cours, la termine ; sinon, il ouvre le menu contextuel avec les actions disponibles pour le nœud sous le curseur.

Le menu contextuel (simple clic droit) propose différentes options selon le nœud indiqué :

| Situation des nœuds | Options des menus |
|---------------------|--------------------|
| Il n'y a pas encore d'itinéraire | **Commencez un nouveau chemin ici** |
| Nœud intermédiaire de l'itinéraire (pas encore nœud de passage) | **Déclarer le nœud de passage** |
| Nœud d'étape d'origine de l'itinéraire principal | **Étendre le chemin**, **Créer une branche** |
| Nœud de passage extrême (fin d'un parcours) | **Étendre le chemin**, **Créer une branche**, **Déplacer le nœud de passe**, **Supprimer le nœud de passe** |
| Nœud de passage intérieur de l'itinéraire | **Créer une branche**, **Déplacer le nœud de passe**, **Supprimer le nœud de passe** |
| Nœud de branche (origine d'une branche) | **Créer une branche** |

> 💡 Le bouton **Aide** de la barre d'outils du dock (icône ⓘ) ouvre à tout moment la boîte de dialogue **"Comment éditer les trajectoires"**, avec ces mêmes informations récapitulatives.

---

## Info-bulle interactive

Lorsque vous déplacez la souris sur le graphique, une ligne verticale pointillée indique la position du curseur. Au-dessus de chaque série active, un cercle de surbrillance apparaît sur le nœud le plus proche et une boîte d'information avec :

-ID de l'élément
- Distance accumulée depuis le nœud initial
- Valeur de la variable pour chaque série active

Des **lignes de référence verticales** sont tracées sur le graphique à la position X de chaque nœud du chemin : de fines lignes bleu clair pour tous les nœuds et des lignes plus épaisses pour les nœuds de référence.

### Synchronisation bidirectionnelle avec la carte

L'interaction entre le graphique et la carte est bidirectionnelle et se met à jour en temps réel :

- Lorsque vous déplacez votre souris sur le **graphique**, le nœud le plus proche est mis en évidence sur le **canevas de la carte** avec un cercle orange.
- Passer la souris sur la **carte** pendant que **Modifier les trajectoires** est actif déplace le curseur du graphique vers le nœud correspondant.

---

## Configuration d'importation et d'exportation

Deux boutons de la barre d'outils vous permettent d'enregistrer et de rappeler la configuration complète d'un panneau de profil.

**Chemin par défaut** : le même dossier que les résultats de simulation, avec le nom `{salida}_Profile_Config.cfg`.

Les paramètres stockés incluent :

- Variable principale et variable d'axe secondaire (le cas échéant)
- Nœuds de référence de l'itinéraire principal
- Toutes les branches définies
- Options d'affichage : symboles, étiquettes, enveloppe
- Configuration des axes (échelle, étiquettes, grille)
- Styles de courbes (couleur, épaisseur, type de ligne, marqueurs)
- Texte de description libre associé au panneau

> 💡 Le dock comprend un champ de texte libre (description ou commentaire) qui est enregistré avec la configuration et peut être utilisé pour identifier l'analyse ou noter des observations.

Lors de l'**importation** d'une configuration, le profil est recalculé à partir des nœuds stockés. Si un nœud n'existe plus dans le réseau, le plugin affiche un avertissement et continue avec les nœuds disponibles.

---

## Personnalisation du graphique

La boîte de dialogue **Options du graphique** (bouton de configuration sur la barre) comporte quatre onglets. Le bouton **Appliquer** prévisualise les modifications en temps réel sans fermer la boîte de dialogue.

**Onglet Axes**
Pour chaque axe (X = distance, Y = variable) :
- Titre personnalisé.
- Mise à l'échelle automatique (activée par défaut) ou plage fixe manuelle.
- Afficher ou masquer la grille.

Lorsqu'une variable est active sur l'**axe secondaire**, un groupe supplémentaire **Axe Y (à droite)** apparaît avec ses propres paramètres d'échelle et d'étiquette, indépendants de l'axe Y principal.

**Onglet Courbes**
Pour chaque série active :
- Couleur, style de ligne (Solide / Pointillé / Pointillé) et épaisseur.
- Signets : afficher/masquer et taille.

**Onglet Légende**
- Afficher/masquer la légende.
- Position (Gauche/Centre/Droite), taille de police et taille du symbole.
- Afficher le cadre et la couleur d'arrière-plan de la légende.

**Onglet Général**
- Couleur de fond de la zone graphique.
