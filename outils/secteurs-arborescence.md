# Secteurs et arbre de demande

Les deux derniers outils de la barre Outils effectuent des analyses topologiques sur le réseau : sectorisation par débitmètres et calcul de l'arbre de coût minimum à partir d'un nœud origine.

---

## Obtenir les secteurs de demande

**Barre d'outils → Obtenir les secteurs de demande** (anciennement « Constructeur de secteurs de demande… »)

Il génère une sectorisation du réseau basée sur la présence de **débitmètres** (débitmètres). Chaque secteur de demande est le sous-réseau alimenté par un seul débitmètre, sans croiser d'autres débitmètres.

### Différence avec les filières hydrauliques

| | Secteurs hydrauliques (Barre de débogage) | Secteurs de demande (Barra Tools) |
|-|-------------------------------------|-----------------------------------|
| **Base** | Présence de réservoir ou de bâche | Présence de débitmètres |
| **Question** | D'où vient l'eau ? | Que mesure chaque débitmètre ? |
| **Classement** | H-Q / H-nQ / nH-Q / nH-nQ | Aucun type, uniquement coloré par secteur |
| **Utiliser** | Diagnostic avant simulation | Bilan hydrique par secteur |

### Résultat

L'outil génère la couche `DemandSectors` sur la carte, avec chaque secteur dans une couleur différente. Si le réseau ne dispose pas de débitmètres chargés, le résultat est un seul secteur qui s'étend sur l'ensemble du réseau.

Aucune configuration requise : se lance directement sans dialogue.

---

## Arbre à coût minimum…

**Barre d'outils → Arbre de coût minimum…**

Calcule l'**arbre couvrant le coût minimum** du réseau à partir d'un nœud sélectionné. Il montre le chemin le plus efficace sur le plan hydraulique (moindre résistance cumulée) depuis ce nœud vers tous les autres points accessibles du réseau.

### Processus

1. Activez l'outil.
2. Cliquez sur le nœud source (par exemple, une source d'approvisionnement ou un point de livraison d'eau élevée).
3. QGISRed propose un nom pour l'arbre (par défaut, l'ID du nœud suivi de la fonction de coût choisie, par ex. `J5_R`) ; vous pouvez le modifier avant de calculer.
4. QGISRed calcule l'arbre et génère son propre groupe **Tree_&lt;nom&gt;** sur la carte, avec la distance accumulée depuis l'origine étiquetée sur chaque tronçon.

<figure><img src="../assets/images/tools/minimum-cost-tree-dialog.png" alt="Dialogue Minimum Cost Tree avec le nœud d'origine déjà sélectionné"><figcaption><p>Dialogue Minimum Cost Tree avec le nœud d'origine déjà sélectionné</p></figcaption></figure>

> 📝 Vous pouvez avoir **plusieurs arbres ouverts à la fois**, chacun avec son propre nom, groupe et paire de couches (nœuds et tronçons) indépendants — ils ne se remplacent pas entre eux. La boîte de dialogue de l'outil elle-même liste les arbres déjà calculés pour le projet et permet de supprimer individuellement n'importe lequel d'entre eux, sans affecter les autres.

### Interprétation du résultat

<figure><img src="../assets/images/tools/minimum-cost-tree-result.png" alt="Arbre à coût minimal calculé, avec la distance cumulée étiquetée sur chaque tronçon"><figcaption><p>Arbre à coût minimal calculé, avec la distance cumulée étiquetée sur chaque tronçon</p></figcaption></figure>

L'arborescence résultante montre quel chemin l'eau suivrait depuis le nœud source si le réseau était purement ramifié (pas de boucles). Il est utile pour :

- Identifier les canalisations qui fonctionnent toujours dans un seul sens d'écoulement.
- Détecter les pipes redondantes dans la topologie (elles n'apparaissent pas dans l'arborescence car il y a un chemin plus court).
- Analyser la structure d'approvisionnement en conditions d'urgence avec une partie du réseau fermée.
- Planifier des schémas de sectorisation des pressions.

### ID du nœud racine

Dans la couche de nœuds générée par l'arborescence, le nœud d'origine (racine) est identifié avec la valeur **"ROOT"** dans le champ `NodeType`. Le reste des nœuds ont leur type EPANET habituel (Jonction, Tank, Reservoir...). Cela vous permet de créer des règles de symbologie spécifiques pour le nœud racine directement dans QGIS.

Le nœud racine conserve également, uniquement dans sa propre ligne, les paramètres avec lesquels l'arbre a été généré : le champ `CostFn` indique la fonction de coût utilisée (résistance hydraulique, diamètre ou longueur) et `IgnClosed` si les tuyaux fermés ont été ignorés. Utile pour vérifier comment un arbre déjà généré a été calculé sans avoir à répéter le processus.
