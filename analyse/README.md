# 🧪Analyse

La barre **Analyse** regroupe les outils de simulation hydraulique, de visualisation des résultats et d'export du modèle. C'est la barre qui clôture le cycle de travail : une fois le modèle défini, vérifié et calibré, cette barre permet de lancer EPANET, d'explorer les résultats sur la carte et d'exporter vers d'autres formats.

> Avant de simuler il est conseillé d'avoir passé le [vérifications de topologie et d'attributs](../debug/README.md) pour éviter les erreurs de convergence.

<figure><img src="../assets/images/analisis/barra-analysis.png" alt="Barre d'outils d'analyse QGISRed"><figcaption><p>Barre d'outils d'analyse QGISRed</p></figcaption></figure>
*Barre d'analyse : simulation, visionneuse de résultats, séries temporelles et export.*

---

## Outils de la barre d'analyse

| # | Outil | Fonction |
|---|-------------|---------|
| 1 | **Exécuter le modèle** | Exécutez la simulation EPANET et chargez les résultats dans la carte |
| — | **Navigateur de résultats** | Ouvrez le panneau de résultats avec les données de la dernière simulation |
| — | **Rapport de situation** | Ouvrez le panneau des résultats dans l'onglet Rapport d'état |
| 2 | **Options d'analyse…** | Configurer les paramètres du moteur EPANET (unités, formule, temps, qualité) |
| 3 | **Séries chronologiques…** | Activer l'outil de graphiques d'évolution temporelle par élément |
| 4 | **Exporter les résultats au format CSV…** | Exporter les résultats de simulation vers des fichiers CSV séparés pour les nœuds et les tuyaux |
| 5 | **Exporter le modèle vers INP…** | Exporter le modèle complet vers EPANET `.inp` |

*Exécuter le modèle, le navigateur de résultats et le rapport d'état partagent un bouton déroulant dans la barre.*

---

## Dans cette rubrique

* [Exécution et options](ejecucion.md) — simulation, options du moteur et accès au rapport d'état
* [Visionneuse de résultats](resultados.md) — panneau de résultats, navigation temporelle et séries chronologiques
* [Exportation de modèle](exportacion.md) — exportation vers INP et CSV des résultats
