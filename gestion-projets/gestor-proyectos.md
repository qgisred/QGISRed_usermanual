# Chef de projet

**Barre Générale → Gestionnaire de projet** (ou depuis le menu QGISRed → Général → Gestionnaire de projet)

Le Gestionnaire de Projet est la fenêtre d'administration centrale de QGISRed. Permet d'accéder à tous les projets connus sans avoir à se rappeler où ils sont stockés.

<figure><img src="../assets/images/general/gestor-proyectos.png" alt="Fenêtre du gestionnaire de projet QGISRed"><figcaption><p>Fenêtre du gestionnaire de projet QGISRed</p></figcaption></figure>
*Fenêtre Gestionnaire de projets : liste des projets récents et des opérations disponibles.*

---

## Liste des projets récents

La fenêtre affiche tous les projets qui ont déjà été ouverts sur cet ordinateur. Pour chaque projet, le **nom du réseau** et le **chemin du dossier** sont affichés.

- **Double-cliquez** sur n'importe quel projet → l'ouvre directement.
- S'il existe un projet ouvert avec des modifications non enregistrées, QGISRed demandera une confirmation avant de le fermer.

## Opérations disponibles

### Charger (Charger)

Permet d'ajouter à la liste un projet qui n'apparaît pas dans l'historique (par exemple, si le projet a été créé sur un autre ordinateur et que le dossier a été copié).

1. Appuyez sur **Charger**.
2. Saisissez le **nom du réseau** (pas d'extension, pas de préfixe de dossier).
3. Sélectionnez le **dossier du projet** avec l'explorateur.
4. QGISRed vérifiera que le fichier `{nombre}_Pipes.shp` existe dans ce dossier avant de l'ouvrir.

### Cloner

Créez une copie complète du projet sous un nom différent. Utile pour créer des variantes sans perdre l'original.

1. Sélectionnez le projet que vous souhaitez cloner.
2. Appuyez sur **Cloner**.
3. Saisissez le nouveau nom du réseau.
4. Choisissez le dossier de destination (il peut s'agir du même dossier si le nom est différent).

> 💡 Le clonage copie tous les fichiers et métadonnées SHP, DBF. Les résultats de simulation ne sont **pas** clonés pour économiser de l'espace.

### Exporter

Conditionne le projet sélectionné dans un ZIP portable (SHP/DBF, `.qgz` et, éventuellement, résultats, problématiques, requêtes, couches auxiliaires et données complémentaires). C'est la seule façon d'exporter un projet : il n'y a plus de bouton équivalent dans la barre **Projet**.

1. Sélectionnez le projet dans la liste (il n'est pas nécessaire de l'ouvrir dans QGIS).
2. Appuyez sur **Exporter**.
3. Complétez la boîte de dialogue d'exportation.

Voir le détail complet du dialogue, ce qui est inclus et ce qui ne l'est pas, dans [Enregistrer, exporter et fermer le projet](../projet-actif/guardar-backup.md#exportar-el-proyecto).

### Renommer

Renomme le réseau et met automatiquement à jour le nom de **tous les fichiers** du projet (SHP, DBF, PRJ, etc.). Il ne s'agit pas d'un simple changement de nom dans la liste : il déplace et renomme les fichiers sur le disque.

1. Sélectionnez le projet.
2. Appuyez sur **Renommer**.
3. Saisissez le nouveau nom.

> ⚠️ Si le projet est ouvert dans QGIS, fermez-le avant de le renommer pour empêcher QGIS de maintenir des verrous sur les fichiers.

### Supprimer de la liste (Décharger)

Supprime le projet de l'historique récent **sans supprimer les fichiers sur le disque**. Le projet existe toujours dans votre dossier et peut être rajouté avec **Upload**.

### Supprimer du disque (Supprimer)

Supprimez le projet de l'historique **et supprimez tous les fichiers du projet** du disque. Cette opération est irréversible.

> ❗ QGISRed demandera une confirmation avant de supprimer. Assurez-vous d'avoir une sauvegarde si vous devez récupérer le projet à l'avenir.

### Ouvrir le dossier

Ouvrez l'Explorateur Windows directement dans le dossier du projet sélectionné.

---

## Comment QGISRed identifie le projet actif

Lorsque vous ouvrez QGIS avec un projet `.qgz` déjà enregistré, QGISRed reconnaît automatiquement le réseau actif en recherchant les couches chargées dont une correspond à `_Pipes.shp` et possède la propriété interne `qgisred_identifier`.

Si la couche de tuyauterie est chargée mais n'a pas cet identifiant (par exemple, parce qu'elle a été ajoutée manuellement sans passer par QGISRed), le plugin vous avertira avec le message :

> _"Veuillez ouvrir le projet depuis le gestionnaire de projet QGISRed"_

Dans ce cas, fermez les calques et utilisez le Gestionnaire de projet pour ouvrir correctement le projet.
