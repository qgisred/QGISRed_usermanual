# Configuration système requise

Avant d'installer QGISRed, vérifiez que votre ordinateur répond aux exigences suivantes.

---

## Système d'exploitation

**Windows 10 ou version ultérieure (x64)**.

QGISRed n'est pas disponible pour Linux ou macOS. Le moteur de calcul utilise des DLL compilées en .NET qui nécessitent l'environnement Windows.

---

##QGIS

**Version 3.28 ou supérieure**, y compris la série 4.x.

### Comment vérifier votre version de QGIS

Accédez à **Aide → À propos de QGIS**. La version apparaît dans la première ligne du dialogue.

Si votre version est antérieure à la 3.28, téléchargez la dernière version LTR (Long Term Release) depuis [qgis.org](https://qgis.org/download/).

> Les versions antérieures à 3.28 ne sont plus supportées par le plugin depuis QGISRed 0.18. Si vous devez travailler avec une ancienne version de QGIS, utilisez QGISRed 0.17 ou une version antérieure.

---

## .NET Framework

**Version 4.8.1**.

### Comment vérifier s'il est installé

1. Ouvrez **Panneau de configuration → Programmes → Programmes et fonctionnalités**.
2. Cliquez sur **Activer ou désactiver des fonctionnalités Windows**.
3. Recherchez **.NET Framework 4.8.1** dans la liste. S'il apparaît coché, il est déjà installé.

Sous Windows 11 et les versions récentes de Windows 10, .NET Framework 4.8.1 peut être préinstallé. Sur les anciennes versions ou sur Windows Server, vous devrez peut-être le télécharger et l'installer manuellement depuis Microsoft.

---

## Connexion Internet

Nécessaire **à la première utilisation** du plugin, pour télécharger les dépendances (les DLL du moteur de calcul). Les téléchargements ultérieurs (mises à jour du plugin) nécessitent également une connexion.

Une fois les dépendances installées, QGISRed peut fonctionner **sans connexion internet**.

> Si vous n'avez pas de connexion internet, vous pouvez installer les dépendances manuellement : demandez à quelqu'un de vous fournir le ZIP des dépendances et l'installateur MSI du .NET Framework 4.8.1. Avec les deux fichiers, vous pourrez terminer l'installation sans avoir besoin de connexion. Voir la section [Gestion des dépendances](dependencias.md) pour plus de détails.
