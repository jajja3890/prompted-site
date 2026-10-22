"""Serve generated static pages through real HTTP and test browser resource loading.

Simulates *configured* Vercel response headers on an isolated 127.0.0.1 origin.
This does NOT prove actual Vercel deployment headers, cookie policy, SSO or real device behavior.
"""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
import json
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
config=json.loads((ROOT/'vercel.json').read_text(encoding='utf-8'))
HEADERS={x['key']:x['value'] for group in config['headers'] for x in group['headers']}
ROUTES={
    'fi':['','literacy','capability','transformation','yritys','yhteys','tietosuoja','ehdot','tutustu'],
    'en':['','literacy','capability','transformation','company','contact','privacy','terms','explore']
}
class PreviewHandler(SimpleHTTPRequestHandler):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,directory=str(ROOT),**kwargs)
    def end_headers(self):
        for name,value in HEADERS.items():
            self.send_header(name,value)
        super().end_headers()
    def log_message(self,fmt,*args):
        pass

server=ThreadingHTTPServer(('127.0.0.1',0),PreviewHandler)
thread=Thread(target=server.serve_forever,daemon=True)
thread.start()
origin=f'http://127.0.0.1:{server.server_port}'
failures=[]
checks=0

def must(test,location,reason):
    global checks
    checks+=1
    if not test:
        failures.append(f'{location}: {reason}')

try:
    with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
        for lang,routes in ROUTES.items():
            for route in routes:
                path=f'/{lang}/'+(route+'/' if route else '')
                label=path
                context=browser.new_context(viewport={'width':390,'height':844},
                                            locale='fi-FI' if lang=='fi' else 'en-GB')
                page=context.new_page()
                page_errors=[]
                broken_http=[]
                outside=[]
                csp=[]
                page.add_init_script("""(() => {
                  window.__policyViolations=[];
                  addEventListener('securitypolicyviolation',event=>{
                    window.__policyViolations.push({
                      directive:event.effectiveDirective,blocked:event.blockedURI
                    });
                  });
                })()""")
                page.on('pageerror',lambda err:page_errors.append(str(err)))
                page.on('response',lambda resp:broken_http.append((resp.status,resp.url)) if resp.status>=400 else None)
                page.route('**/*',lambda r:r.continue_() if r.request.url.startswith(origin+'/') else (outside.append(r.request.url),r.abort()))
                try:
                    response=page.goto(origin+path,wait_until='load',timeout=15000)
                    must(response is not None and response.status==200,label,'route is not HTTP 200')
                    headers=response.headers if response else {}
                    must('noindex' in headers.get('x-robots-tag',''),label,'HTTP X-Robots-Tag missing')
                    must("script-src 'self'" in headers.get('content-security-policy',''),label,'configured CSP missing')
                    must("style-src 'self'" in headers.get('content-security-policy',''),label,'style CSP missing')
                    must(page.locator('main#main').count()==1,label,'rendered main missing')
                    must(page.locator('h1').count()==1,label,'rendered heading missing')
                    must(len(page.evaluate('document.styleSheets'))>=4,label,'linked CSS was not loaded')
                    must(page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'),label,'mobile overflow')
                    for asset in page.locator('img[src^="/assets/"]').all():
                        # Lazy-loaded below-fold art should be checked only after a
                        # user-like scroll; testing pre-scroll completion is invalid.
                        asset.scroll_into_view_if_needed(timeout=10000)
                        decoded=asset.evaluate('(img)=>img.decode().then(()=>true).catch(()=>false)')
                        must(decoded,label,'image did not load even after entering viewport')
                    if route in ('tutustu','explore'):
                        must(page.locator('[data-enter="buyer"]').count()==1,label,'buyer entry missing')
                        page.locator('[data-enter="buyer"]').click()
                        must(page.locator('[data-pane="buyer"]').is_visible(),label,'buyer script does not run under CSP')
                        page.locator('[data-report="evidence"]').click()
                        must('14' in page.locator('[data-report-body]').inner_text(),label,'report JS not working')
                        page.locator('.dx-view-switch [data-view="learner"]').click()
                        must(page.locator('[data-pane="learner"]').is_visible(),label,'learner route does not open')
                        page.locator('input[name="dx-friction"][value="quality"]').check()
                        must(page.locator('[data-coach-title]').inner_text().strip()!='',label,'coach content does not respond')
                    csp=page.evaluate('window.__policyViolations || []')
                    must(not page_errors,label,'JavaScript runtime exceptions: '+repr(page_errors))
                    must(not broken_http,label,'HTTP resource errors: '+repr(broken_http))
                    must(not outside,label,'external resource requests blocked')
                    must(not context.cookies(),label,'unexpected site cookies')
                    must(page.evaluate('localStorage.length')==0,label,'unexpected browser storage')
                except Exception as exc:
                    failures.append(f'{label}: test failed: {str(exc).splitlines()[0][:200]}')
                finally:
                    page.close()
                    context.close()
        browser.close()
finally:
    server.shutdown()
    server.server_close()
    thread.join(timeout=3)

result={
 'status':'PASS' if not failures else 'FAIL',
 'checks':checks,'routes':sum(map(len,ROUTES.values())),
 'failures':failures,
 'scope':'Local HTTP server with preview CSP and security headers from vercel.json; real Chromium navigation and static asset loading; no external requests or credentials',
 'excludes':'Deployed Vercel HTTP, SSO, real devices, production SEO, server caching and provider cookies'
}
(ROOT/'tools'/'staging_http_browser_qa_results.json').write_text(
 json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
if failures:
    raise SystemExit(1)
