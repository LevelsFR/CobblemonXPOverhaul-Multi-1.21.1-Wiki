# Configuration guide

The mod creates two JSON files in `config/cobblemon_xp_overhaul/`:

| File | Purpose |
| --- | --- |
| `cobblemon_xp_overhaul-server.json` | Capture and battle rewards, Lucky Eggs and XP Flask |
| `cobblemon_xp_overhaul-common.json` | Action bar messages, queues and debug options |

## Edit the configuration

1. Start the instance or server once to generate the files.
2. Back up the two JSON files.
3. Edit the relevant keys. JSON does not accept comments or trailing commas.
4. Run `/cxpo reload` with permission level 2.
5. Test a capture or battle to confirm the result.

The **Cloth Config** screen offers a client UI for settings. For multiplayer balance changes, edit the authoritative **server's** files.

## Example: Exp All

Set the existing `pokemon.capture.expAllEnabled` property:

```json
"pokemon": {
  "capture": {
    "expAllEnabled": true,
    "expAllMultiplier": 0.35,
    "expShareBonusWithExpAllEnabled": false
  }
}
```

This is a partial illustration of the nested structure, not a replacement for the complete server JSON.

## Example: capture XP balancing

```json
"player": {
  "capture": {
    "baseXp": 4,
    "levelMultiplier": 0.2,
    "globalMultiplier": 1.0
  }
}
```

The mod normalizes invalid values and migrates certain older flat section names on reload. Malformed JSON can trigger safe defaults, so **make backups** before editing.

For every exact key and default, use the [full configuration reference](/guide/configuration-reference).
