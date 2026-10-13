# XP progression

**Player XP** (Minecraft experience bar) and **Pokémon XP** are configurable separately.

## Player XP from captures

Capturing a Pokémon can grant player XP determined by a base value, captured level, global multiplier and bonuses. The default base is `4` and level multiplier is `0.2`.

Capture modifiers can apply to:
- A species captured for the first time, or repeated captures of the same species
- Shiny, Alpha and special forms
- Legendary, Mythical and Ultra Beast Pokémon
- Lucky Egg bonuses, if enabled

The same species history is tracked per player. Shiny and Alpha multipliers are **1.0 by default**, so they do not increase XP unless configured.

## Player XP from battles

Victory rewards have separate profiles for **wild**, **NPC trainer**, and **PvP** battles. Each profile has its own enabled state, base XP, per-level multiplier and global multiplier. A minimum defeated Pokémon level can be configured.

Capture-triggered wild victories are skipped by default to prevent duplicate player rewards.

## Pokémon XP from captures

Eligible party Pokémon can receive configurable capture XP. The mod distinguishes:
- **Participants** with `participantMultiplier` (default **1.0**).
- **Exp Share** holders when Exp All is disabled, with `expShareMultiplier` (default **0.5**).
- **Exp All** recipients when enabled, with `expAllMultiplier` (default **0.35**).

`pokemon.capture.expAllEnabled` defaults to `false`. With Exp All enabled, Exp Share holders can receive an optional additional **10%** bonus. The captured Pokémon can also receive Exp All XP when `allowCapturedPokemonWithExpAll` is enabled.

## Pokémon XP from trainer fights

During trainer battles, XP is awarded on eligible **knockouts** instead of being deferred until battle victory. This means eligible KO rewards can persist even after a later battle loss.

## Lucky Egg

The player reward checks inventory or party-held Lucky Eggs according to the `luckyEgg` config. Pokémon capture XP checks the recipient's held Lucky Egg individually. Default lucky egg multiplier for applicable custom rewards is **1.5**.

## Inspect the last player XP calculation (v2.1)

Server operators can use `/cxpo xp explain` or `/cxpo xp explain <player>` to see the latest recorded **player XP** formula, bonuses and split between the player and the XP Flask. The diagnostic record is session-only. See [commands](/guide/commands).

See the [full settings reference](/guide/configuration-reference).
