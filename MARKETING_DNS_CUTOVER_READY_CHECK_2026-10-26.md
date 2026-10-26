# Prompted.fi — updated marketing-only DNS and rollback decision sheet

**Observed 26 October 2026 by read-only Vercel account access. NO DNS or project assignment changes. NOT AUTHORISED FOR CUTOVER.**

## Current confirmed account mappings

| Domain/host | Observed routing or association | Cutover rule |
| --- | --- | --- |
| `prompted.fi` | Domain is verified in Vercel team, externally served by **Domainhotelli** `ns1.domainhotelli.fi`, `ns2.domainhotelli.fi`; current Vercel observed A **185.158.133.1**. No attachment to `prompted-site`. | Change marketing apex only after final full Domainhotelli zone export and owner release. |
| `www.prompted.fi` | Current observed A **185.158.133.1** and same external authority. | Prepare intended redirect/canonical semantics; do not change before marketing cutover approval. |
| `app.prompted.fi` | **Only Vercel project-domain association under prompted.fi**; bound to separate app project `prj_MfK5ICUXV5eD0k6VuUiy3BMgCLkU`, verified. 23 Oct authority snapshot showed CNAME `cname.vercel-dns-0.com.`. | **NEVER edit** as part of marketing-site DNS, SSL, release, app/Supabase/database work. |
| Email records | 23 Oct authoritative MX snapshot documented five Workspace MX records, TTL 3600. SPF/DKIM/DMARC/TXT details not fully export-backed. | Never change/remove MX, TXT, DKIM, SPF, DMARC, CAA or nameservers for this marketing cutover. |

New site: Vercel project `prompted-site`, ID `prj_O7rI2YYJd1HTR7emNksmIalWiqe9`; **`live=false`** with authenticated previews. No `prompted.fi` apex/www project domain association on the account as of this observation.

**Important:** Vercel's **newly queried recommended target values** differ from earlier generic examples (the 26 Oct response lists recommended IPv4 combinations `216.150.1.1` and `216.150.16.1`, fallback `76.76.21.21`, and a deployment-specific recommended CNAME). **None of these is an authorised manual DNS edit now**; query and follow the assigned project's actual live recommendation at the moment of the approved cutover. Do not treat stale sample IPs as the target.

## Strict cutover runbook (not executed)

1. **Snapshot owner zone**: before changing anything, export/screenshoot the *entire authoritative* Domainhotelli zone and original hosting configuration, including apex/www A/AAAA/CNAME, every TXT/MX/CAA/CNAME, TTL, current host/origin, SSL behavior and current website route behavior. Keep private zone secrets out of the public repo; record a non-secret completion receipt.
2. **Freeze release**: all seven approvals and the privacy sub-safeguards must pass, with an exact owner-approved Git commit. Preserve existing indexed paths and current marketing content as rollback evidence.
3. **Stage final approved release** on a separate protected temporary URL (without transferring apex), verify all 18 FI/EN routes, security, image rendering, both contact links, on-page policies, robots configuration, old URL redirects and social share.
4. **Cutover**: assign only the approved marketing apex and `www` to the intended project, apply only the fresh project-specific DNS records while leaving app, email and nameservers alone. Verify certificate and expected public response before indexing or marketing announcement.
5. **Immediate public smoke**: check root FI, EN, products, demos, legal pages, contact, redirects, HTML/canonical/OG, cookies/storage and network calls. Recheck `app.prompted.fi` unaffected, and monitor mail. If any material problem, stop promotion.
6. **Rollback**: restore *the exact captured original apex/www records and TTLs* and original hosting account routing; verify old legal/public routes and preserve the independent app. Never reconstruct old records from only this document or from Vercel's current recommendations. Record rollback actions/time.

## What remains outstanding

- **Domainhotelli complete zone/export, original host credential/rollback readiness, and human responsible approval** still missing from this chat's connected access. Previous authoritative partial 23 Oct snapshot is helpful but **not a complete rollback backup**.
- Full `domain_rollback` approval stays **pending**.
- Owner public release of exact source SHA stays **pending**.
- Production changes, DNS edits, email records and the customer app have **not** been made.

Related evidence: `DNS_AUTHORITY_OBSERVED_2026-10-23.md`, `DNS_ROLLBACK_SNAPSHOT_2026-10-22.md`, `RELEASE_CUTOVER_PLAN.md`.
