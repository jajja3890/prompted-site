# Prompted.fi — Integrated Visual System Preview

**Status:** Prelaunch design integration — NOT APPROVED FOR PRODUCTION (21 October 2026).

This is the first unified 16-page FI/EN visual implementation built from the Prompted product-truth design gate, not an RC7 merge and not an assertion of visual sign-off. It supersedes the *standalone two-page proof of concept* for structure, while the full website's final sign-off is still open.

## Why this edition exists

- Three real product landing pages in both languages (Literacy, Capability, Transformation), not cards with placeholder links.
- Common original Prompted brand, navigation, product pages, responsive CSS, and accessible mobile menu.
- One truthful product architecture: participant work, coaching support, and separately published restricted group evidence. It is a **conceptual diagram, not a product screenshot or a client result**.
- The company founder link, legal pages, and contact paths exist in both languages.
- Search metadata, structured data and language alternates remain ready for later review, while `robots.txt`, HTML `noindex`, and Vercel `X-Robots-Tag` block indexation during prelaunch.
- No third-party fonts, analytics, cookies, marketing pixels, form capture or Lovable dependency.

## Routes

FI `/fi/`, `/fi/literacy/`, `/fi/capability/`, `/fi/transformation/`, `/fi/yritys/`, `/fi/yhteys/`, `/fi/tietosuoja/`, `/fi/ehdot/`.
EN `/en/`, `/en/literacy/`, `/en/capability/`, `/en/transformation/`, `/en/company/`, `/en/contact/`, `/en/privacy/`, `/en/terms/`.

## Ownership and future updates

- All generated pages are committed in the package. They do **not** require Python to serve or a recurring Lovable subscription.
- To change copy: edit `content.json` for the commercial and legal/service content, or `templates/index.html` / `templates/capability.html` for the hero and product illustration copy. EN translations for prototype fragments currently live in the `trans` mapping in `build.py`.
- Regenerate: `python3 -m pip install -r requirements-build.txt` and `python3 build.py`.
- Style: `assets/concept.css` (approved direction not yet signed off), `assets/pages.css` for supporting pages.
- To review locally, serve this directory from a local static server at its root, e.g. `python3 -m http.server 8000`, then visit `http://localhost:8000/fi/`. Directory routes deliberately use absolute paths.
- Tests: `python3 tools/browser_qa.py` uses Chromium and Playwright; the source HTML itself runs in any standards-compliant browser.

## Release safety

**NOT RELEASE READY.** H01 architectural image remains an unapproved art study; true Coach/Data screenshots have not been captured or cleared; legal notice and contact inbox require human checks; rendered Chrome previews have not been checked on real iPhone hardware, Lighthouse/CWV not run against public Vercel URL. `noindex` must not be lifted until all release gates are signed off. See `QUALITY_GATE.md`.

Do not merge any predecessor's rejected RC7 branch, do not change DNS, and do not confuse `jajja3890/prompted-site` (public marketing) with `jajja3890/Prompted` (authenticated application).
