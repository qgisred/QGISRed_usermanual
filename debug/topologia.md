# Topologie et connectivité

Les outils du premier groupe de la barre de débogage détectent et corrigent les erreurs structurelles les plus courantes : éléments en double, sommets inutiles, tuyaux fragmentés et zones déconnectées. Il est conseillé de les exécuter dans l'ordre dans lequel ils apparaissent sur la barre avant de simuler pour la première fois.

---

## Vérifier et valider les données

**Barre de débogage → Vérifier et valider les données**

C'est le principal outil de validation. Il parcourt tous les éléments du projet, vérifie la cohérence des données (dimensions, diamètres, identifiants en double, références à des courbes et motifs inexistants, etc.) et **consolide les modifications en attente**.

### Qu'est-ce qui est valide

- ID en double sur n'importe quelle couche.
- Tuyaux sans nœuds d'extrémité valides (connectivité rompue).
- Références à des courbes ou des motifs qui n'existent pas dans le projet.
- Valeurs obligatoires vides (diamètre nul, dimension vide...).
- Cohérence interne du fichier `_Options.dbf`.

### Résultat

- Si tout est valide : message _"Les données d'entrée sont valides"_ en vert.
- S'il y a des erreurs : liste des problèmes avec l'ID et le type de l'élément concerné. Les éléments comportant des erreurs sont automatiquement sélectionnés sur la carte pour les rendre plus faciles à localiser.

> Exécutez **Check && commit data** chaque fois que vous avez modifié la table attributaire manuellement (en dehors de la boîte de dialogue des propriétés), car ces modifications ne passent pas par la validation automatique du plugin.

---

## Supprimer les éléments qui se chevauchent

**Barre de débogage → Supprimer les éléments qui se chevauchent**

Détecte les éléments qui partagent exactement la même position géographique : nœuds sur nœuds, canalisations sur canalisations ou nœuds à l'extrémité d'une autre couche.

### Lorsque des doublons apparaissent

- Lors d'un import depuis un `.inp` avec des coordonnées arrondies.
- Lors de la combinaison de données provenant de différentes sources SIG.
- Lors d'un copier-coller d'éléments sans vérifier le chevauchement.

### Opération

L'outil fonctionne sur la sélection en cours ou sur l'ensemble du réseau s'il n'y a pas de sélection. Élimine l'élément en double, en gardant celui avec le plus de connexions ou, en cas d'égalité, celui avec l'ID le plus bas. Les attributs de l'élément supprimé sont ignorés.

> Exécutez cet outil **avant de créer des connexions T** et **avant de vérifier la connectivité** pour éviter les faux positifs de connectivité causés par des nœuds en double.

---

## Simplifier les sommets des liens

**Barre de débogage → Simplifier les sommets des liens**

Supprime les sommets intermédiaires alignés (dans un seuil de tolérance angulaire) avec les segments adjacents. Ces sommets ne fournissent pas d'informations géométriques mais augmentent la taille du SHP et ralentissent le rendu.

### Quand est-ce utile

- Après importation depuis AutoCAD ou un SIG municipal où les lignes ont des sommets tous les quelques centimètres.
- Après avoir utilisé des outils de lissage externes qui ajoutent des points inutiles.

### Ce qui préserve

Les sommets aux points de rupture réels (changement de direction) ne sont pas supprimés. Seuls ceux qui tombent sur le prolongement du segment antérieur, dans l’angle de tolérance interne du plugin, sont éliminés.

---

## Rejoindre des tuyaux consécutifs

**Barre de débogage → Joindre des tuyaux consécutifs (= diamètre, matériau et année)**

Fusionnez les tuyaux adjacents lorsqu'ils partagent **les trois attributs** : diamètre, matériau et année d'installation. Le nœud intermédiaire est supprimé s'il n'est pas demandé ou connecté à d'autres couches.

### Résultat

Les canalisations précédemment fragmentées (par importation depuis le SIG, par divisions précédentes ou par conception incrémentielle) sont fusionnées en une seule section. Ceci :
- Réduit le nombre d'éléments dans le modèle.
- Simplifie la table attributaire.
- Améliore les performances de simulation.

> Si le nœud intermédiaire a une demande attribuée non nulle, le pipeline n'est **pas** fusionné. QGISRed préserve le nœud afin de ne pas perdre les données de consommation.

---

## Créer des connexions T

**Barre de débogage → Créer des connexions T**

Détecte automatiquement les situations dans lesquelles l'extrémité d'un tuyau (ou un nœud de demande) tombe sur le tracé d'un autre tuyau, sans y être connecté. Dans ces cas, le plugin divise le canal et crée le nœud de jonction.

### Problème résolu

Lors de la numérisation manuelle des réseaux, il est courant qu'une branche reste « flottante » au-dessus de la branche principale sans connexion topologique. Visuellement, cela semble correct, mais dans la simulation, cette branche n'a pas de véritable connexion. Cet outil le détecte et le corrige automatiquement.

### Tolérance

Utilise la tolérance de nœud configurée dans **Barre de projet → Valeurs par défaut**. Si l’extrémité du tuyau est inférieure à cette distance de l’axe d’un autre tuyau, elle est considérée comme un té à résoudre.

---

## Vérifier la connectivité

**Barre de débogage → Vérifier la connectivité** *(avec la sous-option Supprimer les sous-zones isolées)*

Analyse la connectivité de l'ensemble du réseau à partir des sources d'approvisionnement (Réservoirs et Réservoirs). Identifiez quels tuyaux et nœuds ne sont **connectés** à aucune source.

<figure><img src="../assets/images/debug/check-connectivity.png" alt="Résultat de la vérification de la connectivité : zones isolées colorées en rouge sur la carte"><figcaption><p>Résultat de la vérification de la connectivité : zones isolées colorées en rouge sur la carte</p></figcaption></figure>
*Zones isolées identifiées : en rouge les éléments sans connexion à aucune source.*

### Option 1 : Vérifier la connectivité (affichage uniquement)

Colorez les éléments en fonction de leur zone de connectivité. Les éléments non connectés à aucune source sont mis en surbrillance. Cela ne modifie pas le réseau.

### Option 2 : Supprimer les sous-zones isolées

Ouvre une boîte de dialogue demandant le **nombre maximum de canalisations** dans une sous-zone à supprimer. Les sous-zones comportant ce nombre de canalisations ou moins sont automatiquement supprimées. Les plus grands sont conservés même s'ils sont isolés (il peut s'agir de secteurs valides non encore connectés).

Ce seuil est utile pour nettoyer les « déchets » topologiques – des fragments de 1 à 3 tuyaux laissés en vrac après une importation.

> Exécutez toujours **Supprimez les éléments qui se chevauchent** avant de **Vérifier la connectivité** pour éviter que les nœuds en double ne génèrent de fausses isolations.
