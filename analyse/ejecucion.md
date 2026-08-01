# Exécution et options

Les trois premières actions de la barre Analyse contrôlent le cycle de simulation : configurer les options du moteur, lancer la simulation et consulter le rapport d'état.

---

## Options d'analyse…

**Barre d'analyse → Options d'analyse…**

Ouvre la boîte de dialogue Options du moteur EPANET. Il permet de configurer tous les paramètres qui contrôlent la manière dont la simulation hydraulique et qualité est réalisée.

<figure><img src="../assets/images/analisis/analysis-options.png" alt="Boîte de dialogue Options d'analyse avec les onglets de configuration du moteur EPANET"><figcaption><p>Boîte de dialogue Options d'analyse avec les onglets de configuration du moteur EPANET</p></figcaption></figure>
*Boîte de dialogue Options d'analyse : configuration complète du moteur EPANET.*

### Paramètres configurables

| Groupe | Paramètres principaux |
|-------|------------------------|
| **Hydraulique** | Unités de débit (LPS, GPM, CMH…), formule de perte de charge (H-W / D-W / C-M), viscosité, densité |
| **Qualité** | Type d'analyse de qualité (aucun, chlore, âge de l'eau, trace de source), coefficients de réaction |
| **Horaires** | Durée totale de la simulation, pas de temps hydraulique, pas de temps qualité, étape du rapport, heure de début |
| **Énergie** | Prix ​​de l'électricité, efficacité globale des pompes |
| **Général** | Mode PDA (Pressure Dependent Analysis) : active la demande locale dépendante de la pression |

> Le tableau des matériaux du projet stocke la rugosité en unités D-W (mm). Si vous modifiez la formule hydraulique ici, QGISRed vous proposera de convertir automatiquement les coefficients de rugosité existants.

---

## Exécuter le modèle

**Barre d'analyse → Exécuter le modèle**

Lancez la simulation EPANET avec les options configurées et chargez les résultats dans le panneau des résultats.

### Processus

1. QGISRed valide le projet (couches actives, aucune couche en cours d'édition).
2. Appelez le moteur EPANET via la boîte à outils QGISRed.
3. Une fois terminé, il ouvre automatiquement le dock Résultats à droite de l'écran et charge les données calculées.
4. La carte met à jour la symbologie de la couche avec les valeurs du premier instant disponible.

Si la simulation détecte des problèmes (pressions négatives, nœuds déconnectés, pompes en cavitation), le rapport d'état les enregistre à un niveau d'avertissement.

### Options de la boîte de dialogue de progression

La boîte de dialogue de progression comprend un bouton **Pause** (icône ‖). Lorsqu'on appuie dessus, la simulation s'arrête à la fin du pas de temps en cours et l'icône se transforme en ▶. Un nouvel appui reprend l'exécution. Le bouton disparaît une fois la simulation terminée.

La boîte de dialogue inclut également la case à cocher **"Ne plus afficher cette fenêtre de progression"**. Si vous le cochez et que la simulation se termine avec succès, les exécutions suivantes lanceront directement le calcul sans afficher la boîte de dialogue.

> ⚠️ **Exception pour les grands réseaux** : si le produit (nombre de nœuds : jonctions + réservoirs + réservoirs) × (nombre d'instants de calcul = Durée / pas de temps hydraulique) dépasse **500 000**, la boîte de dialogue de progression est toujours affichée dans ce run, même si la case "Ne plus afficher cette fenêtre de progression" est cochée lors d'un run précédent. De plus, dans ce cas, la boîte elle-même est masquée dans la boîte de dialogue, puisque la préférence enregistrée reste inefficace pendant toute la durée de ce grand réseau.

> Pour réactiver la boîte de dialogue de progression sur les réseaux qui ne dépassent pas ce seuil, accédez à **Propriétés du projet** et décochez l'option *"Ne pas afficher la fenêtre de progression lors de l'exécution de la simulation"*.

> ⚠️ Lorsque la fenêtre de progression est masquée, le curseur système se transforme en curseur de veille dans toutes les applications pendant que la simulation est en cours. Le curseur est automatiquement restauré à la fin du calcul.

### Messages d'état pendant l'exécution

La boîte de dialogue de progression informe sur les différentes phases du calcul :

- **Sauvegarde des résultats…** : indique que les résultats sont en cours d'écriture sur le disque une fois le calcul hydraulique terminé.
- Si les fichiers de résultats (`.out`, `.hyd`) sont **verrouillés par une autre application** (par exemple, EPANET Desktop ouvert avec le même projet), le plugin le détecte et avertit l'utilisateur avec un avertissement spécifique.

### Gestion des erreurs

- Si EPANET renvoie une erreur lors du calcul, le contenu du rapport (`.rpt`) s'affiche automatiquement dans le journal des incidents sans qu'il soit nécessaire de le rechercher manuellement.
- Les exceptions inattendues au cours du processus sont également capturées et affichées dans le journal, évitant ainsi les échecs silencieux.

---

## Navigateur de résultats

**Barre d'analyse → Navigateur de résultats**

Ouvre le panneau des résultats si une simulation précédente existe déjà pour le projet actif, sans simuler à nouveau. S'il n'y a aucun résultat, il lance automatiquement la simulation.

C'est équivalent à **Run model** mais en priorisant les résultats déjà calculés : si le fichier `.out` existe et correspond au projet en cours, il les charge directement. Utile pour rouvrir la visionneuse après l'avoir fermée sans perdre les résultats.

---

## Rapport d'état

**Barre d'analyse → Rapport d'état**

Ouvre le panneau de résultats directement dans l'onglet **Rapport d'état**, qui affiche le rapport texte généré par le moteur EPANET à la fin de la simulation.

Le rapport comprend :

- Bilan massique général du réseau.
- Liste des nœuds à pression négative ou hors de portée.
- Avertissements de pompes fonctionnant en dehors de leur courbe.
- Statut de convergence du calcul hydraulique à chaque étape.
- Synthèse des réactions qualité (si la qualité a été simulée).

> Le rapport d'état est le premier endroit à consulter lorsqu'une simulation produit des résultats inattendus ou ne converge pas.
