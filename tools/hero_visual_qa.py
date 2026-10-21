from pathlib import Path
import json, base64, mimetypes
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'previews_product_first';P.mkdir(exist_ok=True)
results=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-gpu'])
 for loc,page,width,height in [('fi','home',1440,900),('fi','home',390,844),('fi','capability',1440,900),('en','home',1440,900),('en','home',390,844),('fi','home',768,1100),('fi','home',1024,850),('fi','home',360,780),('fi','capability',390,844)]:
  ctx=b.new_context(viewport={'width':width,'height':height},device_scale_factor=1,reduced_motion='reduce')
  tab=ctx.new_page()
  issues=[]
  tab.on('pageerror',lambda err:issues.append(str(err)))
  path=ROOT/loc/('capability' if page=='capability' else '')/'index.html'
  # use direct file urls, assets / fail. Need local HTTP service (see script launched externally)
  url=f'http://127.0.0.1:8765/{loc}/'+('capability/' if page=='capability' else '')
  soup=BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser')
  for el in soup.select('link[rel="stylesheet"],script[src]'):
   el.decompose()
  for image in soup.select('img[src]'):
   src=image.get('src','')
   if src.startswith('/assets/'):
    data=(ROOT/src.lstrip('/')).read_bytes()
    mime=mimetypes.guess_type(src)[0] or 'application/octet-stream'
    image['src']='data:'+mime+';base64,'+base64.b64encode(data).decode()
  style=soup.new_tag('style')
  style.string='\n'.join((ROOT/'assets'/sh).read_text(encoding='utf-8') for sh in ['concept.css','pages.css','product-first.css'])
  soup.head.append(style)
  script=soup.new_tag('script')
  script.string=(ROOT/'assets'/'concept.js').read_text(encoding='utf-8')
  soup.body.append(script)
  tab.set_content(str(soup),wait_until='load')
  tab.wait_for_timeout(120)
  tab.screenshot(path=str(P/f'{page}-{loc}-{width}.png'),full_page=True)
  tab.screenshot(path=str(P/f'{page}-{loc}-{width}-first.png'),full_page=False)
  data=tab.evaluate('''()=>({sw:document.documentElement.scrollWidth,cw:document.documentElement.clientWidth,hasHero:!!document.querySelector('.pf-hero'),hasArt:!!document.querySelector('.pf-browser'),text:document.querySelector('.pf-art-disclaimer')?.innerText,links:[...document.querySelectorAll('.pf-actions a')].map(x=>x.getAttribute('href')),pageTitle:document.title})''')
  results.append(dict(loc=loc,page=page,width=width,data=data,pageErrors=issues,overflow=data['sw']>data['cw']))
  ctx.close()
 b.close()
(P/'report.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
print(json.dumps(results,ensure_ascii=False,indent=2))
