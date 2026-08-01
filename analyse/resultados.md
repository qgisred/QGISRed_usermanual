# Visionneuse de résultats

Une fois la simulation terminée, QGISRed propose deux outils complémentaires pour explorer les résultats : le dock Résultats, qui contrôle l'affichage sur la carte, et le dock Séries temporelles, qui montre l'évolution de toute variable au fil du temps pour des éléments individuels.

---

## Dock des résultats

Le dock Résultats est ancré dans la zone droite de l’écran. Contient **trois onglets** :

- **Résultats** : visualisation interactive sur la carte avec sélection de variables, navigation temporelle et options cartographiques.
- **Rapport** : rapport texte du moteur EPANET.
- **Apparence** : configuration complète de l'apparence visuelle des résultats sur la carte.

<figure><img src="../assets/images/analisis/results-dock.png" alt="Panneau de résultats avec sélecteur de variable et barre de temps"><figcaption><p>Panneau de résultats avec sélecteur de variable et barre de temps</p></figcaption></figure>
*Dock de résultats : sélection de variables, mode statistiques et navigation par instants de temps.*
<!-- TODO : capture d'écran obsolète après l'ajout du bouton Taux de lecture constant à côté du curseur de vitesse -->

---

### Onglet Résultats

#### Groupe de synchronisation

Affiche l'instant de l'heure actuelle au format `HH:MM:SS` (ou au format am/pm si actif). Comprend des boutons pour basculer entre le format civil et le format de temps écoulé.

Lorsqu'un mode statistique est actif (Maximum, Minimum...), la zone horaire affiche le nom et la description de la statistique à la place de l'horloge.

#### Navigation temporelle (Contrôles temporels)

| Contrôle | Descriptif |
|---------|-------------|
| **Curseur temporel** | Faites défiler les moments du reportage. |
| **Combo de moments** (`cbTimes`) | Liste déroulante avec tous les moments disponibles. |
| **Boutons avant/arrière** | Suivant, précédent, début, fin. |
| **Jouer / Jouer en arrière** | Animation automatique vers l'avant ou vers l'arrière. |
| **Curseur de vitesse** | Contrôle la vitesse relative de l'animation (1–10). Il est masqué lorsque **Taux de lecture constant** est actif. |
| **Taux de lecture constant** | Bouton commutable à côté du curseur de vitesse. Lorsqu'il est activé, le curseur est remplacé par le champ **"1h in: N sec"** : N sont les secondes réelles nécessaires pour lire une heure de temps simulé (1–3600), donc la vitesse de lecture est constante par rapport au temps simulé même si le pas entre les instants n'est pas uniforme. Lorsque vous le désactivez, le curseur de vitesse relative est à nouveau utilisé. L'état et la valeur sont enregistrés dans le projet. |
| **Boucle** | Répétez l'animation en boucle. |

> 💡 Lorsque vous changez l'instant temporel, activez ou désactivez un mode statistiques, modifiez les décimales dans l'onglet Apparence, ou chargez tous les résultats d'un coup, QGISRed relit et reformate les valeurs. Si l'opération prend du temps (grands réseaux avec de nombreux éléments), une mention apparaît superposée et centrée sur la carte : **"Lecture des résultats… NN%"**. Lors d'opérations rapides, il ne s'affiche pas pour éviter le scintillement.

#### Temps rapportés et statistiques

Deux combos situés sous les contrôles horaires :

| Combiné | Descriptif |
|-------|-------------|
| **Temps signalés** (`cbResultTimes`) | Filtrez les moments qui sont affichés : Période unique, Temps d'étape ou Tous les temps de calcul. |
| **Statistiques** (`cbStatistics`) | Applique une statistique sur toutes les périodes : Maximum, Minimum, Plage, Moyenne, StdDev, Avertissement. Lorsqu'elle est active, l'horloge est remplacée par le nom de la statistique. |

> 💡 En modes **Maximum** et **Minimum**, les étiquettes de la carte affichent la valeur ainsi que l'heure d'occurrence au format `valor (@ HH:MM:SS)`. Lorsque vous placez le curseur sur un élément de la carte, l'info-bulle inclut une ligne supplémentaire `@ HH:MM:SS` avec le moment exact auquel ce maximum ou ce minimum s'est produit.

> 💡 Avec n'importe quel mode statistique actif, l'info-bulle ajoute à la valeur l'abréviation de la statistique affichée : **Max**, **Min**, **Avg** (Moyenne), **Rng** (Plage) ou **Std** (StdDev). Par exemple, `Max 45.2` au lieu de simplement `45.2`.

#### Groupe de mappage — Nœuds

