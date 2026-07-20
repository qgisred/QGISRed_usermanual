# Formats et gestion DBF

Référence pour les utilisateurs qui modifient les données du projet directement dans les tables attributaires de QGIS ou à partir d'outils externes, sans passer par les boîtes de dialogue QGISRed.

---

## Format des dates

Le champ `InstalDate` de la couche `Pipes` stocke la date d'installation sous forme de chaîne de texte au format :

```
yyyyMMdd
```

| Composant | Descriptif | Exemple |
|------------|-------------|---------|
| `yyyy` | Année (4 chiffres) | `2023` |
| `MM` | Mois (2 chiffres, avec un zéro non significatif) | `07` |
| `dd` | Jour (2 chiffres, avec un zéro non significatif) | `15` |

**Exemple correct** : `20230715` (15 juillet 2023)

Si la valeur ne suit pas ce format exact, l'outil **Vérifier les dates d'installation des tuyaux** (barre de débogage) le signalera comme un problème et l'outil **Définir les coefficients de rugosité** (barre d'outils) ne pourra pas calculer la rugosité de vieillissement de ce tuyau.

---

## Modèles et courbes (DBF)

Les modèles et courbes de demande (H-Q, efficacité, volume) sont stockés dans des tableaux DBF séparés. Si vous les modifiez directement en dehors de QGIS :

- **Séparateur décimal** : utilisez toujours le **point** (`.`), quels que soient les paramètres régionaux du système. Les virgules comme séparateur décimal provoquent des erreurs de lecture.
- **Champ d'ordre** : chaque tableau possède un champ d'ordre numérique (`Order` ou similaire) qui détermine la séquence des points ou des facteurs au sein de la série. Ne modifiez pas ce champ et ne laissez pas de vide dans la numérotation.

---

## Règles

Les règles de contrôle sont stockées sous forme d'enregistrements individuels dans la table des règles DBF. Chaque règle occupe plusieurs lignes (une par ligne logique : SI, ET, OU, ALORS, ELSE). Si vous affichez la table en dehors du gestionnaire de règles QGISRed, triez les lignes selon ces deux colonnes dans cet ordre afin que les règles soient lisibles :

1. **`RuleOrder`** — regroupe toutes les lignes de la même règle.
2. **`LineOrder`** — définit l'ordre logique des conditions au sein de chaque règle.

Le champ **`Name`** stocke un label descriptif visible dans le gestionnaire de règles. Il n'affecte pas la simulation et peut rester vide.
