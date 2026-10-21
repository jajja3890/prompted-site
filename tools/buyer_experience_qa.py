from pathlib import Path
import json, sys, mimetypes, base64
from urllib.parse import urlparse,unquote
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
base='https://prompted-local-review.invalid'
checks=[];fail=[]
styles='\n'.join((ROOT/'assets'/x).read_text() for x in ['concept.css','pages.css','product-first.css','product-system.css','buyer-experience.css'])
script=(ROOT/'assets'/'buyer-experience.js').read_text()
def load_document(page,lang,path):
 f=ROOT/lang/path/'index.html' if path else ROOT/lang/'index.html'
 s=BeautifulSoup(f.read_text(), 'html.parser')
 for img in s.select('img[src^="/assets/"]'):
  imgpath=ROOT/img.get('src','').lstrip('/')
  if imgpath.is_file():
   mim=mimetypes.guess_type(str(imgpath))[0] or 'application/octet-stream'
   img['src']='data:'+mim+';base64,'+base64.b64encode(imgpath.read_bytes()).decode('ascii')
 for tag in list(s.select('link[rel="stylesheet"],script[src]')):tag.decompose()
 st=s.new_tag('style');st.string=styles;s.head.append(st)
 page.set_content(str(s),wait_until='load',timeout=18000)
 if path in ('tutustu','explore'):page.add_script_tag(content=script)

def check(c,d):
 checks.append((d,bool(c)))
 if not c:fail.append(d)
def static_route(route):
 u=urlparse(route.request.url)
 candidate=(ROOT/unquote(u.path).lstrip('/'))
 if candidate.is_dir():candidate=candidate/'index.html'
 try:
  if not candidate.resolve().is_relative_to(ROOT.resolve()):raise ValueError('bad path')
  if candidate.is_file():route.fulfill(path=str(candidate),content_type=mimetypes.guess_type(str(candidate))[0] or 'application/octet-stream');return
 except Exception:pass
 route.fulfill(status=404,body='Not found')

with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 for lang,path in [('fi','tutustu'),('en','explore')]:
  for width in (320,390,768,1024,1440):
   page=browser.new_page(viewport={'width':width,'height':900},locale='fi-FI' if lang=='fi' else 'en-GB')
   page.route('**/*',static_route)
   errors=[];calls=[];page.on('pageerror',lambda e:errors.append(str(e)))
   page.on('request',lambda req:calls.append(req.url) if not req.url.startswith(base) else None)
   load_document(page,lang,path)
   check(page.locator('html').count()==1,f'{lang} {width}: parsed HTML')
   check(page.locator('[data-buyer-experience]').count()==1,f'{lang} {width}: experience root')
   check(page.evaluate('document.documentElement.scrollWidth <= window.innerWidth+1'),f'{lang} {width}: no sideways overflow initial')
   check(page.locator('main').count()==1,f'{lang} {width}: one main')
   check(page.locator('h1').count()==1,f'{lang} {width}: one h1')
   check(not errors,f'{lang} {width}: JS errors initial {errors}')
   check(not calls,f'{lang} {width}: no third party requests {calls}')
   if width in (390,1440):
    out=ROOT/'previews_buyer_led';out.mkdir(exist_ok=True)
    page.screenshot(path=str(out/f'experience-{lang}-{width}-intro.png'),full_page=width==390)
    page.locator('.be-shell').screenshot(path=str(out/f'experience-{lang}-{width}-workspace.png'))
    page.locator('[data-role="people"]').click()
    check(page.locator('[data-scenario="quality"]').count()==1,f'{lang} {width}: role reveals scenarios')
    page.locator('[data-scenario="quality"]').click()
    page.locator('[data-next]').click()
    check(page.locator('.be-coach-card').count()==1,f'{lang} {width}: coaching stage')
    original=page.locator('.be-coach-move').inner_text()
    page.locator('[data-friction="quality_uncertain"]').click()
    changed=page.locator('.be-coach-move').inner_text()
    check(changed!=original,f'{lang} {width}: coach decision adapts')
    page.locator('[data-support="independent"]').click()
    check(page.locator('.be-coach-card').count()==1,f'{lang} {width}: support change')
    page.locator('[data-next]').click()
    page.locator('[data-evidence="4"]').click()
    check('04' in page.locator('.be-evidence-grid').inner_text(),f'{lang} {width}: evidence')
    page.locator('[data-next]').click()
    check('20' in page.locator('.be-report-metrics').inner_text(),f'{lang} {width}: buyer fictional report')
    page.locator('[data-next]').click()
    val1=page.locator('[data-impact-hours]').inner_text()
    page.locator('[data-impact="minutes"]').fill('60')
    val2=page.locator('[data-impact-hours]').inner_text()
    check(val1!=val2,f'{lang} {width}: calculator reacts')
    page.locator('[data-impact="people"]').fill('40')
    val3=page.locator('[data-impact-hours]').inner_text()
    check(val2!=val3,f'{lang} {width}: second calculator variable reacts')
    page.screenshot(path=str(out/f'experience-{lang}-{width}-impact.png'),full_page=width==390)
    with page.expect_download() as dl:
     page.locator('[data-next]').click()
    d=dl.value
    check(d.suggested_filename.startswith('Prompted-example-summary'),f'{lang} {width}: downloadable buyer summary')
    page.locator('[data-reset]').click()
    check(page.locator('[data-role="people"]').get_attribute('aria-pressed')=='false',f'{lang} {width}: reset')
    check(page.evaluate('document.documentElement.scrollWidth <= window.innerWidth+1'),f'{lang} {width}: no sideways overflow after interaction')
    check(not errors,f'{lang} {width}: no runtime JS errors {errors}')
    check(not calls,f'{lang} {width}: no requests beyond same site {calls}')
   page.close()
 # marketing CTAs and language parity
 for lang in ('fi','en'):
  pth='tutustu' if lang=='fi' else 'explore'
  for path in ('','capability','literacy','transformation'):
   page=browser.new_page();load_document(page,lang,path)
   check(page.locator(f'a[href^="/{lang}/{pth}/"]').count()>0,f'{lang}/{path}: interactive CTA')
   page.close()
 browser.close()
report={'passed':len(checks)-len(fail),'total':len(checks),'failures':fail}
(ROOT/'tools'/'buyer_experience_qa_results.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(report,ensure_ascii=False))
if fail:raise SystemExit(1)
