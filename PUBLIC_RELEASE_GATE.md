# Public site release-pack builder — fail closed

This **does not publish**. The existing Vercel preview and `prompted.fi` domain are unchanged. The public bundle generator lives in `tools/public_release_gate.py`. The current tracked `PUBLIC_RELEASE_APPROVALS.example.json` intentionally has *all approvals pending*.

## How the gate works

- GitHub Actions calls `python tools/public_release_gate.py --check`. It emits a `BLOCKED` report until legally and operationally approved, but the normal Preview CI can still pass. **CI success does not mean launch approval.**
- For actual release preparation, a reviewer creates an evidence-filled copy of the approval manifest, specifying a dated approver and verifiable evidence for each gate: legal, image rights, commercial copy, protected-preview HTTP, real-device visual review, DNS rollback and explicit owner sign-off.
- The preparer checks all seven approvals, refuses unresolved privacy placeholders in either language and verifies preview safeguards before assembling a **private output folder**. No code runs a Vercel deploy or modifies DNS. It requires the intended Git commit SHA explicitly.
- A future approved release bundle can contain only 18 FI/EN static pages and the reviewed necessary assets. It removes preview noindex/draft banners **only in the isolated output**, creates `robots.txt` and `sitemap.xml`, and preserves security headers. It excludes unused `hero-material.webp`, unapproved `wordmark-light.svg`, Python source files, build logs, draft approval records and tests.
- The current FI/EN privacy text still describes an **unimplemented proposed 12-month retention policy**. The release tool explicitly blocks the phrases `suunniteltu säilytyskäytäntö` and `our proposed retention practice`, as well as other legal placeholders. The deletion or review process must actually be implemented, verified and truthfully described in both languages. An approved JSON file alone cannot unlock packaging.
- The release output must be revalidated as an independent website on a **separate protected/staged production preview** before assigning `prompted.fi` and indexability. The builder is not a legal or rights attestation; its manifest records the responsible decisions.

## Last-mile tasks

1. Verify existing `prompted.fi/en/terms` live terms, as the indexed copy still mentions another business.
2. Confirm hosting and email retention/transfer facts, then finalize FI/EN legal content and review it.
3. Obtain rights evidence for H01, OG image and logo.
4. Fix Vercel connection scope to read protected preview response; review actual HTTP/CSP and physical devices.
5. Save DNS apex/www/TTL rollback snapshot at Domainhotelli and explicit permission for public site cutover.
6. Approve **exact revision** and stage the production bundle without assigning apex domain. Never touch `app.prompted.fi`.

**Current decision:** NO GO. The released customer application is excluded from this site release.

## Packaging regression QA

A dedicated CI step now runs `python tools/public_release_packaging_qa.py`. It verifies that the **actual public-release guard remains BLOCKED** on the unapproved project, including explicit FI/EN enforcement against calling an unimplemented twelve-month mailbox policy completed. It also calls the isolated bundling function in a throwaway temporary directory to validate that a **future approved** package would have 18 pages, local image/style assets, 18 sitemap URLs, correct public robots and preserved security headers, with preview draft markers removed. The temporary output is deleted automatically; this never publishes, uploads, authorises, merges or changes DNS. An approved manifest is still mandatory for the real CLI `--prepare` route.
