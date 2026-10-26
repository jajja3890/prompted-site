# Vercel privacy verification — Prompted marketing site — 26 October 2026

**Scope:** Read-only inspection of the Vercel team `team_AQMYKoxdjGdzICtKXiWElLTU`, project `prompted-site` (`prj_O7rI2YYJd1HTR7emNksmIalWiqe9`) and relevant current official supplier documents. Marketing site only, **not** the separate authenticated `app.prompted.fi` service.

## Verified directly from the connected Vercel account, 26 October

| Control | Observed value | Meaning and limit |
| --- | --- | --- |
| Project environment variables | **0 listed** (non-decrypted read) | No project-specific environment variables appeared; says nothing about Vercel's platform-internal request/event processing. |
| Project connector connections | **0 listed** | No separately configured Vercel project connectors appeared. Does not rule out platform-owned technical subprocessors. |
| Team drains (and project-filtered drains) | **0 listed** | No outgoing configured observability/log drains for this team or site. Re-check if integrations or monitoring are introduced later. |
| Project production/public domain | **Not assigned**; `live=false` | `prompted.fi` is not attached to this Vercel site. Production cutover remains unapproved. |
| Protected preview | **Vercel SSO enabled** | User-authenticated preview traffic may involve SSO cookies; prior Vercel read-only preview fetch is not an ordinary browser session. |
| Project code | **Static FI/EN marketing website** | Review of the source/build and local HTTP Chromium QA previously found no marketing tracking scripts, personal-data forms, external fonts, application API calls, or localStorage writes. The public Capability walkthrough uses fictional data. |

**Vercel Pro is confirmed by the owner:** Pro was activated on 12 October 2026 and reconfirmed as active on 26 October 2026. This is an owner-confirmed subscription fact; the connected `get_team` API did not expose plan metadata. Observability Plus status and account-specific DPA execution remain unverified.

## Verified from current Vercel published documentation (not project-specific proof)

- [Vercel DPA](https://vercel.com/legal/dpa), updated **17 March 2026** / effective **31 March 2026**, Introduction and section 4: DPA processor provisions apply to **Pro and Enterprise** customers under the applicable agreement. Section 7 points to a [subprocessor list](https://security.vercel.com); section 13 and Schedule 3 contain international transfer provisions (including EU SCC modules when applicable). Vercel can separately be a controller of some service-generated or contact data; do not describe all Vercel processing as “processor on Prompted's instructions”.
- [Vercel Runtime Logs](https://vercel.com/docs/logs/runtime), last updated **28 August 2026**: typical log visibility/retention periods **Hobby 1 hour, Pro 1 day, Enterprise 3 days; with Observability Plus 30 days** for Pro/Enterprise. **These are product limits, not yet a proven project configuration and not a global promise about CDN/security, request, build, audit or backup data retention.**
- [Vercel Observability Plus](https://vercel.com/docs/observability/observability-plus) specifies 30-day retention for its add-on; its status for this team is **not verified** by the available Vercel connector.
- [Vercel Drains](https://vercel.com/docs/drains/using-drains) describes forwarding log, trace, analytics and speed insight data to configured third-party destinations. Read-only `list_drains` found none for the checked team.
- [Vercel Security & Subprocessors](https://security.vercel.com) is the current subprocessor reference referred to by the DPA. The applicable list and geography must be evaluated against the actual service setup; Vercel's general documentation is not a statement of the location of every individual request or log.

## Safe, accurate FI/EN marketing-privacy position

1. Do **not** claim “Vercel collects no personal data”. Service delivery can create IP addresses, request paths, timestamps, device/browser and security information.
2. Do **not** add a fixed retention deadline for all platform logs: the actual plan/add-ons and Vercel processing categories differ. Keep factual *retention criteria* unless fully substantiated.
3. Do **not** claim a cookie-consent banner is legally required merely because technical hosting logs exist; check actual device storage and non-essential technology on the public host. Do not assert that **all** cookies are absent based on a protected preview's application responses.
4. The site owner is Prompted Oy; website enquiries go to `jarkko@prompted.fi` (Google Workspace CDPA accepted 26 October 2026). Keep the authenticated customer application's privacy notices and agreements entirely separate.
5. The existing FI/EN drafts at `content.json` already identify Vercel and Google Workspace, possible international processing, categories, lawful purposes and factual retention criteria. No unsupported precise retention number needs to be inserted into those drafts.

## Release check status

- [x] Read-only Vercel project configuration and 0 connector connections
- [x] Read-only team and project drain lookup confirms none
- [x] Protected preview previous HTTP/CSP and local-browser no-tracking evidence
- [x] Published DPA scope, subprocessors reference and runtime-log product limits checked
- [x] Vercel Pro plan confirmed by owner (activated 12 October 2026 and reconfirmed 26 October). The published DPA covers qualifying Pro customers. **Still outstanding:** Observability Plus status and any account-specific DPA/processing conditions.
- [ ] **Review account-specific logs, processing locations/subprocessors and any relevant settings**; do not conflate runtime event retention with CDN, firewall, service-generated or backup records
- [ ] Owner/company reviews the exact FI/EN privacy notice and legitimate-interest balancing statement against confirmed actual practices
- [ ] Verify ordinary, unauthenticated public-domain cookies/headers and scripts on the intended public deployment before enabling indexing

These controls inform `privacy_legal` but **do not approve that gate**. All publishing/merging, DNS, `noindex` and authenticated-app safeguards remain untouched.
