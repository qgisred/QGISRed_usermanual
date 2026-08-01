# Vérification d'attribut

Les quatre outils du deuxième groupe de la barre Debug auditent les **données alphanumériques** des canalisations pour détecter des erreurs de transcription, des valeurs incohérentes ou des champs vides qui empêcheraient une simulation correcte ou le calcul de rugosité de vieillissement.

Ils opèrent tous sur la sélection en cours ou sur l'ensemble du réseau s'il n'y a pas de sélection précédente.

---

## Vérifier la longueur des tuyaux

**Barre de débogage → Vérifier les longueurs de tuyaux**

Compare la **longueur stockée dans l'attribut `Length`** de chaque tuyau avec la **longueur géométrique réelle** calculée à partir des sommets SHP.

### Dialogue sur la tolérance

Lorsque vous activez l'outil, une boîte de dialogue s'ouvre dans laquelle vous définissez :

| Champ | Descriptif |
|-------|-------------|
| **Tolérance (%)** | Différence en pourcentage maximale acceptable entre la longueur de l'attribut et la longueur géométrique |
| **Mettre à jour les longueurs** | Si coché, remplace la valeur de l'attribut par la longueur géométrique sur tous les tuyaux qui dépassent la tolérance |

### Quand des différences apparaissent

- Tuyaux importés d'un `.inp` où `Length` a été calculé avec une échelle différente.
- Canalisations dont la géométrie a été modifiée (sommets déplacés) sans mettre à jour l'attribut.
- Réseaux en CRS projetés vs géographiques : si les coordonnées de `.inp` sont en degrés et utilisées en mètres, les longitudes sont incorrectes.

> QGISRed calcule la longueur géométrique toujours dans les unités CRS du projet. Si le projet utilise des coordonnées géographiques (degrés), les longitudes seront incorrectes. Utilisez toujours un CRS métrique projeté.

---

## Vérifier les diamètres

**Barre de débogage → Vérifier les diamètres**

Passez en revue les diamètres de toutes les canalisations sélectionnées (ou de l'ensemble du réseau) et signalez ceux qui sortent de la plage habituelle ou sont nuls.

### Ce qu'il détecte

- Tuyaux de diamètre **zéro ou négatif** (erreur d'importation ou édition manuelle).
- Des canalisations dont les diamètres sont statistiquement atypiques par rapport au reste du modèle (valeurs extrêmement élevées ou faibles).
- Tuyaux sans diamètre assigné (champ vide).

### Résultat

Les entités présentant des diamètres problématiques sont sélectionnées sur la carte et un résumé est affiché dans le panneau de message. Il ne modifie automatiquement aucune valeur : la correction doit être effectuée manuellement depuis la boîte de dialogue des propriétés ou la table attributaire.

---

## Vérifier les matériaux des tuyaux

**Barre de débogage → Vérifier les matériaux des tuyaux**

Vérifiez que la valeur du champ `Material` de chaque tuyau est définie dans la **Tableau des matériaux du projet** (Barre du projet → Table des matériaux).

### Ce qu'il détecte

- Tuyaux vides ou sans matériel.
- Canalisations avec un code matière qui n'existe pas dans la table du projet (par exemple, un code hérité d'un autre système SIG).
- Tuyaux avec la valeur `UNKNOWN` (valeur par défaut lorsque le matériau n'est pas connu).

### Pourquoi c'est important

Le matériau est essentiel pour l'outil **Attribuer des rugosités** (Barre d'outils), qui calcule la rugosité de vieillissement en fonction du matériau et de la date de pose. Si le matériau n'est pas valide, la rugosité ne peut pas être calculée.

---

## Vérifier les dates d'installation des tuyaux

**Barre de débogage → Vérifier les dates d'installation des tuyaux**

Vérifie le champ `InstallYear` des canalisations, qui stocke l'année d'installation au format numérique (`YYYY`).

### Ce qu'il détecte

| Problème | Descriptif |
|----------|-------------|
| **Date vide** | Champ `InstallYear` nul ou zéro |
| **Date future** | Année supérieure à l'année en cours |
| **Format incorrect** | Valeurs non numériques ou valeurs en dehors de la plage raisonnable (avant 1800 ou après l'année en cours) |

### Pourquoi c'est important

La date de pose, combinée au matériau, permet de calculer la **rugosité actuelle** de chaque canalisation grâce à la formule de vieillissement :

```
Rugosidad = Rugosidad_inicial + (Año_actual − InstallYear) × Incremento_anual
```

Si la date est erronée, la rugosité calculée sera fausse et la simulation hydraulique produira des résultats loin de la réalité.
