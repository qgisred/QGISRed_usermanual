# Demandes et scénarios

Les trois outils du deuxième groupe de la barre d'outils gèrent l'affectation de la demande de masse, les scénarios de simulation et l'identification des segments d'isolement opérationnel.

---

## Générateur de demande nodale…

**Barre d'outils → Générateur de demande nodale…**

Attribuez la consommation aux nœuds du réseau en masse à partir de couches SHP externes chargées dans QGIS. Il s'agit du principal outil d'intégration des données de facturation, des recensements d'utilisateurs ou des estimations de polygones dans le modèle EPANET.

<figure><img src="../assets/images/herramientas/demand-builder.png" alt="Boîte de dialogue du générateur de demande nodale avec options de source et de méthode d'affectation"><figcaption><p>Boîte de dialogue du générateur de demande nodale avec options de source et de méthode d'affectation</p></figcaption></figure>
*Générateur de demande nodale : couches sources détectées automatiquement, configuration du champ et méthode de distribution.*

### Sources de données prises en charge

| Type de géométrie | Méthode d'affectation |
|-------------------|----------------------|
| **Points** | Chaque point est attribué au nœud le plus proche. La valeur de la demande est lue à partir d'un champ configurable dans la couche. |
| **Polygones** | La demande totale du polygone est répartie entre tous les nœuds qui en font partie. |
| **Lignes** | La demande pour chaque section est répartie entre les nœuds les plus proches le long de l'axe. |

### Processus

1. Chargez la couche SHP externe avec les données de consommation dans QGIS avant d'ouvrir le gestionnaire.
2. Activez **Générateur de demande nodale**. La boîte de dialogue détecte et répertorie automatiquement les couches externes.
3. Définissez pour chaque calque :
- **Champ Demande** : colonne avec la valeur de consommation.
- **Champ Catégorie** : pour créer plusieurs requêtes par type d'utilisateur (résidentiel, industriel, etc.).
- **Champ Modèle** : ID du modèle de demande à appliquer (facultatif).
4. Sélectionnez éventuellement des nœuds sur la carte pour limiter l'affectation à cette zone.
5. Confirmez. QGISRed écrit les valeurs dans `Junctions` ou `{Red}_MultipleDemands.shp` s'il existe des catégories.

### Restriction aux candidats sélectionnés

La boîte de dialogue propose deux options de contrainte qui peuvent être combinées :

| Options | Effet |
|--------|--------|
| **Limiter les candidats de la demande aux sélectionnés** | Seuls les **nœuds (jonctions) actuellement sélectionnés** sur la carte sont considérés comme candidats à recevoir la demande. Les autres nœuds sont ignorés même s'ils rentrent dans la zone d'influence d'un point de consommation. |
| **Limiter les candidats à la connexion de service aux sélectionnés** | Seules les connexions de service actuellement sélectionnées sur la carte sont considérées comme des points de service candidats. Utile pour réaffecter la demande à des connexions spécifiques sans affecter le reste. |

Les deux options sont indépendantes et peuvent être activées simultanément.

### Unités de demande personnalisées

Par défaut, le Builder interprète les valeurs de demande dans les unités de flux du projet. Si vos données sources utilisent des unités différentes, activez **Unités de demande personnalisées** et saisissez :

- **Étiquette des unités** : étiquette descriptive des unités sources (par exemple, `m³/mes`).
- **Facteur de conversion** : facteur multiplicateur à convertir en unités du projet (par exemple, si le projet utilise des L/s et que les données sont en m³/mois : `1000 / 86400 / 30 ≈ 0.000386`).

Le Builder applique automatiquement le facteur à toutes les valeurs de consommation avant de les affecter aux nœuds.

### Résultat sur la carte

Le calque résultant est affiché avec des couleurs par catégorie et des étiquettes avec la valeur demandée. Les nœuds sans catégorie attribuée apparaissent en orange sous le groupe **Non classé**.

> 💡 Les couches auxiliaires du Demand Builder (ConsumptionPoints, DemandLinks, Sectors...) peuvent également être créées vides depuis le Layer Manager, sans qu'il soit nécessaire de lancer au préalable une analyse (voir [Présentation et gestion des couches](../projet-actif/capas-y-leyenda.md)).

### Nettoyage du procès

Le gestionnaire permet de supprimer des demandes existantes avant d'en attribuer de nouvelles :
- **Supprimer les demandes des nœuds sélectionnés** : élimine les valeurs de `Demand` et les entrées de `MultipleDemands`.
- **Supprimer les modèles orphelins** : supprimez les modèles qui ne sont plus référencés par aucun nœud.

### Affectation de la demande à partir de la couche de segments

Lorsqu'une couche de segments (géométrie de ligne) est utilisée pour répartir les demandes à l'aide du champ `%Dem`, les enregistrements sans ce champ renseigné reçoivent automatiquement le pourcentage restant jusqu'à 100 %, réparti proportionnellement entre eux.

### Modèles par secteurs

La section Modèles de secteur vous permet d'attribuer un modèle de demande à chaque secteur du réseau. Il dispose de **deux modes exclusifs** :

