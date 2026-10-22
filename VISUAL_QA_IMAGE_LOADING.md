# Accurate visual review — late-loaded artwork

Updated 22 October 2026.

**Issue:** previous full-page Chromium screenshots could capture the page while the below-fold `loading="lazy"` H01 editorial image had not been requested/decoded. The image area appeared as a blank dark field even though separate local served-HTTP tests successfully scrolled and decoded the asset. This was a **screenshot test blind spot**, not proof that the actual site fails to render the image during normal scrolling.

**Fixed in visual QA:** the browser now scrolls every lazy image into the viewport, awaits `HTMLImageElement.decode()` and verifies natural dimensions before returning to the top and taking the same 32 full-page screenshots. A decoding failure fails the job. The artifacts now represent image-visible scroll states, not blank unloaded placeholders.

**What this does not prove:** final artistic acceptance, image provenance/license, real Vercel protected HTTP, handset performance, screen-reader certification, or public production eligibility. H01 remains a visual candidate and the site remains draft until released.
