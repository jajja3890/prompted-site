"""Serve actual built static assets over localhost; do not touch Vercel."""
from pathlib import Path
from playwright.sync_api import sync_playwright
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
import threading, json
ROOT=Path(__file__).resolve().parents[1]
server=ThreadingHTTPServer(('127.0.0.1',0),partial(SimpleHTTPRequestHandler,directory=str(ROOT)))
thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
base=f'http://127.0.0.1:{server.server_port}'
issues=[];checks=[]
with sync_playwright() as pw:
 browser=pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for lang in ('fi','en'):
  for route in ('','literacy/','capability/','transformation/'):
   url=f'{base}/{lang}/{route}'
   page=browser.new_page(viewport={'width':390,'height':844},device_scale_factor=1)
   page_errors=[];page.on('pageerror',lambda exc:page_errors.append(str(exc)))
   res=page.goto(url,wait_until='networkidle')
   if not res or res.status!=200:issues.append((url,'unexpected response',res.status if res else None))
   if page_errors:issues.append((url,'browser error',page_errors))
   if page.locator('main').count()!=1:issues.append((url,'main landmark count'))
   if page.locator('h1').count()!=1:issues.append((url,'h1 count'))
   if page.locator('link[rel=stylesheet]').count()!=4:issues.append((url,'stylesheets'))
   # Ensure local CSS/image/scripts really load via HTTP.
   resources=page.evaluate('''()=>performance.getEntriesByType('resource').map(r=>({url:r.name,type:r.initiatorType}))''')
   if any(not x['url'].startswith(base) for x in resources):issues.append((url,'cross-domain resources',resources))
   if any(x['url'].startswith(base) and x['url'].endswith('.css') and not x['type']=='link' for x in resources):issues.append((url,'stylesheet load problem'))
   cookies=page.context.cookies(); storage=page.evaluate('''()=>({local:localStorage.length,session:sessionStorage.length})''')
   if cookies or any(storage.values()):issues.append((url,'unexpected browser storage',str(cookies)+str(storage)))
   if page.evaluate('document.documentElement.scrollWidth>innerWidth+1'):issues.append((url,'horizontal overflow'))
   btn=page.locator('.nav-toggle');btn.click()
   if btn.get_attribute('aria-expanded')!='true':issues.append((url,'mobile nav open'))
   page.keyboard.press('Escape')
   if btn.get_attribute('aria-expanded')!='false':issues.append((url,'mobile nav dismiss'))
   checks.append({'page':f'{lang}/{route}','status':res.status,'resources':len(resources),'storage':'none'})
   page.close()
 browser.close()
server.shutdown()
report={'result':'PASS' if not issues else 'FAIL','checks':len(checks),'pages':checks,'failures':issues}
(ROOT/'tools'/'http_smoke_results.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='pages'},ensure_ascii=False))
if issues:raise SystemExit(1)
