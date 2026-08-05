# Résumé de la barre d'outils

Un aperçu de tout ce que QGISRed peut faire, organisé par barre d'outils.

---

## 🗂️ Général — Gestion de projet

Point d'entrée pour toute séance de travail. De là, vous créez, ouvrez ou importez des projets.

| Outil | Qu'est-ce que ça fait |
|-------------|----------|
| **Chef de projet** | Liste des projets récents, cloner, renommer, supprimer |
| **Ouvrir le projet** | Ouvrir un projet existant en indiquant le nom et le dossier |
| **Créer un projet** | Générer la structure de fichiers SHP pour un nouveau réseau |
| **Importer un projet** | Créer un projet à partir d'un fichier EPANET `.inp` ou de SHP externes |

---

## 📋 Projet — Paramètres et calques

Outils de gestion de projet ouverts.

| Outil | Qu'est-ce que ça fait |
|-------------|----------|
| **Résumé** | Affiche le nombre d'éléments de chaque type dans le réseau |
| **Ajouter des données par importation** | Importer des éléments supplémentaires dans le projet déjà ouvert |
| **Gestionnaire de calques** | Contrôle quels calques sont actifs ; récupérer des calques supprimés accidentellement |
| **Éditeur de légende** | Personnaliser la symbologie de n'importe quelle couche du projet |
| **Options du projet** | Configurer les options EPANET : unités, formule de perte, qualité |
| **Valeurs par défaut** | Définit les préfixes ID, les tolérances géométriques et les valeurs hydrauliques initiales |
| **Tableau des matériaux** | Gérer la liste des matériaux avec leurs rugosités initiales et leurs incréments d'âge |
| **Enregistrer la carte** | Enregistrez le projet QGIS (`.qgz`) |
| **Fermer le projet** | Fermer le projet en cours |

> 💡 L'export du projet (ZIP portable) ne se fait plus dans cette barre : il se fait depuis le bouton **Export** du Chef de Projet (voir [Enregistrer, exporter et fermer le projet](../projet-actif/enregistrer-exporter-fermer.md)).

---

## ✏️ Edition — Création et édition du réseau

Outils pour dessiner et modifier la topologie du réseau directement sur la carte.

| Outil | Qu'est-ce que ça fait |
|-------------|----------|
| **Ajouter un tuyau** | Dessinez un tuyau; crée automatiquement des nœuds extrêmes |
| **Ajouter un réservoir** | Convertir un nœud existant en Tank |
| **Ajouter une bâche** | Convertit un nœud existant en bâche (Reservoir) |
| **Insérer la valve** | Fendre un tuyau et insérer une vanne |
| **Insérer une bombe** | Fendre un tuyau et insérer une pompe |
| **Sélectionner des éléments** | Sélection multiple de nœuds et de lignes |
| **Déplacer les nœuds** | Déplacez un nœud en le faisant glisser ; maintient la connectivité |
| **Modifier les sommets** | Ajouter, déplacer ou supprimer des sommets intermédiaires d'un tuyau |
| **Lien inverse** | Modifier le sens d'écoulement de référence dans les conduites/vannes/pompes |
| **Diviser/Joindre des tuyaux** | Diviser un tuyau en un point ou joindre deux tuyaux consécutifs |
| ** Diviser / Fusionner les nœuds ** | Séparez un nœud en deux ou fusionnez les nœuds qui se chevauchent |
| **Créer/Rétablir T** | Créer ou rompre une connexion en T sur un tuyau existant |
| **Créer/Rétablir un croisement** | Gérer les croisements entre des canalisations se chevauchant géographiquement |
| **Déplacer la vanne / la pompe** | Repositionner une vanne ou une pompe sur un autre tuyau |
| **Changer de statut** | Modifie l'état initial (Ouvert/Fermé/CV) des canalisations, vannes et pompes |
| **Supprimer des éléments** | Supprimer les éléments sélectionnés et reconstruire la connectivité |
| **Modifier les propriétés** | Ouvrir le formulaire des attributs d'un élément |
| **Modulations et courbes** | Gérer les courbes de demande, de rendement et de débit |
| **Contrôles et règles** | Définir des contrôles simples et des règles basées sur des conditions |

---

## 🐛 Debug — Vérification et débogage

Outils pour garantir l’intégrité topologique et attributaire du modèle.

