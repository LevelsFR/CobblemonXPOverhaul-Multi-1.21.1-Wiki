# Compatibility

## Versions and loaders

The source targets **Minecraft 1.21.1**, **Cobblemon 1.8.0+**, and builds for **Fabric** and **NeoForge**. Confirm the precise loader-specific release before installation.

**Fabric:** Loader 0.17.2+, Fabric API, Fabric Language Kotlin 1.13.6+, Cloth Config 15.0.140+, and compatible Cobblemon.

**NeoForge:** NeoForge 21.1.182+, compatible Cobblemon, with Cloth Config 15.0.140+ on clients using the settings screen. The build uses Kotlin for Forge.

Requirements come from the mod metadata and do not guarantee testing against every later release.

## Optional integrations

| Mod | Integration |
| --- | --- |
| **Accessories** | Equippable XP Flask in the `xp_flask` slot; inventory fallback |
| **Mod Menu** | Optional Fabric entry to the settings screen |
| **Radical Cobblemon Trainers (RCT)** | Conditional level-cap compatibility when its expected API is available |

The RCT integration checks classes reflectively and does not require the mod. If its API cannot be resolved, the compatibility hook does not activate.

## Multiplayer and limitations

Reward handling and API Flask application run on the **server**. Install matching game/loader versions across server and clients. Use server JSON for balance settings.

The XP Flask collects XP Overhaul player rewards, not vanilla XP sources. A single use is limited to the next Pokémon level before Cobblemon events. Exp All is **disabled by default**.

See the [FAQ](/guide/faq) and [requirements](/guide/getting-started).
