from pathlib import Path
import json,base64,mimetypes
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parents[1]
checks=[];fail=[]
all_pages=[]
for l in ['fi','en']:
 for key in ['','literacy','capability','transformation','yritys' if l=='fi' else 'company','yhteys' if l=='fi' else 'contact','tietosuoja' if l=='fi' else 'privacy','ehdot' if l=='fi' else 'terms']:
  f=R/l/key/'index.html'
  all_pages.append((l,key,f))
  s=BeautifulSoup(f.read_text(),'html.parser')
  assert s.find('meta',attrs={'name':'robots','content':'noindex,nofollow'})
  assert len(s.select('h1'))==1
  for tag in s.select('[href]'):
   link=tag['href']
   if link.startswith('/'):
    path,_,frag=link.partition('#')
    cand=R/path.lstrip('/')
    if cand.is_dir():cand=cand/'index.html'
    if not cand.exists():fail.append((str(f.relative_to(R)),'missing href',link))
    if frag and cand.exists() and not BeautifulSoup(cand.read_text(),'html.parser').find(id=frag):fail.append((str(f.relative_to(R)),'missing anchor',link))
  if key in ('literacy','transformation'):
   assert len(s.select('.ps-product-panel'))==1
   assert s.find(id='toimitus') is not None
  checks.append({'file':str(f.relative_to(R)),'links_checked':len(s.select('a'))})

def markup(f):
 s=BeautifulSoup(f.read_text(),'html.parser')
 for node in s.select('link[rel=stylesheet],script[src]'):node.decompose()
 for img in s.select('img[src^="/assets/"]'):
  binary=(R/img['src'].lstrip('/')).read_bytes()
  img['src']='data:'+(mimetypes.guess_type(img['src'])[0] or 'application/octet-stream')+';base64,'+base64.b64encode(binary).decode()
 css=s.new_tag('style')
 css.string='\n'.join((R/'assets'/n).read_text() for n in ['concept.css','pages.css','product-first.css','product-system.css'])
 s.head.append(css)
 js=s.new_tag('script');js.string=(R/'assets'/'concept.js').read_text();s.body.append(js)
 return str(s)

samples=[(l,k,f) for l,k,f in all_pages if k in ('','literacy','capability','transformation')]
pic=R/'previews_round3';pic.mkdir(exist_ok=True)
with sync_playwright() as pw:
 b=pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for l,k,f in samples:
  for w in [320,360,390,768,1024,1440,1920]:
   page=b.new_page(viewport={'width':w,'height':900},device_scale_factor=1)
   err=[];page.on('pageerror',lambda exc:err.append(str(exc)))
   page.set_content(markup(f),wait_until='load')
   page.wait_for_timeout(35)
   state=page.evaluate('''()=>({scroll:document.documentElement.scrollWidth,client:document.documentElement.clientWidth,hero:document.querySelector('main>section')?.getBoundingClientRect().height,bodyHeight:document.body.scrollHeight,panels:[...document.querySelectorAll('.ps-product-panel')].map(el=>el.getBoundingClientRect().width)})''')
   if state['scroll']>state['client']+1:fail.append((l,k,w,'horizontal overflow',state))
   if state['hero']<300:fail.append((l,k,w,'hero too short',state))
   if err:fail.append((l,k,w,'errors',err))
   if w==390:
    btn=page.locator('.nav-toggle')
    btn.click();status=btn.get_attribute('aria-expanded')
    if status!='true':fail.append((l,k,w,'mobile menu not opening'))
    page.keyboard.press('Escape');status=btn.get_attribute('aria-expanded')
    if status!='false':fail.append((l,k,w,'mobile menu escape'))
   if (l,k,w) in [('fi','literacy',1440),('fi','literacy',390),('fi','transformation',1440),('fi','transformation',390),('en','literacy',1440),('en','transformation',1440),('fi','',1440),('fi','capability',1440)]:
    name=(k or 'home')+'-'+l+'-'+str(w)+'.png'
    if w==1440:page.screenshot(path=str(pic/name),full_page=False)
    else:page.screenshot(path=str(pic/name),full_page=True)
   checks.append({'lang':l,'route':k or 'home','width':w,'scrollWidth':state['scroll'],'clientWidth':state['client'],'heroHeight':round(state['hero'])})
   page.close()
 b.close()
report={'status':'PASS' if not fail else 'FAIL','routeCount':len(all_pages),'browserWidths':len(samples)*7,'checks':len(checks),'failures':fail,'sizes':checks}
(R/'tools/round3_qa.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in report.items() if k!='sizes'},ensure_ascii=False))
if fail: raise SystemExit(1)
