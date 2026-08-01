# Secteurs et arbre de demande

Les deux derniers outils de la barre Outils effectuent des analyses topologiques sur le réseau : sectorisation par débitmètres et calcul de l'arbre de coût minimum à partir d'un nœud origine.

---

## Obtenir les secteurs de demande

**Barre d'outils → Obtenir les secteurs de demande**

Il génère une sectorisation du réseau basée sur la présence de **débitmètres** (débitmètres). Chaque secteur de demande est le sous-réseau alimenté par un seul débitmètre, sans croiser d'autres débitmètres.

### Différence avec les filières hydrauliques

| | Secteurs hydrauliques (Barre de débogage) | Secteurs de demande (Barra Tools) |
|-|-------------------------------------|-----------------------------------|
| **Base** | Présence de château d'eau ou de réservoir | Présence de débitmètres |
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
3. QGISRed calcule l'arbre et génère la couche `Tree` sur la carte, avec la distance accumulée depuis l'origine étiquetée sur chaque tronçon.

### Interprétation du résultat

L'arborescence résultante montre quel chemin l'eau suivrait depuis le nœud source si le réseau était purement ramifié (pas de boucles). Il est utile pour :

- Identifier les canalisations qui fonctionnent toujours dans un seul sens d'écoulement.
- Détecter les pipes redondantes dans la topologie (elles n'apparaissent pas dans l'arborescence car il y a un chemin plus court).
- Analyser la structure d'approvisionnement en conditions d'urgence avec une partie du réseau fermée.
- Planifier des schémas de sectorisation des pressions.

### ID du nœud racine

Dans la couche de nœuds générée par l'arborescence, le nœud d'origine (racine) est identifié avec la valeur **"ROOT"** dans le champ `NodeType`. Le reste des nœuds ont leur type EPANET habituel (Jonction, Tank, Reservoir...). Cela vous permet de créer des règles de symbologie spécifiques pour le nœud racine directement dans QGIS.
