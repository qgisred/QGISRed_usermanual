# Enregistrer, exporter et fermer le projet

---

## Enregistrer la carte du projet

**Barre de projet → Enregistrer la carte** (Enregistrer la carte du projet)

Enregistre le fichier QGIS (`.qgz`) qui contient les paramètres visuels du projet : couches chargées, styles, visibilité des groupes, cadrage de la carte, etc.

### Première fois

Si le projet QGIS ne possède pas déjà un fichier `.qgz`, le plugin ouvre la boîte de dialogue standard QGIS **"Enregistrer sous"** suggérant automatiquement le dossier du projet QGISRed et le nom du réseau comme nom de fichier :

```
{CarpetaProyecto}/{NombreRed}.qgz
```

### Sauvegardes ultérieures

Si un `.qgz` existe déjà, il l'écrase directement (équivalent à `Ctrl+S` dans QGIS).

> 💡 **Recommandation** : enregistrez le `.qgz` dans le même dossier que les SHP du projet. Ainsi, si vous copiez le dossier sur un autre ordinateur, le fichier `.qgz` trouvera les SHP sans avoir besoin de reconfigurer les chemins.

> ⚠️ Enregistrez le `.qgz` **n'enregistre pas les données réseau**. Les données (diamètres, dimensions, exigences...) sont automatiquement enregistrées dans le SHP+DBF lorsque QGISRed les modifie. Le `.qgz` enregistre uniquement la présentation visuelle.

---

## Exporter le projet

**Chef de projet → Exporter**

> ⚠️ Ce bouton n'est **plus** sur la barre **Projet** : l'ancien bouton _Sauvegarde du projet_ a été supprimé et n'a pas de remplacement sur cette barre. L'export se fait maintenant depuis [Chef de projet](../gestion-projets/gestor-proyectos.md) — sélectionnez le projet dans la liste (il n'est pas nécessaire de l'ouvrir) et appuyez sur **Exporter**.

Génère un fichier ZIP portable avec le projet : le SHP/DBF du réseau, la carte QGIS (`.qgz`) si elle existe, et éventuellement les groupes de contenus et données complémentaires (cartographie de fond, MDT, orthophotos...) que référence cette `.qgz`.

### Avant d'exporter

Si le projet que vous exportez est celui que vous avez ouvert dans QGIS et que son `.qgz` comporte des modifications non enregistrées, QGISRed demande d'abord :

> _"Le projet QGIS comporte des modifications non enregistrées. Voulez-vous l'enregistrer avant de l'exporter ?"_

- **Oui** : enregistrez le `.qgz` et exportez cette version nouvellement enregistrée.
- **Non** : exporte le `.qgz` tel qu'il était lors de la dernière sauvegarde (les modifications en attente ne voyagent pas dans le ZIP).
- **Annuler** : La boîte de dialogue d'exportation ne s'ouvre pas.

### La boîte de dialogue d'exportation

<!-- TODO : capture en attente — Boîte de dialogue "QGISRed : Exporter le projet" -->

| Champ | Fonction |
|-------|---------|
| **Nom du fichier :** | Nom ZIP (sans extension) ; par défaut, le nom du réseau |
| **Dossier :** | Dossier de destination ; par défaut, le dossier Téléchargements de l'utilisateur |
| **Contenu** | Groupes facultatifs à inclure (voir ci-dessous) |
| **Données complémentaires** | Données externes référencées par `.qgz`, sélectionnables une à une |
| **Ouvrez le dossier contenant lorsque vous avez terminé** | Ouvrez l'explorateur de fichiers dans le dossier de destination lorsque vous avez terminé (activé par défaut) |

### Ce qui est toujours inclus

- Le SHP+DBF+PRJ du réseau à la racine du dossier projet (Tuyaux, Jonctions, Vannes, Pompes, Réservoirs, Bâches, Demandes, Sources...) et les fichiers d'options et de métadonnées (`_Options.dbf`, `_Title.dbf`).
- Le fichier carte `.qgz`, si QGISRed le trouve dans le dossier du projet ou dans son dossier parent. S'il n'y a pas de `.qgz` enregistré, la boîte de dialogue avertit que l'affichage de la carte ne sera pas exporté.

