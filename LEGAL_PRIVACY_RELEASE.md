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
The new Vercel `prompted-site` project presently has only Vercel-generated domains, not `prompted.fi`. Vercel SSO protects previews. The connected protected-Preview fetch returned **access denied**, so live HTTP/CSP, redirect, cookie and visual acceptance against the deployment are still unverified. Do not relax preview protection or touch production DNS to workaround missing connection authorization.
