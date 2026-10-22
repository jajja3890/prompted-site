# Prompted Oy marketing website — privacy release verification

Prepared 22 October 2026. Original FI/EN privacy notices for the new static marketing website; customer application out of scope.

## Factual release conditions
- [x] **Independent public-record corroboration** of the company name, business ID 3550114-7, and registered municipality Turku. Secondary listings cite YTJ/PRH; this does not independently verify the mailbox. Sources and verification date below.
- [ ] Verify that `jarkko@prompted.fi` is active, can receive subject-rights requests, and is monitored by the responsible Prompted Oy person.
- [x] **Previously confirmed corporate email system:** Prompted Oy's `jarkko@prompted.fi` mailbox was connected to **Google Workspace (Gmail)** in the owner's account setup, reconfirmed 1 September 2026. This identifies the previously configured provider but not current live MX or Workspace admin contract status.
- [ ] Recheck live mailbox and MX routing; verify Google Workspace Cloud Data Processing Addendum (CDPA) acceptance, subprocessor list, processing locations, applicable EEA transfer safeguards, and deletion policies in the current tenant.
- [x] **Published Vercel DPA text checked:** as of 22 October 2026, effective 31 March 2026; states scope includes Pro and Enterprise plans, identifies US processing and cross-border mechanisms including standard contractual clauses. This verifies the public contractual text, **not** that the specific Prompted Oy account's DPA and provider/subprocessor arrangements were accepted.
- [ ] Verify the actual Vercel plan/account DPA applicability, subprocessors, service locations, log retention/settings, and all production-injected cookies or scripts.
- [ ] Adopt the proposed 12-month non-customer enquiry deletion policy and implement an actual mailbox/contact-data deletion or review procedure.
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

**Release behavior:** `tools/public_release_gate.py` now treats the existing terms `suunniteltu säilytyskäytäntö` and `our proposed retention practice` as unresolved, release-blocking placeholders. A responsible party must implement and verify the retention procedure, then update both notices to state **actual practice** rather than a future intention. No approval record by itself can evade this text-level check.

## Primary references
- GDPR Articles 6, 12–15, 17–22 and Chapter V: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- Traficom cookie guidance: https://kyberturvallisuuskeskus.fi/fi/viestintaverkkojen-ja-palveluiden-saantely/evasteet
- Vercel DPA: https://vercel.com/legal/dpa
- Vercel privacy notice: https://vercel.com/legal/privacy-notice

Until all facts and approvals are established, the site remains a protected noindex preview with visible legal DRAFT labels. No DNS or application changes are authorised.
