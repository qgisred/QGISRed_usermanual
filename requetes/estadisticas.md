# Statistiques

**Barre de requêtes → Statistiques…**

Ouvre le panneau **Statistiques**, qui calcule et affiche la distribution statistique de tout attribut numérique ou catégoriel du réseau, avec prise en charge de la classification automatique, de la seconde classification croisée et de la représentation graphique.

> **ℹ️ Remarque :** Le panneau Statistiques s'ouvre **ancré** dans la fenêtre principale de QGIS et respecte les panneaux déjà regroupés en onglets.

<figure><img src="../assets/images/consultas/statistics-panel.png" alt="Panneau de statistiques avec histogramme des diamètres de tuyaux"><figcaption><p>Panneau de statistiques avec histogramme des diamètres de tuyaux</p></figcaption></figure>
*Panneau de statistiques : histogramme des diamètres de tuyaux avec classification par intervalles.*

---

## Structure du panneau

Le panneau Statistiques est organisé en deux onglets :

- **Setup** : définit ce qui est analysé et comment c'est classé.
- **Rapport** : affiche l'histogramme et le tableau des résultats. Il est activé automatiquement après l'exécution de l'analyse.

---

## Onglet Configuration

### Type d'élément et propriété

Sélectionnez le type d'élément (Jonctions, Canalisations, Réservoirs...) et la propriété à analyser. Le sélecteur de propriétés affiche dans une **liste unifiée** à la fois les champs de conception (Diamètre, Longueur, Rugosité...) et les champs de résultat de simulation (Pression, Débit, Vitesse...). Les champs de résultat apparaissent sur un **fond jaune/crème** pour les différencier visuellement des champs de conception.

### Classement principal

| Paramètre | Descriptif |
|-----------|-------------|
| **Champ** | Propriété à trier par |
| **Méthode** | Comment calculer les intervalles (voir tableau ci-dessous) |
| **Nombre de cours** | Combien de groupes sont générés |

#### Méthodes de tri disponibles

Les méthodes suivantes sont disponibles pour le tri principal et le deuxième tri. La méthode par défaut est **Pretty Breaks**.

| Méthode | Descriptif |
|--------|-------------|
| **Jenks (Pauses naturelles)** | Minimise la variance intra-classe. Idéal pour les distributions non uniformes. |
| **Jolies pauses** | Limites d'intervalle "arrondies". Préférable pour les présentations. *(Par défaut)* |
| **Nombre égal** | Chaque classe contient le même nombre d'éléments. |
| **Intervalle fixe** | Tous les intervalles ont la même amplitude. |
| **Manuel** | L'utilisateur définit directement les limites de chaque intervalle. |

> **ℹ️ Remarque :** Lorsque toutes les valeurs sont identiques ou très similaires, les points de terminaison de classe en double sont réduits en affichant une seule valeur au lieu de "100,0 - 100,0".

> **ℹ️ Remarque :** Lors de l'analyse d'un champ de résultat de simulation dynamique, les **limites de classe sont calculées une fois** en tenant compte de tous les instants simultanément. Au fur et à mesure de l'étape de simulation, le nombre d'éléments par barre varie, mais les limites restent constantes, permettant **de comparer les distributions entre instants de temps** en toute cohérence.

### Pré-filtrage

Avant de calculer, vous pouvez limiter l'ensemble des éléments avec une condition sur n'importe quel champ :

- Champs **numériques** : `>=`, `<=`, `=`, `>`, `<`, `≠`, `Range`
- **liste** champs : `=`
- Champs **texte** : `=`, `≠`, `ILIKE`, `NOT ILIKE`, `LIKE`, `NOT LIKE`
- Sélectionnez **Aucun filtre** pour inclure tous les éléments sans restriction.

Le champ **Valeur** comprend un bouton d'effacement **(×)** : lorsqu'il est enfoncé, il efface le texte saisi et ne laisse aucune sélection active, ce qui facilite le changement rapide du filtre.

Lorsque l'attribut de filtre est un champ de résultat de simulation, la combinaison affiche le même **fond jaune/crème** que celui utilisé pour ces champs dans le sélecteur de propriétés.

> **ℹ️ Note — Débit :** Lors d'un filtrage sur le champ `Flow` avec une valeur numérique écrite, la valeur est toujours interprétée comme **valeur absolue**, il n'est donc pas nécessaire de connaître le signe qu'EPANET attribue en interne au flux.

#### Aperçu sur la carte

La section Filtres comprend deux éléments supplémentaires pour analyser le filtre avant d'exécuter l'analyse complète :

- **case à cocher « Aperçu sur la carte »** : lorsque cette case est cochée, les éléments qui répondent à la condition de filtre sont surlignés en **orange** sur le canevas de la carte. L'aperçu se met automatiquement à jour lorsque vous modifiez un paramètre de filtre.
- **Compteur de correspondance** (par exemple *"43 éléments correspondent"*) : visible à chaque fois que la section Filtres est affichée, avant même de lancer l'analyse.

