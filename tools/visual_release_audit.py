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
                # Full-page screenshots do not necessarily trigger native loading="lazy".
                # Warm below-the-fold imagery with real scrolling and decode, then
                # return to the top before capturing the complete visual composition.
                lazy_images=page.locator('main img[loading="lazy"]')
                lazy_count=lazy_images.count()
                failed_lazy=[]
                for img_index in range(lazy_count):
                    art=lazy_images.nth(img_index)
                    art.scroll_into_view_if_needed(timeout=10000)
                    loaded=art.evaluate('img => img.decode().then(() => img.naturalWidth > 0 && img.naturalHeight > 0).catch(() => false)')
                    if not loaded:
                        failed_lazy.append(img_index)
                page.evaluate('window.scrollTo(0,0)')
                if failed_lazy:
                    failures.append(label+': lazy artwork not decoded '+repr(failed_lazy))
                screenshot=TARGET/f'{label}.png'
                page.screenshot(path=str(screenshot),full_page=True)
                result=page.evaluate("""async () => {
                  const r=await axe.run(document, {runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']},rules:{'region':{enabled:false}}});
                  return r.violations.map(x=>({id:x.id,impact:x.impact,description:x.help,nodes:x.nodes.map(n=>n.target).slice(0,6)}));
                }""")
                severe=[v for v in result if v['impact'] in ('critical','serious')]
                overflow=page.evaluate('document.documentElement.scrollWidth > innerWidth + 1')
                row={'page':label,'screenshot':str(screenshot.relative_to(ROOT)),'serious_or_critical':severe,'moderate_or_minor':[v for v in result if v not in severe],'js_errors':errors,'unexpected_requests':req,'horizontal_overflow':overflow,'lazy_images_decoded':lazy_count-len(failed_lazy),'lazy_image_failures':failed_lazy}
                results.append(row)
                if severe or errors or req or overflow:failures.append(label)
                # The initial Demo selector is not enough: capture and audit both
                # complete buyer and participant experiences at 390/1440 px.
                if route in ('tutustu','explore'):
                    page.locator('[data-enter="buyer"]').click()
                    for view in ('buyer','learner'):
                        if view=='learner':
                            page.locator('.dx-view-switch [data-view="learner"]').click()
                        state_label=f'{label}-{view}'
                        state_shot=TARGET/f'{state_label}.png'
                        page.screenshot(path=str(state_shot),full_page=True)
                        state_result=page.evaluate("""async () => {
                          const r=await axe.run(document, {runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']},rules:{'region':{enabled:false}}});
                          return r.violations.map(x=>({id:x.id,impact:x.impact,description:x.help,nodes:x.nodes.map(n=>n.target).slice(0,6)}));
                        }""")
                        state_severe=[v for v in state_result if v['impact'] in ('critical','serious')]
                        state_overflow=page.evaluate('document.documentElement.scrollWidth > innerWidth + 1')
                        state_row={'page':state_label,'screenshot':str(state_shot.relative_to(ROOT)),'serious_or_critical':state_severe,'moderate_or_minor':[v for v in state_result if v not in state_severe],'js_errors':errors,'unexpected_requests':req,'horizontal_overflow':state_overflow}
                        results.append(state_row)
                        if state_severe or errors or req or state_overflow:failures.append(state_label)
                page.close()
    browser.close()
report={'status':'FAIL' if failures else 'PASS','screenshots':len(results),'failed_pages':failures,'results':results,'scope':'Offline in-memory Chromium with scrolled/decoded lazy artwork before screenshot: responsive visuals, automated axe-core rules. NOT human visual approval, live hosting or comprehensive WCAG certification.'}
(ROOT/'tools'/'visual_release_results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':report['status'],'screenshots':len(results),'failed_pages':failures,'violations':[{ 'page':x['page'],'serious':x['serious_or_critical']} for x in results if x['serious_or_critical']],'notes':'Screenshots saved to CI artifact for human visual review.'},ensure_ascii=False))
if failures:raise SystemExit(1)
