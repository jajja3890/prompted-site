"""Prompted marketing site: deterministic semantic / privacy / preview-safety gate.
No network, credentials, production dependency or synthetic user data.
"""
from pathlib import Path
from bs4 import BeautifulSoup
import json, re
ROOT=Path(__file__).resolve().parents[1]
LOG=[];FAIL=[]
langs={'fi':['','literacy','capability','transformation','yritys','yhteys','tietosuoja','ehdot','tutustu'],
       'en':['','literacy','capability','transformation','company','contact','privacy','terms','explore']}
for lang, routes in langs.items():
    for route in routes:
        target=ROOT/lang/route/'index.html'
        name=f'{lang}/{route or "home"}'
        soup=BeautifulSoup(target.read_text(encoding='utf-8'),'html.parser')
        h1=soup.find_all('h1');mains=soup.find_all('main'); titles=soup.find_all('title')
        must=lambda predicate, description: FAIL.append((name,description)) if not predicate else None
        must(len(mains)==1, f'exactly one main landmark (got {len(mains)})')
        must(len(h1)==1,'exactly one h1')
        must(len(titles)==1 and bool(titles[0].get_text(strip=True)),'one nonempty title')
        must(soup.find('a',class_='skip-link',href='#main') is not None,'skip link')
        must(soup.find('main',id='main') is not None,'main landmark id')
        must(soup.html.get('lang')==lang,'html lang')
        must(soup.find('meta',attrs={'name':'robots','content':'noindex,nofollow'}) is not None,'meta preview noindex')
        must(bool(soup.find('link',rel='canonical')),'canonical')
        must(all(bool(soup.find('link',attrs={'hreflang':l})) for l in ('fi','en','x-default')),'FI/EN alternates')
        must(bool(soup.find('meta',attrs={'property':'og:image'})),'share image')
        must(len(soup.find_all('a',href=''))==0,'no empty hrefs')
        must(not soup.find_all('a',href='#'),'no placeholder links')
        must(not soup.find_all('a',href=re.compile(r'^(javascript|data):',re.I)),'no script hrefs')
        must(not soup.find_all('script',src=re.compile(r'^https?://',re.I)),'no third-party scripts')
        must(not soup.find_all('iframe'),'no third-party embeds')
        must(not soup.find_all('form'),'no data collection forms')
        must(soup.select_one('nav[aria-label]') is not None,'named main navigation')
        mobile=soup.select_one('nav.mobile-nav')
        if mobile:
            mobile_routes=[a.get('href','').split('#')[0] for a in mobile.select('a[href]')]
            must(len(mobile_routes)==len(set(mobile_routes)),'no duplicate mobile navigation destinations')

        must(len(soup.select('h1#pf-heading, h1#ps-service-heading, main h1'))>=1,'semantic main title')
        for i,a in enumerate(soup.find_all('a')):
            accessible=(a.get_text(' ',strip=True) or a.get('aria-label') or (a.find('img') and a.find('img').get('alt')))
            must(bool(accessible),f'unnamed link #{i}')
        for i,img in enumerate(soup.find_all('img')):
            must('alt' in img.attrs,f'image missing alt #{i}')
        if route in ('literacy','capability','transformation'):
            must(bool(soup.find('a',href=f'/{lang}/'+('yhteys' if lang=='fi' else 'contact')+'/')),'commercial CTA to contact')
        if route=='':
            below_fold=soup.select_one('figure.art-figure img[src="/assets/hero-daylight.webp"]')
            must(below_fold is not None and below_fold.get('loading')=='lazy' and below_fold.get('decoding')=='async','non-critical H01 art defers loading and decoding')
        if route in ('tietosuoja','privacy','ehdot','terms'):
            must(('LUONNOS' if lang=='fi' else 'DRAFT') in soup.get_text(' ',strip=True),'legal content clearly marked draft')
            body=soup.get_text(' ',strip=True).lower()
            must(not any(other in body for other in ('datadiscovery','design va oy','info@designva.fi')),'no historical third-party terms or company identity')
            must('Prompted Oy' in soup.get_text(' ',strip=True),'Prompted company identity on legal pages')
            if route in ('tietosuoja','privacy'):
                must(len(soup.select('main .legal-section'))>=8,'privacy notice has explicit processing sections')
        if route in ('yhteys','contact'):
            must(bool(soup.find('a',href='mailto:jarkko@prompted.fi')),'direct mailto contact')
        if route in ('tutustu','explore'):
            js=(ROOT/'assets'/'buyer-experience.js').read_text(encoding='utf-8')
            must(bool(soup.select_one('[data-capability-demo]')),'Capability demo root')
            must(bool(soup.find('script',src='/assets/buyer-experience.js')),'local demo JavaScript')
            must(bool(soup.find('link',href='/assets/buyer-experience.css')),'local demo CSS')
            choices=soup.select('[data-enter]')
            must(len(choices)==2 and {x.get('data-enter') for x in choices}=={'buyer','learner'},'two distinct entry paths')
            panes=soup.select('[data-pane]')
            must(len(panes)==2 and {x.get('data-pane') for x in panes}=={'buyer','learner'},'two separate experiences')
            must(len(soup.select('[data-report]'))==2,'delivery and Evidence report tabs')
            must(bool(soup.select_one('[data-coach-title]')),'choice-dependent coaching content')
            must(len(soup.select('input[name="dx-friction"]'))==3,'three participant coaching choices')
            must(bool(soup.select_one('[data-calc-result]')),'optional impact calculator')
            must(bool(soup.select_one('.dx-fiction')),'fictional data disclosure')
            must(bool(soup.select_one('.dx-sample-banner')),'no-real-data disclosure')
            must('data-capability-demo' in js and 'changeCoach' in js and 'changeReport' in js,'correct demo logic shipped')
            must(bool(soup.find('a',href=f'/{lang}/capability/')),'navigation to Capability product page')

        LOG.append(name)
conf=json.loads((ROOT/'vercel.json').read_text())
headers={h['key']:h['value'] for group in conf.get('headers',[]) for h in group['headers']}
for key,word in [('X-Robots-Tag','noindex'),('Content-Security-Policy',"script-src 'self'"),('X-Frame-Options','DENY')]:
 if word not in headers.get(key,''):FAIL.append(('vercel',f'missing {key}: {word}'))
if 'Disallow: /' not in (ROOT/'robots.txt').read_text():FAIL.append(('robots','missing private preview block'))
for loc in ['concept.css','pages.css','product-first.css','product-system.css','concept.js','buyer-experience.js','buyer-experience.css','favicon.ico','share-prompted.jpg']:
 if not (ROOT/'assets'/loc).is_file():FAIL.append(('assets',loc))
report={'result':'PASS' if not FAIL else 'FAIL','pages':len(LOG),'checks':'semantic landmarks, FI/EN parity, 2-entry demo structure, preview safety, legal drafts, host headers','failures':FAIL}
(ROOT/'tools'/'prelaunch_gate_results.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(report,ensure_ascii=False))
if FAIL:raise SystemExit(1)
