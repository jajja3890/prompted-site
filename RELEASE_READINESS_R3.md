# Prompted Product System | R3 accessibility and prelaunch safety gate
Date: 21 October 2026. Status: **DESIGN PREVIEW ONLY. DO NOT MERGE / PUBLISH.**

## What is verified

- All 16 FI/EN static pages regenerated reproducibly from `build.py` and `content.json`.
- R2 product-first hero preserved on Home and Capability; R3 differentiated product-first Literacy and Transformation.
- HTML structural fix: **one `<main id="main">` landmark per page**, previously nested on both language versions of Home and Capability. Generator now handles translated fragments correctly.
- 320-pixel Capability text overflow fixed with a targeted CSS rule, not a global horizontal-scroll mask.
- `tools/prelaunch_gate.py`: PASS 16/16 routes; semantic landmarks, h1, skip link, named navigation, localized meta/hreflang, valid local CTAs, draft legal labels, absence of tracking/form/iframe, preview security/indexing guard.
- `tools/round3_browser_qa.py`: PASS 72 checks, including 56 viewport scenarios on core product pages at 320,360,390,768,1024,1440,1920px; no browser JS exceptions, no side overflow and mobile menu keyboard Escape operates.
- No source changes to production app, DNS, Vercel project configuration or GitHub main.

## What is not verified

- **Real Vercel rendering for this R3 gate**, SSO access, HTTP security headers, noindex in actual response, actual browser cookie behavior, link previews.
- WCAG 2.2 AA conformance: contrast, keyboard, assistive-tech review and zoom require dedicated manual/automated audit, including actual device tests.
- Field Core Web Vitals and Lighthouse on a deployed URL.
- Contact `jarkko@prompted.fi` inbox delivery, company profile details and external founder URL.
- Legal adequacy of privacy notice and terms; they remain DRAFT.
- Real approved user-interface screenshots; product imagery is **conceptual**, not a working-application screenshot or real client evidence. Source and usage permission for H01/H05 art remains subject to approval.
- An optional HTTP smoke test was attempted but the sandbox disallowed loopback browser navigation (`ERR_BLOCKED_BY_ADMINISTRATOR`); this is an **environment limitation, not a test pass**.

## Only remaining production gates

1. Visually accept desktop/tablet/iPhone across three product offerings, particularly product art disclosures.
2. Approve truthful customer-facing claims and contact delivery. Avoid invented impact, customer logos or certifications.
3. Privacy/legal review with actual service processors, retention, lawful basis, cookie/terminal-storage inventory and contact information.
4. Vercel Preview smoke: FI/EN, root redirect, headers/CSP, mobile, accessibility, performance, LinkedIn share test; SEO/GEO and old URL migration plan.
5. Approve production release separately, removing noindex only for the approved production package. Prepare rollback.

**Do not use this preview-only zip as a production deployment.**
