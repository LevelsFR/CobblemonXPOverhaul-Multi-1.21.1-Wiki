# Cobblemon XP Overhaul

A unified, configurable XP progression system for Minecraft players and Pokémon, covering captures, battles and team training.

::: info Documentation for v2.1
This wiki documents the **v2.1 codebase** for **Minecraft 1.21.1**, **Fabric and NeoForge**. Check [CurseForge](https://www.curseforge.com/minecraft/mc-mods/cobblemon-xp-overhaul) or [Modrinth](https://modrinth.com/mod/cobblemon-xp-overhaul) for the currently published builds.
:::

## What does the mod do?

Cobblemon XP Overhaul replaces the need for several overlapping XP systems with customizable rules for player progression and Pokémon training.

- Player XP for Pokémon captures and wins against wild Pokémon, NPC trainers and other players.
- Pokémon XP for captures and trainer-battle knockouts.
- Optional Exp All and Exp Share interactions.
- Lucky Egg, first-species, repeated-capture, Shiny, Alpha and rare Pokémon modifiers.
- The XP Flask stores a portion of the mod's player XP rewards for later Pokémon training.
- XP Flask preview using **sneak + right-click** (v2.1).
- Admin XP diagnostics using `/cxpo xp explain [player]` (v2.1).
- English and French wiki; expanded in-game translations.

## Requirements

| Component | Version |
| --- | --- |
| Minecraft | 1.21.1 |
| Cobblemon XP Overhaul | v2.1 documentation |
| Cobblemon | 1.8.2 to below 1.9.0 |
| OS Cobblemon Library | 1.3.0 or later — **required** |
| Fabric | Fabric Loader 0.17.2+, Fabric API, Fabric Language Kotlin, Cloth Config |
| NeoForge | 21.1.182+, Cloth Config client UI |
| Java | 21 |

## How XP works

1. **Capture or battle** — a supported event generates a reward.
2. **Calculate** — level, reward type, bonuses and configuration determine XP.
3. **Split** — the configured share of player XP can be stored in the XP Flask.
4. **Train** — use the Flask on an owned Pokémon, or preview the transfer first.

The default capture Exp All is disabled and the XP Flask does not collect normal vanilla Minecraft XP. See [progression](/guide/progression), [XP Flask](/guide/xp-flask) and [commands](/guide/commands).
