# Manipulation géométrique et topologique

Les outils du deuxième groupe de la barre Edition permettent de modifier la géométrie et la topologie du réseau sans rompre la connectivité. QGISRed maintient à tout moment la cohérence entre la géométrie spatiale et les données du modèle.

---

## Sélection multiple (Sélectionner plusieurs éléments)

**Barre d'édition → Sélectionnez plusieurs éléments**

Outil de sélection simultanée sur plusieurs calques. Activez-le et dessinez un rectangle sur la carte : tous les éléments de toutes les couches du projet qui relèvent de la zone sont sélectionnés.

La sélection est utilisée comme **entrée** pour d'autres outils : Inverser les éléments et Supprimer les éléments opèrent sur les éléments sélectionnés s'il y en a, ou vous demandent de cliquer sur la carte s'il n'y a pas de sélection précédente.

> Pour désélectionner, appuyez à nouveau sur le bouton ou utilisez `Ctrl+Shift+A` (désélection globale QGIS).

---

## Déplacer les nœuds (Déplacer les nœuds)

**Barre d'édition → Déplacer les nœuds**

Déplace un ou plusieurs nœuds (Jonctions, Réservoirs, Bâches) en entraînant avec lui **tous les éléments linéaires connectés** (tuyaux, vannes, pompes). Le réseau reste connecté après le mouvement.

<figure><img src="../assets/images/edicion/move-nodes.png" alt="Déplacer un nœud et ses tuyaux connectés sur la carte"><figcaption><p>Déplacer un nœud et ses tuyaux connectés sur la carte</p></figcaption></figure>
*Lorsque vous faites glisser un nœud, tous les tuyaux connectés suivent le mouvement.*

### Comment l'utiliser

1. Activez l'outil.
2. Cliquez sur le nœud que vous souhaitez déplacer (ou sur une zone de nœud dans le calque Jonctions).
3. Faites glisser vers la nouvelle position.
4. Relâchez le bouton de la souris pour confirmer.

> Cet outil ne déplace **pas** les sommets intermédiaires des tuyaux. Pour cela, utilisez **Modifier les sommets du lien**.

---

## Modifier les sommets du lien

**Barre d'édition → Modifier les sommets du lien**

Vous permet d'ajuster la disposition visuelle des tuyaux et autres éléments linéaires en manipulant leurs sommets intermédiaires. Cela n'affecte pas les nœuds d'extrémité ni la topologie.

### Opérations disponibles

| Actions | Geste |
|--------|-------|
| **Déplacer le sommet** | Cliquez sur un sommet existant (cercle bleu) et faites-le glisser |
| **Ajouter un sommet** | Cliquez sur le segment entre deux sommets pour en insérer un nouveau |
| **Supprimer le sommet** | Faites un clic droit sur un sommet pour le supprimer |

---

## Éléments inversés (Éléments inversés)

**Édition Barra → Éléments inversés**

Inverse l'**orientation** des tuyaux et des connexions de service. L'orientation détermine la direction positive de l'écoulement dans les résultats de simulation.

### Deux façons de l'utiliser

1. **Sursélection** : Sélectionnez un ou plusieurs tuyaux avec l'outil de sélection multiple et appuyez sur Inverser. Ils inversent tous leur orientation.
2. **Par clic** : Sans sélection préalable, appuyez sur Inverser et cliquez sur le tuyau que vous souhaitez inverser.

> L'inversion n'affecte que la convention de signe du débit dans les résultats. Il ne modifie pas le comportement hydraulique dans la simulation (EPANET calcule toujours le sens réel de l'écoulement, quelle que soit l'orientation mémorisée).

---

## Diviser/Joindre des tuyaux

**Édition Barra → Diviser/Joindre des tuyaux**

Cliquez sur un tuyau pour le **diviser** au point indiqué : QGISRed crée une nouvelle jonction à ce point et deux sections avec les mêmes attributs de diamètre, de matériau et d'InstallYear que l'original.

Pour **joindre** deux tuyaux, cliquez sur le nœud intermédiaire qu'ils partagent : si ce nœud a exactement deux tuyaux connectés et que les propriétés diamètre, matériau et InstallYear sont les mêmes, QGISRed les fusionne en une seule section et supprime le nœud.

<figure><img src="../assets/images/edicion/split-pipe.png" alt="Fractionner un tuyau : un nœud intermédiaire et deux sections sont créés"><figcaption><p>Fractionner un tuyau : un nœud intermédiaire et deux sections sont créés</p></figcaption></figure>
*Cliquer sur P-5 crée le nœud J-42 et divise le tuyau en P-5 et P-45.*

> Si les deux tuyaux ont des diamètres ou des matériaux différents, le raccordement ne se fait pas et le plugin affiche un avertissement.

---

## Fusionner/Dissoudre les jonctions

**Barra Edition → Fusionner/Dissoudre les jonctions**

Cet outil fonctionne en **deux clics** :

