# XP Flask

The **XP Flask** (`cobblemon_xp_overhaul:xp_flask`) stores part of the player XP awarded **by XP Overhaul itself**, then converts it into Pokémon XP.

::: warning Not a vanilla XP collector
Mining, normal mob drops and other sources outside XP Overhaul do not charge this Flask.
:::

## Crafting recipe

| | | |
|:---:|:---:|:---:|
| Amethyst Shard | Bottle o' Enchanting | Amethyst Shard |
| Exp. Candy L | Exp. Share | Exp. Candy L |
| Lapis Lazuli | Bottle o' Enchanting | Lapis Lazuli |

This is a shaped 3 × 3 recipe injected when the server starts.

## Charging and use

1. Keep an XP Flask in your inventory, or equip one in the optional **Accessories** `xp_flask` slot.
2. Earn player XP through supported XP Overhaul capture or victory rewards.
3. With the Flask feature enabled, part of those rewards goes into the Flask. The remainder goes to the Minecraft XP bar.
4. Right-click a **summoned Pokémon you own** with the filled Flask to grant Pokémon XP.

Only up to the XP required to reach the **next Pokémon level** can be granted per use, before Cobblemon events. Any unused stored XP remains in the Flask. A tooltip shows how much converted Pokémon XP is available.

## Default conversion

| Setting | Default | Meaning |
| --- | --- | --- |
| `coreCaptureRatio` | `0.25` | Redirect 25% of eligible player XP, rounded down |
| `transferMultiplier` | `40.0` | Trainer XP to Pokémon XP factor |
| `transferEfficiency` | `0.9` | Additional conversion factor |
| `enabled` | `true` | Enable Flask processing |

The effective conversion factor is **40 × 0.9 = 36** Pokémon XP for each stored trainer XP, subject to integer rounding and the next-level limit.

## Accessories support

When installed, a Flask equipped in its Accessories slot is selected **before** inventory Flasks. Without Accessories, inventory lookup still works.

## Messages

Use `trainerXpCore.messageMode` as `ACTION_BAR`, `CHAT` or `DISABLED`. The `showTrainerXpCoreMessages` toggle also applies.

Server administrators can inspect or adjust stored XP with [Flask commands](/guide/commands). Other mods can use the [server-side API](/guide/api).
