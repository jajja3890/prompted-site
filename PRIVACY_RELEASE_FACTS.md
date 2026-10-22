# Prompted Oy marketing website — privacy release verification

Prepared 22 October 2026. Original FI/EN privacy notices for the new static marketing website; customer application out of scope.

## Factual release conditions
- [x] **Independent public-record corroboration** of the company name, business ID 3550114-7, and registered municipality Turku. Secondary listings cite YTJ/PRH; this does not independently verify the mailbox. Sources and verification date below.
- [ ] Verify that `jarkko@prompted.fi` is active, can receive subject-rights requests, and is monitored by the responsible Prompted Oy person.
- [ ] Name the actual corporate email provider, processors, roles, locations, contracts and international transfer basis.
- [x] **Published Vercel DPA text checked:** as of 22 October 2026, effective 31 March 2026; states scope includes Pro and Enterprise plans, identifies US processing and cross-border mechanisms including standard contractual clauses. This verifies the public contractual text, **not** that the specific Prompted Oy account's DPA and provider/subprocessor arrangements were accepted.
- [ ] Verify the actual Vercel plan/account DPA applicability, subprocessors, service locations, log retention/settings, and all production-injected cookies or scripts.
- [ ] Adopt the proposed 12-month non-customer enquiry deletion policy and implement an actual mailbox/contact-data deletion or review procedure.
- [ ] Complete legitimate-interest balancing for inbound B2B enquiries and website security.
- [ ] Verify public deployment's cookie/storage behaviour before asserting that no consent mechanism is needed.
- [ ] Confirm site operator's access-control and security claims and identify the privacy rights request owner.
- [ ] Approve exact FI/EN text and source commit, and keep the authenticated customer-app privacy terms separate.


## Independently checked reference facts (22 October 2026)

**Prompted Oy:** two Finnish public company information services report legal name *Prompted Oy*, business ID *3550114-7*, municipality *Turku* and cite the Finnish business register data. These listings are corroboration, not a fresh authoritative extract from the Finnish Trade Register; the controller must still confirm company data and operating contact:
- https://www.asiakastieto.fi/yritykset/fi/prompted-oy/35501147/rekisteritiedot
- https://www.taloustutka.fi/company/3550114-7

**Vercel DPA:** https://vercel.com/legal/dpa is marked updated **17 March 2026**, effective **31 March 2026**. It explicitly applies to Enterprise and Pro plans in its opening scope, lists US processing in international provisions, and supplies transfer clauses including EU SCCs. The published document alone does **not** prove which processor contracts, log retention, email backend or transfers actually apply to the connected site's final production configuration.

**Release behavior:** `tools/public_release_gate.py` now treats the existing terms `suunniteltu säilytyskäytäntö` and `our proposed retention practice` as unresolved, release-blocking placeholders. A responsible party must implement and verify the retention procedure, then update both notices to state **actual practice** rather than a future intention. No approval record by itself can evade this text-level check.

## Primary references
- GDPR Articles 6, 12–15, 17–22 and Chapter V: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- Traficom cookie guidance: https://kyberturvallisuuskeskus.fi/fi/viestintaverkkojen-ja-palveluiden-saantely/evasteet
- Vercel DPA: https://vercel.com/legal/dpa
- Vercel privacy notice: https://vercel.com/legal/privacy-notice

Until all facts and approvals are established, the site remains a protected noindex preview with visible legal DRAFT labels. No DNS or application changes are authorised.