- **Un simple clic** (clic et sans second point) : **Sépare** le nœud indiqué en autant de nœuds indépendants qu'il y a de canalisations qui y sont connectées. Utile lorsqu'un nœud regroupe plusieurs tuyaux qui ne doivent pas être connectés topologiquement.
- **Deux clics** (origine → destination) : **Fusionne** le nœud d'origine avec le nœud de destination. Tous les tuyaux connectés au nœud d'origine sont reconnectés au nœud de destination. Le nœud d'origine disparaît.

Cas d'utilisation courants :
- Fusionner deux nœuds très proches qui ont été séparés lors de l'importation depuis `.inp`.
- Séparez un nœud à une jonction où les tuyaux ne sont pas réellement connectés.

---

## Créer/Supprimer des connexions T

**Barra Edition → Créer/Supprimer des connexions T**

Gère les joints en T : points où un nœud est très proche d'un tuyau mais **pas** connecté à celui-ci.

### Créer un T

1. Cliquez sur le nœud que vous souhaitez connecter.
2. Cliquez sur le tuyau auquel il doit être connecté.
3. QGISRed divise le tuyau au point le plus proche du nœud et connecte les deux avec un tuyau court, ou déplace le nœud vers le tuyau si la distance est inférieure à la tolérance.

### Supprimer un T

Cliquez sur la connexion T existante. QGISRed supprime le nœud intermédiaire et restaure le canal d'origine.

---

## Créer/Supprimer des croisements (Créer/Supprimer des croisements)

**Barre d'édition → Créer/Supprimer des croisements**

Gère les croisements entre les canalisations qui se croisent sur la carte :

- **Créer une jonction** : Cliquez sur le point d'intersection entre deux canalisations qui n'ont pas de nœud partagé. QGISRed divise les deux tuyaux et crée un nœud commun à l'intersection.
- **Supprimer la jonction** : cliquez sur un nœud de jonction comportant exactement quatre tuyaux connectés. QGISRed supprime le nœud et restaure les deux tuyaux d'origine qui passent au-dessus.

> Cet outil n'applique pas de capture pour éviter les faux positifs. La tolérance de détection de croisement utilise la valeur configurée dans **Valeurs par défaut**.

---

## Déplacer les vannes et les pompes (Déplacer les vannes/pompes)

**Édition Barra → Déplacer les vannes/pompes**

Déplace une vanne ou une pompe d'une canalisation à une autre en conservant toutes ses propriétés (type, réglage, courbe...).

### Processus

1. Activez l'outil. Le curseur demande le premier clic.
2. Cliquez sur le **tuyau source** (celui contenant la vanne/pompe actuelle).
3. Cliquez sur le **tube de destination** (là où l'élément sera inséré).
4. QGISRed supprime l'élément de sa position d'origine, restaure le tuyau d'origine et l'insère dans la nouvelle position.

---

## Changer le statut de l'élément

**Barre d'édition → Modifier le statut de l'élément**

Bascule l'état de fonctionnement (Ouvert/Fermé) des tuyaux et des vannes manuelles sans ouvrir la boîte de dialogue des propriétés.

- **Un seul clic** : basculer entre ouvert et fermé.
- **Ctrl + Clic** : Parcourez tous les états disponibles : Ouvert → Fermé → CV (clapet anti-retour) → Ouvert.

La couche **Isolation Valves** peut également être gérée avec cet outil si elle est chargée.

> L'état est stocké dans le champ `InitStatus` de la couche correspondante et exporté vers le `.inp` d'EPANET.

---

## Supprimer des éléments (Supprimer des éléments)

**Barre d'édition → Supprimer des éléments**

Supprimez un ou plusieurs éléments du projet. Cela fonctionne de deux manières :

1. **Sursélection** : sélectionnez les éléments avec l'outil de sélection multiple et appuyez sur Supprimer. Tous les éléments sélectionnés sont supprimés.
2. **Par clic** : Sans sélection, activez l'outil et cliquez sur l'élément à supprimer.

### Comportement lors de la suppression

| Situation | Que se passe-t-il |
|-----------|------------|
| Supprimer un tuyau | Le tuyau est retiré. Les nœuds d'extrémité restent s'ils ont d'autres connexions ; Ils sont éliminés s'ils s'isolent. |
| Supprimer un nœud avec des tuyaux connectés | Tous les tuyaux connectés sont également supprimés. |
| Retirer une vanne ou une pompe | Les deux sections de tuyau dans lesquelles il a été divisé sont automatiquement fusionnées en une seule. |
| Supprimer un réservoir ou une bâche | L'élément est converti en jonction ou supprimé s'il n'a aucune connexion. |

> La suppression est irréversible avec `Ctrl+Z`. QGISRed enregistre automatiquement l'état précédent du projet dans le dossier temporaire avant d'exécuter l'opération, mais le seul moyen de récupérer les données supprimées est d'utiliser une **sauvegarde** précédente.
