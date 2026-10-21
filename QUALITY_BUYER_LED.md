# Buyer-Led Product Experience — verified scope and open gates

Status: **REVIEW ONLY / NOT APPROVED FOR PRODUCTION**.

## Passed locally
- All 18 FI/EN routes generated with one main landmark, canonical/hreflang/OG, noindex preview guard.
- A no-login, same-site guided interaction exists and reacts to visitor choices.
- Both languages contain five steps and matching product link structure.
- 130 Chromium checks passed using browser content-injection because direct HTTP and file navigation are disallowed in the runner. This validates rendered layout and script interactions but **not network delivery**.
- No third-party requests, browser JS exceptions, or horizontal overflows at widths 320, 390, 768, 1024 and 1440px in tests.
- Fictional sample Data and calculator explicitly distinguish illustrative data from genuine outcomes. No participant text or account access.
- No JS analytics, fetch, cookies, local/session storage, nonessential tracking or external dependencies in this local experience.

## Remaining
- Validate on a real **SSO-protected Vercel Preview** after pushing a separate branch / draft PR.
- Conduct full keyboard, screen reader, contrast, zoom and WCAG evaluation, field performance and browser/device tests.
- Review all public demo text for commercial/legal accuracy. The current website Privacy/Terms remain drafts; the hero artwork remains an unapproved illustration.
- Check email deliverability, branding, three product stories and mobile cognitive clarity with real buyers.
- This first public demo intentionally has a deterministic coaching walkthrough and no live AI; a live model requires separate abuse/budget/privacy architecture before any future rollout.

## Rollout discipline
Never merge to main or deploy to production, DNS, or app without explicit written owner go-live authorization.
