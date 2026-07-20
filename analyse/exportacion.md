# Exportation de modèle

La barre Analyse propose deux chemins d'export : le modèle complet sous forme de fichier EPANET `.inp` et les résultats de simulation sous forme de tableaux CSV.

---

## Exporter le modèle vers INP…

**Barre d'analyse → Exporter le modèle vers INP…**

Exporte l'intégralité du modèle au format standard EPANET **INP**. Utile pour partager le modèle avec d'autres utilisateurs, l'exécuter dans l'interface graphique EPANET ou l'intégrer à des outils tiers.

<figure><img src="../assets/images/analisis/export-inp-dialog.png" alt="Boîte de dialogue Exporter au format INP"><figcaption><p>Boîte de dialogue Exporter au format INP</p></figcaption></figure>
*Boîte de dialogue Exporter vers INP : itinéraire de destination, export des données de terrain et ouverture automatique dans EPANET.*

### Options de boîte de dialogue

| Options | Descriptif |
|--------|-------------|
| **Fichier INP** | Chemin complet du fichier `.inp` à générer. Utilisez le bouton `…` pour naviguer. |
| **Exporter des fichiers de données de champ** | Exporte également les fichiers de données de champ auxiliaires associés au modèle. |
| **Ouvrir le fichier INP avec EPANET** | S'il est actif, ouvre le `.inp` dans EPANET une fois l'export terminé. |
| **Chemin Epanet** | Exécutable EPANET détecté sur le système. La liste déroulante affiche toutes les versions installées. |
| **Chemin spécifique Epanet** | Chemin manuel vers un exécutable EPANET non détecté automatiquement. |

Appuyez sur **Exporter vers INP** pour générer le fichier avec la configuration choisie.

> ℹ️ **Précision décimale selon les valeurs par défaut du projet.** Le nombre de décimales utilisé pour chaque champ dans le fichier `.inp` généré respecte la précision configurée dans les valeurs par défaut du projet, la même que celle affichée dans les panneaux Propriétés et Requêtes. Dans les versions précédentes, un format fixe de 4 à 6 décimales était appliqué quelle que soit la configuration du projet.

---

## Exporter les résultats au format CSV…

**Barre d'analyse → Exporter les résultats au format CSV…**

Exporte les résultats de la dernière simulation vers deux fichiers CSV : un pour les nœuds et un pour les canalisations. Il s'agit de la méthode standard pour obtenir des résultats dans Excel, Python, R ou d'autres outils d'analyse externes.

> Uniquement disponible si un fichier de simulation `.out` existe pour le scénario actif.

### Options de boîte de dialogue

| Options | Descriptif |
|--------|-------------|
| **Nœuds CSV** | Chemin du fichier de sortie pour les résultats de nœuds. Par défaut `{Red}_{Escenario}_Nodes.csv` dans le dossier `Results/`. |
| **Liens CSV** | Chemin du fichier de sortie pour les résultats du pipeline. Par défaut `{Red}_{Escenario}_Links.csv`. |
| **Séparateur de liste** | Séparateur de champs (détecté automatiquement depuis le système régional ; `;` commun dans les locaux européens). |
| **Séparateur décimal** | Séparateur décimal (détecté par le système ; commun `,` dans les sites européens). |

### Contenu du fichier

**Nœuds CSV** — une ligne par instant par nœud, avec des colonnes :

`Time | ID | Pressure | Head | Demand | Quality`

**Liens CSV** — une ligne par instant par tuyau/vanne/pompe, avec des colonnes :

`Time | ID | Status | Flow | Velocity | HeadLoss | UnitHdLoss | FricFactor | ReactRate | Quality`

> Les séparateurs s'adaptent aux paramètres régionaux du système d'exploitation pour que le fichier s'ouvre correctement dans Excel sans avoir besoin de conversion.
