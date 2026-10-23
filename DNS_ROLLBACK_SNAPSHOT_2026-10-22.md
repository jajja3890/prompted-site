# prompted.fi — DNS and Vercel routing observation for rollback

**Captured 22 October 2026; READ ONLY.** This is an observed configuration report returned by the connected Vercel *domain configuration* API, not an authoritative registrar-zone export or a change request. The exact TTL, all DNS record types, full original zone and existing website hosting account remain to be verified at Domainhotelli before a cutover. Do not use this document as the sole rollback backup.

## Current observed routing

| Host | Vercel-reported routing observation | Service isolation |
| --- | --- | --- |
| `prompted.fi` | A values: `185.158.133.1`; no CNAME returned | Existing public **marketing site**; **not** assigned to new `prompted-site` Vercel project |
| `www.prompted.fi` | A values: `185.158.133.1`; no CNAME returned | Existing marketing www host; do not assume redirect behavior without testing |
| `app.prompted.fi` | CNAME `cname.vercel-dns-0.com.`; reported A values `76.76.21.123`, `66.33.60.35`; `configuredBy: A`, `misconfigured: false` | **Separate customer application `prompted`**, project `prj_MfK5ICUXV5eD0k6VuUiy3BMgCLkU`; never alter as part of marketing release |

Authoritative nameservers reported by Vercel: **`ns1.domainhotelli.fi` and `ns2.domainhotelli.fi`**. DNS service is external to Vercel. Vercel's `misconfigured: true` flag for apex/www is expected when checking hosts *not configured to point to Vercel* and is not evidence that the current external marketing site is broken.

**Marketing destination:** `prompted-site` project `prj_O7rI2YYJd1HTR7emNksmIalWiqe9`, connected to a draft review branch only. It has no `prompted.fi` or `www.prompted.fi` project-domain association. The verified domain and webroot project assignment are separate concepts.

## Cutover boundaries and exact remaining evidence

1. **Before any edit at Domainhotelli:** export or screenshot the authoritative `@`, `www`, `app` and all `MX/TXT/CAA` records and their TTLs; capture the date/time and original hosting environment. Cross-check the A/CNAME records against this Vercel observation. Current direct authoritative export unavailable to this assistant; DNS query from its sandbox timed out.
2. **No email interruption:** preserve all `MX`, SPF, DKIM and DMARC records unchanged. Mailbox routing must not be guessed from the website's host A record.
3. **Explicit public-owner release authorization, legal and asset rights approval required** for the exact source SHA, final Vercel release and cutover window. Keep the separate `app.prompted.fi` project and all authentication, storage and database settings unchanged.
4. **Assign only `prompted.fi` and the intended `www.prompted.fi` redirect** to approved marketing project after staging the eligible public bundle; use Vercel's per-project recommended DNS target at that time, not an old hardcoded sample value.
5. Verify certificate, both hostnames, FI/EN navigation and old URLs; separately verify `app.prompted.fi` remains reachable and unchanged.
6. **Rollback:** restore the exact *authoritative captured* pre-change `@` and `www` values/TTL and their original hosting routing. Never restore `app` from the snapshot unless an unrelated app-specific change was independently authorized.

## Separate preview-access limitation

Latest new-site review SHA `5906064c20c93639b484949c3ca0c1c1d2dbb4c2` has Vercel READY protected deployment and GitHub CI success. The Vercel connector can inspect metadata but cannot obtain a protected response or shareable preview: `get_access_to_vercel_url` returned 404 (deployment-scope lookup) and `web_fetch_vercel_url` returned 403 (protection access), with the tool recommending reauthorization for the project/team. This is a connector-scope blocker, **not** evidence that the website is down. Do not turn off SSO or weaken security.

**No DNS was changed; this file is for cutover preparation only.**
## Automated authoritative DNS evidence (overnight launch preflight)

Each GitHub Preview CI now runs `tools/dns_cutover_snapshot.py` as a **read-only, best-effort** query directly against `ns1.domainhotelli.fi` and `ns2.domainhotelli.fi` for the apex, www, app and DMARC hosts. It captures A/AAAA/CNAME/MX/NS/CAA/SOA (including answer TTL) and **redacts raw TXT values** from public CI artifacts. Failures produce a `PARTIAL_NOT_AUTHORITY_FOR_CUTOVER` report instead of blocking unrelated static QA. The status is only `AUTHORITATIVE_OBSERVED` when essential named answers are authoritative.

Snapshot output: `tools/dns_cutover_snapshot_results.json`, saved inside the `preview-release-audit` CI artifact. A positive observation does **not** replace exporting all DNS records/TTLs from Domainhotelli's owner account before changes. No DNS is modified. Protect `app.prompted.fi` and all email records.
