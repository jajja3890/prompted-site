"""Quick reproducible structural gate for Capability dual-demo v2 (no new dependencies)."""
from pathlib import Path
import re
R=Path(__file__).resolve().parent.parent
pages=[]
for lang in ('fi','en'):
 for path in R.joinpath(lang).rglob('index.html'):
  pages.append(path)
assert len(pages)==18, f'Expected 18 localized HTML files, got {len(pages)}'
for f in pages:
 s=f.read_text(encoding='utf-8')
 assert len(re.findall(r'<main\\b',s))==1, str(f)
 assert 'noindex' in s, str(f)
 assert 'href="/'+f.parent.parent.name+'/"' in s, str(f)
 assert '>Demo<' in s, 'Missing Demo navigation: '+str(f)
for lang,route in (('fi','tutustu'),('en','explore')):
 s=R.joinpath(lang,route,'index.html').read_text()
 for marker in ('data-capability-demo','data-enter="buyer"','data-enter="learner"','data-pane="buyer"','data-pane="learner"','data-calc="people"'):
  assert marker in s, f'Missing {marker} in {lang} demo'
js=R.joinpath('assets/buyer-experience.js').read_text()
for forbidden in ('fetch(', 'XMLHttpRequest','sendBeacon','localStorage','sessionStorage','document.cookie'):
 assert forbidden not in js, forbidden
print('PASS: 18 FI/EN pages, dual-demo routes and no client network/storage APIs')
