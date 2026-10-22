# Prompted.fi — controlled marketing website cutover plan

22 October 2026 · **NOT AUTHORIZED FOR PRODUCTION** · Draft PR [#6](https://github.com/jajja3890/prompted-site/pull/6)

## What exists

- Proposed new FI/EN marketing site: `jajja3890/prompted-site`, isolated GitHub branch `feat/prompted-capability-dual-demo-direct-20261021`, Vercel project `prompted-site` (`prj_O7rI2YYJd1HTR7emNksmIalWiqe9`).
- Current preview has Vercel Authentication and `noindex`/robots/CSP protections. Preview build reports READY; connector cannot fetch protected HTTP response because deployment access was denied. **READY is not a verified browser or public-domain pass.**
- Vercel project's domain list currently contains only Vercel-hosted domains, **not `prompted.fi`**. Do not assume the new Vercel project currently controls live DNS.
- Existing public `prompted.fi/fi` and `prompted.fi/en` show Prompted content. A web search snapshot dated about two weeks prior shows `https://prompted.fi/en/terms` describing unrelated **DataDiscovery / Design VA Oy** legal terms. This MUST be live-verified and replaced or corrected, not assumed current.
- Business name, Y-tunnus `3550114-7`, and Turku match third-party company listings; mailbox operation and legal copy are **not** independently verified.
- `app.prompted.fi` is a **separate customer product**, outside this marketing cutover. Never modify its DNS, Supabase or Vercel configuration as part of the website launch.

## Current test evidence (offline, not domain acceptance)

GitHub Actions [run 39676373623](https://github.com/jajja3890/prompted-site/actions/runs/39676373623) PASS: 18/18 static pages, 300/300 demo browser assertions, reproducible build, 24 FI/EN screenshots and automated axe checks with no reported findings. Screenshots were reviewed visually from the CI archive. Real devices, screen readers, accessibility certification and live responses remain untested.

## Release gates — all required, no implied approval

1. **Copy and legal:** Confirm final FI/EN policies and terms for the **marketing site only**; verify retention, email provider, technical logs, transfer safeguards and cookie/device-storage inventory with real vendors. Replace DRAFT text only after approval.
2. **Assets:** Document H01, Open Graph image and logo/icon rights; approve final mobile and desktop crops. Remove any H01 draft label before release only if rights are confirmed.
3. **Protected preview:** Reauthorize the connected Vercel project/team if required; then verify real HTTP 200/redirects, CSP, X-Robots-Tag, static files, caching, no unintended cookies and every FI/EN route on the protected preview.
4. **Content and commerce:** Check every pricing/pilot claim, `mailto:jarkko@prompted.fi` deliverability, FI/EN language switch, outside founder link and that every Demo link demonstrates Capability alone. No implied certificates, fictitious results or customer data.
5. **Manual design/device:** Review real phone, tablet and desktop hero, button hierarchy, mobile nav, hero asset crops, readable labels and at least basic keyboard/assistive-technology behavior.
6. **Domain ownership:** Identify the **current authoritative DNS records and existing origin hosting provider**. Record exact previous values, TTL, permissions and rollback steps before changing anything. Confirm control of apex `prompted.fi`, `www` redirect and existing old URL paths. Do NOT touch `app.prompted.fi`.
7. **Publication decision:** Require explicit responsible-owner approval of release revision, written legal/asset approval, cutover window and rollback owner. PR remains draft until then.

## Preplanned cutover

- Freeze accepted source SHA and save screenshots, DNS snapshot, current response headers, old homepage and indexed legal URLs.
- Prepare a **separate production build** from the approved branch; remove only production-facing preview blocks: HTML robots noindex, `X-Robots-Tag` noindex, restrictive `robots.txt`, Preview footer, **and approved-only** legal/art draft markers. Preserve CSP/security and truthful concept disclosures.
- Add sitemap and verify `canonical`, hreflang and Open Graph on 18 paths. Preserve or explicitly redirect existing `/fi`, `/en`, `/en/terms`, `/en/privacy`, old `/capability`, `/literacy`, `/transformation`, `/transformerism` links. Do not claim redirects exist unless deployed and checked.
- Validate production-ready deployment on its **own** temporary URL before associating live domain. Attach domain only under the agreed ownership/DNS plan; never detach or rewrite customer app subdomain.
- Smoke check the live marketing domain: root to FI, both language homepages, product pages, both demo choices, privacy, terms (**Prompted Oy, not DataDiscovery**), contact links, icons/share image, CSP, robots, navigation, and redirects. Check production page source contains no draft markings.
- Record live deployment ID, final SHA, DNS changes and timestamp; then and only then enable indexing. Search-engine indexing can take time.

## Rollback

If security, legal identity, site availability, responsive rendering or broken email/links fail: stop promotion, restore **recorded** previous marketing apex/www DNS/origin routing and verified previous site deployment, or redeploy the verified last-good marketing release. Recheck `/fi`, `/en` and `/en/terms`, monitor DNS propagation and preserve the isolated `app.prompted.fi` customer app. Do not revert blindly without DNS snapshots.

## Links to check on launch

- `https://prompted.fi/`, `/fi/`, `/en/`
- `/fi/literacy/`, `/fi/capability/`, `/fi/transformation/`, `/fi/tutustu/`
- `/en/literacy/`, `/en/capability/`, `/en/transformation/`, `/en/explore/`
- `/fi/tietosuoja/`, `/fi/ehdot/`, `/en/privacy/`, `/en/terms/`
- `mailto:jarkko@prompted.fi`; login link to `https://app.prompted.fi`

## Current decision

**GO for further protected review and internal QA; NO GO for public domain cutover.**

## Verified current ownership and rollback reference — 22 October 2026

Read-only Vercel account inspection (team `team_AQMYKoxdjGdzICtKXiWElLTU`):

- `prompted.fi` is already a **verified external domain** in the connected Vercel team; DNS nameservers are `ns1.domainhotelli.fi`, `ns2.domainhotelli.fi`. Zone is external (`zone:false`), not managed here by Vercel DNS.
- Vercel domain configuration currently reports apex A address **`185.158.133.1`** (documented rollback reference; VERIFY the authoritative registrar/zone before use). Vercel recommends `76.76.21.21` or its applicable recommended CNAME; this is an **observation, not an instruction to change DNS now**.
- The only `prompted.fi` project-domain association returned by Vercel is **`app.prompted.fi`**, tied to a **different** Vercel project `prompted` (`prj_MfK5ICUXV5eD0k6VuUiy3BMgCLkU`). This is the customer application; no changes permitted in this marketing-site release.
- New marketing project `prompted-site` still has no associated `prompted.fi` project domain.
- Before DNS cutover, separately record current **www record**, TTL, exact apex A/AAAA/CNAME at Domainhotelli, existing site deployment and response snapshot. Vercel configuration alone is not a guaranteed authoritative DNS backup.
- Vercel protected-preview authenticated fetch currently returns **403 forbidden** at deployment alias access even though deployment is READY. Do not remove SSO. Reauthorize that Vercel connection/project/team and recheck real HTTP, cookies and CSP before launch.

### 22 October live-site discovery note

Public search returned the last-indexed `https://prompted.fi/en/terms` content under **DataDiscovery / Design VA Oy**. A live HTML fetch could not confirm or refute this due to the current external browser's rendering limitations. Treat as a concrete **check-required risk**, not as a verified current page defect. The next site has a CI check to prevent these third-party names on its four legal pages.
