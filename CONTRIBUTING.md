# Contributing

Documentation corrections and French translations are welcome in pull requests. Keep English/French content aligned and base behavioral claims on public releases or the maintainer's verified source review.

Before opening a PR:

```sh
npm ci
npm run check:links
python3 scripts/check_public_content.py
npm run docs:build
```

**Do not commit** private source code, private URLs, JARs, development files, credentials or backups. Maintainer review is required. Disclose security issues privately as described in [SECURITY.md](SECURITY.md).
