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
- Updated structural gate and offline browser-test source to target the current **two-path** implementation rather than the retired five-step funnel. The previous browser result file is marked pending retest, not misrepresented as a fresh test.
- Verified all 18 generated FI/EN HTML pages for headings, preview noindex, demo navigation, choice routes and local internal links via connected repository inspection. This is a static review, not live browser acceptance.
- Do not promote, merge or remove preview protections without final release review; privacy/terms remain drafts.

## Mobile navigation correction

Removed a duplicate Demo navigation link from all 18 FI/EN generated static pages. The shared build generator has the same fix, so regeneration will not bring the issue back. The prelaunch semantic gate now rejects duplicate mobile link destinations. This was source-verified but requires visual mobile verification before production sign-off.

**Release note:** Browser QA is still pending after the dual-path conversion; no verified live HTTP/CSP, legal acceptance, or real-mobile sign-off. Keep Preview noindex and do not merge until these are resolved.
