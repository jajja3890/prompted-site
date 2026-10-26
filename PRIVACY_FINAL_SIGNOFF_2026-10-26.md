# Prompted Oy: marketing-website privacy closure, 26 October 2026

**Status: NOT legally signed off.** Scope is **only** the new static FI/EN `prompted.fi` marketing website and emails arising from it. This record is deliberately separate from `app.prompted.fi`, Tekoälymörkö and customer-/employee-data processing. It contains no private emails, account credentials, invoices or tenant screenshots.

## What has actually been established

| Check | Status | Evidence |
| --- | --- | --- |
| Site publisher and controller identity | **Checked against external company listings, awaiting owner's final confirmation** | Prompted Oy, 3550114-7, Turku; see `PRIVACY_RELEASE_FACTS.md`. |
| Website implementation | **Verified on protected preview** | All 18 FI/EN routes responded HTTP 200; no first-party form, email sign-up, tracking SDK, marketing pixel, external font or external JS found in reviewed static pages; a deterministic fake-data Capability demo. |
| Browser storage and server responses | **Preview evidence only, not public production sign-off** | Local Chromium checked cookies/storage and third-party requests; sampled Vercel protected-preview HTTP responses contained no `Set-Cookie`. Preview SSO may differ. |
| Vercel project and team data-flow checks | **Verified read-only, 26 October** | Project `prompted-site`: **0 listed environment variables, 0 listed project connectors**. The connected team's **Drains list is empty**, including when filtered to this project. Vercel's platform-side logging and subprocessors still exist independently; see `VERCEL_PRIVACY_VERIFICATION_2026-10-26.md`. |
| DNS and live business mailbox | **Verified: DNS 23 October; Gmail read-only 26 October** | The connected Gmail account identifies itself as `jarkko@prompted.fi`. Recent incoming messages addressed to that mailbox and sent messages from the account were observed in Gmail, without sending any test email or displaying private correspondence. This supports account function and inbound/outbound usage; ongoing monitoring, reply deliverability and specific GDPR request handling remain unconfirmed. |
| Hosting-provider standard DPA | **Public terms verified, account applicability outstanding** | Vercel DPA updated 17 March 2026, effective 31 March 2026, published for Pro/Enterprise processing within its stated scope. This is not proof that Prompted Oy's account is on a qualifying plan or that every processing relationship is covered. |
| Data subject notice | **Complete bilingual draft only** | `content.json` generates `/fi/tietosuoja/` and `/en/privacy/`; actual mailbox retention and third-country processing need controller review before dropping DRAFT. |

## Smallest remaining operational closure checklist

1. **Privacy-request owner named; live process needs validation.** The founder explicitly confirmed on 26 October that he handles `jarkko@prompted.fi` privacy requests. `Prompted/Tietosuojapyynnöt` Gmail label was created on the same date, and a practical rights-request SOP now exists in `MARKETING_ENQUIRY_RETENTION_SOP.md`. This confirms responsibility and creates a triage mechanism, **not** automatic classification, a proven daily check or a fully tested request-response process. Absence coverage and first case drill remain pending.
2. **Google Workspace CDPA accepted; operational email handling remains open.** The company owner supplied an Admin Console screenshot showing **Cloud Data Processing Addendum (CDPA): Accepted by jarkko@prompted.fi on Oct 26, 2026**. This confirms tenant-specific acceptance. Still verify actual Workspace email-retention practices, access responsibilities and relevant subprocessors/transfers as needed for the final FI/EN privacy notice. **CDPA closed; operating controls pending.**
3. **Marketing-enquiry SOP drafted for the named owner; first operation pending.** The written workflow distinguishes requests, marketing enquiries, contracts/legal/accounting records and customer application data, and contains a proposed monthly review cycle. The owner has not yet expressly adopted that cadence or performed an evidenced sample review. **Pending: cadence adoption, first non-personal evidence log and actual disposal or retention decisions.**
4. **Vercel drain/configuration review completed; final contract/account checks remain.** On 26 October the connected Vercel APIs reported zero team/project drains, zero site environment variables and zero project connectors. The official runtime-log retention table was reviewed (Pro standard 1 day; Pro with Observability Plus 30 days); no exact duration is asserted for this account or for all edge/firewall/backups. **Still pending:** current team plan/add-on confirmation, contract/DPA applicability, actual Vercel infrastructure processing settings and applicable subprocessors/transfers. See `VERCEL_PRIVACY_VERIFICATION_2026-10-26.md`.
5. **Privacy notice and legal-basis sign-off.** Review FI/EN notice against those four actual operations, verify GDPR Article 6 bases and `LEGITIMATE_INTEREST_BALANCING.md`, confirm applicable processors/transfers/security wording, and approve the exact source revision and reviewer/date. Keep terms explicitly marketing-site-only and distinguish the authenticated application. **Pending: authorised controller/legal review.**
6. **Post-cutover privacy smoke test.** Before publicly indexing the new production host, inspect `https://prompted.fi` without authenticated preview bypass for response headers, cookies, network calls, analytics and device storage; re-evaluate consent before adding non-essential technologies. Keep `privacy_legal` blocked if the deployed host differs from the reviewed implementation. **Pending: future public-domain release phase.**

## 26 October 2026 — owner assigned and Gmail rights-request label created

The company founder explicitly accepted responsibility for receiving and answering privacy requests at `jarkko@prompted.fi` on 26 October 2026. The Gmail account now has the label `Prompted/Tietosuojapyynnöt` for future manual classification; no pre-existing messages were modified and no automatic filter or scheduled monitoring was installed. The full practical procedure is in `MARKETING_ENQUIRY_RETENTION_SOP.md`. The absence contingency, monitoring discipline, regular retention review and first real case rehearsal still require operational evidence. This is a role assignment, not a designation of an Article 37 DPO.

