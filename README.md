# Cobblemon XP Overhaul Wiki

Official public documentation for **Cobblemon XP Overhaul 2.0** on Minecraft **1.21.1**, for **Fabric** and **NeoForge**.

- **Documentation:** https://levelsfr.github.io/CobblemonXPOverhaul-Multi-1.21.1-Wiki/ (active after GitHub Pages deployment succeeds)
- **CurseForge:** https://www.curseforge.com/minecraft/mc-mods/cobblemon-xp-overhaul
- **Languages:** English at `/`, French at `/fr-FR/`.
- **Private mod repository:** remains private, and no source code is included here.

## Develop and validate
Requires Node.js 22 or newer.

```sh
npm ci
npm run check:links
python3 scripts/check_public_content.py
npm run docs:build
```

GitHub Actions deploys from `main` with short-lived Pages permissions. PRs run read-only validation. External contributors should submit documentation improvements through reviewed PRs.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md). Documentation is public, but **private source code, assets and credentials must never be copied here**. The upstream mod declares All Rights Reserved; this wiki grants no license to reuse private assets.

## Repository settings to enforce
Protect `main` with reviews, required **Validate Wiki** checks, no force-pushes and no branch deletion. Enable **private vulnerability reporting, secret scanning and push protection** if offered. Configure Settings → Pages → GitHub Actions.

Only publish behavior verified against the source or released mod.