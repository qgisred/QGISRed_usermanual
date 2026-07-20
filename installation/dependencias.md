#Gestion des Dépendances

QGISRed a besoin d'un ensemble de bibliothèques de calcul externes **(dépendances du plugin QGISRed)** pour pouvoir exécuter la plupart de ses outils. Ces bibliothèques sont des DLL compilées en .NET qui contiennent le moteur hydraulique (basé sur la boîte à outils EPANET 2.3) et les algorithmes de traitement géospatial.

---

## Première installation

La première fois que vous essayez d'utiliser un outil QGISRed, le plugin détecte que les dépendances ne sont pas installées et affiche une boîte de dialogue de confirmation :

<figure><img src="../assets/images/instalacion/dialogo-dependencias.png" alt="Boîte de dialogue d'installation des dépendances"><figcaption><p>QGISRed demande l'autorisation de télécharger les dépendances.</p></figcaption></figure>

- **Oui** : QGISRed télécharge et installe les bibliothèques automatiquement. Le téléchargement nécessite une connexion Internet et peut prendre quelques secondes en fonction de la vitesse de connexion.
- **Non** : L'outil ne s'exécute pas. La boîte de dialogue réapparaîtra la prochaine fois que vous essaierez d'utiliser le plugin.

> L'installation **ne nécessite pas d'autorisations d'administrateur**. Les DLL sont installées dans le dossier utilisateur `%APPDATA%\QGISRed\`, pas dans les dossiers système.

---

## Où sont-ils installés

Les dépendances sont stockées dans :

```
C:\Users\{tu_usuario}\AppData\Roaming\QGISRed\
```

Vous pouvez accéder à ce dossier en tapant `%APPDATA%\QGISRed` directement dans la barre d'adresse de l'Explorateur Windows.

---

## Mettre à jour les dépendances

Lorsqu'une nouvelle version de QGISRed est publiée et inclut une version mise à jour des dépendances, le plugin le détecte automatiquement au démarrage et propose la mise à jour avec la même boîte de dialogue de confirmation.

---

## Dépannage

**Le téléchargement échoue ou est interrompu**

Vérifiez que vous disposez d'une connexion Internet et qu'aucun pare-feu d'entreprise ne bloque le téléchargement. Si le problème persiste, contactez votre administrateur réseau pour autoriser les connexions sortantes depuis QGIS.

**Le plugin affiche la boîte de dialogue des dépendances à chaque ouverture**

Cela signifie que les bibliothèques n'ont pas été installées correctement lors des sessions précédentes. Vérifiez que le dossier `%APPDATA%\QGISRed\` existe et contient les fichiers `.dll`. S'il est vide, supprimez-le complètement et réessayez l'installation.

**L'appareil n'a pas accès à Internet**

Vous pouvez installer des dépendances hors ligne si vous disposez des fichiers nécessaires :

1. **ZIP des dépendances** : demande à quelqu'un avec le plugin déjà installé le contenu de son dossier `%APPDATA%\QGISRed\` (même version de QGISRed). Copiez ces fichiers dans votre propre dossier `%APPDATA%\QGISRed\`.
2. **Installateur .NET Framework 4.8.1** : téléchargez-le sur un autre ordinateur doté d'Internet ou demandez le MSI à quelqu'un. Exécutez-le avant d'utiliser le plugin.

Une fois les DLL copiées et avec le .NET Framework 4.8.1 installé, le plugin fonctionnera sans nécessiter de connexion Internet à aucun moment.
