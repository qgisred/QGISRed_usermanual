# Modifier par groupe

**Barre d'édition → Modifier les propriétés par groupe…**

L'outil **Modifier les propriétés par groupe** vous permet de modifier un attribut de plusieurs éléments de réseau de manière groupée. Combinez un filtre facultatif avec une action d'édition et appliquez le résultat à tous les éléments qui remplissent la condition, en accumulant les modifications dans un tampon d'édition QGIS jusqu'à ce que l'utilisateur les valide ou les abandonne.

La boîte de dialogue est **non modale** : vous pouvez toujours interagir avec la carte lorsqu'elle est ouverte.

<figure><img src="../assets/images/edicion/edicion-por-grupo.png" alt="Modifier les propriétés par boîte de dialogue de groupe avec filtre et action configurés"><figcaption><p>Modifier les propriétés par boîte de dialogue de groupe avec filtre et action configurés</p></figcaption></figure>
*Boîte de dialogue Modifier par groupe : filtrer par champ numérique et multiplier par action sur les canalisations.*

---

## Types d'articles disponibles

| Élément | Descriptif |
|----------|-------------|
| **Jonctions** | Nœuds de réseau |
| **Demandes multiples** | Réclamations multiples par catégorie |
| **Tuyaux** | Tuyaux |
| **Réservoirs** | Dépôts |
| **Réservoirs** | Réservoirs |
| **Pompes** | Bombes |
| **Valves** | Vannes |
| **Sources** | Sources de qualité |
| **Connexions de services** | Joncs |
| **Vannes d'isolement** | Vannes d'isolement |
| **Mètres** | Débitmètres |

> 🧪 **Champs de qualité chimique :** Les champs BulkCoeff et WallCoeff (tuyaux) et ReactCoef et InitQuality (réservoirs, réservoirs et nœuds) n'apparaissent dans les sélecteurs de champs que lorsque le modèle de qualité du projet est défini sur **Chimique**.

---

## Sélectionner des éléments

La section **Sélectionner les éléments** de la boîte de dialogue regroupe le filtre de champ, l'aperçu de la carte et la portée.

### Filtre de champ

La liste déroulante des champs commence par l'option **Aucun filtre**. Pendant que cette sélection est maintenue, les contrôles d'opérateur et de valeur restent masqués et l'action affecte tous les éléments du type choisi.

Lorsque vous sélectionnez un champ spécifique, les contrôles d'opérateur et de valeur apparaissent :

- L'**opérateur** détermine le type de comparaison (voir tableau ci-dessous).
- La **valeur** est automatiquement remplie avec les valeurs uniques présentes dans le calque. La liste inclut **NULL** comme première option :
- L'opérateur `=` avec NULL génère un filtre **IS NULL**.
- L'opérateur `≠` avec NULL génère un filtre **IS NOT NULL**.
- Le champ de valeur dispose d'un bouton ****** pour le supprimer rapidement. De plus, le champ est **modifiable** : l'utilisateur peut saisir une valeur personnalisée qui n'est pas répertoriée dans la liste déroulante.

#### Opérateurs disponibles par type de champ

| Type de champ | Opérateurs |
|---------------|------------|
| Numérique | `>=`, `<=`, `=`, `>`, `<`, `≠` |
| Liste des valeurs | `=` |
| Texte libre | `=`, `≠`, `ILIKE`, `NOT ILIKE`, `LIKE`, `NOT LIKE` |
| Dates | `=` (sélecteur de calendrier) |

### Aperçu sur la carte

La case à cocher **Aperçu sur la carte** met en évidence en **orange** les éléments qui correspondent au filtre actif, se mettant à jour en temps réel lorsqu'un paramètre de filtre change. À côté de cette case se trouve le **nombre d'éléments** qui correspondent au filtre à ce moment-là.

### Éléments sélectionnés uniquement

En cochant **Uniquement les entités sélectionnées**, l'action affecte uniquement les éléments sélectionnés sur la carte au moment où vous appuyez sur **Appliquer**. La sélection peut être effectuée avant d'ouvrir la boîte de dialogue ou pendant qu'elle est ouverte.

Décochée (par défaut), l'action est appliquée à tous les éléments du type choisi répondant au filtre.

---

## Modifier l'action (section « Faire… »)

Définit quel attribut modifier et avec quelle valeur ou transformation.

### Actions pour les champs numériques

