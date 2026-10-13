#!/usr/bin/env python3
"""Validate generated wiki parity, source constraints and shared layout."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
S=ROOT/"site"
tabs=("overview","getting-started","progression","xp-flask","configuration","configuration-reference","commands","compatibility","faq","api")
for path in (S/"index.html",S/"fr-FR"/"index.html"):
 data=path.read_text(encoding="utf-8")
 for tab in tabs:
  for key in ('data-tab="'+tab+'"','data-panel="'+tab+'"','data-tab-link="'+tab+'"'):
   assert key in data,(str(path),key)
 assert data.count('class="tab-panel active"')==1
 assert data.count('class="tab active"')==1
 assert all(s in data for s in ("brand-mark","community-badge","search-results","Cobblemon XP Overhaul","OS Cobblemon Library","2.1"))
 sidebar=data.split('<aside id="sidebar">',1)[1].split("</aside>",1)[0]
 header=data.split('<header class="topbar">',1)[1].split("</header>",1)[0]
 assert "GitHub Wiki" not in sidebar
 assert 'lang-switch' not in sidebar and "🌐" not in sidebar
 expected_href='../' if 'fr-FR/index.html' in str(path) else 'fr-FR/'
 expected_label="EN" if expected_href=="../" else "FR"
 assert ('class="lang-switch" id="languageSwitch" href="'+expected_href+'"') in header
 assert ('>'+expected_label+'</a>') in header
 assert "PokeBadges" not in data and "Recipe Item Sync" not in data
assert (S/"styles.css").is_file()
assert (S/"app.js").is_file()
assert (S/".nojekyll").exists()
for prefix in ("","fr-FR/"):
 for tab in tabs[1:]:
  assert (S/prefix/"guide"/tab/"index.html").is_file()
print("OK: static wiki follows reference shell; EN/FR and legacy redirects verified")
