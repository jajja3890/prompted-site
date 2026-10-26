# Prompted.fi authoritative DNS snapshot — 23 October 2026

**Observation time:** 2026-10-23 00:46:15 UTC. **Source:** [GitHub Actions CI 39880019125](https://github.com/jajja3890/prompted-site/actions/runs/39880019125) artifact `preview-release-audit/dns_cutover_snapshot_results.json`. Queried **authoritative** `ns1.domainhotelli.fi` (resolved at 31.217.196.245) and `ns2.domainhotelli.fi` (resolved at 35.243.183.207). Result: `AUTHORITATIVE_OBSERVED`, 4/4 critical queries verified, zero query errors. Queries were read-only and no credentials were accessed.

| Name | Record | Observed value | TTL |
| --- | --- | --- | --- |
| `prompted.fi` | A | `185.158.133.1` | 3600 s |
| `www.prompted.fi` | A | `185.158.133.1` | 3600 s |
| `app.prompted.fi` | CNAME | `cname.vercel-dns-0.com.` | 3600 s |
| `prompted.fi` | MX priority 1 | `ASPMX.L.GOOGLE.COM.` | 3600 s |
| `prompted.fi` | MX priority 5 | `ALT1.ASPMX.L.GOOGLE.COM.`, `ALT2.ASPMX.L.GOOGLE.COM.` | 3600 s |
| `prompted.fi` | MX priority 10 | `ALT3.ASPMX.L.GOOGLE.COM.`, `ALT4.ASPMX.L.GOOGLE.COM.` | 3600 s |
| `prompted.fi` | NS | `ns1.domainhotelli.fi.`, `ns2.domainhotelli.fi.` | 3600 s |
| `prompted.fi` | SOA | serial `2026101103` (Domainhotelli) | 3600 s |

Other types were queried and the raw DNS report redacts TXT values to avoid publishing token-like records. SPF was present, but no `_dmarc.prompted.fi` TXT answer appeared in the observed authority response; this is a mail-security follow-up **separate from marketing site launch** and must not trigger unsolicited DNS changes.

**What this proves:** authoritative current A/CNAME/MX routing and TTL can be recorded without registrar access. Existing website and mail setup are separate from `app.prompted.fi`; replacing apex/www must not overwrite app or mail records.

**What remains mandatory for cutover:** export original full Domainhotelli DNS zone/TTL including all MX, TXT, CAA, DKIM and DMARC records (not merely this subset), prove original hosting rollback path, obtain owner and privacy/image-rights approval, verify the actual protected Vercel deployment with authorised credentials, stage and test the public package on a separate destination, then change only approved marketing hosts.

**No publication or DNS modification occurred.** This snapshot is dated evidence, not an instruction to set a specific Vercel IP; Vercel's current recommended target must be checked for the project's actual domain assignment at cutover.
