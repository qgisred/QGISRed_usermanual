# ✅ Débogage

La barre **Debug** regroupe les outils de vérification et de débogage du modèle. Son objectif est de détecter et corriger les erreurs topologiques, les incohérences d'attributs et les problèmes de connectivité **avant de lancer la simulation**, évitant ainsi les erreurs difficiles à diagnostiquer dans EPANET.

<figure><img src="../assets/images/debug/barra-debug.png" alt="Barre d'outils de débogage QGISRed"><figcaption><p>Barre d'outils de débogage QGISRed</p></figcaption></figure>
*Barre de débogage : validation des données, débogage topologique, revue des attributs et des secteurs hydrauliques.*

---

## Outils de la barre de débogage

### Groupe 1 — Topologie et cohérence

| # | Outil | Fonction |
|---|-------------|---------|
| 1 | **Vérifier et valider les données** | Valide toutes les données du modèle et signale les éléments comportant des erreurs |
| 2 | **Supprimer les éléments qui se chevauchent** | Détecter et supprimer les nœuds ou tuyaux en double dans la même position |
| 3 | **Simplifier les sommets des liens** | Élimine les sommets intermédiaires alignés en sections droites |
| 4 | **Rejoignez des tuyaux consécutifs** | Fusionner les tuyaux adjacents de diamètre, matériau et année identiques |
| 5 | **Créer des connexions T** | Détecte les nœuds d'extrémité sur les tuyaux et crée la jointure topologique |
| 6 | **Vérifiez la connectivité** | Identifie les zones isolées des sources d'approvisionnement |
| — | *Supprimer les sous-zones isolées* | (Sous-option) Élimine les sous-zones avec moins de canalisations que le seuil défini |

### Groupe 2 — Vérification des attributs

| # | Outil | Fonction |
|---|-------------|---------|
| 7 | **Vérifiez les longueurs de tuyaux** | Comparez les longueurs des attributs par rapport à la géométrie et soulignez les différences |
| 8 | **Vérifier les diamètres** | Détecte les diamètres en dehors de la plage habituelle du projet |
| 9 | **Vérifiez les matériaux des tuyaux** | Détecte les matériaux non définis dans la table des matériaux du projet |
| 10 | **Vérifiez les dates d'installation des tuyaux** | Détecter les dates d'installation mal formatées ou incohérentes |

### Groupe 3 — Secteurs hydrauliques

| # | Outil | Fonction |
|---|-------------|---------|
| 11 | **Vérifiez les secteurs hydrauliques** | Classe les zones du réseau selon leur capacité d'approvisionnement (types A à D) |

---

## Dans cette rubrique

* [Topologie et connectivité](topologie.md) — validation, chevauchement, simplification, jointure, connexions en T, connectivité
* [Vérification des attributs](attributs.md) — longueurs, diamètres, matériaux, dates d'installation
* [Secteurs hydrauliques](secteurs-hydrauliques.md) — classification des secteurs de type A, B, C et D