| Contrôle | Descriptif |
|---------|-------------|
| **Nœuds combinés** (`cbNodes`) | Propriété à afficher dans les nœuds : Pression, Hauteur, Demande, Qualité. |
| **Afficher les étiquettes des nœuds** | Affiche les étiquettes avec l'ID et la valeur sur chaque nœud de la carte. |
| **Afficher l'histogramme des nœuds** | Ouvre un histogramme intégré dans le dock avec la distribution de la valeur actuelle en nœuds. |
| **Afficher l'évolution du nœud** | Ouvre un mini-graphique intégré avec l'évolution temporelle du nœud sélectionné sur la carte. |

> 💡 Lorsqu'une variable est sélectionnée dans le combo **Nœuds**, une étiquette apparaît à côté de l'en-tête du groupe avec le nom de la variable en gras et son unité entre parenthèses (par exemple, **Pression** (m)).

#### Groupe de cartographie — Liens

| Contrôle | Descriptif |
|---------|-------------|
| **Liens combinés** (`cbLinks`) | Propriété à afficher dans les canalisations/vannes/pompes : Flow, Velocity, HeadLoss, UnitHdLoss, FricFactor, Status, ReactRate, Quality. |
| **Afficher les étiquettes des liens** | Affiche les étiquettes avec l'ID et la valeur sur chaque canal. |
| **Afficher les directions d'écoulement** | Ajoutez des flèches de direction d'écoulement sur les tuyaux. |
| **Afficher l'histogramme des liens** | Histogramme intégré au dock avec répartition de la valeur actuelle dans les canalisations. |
| **Afficher l'évolution du lien** | Mini-graphique intégré avec l'évolution temporelle du pipeline sélectionné sur la carte. |

> 💡 De même, lorsqu'une variable est sélectionnée dans le combo **Liens**, un label apparaît à côté de l'en-tête du groupe avec le nom de la variable en gras et son unité entre parenthèses (par exemple, **Velocity** (m/s)).

> ⚠️ Lorsque la variable **Links** est **Status**, les étiquettes de texte sont simplifiées : les ~13 états internes que EPANET peut retourner sont regroupés en seulement deux textes, **"Fermé"** (inclut "Temp Closed") et **"Active"** (inclut "Active (Rev Pump)"). Les liens avec n'importe quel état **"Ouvert*"** n'affichent aucune étiquette, afin de ne pas encombrer la carte avec la plupart des tuyaux (qui sont généralement ouverts). Ce n'est pas une erreur si, avec le statut actif, la plupart des tuyaux apparaissent sans étiquette.

> Le bouton **Apparence** (icône en entête du groupe Nœuds) vous amène directement à l'onglet Apparence sans avoir à naviguer dans les onglets.

---

### Onglet Rapport

Affiche le rapport texte généré par le moteur EPANET à la fin de la simulation. Comprend :

- Bilan massique général du réseau.
- Liste des nœuds à pression négative ou hors de portée.
- Avertissements de pompes fonctionnant en dehors de leur courbe.
- Statut de convergence du calcul hydraulique à chaque étape.
- Synthèse des réactions qualité (si la qualité a été simulée).
- En cas d'erreur, le contenu complet du rapport est automatiquement affiché ici.

> Le rapport d'état est le premier endroit à consulter lorsqu'une simulation produit des résultats inattendus ou ne converge pas.

---

### Onglet Apparence

Concentre toutes les options de présentation visuelle des résultats sur la carte. Les paramètres sont automatiquement enregistrés dans `{Red}_Results_Config.cfg` dans le dossier `Results/` du projet et restaurés lors de la session suivante.

> 💡 Chaque commande numérique de l'onglet Apparence possède un petit bouton individuel ↺ qui restaure uniquement ce champ à sa valeur par défaut, sans affecter le reste des paramètres.

> ⚠️ Les contrôles du groupe **Nodes** sont automatiquement désactivés lorsque le combo Nodes est défini sur "Aucun", et il en va de même pour **Links**. De plus, le contrôle **Décimales** est désactivé lorsque la variable active est **Statut** (variable catégorielle sans décimales applicables).

#### Étiquettes de carte

