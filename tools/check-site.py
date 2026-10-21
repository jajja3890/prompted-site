from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[1]
count=0
errors=[]
for p in root.glob('**/*.html'):
 if p.name=='index.html' and p.parent==root:continue
 count+=1
 soup=BeautifulSoup(p.read_text('utf-8'),'html.parser')
 for tag in ['title','h1','main','nav','footer']:
  if not soup.find(tag):errors.append(f'{p}: missing {tag}')
 if len(soup.find_all('h1'))!=1:errors.append(f'{p}: h1 count not one')
 if not soup.find('html').get('lang'):errors.append(f'{p}: missing lang')
 for tag in soup.select('a[href], img[src], link[href]'):
  h=tag.get('href') or tag.get('src')
  if h.startswith('/') and not h.startswith('//'):
   path=(root/h.split('#')[0].lstrip('/'))
   if h.endswith('/'):path=path/'index.html'
   if not path.exists():errors.append(f'{p}: broken {h}')
 if 'Design VA Oy' in soup.get_text() or 'DataDiscovery' in soup.get_text():errors.append(f'{p}: old attribution/legal content')
 if not soup.select('meta[name="robots"][content="noindex,nofollow"]'):errors.append(f'{p}: missing noindex release gate')
print(f'Checked {count} FI/EN pages and internal links: '+('PASS' if not errors else 'FAIL'))
for err in errors:print(err)
raise SystemExit(bool(errors))
