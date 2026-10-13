# Référence complète des paramètres

Les tableaux recensent les **clés JSON et valeurs par défaut de la v2.0** dans `config/cobblemon_xp_overhaul/`.

# Paramètres serveur

Fichier : `cobblemon_xp_overhaul-server.json`

## `player.capture`

| Clé JSON | Par défaut |
| --- | --- |
| `enabled` | `true` |
| `baseXp` | `4` |
| `levelMultiplier` | `0.2` |
| `globalMultiplier` | `1` |
| `luckyEggMultiplier` | `1.5` |
| `minimumLevelForRewards.enabled` | `false` |
| `minimumLevelForRewards.level` | `20` |

## `player.battle`

| Clé JSON | Par défaut |
| --- | --- |
| `luckyEggMultiplier` | `1.5` |
| `skipWildCaptureVictories` | `true` |
| `minimumLevelForRewards.enabled` | `false` |
| `minimumLevelForRewards.level` | `20` |

## `player.battle.wild`

| Clé JSON | Par défaut |
| --- | --- |
| `enabled` | `true` |
| `baseXp` | `4` |
| `levelMultiplier` | `0.17` |
| `globalMultiplier` | `1` |

## `player.battle.trainer`

| Clé JSON | Par défaut |
| --- | --- |
| `enabled` | `true` |
| `baseXp` | `5` |
| `levelMultiplier` | `0.19` |
| `globalMultiplier` | `1` |

## `player.battle.pvp`

| Clé JSON | Par défaut |
| --- | --- |
| `enabled` | `true` |
| `baseXp` | `6` |
| `levelMultiplier` | `0.21` |
| `globalMultiplier` | `1` |

## `pokemon.capture`

| Clé JSON | Par défaut |
| --- | --- |
| `enabled` | `true` |
| `baseXp` | `24` |
| `levelMultiplier` | `1.25` |
| `globalMultiplier` | `1` |
| `participantMultiplier` | `1` |
| `expShareMultiplier` | `0.5` |
| `expAllMultiplier` | `0.35` |
| `expAllEnabled` | `false` |
| `expShareBonusWithExpAllEnabled` | `false` |
| `allowCapturedPokemonWithExpAll` | `true` |
| `luckyEggMultiplier` | `1.5` |

## `luckyEgg`

| Clé JSON | Par défaut |
| --- | --- |
| `enabled` | `true` |
| `checkPlayerInventory` | `true` |
| `checkPartyHeldItemsForPlayerXp` | `true` |
| `checkPokemonHeldItems` | `true` |

## `trainerXpCore`

| Clé JSON | Par défaut |
| --- | --- |
| `enabled` | `true` |
| `coreCaptureRatio` | `0.25` |
| `transferMultiplier` | `40` |
| `transferEfficiency` | `0.9` |
| `showTrainerXpCoreMessages` | `true` |
| `messageMode` | `"ACTION_BAR"` |

## `player.capture.bonuses`

| Clé JSON | Par défaut |
| --- | --- |
| `firstSpeciesBonusEnabled` | `true` |
| `firstSpeciesMultiplier` | `1.5` |
| `repeatedSpeciesModifierEnabled` | `true` |
| `repeatedSpeciesMultiplier` | `0.75` |
| `repeatedSpeciesThreshold` | `1` |
| `shinyMultiplier` | `1` |
| `alphaMultiplier` | `1` |
| `legendaryMultiplier` | `1.2` |
| `mythicalMultiplier` | `1.2` |
| `ultraBeastMultiplier` | `1.2` |
| `specialFormMultiplier` | `1` |

## `pokemon.capture.bonuses`

| Clé JSON | Par défaut |
| --- | --- |
| `firstSpeciesBonusEnabled` | `true` |
| `firstSpeciesMultiplier` | `1.5` |
| `repeatedSpeciesModifierEnabled` | `true` |
| `repeatedSpeciesMultiplier` | `0.75` |
| `repeatedSpeciesThreshold` | `1` |
| `shinyMultiplier` | `1` |
| `alphaMultiplier` | `1` |
| `legendaryMultiplier` | `1.2` |
| `mythicalMultiplier` | `1.2` |
| `ultraBeastMultiplier` | `1.2` |
| `specialFormMultiplier` | `1` |


# Paramètres communs

Fichier : `cobblemon_xp_overhaul-common.json`

## `messages.actionBar`

| Clé JSON | Par défaut |
| --- | --- |
| `showPlayerCapture` | `true` |
| `showPlayerBattle` | `true` |
| `showPokemonCapture` | `true` |
| `showPokemonBattle` | `true` |
| `showCategoryLabels` | `false` |
| `queueEnabled` | `true` |
| `queueSpacingTicks` | `30` |

## `debug`

| Clé JSON | Par défaut |
| --- | --- |
| `enabled` | `false` |
| `logToConsole` | `true` |
| `sendToPlayer` | `false` |


## Validation et migration

- Les XP négatives et la plupart des coefficients négatifs sont ramenés à zéro.
- `luckyEggMultiplier` ne descend pas sous `1.0`, et `coreCaptureRatio` reste entre `0` et `1`.
- `queueSpacingTicks`, `repeatedSpeciesThreshold` et le niveau minimum restent supérieurs ou égaux à `1`.
- `trainerXpCore.messageMode` accepte `ACTION_BAR`, `CHAT` ou `DISABLED`.
- Les anciennes sections racines `playerCapture`, `playerBattle` et `pokemonCapture` sont migrées vers la structure actuelle.

Pour modifier ces valeurs, consultez le [guide de configuration](/fr-FR/guide/configuration).
