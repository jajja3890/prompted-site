#!/usr/bin/env python3
"""RC5 design source gate: no undecided hero assets, equal product intro structures."""
from pathlib import Path
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
for lang in ('fi','en'):
    for slug in ('literacy','capability','transformation'):
        doc=BeautifulSoup((ROOT/lang/slug/'index.html').read_text(),'html.parser')
        hero=doc.select_one('main > section.product-page-hero')
        assert hero, (lang,slug,'shared product intro absent')
        assert hero.select_one('h1'), (lang,slug,'missing product headline')
        assert hero.select_one('a.button'), (lang,slug,'missing CTA')
        assert not doc.select('.wide-photo'),(lang,slug,'inconsistent hero image usage')
for page in list((ROOT/'fi').rglob('index.html'))+list((ROOT/'en').rglob('index.html')):
    text=page.read_text()
    assert 'hero-daylight.webp' not in text and 'hero-material.webp' not in text,(page,'unapproved hero referenced')
    assert 'og:image' not in text,(page,'og thumbnail must wait for image approval')
for lang in ('fi','en'):
    s=BeautifulSoup((ROOT/lang/'index.html').read_text(),'html.parser')
    assert s.select_one('.hero-concept'),(lang,'honest conceptual hero diagram absent')
    assert s.select_one('.evidence-diagram'),(lang,'honest evidence process diagram absent')
print('PASS: consistent product intros, no unapproved rendered or social hero images, conceptual diagrams only')
