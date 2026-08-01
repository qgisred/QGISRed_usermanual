# Créer un projet

**Barre Générale → Créer un projet** (ou menu QGISRed → Général → Créer un projet)

Créez un tout nouveau projet QGISRed à partir de zéro, en générant la structure de fichiers SHP nécessaire pour définir un réseau de distribution.

<figure><img src="../assets/images/general/crear-proyecto.png" alt="Boîte de dialogue de création d'un nouveau projet"><figcaption><p>Boîte de dialogue de création d'un nouveau projet</p></figcaption></figure>
*Boîte de dialogue de création de projet : nom, dossier et système de référence.*

---

## Pas à pas

### 1. Nom du réseau

Saisissez un nom court sans espaces ni caractères spéciaux (les lettres, les chiffres et les traits de soulignement sont sécurisés). Ce nom sera le **préfixe** de tous les fichiers du projet.

- ✅ Correct : `RedUrbana`, `Red_Norte_2024`, `SectorA`
- ❌ Évitez : `Red Urbana`, `Réseau_Côte`, `Red/Norte`

### 2. Dossier du projet

Sélectionnez ou créez le dossier dans lequel tous les fichiers seront enregistrés. **Plusieurs projets peuvent coexister dans un même dossier** à condition qu'ils portent des noms différents.

### 3. Système de référence de coordonnées (CRS)

Sélectionnez le CRS approprié pour votre zone de travail. QGISRed l'attribuera à tous les fichiers SHP du projet.

> 💡 Si vous comptez importer de la géométrie depuis d'autres sources (orthophoto, cadastre, etc.), utilisez le même CRS que ces sources ou celui le plus répandu dans votre pays pour éviter les reprojections.

### 4. Options initiales d'EPANET

Dans la même boîte de dialogue, vous pouvez configurer les paramètres de base du modèle :

| Paramètre | Descriptif |
|-----------|-------------|
| **Unités de débit** | LPS (litres/seconde), GPM, CMH, etc. Détermine si le projet fonctionne dans le système SI ou US |
| **Formule de perte de tête** | Darcy-Weisbach (D-W), Hazen-Williams (H-W) ou Chezy-Manning (C-M) |

Ces paramètres peuvent être modifiés ultérieurement à partir des _Options du projet_, mais il est recommandé de les définir dès le début car ils affectent les unités affichées dans toutes les propriétés du réseau.

### 5. Catalogue des matériaux

Sélectionnez le **catalogue de matériaux** qui sera utilisé dans le projet. Ce catalogue est un fichier `.dbf` qui définit les matériaux de canalisation disponibles (nom, coefficient de rugosité initial et incrément de vieillissement).

QGISRed recherche les catalogues disponibles dans les dossiers `materials` et `global_defaults` de `%APPDATA%\QGISRed\`. Si aucun catalogue n'est installé, la liste déroulante apparaîtra vide et le projet sera créé sans matériaux prédéfinis.

> Le catalogue de matériaux permet d'estimer automatiquement la rugosité des canalisations en fonction de leur matériau et de leur âge, facilitant ainsi le calibrage du modèle hydraulique.

---

## Fichiers générés

Après confirmation de la création, QGISRed génère les fichiers suivants dans le dossier choisi et les télécharge automatiquement sur QGIS :

| Archives | Contenu |
|---------|-----------|
| `{Red}_Junctions.shp` | Nœuds de demande |
| `{Red}_Pipes.shp` | Tuyaux |
| `{Red}_Tanks.shp` | Réservoirs |
| `{Red}_Reservoirs.shp` | Bâches ou points d'alimentation |
| `{Red}_Valves.shp` | Vannes de régulation |
| `{Red}_Pumps.shp` | Bombes |
| `{Red}_Options.dbf` | Options EPANET (unités, formule, qualité...) |
| `{Red}_Title.dbf` | Métadonnées du projet (nom du scénario, notes…) |

Ils sont tous regroupés dans la légende de QGIS sous un groupe appelé **"{Red}" → "Inputs"**.

---

## Que faire ensuite

Une fois le projet créé, l'étape suivante consiste à **construire le réseau** à l'aide de la barre **Edition**. Voir la section [Édition et modélisation](../edition/README.md) pour voir comment ajouter des tuyaux, des nœuds et des éléments spéciaux.

> 💡 Si vous possédez déjà un fichier EPANET `.inp`, il est plus rapide d'utiliser [Importer un projet](abrir-importar.md#importar-desde-epanet) que de créer à partir de zéro.
