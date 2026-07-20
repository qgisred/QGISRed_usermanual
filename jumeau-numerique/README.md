# 🧬Jumeau numérique

Le bus **Digital Twin** ajoute au modèle hydraulique les éléments d'infrastructure qui relient le réseau à l'utilisateur final et aux systèmes de surveillance du terrain : connexions, vannes d'arrêt, compteurs et capteurs. Ces éléments ne font pas strictement partie du modèle EPANET mais enrichissent le jumeau numérique d’informations opérationnelles et de télérelevé.

<figure><img src="../assets/images/gemelo-digital/barra-digital-twin.png" alt="Barre d'outils QGISRed Digital Twin"><figcaption><p>Barre d'outils QGISRed Digital Twin</p></figcaption></figure>
*Digital Twin Bar : connexions, vannes d'arrêt, compteurs et chargement des données de terrain.*

---

## Outils numériques à double barre

### Groupe 1 — Éléments de réseau

| # | Outil | Fonction |
|---|-------------|---------|
| 1 | **Ajouter une connexion de service** | Tracer un raccordement du tuyau principal au point d'alimentation du client |
| 2 | **Ajouter une vanne d'isolement** | Ajouter un robinet d'arrêt en cliquant sur un tuyau |
| 3 | **Ajouter un compteur** (liste déroulante) | Placez un compteur ou un capteur sur un tuyau. 11 types disponibles |

### Groupe 2 — Données opérationnelles

| # | Outil | Fonction |
|---|-------------|---------|
| 4 | **Charger les relevés des compteurs…** | Charger les relevés des compteurs intelligents et les associer aux connexions du projet |
| 5 | **Définir l'état initial du tuyau à partir des vannes d'isolement** | Propage l'état ouvert/fermé des vannes d'arrêt dans le champ `InitStatus` des canalisations concernées |
| 6 | **Charger les données du champ…** | Importer les données de terrain SCADA et les associer aux compteurs du projet |

### Groupe 3 — Intégration dans le modèle

| # | Outil | Fonction |
|---|-------------|---------|
| 7 | **Convertir les connexions de service en tuyaux/nœuds** | Convertit les connexions en nœuds ponctuels ou en tuyaux du modèle EPANET |

---

## Dans cette rubrique

* [Raccordements et vannes d'arrêt](acometidas.md) — dessin des connexions, des vannes d'arrêt et conversion au modèle hydraulique
* [Capteurs et compteurs](sensores.md) — types de compteurs, relevés de chargement et données de terrain
