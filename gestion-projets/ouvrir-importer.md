# Ouvrir et importer des projets

QGISRed propose trois façons de commencer à travailler avec un réseau existant :

| Options | Quand l'utiliser |
|--------|---------------|
| **Ouvrir le projet** | Le projet a déjà été créé avec QGISRed et ses fichiers SHP sont sur le disque |
| **Importer un projet** | Vous disposez d'un fichier EPANET `.inp`, de SHP externes sans structure QGISRed, ou d'un ZIP préalablement exporté avec QGISRed |
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

> 💡 Le moyen le plus rapide d'ouvrir un projet connu est de **double-cliquer** sur le [Chef de projet](gestionnaire-projets.md). L'option « Ouvrir le projet » est destinée aux projets qui n'apparaissent pas dans cette liste.

---

## Importer un projet

**Barre générale → Importer un projet**

Convertissez des données externes en un projet QGISRed ou récupérez une donnée précédemment exportée. Prend en charge trois formats d'entrée :

### Importer depuis EPANET (`.inp`) {#import-from-epanet}

Le cas le plus courant : vous disposez d’un modèle EPANET existant et vous souhaitez travailler avec celui-ci dans QGISRed.

<figure><img src="../assets/images/general/importar-inp.png" alt="Boîte de dialogue d'importation de fichier EPANET INP"><figcaption><p>Boîte de dialogue d'importation de fichier EPANET INP</p></figcaption></figure>
*Boîte de dialogue Importer : sélection du fichier .inp, du nom du réseau et du dossier de destination.*

1. Sélectionnez le fichier `.inp`.
2. Indique le **nom du réseau** que portera le projet QGISRed (il peut être différent du nom interne de l'INP).
3. Choisissez le **dossier de destination** où les SHP seront créés.
4. QGISRed convertit tous les éléments (nœuds, tuyaux, vannes, pompes, courbes, modulations, contrôles...) en structure SHP+DBF.

> ⚠️ Les coordonnées de `.inp` doivent être dans le même CRS que vous utiliserez dans QGISRed. Le plugin ne reprojete pas lors de l'importation.

**Ce qui est importé :**
- Tous les éléments du réseau (jonctions, canalisations, réservoirs, bâches, vannes, pompes)
- Courbes (H-Q, rendement, volume, perte de charge)
- Modulations de demande
- Contrôles et règles simples
- Options de simulation (unités, formule, temps, énergie, qualité)
- Demandes multiples par nœud


### Importer depuis des SHP externes

Si vous disposez de couches SHP avec la géométrie du réseau mais sans la structure interne de QGISRed, l'importateur permet de mapper les colonnes d'attributs de chaque couche aux champs attendus par le plugin.

Pour chaque type d'élément, vous pouvez sélectionner la couche SHP correspondante et attribuer ses champs aux attributs du modèle. Les champs automatiquement reconnus (si le nom correspond) sont présélectionnés :

**Tuyaux** — champs mappables : ID, Longueur, Diamètre, Rugosité, Coeff. pertes, **Matériau**, Date d'installation, Etat initial, Coeff. réaction de masse, Coef. réaction du mur, Tag, Description.

**Services** — champs mappables : ID, Longueur, Diamètre, Rugosité, **Matériau**, Demande de base, Modulation, Actif, Date d'installation, Étiquette, Description.

Les autres éléments (vannes, pompes, réservoirs, bâches, nœuds, vannes d'isolement, compteurs) possèdent leurs propres ensembles de champs mappables.

Lorsque l'import crée un nouveau projet, le **catalogue des matériaux** (comme lors de la création d'un projet à partir de zéro) et les paramètres de base EPANET (unités et formule de perte de charge) sont également demandés. S'ils sont importés sur un projet existant, ces paramètres sont ignorés.

> 💡 Le champ **Matériau** des canalisations et raccords est croisé avec le catalogue matériaux du projet pour estimer automatiquement la rugosité en fonction de l'âge de la canalisation.

### Importer un projet QGISRed exporté (ZIP) {#import-zip}

Récupère un projet packagé avec le bouton **Exporter** de [Chef de projet](gestionnaire-projets.md) — voir [Enregistrer, exporter et fermer le projet](../projet-actif/enregistrer-exporter-fermer.md). Il reconnaît également les ZIP générés par les versions précédentes du plugin, même s'ils ne disposent pas du manifeste interne des exports en cours.

<figure><img src="../assets/images/general/importar-proyecto-qgisred.png" alt="Onglet QGISRed project de la boîte de dialogue d'import"><figcaption><p>Onglet QGISRed project de la boîte de dialogue d'import</p></figcaption></figure>

1. Dans l'onglet **Projet QGISRed**, appuyez sur le bouton **...** à côté de **Fichier ZIP :** et sélectionnez le fichier `.zip`.
2. QGISRed inspecte le contenu ZIP sans l'extraire pour l'instant et affiche un résumé sous le champ :
- **Projet :** nom du réseau contenant le ZIP (remplace tout nom que vous avez saisi auparavant ; le champ du nom du projet est masqué dans cet onglet).
- Si le ZIP inclut la carte QGIS, indiquer le fichier `.qgz`/`.qgs` ; S'il n'est pas inclus, il avertit que seules les données seront importées.
- Si le ZIP comprend des données complémentaires (cartographie de fond, MDT, etc.), indiquer le nombre d'éléments et leur taille totale.
3. Si le ZIP comprend des données complémentaires, la case **Importer les données complémentaires incluses dans le fichier ZIP** apparaît, cochée par défaut. Décochez-la si vous ne souhaitez pas les amener.
4. La case à cocher **Créer automatiquement un sous-dossier pour ce projet** détermine si le projet est placé dans un sous-dossier portant le nom du réseau dans le dossier de destination :
- Si le ZIP contient déjà son propre dossier de projet (il a été exporté avec les données de support dans des dossiers frères), QGISRed décoche et désactive automatiquement cette case — l'imbriquer dans un autre dossier briserait les chemins relatifs vers ces données.
- Sinon, vous pouvez librement la cocher ou la décocher.
5. Appuyez sur **Importer depuis le projet**.

Si le ZIP n'est pas un projet QGISRed valide, QGISRed l'indique sans rien importer :

| Situation | Messages |
|-----------|---------|
| Le ZIP ne contient pas de projet QGISRed reconnaissable | _"Le fichier ZIP ne contient pas de projet QGISRed valide"_ |
| Le ZIP a été généré avec une version de QGISRed plus récente que celle installée | _"Ce fichier ZIP a été créé avec une version plus récente de QGISRed. Veuillez mettre à jour le plugin."_ |
| Le ZIP contient des chemins de fichiers dangereux | _"Le fichier ZIP contient des chemins de fichiers dangereux et ne sera pas importé."_ |

> ⚠️ Si un projet du même nom (ou des fichiers du même nom) existe déjà dans le dossier de destination, QGISRed demande confirmation avant de les écraser.

> 💡 Si le ZIP inclut la carte QGIS mais que vous décidez de ne pas importer les données complémentaires, QGISRed vous prévient que certaines couches d'arrière-plan ne seront pas disponibles et laisse QGIS vous demander de les localiser.

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
