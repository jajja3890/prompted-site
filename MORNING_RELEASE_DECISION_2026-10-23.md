# Prompted.fi — morning release decision brief (23 October 2026)

**Status: TECHNICAL PREVIEW QA PASS; PUBLICATION NO GO UNTIL EXPLICIT APPROVALS.** Aimed at getting the new marketing site published the same day when legally and operationally permitted, without risking customer systems.

**Latest fully passed source under this overnight run:** `ce4874248dd6e26ab6e52afb6ec7b11e8fc06456`, CI [39880019125](https://github.com/jajja3890/prompted-site/actions/runs/39880019125), all steps SUCCESS. (This brief may be added in a subsequent documentation-only commit, so review the final PR head before approving.)

**Verified delivery:** 18/18 static FI/EN pages, 300/300 dual-path Capability browser tests, 264 local served-HTTP/CSP checks, 32 responsive browser screenshots with zero reported automated serious/critical accessibility findings; fail-closed public release gate has 7 pending approvals and publishes nothing. FI/EN privacy + terms are complete drafts. Bilingual privacy retention wording uses need-based criteria; it no longer promises an unimplemented 12-month deletion deadline. Google mail exchange DNS and marketing/app domain isolation verified authoritatively (see DNS evidence).

## Highest-value morning decisions, grouped into three conversations

**A. Company facts and rights (owner or delegated responsible reviewer):** confirm Prompted Oy's right to use the official original brand masters, H01 synthetic architecture image and derivative share image for commercial marketing; confirm FI and EN company website privacy/terms, operational enquiry review/deletion approach, actual Google Workspace account DPA, Vercel DPA and any actual cookies/logs. These are approval decisions, not technical obstacles removable by more coding. Do not mark approved without verifiable evidence. Files: `IMAGE_RIGHTS_REGISTER.md`, `PRIVACY_RELEASE_FACTS.md`, `MARKETING_ENQUIRY_RETENTION_SOP.md`.

**B. Protected live preview acceptance:** reauthorize Vercel connection for `prompted-site` project if needed; verify actual live protected preview under SSO (real HTTP, headers, cookies and smartphone). The connector has read metadata but its protected preview HTTP fetch has been rejected 403. Never disable SSO as a workaround. Confirm buyer and participant demo paths, FI/EN language links and legal pages.

**C. Publication and rollback decision:** approve exactly one source SHA and a cutover window. Export full authoritative Domainhotelli zone/TTLs, preserving `app.prompted.fi`, `MX`, `TXT`, SPF/DKIM/DMARC. Run `tools/public_release_gate.py --prepare` only after evidence-approved manifest, stage the separately assembled public output, test the staged public bundle and redirect mapping before attaching apex/www. Only then change the two marketing hosts; restore captured previous host settings on failure.

## Deliverable and guardrail

- **Marketing Vercel project:** `prompted-site`, project `prj_O7rI2YYJd1HTR7emNksmIalWiqe9`, protected and preview-only.
- **Customer app Vercel project:** `prompted`, `prj_MfK5ICUXV5eD0k6VuUiy3BMgCLkU`, `app.prompted.fi`. **Never touch** its settings, secrets, customer auth, database or DNS.
- **Live marketing domain:** existing external hosting at current apex/www `185.158.133.1`, authoritative TTL 3600 s (23 Oct snapshot).
- **Morning GO requires:** seven evidenced approvals; truthful FI/EN notices; licensed/authorised artwork and logo; preview HTTP/device acceptance; full DNS rollback evidence; staged production bundle QA; explicit owner go-live instruction.
- The `owner_release` approval must now record `approved_commit_sha` equal to the **exact HEAD of the proposed release**. Any post-approval code change requires renewed sign-off; a dated project-wide blanket approval cannot bypass this check.

There is no hidden background or auto-deploy guarantee. If these approvals are not available, **do not publish**; the protected preview remains usable for review.
