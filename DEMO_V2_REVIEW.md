# Design review — two-path Capability demo
Date: 21 Oct 2026. Status: **REVIEW / NO GO**.

Founder feedback: prior five-step product experience confused even an informed tester by mixing Literacy and Capability. Solution: separate the marketing propositions and give buyers and participants different entry experiences for **Capability only**.

**Acceptance scenarios**
1. Within 10 seconds a buyer understands there are two viewpoints and can select the buyer path without filling a form.
2. Buyer sees what is being delivered before any sample report; sample group numbers are visibly fictional.
3. Participant sees a work task and changes the coaching response by selecting a different need; the demo explicitly discloses that it is deterministic.
4. Both views allow switching and return to the initial choice.
5. Optional impact calculator does not interrupt the main journey.
6. FI/EN nav and paths match, mobile is usable and no connection to app.prompted.fi customer data exists.

This version fixes navigation and user flow, not the open legal, image and release gates.

## Final copy and QA-source alignment — 21 Oct 2026

- Buyer entry now uses the founder's explicit FI choice **“Haluan kokeilla tilaajana.”**
- Removed the internal-facing “ENSISIJAINEN / RECOMMENDED” badge from the buyer card. Visual emphasis remains buyer-first without instructing buyers what to choose.
- Updated structural gate and offline browser-test source to target the current **two-path** implementation rather than the retired five-step funnel. The previous 130/130 result was obsolete; the current dual-path suite has since been run and passed 300/300 checks on GitHub Actions.
- Verified all 18 generated FI/EN HTML pages for headings, preview noindex, demo navigation, choice routes and local internal links via connected repository inspection. This is a static review, not live browser acceptance.
- Do not promote, merge or remove preview protections without final release review; privacy/terms remain drafts.

## Mobile navigation correction

Removed a duplicate Demo navigation link from all 18 FI/EN generated static pages. The shared build generator has the same fix, so regeneration will not bring the issue back. The prelaunch semantic gate now rejects duplicate mobile link destinations. This was source-verified but requires visual mobile verification before production sign-off.

**Release note:** Offline Chromium browser QA later passed (300/300) at five FI/EN viewport widths. No verified live HTTP/CSP, legal acceptance, or real-device sign-off. Keep Preview noindex and do not merge until these are resolved.

## First browser CI failure and remedy

The new GitHub Actions browser job detected a remaining duplicate in the EN explore mobile menu. The fix is now in the shared generator and in **all 18 generated pages**, including EN explore. Also harmonised English choice labels with the FI 'I want to try...' intent. Added mobile-nav click, Escape-key, responsive overflow and exact FI/EN buyer/participant copy tests to CI. The original CI #1 correctly FAILED and did not execute Playwright after the semantic error. CI #2 then completed successfully, including 300 browser assertions.

## Verified automated QA — 21 Oct 2026

- Baseline application SHA: `ff014e29971bf524581e1a919dc9f446b82b6de2`.
- GitHub Actions run [39672586383](https://github.com/jajja3890/prompted-site/actions/runs/39672586383): **SUCCESS**.
- `tools/prelaunch_gate.py`: **PASS**, all 18 FI/EN pages, no failures.
- `tools/buyer_experience_qa.py`: **PASS**, **300 assertions, zero failures**, offline Chromium, both languages at 320/390/768/1024/1440px.
- Tested: opening/switching/exiting both Capability paths, fictional Data tabs, optional calculator, coaching choices, mobile menu open/Escape, no horizontal overflow, no page errors or external requests.
- This evidence supports the **automated functional gate only**. Release remains **NO GO** pending manual visual/real-device review, rights verification and FI/EN legal/privacy acceptance, live protected-preview HTTP/CSP testing and an explicit production plan. Preview remains private with noindex.
