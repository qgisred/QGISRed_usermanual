# Configuration du projet

La barre **Projet** regroupe trois boîtes de dialogue de configuration qui affectent le comportement hydraulique du modèle et les valeurs par défaut avec lesquelles de nouveaux éléments sont créés.

---

## Options du projet

**Barre de projet → Options du projet** (Paramètres du projet)

Ouvre la boîte de dialogue principale des options d'EPANET. Il équivaut à la section `[OPTIONS]` du fichier `.inp`.

<figure><img src="../assets/images/proyecto/opciones-proyecto.png" alt="Boîte de dialogue Options du projet : onglets Hydraulique, Qualité, Temps et Énergie"><figcaption><p>Boîte de dialogue Options du projet : onglets Hydraulique, Qualité, Temps et Énergie</p></figcaption></figure>
*Boîte de dialogue Options du projet avec ses quatre onglets.*

### Onglet hydraulique

| Champ | Descriptif |
|-------|-------------|
| **Unités de débit** | Définit le système d'unités du projet. Les unités métriques (LPS, LPM, MLD, CMH, CMD) correspondent au SI ; gallons et pieds cubes (CFS, GPM, MGD, IMGD, AFD) aux États-Unis |
| **Formule de perte de charge** | Darcy-Weisbach (D-W), Hazen-Williams (H-W) ou Chezy-Manning (C-M) |
| **Gravité spécifique** | Poids spécifique du fluide par rapport à l'eau pure (1,0 pour l'eau standard) |
| **Viscosité relative** | Facteur de viscosité cinématique de l'eau à 20 °C |
| **Précision** | Critère de convergence du solveur hydraulique |
| **Modèle de demande** | DDA (Demand Driven) ou PDA (Pressure Driven) — dans PDA, la demande est réduite si la pression descend en dessous d'un seuil |
| **Pression minimale / nominale** | Seuils pour le modèle PDA |
| **Max. itérations / rapport** | Paramètres de convergence du solveur |

> 💡 Changer les **unités de débit** ne convertit pas les valeurs déjà saisies. Si le réseau est défini sur LPS et que vous passez à GPM, toutes les valeurs de demande, de débit et de longueur devront être mises à jour manuellement.

### Onglet Qualité

