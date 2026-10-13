#!/usr/bin/env python3
"""Generate the PokeBadges-style EN/FR static wiki using only Python stdlib."""
from pathlib import Path
from html import escape, unescape
import re

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/"site"
SHELL=(ROOT/"scripts"/"layout.html").read_text(encoding="utf-8")
SLUGS=["overview","getting-started","progression","xp-flask","configuration","configuration-reference","commands","compatibility","faq","api"]
L={
 "en":[("👋 Overview","Overview","Introduction"),("📦 Installation","Installation","Getting started"),("🎯 XP Progression","XP Progression","Experience"),("🧪 XP Flask","XP Flask","Training"),("⚙️ Configuration","Configuration","Administration"),("📋 Config Reference","Settings","All JSON settings"),("⌨️ Commands","Commands","Administration"),("🔌 Compatibility","Compatibility","Requirements"),("🛠️ FAQ","FAQ","Troubleshooting"),("🧩 Developer API","Developer API","Integration")],
 "fr":[("👋 Présentation","Présentation","Introduction"),("📦 Installation","Installation","Bien démarrer"),("🎯 Progression XP","Progression XP","Récompenses"),("🧪 Fiole d'XP","Fiole d'XP","Entraînement"),("⚙️ Configuration","Configuration","Administration"),("📋 Paramètres","Paramètres","Référence JSON"),("⌨️ Commandes","Commandes","Administration"),("🔌 Compatibilité","Compatibilité","Prérequis"),("🛠️ FAQ","FAQ","Dépannage"),("🧩 API développeur","API développeur","Intégration")]
}
LINKS=[
 ("https://www.bisecthosting.com/OurStory","🤝 BisectHosting Partner"," sponsored"),
 ("https://discord.gg/kb8NSTF45n","💬 Discord",""),
 ("https://www.curseforge.com/minecraft/mc-mods/cobblemon-xp-overhaul","🧡 CurseForge",""),
 ("https://modrinth.com/mod/cobblemon-xp-overhaul","🟢 Modrinth",""),
 ("https://github.com/LevelsFR/CobblemonXPOverhaul-Multi-1.21.1-Wiki","💻 GitHub Wiki",""),
 ("https://www.patreon.com/c/OurStoryCollection","❤️ Patreon","")
]
TICK=chr(96)

def inline(raw):
 s=escape(raw,quote=False)
 tokens=[]
 def protect(value):
  tokens.append(value)
  return "§§"+str(len(tokens)-1)+"§§"
 def code(m):
  return protect("<code>"+m.group(1)+"</code>")
 s=re.sub(re.escape(TICK)+r"([^"+re.escape(TICK)+r"]+)"+re.escape(TICK),code,s)
 def link(m):
  label,url=m.group(1),unescape(m.group(2))
  clean=url.split("#")[0].rstrip("/")
  if clean.startswith(("/guide/","/fr-FR/guide/")):
   slug=clean.rsplit("/",1)[-1]
   if slug in SLUGS:
    return protect('<a href="#'+slug+'" data-tab-link="'+slug+'">'+label+"</a>")
  if url.startswith("https://"):
   return protect('<a href="'+escape(url,quote=True)+'" target="_blank" rel="noopener noreferrer">'+label+"</a>")
  return label
 s=re.sub(r"\[([^\]]+)\]\(([^)]+)\)",link,s)
 s=re.sub(r"\*\*(.+?)\*\*",r"<strong>\1</strong>",s)
 s=re.sub(r"(?<!\w)\*(.+?)\*(?!\w)",r"<em>\1</em>",s)
 for i in range(len(tokens)-1,-1,-1):
  s=s.replace("§§"+str(i)+"§§",tokens[i])
 return s

def is_block(s):
 s=s.strip()
 return (not s or s.startswith((":::","|",TICK*3))
  or bool(re.match(r"^#{1,6}\s+|^\s*[-*]\s+|^\s*\d+\.\s+",s)))

