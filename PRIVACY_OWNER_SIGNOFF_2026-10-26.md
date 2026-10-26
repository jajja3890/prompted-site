# Prompted Oy — 26 October 2026 privacy controller sign-off packet

**Status: PREPARED FOR INFORMED OWNER DECISION, NOT APPROVED.** This file is not a signature, and there is no public release authorization.

## What exactly is being reviewed

**Website:** the new static FI/EN `prompted.fi` marketing site. **Out of scope:** `app.prompted.fi` authenticated customer processing, Prompted employee/customer learning evidence, and Tekoälymörkö.

**Source files pinned by Git blob ID at review time (26 October 2026):**
- FI/EN notice source `content.json`: `b6e4e37f4b58de1f4b9a7239571087d506105eab`
- FI privacy page `fi/tietosuoja/index.html`: `73f278c7291312ea14ff385fa07e42f3648ba065`
- EN privacy page `en/privacy/index.html`: `3d14c9392f7315ddc4610d0034f920dd704bdf94`
- Balancing assessment `LEGITIMATE_INTEREST_BALANCING.md`: `a7a2d5e396162e959e7f82d1572c3dca165a1459`
- Adopted retention/rights procedure `MARKETING_ENQUIRY_RETENTION_SOP.md`: `69ae4b74ed42be8e7fb3c31ad7fabdb6a823813b`

**Supporting technical evidence:** CI success at commit `a36d9b23ce6d0a107f7527a21e3304f2aa9fc6b3` (run 40325486171, 26 Oct), including FI/EN browser QA and fail-closed public release guard; protected Vercel preview on the marketing site. Subsequent changes only to internal legal review notes and balancing materials still require current CI pass. **Successful CI is not evidence of legal sign-off.**

## Proposed controller decision to adopt — needs explicit yes/no

The Prompted Oy owner would confirm all of the following, **only for the defined marketing website**:

1. **Article 6(1)(f) purpose A:** replies and requested follow-ups to voluntary incoming business enquiries using only relevant contact/message data; no automatic newsletters, cold lead enrichment or unrelated profiling.
2. **Article 6(1)(f) purpose B:** proportionate website delivery and security with the no-tracking static implementation as reviewed; hosting logs and any platform-generated information are constrained to actual necessary provider operations, not an invented zero-log claim.
3. **Risks and safeguards:** accepts the documented ordinary-business residual risks, reasonable individual expectations, data minimisation, GDPR rights and objection handling, actual Google Workspace and Vercel contract/transfer contexts, and separation from customer-app data. Material changes trigger reassessment.
4. **Operational responsibility:** owner monitors `jarkko@prompted.fi` sufficiently to respond to privacy requests within legal deadlines and arranges reasonable coverage/access for absences or incidents. The owner already adopted a **monthly manual review of closed website-specific enquiries** on 26 Oct; the first actual post-launch review remains a future operating task and is not represented as done.
5. **Notice approval:** the exact FI/EN privacy notices identified by blob ID above accurately describe the business's current intended processing and are approved as the marketing website's public notices, subject to verification that the production host matches the protected reviewed candidate.
6. **External review and scope:** recognises no external qualified legal opinion is represented as obtained. This internal controller decision does not approve the general terms, commercial copy, imagery beyond its separate approval, real-device visual appearance, public DNS cutover or the site's launch.

**Explicit answer required:** An affirmative owner response acknowledging these conditions in the working conversation. The previously given “hyväksyn” accepted the **monthly review procedure only**, not this full sign-off packet. Do not mark this packet as approved or flip `privacy_legal` based on that earlier message.

**Decision:** PENDING · **Decision maker:** Prompted Oy owner (identified, not signed here) · **Date:** NOT YET SIGNED · **Evidence:** PENDING.

## Remaining release separation

If and only if the owner explicitly signs off this packet, record dated evidence and the exact approved privacy source SHA in `PUBLIC_RELEASE_APPROVALS.json`, then re-run the fail-closed CI and the privacy-specific status review. Keep `owner_release` and five other non-privacy gate statuses separate. The public-origin smoke test is a distinct cutover check **after** an expressly authorised staged release, before indexability/announcement. The production project is not changed by this record.
