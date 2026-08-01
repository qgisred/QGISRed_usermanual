# Création d'éléments

Les cinq premiers outils de la barre Edition vous permettent d'ajouter des éléments au réseau. Ils activent tous un **mode d'édition interactif** : le curseur change et le plugin attend une action sur la carte. Pour annuler sans rien créer, appuyez à nouveau sur le même bouton ou appuyez sur `Esc`.

---

## Ajouter un tuyau

**Barre d'édition → Ajouter un tuyau**

Mode dessin au trait : chaque clic ajoute un sommet au tuyau. L'outil reste actif jusqu'à ce que vous ayez terminé la mise en page.

<figure><img src="../assets/images/edicion/add-pipe.png" alt="Ajouter un outil de canalisation en action sur la carte QGIS"><figcaption><p>Ajouter un outil de canalisation en action sur la carte QGIS</p></figcaption></figure>
*Dessiner un tuyau : La ligne rouge temporaire suit le curseur jusqu'au prochain clic.*

### Processus

1. Activez l'outil. Le curseur passe en mode dessin.
2. Cliquez pour définir le **point de départ**. QGISRed crée automatiquement une jonction à ce point s'il n'en existe aucune dans le rayon de tolérance.
3. Cliquez pour ajouter des **sommets intermédiaires** (points d'arrêt du chemin).
4. **double-cliquez** ou appuyez sur le **bouton droit** pour terminer le pipeline. QGISRed crée un deuxième nœud au point final.

### Ce que QGISRed crée lors de la confirmation

- Un enregistrement en `{Red}_Pipes.shp` avec la géométrie dessinée.
- Jusqu'à deux nouveaux nœuds en `{Red}_Junctions.shp` (un par extrémité), si un nœud n'existait pas déjà dans la tolérance configurée.
- Les valeurs de diamètre, de rugosité et de demande sont extraites des **Valeurs par défaut** du projet.

### Se connecter aux éléments existants

Si le point de départ ou d'arrivée se situe dans la tolérance d'un nœud, d'une vanne, d'une pompe, d'un château d'eau ou d'un réservoir existant, le nouveau tuyau **se connecte à cet élément** au lieu de créer un nouveau nœud.

> Le réglage au nœud le plus proche utilise la tolérance configurée dans **Barre de projet → Valeurs par défaut → Tolérance de nœud**. Vous pouvez le consulter ou le modifier avant de dessiner des réseaux denses.

---

## Ajouter un château d'eau (Add tank)

**Édition Barra → Ajouter un château d'eau**

Placez un château d'eau de stockage (Tank) sur la carte. Les châteaux d'eau ont un niveau variable et participent à la simulation hydraulique.

### Processus

1. Activez l'outil. Le curseur affiche l'icône de château d'eau.
2. Cliquez sur un **nœud existant** ou sur un point vide de la carte.
- Si vous cliquez sur un nœud existant, ce nœud **devient** un Tank.
- Si vous cliquez sur un point vide, QGISRed crée un nouveau Tank (pas de connexion initiale ; vous devrez le connecter avec un tuyau).
3. QGISRed ouvre la boîte de dialogue des propriétés du nouveau château d'eau afin que vous puissiez saisir les données (élévation du fond, niveau initial, niveau minimum, niveau maximum, diamètre).

### Principaux paramètres du château d'eau

| Paramètre | Descriptif |
|-----------|-------------|
| **Élévation** | Élévation du fond du château d'eau (m ou pi) |
| **InitLevel** | Niveau d'eau initial au-dessus du fond |
| **MinLevel** | Niveau de fonctionnement minimum |
| **MaxLevel** | Niveau de fonctionnement maximum |
| **Diamètre** | Diamètre du château d'eau (pour section circulaire) ; si vous utilisez la courbe de volume, mettez 0 |
| **MinVol** | Volume minimum (facultatif) |
| **VolCurve** | ID de courbe de volume (pour géométrie non cylindrique) |

---

## Ajouter un réservoir (Add reservoir)

**Barre d'édition → Ajouter un réservoir**

Placer un réservoir externe ou un point d'alimentation (Réservoir). Contrairement au Château d'eau, le Réservoir a **niveau fixe** (hauteur piézométrique constante) et représente une source d'eau de capacité illimitée.

Le processus est identique à celui du château d'eau. Les paramètres sont plus simples :

| Paramètre | Descriptif |
|-----------|-------------|
| **Tête** | Charge piézométrique fixe (élévation du niveau d'eau libre, m ou ft) |
| **Modèle** | Modèle de variation de charge dans le temps (facultatif) |

> Utiliser des réservoirs pour représenter des points de distribution d'eau en crue (raccordements avec des systèmes externes) ou des points d'approvisionnement à débit constant.

---

## Insérer la vanne dans le tuyau (Insérer la vanne dans le tuyau)

**Édition Barra → Insérer la vanne dans le tuyau**

Insérez une vanne dans un tuyau existant. Le tuyau d'origine est **divisé en deux sections** qui sont reliées par la vanne.

<figure><img src="../assets/images/edicion/insert-valve.png" alt="Résultat de l'insertion d'une vanne : le tuyau d'origine est divisé en deux"><figcaption><p>Résultat de l'insertion d'une vanne : le tuyau d'origine est divisé en deux</p></figcaption></figure>
*Le tuyau P-12 d'origine est divisé en P-12 et P-13, avec la vanne V-1 entre eux.*

### Processus

1. Activez l'outil. Le curseur se transforme en icône de vanne.
2. Cliquez sur le tuyau où vous souhaitez insérer la vanne.
3. QGISRed détermine le point d'insertion exact (projection du clic sur l'axe du tuyau) et :
- Créez un nœud à ce stade.
- Divise le tuyau d'origine en deux sections avec les mêmes attributs de diamètre et de matériau.
- Créer la valve entre les deux nouvelles extrémités.
4. La boîte de dialogue des propriétés s'ouvre pour configurer le type et le réglage de la vanne.

### Types de vannes disponibles

| Tapez | Nom | Fonction |
|------|--------|---------|
| **PRV** | Soupape de réduction de pression | Réduit la pression en aval jusqu'au point de consigne |
| **PSV** | Soupape de maintien de pression | Maintient la pression en amont au point de consigne |
| **PBV** | Soupape de disjoncteur de pression | Produit une perte de charge fixe |
| **FCV** | Vanne de contrôle de débit | Limite le débit au point de consigne |
| **TCV** | Soupape de commande des gaz | Simule une vanne partiellement fermée à l'aide d'un coefficient de perte |
| **GPV** | Vanne à usage général | Perte de charge définie par une courbe personnalisée |

---

## Insérer la pompe dans le tuyau (Insérer la pompe dans le tuyau)

**Édition Barra → Insérer la pompe dans le tuyau**

Insérez une pompe dans un tuyau existant, en la divisant exactement de la même manière qu'avec des vannes.

### Processus

1. Activez l'outil et cliquez sur le tuyau.
2. QGISRed divise le tuyau et crée la pompe entre les deux sections résultantes.
3. La boîte de dialogue des propriétés s'ouvre pour configurer la courbe H-Q et la vitesse initiale.

### Paramètres de la pompe

| Paramètre | Descriptif |
|-----------|-------------|
| **Courbe** | ID de courbe H-Q (obligatoire pour simuler) |
| **Vitesse** | Facteur de vitesse initial (1,0 = vitesse nominale) |
| **Modèle** | Modèle de variation de vitesse |
| **Puissance** | Puissance constante (alternative à la courbe H-Q) |

> Si la pompe nécessite une courbe d'efficacité pour le calcul de l'énergie, définissez-la dans **l'éditeur de modèles et de courbes** et référencez-la à partir des propriétés de la pompe.