Les surbrillances sont automatiquement supprimées lorsque vous fermez le panneau ou réduisez la section Filtres.

### Deuxième classement *(facultatif)*

Un groupe réductible (réduit par défaut) permet de définir un **deuxième critère de classification** sur le même ensemble d'éléments. Une fois déployés, les éléments suivants sont configurés :

| Paramètre | Descriptif |
|-----------|-------------|
| **Champ** | Propriété de deuxième classement |
| **Méthode** | Jenks (pauses naturelles), jolies pauses, nombre égal, intervalle fixe ou manuel |
| **Nombre de cours** | Deuxièmes groupes de classification |

Lorsque le deuxième tri est actif, le tableau des résultats devient une **matrice croisée** : les lignes représentent les groupes du premier tri et les colonnes représentent les groupes du second.

> **ℹ️ Remarque :** Lors du changement de type d'élément et du retour au précédent, les deuxièmes paramètres de classification (méthode, nombre de classes, intervalles, valeurs manuelles) sont **automatiquement récupérés**.

---

## Onglet Rapport

L'onglet Rapport est divisé en deux cadres : **Histogramme** et **Tableau**.

### Histogramme

L'histogramme montre la distribution de la propriété analysée :

- **Sélecteur de statistiques** : Choisissez ce qui est représenté sur l'axe Y : Count, Sum, Avg, Min, Max ou StdD.
- **Bouton Développer** : ouvre l'histogramme dans une **fenêtre flottante séparée**, utile pour avoir le panneau de paramètres et le graphique visibles en même temps.
- Le **titre du graphique** comprend la statistique sélectionnée en préfixe et les unités du champ. Par exemple : *"Pression moyenne (mca) par diamètres (mm) pour le matériau PVC"*.
- Pour les champs catégoriels, l'histogramme affiche des barres par catégorie au lieu de plages numériques.

### Tableau des résultats

Le tableau affiche les mêmes données sous forme de tableau :

- Les valeurs sont formatées avec les décimales correspondant à chaque champ selon le CSV des unités du projet.
- Les nombres entiers sont affichés sans décimales.
- Le **titre du tableau** reflète toujours les deux dimensions de classification actives, y compris les unités de chaque champ.
- La **ligne d'exportation** comprend un sélecteur de statistiques pour choisir quelle valeur est vidée lors de l'exportation au format CSV (Count, Sum, Avg...).
- L'export CSV inclut les **valeurs de points d'arrêt manuels** des deux classifications (principale et seconde), avec les en-têtes de colonnes accompagnés des unités entre parenthèses.
- Lorsque le deuxième tri est actif, le tableau devient une **matrice croisée** avec des colonnes supplémentaires pour chaque groupe du deuxième tri.

---

## Champs disponibles

### Champs catégoriels

Les champs suivants sont traités comme des catégories (valeurs discrètes) :

| Champ | Descriptif |
|-------|-------------|
| `Material` | Matériau des tuyaux |
| `Type` | Type d'élément |
| `ValveType` | Type de vanne |
| `MeterType` | Type de compteur |
| `SourceType` | Type de police |
| `IniStatus` | Statut opérationnel initial (Ouvert / Fermé / CV) |
| `InstalDate` | Date d'installation |
| `InstDate` | Date d'installation |
| `Tag` | Étiquette gratuite |

### Champs de saisie numérique

Tout champ numérique du modèle : `Diameter`, `Length`, `Roughness`, `Elevation`, `BaseDem`, etc.

### Champs de résultats de simulation

Disponible uniquement si les résultats sont téléchargés :

**Noeuds :**

| Champ | Descriptif |
|-------|-------------|
| `Pressure` | Pression (m.c.a.) |
| `Head` | Hauteur piézométrique (m) |
| `Demand` | Demande calculée (l/s) |
| `Quality` | Qualité de l'eau |

**Tuyaux :**

| Champ | Descriptif |
|-------|-------------|
| `Status` | État en simulation |
| `Flow` | Débit (l/s) |
| `Velocity` | Vitesse (m/s) |
| `HeadLoss` | Perte de charge (m) |
| `UnitHdLoss` | Perte unitaire (m/km) |
| `FricFactor` | Facteur de friction |
| `ReactRate` | Taux de réaction |
| `Quality` | Qualité de l'eau |

> **⚠️ Remarque :** Les champs `Velocity`, `UnitHdLoss`, `FricFactor` et `ReactRate` ne sont pas disponibles lorsque le type d'élément sélectionné est **Pompes** ou **Valves** ; Ils sont exclusifs aux pipes.

---

## Notes d'utilisation

- Le panneau Statistiques ne modifie aucune donnée du modèle.
- Vous pouvez garder le panneau ouvert pendant que vous naviguez sur la carte ou modifiez les paramètres ; met à jour le calcul lorsque vous appuyez à nouveau sur le bouton Exécuter.
- La deuxième classification est réduite par défaut ; déployez-le uniquement lorsque vous avez besoin d’une analyse croisée.
