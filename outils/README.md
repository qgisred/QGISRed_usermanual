# 🔧Outils

La barre **Outils** regroupe les outils de traitement massifs : calcul automatique des propriétés hydrauliques, affectation des demandes provenant de sources externes, gestion de scénarios et analyse topologique. Contrairement aux outils d'Edition, ceux-ci agissent sur l'ensemble du réseau ou sur de larges sélections, et non élément par élément.

<figure><img src="../assets/images/herramientas/barra-tools.png" alt="Barre d'outils Outils QGISRed"><figcaption><p>Barre d'outils Outils QGISRed</p></figcaption></figure>
*Barre d'outils : propriétés hydrauliques, exigences et scénarios, analyse topologique.*

---

## Outils de la barre d'outils

### Groupe 1 — Propriétés hydrauliques

| # | Outil | Fonction |
|---|-------------|---------|
| 1 | **Calculer automatiquement les longueurs de tuyaux** | Recalculer la longueur de chaque tuyau à partir de sa géométrie |
| 2 | **Interpoler l'altitude à partir des fichiers .asc…** | Attribuer des hauteurs aux nœuds par interpolation à partir d'un MDT au format ASC |
| 3 | **Définir les coefficients de rugosité (à partir du matériau et de la date)** | Calculer la rugosité actuelle de chaque tuyau due au vieillissement |
| 4 | **Convertir les coefficients de rugosité…** | Convertir la rugosité entre les formules H-W, D-W et C-M |

### Groupe 2 — Exigences et scénarios

| # | Outil | Fonction |
|---|-------------|---------|
| 5 | **Créateur de demande nodale…** | Attribuer des demandes aux nœuds à partir de couches SHP externes (points ou polygones) |
| 6 | **Constructeur de scénarios…** | Exportez et importez les paramètres du modèle en masse pour gérer les scénarios |
| 7 | **Segments isolés…** | Identifier les vannes à fermer pour isoler une section et les zones laissées sans service |

### Groupe 3 — Analyse topologique

| # | Outil | Fonction |
|---|-------------|---------|
| 8 | **Obtenir les secteurs de demande** | Génère des secteurs de demande délimités par des débitmètres |
| 9 | **Arbre à coût minimum…** | Calculer l'arbre de coût minimum à partir d'un nœud sélectionné |

---

## Dans cette rubrique

* [Propriétés hydrauliques](proprietes-hydrauliques.md) — longueurs, altitudes, rugosité de vieillissement et conversion entre formules
* [Exigences et scénarios](demandes-et-scenarios.md) — affectation massive de demandes, gestion de scénarios et de segments isolés
* [Secteurs et arbre de demande](secteurs-arborescence.md) — sectorisation par débitmètres et arbre de coût minimum
