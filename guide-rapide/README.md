# 🧭 L'interface QGISRed

QGISRed s'intègre à QGIS sous la forme d'un ensemble de **barres d'outils spécialisées**. Chaque barre regroupe les outils d'une étape du workflow : gestion de projet, édition du réseau, vérification, simulation, etc.

<figure><img src="../assets/images/guia-rapida/barra-principal.png" alt="Barre principale de QGISRed avec les boutons déroulants de chaque barre d'outils"><figcaption><p>Barre principale de QGISRed avec les boutons déroulants de chaque barre d'outils</p></figcaption></figure>
*Barre principale de QGISRed : chaque bouton déroulant active/désactive une barre d'outils.*

---

## Le bar principal

Lorsque vous installez le plugin, une **barre principale** apparaît dans QGIS avec un bouton déroulant pour chaque barre d'outils secondaire. Cliquer sur l'un de ces boutons affiche ou masque la barre correspondante. De plus, le menu déroulant de chaque bouton répertorie directement toutes les actions de cette barre d'outils, permettant de les exécuter sans que la barre soit visible.

À droite de la barre principale se trouve un **indicateur d'unités** (par exemple `LPS | D-W`) qui affiche les unités de débit et la formule de perte de charge pour le projet actif.

## Barres d'outils

QGISRed comprend **8 barres d'outils** organisées par zone de travail :

| Barre | Fonction principale |
|-------|------------------|
| **Général** | Créer, ouvrir et importer des projets |
| **Projet** | Configuration, couches et sauvegarde |
| **Édition** | Dessiner et éditer le réseau hydraulique |
| **Débogage** | Vérifier la qualité et la cohérence du modèle |
| **Outils** | Outils de calcul et de gestion de données |
| **Requêtes** | Consulter, filtrer et visualiser les informations |
| **Analyse** | Simuler et explorer les résultats |
| **Jumeau numérique** | Raccordements, vannes d'arrêt et capteurs |

> 💡 **CONSEIL** : activez uniquement les barres dont vous avez besoin à un moment donné pour garder l'espace de travail bien rangé. L'état de visibilité de chaque barre est automatiquement enregistré entre les sessions.

## Le projet QGISRed

Toutes les données réseau sont stockées dans un dossier de projet sous forme de fichiers **SHP + DBF**. Le nom du réseau (par exemple `MiRed`) est le préfixe commun de tous ces fichiers (`MiRed_Pipes.shp`, `MiRed_Junctions.shp`, etc.).

QGISRed ne fonctionne pas avec le fichier QGIS `.qgz` comme source de vérité : la source de vérité est toujours les fichiers SHP du projet. Le `.qgz` est facultatif et permet de sauvegarder l'apparence visuelle (styles, calques visibles, etc.).

---

Consultez [Résumé de la barre d'outils](barres-outils.md) pour voir ce que fait chaque outil, ou passez directement à [Flux de travail typique](flux-de-travail.md) si vous souhaitez commencer le plus tôt possible.
