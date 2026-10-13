# Commandes et permissions

Toutes les commandes exigent la **permission 2**, généralement réservée aux opérateurs.

| Commande | Effet |
| --- | --- |
| `/cxpo reload` | Recharge les deux fichiers de configuration |
| `/cxpo flask get` | Affiche l'XP stockée dans la première fiole utilisable |
| `/cxpo flask set <amount>` | Définit une valeur d'XP stockée positive ou nulle |
| `/cxpo flask add <amount>` | Ajoute une valeur signée, sans descendre sous zéro |
| `/cxpo xp explain` | Explique le dernier calcul enregistré d'**XP du joueur** (capture ou victoire) |
| `/cxpo xp explain <player>` | Explique le dernier calcul d'**XP du joueur** enregistré pour le joueur en ligne ciblé |

L'alias complet `/cobblemonxpoverhaul` accepte les mêmes sous-commandes.

```text
/cxpo reload
/cxpo flask get
/cxpo flask set 250
/cxpo flask add -50
/cxpo xp explain
/cxpo xp explain Steve
```

## Détail des calculs XP (v2.1)

`xp explain` affiche le dernier calcul d'**XP du joueur** de la session serveur : source (capture, combat sauvage, dresseur ou PvP), niveaux concernés, XP de base, calcul par niveau, multiplicateurs appliqués, XP totale, XP reçue et XP redirigée vers la fiole. Les gains nuls et certaines captures ignorées sont également expliqués lorsqu'une trace existe.

Les traces sont conservées **uniquement durant la session serveur**, avec un maximum de 256 joueurs suivis en mémoire. Ce n'est ni un historique persistant, ni un outil de détail de l'XP individuelle des Pokémon. En l'absence de trace, la commande le signale.

L'argument facultatif `<player>` permet d'inspecter un joueur en ligne. Depuis la console, il faut indiquer un joueur, car la version sans argument nécessite une entité joueur.

::: warning Commandes de fiole
Elles doivent être exécutées par un joueur disposant d'une fiole utilisable. Elles n'ont pas d'argument permettant de cibler la fiole d'un autre joueur et ne s'utilisent pas depuis la console comme un joueur.
:::

La fiole du slot facultatif **Accessories** est prioritaire sur les fioles de l'inventaire.

Voir la [configuration](/fr-FR/guide/configuration) et la [fiole d'XP](/fr-FR/guide/xp-flask).