| Champ | Descriptif |
|-------|-------------|
| **Type d'analyse de la qualité** | Aucun (ne simule pas la qualité), Chimique (réactif), Âge (âge de l'eau), Trace (traceur) |
| **Étiquette du réactif** | Nom du produit modélisé (par exemple « Chlore ») — apparaîtra dans les résultats |
| **Noeud traceur** | Pour l’analyse de type Trace, ID du nœud source du traceur |
| **Unités de concentration** | mg/L ou µg/L |
| **Diffusivité** | Coefficient de diffusion moléculaire relatif (1,0 pour le chlore dans l'eau) |
| **Tolérance** | Critère de convergence pour le solveur qualité |

### Onglet Heures

| Champ | Descriptif |
|-------|-------------|
| **Durée de la simulation** | Temps total de simulation. Format `HH:MM:SS` ou en heures (ex. `24:00:00`) |
| **Pas de temps hydraulique** | Intervalle de calcul hydraulique (généralement 1 h) |
| **Pass de temps de qualité** | Intervalle de calcul de la qualité (généralement 5 min) |
| **Pas de temps du rapport** | À quelle fréquence les résultats sont enregistrés (détermine le nombre de moments disponibles dans la visionneuse) |
| **Heure de début de la simulation** | Heure d'horloge correspondant à l'instant 0 de la simulation |
| **Type de statisticien** | Aucun (tous les instants), Moyenne, Minimum, Maximum, Plage |

> 💡 Une **étape de reporting** d'1 h dans une simulation de 24 h génère 25 instants de résultat (0 h à 24 h). Des étapes plus courtes augmentent la résolution temporelle mais aussi la taille des fichiers de résultats.

### Onglet Énergie

Permet de définir le coût énergétique des pompes pour l'analyse de la consommation :

| Champ | Descriptif |
|-------|-------------|
| **Prix global** | Coût par kWh (dans la devise définie) |
| **Modulation de prix** | Courbe de modulation temporelle des prix de l'électricité |
| **Rendement global** | Rendement moyen des pompes (si elles ne disposent pas de courbe de rendement individuelle) |

---

## Valeurs par défaut

**Barre de projet → Valeurs par défaut** (Valeurs par défaut)

Définit les valeurs qui sont automatiquement attribuées aux nouveaux éléments lors de leur création avec les outils d'édition.

<figure><img src="../assets/images/proyecto/valores-defecto.png" alt="Boîte de dialogue des valeurs par défaut avec des sections pour les nœuds, les tuyaux et les préfixes"><figcaption><p>Boîte de dialogue des valeurs par défaut avec des sections pour les nœuds, les tuyaux et les préfixes</p></figcaption></figure>
*Boîte de dialogue Valeurs par défaut : paramètres initiaux pour chaque type d'élément.*

### Préfixes d'identification

Chaque type d'élément possède un préfixe configurable qui est utilisé lors de la génération automatique de l'ID des nouveaux éléments :

| Élément | Préfixe par défaut | Exemple d'ID généré |
|----------|---------------------|------------------------|
| Jonction | J | J-1, J-2… |
| Tuyau | P | P-1, P-2… |
| Réservoir | T | T-1, T-2… |
| Bâche | R | R-1, R-2… |
| Soupape | V | V-1, V-2… |
| Pompe | BM | BM-1, BM-2… |

Les préfixes sont configurables. Le numéro de départ peut également être défini.

### Valeurs hydrauliques initiales

| Champ | Descriptif |
|-------|-------------|
| **Diamètre par défaut** | Diamètre (mm ou pouces) attribué aux nouveaux tuyaux |
| **Rugosité par défaut** | Coefficient de rugosité selon la formule active |
| **Dimension par défaut** | Altitude (m ou ft) attribuée aux nouveaux nœuds |
| **Demande de base par défaut** | Demande initiale des nouveaux nœuds de demande |
| **Vitesse de pompe par défaut** | Facteur de vitesse relative initial pour les pompes |

### Tolérances géométriques

| Champ | Descriptif |
|-------|-------------|
| **Tolérance aux nœuds** | Distance maximale (m ou ft) pour considérer deux points comme étant le même nœud |
| **Longueur minimale pour la division** | Longueur minimale des sections résultantes lors de la division d'un tuyau |
| **Longueur maximale pour la division** | Longueur maximale des sections résultantes lors de la division d'un tuyau |

---

## Tableau des matériaux

**Barre de projet → Tableau des matériaux** (Tableau des matériaux)

Gérez la liste des matériaux disponibles pour les tuyaux et leurs propriétés de vieillissement.

<figure><img src="../assets/images/proyecto/tabla-materiales.png" alt="Table des matériaux : code, dénomination, rugosité initiale et augmentation annuelle"><figcaption><p>Table des matériaux : code, dénomination, rugosité initiale et augmentation annuelle</p></figcaption></figure>
*Tableau des matériaux avec rugosité initiale et augmentation par an.*

### Champs du tableau

| Champ | Descriptif |
|-------|-------------|
| **Abréviation** | Code court du matériau (par exemple PVC, DI, AC) |
| **Description** | Nom complet (par exemple « Fonte ductile », « Amiante-ciment ») |
| **Rugosité initiale (mm)** | Coefficient de rugosité D-W à la date d'installation |
| **Augmentation annuelle (mm)** | Augmentation de la rugosité par année d'âge |

> ⚠️ Il ne peut pas y avoir deux matériaux avec la même abréviation — s'il y en a, QGISRed vous avertit et empêche la sauvegarde jusqu'à ce que vous corrigiez celui qui est répété.

### Ajouter un matériau

Le tableau affiche toujours une **ligne vide** à la fin. Écrivez-y directement (abréviation, description, rugosité initiale et incrément annuel) et, dès que vous quittez la ligne, QGISRed l'enregistre comme un nouveau matériau et ajoute une autre ligne vide en dessous — aucun bouton "Ajouter" distinct n'est nécessaire. Si vous laissez la rugosité ou l'incrément initial vide, ils sont enregistrés sous la valeur 0.

### Supprimer un matériau

Sélectionnez une ligne et appuyez sur **Suppr** pour la supprimer. Si le matériau est attribué à un tuyau ou à une connexion, QGISRed informe du nombre d'éléments qui l'utilisent et demande une confirmation avant de le supprimer. Si vous acceptez, ces éléments restent sans matériau attribué.

### Utiliser avec l'outil "Attribuer la rugosité"

Lorsque vous utilisez l'outil **Attribuer des rugosités** depuis la barre d'outils, QGISRed recherche dans ce tableau le matériau de chaque tuyau et calcule :

```
Rugosidad = Rugosidad_inicial + (Año_actual - Año_instalación) × Incremento_anual
```

> 💡 Vous pouvez ajouter des matériaux personnalisés. Les matériaux définis ici sont également disponibles lors de la création de nouvelles canalisations à partir de la barre d'édition.

### Matériaux inclus par défaut

QGISRed inclut une table de matériaux prédéfinis avec les plus courants (FG, FD, ACE, PVC, PE, PE-AD...). Vous pouvez les modifier ou les étendre en fonction des caractéristiques de votre système.

### Enregistrer et réutiliser les tables entre les projets

La table des matériaux est unique à chaque projet, mais peut être partagée avec d'autres projets en l'enregistrant en tant que table **globale** (enregistrée dans le profil utilisateur, en dehors de tout projet — un `.dbf` par table).

**Avec un projet actif** (fenêtre "Matériaux du projet"), la boîte de dialogue édite directement le tableau du projet (sans liste déroulante) et propose ces boutons :

| Bouton | Actions |
|-------|--------|
| **Enregistrer** | Ferme la boîte de dialogue et enregistre les modifications apportées au projet. |
| **Enregistrer comme global** | Enregistre une copie de la table actuelle en tant que **nouvelle** table globale, demandant un nom. Si une table globale portant ce nom existe déjà, demande confirmation avant de l'écraser. |
| **Restaurer les matériaux par défaut (langue)** | Remplace la table du projet par celle prédéfinie de QGISRed dans la langue indiquée entre parenthèses (celle de l'interface), en supprimant les matériaux du projet actuel. |
| **Charger la table des matériaux** | Remplace la table du projet par une autre, choisie dans une boîte de dialogue séparée qui répertorie à la fois les tables globales enregistrées par l'utilisateur et celles prédéfinies par QGISRed (marquées "(par défaut)"). |
| **Annuler** | Ferme la boîte de dialogue sans enregistrer les modifications. |

> ⚠️ Il ne peut pas y avoir deux matériaux avec la même abréviation — s'il y en a, QGISRed vous avertit avec un message rouge sous le tableau et empêche la sauvegarde jusqu'à ce que vous corrigiez celui qui est répété. La même vérification s'applique lorsque vous appuyez sur "Enregistrer" et "Enregistrer comme global".

### Aucun projet actif : gestionnaire de tables global

Si vous ouvrez **Table des matériaux** sans aucun projet QGISRed actif (par exemple, dès que vous ouvrez QGIS, avant de créer ou d'ouvrir un projet), la boîte de dialogue s'ouvre sous la forme d'une fenêtre séparée ("Tableaux de matériaux globaux") pour gérer les tables globales enregistrées, avec l'étiquette **"Sélectionnez la table de matériaux globale"** à côté d'une liste déroulante répertoriant toutes celles disponibles :

- **Tableaux globaux enregistrés** par l'utilisateur (créés avec "Enregistrer" ou "Enregistrer sous..."), modifiables.
- Les **tables prédéfinies** de QGISRed par langue, marquées du suffixe **"(par défaut)"** — en lecture seule : la grille ne peut pas être modifiée tant que l'une d'entre elles est sélectionnée.

À côté de la liste déroulante se trouve un bouton **Supprimer** qui supprime la table globale sélectionnée ; il n'est disponible que pour vos propres tables, pas pour celles prédéfinies en lecture seule.

Les boutons ci-dessous changent en fonction de la table sélectionnée :

| Bouton | Quand apparaît-il | Actions |
|-------|-----------------|--------|
| **Enregistrer** | Uniquement avec votre propre table sélectionnée (non prédéfinie) | Enregistre les modifications **sur la table déjà sélectionnée**, sans demander de nouveau nom — contrairement à **Enregistrer sous...**. |
| **Enregistrer sous...** | Toujours | Demande un nouveau nom et enregistre une copie en tant que table globale ; si le nom existe déjà, demande confirmation avant de l'écraser. En cas de succès, il l'ajoute à la liste déroulante et le sélectionne ensuite. |
| **Restaurer les matériaux par défaut (langue)** | Uniquement avec votre propre table sélectionnée (non prédéfinie) | Remplace le contenu de la table courante par celui prédéfini de la langue de l'interface. |
| **Annuler** | Toujours | Ferme la fenêtre. |

> ⚠️ Si vous modifiez des tables dans la liste déroulante avec des modifications non enregistrées, QGISRed vous demande si vous souhaitez les enregistrer avant de les modifier (Oui/Non/Annuler). Fermer la fenêtre avec « Annuler » (ou avec le X), en revanche, ne demande rien : comme il n'y a pas de bouton final qui confirme tous les changements d'un coup (contrairement à un projet actif), seul ce que vous avez déjà enregistré explicitement avec « Enregistrer » ou « Enregistrer sous... » est conservé ici.
