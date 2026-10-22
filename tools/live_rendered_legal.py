"""Read-only actual browser rendering of existing public marketing legal routes.

Complements live_origin_audit.py: /en/terms HTML is a React shell with
no legal text in HTTP source. Run only on GitHub Actions with Chromium.
Captures no visitor identity, cookies, storage or full body, and makes no writes.
"""
import json
from datetime import datetime,timezone
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE='https://prompted.fi'
ROUTES=['/en/terms','/en/privacy','/fi/tietosuoja']
rows=[]
with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
    for path in ROUTES:
        page=browser.new_page(viewport={'width':1280,'height':900},locale='en-GB' if path.startswith('/en') else 'fi-FI')
        failures=[]
        page.on('pageerror',lambda e:failures.append(type(e).__name__))
        item={'path':path,'status':'UNVERIFIED'}
        try:
            response=page.goto(BASE+path,wait_until='domcontentloaded',timeout=25000)
            page.wait_for_timeout(2200)
            visible=page.locator('body').inner_text(timeout=10000)
            lower=visible.lower()
            title=page.title()
            third_party=('datadiscovery' in lower or 'design va oy' in lower or 'info@designva.fi' in lower)
            item.update({'http_code':response.status if response else None,
                         'final_url':page.url,'title':title[:140],
                         'rendered_chars':len(visible),
                         'mentions_design_va_or_datadiscovery':third_party,
                         'mentions_prompted_oy':'prompted oy' in lower,
                         'has_terms_heading':'terms of service' in lower or 'service terms' in lower,
                         'js_error_types':failures[:3]})
            if third_party:
                item['status']='WRONG_COMPANY_LEGAL_COPY'
            elif path=='/en/terms' and item['has_terms_heading'] and 'prompted oy' in lower:
                item['status']='PROMPTED_TERMS_RENDERED_REVIEW_REQUIRED'
            elif path=='/en/terms':
                item['status']='NO_VERIFIABLE_ENGLISH_TERMS'
            else:
                item['status']='RENDERED_NO_THIRD_PARTY_MARKERS' if len(visible)>100 else 'EMPTY_OR_UNVERIFIED'
        except Exception as e:
            item.update({'status':'FETCH_ERROR','error_type':type(e).__name__,
                         'error_summary':str(e).splitlines()[0][:160]})
        rows.append(item)
        page.close()
    browser.close()
report={'observed_utc':datetime.now(timezone.utc).isoformat(),
        'mode':'RENDERED_PUBLIC_PAGES_READ_ONLY',
        'routes':rows,
        'warning':'This shows present rendered output on the tested runner, not approval of service terms.'}
Path('tools/live_rendered_legal_results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