| Mode | Descriptif |
|------|-------------|
| **Importer des modèles à partir d'un thème sectoriel** | Sélectionnez la couche de polygones avec les secteurs dans une liste déroulante qui répertorie les couches de polygones déjà chargées dans QGIS (ou importez-la avec le bouton `...` si elle n'est pas déjà chargée). Choisissez ensuite les champs **Sector Id (facultatif)**, **Id request pattern** et **Priority (facultatif)** parmi les combinaisons correspondantes. Le champ Sector Id est facultatif : s’il n’est pas identifié, QGISRed génère automatiquement des identifiants internes. Eventuellement, enregistrez le résultat en tant que couche interne du projet avec le bouton **Importer et enregistrer**. Une fois enregistrée, cette option est verrouillée. |
| **Utiliser des modèles d'un thème de secteur de projet** | Sélectionnez un calque de tranche déjà chargé dans le projet. Une liste s'affiche avec les secteurs et, à côté de chacun, un combo **éditable** pour choisir le motif : vous pouvez sélectionner un motif existant dans la liste ou écrire directement l'Id d'un nouveau motif. Les nœuds sans secteur sont regroupés dans un secteur supplémentaire. |

### Efficacité par secteurs

La section efficacité hydraulique par secteurs présente également **deux modes exclusifs** :

| Mode | Descriptif |
|------|-------------|
| **Importer des gains d'efficacité à partir d'un thème sectoriel** | Sélectionnez la couche de polygones avec les secteurs dans une liste déroulante qui répertorie les couches de polygones déjà chargées dans QGIS (ou importez-la avec le bouton `...`), et choisissez les champs **Id de secteur (facultatif)**, **Efficacité** et **Priorité (facultatif)**. Le champ ID de secteur est facultatif. Eventuellement, enregistrez le résultat en tant que couche interne du projet avec le bouton **Importer et enregistrer**. Une fois enregistrée, l'option d'importation est bloquée. |
| **Utiliser les gains d'efficacité d'un thème sectoriel de projet** | Sélectionnez un calque de tranche existant ; Le plugin identifie automatiquement les champs d'efficacité. |

#### Corrections d'efficacité et de modèles

Après avoir défini les efficacités par secteurs, le gestionnaire propose des options de correction supplémentaires :

- **Corriger les efficacités des catégories pour répondre à l'efficacité du secteur** : ajuste proportionnellement les efficacités de chaque catégorie de demande afin que l'efficacité résultante dans chaque secteur corresponde à l'objectif déclaré. Exclusif avec la correction vers l'efficacité globale.
- **Corriger les modèles sectoriels pour se conformer au modèle global** : après avoir attribué les modèles sectoriels, corrigez ces modèles afin que leur combinaison soit conforme au modèle global précédemment déclaré. Les options de correction sont réparties par portée de modèle (globale ou catégorie).

### Couche de connexions isolées avec demande

Lors de l'exécution de l'analyse de segments isolés ou de secteurs hydrauliques, le plugin génère une couche supplémentaire avec des **connexions qui ont une demande affectée mais appartiennent à des secteurs hydrauliques isolés** (sans alimentation). Cette couche est représentée par des marqueurs circulaires entourés de rouge et comprend les champs `Id`, `BaseDemand` et `Category`.

---

## Générateur de scénarios…

**Barre d'outils → Générateur de scénarios…**

Exportez et importez en masse les paramètres du modèle, créant des « instantanés » de l’état du réseau qui peuvent être restaurés à tout moment. C'est l'outil permettant de gérer les variantes de modèles sans dupliquer les projets.

### Paramètres gérés

| Paramètre | Descriptif |
|-----------|-------------|
| **Rugosité** | Coefficients de rugosité de tous les tuyaux |
| **StatutInit** | États d'ouverture/fermeture des canalisations et vannes |
| **Demandes** | Exigences de base de tous les nœuds |
| **InitQualité** | Qualités initiales des nœuds et des canalisations |
| **Élévations** | Niveaux de nœuds, châteaux d'eau et réservoirs |

### Flux de travail typique

1. Construisez le modèle dans l’état actuel (année de base).
2. Exportez le scénario de base avec **Scenario Builder → Export**.
3. Modifier le modèle pour l'horizon futur (nouvelles demandes, canalisations vieillissantes, etc.).
4. Exportez le scénario futur sous un autre nom.
5. Pour comparer ou restaurer, utilisez **Scenario Builder → Import** et sélectionnez le scénario souhaité.

Les fichiers de scénario sont enregistrés au format CSV dans le dossier du projet.

---

## Segments isolés…

**Barre d'outils → Segments isolés…**

Répond à la question opérationnelle : **"Quelles vannes dois-je fermer pour réparer ce pipeline et quels utilisateurs seront laissés sans service ?"**

<figure><img src="../assets/images/herramientas/isolated-segments.png" alt="Résultat des segments isolés : canalisation concernée, vannes d'arrêt et zone sans service"><figcaption><p>Résultat des segments isolés : canalisation concernée, vannes d'arrêt et zone sans service</p></figcaption></figure>
*En rouge le tuyau à réparer, en jaune les vannes à fermer et en bleu la zone sans service.*

### Processus

1. Activez l'outil et cliquez sur la canalisation à réparer ou à isoler.
2. QGISRed calcule le **segment minimum** qui serait isolé lors de la fermeture des vannes manuelles les plus proches et identifie les garanties affectées.
3. Le résultat s'affiche sur la carte :
- **Tuyau cible** : en rouge.
- **Valves à fermer** : en jaune.
- **Zone sans service** (personnes concernées collatéralement) : en bleu.
4. Vous pouvez cliquer sur plusieurs tuyaux au sein de la même session pour accumuler l'analyse.

La couche auxiliaire `IsolatedSegments` est générée avec toutes les informations. Ne modifie pas le modèle.
