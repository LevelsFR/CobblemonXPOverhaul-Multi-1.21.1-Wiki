# Guide de configuration

Le mod crée deux fichiers JSON dans `config/cobblemon_xp_overhaul/` :

| Fichier | Usage |
| --- | --- |
| `cobblemon_xp_overhaul-server.json` | XP des captures et combats, Œuf Chance, fiole d'XP |
| `cobblemon_xp_overhaul-common.json` | Messages, file d'attente Action Bar, débogage |

## Modifier les réglages

1. Démarrer une fois le jeu ou serveur pour générer les fichiers.
2. Faire une sauvegarde des deux JSON.
3. Modifier les clés voulues. JSON n'autorise ni commentaires ni virgules finales.
4. Exécuter `/cxpo reload` avec une permission de niveau 2.
5. Tester en jeu.

Une interface cliente **Cloth Config** est également prévue. En multijoueur, les réglages d'équilibrage doivent être faits dans les fichiers **du serveur**.

## Exemple : activer Exp All

Modifier la propriété `pokemon.capture.expAllEnabled` :

```json
"pokemon": {
  "capture": {
    "expAllEnabled": true,
    "expAllMultiplier": 0.35,
    "expShareBonusWithExpAllEnabled": false
  }
}
```

Il s'agit d'un extrait de l'arborescence, pas d'un fichier JSON complet.

## Exemple : XP de capture

```json
"player": {
  "capture": {
    "baseXp": 4,
    "levelMultiplier": 0.2,
    "globalMultiplier": 1.0
  }
}
```

Les paramètres invalides sont normalisés et certains anciens noms sont migrés au rechargement. En cas de JSON mal formé, des valeurs par défaut peuvent être rétablies : **gardez une sauvegarde**.

Pour diagnostiquer une formule d'XP du joueur en v2.1, utilisez `/cxpo xp explain [player]` avec les droits opérateur. Aucun nouveau paramètre JSON n'est nécessaire.

Consultez la [référence des paramètres](/fr-FR/guide/configuration-reference).
