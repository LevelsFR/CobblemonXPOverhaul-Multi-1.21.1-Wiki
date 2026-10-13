# Commands and permissions

All commands below require **permission level 2**, typically a server operator.

| Command | Effect |
| --- | --- |
| `/cxpo reload` | Reload both JSON config files |
| `/cxpo flask get` | Show XP in the first usable Flask |
| `/cxpo flask set <amount>` | Set stored XP to a nonnegative integer |
| `/cxpo flask add <amount>` | Add a signed amount and clamp the stored XP to zero or more |
| `/cxpo xp explain` | Explain your latest recorded **player XP** capture or victory calculation |
| `/cxpo xp explain <player>` | Explain the latest recorded **player XP** calculation for the specified online player |

The full alias `/cobblemonxpoverhaul` supports the same subcommands.

```text
/cxpo reload
/cxpo flask get
/cxpo flask set 250
/cxpo flask add -50
/cxpo xp explain
/cxpo xp explain Steve
```

## XP calculation breakdown (v2.1)

The `xp explain` command displays the most recently recorded **player XP** calculation on the current server: its capture/wild/trainer/PvP source, eligible levels, base XP, scaling, applied multipliers, total calculated XP, XP kept by the player and XP redirected into the Flask. It also explains zero rewards and skipped captures when recorded.

Records exist **only for the current server session**, with a bounded memory of up to 256 tracked players. This is not a persistent history, and the command does not explain individual Pokémon XP rewards. If no record exists, it reports that no calculation was recorded.

Use the optional `<player>` argument to inspect another online player. From the console, specify a player explicitly; without an argument, the command requires an in-game player.

::: warning Flask commands
Flask subcommands must be run by a player with a usable Flask. They do not have a target-player argument and cannot be run as a console player substitute.
:::

A Flask in the dedicated optional **Accessories** slot takes priority over a Flask in inventory.

See [configuration](/guide/configuration) and [XP Flask](/guide/xp-flask).
