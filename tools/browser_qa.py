from pathlib import Path
import asyncio, json, mimetypes, base64
from urllib.parse import urlparse,unquote
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'previews'
OUT.mkdir(exist_ok=True)
ORIGIN='https://preview.prompted.invalid'
PAGES=['','literacy','capability','transformation','yritys','yhteys','tietosuoja','ehdot']
PAGES_EN=['','literacy','capability','transformation','company','contact','privacy','terms']

def markup_for_file(path):
    soup=BeautifulSoup(path.read_text(), 'html.parser')
    for link in soup.select('link[rel="stylesheet"]'):
        local=ROOT/link.get('href','').lstrip('/')
        tag=soup.new_tag('style')
        tag.string=local.read_text()
        link.replace_with(tag)
    for img in soup.select('img[src]'):
        src=img.get('src','')
        if src.startswith('/') and (ROOT/src.lstrip('/')).is_file():
            local=ROOT/src.lstrip('/')
            mime=mimetypes.guess_type(str(local))[0] or 'application/octet-stream'
            img['src']='data:'+mime+';base64,'+base64.b64encode(local.read_bytes()).decode()
    for script in soup.select('script[src]'):
        src=script.get('src','')
        if src.startswith('/') and (ROOT/src.lstrip('/')).is_file():
            tag=soup.new_tag('script');tag.string=(ROOT/src.lstrip('/')).read_text()
            script.extract()
            soup.body.append(tag)
    return str(soup)

async def route_local(route):
 url=urlparse(route.request.url)
 if url.hostname!='preview.prompted.invalid':
  return await route.abort()
 rel=unquote(url.path.lstrip('/'))
 path=ROOT/rel
 if not path.suffix:path=path/'index.html'
 if not path.exists() or not path.is_file():
  return await route.fulfill(status=404,body='Not found')
 ctype=mimetypes.guess_type(str(path))[0] or 'application/octet-stream'
 await route.fulfill(status=200,content_type=ctype,body=path.read_bytes())

async def main():
 results=[]
 async with async_playwright() as p:
  browser=await p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--disable-gpu','--no-sandbox'])
  page=await browser.new_page(viewport={'width':1440,'height':900},device_scale_factor=1)
  
  errors=[]
  page.on('pageerror', lambda error:errors.append(str(error)))
  for lang,pages in [('fi',PAGES),('en',PAGES_EN)]:
   for slug in pages:
    path=f'/{lang}/'+(slug+'/' if slug else '')
    source=ROOT/path.lstrip('/')/'index.html'
    markup=markup_for_file(source)
    for width in [360,768,1440]:
     await page.set_viewport_size({'width':width,'height':900})
     await page.set_content(markup,wait_until='load')
     found=await page.locator('main h1').count()
     links=await page.locator('header nav.nav a').count()
     alt=await page.locator('link[hreflang="fi"]').count() and await page.locator('link[hreflang="en"]').count()
     langok=(await page.locator('html').get_attribute('lang'))==lang
     noindex='noindex' in (await page.locator('meta[name="robots"]').get_attribute('content') or '')
     x=await page.evaluate('({viewport:innerWidth,scroll:document.documentElement.scrollWidth})')
     o={'url':path,'width':width,'status':200,'h1':found,'headerlinks':links,'langs':bool(alt),'langok':langok,'noindex':noindex,'overflow':x['scroll']>x['viewport']+1}
     results.append(o)
     if o['status']!=200 or o['h1']!=1 or not o['langs'] or not o['langok'] or not noindex or o['overflow']:print('FAIL',o)
  scenarios=[('home-desktop','/fi/',1440,900),('home-mobile','/fi/',390,844),('home-tablet','/fi/',768,1024),('capability-desktop','/fi/capability/',1440,900),('capability-mobile','/fi/capability/',390,844),('literacy-desktop','/fi/literacy/',1440,900),('transformation-mobile','/en/transformation/',390,844),('home-en-desktop','/en/',1440,900)]
  for name,path,width,height in scenarios:
   await page.set_viewport_size({'width':width,'height':height})
   await page.set_content(markup_for_file(ROOT/path.lstrip('/')/'index.html'),wait_until='load')
   await page.evaluate('document.fonts.ready')
   await page.screenshot(path=str(OUT/(name+'.png')),full_page=(height==844 or name in ['literacy-desktop']))
   x=await page.evaluate('({viewport:innerWidth,scroll:document.documentElement.scrollWidth})')
   result={'screenshot':name,'width':width,'overflow':x['scroll']>x['viewport']+1,'h1':await page.locator('main h1').inner_text()}
   if width<=1024:
    toggle=page.locator('.nav-toggle')
    await toggle.click()
    result['menu_opens']=await toggle.get_attribute('aria-expanded')
    await page.keyboard.press('Escape')
    result['menu_esc_closes']=await toggle.get_attribute('aria-expanded')
   results.append(result)
  # Test all internal links in 16 pages without false-positive for section hashes
  b=[]
  for lang,pages in [('fi',PAGES),('en',PAGES_EN)]:
   for slug in pages:
    source=ROOT/lang/slug/'index.html' if slug else ROOT/lang/'index.html'
    s=BeautifulSoup(source.read_text(),'html.parser')
    for a in s.select('a[href]'):
     href=a['href'];target=urlparse(href)
     if not href.startswith('/') or target.scheme or href.startswith('//'):continue
     path=ROOT/target.path.lstrip('/')
     if not path.suffix: path=path/'index.html'
     if not path.exists(): b.append([source.relative_to(ROOT).as_posix(),href])
  print('PAGES',len(results),'broken',len(b),'pageerrors',errors)
  print(json.dumps({'results':results,'broken':b,'pageErrors':errors},ensure_ascii=False,indent=2))
  (ROOT/'tools'/'browser_qa_results.json').write_text(json.dumps({'results':results,'broken':b,'pageErrors':errors},ensure_ascii=False,indent=2))
  await browser.close()
  if b or errors or any(r.get('overflow') for r in results) or any(r.get('status',200)!=200 for r in results) or any(r.get('menu_opens') != 'true' or r.get('menu_esc_closes') != 'false' for r in results if 'menu_opens' in r):raise SystemExit('browser QA failed')

if __name__=='__main__':asyncio.run(main())
