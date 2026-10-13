#!/usr/bin/env python3
from pathlib import Path
import re,sys
site=Path(__file__).resolve().parents[1]/'site'
names={'getting-started','progression','xp-flask','configuration','configuration-reference','commands','compatibility','faq','api'}
errors=[]
for root in (site/'guide',site/'fr-FR'/'guide'):
  found={p.stem for p in root.glob('*.md')}
  if found!=names:errors.append(f'{root}: missing {sorted(names-found)}; extra {sorted(found-names)}')
pages=list(site.rglob('*.md'))
for page in pages:
  data=page.read_text(encoding='utf8')
  links=re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)',data)
  for link in links:
    link=link.split('#')[0].split('?')[0].strip()
    if not link or link.startswith(('https://','http://','mailto:','#')):continue
    target=(site/link.lstrip('/') if link.startswith('/') else page.parent/link)
    if not any(q.is_file() for q in (target,target.with_suffix('.md'),target/'index.md')):
      errors.append(f'{page.relative_to(site)}: {link}')
if errors:
  print('Invalid wiki links:',*errors,sep='\n - ')
  sys.exit(1)
print(f'OK: {len(pages)} pages, EN/FR parity and local links')
