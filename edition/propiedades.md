# Propriétés des éléments

**Barre d'édition → Modifier les propriétés de l'élément…**

La boîte de dialogue des propriétés est l'outil central pour afficher et modifier tous les attributs de n'importe quel élément de réseau. Il fonctionne comme un formulaire intelligent qui charge les données de l'élément cliqué et vous permet de naviguer entre les éléments sans le fermer.

<figure><img src="../assets/images/edicion/propiedades-elemento.png" alt="Boîte de dialogue Propriétés d'un tuyau avec tous ses champs"><figcaption><p>Boîte de dialogue Propriétés d'un tuyau avec tous ses champs</p></figcaption></figure>
*Boîte de dialogue Propriétés : attributs des éléments, navigateur d'éléments connectés et bouton de centrage.*

---

## Comment ouvrir la boîte de dialogue

1. Activez l'outil en appuyant sur le bouton **Modifier les propriétés de l'élément…** (icône crayon/modifier).
2. Cliquez sur n'importe quel élément du réseau sur la carte : canalisation, nœud, vanne, pompe, château d'eau ou réservoir.
3. La boîte de dialogue s'ouvre affichant tous les attributs de l'élément sélectionné.

> L'outil reste actif tant que le bouton est enfoncé. Vous pouvez cliquer sur différents éléments sans l'activer à nouveau.

---

## Champs de canal

| Champ | Descriptif |
|-------|-------------|
| **ID** | Identifiant unique du tuyau |
| **Longueur** | Longueur automatiquement calculée à partir de la géométrie (m ou ft) |
| **Diamètre** | Diamètre intérieur (mm ou pouces) |
| **Coeff de rugosité** | Rugosité pour la formule de perte de charge configurée |
| **MinorLoss** | Coefficient de perte mineure (0 si non applicable) |
| **InitStatus** | État initial : Ouvert, Fermé ou CV (clapet anti-retour) |
| **Matériel** | Code matériau (référencé dans le tableau des matériaux) |
| **InstallYear** | Année d'installation (format `YYYY`), utilisée pour le calcul de la rugosité au vieillissement |
| **BulkCoeff** | Coefficient de réaction massique (pour les modèles de qualité de type chimique) |
| **WallCoeff** | Coefficient de réaction des parois (pour les modèles de qualité de type chimique) |

---

## Champs de nœuds (Jonctions)

| Champ | Descriptif |
|-------|-------------|
| **ID** | Identificateur de nœud unique |
| **Élévation** | Hauteur du nœud (m ou pi) |
| **Demande** | Demande de base (en unités de flux du projet) |
| **Modèle** | ID du modèle de demande appliqué |
| **EmitterCoeff** | Coefficient d'émetteur (pour modéliser les fuites dépendant de la pression) |
| **InitQuality** | Concentration ou âge initial de l'eau (uniquement si le modèle de qualité est actif) |

### Demandes multiples

Les nœuds peuvent avoir plus d'une demande (catégories d'utilisateurs : résidentiel, industriel, etc.). Si le projet possède la couche facultative `{Red}_MultipleDemands.shp`, la boîte de dialogue affiche une section supplémentaire dans laquelle vous pouvez ajouter, modifier et supprimer des demandes par catégorie :

| Champ | Descriptif |
|-------|-------------|
| **Demande** | Valeur de la demande pour cette catégorie |
| **Modèle** | Modèle de demande spécifique à une catégorie |
| **Nom** | Étiquette de catégorie (informative) |

---

## Champs des châteaux d'eau (Tanks)

| Champ | Descriptif |
|-------|-------------|
| **ID** | Identifiant unique |
| **Élévation** | Niveau inférieur du château d'eau |
| **InitLevel** | Niveau d'eau initial en arrière-plan |
| **MinLevel** | Niveau de fonctionnement minimum |
| **MaxLevel** | Niveau de fonctionnement maximum |
| **Diamètre** | Diamètre du château d'eau (0 si utilisation de la courbe de volume) |
| **MinVol** | Volume minimal (m³) |
| **VolCurve** | ID de courbe de volume (pour géométrie non cylindrique) |
| **MixModel** | Modèle de mélange : MIXTE, 2COMP, FIFO, LIFO |
| **MixFraction** | Fraction du premier compartiment (modèle 2COMP) |

---

## Champs des réservoirs (Reservoirs)

| Champ | Descriptif |
|-------|-------------|
| **ID** | Identifiant unique |
| **Tête** | Hauteur piézométrique fixe (m ou ft) |
| **Modèle** | Modèle de variation de charge dans le temps |

---

## Champs de vannes (Vannes)

| Champ | Descriptif |
|-------|-------------|
| **ID** | Identifiant unique |
| **Diamètre** | Diamètre (mm ou pouces) |
| **Type de vanne** | Type de vanne : PRV, PSV, PBV, FCV, TCV, GPV |
| **Paramètre** | Consigne de régulation (pression, débit ou perte de charge selon le type) |
| **MinorLoss** | Coefficient de perte mineure |
| **InitStatus** | État initial : Ouvert, Fermé, Actif |

---

## Champs de bombes (pompes)

| Champ | Descriptif |
|-------|-------------|
| **ID** | Identifiant unique |
| **Courbe** | ID de courbe H-Q de la pompe |
| **Vitesse** | Facteur de vitesse de rotation (1,0 = nominal) |
| **Modèle** | Modèle de variation de vitesse |
| **Puissance** | Puissance constante (alternative à la courbe H-Q) |
| **EfficiencyCurve** | ID de courbe d'efficacité (pour analyse énergétique) |
| **EnergyPrice** | Prix ​​énergétique spécifique pour cette pompe |
| **PricePattern** | Modèle de variation des prix de l'énergie |
| **InitStatus** | Etat initial : Ouvert ou Fermé |

---

## Navigation entre les éléments

La boîte de dialogue comprend un **navigateur** (Browser) qui permet :

- **Aller à l'élément connecté** : répertorie les nœuds et éléments connectés à l'élément actuel pour y accéder.
- **Historique** : boutons Précédent / Suivant pour revenir aux éléments précédemment visités sans fermer la boîte de dialogue.
- **Centrer sur la carte** : bouton pour déplacer la carte vers l'élément actuellement affiché.

> Lors de la navigation vers un autre élément à partir de la boîte de dialogue, QGISRed enregistre les modifications de l'élément précédent avant de charger le nouveau. Il n'est pas nécessaire de cliquer explicitement sur "Accepter" après chaque modification.

---

## Champs exclusifs QGISRed

Ces champs ne font pas partie du standard EPANET mais sont utilisés par le plugin :

| Champ | Couche | Descriptif |
|-------|------|-------------|
| **Matériel** | Tuyaux | Code matériau référencé dans le tableau des matériaux |
| **InstallYear** | Tuyaux | Année d'installation pour le calcul de la rugosité due au vieillissement |
| **IsActive** | Divers | Activer/désactiver l'élément dans le Digital Twin |
| **Étiquette** | Tout | Tag gratuit (équivalent au champ EPANET TAG) |
