"""Verify generated Prompted marketing site links, assets, anchors and locale SEO.

Offline preflight; no network, production credentials or customer data.
This rejects broken routes before a public-domain cutover.
"""
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
from bs4 import BeautifulSoup
import json

ROOT=Path(__file__).resolve().parents[1]
ORIGIN='https://prompted.fi'
PAIRS=[
 ('',''),('literacy','literacy'),('capability','capability'),
 ('transformation','transformation'),('yritys','company'),
 ('yhteys','contact'),('tietosuoja','privacy'),('ehdot','terms'),
 ('tutustu','explore')
]
COUNTS={'pages':0,'local_references':0,'anchor_targets':0,'seo_links':0,'legacy_redirects':0}
FAIL=[]
DOCS={}
def local_path(lang,route):
    return '/'+lang+'/'+(route+'/' if route else '')
for fi,en in PAIRS:
    for lang,route in [('fi',fi),('en',en)]:
        path=local_path(lang,route)
        target=ROOT/path.lstrip('/')/'index.html'
        if not target.is_file():
            FAIL.append(f'Missing generated page: {path}')
            continue
        DOCS[path]=BeautifulSoup(target.read_text(encoding='utf-8'),'html.parser')
        COUNTS['pages']+=1
DOCS['/']=BeautifulSoup((ROOT/'index.html').read_text(encoding='utf-8'),'html.parser')

# Public footer must never revert to prelaunch or location copy.
for route,soup in DOCS.items():
    if route=='/':
        continue
    footer=soup.select_one('footer.footer')
    if footer is None:
        FAIL.append(f'{route}: public footer is missing')
        continue
    footer_text=footer.get_text(' ',strip=True)
    for obsolete in ('Turku, Finland','PREVIEW','NOT PUBLISHED'):
        if obsolete in footer_text:
            FAIL.append(f'{route}: obsolete footer text {obsolete}')
    if 'Prompted Oy' not in footer_text or '3550114-7' not in footer_text or '© 2026 Prompted Oy' not in footer_text:
        FAIL.append(f'{route}: public company identity or copyright is incomplete')

# Home design must contain one genuine image asset and no old PEOPLE FIRST tile.
for lang in ('fi','en'):
    doc=DOCS[f'/{lang}/']
    if len(doc.select('.pf-home .pf-human-editorial img[src="/assets/prompted-editorial-one-person.webp"]')) != 1:
        FAIL.append(f'/{lang}/: required single editorial hero photo missing')
    if len(doc.select('.art-section--human .art-human-content h2')) != 1:
        FAIL.append(f'/{lang}/: airy PEOPLE FIRST section missing')
    if doc.select('.art-section--human .art-type-panel'):
        FAIL.append(f'/{lang}/: legacy PEOPLE FIRST box still present')

# The Finnish site should not regress to decorative English marketing labels.
# Product names Literacy, Capability, Transformation and Prompted Data remain intentional.
FI_FORBIDDEN_COPY=(
 '03 / SOLUTIONS','01 / FOUNDATION','02 / REAL WORK','03 / AT SCALE',
 'PROMPTED / PEOPLE × TECHNOLOGY × WORK','HUMAN CAPABILITY / REAL WORK',
 'PEOPLE FIRST','WORK → SUPPORT → EVIDENCE',
 'Companies grow when people grow.','Business ID 3550114-7',
 'PROMPTED / CAPABILITY DEMO','CAPABILITY / WORK → EVIDENCE',
 'HR-, People- ja L&D-johdolle','COACH-TUKI'
)
for route,soup in DOCS.items():
 if not route.startswith('/fi/'):continue
 visible=soup.get_text(' ',strip=True)
 for phrase in FI_FORBIDDEN_COPY:
  if phrase in visible:FAIL.append(f'{route}: avoid English marketing label {phrase}')

def resolve_asset(path):
    # A slash-final URL is a route, all other source paths are files.
    decoded=unquote(path)
    if '\\' in decoded:
        return None
    candidate=ROOT/decoded.lstrip('/')
    try:
        if not candidate.resolve().is_relative_to(ROOT.resolve()):
            return None
    except (ValueError,OSError):
        return None
    return candidate/'index.html' if decoded.endswith('/') or decoded=='' else candidate

for path,soup in DOCS.items():
    base=ORIGIN+path
    for node in soup.find_all(['a','img','script','link','source']):
        attr='href' if node.name in ('a','link') else 'src'
        value=node.get(attr)
        if not value:
            continue
        parts=urlsplit(urljoin(base,value))
        if parts.scheme not in ('http','https') or parts.hostname not in ('prompted.fi','www.prompted.fi'):
            continue
        local=unquote(parts.path or '/')
        file=resolve_asset(local)
        COUNTS['local_references']+=1
        if file is None or not file.is_file():
            FAIL.append(f'{path}: broken {node.name} {value} -> {local}')
            continue
        if parts.fragment and node.name=='a':
            dest=DOCS.get(local)
            if dest is None:
                dest=BeautifulSoup(file.read_text(encoding='utf-8'),'html.parser')
                DOCS[local]=dest
            fragment=unquote(parts.fragment)
            COUNTS['anchor_targets']+=1
            if dest.find(id=fragment) is None and dest.find(attrs={'name':fragment}) is None:
                FAIL.append(f'{path}: missing anchor {value}')

