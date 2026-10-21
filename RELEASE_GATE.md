# Go / No-Go — prompted.fi domain cutover

**Owner:** Prompted Oy. **Status:** NO-GO until all items below are verified.

- [ ] Archive the current live prompted.fi URLs and redirects before replacement. The new website is independent of the historical Lovable workspace; no transfer or permission from the old workspace is required under the owner-confirmed source provenance.
- [ ] Verify personal founder link jarkkosjoman.com resolves as intended (not independently reachable in this audit).
- [ ] Open and accept the FI/EN preview on both phone and desktop, including all pages, links and language switch.
- [ ] Verify `jarkko@prompted.fi` mailbox sending and receiving.
- [ ] Check exact approved commercial scope and any price reference. Content currently avoids hard commitments.
- [ ] Confirm privacy statement, technical hosting processors, retention and rights. No copied VA Oy service terms.
- [ ] Visually approve the two created art-direction images as illustrations, not photographs or customer evidence. Provenance is owner-confirmed; no third-party handoff is assumed.
- [ ] Configure verified route redirects from old URLs to new (`/fi/`, `/en/`, etc.) so search engines and links are preserved.
- [ ] Remove preview noindex and allow indexing only in a reviewed production release; generate sitemap and check hreflang/canonicals.
- [ ] Verify Prompted's Vercel `prompted-site` is connected to the right GitHub repo and team's subscription; do NOT use Vercel Hobby for commercial work.
- [ ] Take a DNS snapshot in Domainhotelli (current nameservers ns1/ns2.domainhotelli.fi), note TTLs, and prepare a rollback to the current origin.
- [ ] Attach domain to the right **website** project, never the separate `prompted` app project (app.prompted.fi), then update DNS and verify TLS + FI/EN canonical pages.
- [ ] Keep old site accessible until new origin passes domain smoke test.

This is a reversible replacement, not an invasive workspace transfer. Leave all unrelated historical workspaces and projects untouched. User confirms ownership/control of the domain and all newly created site components; the remaining gate is operational access and technical portability, not a rights clearance request.

## SEO / GEO release addendum — 21 Oct 2026

- [ ] Run `python3 tools/audit_discoverability.py` on the exact RC4 source before pushing a preview.
- [ ] Review `SEO_GEO_AUDIT_2026-10-21.md` and approve new Literacy/Transformation copy, founder information and official links.
- [ ] Confirm production has no `X-Robots-Tag: noindex` header; test HTTP behavior and actual redirects after deploy.
- [ ] Verify Search Console, Bing Webmaster Tools and eligible search-bot access **after** domain cutover.
- [ ] Decide whether training bots such as GPTBot should have the same permissions as search bots; the two purposes are separate.
