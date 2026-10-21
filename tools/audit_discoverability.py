#!/usr/bin/env python3
"""SEO / AI discovery release checks for Prompted static site.
Runs both prelaunch and approved-production builds in an isolated temp folder.
No remote changes. Never writes to prompted.fi or GitHub.
"""
from __future__ import annotations
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_KEYS={'fi':['', 'literacy','capability','transformation','yritys','yhteys','tietosuoja','ehdot'],
               'en':['', 'literacy','capability','transformation','company','contact','privacy','terms']}
EXPECTED_URLS={f'https://prompted.fi/{lang}/{name+"/" if name else ""}' for lang,names in EXPECTED_KEYS.items() for name in names}
CHECKS=0

def check(assertion, reason):
    global CHECKS
    CHECKS+=1
    if not assertion: raise AssertionError(reason)

def audit_build(root:Path,production:bool):
    all_pages={}
    for lang,names in EXPECTED_KEYS.items():
        for name in names:
            path=root/lang/name/'index.html'
            check(path.is_file(),f'Missing {path}')
            soup=BeautifulSoup(path.read_text('utf-8'),'html.parser')
            url=f'https://prompted.fi/{lang}/{name+"/" if name else ""}'
            all_pages[url]=soup
            check(soup.html['lang']==lang,f'wrong language {path}')
            check(len(soup.select('h1'))==1,f'bad H1 count {path}')
            check(bool(soup.select_one('main')),f'no main {path}')
            title=soup.select_one('title')
            check(bool(title and 'Prompted' in title.text),f'no brand in title {path}')
            check(bool(soup.select_one('meta[name="description"]')),f'no description {path}')
            check(soup.select_one('link[rel="canonical"]')['href']==url,f'wrong canonical {path}')
            for alternate in soup.select('link[rel="alternate"][hreflang]'):
                check(alternate['href'] in EXPECTED_URLS,f'broken hreflang {path}')
            key={'':'home','literacy':'literacy','capability':'capability','transformation':'transformation',
                 'yritys':'company','company':'company','yhteys':'contact','contact':'contact',
                 'tietosuoja':'privacy','privacy':'privacy','ehdot':'terms','terms':'terms'}[name]
            rel={'fi':{'home':'','literacy':'literacy','capability':'capability','transformation':'transformation',
                       'company':'yritys','contact':'yhteys','privacy':'tietosuoja','terms':'ehdot'},
                 'en':{'home':'','literacy':'literacy','capability':'capability','transformation':'transformation',
                       'company':'company','contact':'contact','privacy':'privacy','terms':'terms'}}
            for l in ('fi','en'):
                ending=rel[l][key]
                expected=f'https://prompted.fi/{l}/{ending+"/" if ending else ""}'
                actual=[alt['href'] for alt in soup.select(f'link[rel="alternate"][hreflang="{l}"]')]
                check(actual==[expected],f'hreflang {l}: {path}: {actual} vs {expected}')
            blocks=soup.select('script[type="application/ld+json"]')
            check(len(blocks)==1,f'JSON-LD missing/duplicate {path}')
            data=json.loads(blocks[0].text)
            types=[node.get('@type') for node in data.get('@graph',[])]
            for t in ('Organization','WebSite','WebPage'):
                check(t in types,f'missing {t} JSON-LD {path}')
            if name in ('literacy','capability','transformation'):
                check('Service' in types,f'missing Service schema {path}')
            meta=soup.select_one('meta[name="robots"]')
            check(bool(meta),f'no robots directive {path}')
            check(('noindex' not in meta['content'])==production, f'wrong indexing state {path}')
            for tag in soup.select('a[href],img[src],link[href],script[src]'):
                href=tag.get('href') or tag.get('src') or ''
                if href.startswith('/') and not href.startswith('//'):
                    target=href.split('#',1)[0].split('?',1)[0]
                    if not target: continue
                    resource=root/target.lstrip('/')
                    if resource.is_dir(): resource=resource/'index.html'
                    check(resource.exists(),f'broken local link {href} in {path}')
            for nav_area in ('.nav-desktop','.nav-mobile'):
                n=soup.select_one(nav_area)
                check(bool(n),f'missing nav {nav_area} {path}')
                for product_slug,product_label in [('literacy','Literacy'),('capability','Capability'),('transformation','Transformation')]:
                    links=[a for a in n.select(f'a[href="/{lang}/{product_slug}/"]') if a.parent==n]
                    check(len(links)==1 and links[0].get_text(strip=True)==product_label,f'missing or wrong product navigation {path} {nav_area} {product_label}')
            check(not soup.select('script[src^="http"],iframe,form'),f'no tracking/embed/form on public pages {path}')
            check('Design VA' not in soup.get_text() and 'DataDiscovery' not in soup.get_text(),f'legacy legal copy {path}')
            public_text=soup.get_text(' ',strip=True)
            import re
            check(not re.search(r'\b(?:Prompted\s+)?(?:Basic|Pro)\b',public_text,re.IGNORECASE),f'internal placeholder surfaced {path}')
            check(not re.search(r'\bTransformerism\b',public_text,re.IGNORECASE),f'wrong public product label {path}')
            if name in ('transformation',):
                check('Transformation' in public_text,f'correct product name absent {path}')
                check('Transformation' in title.get_text(),f'correct product name absent in title {path}')

    # Hreflang must also be reciprocal; x-default home only.
    for url,soup in all_pages.items():
        for alt in soup.select('link[rel="alternate"][hreflang]'):
            if alt['hreflang']=='x-default': continue
            reciprocal=all_pages[alt['href']]
            check(any(x.get('href')==url for x in reciprocal.select('link[rel="alternate"][hreflang]')),f'hreflang not reciprocal {url}')
    for lang in ('fi','en'):
        home=all_pages[f'https://prompted.fi/{lang}/']
        for service in ['literacy','capability','transformation']:
            check(bool(home.select_one(f'a[href="/{lang}/{service}/"]')),f'unreachable {lang} {service}')
        literacy=all_pages[f'https://prompted.fi/{lang}/literacy/']
        check(len(literacy.select('.qa'))>=2,f'insufficient helpful questions {lang}')
        check(any('ai-act-service-desk.ec.europa.eu' in a.get('href','') for a in literacy.select('a')),f'official AI Act reference missing {lang}')
        transform=all_pages[f'https://prompted.fi/{lang}/transformation/']
        check(not any('ai-act-service-desk.ec.europa.eu' in a.get('href','') for a in transform.select('a')),f'irrelevant regulatory link on Transformation {lang}')
        company=all_pages[f'https://prompted.fi/{lang}/{"yritys" if lang=="fi" else "company"}/']
        check(bool(company.select_one('a[href="https://jarkkosjoman.com/"]')),f'founder profile link missing {lang}')
    css=(root/'assets/style.css').read_text('utf-8')
    check(bool(__import__('re').search(r'@media\s*\(max-width:\s*1150px\).*?\.nav-desktop\s*\{\s*display:\s*none\s*\}.*?\.nav-toggle\s*\{\s*display:\s*flex',css,__import__('re').S)),'tablet navigation menu is hidden')
    check('100dvh' in css,'mobile navigation must scroll when viewport is small')
    robots=(root/'robots.txt').read_text('utf-8')
    vercel=json.loads((root/'vercel.json').read_text('utf-8'))
    headers=[h for g in vercel['headers'] for h in g['headers']]
    noindex_headers=[h for h in headers if h['key'].lower()=='x-robots-tag']
    if production:
        check('OAI-SearchBot' in robots and 'Sitemap:' in robots, 'Search bot/sitemap production robots')
        check(not noindex_headers,'noindex production header found')
        sitemap=root/'sitemap.xml'
        check(sitemap.is_file(),'production sitemap missing')
        tree=ET.parse(sitemap)
        ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls=tree.findall('s:url',ns)
        actual={u.find('s:loc',ns).text for u in urls}
        check(actual==EXPECTED_URLS,f'sitemap mismatch missing={EXPECTED_URLS-actual} extra={actual-EXPECTED_URLS}')
        for u in urls:
            check(u.find('s:lastmod',ns).text=='2026-10-21','lastmod must be meaningful release date')
    else:
        check('Disallow: /' not in robots,'prelaunch robots hides noindex from crawlers')
        check(bool(noindex_headers),'prelaunch HTTP noindex missing')
        check(not (root/'sitemap.xml').exists(),'sitemap must not be published with prelaunch')
    return len(all_pages)

preview_pages=audit_build(ROOT,False)
with tempfile.TemporaryDirectory(prefix='prompted-seo-') as td:
    dst=Path(td)/'site'
    shutil.copytree(ROOT,dst,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    env={**os.environ,'PROMPTED_RELEASE':'approved-production','PROMPTED_APPROVAL':'reviewed-privacy-content-and-domain','PROMPTED_RC7_IMAGES_APPROVED':'both-image-studies-explicitly-approved'}
    subprocess.run([sys.executable,'build.py'],env=env,cwd=dst,check=True,capture_output=True,text=True)
    production_pages=audit_build(dst,True)
print(f'PASS: {CHECKS} assertions; preview {preview_pages} pages; production {production_pages} pages; no remote changes')
