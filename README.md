# Prompted website / RC7 Brand & Product Excellence

This is a **design-review release candidate**. H01 and H05 are **unapproved art studies** prominently labelled on the site. This is NOT publish-approved production art.

- 16 FI/EN pages, three public product names Literacy, Capability, Transformation.
- No Lovable, external font, analytics, trackers, consent popup or synthetic product screenshot.
- Source `build.py`, styles `assets/style.css` and `assets/rc7.css`; static assets in `assets/`.
- `python3 build.py` generates all HTML; `python3 tools/audit_discoverability.py` checks canonical, languages, crawler gates.
- Default prelaunch build carries `noindex` HTML and `X-Robots-Tag` in vercel.json.
- Do not use a production build until hero image(s), privacy/legal, email, truthful commercial claims and live QA are approved.

### Product realism

The Capability visual labelled conceptual representation describes the service architecture. It is **not** a screenshot. Synthetic concepts featuring unrelated company logos were expressly excluded from this repository.

### Review first

1. Home desktop and mobile.
2. Capability desktop and mobile, including Data/Evidence architecture.
3. FI and EN product / utility pages after design direction signoff.

See `DESIGN_SYSTEM_RC7.md`.
