# Raccordements et vannes d'arrêt

Les raccordements et les vannes de coupure sont les deux éléments qui relient le modèle hydraulique à la réalité opérationnelle du réseau : les connexions représentent la connexion individuelle avec chaque client et les vannes de coupure permettent l'isolement des secteurs à modéliser sans avoir besoin de modifier la topologie du modèle EPANET.

---

## Ajouter une connexion au service

**Digital Twin Bar → Ajouter une connexion de service**

Dessine une goutte sous forme de polyligne depuis le tuyau principal jusqu'au point de livraison du client. La connexion est stockée dans la couche complémentaire `ServiceConnections` du projet.

<figure><img src="../assets/images/gemelo-digital/add-service-connection.png" alt="Outil de dessin de connexion sur la carte"><figcaption><p>Outil de dessin de connexion sur la carte</p></figcaption></figure>
*Dessin de service : la ligne part du tuyau principal et atteint la limite du terrain du client.*

### Processus

1. Activez **Ajouter une connexion de service**. Le curseur passe en mode dessin au trait.
2. Cliquez sur le tuyau principal au point d'admission.
3. Cliquez sur les points intermédiaires du tracé si la connexion n'est pas droite.
4. Double-cliquez sur le point final (limite de tracé ou compteur) pour terminer la mise en page.
5. QGISRed appelle le moteur C# (`GISRed.AddConnection`) et met à jour la couche `ServiceConnections`.

La connexion hérite automatiquement du nœud de connexion le plus proche du réseau principal. Le champ `IsActive` de chaque connexion permet d'activer ou de désactiver l'alimentation individuellement sans supprimer l'élément.

---

## Ajouter une vanne d'isolement

**Digital Twin Bar → Ajouter une vanne d'isolement**

Ajoutez une vanne d'arrêt manuelle à un tuyau existant en cliquant dessus. Les vannes de coupure sont stockées dans la couche complémentaire `IsolationValves` et ne sont pas des éléments EPANET : elles n'apparaissent pas dans la simulation mais elles apparaissent dans l'analyse des segments isolés (**Segments isolés**, Barre d'outils).

### Processus

1. Activez **Ajouter une vanne d'isolement**.
2. Cliquez sur le tuyau à l'endroit où vous souhaitez placer la vanne.
3. QGISRed l'insère dans la couche `IsolationValves` et le représente sur la carte.

### Relation avec la simulation

Les vannes d'arrêt à elles seules ne modifient pas le modèle EPANET. Pour que son état (ouvert/fermé) affecte la simulation, utilisez l'outil **Définir l'état initial du tuyau à partir des vannes d'isolement** dans le groupe 2.

---

## Convertir les connexions de service en tuyaux/nœuds

**Digital Twin Bar → Convertir les connexions de service en tuyaux/nœuds**

Intègre les connexions tracées dans `ServiceConnections` au modèle EPANET actif. Nécessite que la couche `ServiceConnections` existe et contienne au moins une connexion.

### Options de conversion

Lorsque vous exécutez l'outil, une boîte de dialogue apparaît avec deux options :

| Options | Résultat dans le modèle |
|--------|------------------------|
| **En tant que nœuds** | Chaque connexion devient un nœud de demande ponctuel au point de connexion avec le pipeline principal. La géométrie de la connexion n'entre pas dans le modèle. |
| **Comme des tuyaux** | Chaque connexion devient un tuyau de petit diamètre qui va du nœud d'admission à un nouveau nœud final. Permet de simuler des pertes dans la connexion client. |

### Quand utiliser chaque option

- **En nœuds** : lorsque le seul intérêt est d'intégrer la demande du client dans le modèle sans simuler les pertes internes de la connexion. C'est l'option habituelle pour les réseaux de distribution à l'échelle du quartier ou de la ville.
- **En canalisations** : lorsqu'on souhaite simuler des réseaux d'abonnés avec des diamètres de raccordement réels, ou lorsque la longueur du raccordement est importante par rapport au réseau principal.

> Cette opération modifie le modèle EPANET (couche `Junctions` et/ou `Pipes`). Enregistrez le projet avant de l'exécuter si vous souhaitez conserver l'état précédent.