## Connected mailbox audit boundary, 26 October 2026

Read-only verification used the actual newly authorised Gmail account. The account profile is `jarkko@prompted.fi`; both inbound and sent traffic were present in October 2026. No Gmail administrative capabilities, Workspace CDPA acceptance, mailbox account-retention configuration or monitoring assignment were exposed by these mailbox operations. The Gmail search was **not** a compliance audit of every historical email or data-subject request. Do not store personal email bodies, sender identities, message IDs or subjects in this public project or equate an inbox message with a validated GDPR rights request.

## 26 October 2026 — Workspace Admin Console CDPA status (owner-provided visual evidence)

The company owner provided a screenshot from **Google Workspace Admin Console → Account settings → Legal and compliance → Security and Privacy Additional Terms**. At the time of the screenshot, **Cloud Data Processing Addendum (CDPA): Not accepted**. The adjacent optional certification of European data protection law also says **Not accepted**; Google documents that this specific certification step applies where the customer's billing address is outside EMEA. The HIPAA business-associate amendment also says **Not accepted**; there is no established HIPAA need for this marketing website. These visible statuses do not prove whether the CDPA is separately incorporated by reference in the existing Workspace agreement.

**Historical action — completed 26 October 2026:** the authorised Workspace administrator subsequently accepted the CDPA; the screenshot confirmation in the next section supersedes this earlier pending state. See Google's help: https://knowledge.workspace.google.com/admin/compliance/privacy-compliance-and-records-for-google-workspace-and-cloud-identity

## 26 October 2026 — subsequent Google Workspace CDPA acceptance (owner screenshot)

A later screenshot from the same tenant's **Security and Privacy Additional Terms** page explicitly states **“Accepted by jarkko@prompted.fi on Oct 26, 2026.”** This **supersedes the earlier “Not accepted” observation**. Record the CDPA acceptance as **verified on owner-provided account-admin screenshot**. The screenshot has not been placed in the public GitHub repository. The neighbouring **EU-law certification** relates to qualifying billing addresses outside EMEA, and the **HIPAA amendment** is unrelated to ordinary Prompted B2B marketing absent applicable US healthcare obligations. Neither should be assumed accepted. CDPA acceptance does not establish inbox retention, deletion, monitoring, all transfers or final GDPR compliance.

## 26 October 2026 — direct Vercel hosting inspection

A read-only inspection confirmed that `prompted-site` contains no listed environment variables or project connector connections, and **neither project-filtered nor team-wide Vercel Drains were configured**. Current published Vercel DPA (Pro/Enterprise) and runtime-log retention documentation were checked separately. The connector does not show the subscribed billing plan or Observability Plus entitlement, so no exact account-specific processing/retention period is claimed. Evidence, official links and remaining tasks: `VERCEL_PRIVACY_VERIFICATION_2026-10-26.md`.

## FI/EN privacy notice source consistency check, 26 October 2026

The current `content.json` contains **14 aligned privacy-notice sections in both Finnish and English**. Both languages identify Prompted Oy as controller and `jarkko@prompted.fi` as contact; they disclose Vercel and Google Workspace, categories and purposes, possible transfers outside the EEA, retention **criteria** (not a fabricated 12-month or platform-log deadline), cookies/analytics, security, data subject rights, Finnish authority, and a boundary for the authenticated application. Both versions contain no fixed number of days or months for Vercel log deletion. The owner's privacy-role and Google's CDPA are internal evidence, and need not create an extraneous personal attribution or legal certificate in the public notice.

**Draft review outcome:** wording remains suitable for final legal/controller review without changing the public-site source text. Contract/account plan applicability, active marketing-retention practice, any final host tracking/cookie behaviour, and the company's approval of the exact version still remain open. In particular, no new Google/Vercel claim should be asserted merely from a vendor standard document.

## Exact supplier references and implications

- [Vercel DPA](https://vercel.com/legal/dpa), updated 17 March 2026, effective 31 March 2026, sections 1, 4, 7 and 13: scope, roles, subprocessors and transfers. Standard text **does not validate the connected team's commercial agreement**.
- [Vercel Runtime Logs](https://vercel.com/docs/logs/runtime): plan-dependent log visibility/retention; compare with the actual team plan and any observability add-on, and investigate drains separately.
- [Google Workspace: Privacy compliance and records](https://knowledge.workspace.google.com/admin/compliance/privacy-compliance-and-records-for-google-workspace-and-cloud-identity), updated 10 August 2026: CDPA may already be included; if not, super admin can accept under Legal and compliance.
- [Traficom: Evästeet](https://www.kyberturvallisuuskeskus.fi/fi/viestintaverkkojen-ja-palveluiden-saantely/evasteet): non-essential cookies/equivalent access requires consent; banner should reflect **actual use**, not be deployed for appearance.
- [GDPR, Articles 5–6 and 12–15](https://eur-lex.europa.eu/eli/reg/2016/679/oj): information duties and legal bases; review final language against actual operations.

## Release-decision boundary

- `image_rights` is owner-attested approved in `PUBLIC_RELEASE_APPROVALS.json`, scoped to five exact Git blobs. Image approval is **not** legal acceptance of the full website.
- `privacy_legal` remains `pending` until all directly relevant account, operational, text and post-cutover checks are evidenced.
- `owner_release` remains `pending` and **explicit_public_release=false**. Do not merge the design-review PR, deploy a public release, alter DNS, remove the preview noindex flag or touch `app.prompted.fi` as a result of this document.
