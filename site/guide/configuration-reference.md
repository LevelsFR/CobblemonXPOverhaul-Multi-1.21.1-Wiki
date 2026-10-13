# Full configuration reference

This page lists exact **v2.0 JSON keys and defaults**. Files are located in `config/cobblemon_xp_overhaul/`.

# Server settings

File: `cobblemon_xp_overhaul-server.json`

## `player.capture`

| JSON key | Default |
| --- | --- |
| `enabled` | `true` |
| `baseXp` | `4` |
| `levelMultiplier` | `0.2` |
| `globalMultiplier` | `1` |
| `luckyEggMultiplier` | `1.5` |
| `minimumLevelForRewards.enabled` | `false` |
| `minimumLevelForRewards.level` | `20` |

## `player.battle`

| JSON key | Default |
| --- | --- |
| `luckyEggMultiplier` | `1.5` |
| `skipWildCaptureVictories` | `true` |
| `minimumLevelForRewards.enabled` | `false` |
| `minimumLevelForRewards.level` | `20` |

## `player.battle.wild`

| JSON key | Default |
| --- | --- |
| `enabled` | `true` |
| `baseXp` | `4` |
| `levelMultiplier` | `0.17` |
| `globalMultiplier` | `1` |

## `player.battle.trainer`

| JSON key | Default |
| --- | --- |
| `enabled` | `true` |
| `baseXp` | `5` |
| `levelMultiplier` | `0.19` |
| `globalMultiplier` | `1` |

## `player.battle.pvp`

| JSON key | Default |
| --- | --- |
| `enabled` | `true` |
| `baseXp` | `6` |
| `levelMultiplier` | `0.21` |
| `globalMultiplier` | `1` |

## `pokemon.capture`

| JSON key | Default |
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

| JSON key | Default |
| --- | --- |
| `enabled` | `true` |
| `checkPlayerInventory` | `true` |
| `checkPartyHeldItemsForPlayerXp` | `true` |
| `checkPokemonHeldItems` | `true` |

## `trainerXpCore`

| JSON key | Default |
| --- | --- |
| `enabled` | `true` |
| `coreCaptureRatio` | `0.25` |
| `transferMultiplier` | `40` |
| `transferEfficiency` | `0.9` |
| `showTrainerXpCoreMessages` | `true` |
| `messageMode` | `"ACTION_BAR"` |

## `player.capture.bonuses`

| JSON key | Default |
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

| JSON key | Default |
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


# Common settings

File: `cobblemon_xp_overhaul-common.json`

## `messages.actionBar`

| JSON key | Default |
| --- | --- |
| `showPlayerCapture` | `true` |
| `showPlayerBattle` | `true` |
| `showPokemonCapture` | `true` |
| `showPokemonBattle` | `true` |
| `showCategoryLabels` | `false` |
| `queueEnabled` | `true` |
| `queueSpacingTicks` | `30` |

## `debug`

| JSON key | Default |
| --- | --- |
| `enabled` | `false` |
| `logToConsole` | `true` |
| `sendToPlayer` | `false` |


## Validation and migration

- Negative XP values and most negative multipliers are clamped to zero.
- `luckyEggMultiplier` is at least `1.0`; `coreCaptureRatio` is between `0` and `1`.
- `queueSpacingTicks`, `repeatedSpeciesThreshold`, and minimum reward level are at least `1`.
- `trainerXpCore.messageMode`: `ACTION_BAR`, `CHAT`, `DISABLED`.
- Legacy root sections `playerCapture`, `playerBattle`, `pokemonCapture` are migrated to nested structures.

Learn how to edit safely in the [configuration guide](/guide/configuration).
