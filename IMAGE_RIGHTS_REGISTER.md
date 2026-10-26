# Prompted marketing website — image rights and provenance register

Updated: 26 October 2026 · Owner: Prompted Oy · **OWNER-ATTESTED IMAGE RIGHTS APPROVED; PUBLIC LAUNCH STILL BLOCKED**

The connected repository provides file history and file usage. A Git commit is not evidence of a third party's permission to publish an image or mark.

| Asset | Actual use in 18 generated pages | Status | Evidence required for public use |
| --- | --- | --- | --- |
| `assets/hero-daylight.webp` (H01, 193,374 bytes) | FI + EN homepage, People First section | **OWNER-ATTESTED: ChatGPT-origin visual; website use approved 26 Oct** | Generation or purchase record, creator/owner, permitted commercial use, and final visual/crop approval. It is visibly captioned as an unapproved study. |
| `assets/share-prompted.jpg` (173,931 bytes) | Every FI/EN page via `og:image` | **OWNER-ATTESTED: ChatGPT-origin share art; website/social-preview use approved 26 Oct** | Origin or license; verify actual external link-preview crop. |
| `assets/wordmark-dark.svg` (6,316 bytes) | Every FI/EN header | **AUTHENTIC MASTER VERIFIED**: Git blob SHA `5b6055300e9a75186ae050f9dba916b96c6dccf3` exactly matches `jajja3890/prompted/public/brand/prompted-wordmark-master.svg` | No approximation or re-rendering permitted. Company use-rights remain a release sign-off separate from authenticity. |
| `assets/wordmark-light.svg` (6,316 bytes) | No direct page reference identified | **AUTHENTIC MASTER VERIFIED**: Git blob SHA `06bf329de183163aab577cd6baf9e5453b51a2db` exactly matches `jajja3890/prompted/public/brand/prompted-wordmark-light-bg.svg` | Currently unused by generated pages; brand provenance established, specific website rights remain subject to owner approval. |
| `assets/favicon.ico` and `assets/apple-touch-icon.png` | Browser icon metadata | **OWNER-ATTESTED for current Prompted brand use; exact blobs pinned in manifest** | Confirm wordmark/icon rights and intended commercial use. |
| `assets/hero-material.webp` (92,578 bytes) | No HTML/CSS reference found among current pages | **Unapproved and unused** | Do not feature, link or treat as cleared; omit from an eventual production asset set unless authorized. |
| CSS/HTML product-interface and delivery diagrams | Home/Capability/Literacy/Transformation (FI/EN) | **Concept illustrations, not actual software screenshots** | Original site code and marketing design. Retain the explicit truthful no-customer-data disclaimers; review rights to any adapted marks or third-party components. |

**Technical master provenance checked directly in the company's live application GitHub repository on 22 October 2026:** [canonical dark master](https://github.com/jajja3890/prompted/blob/main/public/brand/prompted-wordmark-master.svg) and [canonical light-background master](https://github.com/jajja3890/prompted/blob/main/public/brand/prompted-wordmark-light-bg.svg). The preview CI independently rejects non-identical wordmark bytes. This establishes exact identity with existing masters, not a license grant. No substitute logo was generated.

The file history introduces the raster assets in `5ac7c18d2e02261042f259d4d8b2c4ddaeb6cb1a` on 21 Oct 2026. That establishes repository origin, **not copyright ownership or downstream commercial-use authorization**.

## 26 October 2026 provenance investigation and shortest clearance path

