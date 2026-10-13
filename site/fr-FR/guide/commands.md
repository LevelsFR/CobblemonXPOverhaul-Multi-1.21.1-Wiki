# Commandes et permissions

Toutes les commandes exigent la **permission 2**, généralement réservée aux opérateurs.

| Commande | Effet |
| --- | --- |
| `/cxpo reload` | Recharge les deux fichiers de configuration |
| `/cxpo flask get` | Affiche l'XP stockée dans la première fiole utilisable |
| `/cxpo flask set <amount>` | Définit une valeur d'XP stockée positive ou nulle |
| `/cxpo flask add <amount>` | Ajoute une valeur signée, sans descendre sous zéro |

L'alias complet `/cobblemonxpoverhaul` accepte les mêmes sous-commandes.

```text
/cxpo reload
/cxpo flask get
/cxpo flask set 250
/cxpo flask add -50
```

::: warning Commandes de fiole
Elles doivent être exécutées par un joueur disposant d'une fiole utilisable. Elles n'ont pas d'argument permettant de cibler la fiole d'un autre joueur et ne s'utilisent pas depuis la console comme un joueur.
:::

La fiole du slot facultatif **Accessories** est prioritaire sur les fioles de l'inventaire.

Voir la [configuration](/fr-FR/guide/configuration) et la [fiole d'XP](/fr-FR/guide/xp-flask).
