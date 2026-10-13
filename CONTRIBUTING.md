# Contributing

Documentation fixes and translations are welcome. Update the Markdown files and keep English/French content aligned. The layout follows the same static, tabbed design across companion wikis.

Before opening a pull request, use Python 3.10+ and run:

```sh
python3 scripts/render_site.py
python3 scripts/check_links.py
python3 scripts/check_public_content.py
python3 scripts/validate_static.py
node --check site/app.js
```

GitHub Actions regenerates the HTML on deployment from Markdown; do not change generated HTML instead of the source.

Never submit credentials, private code, JARs or backup files. Report vulnerabilities privately as described in [SECURITY.md](SECURITY.md).