def render(lines):
 out=[]
 i=0
 while i<len(lines):
  s=lines[i].strip()
  if not s:
   i+=1;continue
  if s.startswith(":::"):
   typ=s[3:].strip().split(" ",1)[0].lower()
   cls="warning" if typ in ("warning","danger","caution") else "success" if typ=="tip" else "info"
   j=i+1
   while j<len(lines) and lines[j].strip()!=":::":
    j+=1
   if j==len(lines):
    raise ValueError("Open admonition")
   inner=lines[i+1:j]
   head=""
   if inner and inner[0].strip() and not is_block(inner[0]):
    head="<strong>"+inline(inner[0].strip())+"</strong>"
    inner=inner[1:]
   out.append('<div class="hint hint-'+cls+'">'+head+render(inner)+"</div>")
   i=j+1;continue
  if s.startswith(TICK*3):
   j=i+1
   while j<len(lines) and not lines[j].strip().startswith(TICK*3):
    j+=1
   if j>=len(lines):
    raise ValueError("Open code fence")
   out.append("<pre><code>"+escape("\n".join(lines[i+1:j]))+"</code></pre>")
   i=j+1;continue
  m=re.match(r"^(#{1,6})\s+(.+)$",s)
  if m:
   t="h3" if len(m.group(1))>=3 else "h2"
   out.append("<"+t+">"+inline(m.group(2))+"</"+t+">")
   i+=1;continue
  if s.startswith("|") and i+1<len(lines) and re.match(r"^\s*\|?[\s:|-]+\|?\s*$",lines[i+1]):
   def cells(row):
    return [c.strip() for c in row.strip().strip("|").split("|")]
   out.append("<table><thead><tr>"+"".join("<th>"+inline(v)+"</th>" for v in cells(s))+"</tr></thead><tbody>")
   i+=2
   while i<len(lines) and lines[i].strip().startswith("|"):
    out.append("<tr>"+"".join("<td>"+inline(v)+"</td>" for v in cells(lines[i]))+"</tr>")
    i+=1
   out.append("</tbody></table>")
   continue
  m=re.match(r"^\s*(?:([-*])\s+|(\d+)\.\s+)(.*)$",lines[i])
  if m:
   ordered=m.group(2) is not None
   tag="ol" if ordered else "ul"
   out.append("<"+tag+">")
   while i<len(lines):
    v=re.match(r"^\s*(?:([-*])\s+|(\d+)\.\s+)(.*)$",lines[i])
    if not v or (v.group(2) is not None)!=ordered:
     break
    out.append("<li>"+inline(v.group(3).strip())+"</li>")
    i+=1
   out.append("</"+tag+">")
   continue
  paragraph=[s]
  i+=1
  while i<len(lines) and not is_block(lines[i]):
   paragraph.append(lines[i].strip())
   i+=1
  out.append("<p>"+inline(" ".join(paragraph))+"</p>")
 return "\n".join(out)

def page(lang):
 fr=lang=="fr"
 shell=SHELL.replace('lang="en"','lang="fr"' if fr else 'lang="en"')
 if fr:
  shell=shell.replace('href="styles.css"','href="../styles.css"').replace('src="app.js"','src="../app.js"')
  shell=shell.replace("Search the documentation...","Rechercher dans la documentation…")
  shell=shell.replace("Cobblemon XP Overhaul v2.1 Documentation</title>","Cobblemon XP Overhaul v2.1 - Documentation FR</title>")
 nav=[];tabs=[];panels=[]
 for n,slug in enumerate(SLUGS):
  icon,short,kicker=L[lang][n]
  active=" active" if n==0 else ""
  nav.append('<a href="#'+slug+'" data-tab-link="'+slug+'"'+(' class="active"' if n==0 else "")+'>'+escape(icon)+"</a>")
  tabs.append('<button class="tab'+active+'" type="button" data-tab="'+slug+'">'+escape(short)+"</button>")
  f=SITE/("fr-FR" if fr else "")/("overview.md" if slug=="overview" else "guide/"+slug+".md")
  source=f.read_text(encoding="utf-8").splitlines()
  if not source or not source[0].startswith("# "):
   raise ValueError("Missing first heading "+str(f))
  title=source[0][2:].strip()
  desc=kicker+": "+short
  panels.append('<section class="tab-panel'+active+'" id="'+slug+'" data-panel="'+slug+'"><div class="page-heading"><span class="page-kicker">'+escape(kicker)+'</span><h1>'+escape(title)+'</h1><p class="page-description">'+escape(desc)+'</p></div>'+render(source[1:])+'</section>')
 ext=[]
 for url,label,sponsor in LINKS:
  ext.append('<a class="sidebar-link" href="'+escape(url,quote=True)+'" target="_blank" rel="noopener noreferrer'+sponsor+'">'+escape(label)+"</a>")
 ext.append('<a class="sidebar-link" href="'+("../" if fr else "fr-FR/")+'">'+("🌐 English" if fr else "🌐 Français")+"</a>")
 extra=('  <div class="layout">\n'
 '    <aside id="sidebar">\n'
 '      <div class="sidebar-title">Documentation</div>\n'
 '      <nav class="sidebar-navigation" aria-label="Documentation sections">\n'+"\n".join(nav)+'\n      </nav>\n'
 '      <div class="sidebar-section"><div class="sidebar-title">Links</div>\n'+"\n".join(ext)+'</div>\n'
 '      <div class="sidebar-footer"><strong>Cobblemon XP Overhaul</strong><span>Documentation for v2.1</span></div>\n'
 '    </aside>\n'
 '    <main>\n'
 '      <div class="tabs" role="tablist" aria-label="Documentation tabs">\n'+"\n".join(tabs)+'</div>\n'
 '      <article>\n'+"\n".join(panels)+'</article>\n'
 '    </main>\n'
 '  </div>\n</body>\n</html>\n')
 return shell+extra

def main():
 (SITE/"index.html").write_text(page("en"),encoding="utf-8")
 (SITE/"fr-FR"/"index.html").write_text(page("fr"),encoding="utf-8")
 (SITE/".nojekyll").touch()
 for prefix in ("","fr-FR/"):
  for slug in SLUGS[1:]:
   target=SITE/prefix/"guide"/slug/"index.html"
   target.parent.mkdir(parents=True,exist_ok=True)
   dest="../../#"+slug
   target.write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url='+dest+'"></head><body><a href="'+dest+'">Open documentation</a></body></html>',encoding="utf-8")
 print("Generated EN/FR pages and legacy redirects.")

if __name__=="__main__":
 main()
