# Prompted.fi — SEO & GEO prepublication audit

**Date:** 2026-10-21  
**Release:** v1.0.0-rc4 — OWNED, PREVIEW-ONLY  
**Owner:** Prompted Oy  
**Publishing status:** **NO-GO** until the release gates are approved. No remote production change has been made.

## Executive verdict

The static FI/EN implementation is a strong technical starting point for traditional search engines and AI-powered discovery: meaningful content is present in the initial HTML, there is no JavaScript dependence for primary text, and URLs are stable and language-specific. However, technical eligibility is only a prerequisite; no bot, search engine or model is guaranteed to index, rank or cite the pages.

## What was audited and corrected

| Dimension | v1.0-rc1 finding | v1.0-rc4 work | Residual risk |
|---|---|---|---|
| Discoverability | `robots.txt` disallowed all bots while HTML said `noindex` | Preview now exposes `noindex` in HTML and `X-Robots-Tag`; robots permits reading it. Production build permits crawling and generates an XML sitemap | Preview should also have Vercel Deployment Protection. Real production headers must be smoke-tested |
| Commercial search intent | Only Capability had its own page | New FI/EN pages for Literacy and Transformation, both with clear buyer language and visible real questions | No verified search-demand data yet |
| Titles and descriptions | Generic and partly brand-only | Unique descriptive SEO titles and meta descriptions | SERP rewriting by engines is normal |
| Semantic entities | No structured organization/service graph | JSON-LD `Organization`, `WebSite`, `WebPage`; `Service` on service pages; `BreadcrumbList` | Validate against live structured-data tools after deploy; rich results not guaranteed |
| International | FI/EN canonical + alternates already present | Tested exact reciprocal `hreflang` pairs; `x-default` added to home | Verify final server slash redirects, response codes, canonical domain |
| Site map | Generated only at production; missing freshness value | 16 canonical URLs plus manually controlled truthful `lastmod` | Update `LAST_MEANINGFUL_UPDATE` only on material revisions; submit after launch |
| AI-search technical access | No specific search-crawler policy | Production `robots.txt` explicitly allows `OAI-SearchBot`; generic access allows major search crawlers | CDN, WAF and authentication may still block verified bots |
| Authority | Company information sparse | Visible founder, responsible organisation, official EU AI Act Article 4 link and clear limits of claims | Founder text and legal details need owner review. No unverified customers/case studies |
| Content | Offer described in broad terms | Concrete answers: who, why, workflow, boundaries, FAQ on new services | Need client-approved evidence and original methodology examples over time |
| Page quality | HTML, CSS, WebP image assets | Retained lightweight HTML delivery and two existing curated images | Core Web Vitals, mobile interaction and accessibility need browser/field verification |

## Verification performed

`python3 tools/audit_discoverability.py` reports **PASS: 2,139 assertions** across prelaunch and a separately generated production build. Each build has **16 FI/EN pages** (8 page types per language). Checks cover files, local links, one H1, metadata, absolute canonical URLs, reciprocal alternates, JSON-LD parseability and graph types, local asset existence, source reference, prelaunch indexing blocks, production robots/index flags and sitemap URLs/lastmod. The script runs the production build in a temporary directory: it does **not** publish it.

This is not a substitute for Lighthouse/Core Web Vitals testing, HTTP-level checks on Vercel, Rich Results Test, Search Console URL Inspection, Bing Webmaster checks, or actual crawler visits.

## AI discovery: practical operating model

1. **Search inclusion:** Make public content crawlable and indexable, with a high-quality, visible text answer on each meaningful URL. For ChatGPT search, allow `OAI-SearchBot`; for Google AI features, meet normal Search technical/indexing requirements. Indexing, ranking and inclusion are never guaranteed.
2. **AI training is separate:** `GPTBot` controls OpenAI model-training crawling independently of `OAI-SearchBot`. Make an explicit publisher policy decision if restricting training is important. Current general `Allow: /` does not restrict training crawlers.
3. **Do not buy GEO tricks:** Google says special `llms.txt` files, compulsory FAQ schema and content 'chunking' are not needed for Google's AI search features. Keep one authentic, readable source of truth.
4. **Get cited for original knowledge:** Publish 2–3 evidence-backed, consented and attributable examples of changed real work when customer evidence exists. Never manufacture logos, impact numbers, citations, testimonials or certificates.
5. **Connect external identity:** Use verified company and founder profiles, legitimate partner and event pages, and relevant business directories that describe what Prompted actually does. Add `sameAs` only after profiles are checked to represent the same organisation.

