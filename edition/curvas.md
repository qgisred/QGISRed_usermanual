# Modèles et courbes

**Barra Edition → Modifier les motifs et les courbes…**

L'éditeur de motifs et de courbes centralise la gestion des données temporelles et fonctionnelles qui contrôlent le comportement dynamique du modèle : comment varie la demande au cours de la journée, comment se comporte une pompe en fonction de son débit, ou encore quel est le volume d'un réservoir irrégulier.

<figure><img src="../assets/images/edicion/editor-curvas.png" alt="Éditeur de motifs et de courbes QGISRed"><figcaption><p>Éditeur de motifs et de courbes QGISRed</p></figcaption></figure>
*Éditeur de motifs et de courbes : liste des éléments à gauche, graphique et tableau de données à droite.*

---

## Modèles de demande (modèles)

Un modèle définit la manière dont vous multipliez la demande de base d'un nœud (ou un autre paramètre) à chaque intervalle de temps de simulation.

### Structure d'un motif

Chaque motif a :
- Un **ID** unique (référencé depuis les nœuds ou bombes).
- Une liste de **facteurs multiplicateurs**, un par intervalle de temps.
- Le **pas de temps du motif** est défini dans les options de simulation ; Si le modèle comporte moins de facteurs que les intervalles de simulation, les valeurs sont répétées de manière cyclique.

### Exemple

Un modèle de 24 facteurs temporels pour une simulation de 24 heures :

```
ID: DomResidential
Factores: 0.4  0.3  0.3  0.3  0.4  0.7  1.1  1.3  1.2  1.0  0.9  0.9
          1.0  1.1  1.0  0.9  1.0  1.2  1.3  1.2  1.0  0.8  0.6  0.4
```

Le nœud avec une demande de base de 2,0 L/s et un modèle `DomResidential` consomme 0,8 L/s à 0 h (2,0 × 0,4) et 2,6 L/s à 7 h (2,0 × 1,3).

### Modification dans la boîte de dialogue

1. Sélectionnez un modèle existant dans la liste ou appuyez sur **Nouveau** pour en créer un.
2. Entrez les facteurs dans le tableau (une ligne par intervalle).
3. Le graphique est mis à jour en temps réel.
4. Vous pouvez **importer des facteurs depuis CSV** (une colonne de valeurs numériques) à l'aide du bouton d'importation.

---

## Courbes de comportement (Courbes)

Les courbes mettent en relation deux grandeurs physiques. EPANET utilise quatre types :

### Courbe H-Q de la pompe (Courbe de la pompe)

Il relie la **Hauteur manométrique** (Tête, axe Y) au **Débit** (Débit, axe X). Définit le point de fonctionnement de la pompe à vitesse nominale.

| Nombre de points | Méthode de réglage |
|--------------|-----------------|
| 1 point | QGISRed s'adapte à la courbe standard EPANET : H₀ = 133% du point, étant donné Q₀, Hmax = 0 à 2×Q₀ |
| 3 points | Ajustement polynomial du deuxième degré passant par les trois points |
| N points | Interpolation linéaire entre points (courbe libre) |

> La courbe H-Q doit avoir une **pente négative** (hauteur de chute plus élevée à débit plus faible). EPANET avertira si la courbe a une pente positive dans une section.

### Courbe d'efficacité (Courbe d'efficacité)

Associe l'**Efficacité** (%) au **Débit** (Débit). Il est utilisé pour l’analyse de la consommation d’énergie. S'il n'est pas défini, EPANET utilise l'efficacité globale du projet.

### Courbe de volume (Courbe de volume)

Relie le **Niveau** du réservoir (m ou ft, axe X) au **Volume** stocké (m³ ou gallons, axe Y). Nécessaire pour les réservoirs à géométrie non cylindrique (bassins coniques, réservoirs de forme irrégulière).

### Courbe de perte de charge GPV (Courbe de perte de charge)

Pour les vannes de type **GPV** (General Purpose Valve), reliez la **Perte de charge** (m ou ft) au **Débit** (Débit). Il permet de modéliser tout appareil de commande hydraulique dont la courbe caractéristique est connue.

---

## Créer et modifier des courbes

1. Sélectionnez le type de courbe dans le sélecteur supérieur.
2. Choisissez une courbe existante dans la liste ou appuyez sur **Nouveau**.
3. Entrez les paires de points (X, Y) dans le tableau.
4. Le graphique montre la courbe résultante avec l'interpolation ou l'ajustement correspondant.
5. Appuyez sur **OK** pour enregistrer. Les courbes sont stockées dans `{Red}_Options.dbf`.

> Pour référencer une courbe d'une pompe ou d'un réservoir, copiez son **ID** exact dans le champ correspondant de la boîte de dialogue des propriétés de l'élément.
