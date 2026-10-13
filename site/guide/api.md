# XP Flask developer API

XP Overhaul v2.0 exposes a server-side integration API for previewing and applying Flask XP to a **Cobblemon Pokémon object**, including Pokémon from party or PC storage.

## Example

```java
import com.cobblemon.mod.common.pokemon.Pokemon;
import net.levelscraft7.cobblemonxpoverhaul.api.XpFlaskApi;
import net.levelscraft7.cobblemonxpoverhaul.api.XpFlaskPreview;
import net.levelscraft7.cobblemonxpoverhaul.api.XpFlaskResult;
import net.minecraft.server.level.ServerPlayer;

XpFlaskPreview preview = XpFlaskApi.preview(player, pokemon);
if (preview.canApply()) {
    XpFlaskResult result = XpFlaskApi.apply(player, pokemon);
    if (result.success()) {
        // Refresh the calling mod's own UI.
    }
}
```

`preview` never mutates player, Flask or Pokémon. `apply` locates the Flask again and recalculates the cost. Do not accept client-supplied XP amounts or levels as authoritative.

## Optional dependency detection

Mod ID: `cobblemon_xp_overhaul`.

- **Fabric:** `FabricLoader.getInstance().isModLoaded("cobblemon_xp_overhaul")`
- **NeoForge:** `ModList.get().isLoaded("cobblemon_xp_overhaul")`

## Contracts and limitations

The API requires a `ServerPlayer` and a server-authoritative `Pokemon`. It checks equipped Accessories Flask first, then inventory. XP resides in the Flask's `StoredTrainerXp` custom data. One application uses at most the XP needed until the next level before Cobblemon events.

- `XpFlaskPreview` contains `status`, `storedTrainerXp`, `availablePokemonXp`, `requiredPokemonXp`, `trainerXpCost`, `pokemonXpToGrant`, `currentLevel`, `resultingLevel`, with `canApply()` and `willLevelUp()`.
- `XpFlaskResult` contains `status`, `consumedTrainerXp`, `grantedPokemonXp`, `previousLevel`, `resultingLevel`, `storedTrainerXpBefore`, `storedTrainerXpAfter`, with `success()`.
- `XpFlaskStatus` values: `SUCCESS`, `FEATURE_DISABLED`, `INVALID_PLAYER`, `INVALID_POKEMON`, `NO_FLASK_FOUND`, `EMPTY_FLASK`, `MAX_LEVEL`, `INSUFFICIENT_XP`, `NO_XP_REQUIRED`, `APPLICATION_FAILED`.

For localization, use `XpFlaskStatus.translationKey()` instead of parsing displayed text. See [admin commands](/guide/commands).
