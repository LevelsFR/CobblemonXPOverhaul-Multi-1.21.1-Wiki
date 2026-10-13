# FAQ and troubleshooting

## Why is my XP Flask empty?

It collects only player XP **granted by XP Overhaul**, not mining or regular mobs. Keep a Flask in your inventory or compatible Accessories slot, and verify `trainerXpCore.enabled=true` and `coreCaptureRatio>0`.

## Why doesn't every Pokémon receive capture XP?

Check `pokemon.capture.enabled`, participation, Exp Share, and `expAllEnabled` (disabled by default). Cobblemon's normal eligibility rules can also apply.

## Why do Shiny and Alpha catches give normal XP?

Their default capture multipliers are both `1.0`. Increase `shinyMultiplier` and `alphaMultiplier` in the relevant bonus section if desired.

## Why can't I use the reload command?

`/cxpo reload` requires operator permission level **2**.

## Can I check a Flask transfer before using it?

Yes, since **v2.1**. Hold Shift (sneak) and right-click your own summoned Pokémon with the Flask to preview the transfer in chat without spending XP. Use a regular right-click to apply it.

## Can operators inspect XP calculations?

Yes. `/cxpo xp explain [player]` shows the last recorded **player XP** reward calculation from the current server session. It does not track Pokémon XP or persist across restarts. Permission level **2** is required.

## Why does the Flask keep some stored XP?

Each application is capped to the amount needed for the next Pokémon level before Cobblemon's XP events run.

## Why does the config revert?

Malformed JSON can trigger replacement with sanitized defaults. Check the logs and restore a backup. The common configuration exposes `debug.enabled` for diagnostic output.

## Can other mods use the Flask on party or PC Pokémon?

Yes. The documented [XP Flask API](/guide/api) works on server-authoritative Cobblemon Pokémon objects. It is not an in-game PC button by itself.

## Where is configuration saved?

In `config/cobblemon_xp_overhaul/` as separate server and common JSON files. See [configuration](/guide/configuration).
