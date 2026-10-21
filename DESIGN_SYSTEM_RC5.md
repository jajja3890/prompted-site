# Prompted digital design system v0.5 — candidate, not final approval

## Direction
Evidence-led editorial minimalism. Black/white/acid-olive remain the identity. Restrained brutalism comes from proportion, negative space and disciplined rules, not overloaded display headings or uncontrolled stock imagery.

## Design tokens
- Container: max 1320 px, gutters 24–72 px.
- Typography: native UI sans stack, fallback system fonts, no external tracking or font requests. H1 48–94 px depending on page; H2 32–61 px; body 16–21 px; labels 12 px minimum.
- Weights: 400/500/600/650/700 (no synthetic 850 as system default). Tight tracking reserved for headline, not body.
- Colors: #000000, #ffffff, #F5F5F2, #BDC923; mid grey #B7B9B3 and ink-soft #272825.
- Three page families: editorial homepage, structured service pages, utility/trust pages.
- Interaction: 44 px minimum targets, 100% keyboard nav, reduced motion respected, no novelty effects.

## Media decision
Current H01 and H05 source images stay in /assets for audit/review but **are deliberately not displayed anywhere in RC5**. No hero has been approved. The editorial diagrams in RC5 are illustrations of the stated Prompted process, not product screenshots, customer evidence, metrics or dashboards. The hero-image choice is a separate explicit future gate.

## Ownership / production
Based on RC4, kept fully static, Lovable-independent, no third-party CSS/JS/fonts, no cookies or analytics added. Preview still noindex at both HTML and HTTP header levels. No live DNS or app.prompted.fi changes.

## Review gates
1) Review first viewport of home and three products in desktop/mobile.
2) Check company/contact/legal against quiet utility templates.
3) Decide whether to introduce a final hero image on home, and if so its particular purpose and crop. Do not use image as a layout crutch.
4) Only after art direction approval, refactor common components and finish technical/human QA.
