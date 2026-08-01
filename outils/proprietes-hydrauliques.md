# Propriétés hydrauliques

Les quatre premiers outils de la barre d'outils calculent ou mettent à jour les propriétés hydrauliques des canalisations et des nœuds en bloc : longueur, altitude et rugosité. Ils travaillent sur la sélection en cours ou sur l'ensemble du réseau s'il n'y a pas de sélection.

---

## Calculer automatiquement les longueurs de tuyaux

**Barre d'outils → Calculer automatiquement les longueurs de tuyaux**

Recalcule le champ `Length` de chaque tuyau en utilisant la longueur géométrique réelle mesurée sur les sommets SHP dans les unités CRS du projet.

### Quand l'utiliser

- Après avoir déplacé des sommets ou des nœuds avec les outils d'édition sans avoir mis à jour l'attribut.
- Après importation depuis un `.inp` dont les longueurs diffèrent de la géométrie réelle (coordonnées à une échelle différente ou projection différente).
- Comme étape précédente pour **Vérifier les longueurs des tuyaux** (Barre de débogage) pour laisser toutes les valeurs synchronisées avant l'audit.

L'outil écrase la valeur de `Length` sans condition sur tous les tuyaux dans la portée de sélection. Il ne demande pas de confirmation ni de filtre de tolérance.

> Utilisez toujours une métrique projetée CRS (UTM, LCC, etc.). Si le projet utilise des coordonnées géographiques (degrés décimaux), la longueur calculée sera en degrés et non en mètres et sera inutile pour la simulation.

---

## Interpoler l'altitude à partir de fichiers .asc…

**Barre d'outils → Interpoler l'altitude à partir de fichiers .asc…**

Attribue l'altitude (champ `Elevation`) aux nœuds, réservoirs et bâches du projet en interpolant leur valeur à partir d'un ou plusieurs Modèles Numériques de Terrain (MNT) au format ASC.

<figure><img src="../assets/images/herramientas/interpolate-elevation.png" alt="Sélecteur de fichiers ASC pour l'interpolation des altitudes"><figcaption><p>Sélecteur de fichiers ASC pour l'interpolation des altitudes</p></figcaption></figure>
*Sélecteur de fichiers MDT : vous pouvez télécharger plusieurs fichiers ASC pour couvrir toute la zone du réseau.*

### Format ASC pris en charge

```
ncols         500
nrows         400
xllcenter     450000.0
yllcenter     4400000.0
cellsize      5.0
nodata_value  -9999
230.4 231.1 231.8 ...
```

| En-tête | Signification |
|----------|-------------|
| `ncols` / `nrows` | Nombre de colonnes et de lignes dans le maillage |
| `xllcenter` / `yllcenter` | Coordonnées du centre de la cellule en bas à gauche (`xllcorner` / `yllcorner` est également accepté) |
| `cellsize` | Taille des cellules en unités CRS |
| `nodata_value` | Valeur que le plugin ignore (cellule sans données) |

### Processus d'affectation

1. Ouvrez le sélecteur et choisissez un ou plusieurs fichiers `.asc`. Vous pouvez combiner plusieurs MDT pour couvrir toute la zone du réseau.
2. QGISRed projette les coordonnées de chaque nœud sur le maillage et obtient l'altitude par interpolation bilinéaire entre les quatre cellules voisines.
3. Seuls les nœuds dont le `Elevation` actuel est égal à la valeur par défaut (généralement 0) sont mis à jour. Les nœuds dont la hauteur est déjà attribuée manuellement ne sont pas modifiés.
4. Les nœuds qui se situent en dehors de la portée de tous les MDT chargés sont marqués comme un incident sur le tableau de messages.

> Le CRS du fichier ASC doit correspondre au CRS du projet. Si elles ne correspondent pas, les coordonnées ne sont pas projetées et les nœuds seront en dehors du maillage.

---

## Définir les coefficients de rugosité (à partir du matériau et de la date)

**Barre d'outils → Définir les coefficients de rugosité (à partir du matériau et de la date)**

Calcule et attribue le coefficient de rugosité actuel de chaque tuyau en fonction de son matériau, de son année d'installation et des paramètres du **Tableau des matériaux** du projet.

### Formule de calcul

```
Rugosidad_actual = Rugosidad_inicial + (Año_actual − InstallYear) × Incremento_anual
```

Où `Rugosidad_inicial` et `Incremento_anual` sont obtenus à partir de la ligne du tableau des matériaux qui correspond au champ `Material` du tuyau.

### Prérequis

Avant d'utiliser cet outil, vérifiez avec la barre de débogage que :
1. Tous les tuyaux ont un `Material` valide (**Vérifiez les matériaux des tuyaux**).
2. Tous les tuyaux ont un `InstallYear` correct (**Vérifiez les dates d'installation des tuyaux**).

Si l'un de ces champs est vide ou invalide pour un tuyau, sa rugosité n'est pas mise à jour et est enregistrée comme un problème.

La rugosité s'écrit dans les unités de la formule du projet actif :

| Formule | Unité de rugosité |
|---------|---------------------|
| Darcy-Weisbach (DW) | mm (rugosité absolue des parois) |
| Hazen-Williams (HW) | Coefficient C sans dimension (typique 100-150) |
| Chézy-Manning (C-M) | Coefficient n (typique 0,010-0,020) |

> Le tableau des matériaux stocke la rugosité initiale en unités D-W (mm). Si le projet utilise H-W ou C-M, la valeur calculée est automatiquement convertie dans le système actif.

---

## Convertir les coefficients de rugosité…

**Barre d'outils → Convertir les coefficients de rugosité…**

Convertit les valeurs du champ `Roughness` de tous les tuyaux entre les trois formules de perte de pression. C'est nécessaire lorsque l'on change la formule hydraulique du projet et que l'on souhaite que les valeurs existantes conservent leur signification physique.

### Conversions disponibles

| Origine | Destination |
|--------|---------|
| Hazen-Williams (HW) | Darcy-Weisbach (DW) |
| Darcy-Weisbach (DW) | Hazen-Williams (HW) |
| Chézy-Manning (C-M) | Darcy-Weisbach (DW) |
| Darcy-Weisbach (DW) | Chézy-Manning (C-M) |

Lors de la modification de la formule hydraulique dans **Options du projet**, QGISRed détecte le changement et propose d'exécuter cet outil automatiquement. Si vous refusez à ce moment-là, vous pouvez le lancer manuellement à partir d'ici.

> La conversion D-W ↔ H-W utilise le diamètre et un débit de référence pour trouver le C qui produit la même perte que la rugosité D-W à ce débit. Le résultat peut différer d'un étalonnage direct car les trois formules ne sont pas mathématiquement équivalentes pour tous les régimes d'écoulement.
