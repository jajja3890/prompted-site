# Prompted Buyer-Led Product Experience — Design Preview v1

**21 October 2026 · Draft / preview only · NO production approval**

This implements the previously agreed `Prompted_Buyer_Led_Product_Experience_2026-10-21.md` strategy inside the R3 product-first website. It restores the missing interactive buyer-led sales funnel. This is *not* a separately sold fourth product.

## What visitors can actually do

1. Start a 60-second, no-login experience (`/fi/tutustu/#kokeilu`, `/en/explore/#kokeilu`).
2. Choose one of three views: HR / People, business leader, or participant.
3. Select one of three real-work example scenarios: quality checks, recurring reporting or decision comparison.
4. Switch friction and preferred support level to see why a predetermined coaching action changes.
5. Explore the four Evidence stages: first signal, repeat, transfer, independence. The page never claims to measure the visitor.
6. Examine a **clearly fictional** buyer Data snapshot, with a clear privacy boundary.
7. Change impact scenario assumptions (participants, minutes, working weeks, hourly value) and see illustrative capacity/value without claiming savings or causality.
8. Download a text summary from the browser without submitting contact details.
9. Read product differences and indicative Capability pilot scope, or voluntarily contact Prompted.

**Not implemented:** real LLM inference, multiuser sessions, access to customer work or the production authenticated Prompted app, recording of leads or visitor sessions, account creation, payment, actual client ROI evidence. No dependency on these for the demonstration.

## Build / code

- Run `python3 build.py` from project root (Python with `beautifulsoup4`).
- Generated static website: 18 FI/EN pages including `/fi/tutustu/` and `/en/explore/`.
- Experience markup and human-reviewed commercial copy: `buyer_experience.py`.
- Interactive finite-state UI and local scenario calculator: `assets/buyer-experience.js`.
- Product-first design: `assets/buyer-experience.css` with existing R3 styles.
- Existing static product pages: `content.json`, `templates/`, generated HTML.
- No third-party tracking, forms, embeds, remote fonts or external scripts. No cookies, localStorage, sessionStorage, fetch, WebSocket, Supabase client or real LLM API calls in the experience JS. Blob download is user-initiated; it does not contact a server.
- `vercel.json` sets preview-wide `X-Robots-Tag: noindex, nofollow` and CSP. HTML carries preview `noindex` and `robots.txt` blocks indexing.
- Static product-first hero renders independently; JavaScript is loaded only on the two interactive experience pages. This is a dependency-free JS design choice, not a claim to mirror the full Next.js app.

## QA and scope

- `python3 tools/prelaunch_gate.py`: 18/18 pages semantic, local security and index safeguards.
- `python3 tools/buyer_experience_qa.py`: 130/130 browser interaction and responsiveness checks in Chromium (HTML/CSS/JS injected into a browser because the execution environment blocks HTTP browser navigation). Captures previews for 390px and 1440px in both FI and EN. Tests role choices, scenario branching, coaching/friction changes, Evidence, fictional buyer report, reactive calculator, browser TXT download and reset.
- Local browser tests **are not** Vercel response/CSP/SSO/speed/real phone/WCAG 2.2 AA certifications. Treat them as a prerequisite, not a release pass.

## Gates before ANY production release

- Founder visual acceptance, buyer comprehension study with 5–8 HR/People/business customers.
- Validate legal/privacy and processor disclosures, even for tracking-free static marketing site.
- Confirm contact inbox and any public company claims; do not use mock screenshots as production screenshots.
- Verify preview on Vercel (FI/EN, 3 products, noindex/CSP, cookie behavior, real mobile and keyboard), and no accidental real telemetry.
- Confirm security / rate limits / budget if a live model is ever added (not in this version).
- Review old URL redirects and rollout/rollback separately.
- **Do not merge a draft PR, remove noindex, alter DNS, or touch `app.prompted.fi` without explicit written approval.**