| Options | Descriptif |
|--------|-------------|
| **Taille de police (pt)** | Taille de police des étiquettes sur la carte (6 à 24 pts, 8 par défaut). |
| **Nœuds / Liens décimaux** | Nombre de décimales affichées respectivement sur les étiquettes des nœuds et des tuyaux (0 à 6). Le contrôle est étiqueté avec le nom de la variable actuellement active. |
| **Couleur du texte** | Couleur par défaut : nœuds **#333333** (gris foncé), passepoil **#0A143C** (bleu marine). **Noir** : texte toujours noir. **Par plage** : La couleur du texte suit la palette de la plage de valeurs active. Lorsque **Show Node ID** ou **Show Link ID** est actif, la ligne Id utilise la couleur de l'élément lui-même et la ligne de valeur utilise la couleur du symbole ou de la plage. |
| **Contexte** | Couleur d’arrière-plan derrière les étiquettes de carte. Comprend un sélecteur de couleurs et un bouton de suppression pour supprimer l'arrière-plan. A côté du sélecteur se trouve une icône **cadenas** : ouvert (par défaut), le fond des étiquettes est indépendant du fond de la carte ; Lorsque vous le fermez, le sélecteur et le bouton d'effacement sont désactivés et l'arrière-plan des étiquettes est lié à la couleur **Map Background** (voir ci-dessous), donc changer cette couleur modifie également automatiquement l'arrière-plan des étiquettes. |
| **Tampon** | Couleur du contour (halo) autour du texte de l'étiquette, avec son propre sélecteur de couleur et son propre bouton de suppression. Il est indépendant du Fond et n’est jamais lié au Fond de la Carte. Sans couleur attribuée (par défaut), aucun halo n'est dessiné. |
| **Afficher l'ID du nœud** / **Afficher l'ID du lien** | Deux cases indépendantes : ajoutez respectivement l'ID du nœud ou du canal dans la première ligne de son label. |

#### Symbologie

| Options | Descriptif |
|--------|-------------|
| **Masquer la bordure aux carrefours** | Masque le bord/contour des marqueurs de jonction. L'activation de cette option supprime le contour entourant le symbole du nœud. |
| **Proportionnel à la valeur** | Met à l'échelle la taille des nœuds et l'épaisseur des tuyaux de manière linéaire avec la valeur représentée. Ne s'applique pas au champ Statut. |
| **Facteur de nœuds** | Facteur d'échelle de base de la taille du marqueur de nœud (0,25 à 4,0, 1,0 par défaut). |
| **Facteur de liens** | Facteur d'échelle de base de l'épaisseur du tuyau (0,25 à 4,0, 1,0 par défaut). |
| **Facteur de flèches** | Facteur d’échelle des flèches de direction du flux (0,25 à 4,0, 1,0 par défaut). |

#### Fond de carte

Vous permet de définir une couleur d’arrière-plan unie pour le canevas de la carte lors de l’affichage des résultats. La couleur est restaurée à l'original lorsque le quai est fermé. Le bouton ****** supprime la couleur d'arrière-plan.

#### Tout réinitialiser

Ramène tous les paramètres de l'onglet Apparence à leurs valeurs par défaut.

---

### Scénarios

Le dock prend en charge plusieurs scénarios de résultats. Chaque scénario est identifié par un nom (par défaut `Base`) et est stocké sous forme de fichiers `.out` / `.hyd` dans le sous-dossier `Results/` du projet. Le nom du scénario actif apparaît dans le titre du panneau.

---

### Propriétés disponibles

**Noeuds** (Jonctions, Réservoirs, Réservoirs) :

| Propriété | Descriptif |
|-----------|-------------|
| `Pressure` | Pression en m.c.a. |
| `Head` | Hauteur piézométrique en m |
| `Demand` | Demande calculée |
| `Quality` | Qualité de l'eau (selon le type configuré dans les options d'analyse) |

**Tuyaux, vannes et pompes** (Liens) :

| Propriété | Descriptif |
|-----------|-------------|
| `Flow` | Débit (avec signe ou sans signe) |
| `Velocity` | Vitesse en m/s |
| `HeadLoss` | Perte de charge en m |
| `UnitHdLoss` | Perte unitaire en m/km |
| `FricFactor` | Facteur de friction |
| `Status` | Statut opérationnel (Ouvert / Actif / Fermé) |
| `ReactRate` | Taux de réaction (modèles de qualité) |
| `Quality` | Qualité de l'eau |

> 💡 Les étiquettes de carte pour la variable **Flow** affichent toujours la valeur absolue (sans signe négatif), même dans les modes statistiques Maximum et Minimum. Le sens du flux est indiqué par les flèches de direction et non par le signe de valeur.

---

## Séries chronologiques (Séries chronologiques…)

**Barre d'analyse → Série chronologique…**

Active un outil de sélection interactif qui trace l'évolution temporelle de toute propriété de résultat pour un ou plusieurs éléments du réseau.

<figure><img src="../assets/images/analisis/time-series-dock.png" alt="Panel Séries temporelles avec courbes de pression multi-nœuds"><figcaption><p>Panel Séries temporelles avec courbes de pression multi-nœuds</p></figcaption></figure>
*Panel Séries temporelles : évolution temporelle de la pression dans plusieurs nœuds sélectionnés simultanément.*

### Processus

