# Prompted Oy marketing website — privacy release verification

Prepared 22 October 2026. Original FI/EN privacy notices for the new static marketing website; customer application out of scope.

## Factual release conditions
- [x] **Independent public-record corroboration** of the company name, business ID 3550114-7, and registered municipality Turku. Secondary listings cite YTJ/PRH; this does not independently verify the mailbox. Sources and verification date below.
- [x] **Live connected Gmail account observed 26 October 2026:** current profile identifies `jarkko@prompted.fi`; recent inbound and outgoing business mail exists. This establishes active mailbox access and actual inbound/outbound use, not yet a specific GDPR-request reply test.
- [ ] **Still to verify:** privacy-request owner, continuous/absence coverage, a documented rights-request procedure, and any fresh send/reply test desired by the controller.
- [x] **Previously confirmed corporate email system:** Prompted Oy's `jarkko@prompted.fi` mailbox was connected to **Google Workspace (Gmail)** in the owner's account setup, reconfirmed 1 September 2026. This identifies the previously configured provider but not current live MX or Workspace admin contract status.
- [x] **Authoritative mail routing verified 23 October 2026:** both Domainhotelli authoritative nameservers answered `prompted.fi MX` with the five established Google Workspace mail exchangers, TTL 3600 seconds; no DNS changes were made. See `DNS_AUTHORITY_OBSERVED_2026-10-23.md`.
- [x] **Google Workspace CDPA accepted 26 October 2026:** owner-provided Google Workspace Admin Console screenshot shows **“Accepted by jarkko@prompted.fi on Oct 26, 2026”** for Cloud Data Processing Addendum. Earlier “Not accepted” status was superseded. Keep the private screenshot in the company's compliance evidence; do not publish it in the GitHub repository.
- [ ] **Still open:** monitoring of privacy requests, email-data retention and deletion implementation, remaining account settings, and applicable subprocessors/transfer details. CDPA acceptance does not close these operational matters.
- [x] **Published Vercel DPA text checked:** as of 22 October 2026, effective 31 March 2026; states scope includes Pro and Enterprise plans, identifies US processing and cross-border mechanisms including standard contractual clauses. This verifies the public contractual text, **not** that the specific Prompted Oy account's DPA and provider/subprocessor arrangements were accepted.
- [ ] Verify the actual Vercel plan/account DPA applicability, subprocessors, service locations, log retention/settings, and all production-injected cookies or scripts.
- [x] FI/EN notice draft now describes **retention criteria rather than an unimplemented 12-month deletion deadline**. This is a copy correction, not evidence of operational deletion.
- [ ] Adopt and operationalise a mailbox/contact-data review and deletion process; record the accountable owner, exceptions, frequency and actual evidence. See `MARKETING_ENQUIRY_RETENTION_SOP.md`.
- [x] A scope-limited draft balancing worksheet has been prepared for inbound enquiries and Vercel technical security data: `LEGITIMATE_INTEREST_BALANCING.md`. This is a documented assessment draft, **not** a final legitimate-interest conclusion.
- [ ] Complete the assessment using actual retention/security/processor facts and obtain accountable Prompted Oy approval before adopting legal basis and publishing notice.
- [ ] Verify public deployment's cookie/storage behaviour before asserting that no consent mechanism is needed.
- [ ] Confirm site operator's access-control and security claims and identify the privacy rights request owner.
- [ ] Approve exact FI/EN text and source commit, and keep the authenticated customer-app privacy terms separate.


## Independently checked reference facts (22 October 2026)

**Prompted Oy:** two Finnish public company information services report legal name *Prompted Oy*, business ID *3550114-7*, municipality *Turku* and cite the Finnish business register data. These listings are corroboration, not a fresh authoritative extract from the Finnish Trade Register; the controller must still confirm company data and operating contact:
- https://www.asiakastieto.fi/yritykset/fi/prompted-oy/35501147/rekisteritiedot
- https://www.taloustutka.fi/company/3550114-7

**Google Workspace contractual background:** Google's [Workspace privacy compliance guide](https://knowledge.workspace.google.com/admin/compliance/privacy-compliance-and-records-for-google-workspace-and-cloud-identity) (updated August 10, 2026) documents the Cloud Data Processing Addendum, which may already be incorporated in a customer agreement or may require review/acceptance by an administrator. Its [GDPR commitments](https://cloud.google.com/privacy/gdpr) describe Workspace SCC frameworks. Neither public page proves acceptance or configuration in Prompted Oy's own tenant.

