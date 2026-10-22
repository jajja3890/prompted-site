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
COUNTS={'pages':0,'local_references':0,'anchor_targets':0,'seo_links':0}
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
        og=soup.find('meta',attrs={'property':'og:url'})
        if og is None or og.get('content')!=expected[lang]:
            FAIL.append(f'{path}: Open Graph URL mismatch')
        else:
            COUNTS['seo_links']+=1
# Every internal local reference resolves; no server or remote route availability implied.
result={'status':'PASS' if not FAIL else 'FAIL','counts':COUNTS,'failures':FAIL,
        'scope':'18 FI/EN static pages, internal links, anchors, static assets, reciprocal canonical/hreflang/OG URLs; offline only'}
(ROOT/'tools'/'site_route_integrity_results.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
if FAIL:
    raise SystemExit(1)