1. Activez **Séries temporelles** (bouton cochable). Le panneau Séries temporelles s'ouvre en bas de l'écran.
2. Cliquez sur n'importe quel élément de la carte (nœud, canalisation, vanne, pompe, réservoir, réservoir).
3. Le panneau dessine la courbe temporelle de la propriété active dans le dock Résultats pour cet élément.
4. L'élément est surligné en bleu sur la carte.

### Sélection multiple

- **Shift + clic** sur un autre élément : ajoute sa courbe au graphique sans supprimer les précédentes. Chaque courbe reçoit une couleur différente de la palette.
- **Shift + clic** sur un élément déjà sélectionné : le supprime du graphique.
- **Cliquez sans Shift** avec plus d'une courbe active : demande une confirmation avant d'effacer la sélection.

### Sélection de propriété

- Par défaut, la propriété active est représentée dans le dock Résultats pour le type d'élément cliqué.
- **Clic droit** sur un élément : ouvre un menu contextuel pour choisir toutes les autres propriétés disponibles pour cet élément sans modifier la vue du dock Résultats.

### Propriétés supplémentaires pour les buckets

Pour le type d'élément **Tank**, deux quantités supplémentaires sont disponibles :

| Magnitude | Descriptif |
|----------|-------------|
| **Volume** | Volume stocké en m³ (ou ft³ selon les unités du projet), calculé à partir des binaires de sortie EPANET. |
| **Déversement de réservoir** | Débordement. Il n'est différent de zéro que si l'option de débordement EPANET est activée dans le référentiel. |

### Variables globales du réseau

En plus des éléments individuels, le panneau Séries temporelles vous permet d'ajouter des **séries globales** qui regroupent les valeurs sur l'ensemble du réseau. Ces séries ne nécessitent pas de cliquer sur la carte : elles sont ajoutées depuis le menu de sélection des variables du graphique.

| Variable globale | Descriptif |
|-----------------|-------------|
| **Approvisionnement total en eau** | Débit total fourni par tous les réservoirs et sources du réseau. |
| **Demande totale en eau** | Demande totale consommée par tous les nœuds du réseau. |
| **Pression moyenne du nœud** | Pression moyenne de tous les nœuds (exclut les réservoirs et les réservoirs). |
| **Volume total stocké** | Volume total stocké en ajoutant tous les dépôts du réseau. |
| **TotalTankSpill** | Débordement total additionnant tous les réservoirs du réseau. |

### Configuration des courbes

À partir du panneau Série temporelle, vous pouvez ajuster chaque courbe :

- Nom dans la légende.
- Couleur, style de trait (plein, pointillé, pointillé) et épaisseur.
- Marqueurs : symbole, taille, couleur, espace.
- Afficher les valeurs à chaque point de la courbe.
- Visibilité (afficher/masquer sans supprimer).

### Tableau des valeurs

Le tableau des valeurs affiche les données numériques de toutes les courbes actives. La **première colonne** (instant instantané) est **fixe** : elle ne disparaît pas lors du défilement horizontal du tableau lorsqu'il y a beaucoup de courbes. Cela permet d'identifier facilement où se trouve chaque ligne sans avoir à revenir au début.

### Synchronisation avec la table de valeurs

Lorsque vous déplacez le curseur sur le graphique, la ligne correspondante du tableau boursier est automatiquement mise en évidence en temps réel.

### Copier le tableau dans le presse-papiers

La fonction de copie génère **deux lignes d'en-tête** : la première avec le nom de l'élément ou de la magnitude et la seconde avec l'unité. Facilite le collage direct dans des feuilles de calcul.

### Exporter et importer les paramètres du graphique

Les boutons **Exporter la configuration du graphique** et **Importer la configuration du graphique** enregistrent et récupèrent la configuration complète des courbes, des axes et des styles dans un fichier `.cfg`. Il est également possible d'exporter la configuration générale du modèle (axes, styles) même si aucune courbe n'est chargée, et de l'appliquer lors de son import sur un nouveau graphique.

### Plusieurs fenêtres de graphique

Le bouton **Nouvelle fenêtre de graphique** ouvre une nouvelle fenêtre de série chronologique indépendante. Chaque fenêtre possède son propre contexte de courbe, ses propriétés et ses éléments sélectionnés. Vous pouvez garder plusieurs fenêtres ouvertes simultanément pour comparer différentes variables ou zones du réseau.

### Synchronisation du format d'heure

La colonne « Heure du jour » du tableau des valeurs utilise automatiquement le même format (24h ou am/pm) que le panneau Résultats.

### Clôture

Lorsque vous désactivez le bouton **Séries temporelles** ou fermez le panneau, la surbrillance disparaît et le curseur revient au mode de navigation standard.
