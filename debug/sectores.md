# Secteurs Hydrauliques

**Barre de débogage → Vérifier les secteurs hydrauliques**

L'outil des secteurs hydrauliques scanne le réseau à l'aide d'un algorithme BFS (breadth-first search) à partir de toutes les sources d'approvisionnement et classe chaque sous-réseau connecté selon qu'il dispose ou non d'une source hydraulique (H) et qu'il ait ou non une demande (Q). Le résultat est transféré dans les couches SHP et dans un rapport CSV.

<figure><img src="../assets/images/debug/sectores-hidraulicos.png" alt="Carte des secteurs hydrauliques : zones colorées par type H-Q, H-nQ, nH-Q et nH-nQ"><figcaption><p>Carte des secteurs hydrauliques : zones colorées par type H-Q, H-nQ, nH-Q et nH-nQ</p></figcaption></figure>
*Secteurs hydrauliques : chaque couleur représente un type de classification. Les secteurs nH-Q (aucune source avec demande) apparaissent en rouge.*

---

## Classification sectorielle

L'outil attribue à chaque secteur un de ces quatre types. Voici les **balises réelles** qui apparaissent dans la couche SHP et dans le rapport CSV :

| Étiquette | Source (H) | Demande (Q) | Signification |
|----------|-----------|-------------|-------------|
| **H-Q** | ✅ Oui | ✅ Oui | Secteur fonctionnel : dispose d'une source d'approvisionnement et de nœuds avec demande. Il peut être simulé correctement. |
| **H-nQ** | ✅ Oui | ❌ Non | Secteur latent : a une source mais pas de nœuds avec une demande > 0. Il peut être simulé mais sans flux réel. |
| **nH-Q** | ❌ Non | ✅ Oui | **Secteur critique** : nœuds avec demande mais sans aucune source connectée. EPANET ne convergera pas. |
| **nH-nQ** | ❌ Non | ❌ Non | Secteur passif : ni source ni demande. Cela ne provoque pas d'erreur dans la simulation mais il est déconnecté. |

> **H** = présence d'au moins un Réservoir ou Réservoir dans le secteur.
> **Q** = présence d'au moins une jonction avec une demande de base > 0.
> **n** = négation (absence de cette condition).

Il existe également un pseudo-secteur spécial appelé **ClosedLinks** qui regroupe les canalisations avec le statut `Closed` qui se trouvent en dehors de tout secteur connecté. Cela ne compte pas dans le nombre total de secteurs du rapport.

---

## Sorties générées

L'outil produit trois sorties qui sont automatiquement ajoutées au projet :

| Sortie | Tapez | Contenu |
|--------|------|-----------|
| `HydraulicSectors` | Couche SHP | Géométrie de tous les éléments colorés par type de secteur |
| `HydraulicSectors_IsolatedDemands` | Couche SHP | Nœuds et connexions de type **nH-Q** avec leur demande isolée |
| `{Red}_HydraulicSectors_Report.csv` | CSV | Tableau avec identifiant de secteur, nombre d'éléments et classification |

Le CSV a le format :
```
SectorID; NumElements; Classification
S1; 1 243; H-Q
S2; 47; H-nQ
S3; 12; nH-Q
S4; 3; nH-nQ
```

---

## Comment interpréter chaque type

### H-Q — Fonctionnel

Statut correct. Chaque secteur qui va être simulé doit être H-Q. Un réseau correctement construit aura un seul grand secteur H-Q (ou plusieurs s'il existe une véritable sectorisation hydraulique avec des vannes fermées entre eux).

### H-nQ — Latent

Il existe une source connectée mais tous les nœuds de ce secteur ont une demande = 0. Causes courantes :

- Zone réseau importée sans encore de données de demande attribuées.
- Contourner ou réserver une branche sans consommateurs (peut être correct de par sa conception).

Dans le premier cas, les demandes doivent être assignées avant que la simulation ne soit réaliste.

### nH-Q — Critique (le plus important à corriger)

C'est le seul type qui empêche la simulation. Il existe des nœuds avec une demande qui n'ont aucun chemin vers un réservoir ou un réservoir.

**Causes fréquentes :**
- Il manque une conduite qui devrait relier ce secteur au réseau principal.
- Il y a une vanne fermée entre ce secteur et la source (fonctionnement correct, mais il faut la modéliser ainsi volontairement).
- Erreur topologique : le tuyau de connexion existe visuellement mais il y a une rupture de connectivité — détectée avec **Vérifier la connectivité**.

La couche `HydraulicSectors_IsolatedDemands` montre exactement quels nœuds et connexions ont une demande sans source, ce qui facilite la localisation du problème.

### nH-nQ — Passif

Fragments déconnectés sans consommation. Il s’agit généralement de restes importés ou de branches de projet incomplètes. Ils ne provoquent pas d’erreur de simulation, mais salissent le modèle. S'ils ne font pas partie de la mise en page, supprimez-les avec **Supprimer les éléments** ou l'option **Supprimer les sous-zones isolées** de **Vérifier la connectivité**.

---

## Flux de travail recommandé

Avant la première simulation ou après l'importation d'un nouveau réseau :

1. **Vérifier && valider les données** : garantit que la topologie et les attributs de base sont cohérents.
2. **Supprimer les éléments qui se chevauchent** — élimine les nœuds et les tuyaux en double qui pourraient générer des secteurs artificiels.
3. **Vérifier la connectivité** — identifie visuellement les zones isolées et, s'il y a des « indésirables » topologiques, utilise **Supprimer les sous-zones isolées**.
4. **Vérifiez les secteurs hydrauliques** — obtenez le classement complet. Notez le nombre de secteurs nH-Q.
5. **Corriger les secteurs nH-Q** — ajoutez des tuyaux ou corrigez les erreurs topologiques jusqu'à ce qu'elles disparaissent.
6. Réexécutez **Vérifiez les secteurs hydrauliques** — confirmez que tous les secteurs sont H-Q, H-nQ ou nH-nQ (pas de nH-Q).

> Ce n'est que lorsqu'il n'y a pas de secteurs **nH-Q** que la simulation EPANET peut s'exécuter sans erreurs de convergence.
