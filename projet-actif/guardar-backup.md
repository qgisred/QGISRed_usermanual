# Enregistrer et sauvegarder

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

## Sauvegarde

**Barre de projet → Sauvegarde** (Sauvegarde du projet)

Crée une copie complète de tous les fichiers SHP, fichiers DBF et métadonnées du projet dans un sous-dossier avec la date et l'heure actuelles.

### Où est-il enregistré

```
{CarpetaProyecto}/Backups/{NombreRed}_{YYYYMMDD_HHMMSS}/
```

Par exemple :
```
RedUrbana/Backups/RedUrbana_20241215_143022/
    RedUrbana_Junctions.shp
    RedUrbana_Pipes.shp
    RedUrbana_Options.dbf
    ...
```

Une fois terminé, QGISRed affiche le chemin complet de la copie créée dans la barre de message.

### Ce qui est inclus dans la sauvegarde

- Tous les fichiers SHP+DBF+PRJ dans le dossier principal du projet
- Les fichiers d'options et de métadonnées (`_Options.dbf`, `_Title.dbf`)
- Les sous-dossiers de données auxiliaires (Demands Builder, etc.)

### Ce qui n'est pas inclus

- Le dossier `Results/` (les résultats de simulation peuvent être très volumineux et peuvent être régénérés en exécutant à nouveau la simulation)
- Le dossier `Issues/` (régénéré lors de la relance des vérifications)
- Le fichier `.qgz` (enregistrez-le manuellement avec _Save Map_ si vous souhaitez l'inclure)

> 💡 **Bonnes pratiques** : Effectuez une sauvegarde avant les opérations qui modifient plusieurs éléments à la fois (importations groupées, modifications CRS, conversions de rugosité). Il est également recommandé avant de mettre à jour la version du plugin.

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
| Sauvegarde | Tous les SHP/DBF du projet | Sous-dossier `Backups/` |
