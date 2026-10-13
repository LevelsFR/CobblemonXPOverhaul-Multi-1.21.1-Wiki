#!/usr/bin/env python3
"""Heuristic public-doc repository scanner, supplementing human review."""
from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]
top={'.github','.gitignore','README.md','SECURITY.md','CONTRIBUTING.md','package.json','package-lock.json','site','scripts'}
safe={'.yml','.yaml','.json','.md','.py','.ts','.mts','.css','.svg','.html','.js'}
errors=[]
for p in root.rglob('*'):
  if not p.is_file() or '.git' in p.parts or 'node_modules' in p.parts or '.vitepress/dist' in str(p) or '.vitepress/cache' in str(p):continue
  rel=p.relative_to(root)
  if rel.parts[0] not in top:errors.append(f'{rel}: unexpected path')
  if p.suffix not in safe and p.name not in {'.gitignore','CODEOWNERS','.nojekyll'}:errors.append(f'{rel}: unexpected file type');continue
  if p.stat().st_size>400000:errors.append(f'{rel}: oversized file');continue
  try:data=p.read_text(encoding='utf8')
  except UnicodeDecodeError:errors.append(f'{rel}: binary content');continue
  for token in ['-----BEGIN '+'PRIVATE KEY', 'github_'+'pat_', 'gh'+'p_', 'gh'+'o_', 'AK'+'IA']:
    if token in data:errors.append(f'{rel}: possible secret, review required');break
if errors:
  print('Public repository safety checks failed:',*errors,sep='\n - ');sys.exit(1)
print('OK: public documentation safety heuristics passed')
