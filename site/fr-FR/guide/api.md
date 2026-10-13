# API développeur : XP Flask

La version 2.1 propose une API **côté serveur** pour prévisualiser puis appliquer la conversion de la fiole à un objet **Pokémon Cobblemon**, provenant notamment de l'équipe ou du PC.

## Exemple Java

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
        // Actualiser l'interface du mod appelant.
    }
}
```

**Aperçu côté joueur (v2.1) :** Shift + clic droit avec la fiole sur son Pokémon invoqué affiche une estimation dans le chat. L'API ci-dessous permet les intégrations serveur dans d'autres mods.

`preview` ne modifie rien. `apply` recherche à nouveau la fiole et recalcule le coût. Les quantités d'XP et niveaux transmis par un client ne doivent pas être considérés comme fiables.

## Détection facultative

Identifiant du mod : `cobblemon_xp_overhaul`.

- **Fabric :** `FabricLoader.getInstance().isModLoaded("cobblemon_xp_overhaul")`
- **NeoForge :** `ModList.get().isLoaded("cobblemon_xp_overhaul")`

## Contrat et restrictions

Appeler les méthodes avec un `ServerPlayer` et un `Pokemon` faisant autorité sur le serveur. La fiole Accessories équipée est vérifiée en priorité, suivie de l'inventaire. L'XP stockée utilise la donnée personnalisée `StoredTrainerXp`. Un appel accorde au maximum l'XP nécessaire jusqu'au prochain niveau, avant les événements Cobblemon.

- `XpFlaskPreview` : `status`, `storedTrainerXp`, `availablePokemonXp`, `requiredPokemonXp`, `trainerXpCost`, `pokemonXpToGrant`, `currentLevel`, `resultingLevel`. Méthodes `canApply()` et `willLevelUp()`.
- `XpFlaskResult` : `status`, `consumedTrainerXp`, `grantedPokemonXp`, `previousLevel`, `resultingLevel`, `storedTrainerXpBefore`, `storedTrainerXpAfter`. Méthode `success()`.
- `XpFlaskStatus` : `SUCCESS`, `FEATURE_DISABLED`, `INVALID_PLAYER`, `INVALID_POKEMON`, `NO_FLASK_FOUND`, `EMPTY_FLASK`, `MAX_LEVEL`, `INSUFFICIENT_XP`, `NO_XP_REQUIRED`, `APPLICATION_FAILED`.

Pour traduire le résultat, utiliser `XpFlaskStatus.translationKey()`. Voir les [commandes](/fr-FR/guide/commands).
