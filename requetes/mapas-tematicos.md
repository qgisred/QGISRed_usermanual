# Cartes thématiques

**Barre de requêtes → Cartes thématiques…**

Ouvre la boîte de dialogue **Cartes thématiques**, qui génère une représentation visuelle du réseau en colorant les canalisations par intervalles de tout attribut hydraulique ou résultat de simulation.

<figure><img src="../assets/images/consultas/thematic-maps-dialog.png" alt="Boîte de dialogue Cartes thématiques avec sélecteur de champs et gamme de couleurs"><figcaption><p>Boîte de dialogue Cartes thématiques avec sélecteur de champs et gamme de couleurs</p></figcaption></figure>
*Boîte de dialogue Cartes thématiques : sélection des champs, nombre de classes et palette de couleurs.*

---

## Elément actif : tuyaux

Dans la version actuelle, **Les cartes thématiques fonctionnent exclusivement sur la couche Pipes**. Les options pour d'autres types d'éléments (nœuds, vannes, pompes, réservoirs, réservoirs) sont présentes dans l'interface mais sont automatiquement masquées car non encore implémentées. Lorsqu'elle est disponible, la boîte de dialogue affiche un sélecteur de type d'élément.

---

## Processus

1. Ouvrez les **Cartes thématiques** depuis la barre de requêtes.
2. Sélectionnez le **champ à représenter** dans le menu déroulant (attribut d'entrée ou résultat de simulation).
3. Choisissez le **nombre de classes de couleurs**.
4. Sélectionnez la **palette de couleurs** (dégradé à plage unique ou bichromatique).
5. Définissez la **plage** si vous souhaitez exclure les valeurs extrêmes.
6. Confirmez. QGISRed génère la couche `ThematicPipes` dans le groupe de couches thématiques du panneau des couches QGIS.

---

## Champs disponibles pour les tuyaux

### Attributs d'entrée du modèle

| Champ | Descriptif |
|-------|-------------|
| `Diameter` | Diamètre du tuyau (mm) |
| `Length` | Longueur (m) |
| `Roughness` | Coefficient de rugosité |
| `InstallYear` | Année d'installation |

### Résultats des simulations

Disponible uniquement si des résultats sont chargés dans le projet :

| Champ | Descriptif |
|-------|-------------|
| `Flow` | Débit (l/s ou unité configurée) |
| `Velocity` | Vitesse (m/s) |
| `HeadLoss` | Perte de charge (m) |
| `UnitHdLoss` | Perte unitaire (m/km) |
| `FricFactor` | Facteur de friction |
| `ReactRate` | Taux de réaction (modèles de qualité) |
| `Quality` | Qualité de l'eau |

---

## Résultat sur la carte

L'outil génère la couche **`ThematicPipes`** au sein d'un groupe de couches thématiques QGISRed. La légende des couleurs est affichée directement dans le panneau des couches QGIS.

Si vous exécutez à nouveau les cartes thématiques, l'ancienne couche est remplacée par les nouveaux paramètres.

---

## Notes d'utilisation

- La génération des cartes thématiques ne modifie aucune donnée du modèle ; seule la symbologie de la couche change.
- Pour revenir à la symbologie standard, supprimez la couche `ThematicPipes` du panneau des couches ou rechargez la symbologie par défaut depuis les propriétés de la couche QGIS.
- Si le projet ne dispose pas de résultats de simulation, les champs de résultats n'apparaissent pas dans la liste déroulante.
