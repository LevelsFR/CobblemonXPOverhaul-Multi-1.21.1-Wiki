# FAQ et dépannage

## Pourquoi ma fiole reste-t-elle vide ?

Elle collecte uniquement l'XP du joueur **donnée par XP Overhaul**, pas celle du minage ou des créatures vanilla. Gardez-la dans l'inventaire ou dans le slot Accessories compatible, puis vérifiez `trainerXpCore.enabled=true` et `coreCaptureRatio>0`.

## Pourquoi toute mon équipe ne reçoit-elle pas d'XP ?

Vérifiez `pokemon.capture.enabled`, la participation, le Multi Exp et `expAllEnabled` (**désactivé par défaut**). Les règles normales de Cobblemon s'appliquent aussi.

## Pourquoi les captures Shiny ou Alpha ne donnent-elles pas plus d'XP ?

Les multiplicateurs `shinyMultiplier` et `alphaMultiplier` valent tous deux `1.0` par défaut.

## Pourquoi la commande reload ne fonctionne-t-elle pas ?

`/cxpo reload` nécessite la **permission 2**.

## Pourquoi reste-t-il de l'XP dans la fiole ?

Chaque usage est plafonné à l'XP requise pour atteindre le prochain niveau, avant les événements Cobblemon.

## Pourquoi mes réglages reviennent-ils aux valeurs par défaut ?

Un JSON invalide peut déclencher l'application de valeurs sécurisées. Consultez les logs et restaurez une sauvegarde. `debug.enabled` peut aider au diagnostic.

## Peut-on utiliser la fiole avec les Pokémon du PC ?

Une autre extension peut employer l'[API de fiole](/fr-FR/guide/api) sur les objets Pokémon serveur du PC ou de l'équipe. Cela n'ajoute pas, à lui seul, de bouton à l'interface PC.

## Où sont les fichiers de configuration ?

Dans `config/cobblemon_xp_overhaul/`, sous forme de deux JSON. Voir la [configuration](/fr-FR/guide/configuration).
