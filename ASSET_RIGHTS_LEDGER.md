# Website visual asset and provenance register
21 Oct 2026 · **Publication blocked until licensed source evidence or owner approval is recorded**

This register is for the new Prompted *marketing website*. It does not grant any intellectual-property rights, does not imply product-screen authenticity, and does not substitute for an original designer/author or licence confirmation.

| Asset | Current technical role | Source evidence currently available | Release action |
|---|---|---|---|
| `assets/wordmark-dark.svg`, `assets/wordmark-light.svg` | Brand and header identity | **Verified exact canonical app master files** on 22 October 2026: dark Git blob `5b6055300e9a75186ae050f9dba916b96c6dccf3`, light `06bf329de183163aab577cd6baf9e5453b51a2db`; matching `jajja3890/prompted/public/brand/*`. Preview CI checks both bytes against these hashes. | Preserve official SVG files unchanged; Prompted Oy's commercial-use authorization / ownership confirmation still belongs in release approvals. |
| `assets/hero-daylight.webp` | Art study, in asset folder | Git commit confirms repository provenance, **not** creation author, rights, or model release | Identify actual source, author and licence; do not rely on rights from merely uploading |
| `assets/hero-material.webp` | Secondary art study in asset folder | Same as above | Confirm source and usage permission; keep unused unless approved |
| `assets/share-prompted.jpg` | **Referenced in every page's Open Graph metadata** | Repo history only; copyright/source evidence not present | **Blocking**: verify licensed ownership or replace with rights-cleared original before publishing |
| `assets/apple-touch-icon.png`, `assets/favicon.ico` | Brand icons | Only source commit provenance, no independent author approval | Confirm same rights as Prompted visual identity |
| Inline CSS/SVG diagrams in source | Conceptual product and service illustrations | Authored inside site source; no third-party image dependencies in inspected markup | Verify no unauthorized third-party assets and maintain clear conceptual disclosures |

## Required human visual sign-off
- Open screenshots from `preview-release-audit` CI artifact and inspect the first screen, responsive spacing, truncation, images and tap target hierarchy on mobile and desktop.
- Test a real iPhone and tablet as final acceptance; offline Chromium screenshots are **not** physical device testing.
- Check buyer-first visual hierarchy on `/fi/tutustu/` and `/en/explore/`, plus credible Home/Capability/Literacy/Transformation imagery, not only the isolated demo.
- Source generated share photo/licensing and brand wordmark authorization in the company data room before launch.
- No publication decision is implied by automated screenshot capture.