| Actions | Formule |
|--------|---------|
| **Remplacer par** | `operando` |
| **Multiplier par** | `valor_actual × operando` |
| **Ajouter** | `valor_actual + operando` |
| **Soustraire** | `valor_actual − operando` |
| **Diviser par** | `valor_actual / operando` |
| **Serrer minimum à** | `max(valor_actual, operando)` |
| **Serrer maximum à** | `min(valor_actual, operando)` |

### Actions pour les champs de texte

| Actions | Résultat |
|--------|-----------|
| **Défini sur** | Remplace la valeur entière |
| **Ajouter** | Ajoute le texte à la valeur actuelle |
| **Ajouter** | Ajoute le texte à la fin de la valeur actuelle |
| **Rechercher et remplacer** | Rechercher et remplacer (sensible à la casse) |

### Actions pour les champs énumérés

Il suffit de **Remplacer par**, en sélectionnant la nouvelle valeur dans une liste. Les options disponibles dépendent du type de champ :

| Champ | Source des options |
|-------|--------------------|
| `InitStatus` | Liste EPANET fixe (Ouverte, Fermée, CV, Actif…) |
| `Material` | Tableau des matériaux du projet |
| `Curve` | Courbes du projet filtrées par type (pompe, volume, rendement, perte de charge) |
| `Pattern` | Modèles de projets filtrés par type (demande, qualité, tête, rapidité, prix) |

### Champs de date

Action **Définir sur** : La date est sélectionnée à partir de la combinaison de dates existante sur le calque ou via le bouton du calendrier.

---

## Boutons de dialogue

| Bouton | Comportement |
|-------|----------------|
| **Postuler** | Affiche une boîte de dialogue de pré-validation détaillant les modifications à appliquer temporairement (type d'élément, champ et nombre d'éléments affectés) et demande une confirmation avant d'écrire dans le tampon d'édition QGIS. Il peut être appelé plusieurs fois pour accumuler les modifications sur différents attributs. Les éléments modifiés sont sélectionnés sur la carte et leur table attributaire est ouverte ou réactivée. |
| **Accepter** | Il affiche une simple confirmation et, après acceptation, enregistre définitivement toutes les modifications accumulées dans le tampon sur le disque. Fermez le dialogue ; les tables attributaires restent ouvertes. |
| **Annuler** | Annule **toutes** les modifications accumulées dans le tampon (restauration complète) et ferme la boîte de dialogue. Efface la sélection sur la carte, mais les tables attributaires restent ouvertes. |

> Les modifications ne sont écrites sur le disque que lorsque vous appuyez sur **Accepter**. Lorsque vous travaillez avec **Apply**, les données se trouvent dans le tampon d'édition de QGIS et peuvent être annulées en masse avec **Cancel** à tout moment.

---

## Table attributaire

Après chaque **Appliquer**, l'outil ouvre ou réactive la table attributaire de la couche affectée, qu'elle soit ancrée ou flottante, sans la dupliquer. Les éléments modifiés apparaissent ordonnés au début. Si plusieurs couches sont modifiées successivement **Appliquer**, chaque table est gérée indépendamment.

Lorsque vous appuyez sur **Annuler** ou **Accepter**, les tables attributaires restent ouvertes ; seule la sélection sur la carte est effacée.

---

## Mise à jour automatique de la boîte de dialogue

Lorsque des couches sont ajoutées ou supprimées alors que la boîte de dialogue est ouverte, elle met automatiquement à jour et restaure les sélections précédentes de type d'élément, de champ et de filtre. Si le projet est fermé ou si un autre projet est chargé, la boîte de dialogue se ferme automatiquement.

---

## Exemples d'utilisation

**Changer le matériau pour des tuyaux d'un diamètre spécifique**
Élément : Tuyaux — Filtre : `Diameter = 200` — Do : `Material → Replace with → PVC`

**Augmente la rugosité des tuyaux en fonte de 10 %**
Filtrer : `Material = FD` — Faire : `Roughness → Multiply by → 1.1`

**Fermez toutes les vannes d'isolement**
Élément : Vannes d'isolement — Filtre : Pas de filtre — Faire : `InitStatus → Replace with → CLOSED`

**Attribuer un motif à un ensemble de nœuds sélectionné**
Cochez "Uniquement les entités sélectionnées" — Élément : Jonctions — Faire : `Pattern → Replace with → PAT_RESIDENCIAL`

**Remplacer le texte dans les étiquettes**
Élément : Jonctions — Faire : `Tag → Find and replace → Buscar: "SEC" / Reemplazar: "ZN"`
