# Commands and permissions

All commands below require **permission level 2**, typically a server operator.

| Command | Effect |
| --- | --- |
| `/cxpo reload` | Reload both JSON config files |
| `/cxpo flask get` | Show XP in the first usable Flask |
| `/cxpo flask set <amount>` | Set stored XP to a nonnegative integer |
| `/cxpo flask add <amount>` | Add a signed amount and clamp the stored XP to zero or more |

The full alias `/cobblemonxpoverhaul` supports the same subcommands.

```text
/cxpo reload
/cxpo flask get
/cxpo flask set 250
/cxpo flask add -50
```

::: warning Flask commands
Flask subcommands must be run by a player with a usable Flask. They do not have a target-player argument and cannot be run as a console player substitute.
:::

A Flask in the dedicated optional **Accessories** slot takes priority over a Flask in inventory.

See [configuration](/guide/configuration) and [XP Flask](/guide/xp-flask).
