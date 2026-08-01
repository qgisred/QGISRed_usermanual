# Contrôles et règles

**Barre d'édition → Champs d'édition…**

L'éditeur de contrôles définit la **logique de fonctionnement** du réseau : lorsqu'une vanne s'ouvre, lorsqu'une pompe démarre ou quelle séquence d'actions déclenche un certain état du système. EPANET prend en charge deux niveaux de contrôle de complexité différente.

<figure><img src="../assets/images/edicion/editor-controles.png" alt="Éditeur de règles et de contrôles QGISRed"><figcaption><p>Éditeur de règles et de contrôles QGISRed</p></figcaption></figure>
*Éditeur de contrôles : onglets Contrôles et Règles simples, sélecteur d'éléments et de conditions.*

---

## Contrôles simples

Un contrôle simple définit une **action unique** qui est exécutée lorsqu'une **condition unique** est remplie. Ils suffisent pour la plupart des automatisations de base.

###Structure

```
IF [elemento] [condición]  THEN [acción]
```

### Types de conditions

| Tapez | Exemple d'utilisation |
|------|---------------|
| **Niveau de réservoir** | Si le niveau du réservoir T-1 dépasse 4,5 m → fermer la pompe BM-1 |
| **Pression du nœud** | Si la pression dans J-120 descend en dessous de 10 m → ouvrir la vanne V-3 |
| **Temps de simulation** | A 6 heures de simulation → allumer la bombe BM-2 |
| **Horloge** | À 23h00 (heure d'horloge) → fermer le pipeline P-55 |

### Actions disponibles

| Actions | S'applique à |
|--------|---------|
| **OUVERT** | Tuyaux, vannes, pompes |
| **FERMÉ** | Tuyaux, vannes, pompes |
| **Paramètre = valeur** | Vannes (modifie le point de consigne de régulation) |
| **Vitesse = valeur** | Bombes (change la vitesse relative) |

### Exemple complet

```
; Arrancar bomba cuando el depósito esté bajo
IF TANK T-DEPOSITO1 LEVEL BELOW 1.5
THEN PUMP BM-ELEVADORA OPEN

; Parar bomba cuando el depósito esté lleno
IF TANK T-DEPOSITO1 LEVEL ABOVE 4.0
THEN PUMP BM-ELEVADORA CLOSED

; Encender bomba de refuerzo a hora punta
IF CLOCKTIME 7:00 AM
THEN PUMP BM-REFUERZO OPEN

IF CLOCKTIME 10:00 AM
THEN PUMP BM-REFUERZO CLOSED
```

---

## Règles de fonctionnement (Règles)

Les règles vous permettent de combiner **plusieurs conditions** avec des opérateurs logiques, ainsi que de définir des actions et des priorités alternatives. Ils sont équivalents aux `[RULES]` du fichier EPANET `.inp`.

### Structure générale

```
RULE [ID]
IF   [condición 1]
AND  [condición 2]          (opcional)
OR   [condición alternativa] (opcional)
THEN [acción principal]
ELSE [acción alternativa]   (opcional)
PRIORITY [número]           (opcional)
```

### Opérateurs logiques

| Opérateur | Utilisation |
|----------|-----|
| **ET** | Toutes les conditions doivent être remplies simultanément |
| **OU** | Il suffit que l'une des conditions soit remplie |

### PRIORITÉ

Lorsque deux règles avec des conditions contradictoires sont activées en même temps, celle avec le **numéro de priorité le plus élevé** l'emporte. La valeur par défaut est 0.

### Exemple complet

```
RULE R-01
IF   TANK T-DEP1 LEVEL BELOW 2.0
AND  PUMP BM-ELEV STATUS = CLOSED
THEN PUMP BM-ELEV OPEN
PRIORITY 2

RULE R-02
IF   NODE J-SALIDARED PRESSURE BELOW 8.0
OR   TANK T-DEP1 LEVEL BELOW 1.0
THEN PUMP BM-REFUERZO OPEN
ELSE PUMP BM-REFUERZO CLOSED
PRIORITY 1
```

---

## Édition dans QGISRed

La boîte de dialogue QGISRed présente les règles dans un format texte directement éditable, équivalent aux sections `[CONTROLS]` et `[RULES]` du fichier `.inp`. Vous pouvez :

- **Écrivez** des contrôles et des règles directement dans la zone de texte.
- **Activer ou désactiver** une règle en mettant un `;` au début (convertit la ligne en commentaire).
- **Vérifiez la syntaxe** avec le bouton de validation avant de sauvegarder.

> Les champs sont exportés exactement tels qu'ils apparaissent lors de la génération du `.inp` depuis la barre d'outils. Si la syntaxe est incorrecte, EPANET rejettera le fichier en simulation.

---

## Conseils de modélisation

- Pour un système avec pompe et réservoir, définir toujours **deux commandes par pompe** : une pour démarrer (niveau bas) et une pour arrêter (niveau haut). Sans la commande d'arrêt, la pompe fonctionne indéfiniment.
- Les contrôles simples sont traités **avant** les règles à chaque pas de temps. Si vous disposez d’un contrôle simple et d’une règle qui agissent sur le même élément, le résultat peut être contradictoire.
- L'ordre des contrôles simples **n'a pas d'importance** ; Celui des règles non plus, car la priorité les ordonne. Mais si deux règles ont la même priorité et des conditions contradictoires, le résultat est indéterminé.
- Eviter de créer des boucles de contrôle (la règle A active B, la règle B désactive A dans le même pas de temps) : EPANET risque de ne pas converger.
