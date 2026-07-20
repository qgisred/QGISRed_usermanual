# ✏️Édition

La barre **Edition** contient tous les outils pour construire et modifier le réseau directement sur la carte QGIS. Travaillez sur les couches du projet actif sans avoir à ouvrir des tables attributaires ou des fichiers externes.

<figure><img src="../assets/images/edicion/barra-edition.png" alt="Barre d'outils QGISRed Edition"><figcaption><p>Barre d'outils QGISRed Edition</p></figcaption></figure>
*Bar Edition : création d'éléments, édition géométrique et topologique, propriétés et données d'exploitation.*

> Tous les boutons nécessitent un projet valide téléchargé. S'il n'y en a pas, le plugin affiche _"Aucun projet valide n'est ouvert"_.

---

## Outils de barre d'édition

### Groupe 1 — Création d'éléments

| # | Outil | Fonction |
|---|-------------|---------|
| 1 | **Ajouter un tuyau** | Dessinez des tuyaux en cliquant sur la carte ; crée automatiquement des nœuds aux extrémités |
| 2 | **Ajouter un réservoir** | Placer un Tank sur un nœud existant |
| 3 | **Ajouter un réservoir** | Placer un réservoir ou un point d'alimentation (Réservoir) sur un nœud existant |
| 4 | **Insérer la vanne dans le tuyau** | Insérez une vanne dans un tuyau existant, en le divisant |
| 5 | **Insérer la pompe dans le tuyau** | Insérez une pompe dans un tuyau existant, en le divisant |

### Groupe 2 — Édition géométrique et topologique

| # | Outil | Fonction |
|---|-------------|---------|
| 6 | **Sélectionnez plusieurs éléments** | Sélection multicouche par zone rectangulaire sur la carte |
| 7 | **Déplacer les nœuds** | Déplacez les nœuds en faisant glisser tous les éléments connectés |
| 8 | **Modifier les sommets du lien** | Ajouter, déplacer et supprimer des sommets de tuyaux intermédiaires |
| 9 | **Éléments inversés** | Inverse le sens d'orientation des tuyaux ou des raccords de service |
| 10 | **Diviser/Joindre des tuyaux** | Diviser un tuyau au point indiqué ou joindre deux sections adjacentes |
| 11 | **Fusionner/Dissoudre les jonctions** | Fusionner deux nœuds en un seul ou séparer un nœud en plusieurs |
| 12 | **Créer/Supprimer des connexions T** | Créer ou supprimer un joint en T entre un nœud et un tuyau à proximité |
| 13 | **Créer/Supprimer des croisements** | Crée ou supprime une jonction (nœud partagé) entre des tuyaux qui se croisent |
| 14 | **Déplacer les vannes/pompes** | Déplacer une vanne ou une pompe d'un tuyau à un autre |
| 15 | **Modifier le statut de l'élément** | Bascule l'état Ouvert/Fermé des tuyaux et des vannes |
| 16 | **Supprimer des éléments** | Supprimer l'élément en surbrillance ou les éléments sélectionnés |

### Groupe 3 — Propriétés et données de fonctionnement

| # | Outil | Fonction |
|---|-------------|---------|
| 17 | **Modifier les propriétés de l'élément…** | Ouvre la boîte de dialogue des propriétés de l'élément cliqué |
| 18 | **Modifier les motifs et les courbes…** | Éditeur de modèles et de courbes de demande de pompe/réservoir |
| 19 | **Modifier les contrôles…** | Editeur de commandes simples et de règles de fonctionnement |

---

## Dans cette rubrique

* [Création d'éléments](creacion.md) — tuyaux, réservoirs, réservoirs, vannes, pompes
* [Manipulation géométrique et topologique](manipulacion.md) — déplacer, diviser, inverser, croiser, supprimer
* [Propriétés des éléments](propiedades.md) — boîte de dialogue d'édition avec navigateur intégré
* [Motifs et courbes](curvas.md) — modèles de demande, courbes H-Q, efficacité et volume
* [Contrôles et règles](controles.md) — commandes simples et règles de fonctionnement automatiques
