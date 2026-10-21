# Prompted — Product System, Design Review R3
21 October 2026 · **PREVIEW DESIGN ONLY — NOT FOR PRODUCTION**

## Design decision

The founder responded that the Round 2 product-first homepage hero was **substantially better**. R3 therefore preserves that hero design, while extending its clarity and polish to the two services that had still used legacy dark two-column text heroes. **Do not replace the approved direction with more abstract architectural compositions.**

## What changed, specifically

1. **Literacy / FI+EN**: New paper-toned product-first hero with an original delivery-structure illustration: real-work context, judgement, common foundation, documented actions. The shorter Finnish/English headline prevents long wrapped text blocks. Clear disclaimer: conceptual model, not software screenshot or certified outcome.
2. **Transformation / FI+EN**: Complementary but distinct hero with a charcoal-on-olive framework: leadership purpose → changed ways of working → capability support → evidence. No fictitious adoption percentages, metrics, clients or ROI.
3. **Buyer journey:** Both secondary services include a contextual, non-pushy bridge to Capability, framed as the focused work-based pilot option; each retains its own main consultation CTA.
4. **Contact path:** Corrected final CTA on FI and EN contact pages to launch an email directly, rather than linking back to the same page.
5. All 16 FI/EN pages regenerated from `build.py` + `content.json`. Round 2 product-first home and Capability heroes and their original implementation are preserved.

## Verification, not claims of approval

- `python3 tools/round3_browser_qa.py`: PASS.
- 16 pages inspected for correct structure and local links; 8 key FI/EN pages checked across **7 widths each** (320, 360, 390, 768, 1024, 1440, 1920 px), for **56 browser width scenarios**. No horizontal overflow, missing in-page anchor or JavaScript exception detected.
- Chromium checks used locally inlined CSS and assets: they are NOT a test against the Vercel preview, a physical device, screen reader or real Web Vitals.
- Screenshots: `previews_round3/literacy-fi-1440.png`, `transformation-fi-1440.png`, corresponding mobile full-page renderings, plus English counterparts.

## Product-truth boundaries

The R2 homepage Capability/browser/Data/mobile art remains a **clearly labelled conceptual illustration based on the application's documented work/evidence architecture**. The new Literacy/Transformation panels are **conceptual delivery diagrams**, not invented app dashboards or customer results. All legal copy is still marked DRAFT.

## Unresolved publish gates

1. Visually approve both new service pages alongside homepage and Capability, including physical iPhone and tablet.
2. Obtain two real, permission-safe Coach / Data screenshots if they can be captured truthfully; no protected personal transcripts, customer branding or speculative numbers.
3. Verify commercial wording, email deliverability, company data, founder claims, image licensing, source rights.
4. Finish privacy notice and terms: controller processing details, hosting recipients, lawful basis/retention; verify tracking/cookie behavior in actual deployed environment.
5. Validate live Vercel SSO/noindex/CSP, WCAG 2.2 AA where applicable, device accessibility and Core Web Vitals. Domain, SEO migration/redirect, recovery plan and final production sign-off remain separate.

**No GitHub writes, no Vercel deployments, no `main` merge, no DNS or live `prompted.fi` modifications in R3.** Existing approved draft preview branch and PR remain untouched.
