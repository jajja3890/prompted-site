"""Offline visual and automated accessibility preflight; never a live Vercel or human sign-off.

Captures FI/EN product page screenshots at mobile and desktop for review.
Uses a bundled axe-core script to flag critical/serious WCAG 2.x findings.
"""
from pathlib import Path
import json, base64, mimetypes
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
TARGET=ROOT/'tools'/'visual_review'
TARGET.mkdir(exist_ok=True)
FILES={
  'fi':['','literacy','capability','transformation','tutustu','tietosuoja','ehdot'],
  'en':['','literacy','capability','transformation','explore','privacy','terms'],
}
SHEET='\n'.join((ROOT/'assets'/s).read_text(encoding='utf-8') for s in ['concept.css','pages.css','product-first.css','product-system.css','buyer-experience.css'])
NAV=(ROOT/'assets'/'concept.js').read_text(encoding='utf-8')
DEMO=(ROOT/'assets'/'buyer-experience.js').read_text(encoding='utf-8')
AXE=ROOT/'node_modules'/'axe-core'/'axe.min.js'
if not AXE.is_file():
    raise SystemExit('Missing axe-core; run npm install --no-save --package-lock=false axe-core')
def prepare(lang,route):
    f=ROOT/lang/route/'index.html' if route else ROOT/lang/'index.html'
    soup=BeautifulSoup(f.read_text(encoding='utf-8'),'html.parser')
    for tag in soup.select('link[rel="stylesheet"],script[src]'):
        tag.decompose()
    for img in soup.select('img[src^="/assets/"]'):
        asset=ROOT/img['src'].lstrip('/')
        if asset.is_file():
            mime=mimetypes.guess_type(str(asset))[0] or 'application/octet-stream'
            img['src']='data:'+mime+';base64,'+base64.b64encode(asset.read_bytes()).decode('ascii')
    style=soup.new_tag('style');style.string=SHEET;soup.head.append(style)
    return str(soup)
results=[];failures=[]
with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
    for lang,routes in FILES.items():
        for route in routes:
            for width in ((390,) if route in ('tietosuoja','ehdot','privacy','terms') else (390,1440)):
                label=f'{lang}-{route or "home"}-{width}'
                page=browser.new_page(viewport={'width':width,'height':860},locale='fi-FI' if lang=='fi' else 'en-GB',reduced_motion='reduce')
                errors=[];req=[]
                page.on('pageerror',lambda exc: errors.append(str(exc)))
                page.on('request',lambda req_: req.append(req_.url))
                page.route('**/*',lambda r:r.abort())
                page.set_content(prepare(lang,route),wait_until='load')
                page.add_script_tag(content=NAV)
                if route in ('tutustu','explore'):
                    page.add_script_tag(content=DEMO)
                page.add_script_tag(path=str(AXE))
                page.evaluate('document.fonts.ready')
                screenshot=TARGET/f'{label}.png'
                page.screenshot(path=str(screenshot),full_page=True)
                result=page.evaluate("""async () => {
                  const r=await axe.run(document, {runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']},rules:{'region':{enabled:false}}});
                  return r.violations.map(x=>({id:x.id,impact:x.impact,description:x.help,nodes:x.nodes.map(n=>n.target).slice(0,6)}));
                }""")
                severe=[v for v in result if v['impact'] in ('critical','serious')]
                overflow=page.evaluate('document.documentElement.scrollWidth > innerWidth + 1')
                row={'page':label,'screenshot':str(screenshot.relative_to(ROOT)),'serious_or_critical':severe,'moderate_or_minor':[v for v in result if v not in severe],'js_errors':errors,'unexpected_requests':req,'horizontal_overflow':overflow}
                results.append(row)
                if severe or errors or req or overflow:failures.append(label)
                page.close()
    browser.close()
report={'status':'FAIL' if failures else 'PASS','screenshots':len(results),'failed_pages':failures,'results':results,'scope':'Offline in-memory Chromium: responsive visuals, automated axe-core rules. NOT human visual approval, live hosting or comprehensive WCAG certification.'}
(ROOT/'tools'/'visual_release_results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':report['status'],'screenshots':len(results),'failed_pages':failures,'violations':[{ 'page':x['page'],'serious':x['serious_or_critical']} for x in results if x['serious_or_critical']],'notes':'Screenshots saved to CI artifact for human visual review.'},ensure_ascii=False))
if failures:raise SystemExit(1)
