# Prompted Oy — 26 October 2026 privacy controller sign-off packet

**Status: OWNER APPROVAL RECORDED WITH PRELAUNCH CONDITIONS ON 26 OCTOBER 2026.** This is a scoped internal controller decision, not an external legal opinion or permission to publish.

## What exactly is being reviewed

**Website:** the new static FI/EN `prompted.fi` marketing site. **Out of scope:** `app.prompted.fi` authenticated customer processing, Prompted employee/customer learning evidence, and Tekoälymörkö.

**Source files pinned by Git blob ID at review time (26 October 2026):**
- FI/EN notice source `content.json`: `b6e4e37f4b58de1f4b9a7239571087d506105eab`
- FI privacy page `fi/tietosuoja/index.html`: `73f278c7291312ea14ff385fa07e42f3648ba065`
- EN privacy page `en/privacy/index.html`: `3d14c9392f7315ddc4610d0034f920dd704bdf94`
- Original reviewed balancing assessment `LEGITIMATE_INTEREST_BALANCING.md`: `a7a2d5e396162e959e7f82d1572c3dca165a1459`. Updated owner-annotated assessment blob: `c2962cae70e817c80b08aa3a89c6cc892158f091`.
- Adopted retention/rights procedure `MARKETING_ENQUIRY_RETENTION_SOP.md`: `69ae4b74ed42be8e7fb3c31ad7fabdb6a823813b`

**Supporting technical evidence:** CI success at commit `a36d9b23ce6d0a107f7527a21e3304f2aa9fc6b3` (run 40325486171, 26 Oct), including FI/EN browser QA and fail-closed public release guard; protected Vercel preview on the marketing site. Subsequent changes only to internal legal review notes and balancing materials still require current CI pass. **Successful CI is not evidence of legal sign-off.**

## Scope of the expressly adopted controller decision

The Prompted Oy owner agreed to the following, **only for the defined marketing website**:

1. **Article 6(1)(f) purpose A:** replies and requested follow-ups to voluntary incoming business enquiries using only relevant contact/message data; no automatic newsletters, cold lead enrichment or unrelated profiling.
2. **Article 6(1)(f) purpose B:** proportionate website delivery and security with the no-tracking static implementation as reviewed; hosting logs and any platform-generated information are constrained to actual necessary provider operations, not an invented zero-log claim.
3. **Risks and safeguards:** accepts the documented ordinary-business residual risks, reasonable individual expectations, data minimisation, GDPR rights and objection handling, actual Google Workspace and Vercel contract/transfer contexts, and separation from customer-app data. Material changes trigger reassessment.
4. **Operational responsibility:** owner monitors `jarkko@prompted.fi` sufficiently to respond to privacy requests within legal deadlines and arranges reasonable coverage/access for absences or incidents. The owner already adopted a **monthly manual review of closed website-specific enquiries** on 26 Oct; the first actual post-launch review remains a future operating task and is not represented as done.
5. **Notice approval:** the exact FI/EN privacy notices identified by blob ID above accurately describe the business's current intended processing and are approved as the marketing website's public notices, subject to verification that the production host matches the protected reviewed candidate.
6. **External review and scope:** recognises no external qualified legal opinion is represented as obtained. This internal controller decision does not approve the general terms, commercial copy, imagery beyond its separate approval, real-device visual appearance, public DNS cutover or the site's launch.

**Decision record:** After receiving the precise separate question whether the company approves both scoped Article 6(1)(f) assessments and the 26 October FI/EN notices subject to operational safeguards, monitoring during absences and reassessment on material change, the founder explicitly replied **yes**. This is a different decision from the earlier monthly-retention policy acceptance. The company approved these legal assessments and exact notices **conditionally**, but has not thereby attested that every operational safeguard has already been tested or activated.

**Decision:** APPROVED SUBJECT TO THE DOCUMENTED SAFEGUARDS · **Decision maker:** Jarkko Sjöman, Prompted Oy founder · **Date:** 26 October 2026 · **Evidence:** separate explicit affirmative reply in this conversation accepting the two assessed purposes and FI/EN privacy notices, conditional on safeguards, absence monitoring and reassessment of material changes.

## Remaining release separation

The owner has now approved this specifically scoped privacy content and balancing. Record the approval in `PUBLIC_RELEASE_APPROVALS.json`, preserving the exact reviewed file identifiers and **requiring actual evidence of prelaunch privacy-request continuity before an eligible public bundle may be prepared**. This decision does not approve website publication, commercial copy, DNS, devices, or the other gates. Do not mark conditional operating checks as complete on the strength of owner acceptance alone.
