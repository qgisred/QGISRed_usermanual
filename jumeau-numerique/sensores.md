# Capteurs et compteurs

Les compteurs et capteurs Digital Twin sont des éléments qui enregistrent des grandeurs physiques à des points spécifiques du réseau. QGISRed les stocke dans la couche complémentaire `Meters` et les utilise pour charger les données de terrain et les comparer avec les résultats de simulation.

---

## Ajouter un compteur (liste déroulante)

**Digital Twin Bar → Ajouter un compteur**

Placez un compteur ou un capteur sur une canalisation en cliquant sur le point d'installation. Le menu déroulant des boutons permet de choisir le type avant de le placer ; Le dernier type utilisé reste l'action par défaut du bouton.

<figure><img src="../assets/images/gemelo-digital/add-meter-dropdown.png" alt="Liste déroulante des types de compteurs dans la barre Digital Twin"><figcaption><p>Liste déroulante des types de compteurs dans la barre Digital Twin</p></figcaption></figure>
*Ajouter une liste déroulante de compteur : les 11 types de compteurs disponibles.*

### Types de compteurs disponibles

| Tapez | Nom sur la barre | Magnitude enregistrée |
|------|--------------------|---------------------|
| **Compteur automatique** | Ajouter un compteur automatique | Type automatiquement déterminé par le contexte |
| **Manomètre** | Ajouter un manomètre | Pression (m.c.a.) |
| **Débitmètre** | Ajouter un débitmètre | Débit (l/s ou unité configurée) |
| **Contremètre** | Ajouter un compteur | Volume accumulé (compteur d'eau) |
| **Niveau du capteur** | Ajouter un capteur de niveau | Niveau de lame libre dans le château d'eau |
| **Manomètre différentiel** | Ajouter un manomètre différentiel | Différence de pression entre deux points |
| **Capteur de qualité** | Ajouter un capteur de qualité | Concentration de chlore ou autre paramètre de qualité |
| **Capteur d'énergie** | Ajouter un capteur d'énergie | Puissance ou énergie consommée (groupes de pompage) |
| **État du capteur** | Ajouter l'état du capteur | État de fonctionnement d'une canalisation ou d'une vanne |
| **Ouverture de vanne** | Ajouter une ouverture de valve | Degré d'ouverture d'une vanne de régulation |
| **Tachymètre** | Ajouter un tachymètre | Vitesse de rotation d'une pompe (tr/min) |

### Processus

1. Choisissez le type de compteur dans le menu déroulant.
2. Cliquez sur le tuyau au point d'installation.
3. QGISRed appelle `GISRed.AddMeter` avec le type sélectionné et met à jour la couche `Meters`.

---

## Charger les relevés des compteurs…

**Digital Twin Bar → Charger les relevés du compteur…**

Importe les relevés des compteurs intelligents (smart metering) et les associe aux connexions du projet. Les lectures enrichissent les demandes du modèle avec des données de consommation réelles plutôt que des demandes estimées.

### Formats d'importation pris en charge

| Formater | Structure du fichier |
|---------|------------------------|
| **Tableau** | Première ligne : en-tête avec `Time; Id1; Id2; …`. Colonnes : un compteur par colonne. |
| **Série** | Une ligne par enregistrement : `Id; Time; Demand`. Tous les compteurs dans le même fichier. |

Les séparateurs de champs sont automatiquement détectés à partir du système régional. Le champ `Time` accepte à la fois les horodatages absolus et le décalage en heures depuis le début de la simulation.

---

## Définir l'état initial du tuyau à partir des vannes d'isolement

**Digital Twin Bar → Définir l'état initial du tuyau à partir des vannes d'isolement**

Propage l'état d'ouverture ou de fermeture des vannes de coupure de la couche `IsolationValves` au champ `InitStatus` des canalisations qui traversent chaque vanne. Ainsi, le modèle EPANET collecte l'état réel du réseau sans qu'il soit nécessaire de modifier manuellement chaque canal.

### Exigence

La couche `IsolationValves.shp` doit exister dans le répertoire du projet. S'il n'existe pas, l'outil affiche un avertissement et n'apporte aucune modification.

### Quand l'utiliser

- Avant de simuler un scénario opérationnel précis (par exemple avec un secteur fermé pour maintenance).
- Après avoir mis à jour l'état de plusieurs vannes de coupure sur la carte et avant de lancer **Run model**.

> Cette opération modifie le modèle EPANET (champ `InitStatus` de `Pipes`). Pour revenir à l'état d'origine, utilisez **Scenario builder** (barre d'outils) si vous aviez enregistré le scénario de base avant l'opération.

---

## Charger les données du champ…

**Digital Twin Bar → Charger les données du champ…**

Importe les données de terrain des systèmes SCADA ou des enregistreurs de données et les associe aux compteurs de la couche `Meters`. Les données téléchargées sont liées à chaque capteur pour une comparaison ultérieure avec les résultats de simulation.

La boîte de dialogue vous permet de sélectionner le fichier de données et de configurer le format date/heure et le séparateur de champ. QGISRed appelle `GISRed.LoadScada` et met à jour les enregistrements de la couche `Meters` avec la série chronologique importée.

### Utilisation typique

1. Exportez les données du capteur de terrain de SCADA vers un fichier CSV ou DAT.
2. Exécutez **Charger les données du champ** et sélectionnez le fichier.
3. Exécutez la simulation (**Exécuter le modèle**).
4. Comparez visuellement les valeurs mesurées (champ) et calculées (simulation) pour chaque capteur dans le dock **Séries temporelles**.
