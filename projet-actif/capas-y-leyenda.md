# Gestionnaire de couches et légende

---

## Gestionnaire de couches

**Barre de projet → Gestionnaire de calques** (Gestionnaire de calques)

Contrôle quelles couches de projet sont actives dans QGIS et vous permet de récupérer des couches qui ont été accidentellement supprimées.

<figure><img src="../assets/images/proyecto/gestor-capas.png" alt="Boîte de dialogue Gestionnaire de couches QGISRed"><figcaption><p>Boîte de dialogue Gestionnaire de couches QGISRed</p></figcaption></figure>
*Gestionnaire de calques : liste de tous les calques du projet avec leur état de chargement.*

### Couches de base (Entrées)

Affiche les 6 éléments de base d'EPANET ainsi que les couches optionnelles (demandes multiples, sources, connexions de service, vannes d'isolement, compteurs). Pour chacun, indiquez s'il est chargé dans QGIS ou non.

- **Box cochée** → la couche est chargée et visible dans la légende QGIS.
- **case non cochée** → la couche existe sur le disque mais n'est pas chargée.

Vous pouvez cocher ou décocher n’importe quelle couche pour la télécharger ou la télécharger sans affecter les données.

### Récupérer un calque supprimé

Si vous avez accidentellement supprimé une couche de la légende QGIS (ou son fichier SHP sur le disque), le gestionnaire de couches vous permet de la **recréer vide** :

1. Sélectionnez le calque manquant (il apparaîtra avec une icône d'avertissement).
2. Appuyez sur **Récupérer** (ou le bouton équivalent selon la version).
3. QGISRed crée le SHP vide avec la structure de champ correcte et le charge dans QGIS.

> ⚠️ Recovery crée le calque vide. Les données qui s'y trouvaient (si le SHP a été effacé du disque) ne peuvent être récupérées que si vous disposez d'une copie de sauvegarde.

### Résumé du modèle (Résumé)

**Barre de projet → Résumé**

Générez un rapport rapide avec le nombre d'éléments de chaque type présents dans le projet :

```
Junctions: 1 243
Pipes: 1 876
Tanks: 3
Reservoirs: 2
Valves: 47
Pumps: 8
```

Utile pour vérifier que l'importation a été terminée ou pour documenter la taille du modèle.

---

## Éditeur de légende

**Barre de projet → Éditeur de légende** (Éditeur de légende)

Ouvre un panneau flottant qui vous permet de personnaliser la **symbologie** des couches du projet sans avoir à naviguer dans le menu des propriétés de la couche QGIS.

<figure><img src="../assets/images/proyecto/editor-leyenda.png" alt="Panneau de l'éditeur de légende QGISRed"><figcaption><p>Panneau de l'éditeur de légende QGISRed</p></figcaption></figure>
*Panneau Legend Editor : styles prédéfinis et personnalisation des couleurs et des tailles.*

### Styles prédéfinis

QGISRed inclut des styles QML prédéfinis pour chaque type d'élément, adaptés au système d'unités du projet (SI/US). L'éditeur permet d'appliquer ces styles en un seul clic :

- Style par **matériau** (codage couleur par matériau du tuyau)
- Style par **diamètre** (échelle de couleurs proportionnelle au diamètre)
- Style par **longueur**
- Style **base** (couleurs QGISRed standard)

### Personnalisation manuelle

Pour chaque calque, vous pouvez ajuster :
- Couleur de remplissage et de bordure pour les éléments ponctuels
- Couleur et épaisseur de trait pour les tuyaux
- Taille du symbole

Les modifications sont enregistrées dans le fichier du projet QGIS `.qgz`. Si vous n'avez pas enregistré le `.qgz`, les styles personnalisés seront perdus lorsque vous fermerez QGIS.

> 💡 Si vous changez de version du plugin et que les styles sont réinitialisés à l'ouverture du projet, c'est normal : QGISRed détecte le changement de version et applique les styles par défaut mis à jour. Vous pouvez à nouveau personnaliser à partir de l'éditeur de légende.
