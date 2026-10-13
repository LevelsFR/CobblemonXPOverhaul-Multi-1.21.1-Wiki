# Compatibility

## Versions and loaders

The source targets **Minecraft 1.21.1**, **Cobblemon 1.8.2 up to but excluding 1.9.0**, and builds for **Fabric** and **NeoForge**. Confirm the precise loader-specific release before installation.

**Fabric:** Loader 0.17.2+, Fabric API, Fabric Language Kotlin 1.13.6+, Cloth Config 15.0.140+, **OS Cobblemon Library 1.3.0+** and Cobblemon 1.8.2–1.8.x.

**NeoForge:** NeoForge 21.1.182+, Cobblemon 1.8.2–1.8.x, **OS Cobblemon Library 1.3.0+**, with Cloth Config 15.0.140+ on clients using the settings screen. The build uses Kotlin for Forge.

**OS Cobblemon Library is required on both loaders**, not an optional compatibility mod. The mod uses the library's Pokémon party storage access.

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

The XP Flask collects XP Overhaul player rewards, not vanilla XP sources. A regular use is limited to the next Pokémon level before Cobblemon events. Sneak + right-click previews the transfer without changing XP. Exp All is **disabled by default**.

See the [FAQ](/guide/faq) and [requirements](/guide/getting-started).
