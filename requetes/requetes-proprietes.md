# Demandes de propriété

**Barre de requêtes → Requêtes par propriétés…**

Ouvre le panneau **Requêtes par propriétés**, un outil de filtrage qui met en évidence sur la carte tous les éléments qui remplissent une ou plusieurs conditions sur leurs attributs. C'est le moyen le plus rapide de retrouver, par exemple, toutes les canalisations d'un diamètre inférieur à 80 mm, tous les nœuds dont la pression est inférieure à un seuil, ou encore toutes les vannes à l'état fermé.

<figure><img src="../assets/images/queries/queries-by-properties.png" alt="Panneau Requêtes par propriétés avec conditions configurées et résultat mis en évidence en magenta"><figcaption><p>Panneau Requêtes par propriétés avec conditions configurées et résultat mis en évidence en magenta</p></figcaption></figure>
*Requêtes par panneau de propriétés : conditions configurées sur les attributs du canal. Les éléments qui remplissent la condition sont surlignés en magenta sur la carte.*

---

## Interface du tableau de bord

Le panneau a une couleur d'identification **violet** (`#7B1FA2`) dans son en-tête pour le distinguer du reste des panneaux QGISRed. Contient :

- **Sélecteur de type d'élément** : Tuyaux, Jonctions, Réservoirs, Bâches, Pompes, Vannes
- **Mode de critère** : deux options, **One Criterion** (une seule condition active) et **Multiple Criteria** (liste de conditions combinables, voir plus bas)
- **Zone Conditions** : une ou plusieurs lignes avec champ, opérateur et valeur
- **Bouton Exécuter** : applique la requête et met en surbrillance le résultat
- **Bouton Effacer** : supprime la surbrillance de la carte
- **Panneau Statistiques** : sélecteur de propriété et tableau avec les résultats numériques de la requête (voir plus bas)
- **Étiquette temporelle** : Lorsque les résultats de la simulation sont chargés, affiche l'instant actif avec le préfixe "Time :" suivi de la valeur en gras au format `HH:MM:SS`. L'étiquette statistique du résultat est également affichée en gras.

---

## Types de conditions

L'opérateur disponible pour chaque champ dépend du type de données :

### Champs numériques

| Opérateur | Signification |
|----------|-------------|
| `All` | Aucun filtre (toutes les valeurs) |
| `>=` | Supérieur ou égal à |
| `<=` | Inférieur ou égal à |
| `=` | Égal à |
| `>` | Supérieur à |
| `<` | Moins de |
| `≠` | Autre que |
| `Range` | Entre deux valeurs (intervalle fermé) |

### Champs de liste (énumérés)

Champs comme `Status` qui ont un ensemble fini de valeurs possibles :

| Opérateur | Signification |
|----------|-------------|
| `All` | Pas de filtre |
| `=` | Égal à la valeur sélectionnée |

> ℹ️ Pour `Type`/`ValveType` sur les vannes, le sélecteur de valeur affiche le nom long descriptif du type (par exemple « Stabilisatrice Aval » pour PRV) au lieu du code EPANET.

### Champs de texte libres

Champs comme `Tag` ou `Id` :

| Opérateur | Signification |
|----------|-------------|
| `All` | Pas de filtre |
| `=` | Exactement pareil |
| `≠` | Différent |
| `ILIKE` | Contient (insensible à la casse) |
| `NOT ILIKE` | Ne contient pas (insensible à la casse) |
| `LIKE` | Contient (sensible à la casse) |
| `NOT LIKE` | Ne contient pas (sensible à la casse) |

---

## Processus

1. Ouvrez les **Requêtes par propriétés** à partir de la barre Requêtes.
2. Sélectionnez le **type d'élément** sur lequel vous souhaitez filtrer.
3. Ajoutez une ou plusieurs conditions : choisissez le champ, l'opérateur et écrivez la valeur.
4. Appuyez sur **Exécuter**. QGISRed évalue la requête et met en évidence en **magenta** les éléments qui la remplissent — en mode Multiple Criteria, selon la logique d'inclusion/exclusion expliquée plus bas.
5. Les éléments en surbrillance restent visibles lorsque le panneau est actif. Appuyez sur **Effacer** pour supprimer la surbrillance.

---

## Mode critère unique ou multiple

Le bouton radio **One Criterion** limite le panneau à une seule condition active à la fois : changer le champ, l'opérateur ou la valeur remplace la condition précédente. C'est le mode le plus simple pour des requêtes ponctuelles.

Le bouton radio **Multiple Criteria** ouvre une liste de conditions indépendantes qui peuvent être combinées entre elles :

