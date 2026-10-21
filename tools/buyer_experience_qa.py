"""Capability two-perspective demo browser checks (FI/EN, no network or customer data).

Run from repo root with Playwright, BeautifulSoup and Chromium installed.
Renders the real generated HTML and bundled assets inside an offline browser.
This test is NOT a live Vercel, legal, accessibility certification or production release check.
"""
from pathlib import Path
import json, base64, mimetypes
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT/'assets'
styles = '\n'.join((ASSETS/name).read_text(encoding='utf-8') for name in (
    'concept.css','pages.css','product-first.css','product-system.css','buyer-experience.css'))
script = (ASSETS/'buyer-experience.js').read_text(encoding='utf-8')
nav_script = (ASSETS/'concept.js').read_text(encoding='utf-8')
checks=[]
failures=[]

def check(condition, label):
    checks.append(label)
    if not condition:
        failures.append(label)

def document(page, lang):
    rel='tutustu' if lang=='fi' else 'explore'
    soup=BeautifulSoup((ROOT/lang/rel/'index.html').read_text(encoding='utf-8'),'html.parser')
    for tag in soup.select('link[rel="stylesheet"],script[src]'):
        tag.decompose()
    for img in soup.select('img[src^="/assets/"]'):
        p=ROOT/img['src'].lstrip('/')
        if p.is_file():
            mime=mimetypes.guess_type(str(p))[0] or 'application/octet-stream'
            img['src']='data:'+mime+';base64,'+base64.b64encode(p.read_bytes()).decode('ascii')
    style=soup.new_tag('style')
    style.string=styles
    soup.head.append(style)
    page.set_content(str(soup),wait_until='load',timeout=25000)
    page.add_script_tag(content=nav_script)
    page.add_script_tag(content=script)

with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,**({'executable_path':'/usr/bin/chromium'} if Path('/usr/bin/chromium').is_file() else {}),args=['--no-sandbox','--disable-dev-shm-usage'])
    for lang in ('fi','en'):
        for width in (320,390,768,1024,1440):
            label=f'{lang}/{width}'
            page=browser.new_page(viewport={'width':width,'height':900},locale='fi-FI' if lang=='fi' else 'en-GB')
            errors=[]
            requests=[]
            page.on('pageerror',lambda exc:errors.append(str(exc)))
            page.on('request',lambda request:requests.append(request.url))
            page.route('**/*',lambda route:route.abort())
            document(page,lang)
            root=page.locator('[data-capability-demo]')
            check(root.count()==1,label+' root')
            check(page.locator('main').count()==1,label+' main')
            check(page.locator('h1').count()==1,label+' title')
            check(page.locator('[data-enter]').count()==2,label+' two paths')
            check(page.locator('[data-stage]').is_hidden(),label+' initially no stage')
            check(page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'),label+' initial no horizontal overflow')

            toggle=page.locator('.nav-toggle')
            if width<=1040:
                check(toggle.is_visible(),label+' mobile toggle available')
                toggle.click()
                check(toggle.get_attribute('aria-expanded')=='true',label+' mobile menu opens')
                check(page.locator('.mobile-nav').get_attribute('aria-hidden')=='false',label+' mobile menu accessibility state opens')
                demo_url=f'/{lang}/'+('tutustu' if lang=='fi' else 'explore')+'/'
                check(page.locator('.mobile-nav a[href="'+demo_url+'"]').count()==1,label+' one mobile Demo link')
                check(page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'),label+' mobile menu has no horizontal overflow')
                page.keyboard.press('Escape')
                check(toggle.get_attribute('aria-expanded')=='false',label+' Escape closes mobile menu')
            else:
                check(not toggle.is_visible(),label+' desktop menu has no mobile toggle')
            check(page.locator('[data-enter="buyer"] strong').inner_text().strip()==
                  ('Haluan kokeilla tilaajana.' if lang=='fi' else 'I want to try as a buyer.'),label+' exact buyer entry copy')
            check(page.locator('[data-enter="learner"] strong').inner_text().strip()==
                  ('Haluan kokeilla osallistujana.' if lang=='fi' else 'I want to try as a participant.'),label+' exact participant entry copy')

            page.locator('[data-enter="buyer"]').click()
            check(page.locator('[data-stage]').is_visible(),label+' buyer stage opens')
            check(page.locator('[data-pane="buyer"]').is_visible(),label+' buyer pane visible')
            check(page.locator('[data-pane="learner"]').is_hidden(),label+' learner pane hidden')
            check(page.locator('.dx-fiction').count()==1,label+' fictional buyer data clearly marked')
            page.locator('[data-report="evidence"]').click()
            check(page.locator('[data-report="evidence"]').get_attribute('aria-pressed')=='true',label+' report tab selected')
            check('14' in page.locator('[data-report-body]').inner_text(),label+' sample evidence displayed')
            page.locator('details.dx-optional summary').click()
            page.locator('input[data-calc="people"]').fill('40')
            check('920' in page.locator('[data-calc-result]').inner_text(),label+' impact assumptions update')
            check(page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'),label+' buyer no horizontal overflow')

            page.locator('.dx-view-switch [data-view="learner"]').click()
            check(page.locator('[data-pane="learner"]').is_visible(),label+' learner pane visible')
            check(page.locator('[data-pane="buyer"]').is_hidden(),label+' buyer pane hidden')
            previous=page.locator('[data-coach-title]').inner_text()
            page.locator('input[name="dx-friction"][value="quality"]').check()
            check(previous!=page.locator('[data-coach-title]').inner_text(),label+' coaching responds to friction')
            check(page.locator('.dx-evidence-steps').count()==1,label+' Evidence ladder')
            check(page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'),label+' learner no horizontal overflow')
            page.locator('.dx-view-switch [data-view="buyer"]').click()
            check(page.locator('[data-pane="buyer"]').is_visible(),label+' reversible switching')
            page.locator('[data-exit]').click()
            check(page.locator('[data-choice]').is_visible() and page.locator('[data-stage]').is_hidden(),label+' return to entry')
            check(not errors,label+' no JS errors: '+repr(errors))
            check(not requests,label+' no network requests: '+repr(requests))
            page.close()
    browser.close()

result={'status':'PASS' if not failures else 'FAIL','checks':len(checks),'failures':failures,
        'scope':'offline FI/EN Chromium at 320/390/768/1024/1440, two-path interactions and privacy boundary',
        'excludes':'live Vercel HTTP, protected preview, real device, WCAG certification'}
(ROOT/'tools'/'buyer_experience_qa_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
if failures:
    raise SystemExit(1)
