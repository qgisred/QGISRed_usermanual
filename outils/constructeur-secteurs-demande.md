# Constructeur de secteur de demande

**Barre d'outils → Générateur de secteur de demande…**

Le **Demand Sector Builder** est une boîte de dialogue modale qui vous permet de créer et de gérer plusieurs **sectorisations nommées** du réseau

<figure><img src="../assets/images/herramientas/constructor-sectores.png" alt="Boîte de dialogue Demand Sector Builder avec liste des sectorisations et paramètres de sujet"><figcaption><p>Boîte de dialogue Demand Sector Builder avec liste des sectorisations et paramètres de sujet</p></figcaption></figure>
*Demand Sector Builder : liste des sectorisations (panneau de gauche), paramètres de détection et sujets à générer (panneau de droite).*, chacun avec ses propres secteurs de demande. Chaque sectorisation regroupe les nœuds du réseau en zones selon la topologie et les limites définies par l'utilisateur, et génère les couches auxiliaires nécessaires pour une utilisation dans le Nodal Demand Builder ou pour l'analyse du bilan hydrique.

---

## Concepts clés

| Concepts | Descriptif |
|----------|-------------|
| **Sectorisation** | Ensemble nommé de secteurs qui couvre l’ensemble du réseau. Il peut y avoir plusieurs sectorisations dans un même projet. |
| **Secteur** | Sous-ensemble de nœuds et de liens délimités par des frontières. Chaque nœud appartient exactement à un secteur au sein d’une sectorisation. |
| **Thème** | Type de couche géométrique qui représente les secteurs. Le Builder peut générer jusqu'à 6 types de sujets pour chaque sectorisation. |
| **Bordure** | Élément ou ensemble d'éléments qui délimite deux secteurs adjacents (tuyaux frontaliers, vannes, débitmètres). |

---

## Créer et gérer des sectorisations

### Liste des sectorisations

Le volet gauche de la boîte de dialogue affiche toutes les tranches du projet. Chaque entrée contient :
- Nom modifiable.
- Boutons Ajouter (＋) et Supprimer (✕).

### Ajouter une sectorisation

1. Appuyez sur **＋** dans la liste des secteurs.
2. Entrez un nom convivial (par exemple, `Sectorizacion_2024`, `Zonas_Presion`).
3. Configurez les paramètres de détection et les rubriques à générer.
4. Appuyez sur **Build** pour exécuter l'analyse.

Les sectorisations sont stockées dans les couches auxiliaires du projet sous le groupe **Couches auxiliaires > DemandSectors**.

---

## Détection de secteur

Le Builder détecte les secteurs à l'aide d'un algorithme **BFS** (recherche en largeur) qui parcourt la topologie du réseau à partir des éléments de bordure marqués.

### Types de bordures

| Tapez | Descriptif |
|------|-------------|
| **Tuyaux** | Tuyaux marqués d'une bordure ; le flux qui les traverse délimite des secteurs |
| **Vannes d'isolement** | Vannes d'isolement dans le réseau |
| **Mètres** | Débitmètres (délimiter les secteurs de bilan hydrique) |

La sélection du type d'élément faisant office de bordure est configurée à l'aide des cases à cocher dans la boîte de dialogue. Plusieurs types peuvent être activés simultanément.

### Tolérance géométrique

Le générateur utilise une tolérance de **0,01 unités cartographiques** pour vérifier l'accord géométrique entre les nœuds et les éléments de limite. Les nœuds qui ne correspondent pas exactement au réseau mais qui se trouvent dans cette plage sont considérés comme connectés.

---

## Sujets générés

Pour chaque sectorisation, le Builder peut générer jusqu'à **6 types de sujets** :

| Thème | Géométrie | Descriptif |
|------|-----------|-------------|
| **Frontiers** | Lignes | Éléments frontaliers entre secteurs adjacents |
| **Links** | Lignes | Pipes et liens internes de chaque secteur |
| **Nodes** | Points | Nœuds de réseau avec le champ `SectorId` attribué |
| **Polygons** | Polygones | Enveloppe géométrique convexe de chaque secteur |
| **MultiLinks** | Multiligne | Tous les liens d'un secteur fusionnés en une seule géométrie par secteur |
| **MultiNodes** | Multipoints | Tous les nœuds d'un secteur fusionnés en une seule géométrie par secteur |

Les thèmes à générer sont sélectionnés individuellement avec des cases à cocher avant de cliquer sur **Build**. Au moins un sujet doit être actif.

---

## Validations d'intégrité

Avant de générer les secteurs, le Builder exécute **7 contrôles d'intégrité** :

1. Le réseau possède au moins un nœud.
2. Il existe des éléments de bordure du type sélectionné.
3. Il n'y a pas de nœuds isolés (pas de connectivité).
4. Les éléments de bordure disposent des champs nécessaires.
5. Il n'y a pas de secteurs vides (pas de nœuds).
6. Chaque nœud appartient exactement à un secteur.
7. Les polygones générés ne se chevauchent pas.

Si une validation échoue, la boîte de dialogue affiche un message d'erreur descriptif et ne génère pas les couches.

---

## Résultat dans le projet

Les couches pour chaque sectorisation sont créées dans le groupe **Couches auxiliaires > DemandSectors > [nom de la sectorisation]** dans le panneau des couches QGIS. Chaque couche de type de nœuds comprend le champ `SectorId` qui peut être utilisé directement dans **Nodal Demand Builder** pour attribuer des modèles ou des efficacités par secteur.

### Utilisation dans Nodal Demand Builder

Une sectorisation générée avec le Demand Sector Builder peut être sélectionnée dans le Nodal Demand Builder à l'aide de l'option **"Utiliser le thème des secteurs du projet"**, évitant ainsi d'avoir besoin d'importer un SHP externe. Voir [Exigences et scénarios](demandes-et-scenarios.md) pour plus de détails.

---

## Flux de travail typique

1. **Définir les bordures** : dans le calque Canalisations (ou Compteurs), marquer en bordure les éléments qui délimitent les secteurs (champ `IsFrontier` ou équivalent, ou par sélection).
2. **Ouvrez le Builder** : Outils → Demand Sector Builder.
3. **Créer une sectorisation** : appuyez sur ＋, nommez-la et sélectionnez les sujets à générer.
4. **Exécuter** : appuyez sur **Build**. Les couches apparaissent dans Couches auxiliaires > DemandSectors.
5. **Utilisation dans Nodal Demand Builder** : Dans la section Modèles sectoriels ou efficacités, choisissez la nouvelle sectorisation comme thème du projet.
