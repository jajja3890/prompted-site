from pathlib import Path
from bs4 import BeautifulSoup
import json
from playwright.sync_api import sync_playwright
import mimetypes,base64
ROOT=Path(__file__).resolve().parents[1]
page_rel=[f'{lang}/{key}/index.html' if key else f'{lang}/index.html' for lang in ('fi','en') for key in ('','literacy','capability','transformation','yritys' if lang=='fi' else 'company','yhteys' if lang=='fi' else 'contact','tietosuoja' if lang=='fi' else 'privacy','ehdot' if lang=='fi' else 'terms')]
failed=[];verified=0
for rel in page_rel:
 html=(ROOT/rel).read_text(encoding='utf-8')
 soup=BeautifulSoup(html,'html.parser')
 for label,flag in [('HTML noindex',bool(soup.find('meta',attrs={'name':'robots','content':'noindex,nofollow'}))),('lang',soup.html.get('lang') in ['fi','en']),('one h1',len(soup.select('h1'))==1),('official logo',len(soup.select('header .logo img'))==1)]:
  verified+=1
  if not flag:failed.append((rel,label))
 for attr in ['href','src']:
  for tag in soup.select(f'[{attr}]'):
   target=tag[attr]
   if not target or target.startswith(('mailto:','https://','http://','data:')): continue
   if target.startswith('#'):
    valid=soup.find(id=target[1:]) is not None
   elif target.startswith('/'):
    target_path,_,anchor=target.partition('#')
    full=ROOT/target_path.strip('/')
    candidate=full if full.is_file() else (full/'index.html')
    valid=candidate.exists()
    if valid and anchor: valid=BeautifulSoup(candidate.read_text(encoding='utf-8'),'html.parser').find(id=anchor) is not None
   else:valid=True
   verified+=1
   if not valid: failed.append((rel,'broken '+attr,target))
 for mandatory in ['Literacy','Capability','Transformation']:
  verified+=1
  if mandatory not in soup.get_text(' ',strip=True):failed.append((rel,'missing product',mandatory))
for rel in ['fi/index.html','en/index.html','fi/capability/index.html','en/capability/index.html']:
 soup=BeautifulSoup((ROOT/rel).read_text(encoding='utf-8'),'html.parser')
 for key in ['.pf-browser','.pf-phone','.pf-data-overlay','.pf-art-disclaimer']:
  verified+=1
  if not soup.select_one(key):failed.append((rel,'missing',key))
# verify prelaunch robots header and close-release status
settings=json.loads((ROOT/'vercel.json').read_text(encoding='utf-8'))
verified+=1
if not any(h.get('key')=='X-Robots-Tag' and 'noindex' in h.get('value','') for item in settings['headers'] for h in item['headers']): failed.append(('vercel.json','Missing response noindex'))
# In-memory browser rendering (network forbidden in container).
def page_markup(rel):
 soup=BeautifulSoup((ROOT/rel).read_text(encoding='utf-8'),'html.parser')
 for element in soup.select('link[rel="stylesheet"],script[src]'):element.decompose()
 for img in soup.select('img[src^="/assets/"]'):
  src=img['src']; data=(ROOT/src.lstrip('/')).read_bytes()
  img['src']='data:'+(mimetypes.guess_type(src)[0] or 'application/octet-stream')+';base64,'+base64.b64encode(data).decode()
 st=soup.new_tag('style');st.string='\n'.join((ROOT/'assets'/x).read_text(encoding='utf-8') for x in ('concept.css','pages.css','product-first.css'))
 soup.head.append(st)
 sc=soup.new_tag('script');sc.string=(ROOT/'assets'/'concept.js').read_text(encoding='utf-8');soup.body.append(sc)
 return str(soup)
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for rel in ['fi/index.html','en/index.html','fi/capability/index.html','en/capability/index.html']:
  for w in [320,360,390,768,1024,1440,1920]:
   page=browser.new_page(viewport={'width':w,'height':900})
   errors=[];page.on('pageerror',lambda x: errors.append(str(x)))
   page.set_content(page_markup(rel),wait_until='load')
   dat=page.evaluate('''()=>({doc:document.documentElement.scrollWidth,client:document.documentElement.clientWidth,screen:document.querySelector('.pf-browser').getBoundingClientRect().height,visible:document.querySelector('.pf-browser').getBoundingClientRect().width})''')
   verified+=3
   if dat['doc']>dat['client']: failed.append((rel,w,'horizontal overflow',dat))
   if dat['screen']<150 or dat['visible']<150: failed.append((rel,w,'missing visible screen',dat))
   if errors: failed.append((rel,w,'js errors',errors))
   if w==390:
    button=page.locator('button.nav-toggle')
    button.click()
    verified+=1
    if button.get_attribute('aria-expanded')!='true':failed.append((rel,w,'mobile menu does not open'))
    page.keyboard.press('Escape')
    verified+=1
    if button.get_attribute('aria-expanded')!='false':failed.append((rel,w,'mobile menu does not close on Escape'))
   page.close()
 browser.close()
res={'verified_assertions':verified,'issues':failed,'pages':len(page_rel),'browser_hero_breakpoints':28}
(ROOT/'tools'/'product_first_qa.json').write_text(json.dumps(res,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(res,ensure_ascii=False,indent=2))
if failed:raise SystemExit(1)