for fi,en in PAIRS:
    expected={'fi':ORIGIN+local_path('fi',fi),'en':ORIGIN+local_path('en',en)}
    for lang,route in [('fi',fi),('en',en)]:
        path=local_path(lang,route)
        soup=DOCS.get(path)
        if not soup:
            continue
        canonical=soup.select_one('link[rel="canonical"]')
        if canonical is None or canonical.get('href')!=expected[lang]:
            FAIL.append(f'{path}: canonical does not match intended path')
        else:
            COUNTS['seo_links']+=1
        for key in ('fi','en','x-default'):
            alternate=soup.find('link',attrs={'rel':'alternate','hreflang':key})
            want=expected['fi' if key=='x-default' else key]
            if alternate is None or alternate.get('href')!=want:
                FAIL.append(f'{path}: wrong hreflang {key}')
            else:
                COUNTS['seo_links']+=1
        # Marketing and canonical SEO must point to real shipped assets.
        ogimage=soup.find('meta',attrs={'property':'og:image'})
        image_url=ogimage.get('content','') if ogimage else ''
        image_parts=urlsplit(image_url)
        if image_parts.hostname!='prompted.fi' or not image_parts.path.startswith('/assets/') or not resolve_asset(image_parts.path).is_file():
            FAIL.append(f'{path}: Open Graph image not available in generated package')
        else:
            COUNTS['seo_links']+=1
        switch=soup.select_one('.bar-right .language a[href]')
        other='en' if lang=='fi' else 'fi'
        other_route=en if lang=='fi' else fi
        if switch is None or switch.get('href')!=local_path(other,other_route):
            FAIL.append(f'{path}: desktop language switch is not reciprocal')
        else:
            COUNTS['seo_links']+=1
        mobile=soup.select_one('nav.mobile-nav')
        if mobile is None or mobile.find('a',href=local_path(other,other_route)) is None:
            FAIL.append(f'{path}: mobile language switch is missing')
        else:
            COUNTS['seo_links']+=1
        og=soup.find('meta',attrs={'property':'og:url'})
        if og is None or og.get('content')!=expected[lang]:
            FAIL.append(f'{path}: Open Graph URL mismatch')
        else:
            COUNTS['seo_links']+=1
# Preserve legacy inbound links both before and after Vercel's trailing-slash normalization.
legacy_redirects={
    '/capability':'/fi/capability/',
    '/literacy':'/fi/literacy/',
    '/transformation':'/fi/transformation/',
    '/transformerism':'/fi/transformation/',
    '/fi/transformerism':'/fi/transformation/',
    '/en/transformerism':'/en/transformation/',
}
redirects=json.loads((ROOT/'vercel.json').read_text(encoding='utf-8')).get('redirects',[])
for source,destination in legacy_redirects.items():
    for candidate in (source,source+'/'):
        matching=[r for r in redirects if r.get('source')==candidate]
        COUNTS['legacy_redirects']+=1
        if len(matching)!=1 or matching[0].get('destination')!=destination or matching[0].get('permanent') is not True:
            FAIL.append(f'Legacy URL redirect missing or invalid: {candidate} -> {destination}')

# Prevent iPhone emoji arrows and displaced offer-card action icons.
import re
for route,soup in DOCS.items():
    if route=='/':
        continue
    html_string=str(soup)
    if re.search(r'↗(?!︎)',html_string):
        FAIL.append(f'{route}: bare U+2197 emoji-capable arrow without text variation selector')
for lang in ('fi','en'):
    home=DOCS.get(f'/{lang}/')
    if home:
        tiles=home.select('.offer-strip a.offer-tile')
        if len(tiles)!=3:
            FAIL.append(f'/{lang}/: expected three linked offer cards, found {len(tiles)}')
        for tile in tiles:
            if tile.select_one('.tile-foot[aria-hidden="true"] svg path') is None:
                FAIL.append(f'/{lang}/: offer card is missing semantic-safe SVG arrow')
css=(ROOT/'assets'/'concept.css').read_text(encoding='utf-8')
if 'position:absolute;right:var(--edge);margin-top:-50px' in css:
    FAIL.append('mobile offer-card icons still use legacy absolute-position/negative-margin workaround')

# Every internal local reference resolves; no server or remote route availability implied.
result={'status':'PASS' if not FAIL else 'FAIL','counts':COUNTS,'failures':FAIL,
        'scope':'18 FI/EN static pages, internal links, anchors, static assets, reciprocal canonical/hreflang/OG URLs; offline only'}
(ROOT/'tools'/'site_route_integrity_results.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
if FAIL:
    raise SystemExit(1)
