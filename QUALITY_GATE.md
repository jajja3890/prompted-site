# Integrated FI/EN visual system — Quality gate

2026-10-21 · **No-go for production**, approved only as locally testable preview artifact.

## Proven improvements

1. Homepage and Capability source-grounded diagrams integrated into the same styling as all 16 pages.
2. Three distinct products in visible primary navigation with working, localized links.
3. Locale switch is functional and preserves page context, all 8 route pairs reciprocal.
4. One visual system across commerce, founder, contact, privacy and terms; original wordmark and brand accent preserved.
5. JavaScript only powers the menu. It opens, closes on link selection and Escape, and sets `aria-expanded`; no third-party scripts, analytics, marketing cookies or forms.
6. Preview index block exists in HTML, robots.txt, and vercel.json. This is strictly a preview package, NOT a production release generator.

## Automated test evidence

`tools/browser_qa_results.json`: 16 pages inspected at 360, 768, 1440 pixel viewports = 48 responsive checks, plus 8 screenshot scenarios, 56 recorded checks overall. No layout overflow, no browser exceptions, no missing local links in any page. Accessible mobile nav open/Escape tested in 4 scenarios. This **does not** certify WCAG 2.2 AA, field performance or actual deployed Vercel behavior.

## Unresolved approval blocks

**A. True interface:** Obtain and consent-clear precisely two real app visuals from a separate authenticated, permission-cleared session. Learner's Coach/work view and sponsor's restricted `/data` view. No synthetic numbers, false reports, test users misrepresented as paying customers or private transcripts. Can defer imagery if genuine product is not visually ready, but must acknowledge that this is weaker for investors.

**B. Art:** H01 Daylight study still unapproved, displayed with an explicit draft caption. Final image source rights, provenance, visual quality and responsive crops require approval. H05 included in assets for possible later use but not necessary for this homepage.

**C. Commercial:** Validate primary offer names, tone and CTA, pilot scope and timing, price-in-proposal caveat. Do not claim customers, funding, results, certifications or verified legal compliance that have not been evidenced.

**D. Legal:** Confirm Prompted Oy contact email, data controller notice, legal basis and retention, processors/hosting and transfers, browser/device storage before concluding no cookie consent is required. Preview contains draft text marked as draft. No tracking script exists in package, but a final host/configuration check remains essential.

**E. Production:** Configure public website Vercel preview on isolated branch, verify protection/noindex, conduct real mobile/desktop and Lighthouse/Core Web Vitals tests, keyboard/color-contrast/assistive-technology audit, old URL migrations, launch rollback, and explicit approval to remove noindex only for production. Existing `prompted.fi` and `app.prompted.fi` untouched.

## Decision

Keep the integrated preview as the preferred *structural* candidate. Do not call it final/"world class" until authentic product proof and live visual acceptance are achieved. Move no source to `main` and do not change Vercel domain or DNS.
