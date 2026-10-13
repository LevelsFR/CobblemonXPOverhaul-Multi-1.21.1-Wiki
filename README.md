# Cobblemon XP Overhaul Wiki

Public documentation for **Cobblemon XP Overhaul v2.1**, for Minecraft **1.21.1**, **Fabric** and **NeoForge**.

**Documentation website:** https://levelsfr.github.io/CobblemonXPOverhaul-Multi-1.21.1-Wiki/

**Download:** [CurseForge](https://www.curseforge.com/minecraft/mc-mods/cobblemon-xp-overhaul) · [Modrinth](https://modrinth.com/mod/cobblemon-xp-overhaul)

## What you'll find

- Installation, supported versions and dependencies
- Player and Pokémon experience rewards and bonuses
- XP Flask, crafting, storage and transfer preview
- Server and common configuration
- Commands, XP diagnostics, compatibility and troubleshooting
- Developer API

The documentation is available in **English** and **French**.

## Presentation and maintenance

The wiki uses the shared static documentation layout with navigation tabs, sidebar, search, theme toggle and community badges.

Markdown sources are in `site/overview.md`, `site/guide/`, `site/fr-FR/overview.md` and `site/fr-FR/guide/`. The static site is generated using `scripts/render_site.py`.

```sh
python3 scripts/render_site.py
python3 scripts/check_links.py
python3 scripts/check_public_content.py
python3 scripts/validate_static.py
node --check site/app.js
```

GitHub Actions generates the public HTML and publishes it with GitHub Pages.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md). Do not include credentials, private files or unrelated materials in public contributions.

**License:** All Rights Reserved.