| Outil | Qu'est-ce que ça fait |
|-------------|----------|
| **Consolider et examiner les données** | Vérifier et consolider tous les attributs ; génère un rapport d'incident |
| **Supprimer les éléments qui se chevauchent** | Détecter et supprimer les tuyaux ou nœuds en double dans la même position |
| **Simplifier les sommets des liens** | Élimine les sommets redondants dans les sections droites |
| **Rejoignez des tuyaux consécutifs** | Fusionne les tuyaux adjacents de même diamètre, matériau et année d'installation |
| **Créer des connexions T** | Créez des nœuds de connexion là où les tuyaux se croisent sans nœud commun |
| **Vérifier la connectivité** | Analyser la connectivité réseau et identifier les zones isolées |
| **Éliminer les zones isolées** | Supprime les sous-zones sans connexion à aucune source de pression |
| **Vérifier les longueurs** | Détecte les canalisations trop courtes ou trop longues par rapport aux seuils définis |
| **Vérifier les diamètres** | Vérifiez que les diamètres se situent dans les plages valides |
| **Vérifier les matériaux** | Détecte les tuyaux sans matériau attribué |
| **Vérifiez les dates** | Vérifier la cohérence des dates d'installation |
| **Secteurs hydrauliques** | Calcule et visualise les secteurs du réseau (H-Q, H-nQ, nH-Q, nH-nQ) en fonction de leur relation avec les sources et les nœuds de demande |

---

## 🔧 Outils — Outils de calcul

Utilitaires pour automatiser les tâches de préparation et de gestion des modèles.

| Outil | Qu'est-ce que ça fait |
|-------------|----------|
| **Calculer les longueurs** | Recalculer les longueurs des canalisations à partir de leur géométrie |
| **Interpoler les dimensions** | Attribue des dimensions aux nœuds à partir d'un MDT au format `.asc` |
| **Attribuer la rugosité** | Calculer le coefficient de rugosité en fonction du matériau et de l'âge |
| **Convertir la rugosité** | Transformez les coefficients de rugosité entre les formules (D-W ↔ H-W ↔ C-M) |
| **Constructeur de demandes nodales** | Répartir les consommations entre nœuds à partir de polygones surfaciques ou de points géoréférencés |
| **Constructeur de scénarios** | Exportez et importez les paramètres du modèle (rugosités, exigences, dimensions, états, qualités) en masse pour gérer les variantes sans dupliquer les projets |
| **Segments isolés** | Calculer les segments qui seraient isolés lorsque chaque vanne d'arrêt est fermée |
| **Secteurs de demande** | Génère des secteurs en fonction de la demande et des courbes de modulation de consommation |
| **Arbre à coût minimum** | Calcule l'arbre couvrant de la résistance hydraulique minimale à partir d'un nœud source sélectionné |

---

## 🔍 Requêtes — Consultations

Modélisez des outils de requête et d’inspection sans modifier ses données.

| Outil | Qu'est-ce que ça fait |
|-------------|----------|
| **Rechercher un article par ID** | Localisez et sélectionnez n'importe quel élément en fonction de son identifiant |
| **Propriétés des éléments** | Affiche toutes les propriétés d'un élément lorsque vous cliquez dessus |
| **Cartes thématiques** | Générer des couches d'affichage thématiques par n'importe quel attribut numérique |
| **Enquêtes immobilières** | Filtre les éléments qui remplissent les conditions sur leurs attributs |
| **Statistiques** | Calcule les statistiques descriptives de n'importe quel champ numérique |

---

## 📊 Analyse — Simulation et résultats

Des outils pour exécuter une simulation hydraulique et explorer les résultats.

| Outil | Qu'est-ce que ça fait |
|-------------|----------|
| **Exécuter le modèle** | Lancer la simulation EPANET et charger les résultats sous forme de couches |
| **Visionneuse de résultats** | Ouvrez le panneau latéral pour explorer les variables au fil du temps |
| **Rapport de situation** | Affiche le rapport texte généré par EPANET |
| **Options d'analyse** | Configurer l'hydraulique, la qualité, les délais et l'énergie |
| **Séries chronologiques** | Représente graphiquement l'évolution temporelle d'un élément |
| **Exporter les résultats** | Exporter tous les résultats vers des fichiers CSV |
| **Exporter vers INP** | Génère un fichier `.inp` compatible EPANET |

---

## 🧬 Jumeau numérique — Jumeau numérique

Éléments avancés pour représenter la véritable infrastructure réseau.

| Outil | Qu'est-ce que ça fait |
|-------------|----------|
| **Ajouter une connexion** | Créer une connexion de service du réseau vers un point de consommation |
| **Ajouter une vanne d'arrêt** | Incorpore des vannes de sectionnement manuelles au réseau |
| **Ajouter un compteur** (sous-menu) | Ajoutez différents types de capteurs : débitmètre, manomètre, compteur, niveau, qualité, énergie, état, ouverture, tachymètre |
| **Charger les lectures** | Importer des lectures réelles de capteurs pour l'étalonnage ou la comparaison |
| **État initial des vannes** | Applique l'état réel des vannes d'arrêt comme état initial du modèle |
| **Charger les données du champ** | Importer des données géoréférencées à partir de campagnes de capacité |
| **Convertir les connexions** | Transformer les connexions en tuyaux et nœuds de demande du modèle |