**Vercel DPA:** https://vercel.com/legal/dpa is marked updated **17 March 2026**, effective **31 March 2026**. It explicitly applies to Enterprise and Pro plans in its opening scope, lists US processing in international provisions, and supplies transfer clauses including EU SCCs. The published document alone does **not** prove which processor contracts, log retention, email backend or transfers actually apply to the connected site's final production configuration.

**Release behavior:** Both notices were redrafted to describe *retention criteria* without promising an unimplemented 12-month deletion deadline. Release requires explicit `privacy_legal` owner/legal sign-off and a verified operational handling procedure; the seven fail-closed approval gates remain unchanged. The release code retains a check for unimplemented fixed-deadline placeholders if they return.

## Primary references
- GDPR Articles 6, 12–15, 17–22 and Chapter V: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- Traficom cookie guidance: https://kyberturvallisuuskeskus.fi/fi/viestintaverkkojen-ja-palveluiden-saantely/evasteet
- Vercel DPA: https://vercel.com/legal/dpa
- Vercel privacy notice: https://vercel.com/legal/privacy-notice

Until all facts and approvals are established, the site remains a protected noindex preview with visible legal DRAFT labels. No DNS or application changes are authorised.


## 26 October 2026 — Workspace tenant-specific CDPA approval

An owner-provided screenshot from **Google Workspace Admin Console → Account settings → Legal and compliance** confirms **Cloud Data Processing Addendum accepted by jarkko@prompted.fi on 26 October 2026**. This is a directly observed acceptance status of the actual Prompted Workspace tenant, as distinct from general Google public documentation. It is sufficient to close the **CDPA acceptance** subtask, not the overall `privacy_legal` release gate. Account operations, legal wording and full production privacy behaviour remain under review.

## 26 October 2026 — read-only Gmail mailbox verification

The newly connected Gmail account reported profile email `jarkko@prompted.fi`. Existing inbound messages to that address (including a message dated 26 October) and outgoing messages sent from the account (including 25 October) were observed. This verifies a functioning configured mailbox and recent inbound/outbound correspondence, **not** a deliberately sent external bounce/reply test, constant owner monitoring, an accepted Google Workspace CDPA or a deletion workflow. Private sender names, email subjects, bodies and message IDs were not copied into this public repository. The operational evidence and remaining steps are in `PRIVACY_FINAL_SIGNOFF_2026-10-26.md`.

## 26 October 2026 — directly observed protected-preview website behaviour (not legal sign-off)

Read-only Vercel connector requests against the isolated `prompted-site` protected preview returned **HTTP 200 on all 18 FI/EN pages**. Sampled HTML response headers on FI home, FI Capability demo, FI privacy and static assets include a restrictive self-only Content Security Policy, `X-Robots-Tag: noindex, nofollow`, `X-Content-Type-Options: nosniff`, HTTPS HSTS, and no `Set-Cookie` header on those sampled application responses. This inspection was performed using the Vercel connector's temporary protected-deployment access, **not** a public production host/browser session.

The reviewed page source loads JavaScript and styles only from this site's own `/assets/` paths. Local Chromium HTTP QA for all 18 routes found no cookies, no localStorage writes and no unexpected third-party network requests under the simulated preview CSP (CI run [40305814827](https://github.com/jajja3890/prompted-site/actions/runs/40305814827)). The public Capability demo remains deterministic sample content, without an external AI API or analytics SDK.

**Boundaries:** These are observations of the current preview code and selected server responses. They do not certify what Vercel's login/SSO, edge infrastructure, production domain, integrated analytics or any future additions will set in an end user's browser. The actual Google Workspace tenant contract, Vercel account-level processor agreement, hosting log retention, mailbox handling and final production cookie/storage inventory still require verification. No marketing-site `privacy_legal` approval is implied or recorded.

## 23 October 2026, 00:46:15 UTC — read-only authoritative check passed

The GitHub Actions [overnight CI 39880019125](https://github.com/jajja3890/prompted-site/actions/runs/39880019125) completed with **SUCCESS**, including a live read-only DNS query against Domainhotelli's delegated authoritative nameservers. Result `AUTHORITATIVE_OBSERVED`, **4/4 required DNS queries confirmed**, zero query errors. Evidence report lives in the CI artifact `preview-release-audit/dns_cutover_snapshot_results.json`, and a durable human-readable record is in `DNS_AUTHORITY_OBSERVED_2026-10-23.md`.

This now verifies current apex/www A answers and TTL, plus Google MX routing and the protected app CNAME. It does **not** establish mailbox delivery, Google contractual acceptance, permission to modify the registrar zone, or all raw TXT/DKIM records, and does not lift release gates.
