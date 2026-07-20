# Flux de travail typique

C'est le chemin habituel pour construire, vérifier et simuler un réseau de distribution avec QGISRed.

---

## Étape 1 — Créer ou ouvrir le projet

Utilisez la barre **Général** pour commencer :

- **Nouveau projet à partir de zéro** : _Créer un projet_ → choisissez le nom, le dossier et le système de référence. QGISRed génère automatiquement les 6 SHP de base (Jonctions, Tuyaux, Réservoirs, Réservoirs, Vannes, Pompes).
- **Projet existant** : _Chef de projet_ → double-cliquez sur le projet dans la liste récente.
- **À partir d'un fichier EPANET** : _Importer un projet_ → sélectionner le `.inp`. QGISRed le convertit en SHP et l'ouvre.

## Étape 2 — Configurer les options du projet

Dans la barre **Projet**, accédez aux _Options du projet_ pour définir :
- **Unités de débit** (LPS, GPM, CMH…)
- **Formule de perte de charge** (D-W, H-W, C-M)
- **Modèle de qualité** (Aucun, Chlore, Âge, Traceur)

L'indicateur sur la barre principale (`LPS | D-W`) reflète toujours les valeurs actives.

## Étape 3 — Construire le réseau

Activez la barre **Edition** et dessinez le réseau sur la carte :

1. Commencez par les **tuyaux** — les nœuds extrêmes se créent d'eux-mêmes.
2. Ajoutez des **réservoirs et réservoirs** en cliquant sur les nœuds existants.
3. Insérez **vannes et pompes** en cliquant sur un tuyau.
4. Editez les **propriétés** de chaque élément (diamètre, rugosité, dimension, demande...).

> 💡 Vous pouvez importer la géométrie existante (infrastructure SHP, orthophoto d'arrière-plan) et tracer le réseau dessus.

## Étape 4 — Vérifier la qualité du modèle

Avant de simuler, utilisez la barre **Debug** :

1. **Consolider et examiner les données** : détecte les attributs incomplets ou incohérents.
2. **Vérifier la connectivité** — identifie les zones isolées sans source de pression.
3. **Secteurs hydrauliques** — vérifiez l'alimentation électrique de chaque secteur.

Corrigez tout problème noté dans le rapport d'incident avant de continuer.

## Étape 5 — Préparer les données de demande

Depuis la barre **Outils** :

- **Interpoler les élévations** si les nœuds n'ont pas d'élévations attribuées.
- **Attribuer la rugosité** en fonction du matériau et de la date d'installation.
- **Demand manager** pour répartir la consommation.

## Étape 6 — Simuler

Depuis la barre **Analyse** :

1. _Options d'analyse_ — vérifiez la durée et le pas de temps.
2. _Exécuter le modèle_ — la simulation peut prendre d'une seconde à plusieurs minutes selon la taille du réseau.
3. Une fois terminé, QGISRed charge automatiquement les couches de résultats et ouvre la **Results Viewer**.

## Étape 7 — Explorer les résultats

Dans le panneau latéral de la visionneuse de résultats :

- Sélectionnez quelle **variable** afficher dans les nœuds (Pression, Demande, Qualité) et dans les tuyaux (Débit, Vitesse, Perte unitaire...).
- Déplacez le **curseur temporel** pour voir l'évolution tout au long de la période simulée.
- Activez **Map Notices** pour lire les valeurs lorsque vous passez la souris sur n'importe quel élément.
- Utilisez **Time Series** pour représenter graphiquement l'évolution d'un point spécifique.

## Étape 8 — Enregistrer

- _Save Map_ enregistre le projet QGIS (`.qgz`) avec les couches et styles visibles.
- _Backup_ crée un instantané de tous les fichiers SHP dans un sous-dossier daté.

---

> ❗ **IMPORTANT** : QGISRed ne modifie pas les couches lorsqu'elles sont en **Mode Édition** de QGIS. Assurez-vous de valider (`Ctrl+S` sur la couche) ou d'annuler vos modifications avant d'utiliser des outils de plugin.
