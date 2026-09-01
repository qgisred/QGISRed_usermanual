# Cartes thématiques

**Barre de requêtes → Cartes thématiques…**

Ouvre la boîte de dialogue **Cartes thématiques**, qui génère des couches qui colorent les canalisations et les nœuds par intervalles d'un attribut hydraulique. Contrairement aux autres boîtes de dialogue QGISRed, vous n'avez pas besoin de choisir un « champ et de confirmer » : chaque attribut disponible a sa propre case, et vous pouvez en cocher autant que vous le souhaitez à la fois — chacun génère sa propre couche, et ils vivent tous simultanément sur la carte.

<!-- TODO : capture en attente — Boîte de dialogue Cartes thématiques avec boîtes Tuyaux et Nœuds -->

---

## Éléments actifs : tuyaux et nœuds

Dans la version actuelle, **Les cartes thématiques fonctionnent sur les couches Canalisations et Jonctions**. Les options pour les autres types d'éléments (vannes, pompes, cuves, réservoirs) sont présentes dans l'interface mais sont automatiquement masquées car pas encore implémentées. Les groupes **Connexions de service**, **Vannes d'isolement** et **Compteurs** sont visibles, mais leur seule case à cocher ("Temporaire") n'est pas encore opérationnelle — ne la cochez pas.

---

## Processus

1. Ouvrez les **Cartes thématiques** depuis la barre de requêtes.
2. Cochez les cases des attributs que vous souhaitez représenter (vous pouvez cocher plusieurs tuyaux et nœuds en même temps).
3. Appuyez sur **Accepter**. QGISRed crée une couche pour chaque case cochée, dans le groupe **Requêtes → Cartes thématiques** du panneau Calques QGIS.
4. Pour supprimer une carte déjà générée, rouvrez la boîte de dialogue, décochez sa case et appuyez sur **Accepter** — QGISRed supprime cette couche spécifique sans toucher au reste. Les cases sur les cartes déjà générées apparaissent pré-marquées.

> 💡 Vous pouvez ouvrir plusieurs cartes thématiques à la fois (par exemple, matériau de canalisation et année d'installation ainsi que demande de base de nœud) — chacune est une couche distincte, elles ne se remplacent pas comme c'était le cas auparavant.

---

## Champs disponibles pour les tuyaux

| Champ | Descriptif |
|-------|-------------|
| `Diameter` | Diamètre du tuyau |
| `Length` | Longueur |
| `Material` | Matériau du tuyau, coloré avec la palette fixe de QGISRed (voir tableau ci-dessous) |
| `Roughness` | Coefficient de rugosité — les classes et le fichier de style dépendent de la **formule de perte de pression** active dans le projet (Hazen-Williams, Colebrook-White ou Darcy-Weisbach) |
| `Age` | Âge, calculé à partir de l'année d'installation ; les classes sont étiquetées avec le suffixe « ans » |
| `Installation Year` | Année d'installation |

> Les cartes **Âge** et **Année d'installation** ajoutent trois colonnes ensemble à la table attributaire de la couche : la date d'installation brute (`InstalDate`), l'année extraite (`InstYear`) et l'âge calculé (`Age`) — les voir toutes en même temps est utile même si vous n'avez marqué qu'une des deux cartes.

---

## Champs disponibles pour les nœuds

| Champ | Descriptif |
|-------|-------------|
| `Elevation` | Niveau nœud. Les classes sont automatiquement calculées à partir des valeurs réelles du projet (il n'y a pas de plages standard) — la légende montre les coupes avec l'unité de longueur du projet (par exemple "< 120 m", "120 < 180 m", ">= 180 m"). |
| `Total Base Demand` | Demande de base totale du nœud. Les cercles sont **dimensionnés proportionnellement** à la demande (non linéaire, afin que les très grandes valeurs ne dominent pas visuellement la carte), en classes également calculées à partir des données réelles, étiquetées sur l'unité de flux active du projet. Si le nœud a plusieurs catégories de demande (voir [Exigences et scénarios](../outils/demandes-et-scenarios.md)), la couche reflète la somme globale ; les nœuds avec une demande nulle ne sont pas affichés. |

---

## Palette de matériaux

La carte **Matériau** colore chaque tuyau en fonction de la valeur de son champ `Material`, en le comparant (insensible à la casse) avec l'abréviation ou le nom dans ce tableau fixe — un matériau qui n'apparaît pas ici reçoit une couleur aléatoire à la place :

| Abrégé | Matériaux | Abrégé | Matériaux |
|--------|----------|--------|----------|
| FG | Fonte grise | Pb | Plomb |
| FD | Coulée ductile | PVC | Chlorure de polyvinyle |
| AS | Acier | PE | Polyéthylène |
| ACIER INOXYDABLE | Acier inoxydable | PVC-BO | PVC orienté |
| FC | Fibro-ciment | PVC-R | PVC rigide |
| AGal | Acier galvanisé | Cu | Cuivre |
| CCHC | Béton avec gaine en tôle | PE-AD | Polyéthylène haute densité |
| CCSS | Béton sans gaine en tôle | PE-BD | Polyéthylène basse densité |
| HAr | Béton armé | PE-MD | Polyéthylène densité moyenne |
| HPr | Béton précontraint | PRV | Polyester renforcé de fibre de verre |

> Cette table de couleurs s'applique uniquement au style **par défaut** fourni avec QGISRed. Si vous enregistrez votre propre légende de matériaux depuis l'éditeur de légende (voir [Présentation et gestion des couches](../projet-actif/couches-et-legende.md)), vos couleurs ont priorité sur cette palette lorsque vous régénérez la carte.

---

## Avis de carte obsolète

Si vous modifiez les **unités**, la **formule de perte de charge** ou les **unités de débit** du projet après avoir généré une carte thématique qui en dépend (Diamètre, Longueur, Rugosité, Demande de base...), QGISRed marque cette couche avec une icône d'avertissement ⚠ dans le panneau des couches — la même icône qu'il utilise déjà pour avertir des résultats de simulation obsolètes.

- Passez la souris sur l'icône pour voir la raison.
- Cliquez sur l'icône pour reconstruire cette couche avec la configuration actuelle, sans avoir à rouvrir la boîte de dialogue.

---

## Résultat sur la carte

Chaque case cochée génère sa propre couche (par exemple `Pipe Materials`, `Junction Elevations`) au sein du groupe **Requêtes → Cartes thématiques**. Les couches sont en lecture seule et se mettent à jour automatiquement lorsque vous modifiez le canal ou le nœud source (il n'est pas nécessaire de régénérer la carte manuellement après une modification spécifique) — la légende de chacune montre également le nombre d'éléments de chaque classe.

Si vous cochez et confirmez à nouveau une case déjà générée, QGISRed remplace cette couche spécifique par la nouvelle configuration, sans toucher au reste des cartes actives.

---

## Notes d'utilisation

- La génération des cartes thématiques ne modifie aucune donnée du modèle ; il crée uniquement de nouveaux calques avec la symbologie correspondante.
- Pour supprimer une carte, décochez-la dans la boîte de dialogue (voir "Processus" ci-dessus) ou supprimez sa couche directement depuis le panneau des couches QGIS.
- La carte **Total Base Demand** nécessite l'existence de nœuds avec une demande assignée ; Si le projet n'a aucune demande chargée, la couche est générée vide.
