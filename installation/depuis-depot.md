# Installation à partir du référentiel

C'est la méthode recommandée. Installez QGISRed directement depuis le référentiel officiel du plugin QGIS et permettez-vous de recevoir des mises à jour automatiques.

---

## Pas à pas

1. Ouvrez QGIS.
2. Allez dans le menu **Plugins → Gérer et installer les plugins…**
3. Dans l'onglet **Tous**, tapez `QGISRed` dans la zone de recherche.
4. Sélectionnez **QGISRed** dans la liste des résultats.
5. Cliquez sur **Installer le plug-in**.

Une fois terminé, la barre principale de QGISRed et le menu **QGISRed** apparaîtront dans la barre de menus de QGIS.

---

## Première exécution

La première fois que vous utilisez un outil de plug-in, QGISRed détecte que les **dépendances** ne sont pas installées et affiche une boîte de dialogue d'installation. Voir [Gestion des dépendances](dependances.md) pour plus de détails.

---

## Mises à jour automatiques

Au démarrage de QGIS, QGISRed vérifie si une nouvelle version est disponible. Si elle existe, la fenêtre d'actualités de QGISRed s'ouvrira automatiquement pour vous informer de la nouvelle version. Pour mettre à jour à partir de là :

1. Accédez à **Plugins → Gérer et installer les plugins…**
2. Ouvrez l'onglet **Mise à jour**.
3. Sélectionnez **QGISRed** et cliquez sur **Mettre à jour le plugin**.

> Vous pouvez également activer la mise à jour automatique dans l'onglet **Paramètres** du gestionnaire de plugins.

---

## Dépannage

**QGISRed n'apparaît pas dans les résultats de recherche**

Le gestionnaire de plugins doit avoir configuré le référentiel QGIS officiel. Allez dans **Plugins → Gérer et installer les plugins… → Paramètres** et vérifiez que le référentiel `https://plugins.qgis.org/plugins/plugins.xml` est actif.

**Le bouton "Installer le plugin" est désactivé**

Cela peut être dû au fait que la version installée de QGIS est antérieure à 3.28. Mettez d'abord à jour QGIS.
