# Prompted website — own-source, Vercel-ready static release

Version: 1.0.0-rc4 — 2026-10-21. Owner: Prompted Oy.

## Architecture

100% static, generated FI/EN pages, no Lovable runtime, no database, no form service, no analytics script. Deploy to a Vercel project connected to `jajja3890/prompted-site`. `build.py` generates HTML for routes and metadata; visual styling is in `assets/style.css`; site interactions in `assets/site.js`.

Included pages: FI+EN home, Literacy, Capability, Transformation, Company, Contact, Privacy and Service terms notice. Original official Prompted master SVGs and two curated Hero Core v0.7 studies. Images are creative illustrations, never client evidence or real product screenshots.

## Publish gates — do not bypass

- The pages currently carry `noindex` in HTML and an `X-Robots-Tag` response header in the preview Vercel configuration. Preview robots.txt allows crawling so engines can read the noindex rule. The **approved production build** removes these blocks, allows crawlers (including OAI-SearchBot), and generates the sitemap. Do not activate production indexing until approvals and DNS readiness.
- Verify outgoing email address `jarkko@prompted.fi` works (it appeared on the existing live public site).
- Confirm privacy copy meets Prompted's actual processing activity, hosting and retention. The privacy document is a working prepublication draft.
- Confirm commercial claims, service readiness, and date/participant language before publish.
- Confirm visual quality and absence of image artefacts before final lock (v0.7 Hero Core images are not yet final approvals). Source/IP provenance is confirmed by the owner; no legacy third-party asset transfer is assumed.
- Record old routes and 301 redirects before replacing the active domain.
- Do not change prompted.fi DNS until a verified Vercel preview works end to end and you have a rollback point.

## Local preview

`python3 build.py && python3 -m http.server 8021` then open `http://localhost:8021/fi/`.

## Cost model

No Lovable dependency; no custom runtime/backend. Intended to run inside Prompted's existing Vercel Pro subscription with low usage. Domains and Vercel billing remain separate.

## Approved production build

Only after all release gates and DNS cutover are approved, run:

`PROMPTED_RELEASE=approved-production PROMPTED_APPROVAL=reviewed-privacy-content-and-domain python3 build.py`

This generates indexable pages, robots.txt and sitemap.xml. Do not do this in the release candidate.

## Search/AI discovery audit — RC4

Read `SEO_GEO_AUDIT_2026-10-21.md` for findings, corrections and outstanding gates. Run `python3 tools/audit_discoverability.py` (requires `beautifulsoup4`) to test both prelaunch and an isolated production simulation, without publishing anything.

Do not substitute `llms.txt`, unverified AI visibility claims or automated testimonials for original customer evidence.

## RC4 safety note
- Product names are exactly Literacy, Capability and Transformation; internal placeholders never go public.
- UI was statically audited but **has not yet received visual sign-off in a real browser**.
- The founder’s personal-site URL and domain/email settings must be checked live before cutover.
- No consent banner is included because the delivered code has no optional cookies, marketing analytics or embeds; hosting/config changes can alter that assessment.
