# Cobblemon XP Overhaul Wiki

Public documentation for **Cobblemon XP Overhaul v2.1**, supporting Minecraft **1.21.1** with Fabric and NeoForge.

**Documentation website:** https://levelsfr.github.io/CobblemonXPOverhaul-Multi-1.21.1-Wiki/

**Download the mod:** https://www.curseforge.com/minecraft/mc-mods/cobblemon-xp-overhaul

## Available documentation

- Installation, supported versions and dependencies
- Player and Pokémon experience rewards
- XP Flask mechanics, crafting and transfer preview
- Configuration options and default values
- XP calculation diagnostics, commands, compatibility and troubleshooting
- Integration API for compatible mods

Documentation is available in **English** and **French** (`/fr-FR/`).

## Local development

Node.js 22 or later is recommended:

```sh
npm ci
npm run check:links
python3 scripts/check_public_content.py
npm run docs:build
npm run docs:dev
```

## Contributing and security

Documentation improvements are welcome through pull requests. Review [CONTRIBUTING.md](CONTRIBUTING.md) before contributing. See [SECURITY.md](SECURITY.md) for responsible vulnerability reporting and repository security practices.

All documentation should describe verified features. Never include credentials, private files or unrelated project data in public contributions.

**License:** All Rights Reserved.
