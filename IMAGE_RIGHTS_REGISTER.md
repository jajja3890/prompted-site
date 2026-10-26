# Prompted marketing website — image rights and provenance register

Version: 22 October 2026 · Owner: Prompted Oy · **REVIEW OPEN, NOT A LICENSE CERTIFICATE**

The connected repository provides file history and file usage. A Git commit is not evidence of a third party's permission to publish an image or mark.

| Asset | Actual use in 18 generated pages | Status | Evidence required for public use |
| --- | --- | --- | --- |
| `assets/hero-daylight.webp` (H01, 193,374 bytes) | FI + EN homepage, People First section | **BLOCKED: no verified source / use rights** | Generation or purchase record, creator/owner, permitted commercial use, and final visual/crop approval. It is visibly captioned as an unapproved study. |
| `assets/share-prompted.jpg` (173,931 bytes) | Every FI/EN page via `og:image` | **BLOCKED: image provenance unverified** | Origin or license; verify actual external link-preview crop. |
| `assets/wordmark-dark.svg` (6,316 bytes) | Every FI/EN header | **AUTHENTIC MASTER VERIFIED**: Git blob SHA `5b6055300e9a75186ae050f9dba916b96c6dccf3` exactly matches `jajja3890/prompted/public/brand/prompted-wordmark-master.svg` | No approximation or re-rendering permitted. Company use-rights remain a release sign-off separate from authenticity. |
| `assets/wordmark-light.svg` (6,316 bytes) | No direct page reference identified | **AUTHENTIC MASTER VERIFIED**: Git blob SHA `06bf329de183163aab577cd6baf9e5453b51a2db` exactly matches `jajja3890/prompted/public/brand/prompted-wordmark-light-bg.svg` | Currently unused by generated pages; brand provenance established, specific website rights remain subject to owner approval. |
| `assets/favicon.ico` and `assets/apple-touch-icon.png` | Browser icon metadata | **BLOCKED: derivative rights depend on mark** | Confirm wordmark/icon rights and intended commercial use. |
| `assets/hero-material.webp` (92,578 bytes) | No HTML/CSS reference found among current pages | **Unapproved and unused** | Do not feature, link or treat as cleared; omit from an eventual production asset set unless authorized. |
| CSS/HTML product-interface and delivery diagrams | Home/Capability/Literacy/Transformation (FI/EN) | **Concept illustrations, not actual software screenshots** | Original site code and marketing design. Retain the explicit truthful no-customer-data disclaimers; review rights to any adapted marks or third-party components. |

**Technical master provenance checked directly in the company's live application GitHub repository on 22 October 2026:** [canonical dark master](https://github.com/jajja3890/prompted/blob/main/public/brand/prompted-wordmark-master.svg) and [canonical light-background master](https://github.com/jajja3890/prompted/blob/main/public/brand/prompted-wordmark-light-bg.svg). The preview CI independently rejects non-identical wordmark bytes. This establishes exact identity with existing masters, not a license grant. No substitute logo was generated.

The file history introduces the raster assets in `5ac7c18d2e02261042f259d4d8b2c4ddaeb6cb1a` on 21 Oct 2026. That establishes repository origin, **not copyright ownership or downstream commercial-use authorization**.

## 26 October 2026 provenance investigation and shortest clearance path

The first containing commit has been verified as [`5ac7c18`](https://github.com/jajja3890/prompted-site/commit/5ac7c18d2e02261042f259d4d8b2c4ddaeb6cb1a), with the GitHub user `jajja3890` recorded as its author and committer. The commit includes both `hero-daylight.webp` and `share-prompted.jpg`. **GitHub commit authorship establishes file introduction only, not that this user created the artwork or holds its commercial rights.** A search of earlier Prompted visual design discussions documents the H01/H05 collection and subsequent selection but does not supply an original generation record, a stock licence, a creator assignment or third-party permission. Neither image is cleared yet.

**One shared source decision, two output files:** the social share image depicts the same architectural subject as H01, with Prompted branding overlaid. If both originate from the same rights-cleared master, retain evidence for the master **and** record that the crop/overlay was authorised or created for Prompted. If their source differs, record each source independently. Include the asset names and current content hashes in the private company legal/data room; do not put invoices, personal identity records or license credentials in this public repo.

**Fastest defensible options (choose on evidence, not convenience):**
1. *Company-origin artwork*: owner identifies how H01 was created, confirms use rights for a commercial website and social distribution, and confirms the share-graphic adaptation. Save the original generation/export record or an attributable dated statement, with terms if relevant.
2. *Licensed third-party artwork*: preserve the exact provider/licence, acquisition/creator attribution, commercial distribution and editing permissions, and whether credit is required.
3. *No reliable rights record*: **do not approve this image**; replace H01 and the share graphic with new original or rights-cleared assets, and re-check FI/EN layout, crop and Open Graph preview before owner approval.

The original official Prompted wordmark SVG is byte-matched to the Prompted application master; **the company owner still has to confirm the rights to use that logo and derived favicons in Prompted Oy's marketing.**

This is a sign-off pathway, not approval. The `image_rights` gate and `owner_release` gate remain `pending`, and the project must not be publicly deployed on the strength of this note.

## Minimum sign-off

- [ ] H01 source and commercial-use rights documented; select final crop on desktop and phone
- [ ] Open Graph image rights and share-image preview approved
- [ ] Prompted logo/icon rights confirmed for this company and site
- [ ] No unapproved art studies, temporary captions or design review labels on public pages
- [ ] Product mockups remain accurately labelled conceptual, never real user or verified customer performance
- [ ] Save asset/source links or authorization with a durable date and approver

**No production authorization is implied by automated screenshots or CI status.**
