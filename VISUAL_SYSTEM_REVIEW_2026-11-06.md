# Prompted.fi — Visual System & Art Direction · Proposal 01
**6 November 2026 · DESIGN REVIEW ONLY · NOT APPROVED · NO PRODUCTION CHANGES**

## Scope and constraints
The current public site is working. Improve distinctiveness, beauty and buyer confidence without redesigning its architecture or compromising its conversion paths. All design exploration is done in this isolated GitHub branch. No production deploy, merge, DNS, app.prompted.fi, live customer records or change to the approved Prompted brand system without owner review.

**Verified source baseline:** `main` commit `75c5dded8a6ddab406f60b45c52a9f87693468d4`. The site has nine routes per language (18 in total), an official Prompted SVG wordmark and generated FI/EN static pages. The image inventory contains `hero-daylight.webp`, `hero-material.webp`, `share-prompted.jpg`, wordmarks and browser icons. The only `<img>` embedded in inspected main pages is the brand wordmark; the product/method illustrations are primarily HTML/CSS. `share-prompted.jpg` is the shared OG image for all 18 pages. Architectural H01 does not appear as an image in the current HTML; home instead has a PEOPLE FIRST typographic panel. These are source-level findings, not physical-device rendered image acceptance.

## Current brand truth — retain
- Canonical Prompted SVG wordmarks, not recreated logos.
- Base palette from `assets/concept.css`: Ink `#090b09`, Paper `#F5F5F2`, Acid Olive `#BDC923`, Light `#F7F8F4`. The existing product/UI and editorial system stays in place.
- Expressive editorial typography and controlled spacing; no unrelated new visual identity, neon AI tropes, stock office smiling teams or made-up customers/results.
- Capability hero and the buyer/participant demo are conceptual implementations and must remain clearly distinguishable from authentic logged-in software screenshots.

## Three coordinated visual layers
### 1 — Brand imagery
Purpose: memorable human-centred point of view; how real work, learning and people change, not science-fiction architecture or generic AI.
Direction **proposed**, not accepted: carefully art-directed people-at-work/editorial compositions, warm natural lighting, tactile detail and deliberate negative space. Limit initial use to one strong homepage section and optionally a company-page treatment. Do not claim generated people are customers or the founder; do not add a fictional founder portrait.

### 2 — Method / product visuals
Purpose: show what Literacy, Capability and Transformation actually deliver.
- Literacy: simple four short modules + knowledge check; accessible and welcoming, not enterprise control panels.
- Capability: preserve the product-first view and buyer/participant separation. Real, privacy-safe UI screenshots should replace conceptual devices only after being captured and reviewed.
- Transformation: one scalable leadership → work → people → evidence operating-model diagram. Avoid another dashboard metaphor.
- Demo: no extra imagery; protect clarity, interaction and load speed.
Maintain a visible separation between *conceptual illustration*, *real UI* and *illustrative sample data*.

### 3 — Social share cards
Purpose: at a glance, a genuine Prompted identity and understandable customer promise.
- Replace global `assets/share-prompted.jpg` architecture moodboard image only after review.
- First candidate: a clean `1200×630` original, typographic Prompted share card with canonical logo and high-contrast brand colors; short message `Tekoäly osaksi oikeaa työtä.` / `Make AI part of real work.` depending on page language. Avoid tiny text and screenshot details. Confirm image rendering in WhatsApp, LinkedIn and mobile.
- A later phase may make one product-specific card per Literacy/Capability/Transformation; no 18 individually hand-made cards.

## Page-by-page backlog (the FI/EN equivalent shares the same design)
| Route | What is there in source | Audit interpretation | Proposed action | Priority |
|---|---|---|---|---|
| Home `/fi/`, `/en/` | Product-first HTML/CSS browser/device hero, offer tiles, PEOPLE FIRST typographic section | Credible platform, slightly narrow human-story range | Add **one** editorial human/work signature visual to a carefully selected section (do not stack a second busy hero); preserve current first-screen clarity | P1 |
| Literacy | Course-stage HTML/CSS illustration; four modules + final assessment; dense explanatory sections | Understandable but dry to a beginner | Rebalance existing course progression, visual hierarchy and whitespace before commissioning another image | P2 |
| Capability | Product-first concept hero + stages + learner/buyer narrative | Existing visual emphasis is appropriate | Refine text density, device credibility, legibility; prioritise authentic permission-safe screenshot later | P2 |
| Transformation | Four-dimension framework and 8 sections, no photos | Right conceptual idea; could be more distinctive and executive-grade | Redesign **existing** 4-dimension editorial diagram as one clear operating model; avoid added random image | P1 |
| Demo | Deterministic buyer/participant interface and illustrative device | High-intent interaction, not a brand gallery | Keep imagery out; test buyer comprehension and mobile UI instead | Preserve |
| Company | Minimal text, founder/company description, no photo | Weaker human connection/trust than home promise | Design a quiet editorial company identity treatment; genuine founder image only if specifically chosen and provided/approved | P1/P2 |
| Contact | Text and process/CTA | Stronger without decoration | Keep minimal; polish whitespace/type if needed | Preserve |
| Privacy | Legal typography | Appropriate | No imagery | Preserve |
| Terms | Legal typography | Appropriate | No imagery | Preserve |

## First wave — strictly four changes max
1. **Share card**: single distinctive global card, approved in both languages before swapping OG references. (P1)
2. **Home editorial asset / image composition**: one meaningful human + real-work brand visual, not generic corporate stock; placed to complement, not fight, product hero. (P1)
3. **Transformation operating model**: improve existing diagram's visual storytelling/typography. (P1)
4. **Company human trust treatment**: typography and original editorial arrangement, optional authentic founder photo only with permission. (P2)

Literacy and Capability initially receive quality/legibility passes, not more competing pictures. Re-evaluate after first-wave comparisons.

## Review process
1. Owner chooses the desired art direction: **A (recommended): restrained human/editorial imagery + product evidence**, or **B: pure graphic and typographic system + product evidence**.
2. Build 2 distinct design study variants on this branch, without editing production.
3. Review side-by-side: home desktop, home mobile, company desktop and Transformation desktop; social card at actual WhatsApp crop.
4. Review brand fidelity, accessibility, image rights, truthful product claims, responsive performance and consistency across FI/EN.
5. Only after explicit owner go/no-go should a production PR be prepared. Never infer approval from preview readiness.

## Source anchors
- `build.py`: generated pages, Hero/OG and typography.
- `assets/concept.css`, `assets/product-first.css`, `assets/product-system.css`, `assets/pages.css`: existing style language.
- `HERO_DESIGN_DECISION.md` and `DESIGN_REVIEW_R3.md`: earlier founder preference for a compelling product-first hero rather than generic architectural images.
- `assets/share-prompted.jpg` and `assets/hero-daylight.webp`: inherited visual studies.
