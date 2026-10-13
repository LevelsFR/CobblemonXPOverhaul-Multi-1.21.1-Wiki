# Fiole d'XP

La **XP Flask** (`cobblemon_xp_overhaul:xp_flask`) stocke une partie de l'XP du joueur **accordée par XP Overhaul** pour la convertir ensuite en XP Pokémon.

::: warning XP vanilla
La fiole ne collecte pas l'XP du minage, des créatures habituelles ni d'autres sources non gérées par XP Overhaul.
:::

## Recette

| | | |
|:---:|:---:|:---:|
| Éclat d'améthyste | Fiole d'expérience | Éclat d'améthyste |
| Bonbon Exp. L | Multi Exp | Bonbon Exp. L |
| Lapis-lazuli | Fiole d'expérience | Lapis-lazuli |

La recette 3 × 3 est ajoutée au démarrage du serveur.

## Charger et utiliser la fiole

1. Garder la fiole dans l'inventaire ou l'équiper dans le slot facultatif **Accessories** `xp_flask`.
2. Recevoir une récompense d'XP du joueur lors d'une capture ou victoire admissible.
3. Une fraction alimente la fiole si le système est activé, le reste rejoint la barre d'expérience Minecraft.
4. Faire un clic droit avec la fiole remplie sur **son propre Pokémon invoqué**.

Une utilisation ne donne au maximum que l'XP nécessaire pour atteindre le **niveau suivant**, avant le traitement des événements Cobblemon. Le solde reste dans la fiole. Son infobulle affiche la quantité d'XP Pokémon convertible disponible.

## Conversion par défaut

| Paramètre | Défaut | Effet |
| --- | --- | --- |
| `coreCaptureRatio` | `0.25` | Redirige 25 % de l'XP admissible (arrondi inférieur) |
| `transferMultiplier` | `40.0` | Coefficient de conversion |
| `transferEfficiency` | `0.9` | Efficacité |
| `enabled` | `true` | Activation |

Le facteur de conversion effectif est **40 × 0.9 = 36** XP Pokémon par point d'XP stocké, avant les arrondis et la limitation au niveau suivant.

## Accessories et messages

Avec Accessories, la fiole équipée est recherchée **avant** celles de l'inventaire. Sans ce mod, l'inventaire fonctionne normalement.

`trainerXpCore.messageMode` accepte `ACTION_BAR`, `CHAT` et `DISABLED`. Le paramètre `showTrainerXpCoreMessages` peut également masquer les messages.

Voir les [commandes](/fr-FR/guide/commands) et l'[API](/fr-FR/guide/api).
