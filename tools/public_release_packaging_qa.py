"""Regression test for producing the eventual STATIC public marketing bundle.

Never calls the release CLI, changes approvals, uses credentials, uploads an artifact
or deploys. The in-memory/temp release is an intentionally isolated software test.
The REAL public-release gate must still be BLOCKED.
"""
from pathlib import Path
from tempfile import TemporaryDirectory
from xml.etree import ElementTree
from bs4 import BeautifulSoup
import json

from public_release_gate import (
    ROOT, ROUTES, MARKERS, LEGAL_OPEN, GATES, check, make_public,
)

def must(condition, reason):
    if not condition:
        raise AssertionError(reason)

# Confirm all public approvals remain pending and the proposed retention
# policy cannot accidentally be deemed implemented through JSON sign-off.
blockers = check(ROOT / 'PUBLIC_RELEASE_APPROVALS.example.json')
must(bool(blockers), 'Release gate unexpectedly eligible')
must(any('owner_release' in b for b in blockers), 'Owner permission gate absent')
for lang, token in (('fi', 'suunniteltu säilytyskäytäntö'),
                    ('en', 'our proposed retention practice')):
    must(any(lang in b and token in b for b in blockers),
         f'{lang}: unimplemented retention promise must still block public release')

checks = 0
with TemporaryDirectory(prefix='prompted-isolated-packaging-test-') as tmp:
    dest = Path(tmp) / 'release'
    # Function-level packaging test, deliberately isolated and unpublishable.
    # NEVER bypass check() in the real --prepare CLI entrypoint.
    make_public(dest)
    pages = sorted(dest.glob('*/**/index.html'))
    must(len(pages) == 18, f'Public package has {len(pages)} pages instead of 18')
    for lang, routes in ROUTES.items():
        for route in routes:
            path = dest / lang / route / 'index.html'
            must(path.exists(), f'Missing output: {lang}/{route}')
            soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
            must(soup.find('main', id='main') is not None, 'Missing main landmark')
            must(len(soup.find_all('h1')) == 1, 'Incorrect h1 count')
            must(not soup.select('.legal-draft'), 'Legal draft banner still visible')
            must(not soup.find('meta', attrs={'name': 'robots', 'content': 'noindex,nofollow'}),
                 'Preview robots flag remains in packaged HTML')
            html = str(soup)
            must(not any(marker in html for marker in MARKERS), 'Draft preview marker remains')
            must('noindex' not in html.lower(), 'HTML still contains a noindex restriction')
            for node in soup.find_all(['img', 'script', 'link']):
                url = node.get('src') or node.get('href') or ''
                if url.startswith('/assets/'):
                    must((dest / url.lstrip('/')).is_file(),
                         f'{lang}/{route}: missing bundled referenced asset: {url}')
            checks += 1

    rootsoup = BeautifulSoup((dest/'index.html').read_text(encoding='utf-8'), 'html.parser')
    must('noindex' not in str(rootsoup).lower(), 'Root page still marked noindex')
    config = json.loads((dest/'vercel.json').read_text(encoding='utf-8'))
    headers = {h['key'].lower():h['value'] for group in config['headers']
               for h in group['headers']}
    must('x-robots-tag' not in headers, 'Unintended noindex HTTP header in release')
    must("script-src 'self'" in headers.get('content-security-policy',''), 'Release CSP lost')
    must(headers.get('x-frame-options') == 'DENY', 'Release frame protection lost')
    must('Allow: /' in (dest/'robots.txt').read_text(), 'Public robots not enabled')
    must('Disallow: /' not in (dest/'robots.txt').read_text(), 'Robots still blocked')
    sitemap = ElementTree.parse(dest/'sitemap.xml')
    ns = {'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls = [e.text for e in sitemap.findall('.//s:loc',ns)]
    must(len(urls) == 18 and len(set(urls)) == 18,
         'Sitemap must have 18 unique URLs')
    must(all(u.startswith('https://prompted.fi/') for u in urls),
         'Incorrect public canonical domain')
    actual_assets={p.name for p in (dest/'assets').iterdir()}
    must('hero-material.webp' not in actual_assets, 'Unapproved unused artwork bundled')
    must('wordmark-light.svg' not in actual_assets, 'Unused wordmark bundled')

print(json.dumps({
    'result':'PASS','tested_public_pages':checks,'sitemap_urls':18,
    'test_mode':'isolated temporary package, immediately deleted',
    'real_public_release_status':'BLOCKED','actual_artifact_created':False,
    'accountable_approvals':list(GATES),
    'note':'This is not a publication, legal approval, domain change or rights validation.'
},ensure_ascii=False))