### Ce qui est inclus en option

Quatre groupes de contenus, chacun avec sa propre case dans la section **Contenu** (cochée par défaut si le groupe dispose de données de ce réseau ; si vide, la case est désactivée) :

| Boîte | Contenu |
|---------|-----------|
| **Résultats** | Résultats de simulation enregistrés dans `Results/` |
| **Problèmes** | Incidents détectés par vérifications, en `Issues/` |
| **Requêtes** | Requêtes enregistrées, dans `Queries/` |
| **Couches auxiliaires** | Couches auxiliaires (par exemple, du Demands Builder), dans `Auxiliary Layers/` |

Si le `.qgz` fait référence à des données complémentaires, la boîte de dialogue ajoute une table **Données complémentaires** avec une ligne par couche (nom, emplacement et état), chacune avec sa propre case à cocher — vous pouvez donc laisser de côté, par exemple, un MDT de plusieurs Go sans abandonner le reste.

### Ce qui n'est pas inclus

- Groupes de contenu que vous laissez décochés.
- Les données complémentaires qui se trouvent en dehors du dossier projet et de son dossier parent : la boîte de dialogue les marque comme _"Non exportable"_ et prévient avant l'exportation. Pour les inclure, déplacez-les avec l'explorateur de fichiers vers le dossier du projet (ou à côté) et rouvrez le projet pour que QGISRed les relie.
- Couches de fond distantes (services WMS, XYZ, bases de données) : il n'y a rien à copier, elles ne bloquent donc jamais l'export ni n'apparaissent dans le tableau.

> ⚠️ Si vous omettez un groupe de contenu ou une couche complémentaire que `.qgz` utilise encore, QGISRed vous avertit avant d'exporter. Appuyez sur **OK** une deuxième fois si vous souhaitez quand même continuer.

### Où est-il enregistré

```
{CarpetaDestino}/{NombreArchivo}.zip
```

Par défaut, `{CarpetaDestino}` est le dossier Téléchargements de l'utilisateur et `{NombreArchivo}` est le nom du réseau, mais les deux sont modifiables dans la boîte de dialogue. Si un ZIP portant ce nom existe déjà, QGISRed vous demande si vous souhaitez l'écraser.

Une fois terminé, QGISRed affiche le chemin complet du ZIP créé dans la barre de messages.

> 💡 **Bonnes pratiques** : Exportez le projet avant les opérations qui modifient plusieurs éléments à la fois (importations groupées, modifications CRS, conversions de rugosité) et avant de mettre à jour la version du plugin. Pour récupérer un projet exporté, utilisez **Importer le projet → onglet "Projet QGISRed"** — voir [Ouvrir et importer des projets](../gestion-projets/abrir-importar.md).

---

## Fermer le projet

**Barre de projet → Fermer le projet** (Fermer le projet)

Fermez le projet QGISRed actuel et nettoyez la session QGIS : supprimez toutes les couches chargées et restaurez l'état initial.

Cela équivaut à utiliser _Projet → Nouveau_ dans le menu QGIS.

> ⚠️ S'il y a des modifications non enregistrées dans le fichier `.qgz`, QGIS vous demandera si vous souhaitez les enregistrer avant de fermer.

---

## Résumé : ce que chaque option permet d'économiser

| Opération | Ce qui garde | Où |
|-----------|-----------|-------|
| Outils d'édition | Attributs et géométrie | SHP/DBF sur disque, immédiatement |
| Enregistrer la carte | Styles, calques visibles, cadrage | Fichier `.qgz` |
| Exporter le projet (Chef de projet → Exporter) | Réseau SHP/DBF, `.qgz` et éventuellement groupes de données et de contenus supplémentaires | Fichier `.zip` dans le dossier de votre choix |
