# Cobblemon XP Overhaul

Un système d'XP unifié et configurable pour les joueurs et leurs Pokémon : captures, combats et entraînement.

::: info Documentation de la v2.1
Ce wiki décrit le **code v2.1** pour **Minecraft 1.21.1**, **Fabric et NeoForge**. Vérifiez les versions effectivement publiées sur [CurseForge](https://www.curseforge.com/minecraft/mc-mods/cobblemon-xp-overhaul) ou [Modrinth](https://modrinth.com/mod/cobblemon-xp-overhaul).
:::

## À quoi sert le mod ?

Cobblemon XP Overhaul réunit la progression XP dans un même système, avec des récompenses configurables et des mécanismes d'entraînement.

- XP du joueur après les captures et les victoires contre des Pokémon sauvages, des dresseurs PNJ ou d'autres joueurs.
- XP Pokémon lors des captures et des K.O. en combat de dresseur.
- Interactions configurables entre Exp All et Multi Exp.
- Bonus Œuf Chance, première capture, captures répétées, Shiny, Alpha et Pokémon rares.
- Fiole d'XP permettant de stocker une partie des récompenses du mod pour entraîner un Pokémon.
- Aperçu d'un transfert avec **Shift + clic droit** (v2.1).
- Diagnostic administrateur avec `/cxpo xp explain [player]` (v2.1).
- Wiki anglais et français et traductions en jeu enrichies.

## Prérequis

| Composant | Version |
| --- | --- |
| Minecraft | 1.21.1 |
| Cobblemon XP Overhaul | Documentation v2.1 |
| Cobblemon | 1.8.2 minimum, inférieur à 1.9.0 |
| OS Cobblemon Library | 1.3.0 minimum — **obligatoire** |
| Fabric | Fabric Loader 0.17.2+, Fabric API, Fabric Language Kotlin, Cloth Config |
| NeoForge | 21.1.182+, Cloth Config pour l'interface cliente |
| Java | 21 |

## Fonctionnement de l'XP

1. **Capturer ou combattre** — un événement génère une récompense.
2. **Calculer** — les niveaux, bonus et réglages déterminent l'XP.
3. **Répartir** — une fraction de l'XP du joueur peut rejoindre la fiole.
4. **Entraîner** — utiliser la fiole sur un Pokémon possédé, après aperçu si besoin.

L'Exp All des captures est désactivé par défaut. La fiole ne collecte pas l'XP vanilla. Voir la [progression](/fr-FR/guide/progression), la [fiole d'XP](/fr-FR/guide/xp-flask) et les [commandes](/fr-FR/guide/commands).
