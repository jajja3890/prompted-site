# Website legal and privacy release review

21 October 2026 · **DRAFT / NOT LEGALLY APPROVED / DO NOT PUBLISH**

Scope: marketing website **only**. This is not a privacy notice or DPA for the authenticated Capability application, Coach or Data customer processing.

## Improved copy
- FI and EN notices now identify the data subject's contact route, email and technical data categories, purpose, proposed legal grounds, recipients, retention criteria, international transfer review, cookies, rights and automated-decision disclosures.
- Added explicit owner verification flags to unconfirmed processing, hosting and storage statements rather than inventing retention periods or overseas processor arrangements.
- Terms make clear the static marketing site does not take orders, show real client outcomes or supersede a written B2B contract.
- Only deterministic sample data on Capability public demo; no form, analytics script, tracking SDK or user profiles visible in the checked source.

## To complete before removing DRAFT / noindex
1. Confirm company business ID, contact inbox and actual operating entity.
2. Verify the mailbox provider, Vercel DPA/hosting logs, subprocessors and any EEA-to-third-country transfer safeguards.
3. Confirm email/technical lawful grounds, legitimate-interest assessment (if relying on Art. 6(1)(f)), exact retention periods or legitimate determining criteria.
4. Review the **deployed** public origin for security, analytics, Vercel edge logs, cookies/storage and any third-party scripts. Existing repository static tests do **not** establish cookie consent requirements for the eventual host.
5. Approve FI and EN language by responsible company decision maker and qualified privacy/legal reviewer. Document approval date and version before publication.
6. Confirm the customer app has **separate** privacy, service agreement and any processing agreement as appropriate. Do not conflate them with the public website.

Normative checklist: GDPR Art. 13, https://eur-lex.europa.eu/eli/reg/2016/679/art_13/oj

## Host and release
The new Vercel `prompted-site` project still has only Vercel-generated domains, not `prompted.fi`. Its previews remain protected by SSO. **26 October 2026: protected-preview access was restored** through the Vercel connector; all 18 FI/EN routes returned HTTP 200, and the current protected preview was checked for CSP, HSTS, `X-Robots-Tag: noindex`, assets and legacy redirects. Twelve slash/no-slash legacy redirects were independently rechecked against the deployed preview. In checked application HTTP responses, no `Set-Cookie` header appeared. Local Chromium browser QA checked cookie/storage behaviour, external requests and demo interactions. These observations do **not** verify end-user SSO cookies, actual public production domain, mail-provider processing, or completed legal/rights/device approval. See `PRIVACY_RELEASE_FACTS.md` and successful QA run [40310914435](https://github.com/jajja3890/prompted-site/actions/runs/40310914435). Do not relax preview protection or touch production DNS before explicit owner release.

### Supplier-document verification and remaining operator controls (26 October 2026)
- **Vercel:** the public [Data Processing Addendum](https://vercel.com/legal/dpa) was updated 17 March 2026, effective 31 March 2026. Its stated processor scope covers **Pro and Enterprise** customers, with subprocessors and SCC-based international transfer provisions. The Vercel connection identifies the site's team and project but **does not establish Prompted Oy's actual contract plan/acceptance, full logs settings, or the legally applicable controller/processor roles for every data category**.
- **Google Workspace:** [Google's admin compliance guidance](https://knowledge.workspace.google.com/admin/compliance/privacy-compliance-and-records-for-google-workspace-and-cloud-identity) explains the CDPA. **The actual Prompted Workspace account now shows CDPA accepted by jarkko@prompted.fi on 26 October 2026**, verified in an owner-provided Admin Console screenshot. This closes the tenant-specific CDPA acceptance question. It does not verify the email retention process, monitoring responsibility or all transfer and subprocessor details.
- **Cookies:** [Traficom's guidance](https://kyberturvallisuuskeskus.fi/fi/viestintaverkkojen-ja-palveluiden-saantely/evasteet) distinguishes essential technologies from non-essential cookies/device access requiring consent. No consent banner is proposed for the current no-tracking static preview **solely on the checked behaviour**; re-evaluate if analytics, pixels, third-party embeds, or production-set non-essential technology is added.
- **Operational owner actions:** Gmail inbound/outbound activity and Workspace CDPA acceptance are now verified. Identify who monitors `jarkko@prompted.fi` for data subject requests; adopt the enquiry closure/retention review SOP with an accountable reviewer and sample evidence; inspect final production cookies/headers and Vercel account contract/logging and remaining Google email practices. Keep all access credentials and personal inbox data out of this public repository. Record FI/EN legal review and explicit company release approval only after those facts are satisfied.
