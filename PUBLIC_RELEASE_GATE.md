# Public site release-pack builder — fail closed

This **does not publish**. The existing Vercel preview and `prompted.fi` domain are unchanged. The public bundle generator lives in `tools/public_release_gate.py`. The tracked `PUBLIC_RELEASE_APPROVALS.example.json` remains an all-pending template. The active tracked `PUBLIC_RELEASE_APPROVALS.json` records an owner-attested **image_rights: approved** for five exact asset blobs. The other six gates, including `owner_release`, remain pending.

## How the gate works

- GitHub Actions calls `python tools/public_release_gate.py --check` against the active `PUBLIC_RELEASE_APPROVALS.json`. It emits a `BLOCKED` report until legally and operationally approved, but the normal Preview CI can still pass. **CI success does not mean launch approval.**
- For actual release preparation, the active approval manifest must be completed with a dated approver and verifiable evidence for each gate: legal, image rights, commercial copy, protected-preview HTTP, real-device visual review, DNS rollback and explicit owner sign-off. The image-rights record is already present, with hashes verified at release-check time; unapproved records must not be automatically inferred from CI success.
- The owner-release record additionally requires `approved_commit_sha`, **exactly matching the checked-out 40-character Git HEAD SHA**; a future change after sign-off invalidates approval. Save the owner sign-off in a separate evidence manifest; never add sensitive authorization tokens or private legal evidence to this public repository.
- The preparer checks all seven approvals, refuses unresolved privacy placeholders in either language and verifies preview safeguards before assembling a **private output folder**. No code runs a Vercel deploy or modifies DNS. It requires the intended Git commit SHA explicitly.
- A future approved release bundle can contain only 18 FI/EN static pages and the reviewed necessary assets. It removes preview noindex/draft banners **only in the isolated output**, creates `robots.txt` and `sitemap.xml`, and preserves security headers. It excludes unused `hero-material.webp`, unapproved `wordmark-light.svg`, Python source files, build logs, draft approval records and tests.
- The FI/EN privacy wording now describes retention *criteria* instead of an unimplemented 12-month deletion promise. The actual email review/retention process still requires operational evidence and explicit `privacy_legal` approval. The release tool still rejects any future `suunniteltu säilytyskäytäntö` / `our proposed retention practice` placeholders and always checks all seven release approvals; no draft automatically becomes public.
- The release output must be revalidated as an independent website on a **separate protected/staged production preview** before assigning `prompted.fi` and indexability. The builder is not a legal or rights attestation; its manifest records the responsible decisions.

## Last-mile tasks

1. Recheck the current `prompted.fi` public site's *rendered* legal routes during cutover; the 26 October read-only HTTP source audit served a generic SPA shell and did not establish which legal text a visitor sees after JavaScript execution.
2. Confirm hosting and email retention/transfer facts, then finalize FI/EN legal content and review it.
3. Image-rights owner attestation is recorded for H01, OG image, logo and brand derivatives, with immutable blob IDs in `PUBLIC_RELEASE_APPROVALS.json`; preserve final social/device visual review as a separate gate.
4. Vercel connection and protected preview HTTP/CSP checks now work; remaining checks include the real physical devices and final public-site browser and security inspection.
5. Save DNS apex/www/TTL rollback snapshot at Domainhotelli and explicit permission for public site cutover.
6. Approve **exact revision** and stage the production bundle without assigning apex domain. Never touch `app.prompted.fi`.

**Current decision (26 October 2026): NO GO.** Image rights approved on owner attestation for pinned files; other six sign-offs pending. The released customer application is excluded from this site release.

## Packaging regression QA

A dedicated CI step now runs `python tools/public_release_packaging_qa.py`. It verifies that the **actual public-release guard remains BLOCKED** on the unapproved project, including explicit FI/EN enforcement against calling an unimplemented twelve-month mailbox policy completed. It also calls the isolated bundling function in a throwaway temporary directory to validate that a **future approved** package would have 18 pages, local image/style assets, 18 sitemap URLs, correct public robots and preserved security headers, with preview draft markers removed. The temporary output is deleted automatically; this never publishes, uploads, authorises, merges or changes DNS. An approved manifest is still mandatory for the real CLI `--prepare` route.
