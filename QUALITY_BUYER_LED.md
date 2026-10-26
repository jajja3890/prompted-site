# Capability dual-demo v2 — Test evidence and release gates
Status: **Design review only; not approved for production** (21 Oct 2026).

## Verified locally
- Both FI/EN experiences produced from the same source.
- R3 product-first appearance retained; dedicated top navigation Demo and truthful product-page CTA separation.
- Buyer/participant entry; switching; illustrative buyer delivery and Evidence tabs; participant coaching friction branches; four-stage evidence explanation; optional buyer calculator.
- Local browser `tools/dual_demo_qa.py` (development worktree): **230/230 responsive + functional checks** at 320–1920 px; static 18/18 generated page checks. No script exceptions, lateral overflow or demo network requests in that local execution.
- Candidate source was transferred unchanged as patches to this independent GitHub branch; each original file length and reconstructed target length was checked before commit.
- Main branch, app.prompted.fi, public domain and DNS untouched.

## Need verification before release
- **Live authenticated Vercel Preview:** assess both paths on laptop and mobile including browser CSP, runtime JavaScript, link transitions and actual HTTP noindex headers.
- WCAG 2.2 AA manual and automated: keyboard/assistive tech, focus, zoom, contrast, error messaging.
- 5–8 actual business/HR buyers: can they distinguish buyer versus learner view, what buyer sees, and difference from Literacy / Transformation without help?
- Truthful UI claims, image provenance, FI/EN copy, legal/privacy controller disclosure, cookie/terminal storage, email deliverability, old URL redirects.
- No genuine tenant data or live AI model is exposed. A real LLM trial is NOT a launch requirement.
- Do not report local browser checks as remote/live passes.

## No-go
No merge to main, no promotion or DNS change, no removing noindex, no public launch absent an explicit separate decision.