The first containing commit has been verified as [`5ac7c18`](https://github.com/jajja3890/prompted-site/commit/5ac7c18d2e02261042f259d4d8b2c4ddaeb6cb1a), with the GitHub user `jajja3890` recorded as its author and committer. The commit includes both `hero-daylight.webp` and `share-prompted.jpg`. **GitHub commit authorship establishes file introduction only, not that this user created the artwork or holds its commercial rights.** A search of earlier Prompted visual design discussions documents the H01/H05 collection and subsequent selection but does not supply an original generation record, a stock licence, a creator assignment or third-party permission. At the time of this investigation, neither image was cleared; the subsequent 26 October owner attestation and approval below supersede that initial status.

**Exact approval objects in the current development branch (Git blob SHA):**
- H01 `assets/hero-daylight.webp`: `e2be6f8fb27aa9c155e0112c5396e110f6a3f366`
- Open Graph `assets/share-prompted.jpg`: `9229344275dca9dc169ecd87efaf12eba27d451a`
- Canonical header wordmark `assets/wordmark-dark.svg`: `5b6055300e9a75186ae050f9dba916b96c6dccf3`
- Brand derivatives `assets/favicon.ico`: `388bf7862adcd1d2c803d7de39bad813cf221baa`; `assets/apple-touch-icon.png`: `c9f538626ae88d916b8f2079f7dc340938b702c7`

These hashes identify bytes for a later specific owner attestation; **hashes are not licenses**.

**One shared source decision, two output files:** the social share image depicts the same architectural subject as H01, with Prompted branding overlaid. If both originate from the same rights-cleared master, retain evidence for the master **and** record that the crop/overlay was authorised or created for Prompted. If their source differs, record each source independently. Include the asset names and current content hashes in the private company legal/data room; do not put invoices, personal identity records or license credentials in this public repo.

**If the H01 master was created using ChatGPT/ImageGen:** the [OpenAI EEA Terms of Use](https://openai.com/en-GB/policies/eu-terms-of-use/) (updated 16 January 2026) state that, as between the user and OpenAI and to the extent permitted by applicable law, the user owns the output; user-provided input and third-party rights remain the user's responsibility. This is a useful *conditional* rights basis, **not evidence that H01 actually came from ChatGPT** or that the input was independently cleared. Preserve the original generation/export reference and record Prompted Oy's permission to commercially use that specific output.

**Fastest defensible options (choose on evidence, not convenience):**
1. *Company-origin artwork*: owner identifies how H01 was created, confirms use rights for a commercial website and social distribution, and confirms the share-graphic adaptation. Save the original generation/export record or an attributable dated statement, with terms if relevant.
2. *Licensed third-party artwork*: preserve the exact provider/licence, acquisition/creator attribution, commercial distribution and editing permissions, and whether credit is required.
3. *No reliable rights record*: **do not approve this image**; replace H01 and the share graphic with new original or rights-cleared assets, and re-check FI/EN layout, crop and Open Graph preview before owner approval.

The original official Prompted wordmark SVG is byte-matched to the Prompted application master. The 26 October owner-authorised image manifest now also records website use permission for the present wordmark and derived favicons; this is not an independent third-party IP search.

The `image_rights` gate is now **approved on owner attestation** for the exact files in `PUBLIC_RELEASE_APPROVALS.json`; `owner_release` and the other release gates remain pending. No public deployment is authorised by this note.

## 26 October 2026 owner confirmation and release-record scope

The owner explicitly confirmed in the working ChatGPT conversation that **all the visuals in question were produced together within ChatGPT**, rather than sourced from an external third-party asset library, and then approved proceeding with the image-rights approval manifest. This is recorded in `PUBLIC_RELEASE_APPROVALS.json`, including the five individual, fixed Git blob SHAs and an explicit permission basis for Prompted Oy's company-site use and social previews.

This records owner-origin attestation and the company owner's permission. It does **not** reconstruct the original prompts, determine whether every possible third-party right could arise from user-supplied inputs, independently certify copyright subsistence under Finnish law, or approve the complete website's publication. Keep visual-device, privacy/legal, commercial copy, domain rollback and public owner-release checks separate.

## Minimum sign-off

- [x] H01 owner-origin attestation and specific company website use recorded; visual/device crop review belongs to separate `visual_device` gate
- [x] Open Graph artwork origin and website/social distribution authorised by owner; actual link-preview appearance remains part of visual release QA
- [x] Owner authorised current exact Prompted master logo and derived brand icons for the company site in the image approval manifest
- [ ] No unapproved art studies, temporary captions or design review labels on public pages
- [ ] Product mockups remain accurately labelled conceptual, never real user or verified customer performance
- [x] Saved source evidence, current Git blob SHAs, date and named owner in `PUBLIC_RELEASE_APPROVALS.json`

**No production authorization is implied by automated screenshots or CI status.**