## Priority checklist before switching `prompted.fi`

**P0 — release blocking**

- [ ] Owner reviews and confirms FI/EN copy and scope for Literacy, Capability and Transformation. Do not treat the pages as independent promises of new operational readiness.
- [ ] Confirm `jarkko@prompted.fi` accepts and delivers messages.
- [ ] Approve privacy statement and service-terms wording against actual data processing, processors, hosting, legal obligations and contract model.
- [ ] Verify rights, artifacts and visual appropriateness of H01 and H05 generated images.
- [ ] Inspect Vercel preview on a real phone and desktop, including headings, overlays, menus, focus, reduced motion and image composition. Run Lighthouse and/or PageSpeed tests.
- [ ] Validate HTTP redirects from the existing indexed routes (`/fi`, `/en`, `/en/terms`, current legal URLs) to the new canonical paths, preserving old backlinks. Redirects must not loop.
- [ ] Confirm the new website has its own Vercel project and preview branch protections, separate from `app.prompted.fi`. Capture current DNS and rollback targets.
- [ ] Only after approvals: build approved-production, inspect for no leftover `noindex` in response header or page HTML, then switch the domain.

**P1 — immediately following production**

- [ ] Verify Google Search Console ownership (domain property), submit `https://prompted.fi/sitemap.xml`, inspect `/fi/`, `/en/`, `/fi/literacy/`, `/en/capability/` and old redirected URLs.
- [ ] Verify Bing Webmaster Tools, submit the same sitemap; consider IndexNow for future content updates once the site's public endpoint and ownership are confirmed.
- [ ] Crawl production as non-logged-in Googlebot/Bingbot/OAI-SearchBot and confirm HTTP 200/3xx, accessible HTML, no WAF/CDN bot blocks and responsive mobile content.
- [ ] Inspect structured data against the rendered live site; test Open Graph previews and link unfurling.
- [ ] Monitor impressions, click-throughs, index coverage, branded/nonbranded queries and qualified enquiries. Prefer actual Search Console/Bing metrics to artificial GEO visibility scores.

**P2 — content strength over the next 1–3 months**

- [ ] Add verified, with-permission customer case studies as evidence becomes available. Describe the task, baseline, changed practice and what the evidence can/cannot prove.
- [ ] Publish 1–2 authored, genuinely useful explainers (not mass-produced generic AI tips) addressing live buyer questions and linking to official primary sources where useful.
- [ ] Add verified third-party company/partner references, founder identity profiles and real buyer testimonials; then link relevant confirmed profiles with `sameAs`.
- [ ] Review discovery in AI responses as an *observed* metric rather than a promised ranking outcome. Keep a record of the questions and systems tested.

## Independent primary guidance reviewed (21 Oct 2026)

- [Google: Optimizing your website for generative AI features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- [Google: Organization structured data](https://developers.google.com/search/docs/appearance/structured-data/organization)
- [Google: Multi-language and hreflang](https://developers.google.com/search/docs/specialty/international/localized-versions)
- [Google: noindex is invisible if robots blocks crawling](https://developers.google.com/search/docs/crawling-indexing/block-indexing)
- [OpenAI: OAI-SearchBot vs GPTBot](https://developers.openai.com/api/docs/bots)
- [Bing: URL submission, IndexNow](https://www.bing.com/webmasters/help/URL-Submission-62f2860b)
- [European Commission: AI Act Article 4](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-4)

**Not audited:** actual site-index coverage, live Vercel HTTP behavior, Search Console/Bing configuration, authenticated analytics, DNS cutover, final legal correctness, final image licensing approval and real-user performance. Those require a real deployment and/or owner approval.
