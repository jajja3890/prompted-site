# Prompted Website — Capability demo v2 (DESIGN REVIEW ONLY)

**Do not merge to main, promote, change DNS or remove noindex without explicit owner approval.**

## What is here
A standalone FI/EN Prompted marketing site with 18 pages and three separate commercial offerings: **Literacy**, **Capability**, **Transformation**. The primary **Demo** navigation item demonstrates **Capability only**.

- `/fi/tutustu/`, `/en/explore/`: two clear paths on **one** service.
- **Buyer/sponsor is first**: see the indicative organisation pilot, sample restricted group-level Data and optionally an assumption-based impact calculation.
- **Participant is second**: explore one real-work task, choose where help is needed and see a different deterministic next coaching step, plus the Evidence progression.
- Each path can switch to the other without a five-screen wizard.
- All sample metrics are **fictional**, all calculations illustrative. The demo is **not** a screenshot of an authenticated product or a live LLM.
- No form, email requirement, analytics, cookies, external fonts, remote demo API or private app/Supabase connection.

## Maintain the site
Edit commercial/utility copy in `content.json`, the product-first pages in `templates/`, and the demo HTML in `buyer_experience.py`. Styling: `assets/product-first.css`, `assets/product-system.css`, `assets/buyer-experience.css`. Interaction: `assets/buyer-experience.js`.

Rebuild static pages with `python3 build.py` (requires `beautifulsoup4`, as listed in `requirements-build.txt`). Rebuild output is committed so Vercel can serve directly without Python.

## Release gate
Preview uses HTML noindex, robots.txt and Vercel X-Robots-Tag, with protected Vercel Preview enabled on the project. The public GitHub source remains public. See `QUALITY_BUYER_LED.md` and `SAFE_DEMO_DECISIONS.md` for test limitations and release blockers.
