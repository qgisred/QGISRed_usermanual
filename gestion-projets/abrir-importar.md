# Ouvrir et importer des projets

QGISRed propose trois façons de commencer à travailler avec un réseau existant :

| Options | Quand l'utiliser |
|--------|---------------|
| **Ouvrir le projet** | Le projet a déjà été créé avec QGISRed et ses fichiers SHP sont sur le disque |
| **Importer un projet** | Vous disposez d'un fichier EPANET `.inp` ou de SHP externes sans structure QGISRed |
| **Ajouter des données par importation** | Vous avez déjà un projet ouvert et souhaitez intégrer des données supplémentaires |

---

## Ouvrir le projet

**Barre générale → Ouvrir le projet**

Ouvre un projet QGISRed existant (précédemment créé avec le plugin) qui n'apparaît pas dans le Gestionnaire de projets, ou qui a été déplacé d'un dossier.

<figure><img src="../assets/images/general/abrir-proyecto.png" alt="Boîte de dialogue d'ouverture du projet"><figcaption><p>Boîte de dialogue d'ouverture du projet</p></figcaption></figure>
*Boîte de dialogue d'ouverture : saisissez le nom du réseau et sélectionnez le dossier.*

### Processus

1. Saisissez le **nom du réseau** exactement tel qu'il apparaît dans le préfixe des fichiers SHP (sans extension).
2. Sélectionnez le **dossier** où se trouvent les fichiers.
3. QGISRed vérifie que `{nombre}_Pipes.shp` existe dans ce dossier et charge toutes les couches du projet.

### Que se passe-t-il lorsque vous ouvrez

- Le groupe de couches **Inputs** est chargé avec les 6 SHP de base plus toutes les couches auxiliaires (requêtes multiples, sources, etc.).
- Si le projet comporte des résultats de simulations précédentes, le groupe **Résultats** est également chargé.
- Les options du projet (`_Options.dbf`) sont lues et l'indicateur d'unités dans la barre principale est mis à jour.
- Si les styles visuels (QML) ont changé par rapport à la version du plugin avec lequel ils ont été enregistrés, ils sont automatiquement mis à jour.

> 💡 Le moyen le plus rapide d'ouvrir un projet connu est de **double-cliquer** sur le [Chef de projet](gestor-proyectos.md). L'option « Ouvrir le projet » est destinée aux projets qui n'apparaissent pas dans cette liste.

---

## Importer un projet

**Barre générale → Importer un projet**

Convertit les données externes en un projet QGISRed. Prend en charge deux formats d'entrée :

### Importer depuis EPANET (`.inp`) {#import-from-epanet}

Le cas le plus courant : vous disposez d’un modèle EPANET existant et vous souhaitez travailler avec celui-ci dans QGISRed.

<figure><img src="../assets/images/general/importar-inp.png" alt="Boîte de dialogue d'importation de fichier EPANET INP"><figcaption><p>Boîte de dialogue d'importation de fichier EPANET INP</p></figcaption></figure>
*Boîte de dialogue Importer : sélection du fichier .inp, du nom du réseau et du dossier de destination.*

1. Sélectionnez le fichier `.inp`.
2. Indique le **nom du réseau** que portera le projet QGISRed (il peut être différent du nom interne de l'INP).
3. Choisissez le **dossier de destination** où les SHP seront créés.
4. QGISRed convertit tous les éléments (nœuds, tuyaux, vannes, pompes, courbes, modèles, contrôles...) en structure SHP+DBF.

> ⚠️ Les coordonnées de `.inp` doivent être dans le même CRS que vous utiliserez dans QGISRed. Le plugin ne reprojete pas lors de l'importation.

**Ce qui est importé :**
- Tous les éléments du réseau (jonctions, canalisations, réservoirs, vannes, pompes)
- Courbes (H-Q, rendement, volume, perte de charge)
- Modèles de demande
- Contrôles et règles simples
- Options de simulation (unités, formule, temps, énergie, qualité)
- Demandes multiples par nœud


### Importer depuis des SHP externes

Si vous disposez de couches SHP avec la géométrie du réseau mais sans la structure interne de QGISRed, l'importateur permet de mapper les colonnes d'attributs de chaque couche aux champs attendus par le plugin.

Pour chaque type d'élément, vous pouvez sélectionner la couche SHP correspondante et attribuer ses champs aux attributs du modèle. Les champs automatiquement reconnus (si le nom correspond) sont présélectionnés :

**Tuyaux** — champs mappables : ID, Longueur, Diamètre, Rugosité, Coeff. pertes, **Matériau**, Date d'installation, Etat initial, Coeff. réaction de masse, Coef. réaction du mur, Tag, Description.

**Services** — champs mappables : ID, Longueur, Diamètre, Rugosité, **Matériau**, Demande de base, Modèle, Actif, Date d'installation, Étiquette, Description.

Les autres éléments (vannes, pompes, réservoirs, réservoirs, nœuds, vannes d'isolement, compteurs) possèdent leurs propres ensembles de champs mappables.

Lorsque l'import crée un nouveau projet, le **catalogue des matériaux** (comme lors de la création d'un projet à partir de zéro) et les paramètres de base EPANET (unités et formule de perte de charge) sont également demandés. S'ils sont importés sur un projet existant, ces paramètres sont ignorés.

> 💡 Le champ **Matériau** des canalisations et raccords est croisé avec le catalogue matériaux du projet pour estimer automatiquement la rugosité en fonction de l'âge de la canalisation.

---

## Ajouter des données par import

**Barre de projet → Ajouter des données par importation**

Disponible uniquement lorsqu'un projet est déjà ouvert. Il permet d'enrichir le projet avec des données supplémentaires sans fermer ce qui est chargé.

Cas d'utilisation typiques :
- Intégrer une nouvelle zone réseau conçue dans un `.inp` séparé.
- Ajouter des demandes pour une nouvelle base de données.
- Intégrer les données d'un secteur importées d'un autre système.

Le processus est le même que l'importation, mais les éléments importés sont **ajoutés** au projet existant au lieu d'en créer un nouveau. QGISRed vérifie qu'il n'y a pas de conflits d'ID avant d'incorporer les données.

---

## Considérations lors du changement d'équipement

Si vous copiez le dossier du projet sur un autre ordinateur :

1. Utilisez **Télécharger** dans le Gestionnaire de projets pour l'ajouter à l'historique local.
2. Si le projet a un `.qgz` enregistré, ouvrez-le normalement depuis QGIS — QGISRed le reconnaîtra automatiquement.
3. Si le `.qgz` n'est pas là ou si les chemins ont changé, utilisez **Open Project** pour le charger directement depuis les SHP.