- **Add** : ajoute la condition configurée ci-dessus à la liste, marquée comme condition d'**inclusion** (`+`).
- **Subtract** : ajoute la condition configurée ci-dessus à la liste, marquée comme condition d'**exclusion** (`-`).
- Chaque ligne de la liste peut être **réordonnée** (flèches haut/bas), **modifiée** (double-clic ou bouton d'édition), **supprimée**, ou **activée/désactivée** temporairement sans la supprimer (bouton « Enable/disable selected criterion ») pour essayer des combinaisons sans perdre les conditions déjà définies.

En passant de **Multiple Criteria** à **One Criterion** avec plus d'une condition dans la liste, QGISRed demande une confirmation : seule la première est conservée, le reste est abandonné.

### Logique de combinaison

Les conditions d'inclusion (`+`) se combinent entre elles avec **OR** : un élément est mis en évidence s'il remplit **l'une quelconque** d'entre elles. Les conditions d'exclusion (`-`) se combinent entre elles avec **AND** et le résultat est **soustrait** du précédent. En résumé :

> *(n'importe quelle condition d'inclusion)* **AND NOT** *(toutes les conditions d'exclusion)*

Par exemple, pour trouver toutes les canalisations de diamètre ≥ 300 mm qui **ne sont pas** en fonte : une condition `Diameter >= 300` marquée avec **Add**, et une condition `Material = Cast Iron` marquée avec **Subtract**.

En mode **One Criterion**, il n'y a qu'une seule condition, donc cette combinaison ne s'applique pas.

---

## Résultats des simulations

Si le projet a des résultats de simulation chargés, les champs de résultats (pression, débit, vitesse...) apparaissent également dans le sélecteur de champs, permettant de filtrer, par exemple, les canalisations avec une vitesse inférieure à 0,5 m/s ou les nœuds avec une pression négative.

> ⚠️ **Champs qualité conditionnels.** Les champs de résultat `Quality` et `ReactRate` n'apparaissent que lorsque le modèle qualité du projet le permet : `Quality` est masqué avec le modèle *Aucun* et `ReactRate` n'est visible qu'avec le modèle *Chimique*. Les champs de qualité statiques (`BulkCoeff`, `WallCoeff`, `ReactCoef`, `IniQuality`) sont masqués lorsque le modèle de qualité est *Aucun*, *Age* ou *Trace*.

---

## Tableau de statistiques

Le panneau calcule des statistiques numériques sur les éléments mis en évidence sans besoin d'exporter quoi que ce soit. Sélectionnez dans la liste déroulante **Statistics of... for selected Elements** la propriété à calculer — n'importe quel champ numérique du type d'élément actif, ou une des variables de résultat si une simulation est chargée — et le tableau se met à jour automatiquement.

Les colonnes dépendent du type de propriété :

| Propriété | Colonnes |
|---|---|
| Champ de texte ou de liste | **Count** (nombre d'éléments) |
| Champ numérique | **Count**, **Avg**, **Min**, **Max**, et **Sum** ou **StdD** selon la propriété (les débits et les demandes affichent la somme ; le reste, l'écart type) |
| **None** (sans propriété) | seulement **Count** |

En mode **One Criterion**, le tableau affiche une seule ligne avec le résultat de la condition active. En mode **Multiple Criteria** avec plusieurs conditions activées, il affiche une ligne par condition (étiquetée `Cr1`, `Cr2`...) et une dernière ligne **All** en jaune avec le résultat combiné (la même logique d'inclusion/exclusion que la mise en évidence sur la carte) — ce qui permet de comparer combien d'éléments apporte chaque condition séparément par rapport au total combiné.

## Exporter les critères et les statistiques

Les boutons d'exportation du panneau (critères de requête et tableau de statistiques) enregistrent par défaut dans le sous-dossier `Queries/Queries by properties` du projet, au lieu du dossier racine.

> 📝 Lors de l'exportation de plusieurs critères combinés en texte ou en CSV, chaque ligne est numérotée `Cr1:`, `Cr2:`... au lieu de commencer directement par l'opérateur de la condition — ainsi un tableur n'interprète pas par erreur un critère commençant par `+` ou `-` comme une formule.

Le CSV de statistiques inclut, avant le tableau de valeurs, des lignes d'en-tête avec le projet, le scénario, le type d'élément, la ou les requêtes appliquées et la grandeur exportée.

## Notes d'utilisation

- La requête ne modifie aucune donnée du modèle ni ne crée de nouvelles couches : elle change uniquement la symbologie temporelle.
- La surbrillance magenta est visible sur n'importe quel arrière-plan de carte.
- Lorsque vous fermez le panneau, la surbrillance disparaît et la symbologie revient à l'état précédent.

## Résolution du champ ID

Le panneau utilise la même logique de résolution de champ d'identifiant automatique que l'explorateur d'éléments (`getIdFieldName(layer)`). Les champs de requête par ID (`PipeID`, `TankID`, etc.) sont automatiquement détectés en fonction du type de couche, de sorte que les requêtes sur le champ `Id` fonctionnent correctement quel que soit le nom réel du champ dans le fichier de formes du projet. Voir [Explorateur d'éléments](explorateur-elements.md) pour plus de détails.

Les alias `PumpCurvID`, `BaseDem` et `SourceQual` sont automatiquement reconnus comme des champs de type numérique pour les pompes, les demandes et les sources respectivement. Le type de données de chaque champ (numérique, liste ou texte libre) est déterminé automatiquement à partir du schéma de l'élément, sans nécessiter de configuration manuelle.
