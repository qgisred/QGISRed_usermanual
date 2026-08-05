# Demandes de propriété

**Barre de requêtes → Requêtes par propriétés…**

Ouvre le panneau **Requêtes par propriétés**, un outil de filtrage qui met en évidence sur la carte tous les éléments qui remplissent une ou plusieurs conditions sur leurs attributs. C'est le moyen le plus rapide de retrouver, par exemple, toutes les canalisations d'un diamètre inférieur à 80 mm, tous les nœuds dont la pression est inférieure à un seuil, ou encore toutes les vannes à l'état fermé.

<figure><img src="../assets/images/consultas/queries-by-properties.png" alt="Panneau Requêtes par propriétés avec conditions configurées et résultat mis en évidence en magenta"><figcaption><p>Panneau Requêtes par propriétés avec conditions configurées et résultat mis en évidence en magenta</p></figcaption></figure>
*Requêtes par panneau de propriétés : conditions configurées sur les attributs du canal. Les éléments qui remplissent la condition sont surlignés en magenta sur la carte.*

---

## Interface du tableau de bord

Le panneau a une couleur d'identification **violet** (`#7B1FA2`) dans son en-tête pour le distinguer du reste des panneaux QGISRed. Contient :

- **Sélecteur de type d'élément** : Tuyaux, Jonctions, Réservoirs, Bâches, Pompes, Vannes
- **Zone Conditions** : une ou plusieurs lignes avec champ, opérateur et valeur
- **Bouton Exécuter** : applique la requête et met en surbrillance le résultat
- **Bouton Effacer** : supprime la surbrillance de la carte
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
4. Appuyez sur **Exécuter**. QGISRed évalue la requête et met en évidence en **magenta** tous les éléments qui remplissent toutes les conditions simultanément (logique ET).
5. Les éléments en surbrillance restent visibles lorsque le panneau est actif. Appuyez sur **Effacer** pour supprimer la surbrillance.

---

## Combinaison de conditions

Toutes les conditions actives sont combinées avec la logique **ET** : un élément n'est mis en évidence que s'il remplit **toutes** les conditions à la fois. Pour une logique OU (n'importe laquelle des conditions), il exécute des requêtes distinctes avec un seul critère à la fois.

---

## Résultats des simulations

Si le projet a des résultats de simulation chargés, les champs de résultats (pression, débit, vitesse...) apparaissent également dans le sélecteur de champs, permettant de filtrer, par exemple, les canalisations avec une vitesse inférieure à 0,5 m/s ou les nœuds avec une pression négative.

> ⚠️ **Champs qualité conditionnels.** Les champs de résultat `Quality` et `ReactRate` n'apparaissent que lorsque le modèle qualité du projet le permet : `Quality` est masqué avec le modèle *Aucun* et `ReactRate` n'est visible qu'avec le modèle *Chimique*. Les champs de qualité statiques (`BulkCoeff`, `WallCoeff`, `ReactCoef`, `IniQuality`) sont masqués lorsque le modèle de qualité est *Aucun*, *Age* ou *Trace*.

---

## Notes d'utilisation

- La requête ne modifie aucune donnée du modèle ni ne crée de nouvelles couches : elle change uniquement la symbologie temporelle.
- La surbrillance magenta est visible sur n'importe quel arrière-plan de carte.
- Lorsque vous fermez le panneau, la surbrillance disparaît et la symbologie revient à l'état précédent.

## Résolution du champ ID

Le panneau utilise la même logique de résolution de champ d'identifiant automatique que l'explorateur d'éléments (`getIdFieldName(layer)`). Les champs de requête par ID (`PipeID`, `TankID`, etc.) sont automatiquement détectés en fonction du type de couche, de sorte que les requêtes sur le champ `Id` fonctionnent correctement quel que soit le nom réel du champ dans le fichier de formes du projet. Voir [Explorateur d'éléments](explorateur-elements.md) pour plus de détails.

Les alias `PumpCurvID`, `BaseDem` et `SourceQual` sont automatiquement reconnus comme des champs de type numérique pour les pompes, les demandes et les sources respectivement. Le type de données de chaque champ (numérique, liste ou texte libre) est déterminé automatiquement à partir du schéma de l'élément, sans nécessiter de configuration manuelle.
