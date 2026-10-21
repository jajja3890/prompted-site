# Prompted Product System — Round 3

Local design candidate. **Not publish-approved**. Focus: matching Literacy and Transformation to Round 2's better, product-first home / Capability visual identity while staying honest about which offerings are software-enabled.

**Review first**: the four screenshots in `previews_round3/` for Literacy and Transformation in Finnish, desktop and mobile. Home and Capability remain the Round 2 design, not new art studies.

## Rebuild locally

```sh
python3 -m pip install -r requirements-build.txt
python3 build.py
python3 tools/round3_browser_qa.py
```

- HTML pages: `/fi/`, `/en/` and 3 product + company/contact/privacy/terms per language.
- CSS: `assets/product-system.css` adds only new service-hero layouts; `assets/product-first.css` still owns home + Capability.
- Copy source: `content.json` plus localised copy and visuals in `build.py`.
- Standalone static hosting, no Lovable, remote fonts, marketing scripts, cookie banner or analytics added by this work.
- Every preview page remains `noindex,nofollow`; `robots.txt` blocks crawling, Vercel headers enforce noindex, and previews remain protected in Vercel project configuration (to be reverified if deployed).

No actions taken in remote repositories or live environments.
