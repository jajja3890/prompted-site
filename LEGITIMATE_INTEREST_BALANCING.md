# Prompted Oy — legitimate interests assessment, marketing website only

**Assessment prepared:** 22 October 2026 · **Evidence and balancing updated:** 26 October 2026 · **Assessment author:** ChatGPT supporting Prompted Oy · **Business owner and responsible reviewer:** Jarkko Sjöman · **Formal controller adoption:** PENDING (not silently assumed).

**Scope:** the future *public* static FI/EN `prompted.fi` website, ordinary **inbound** business enquiries about its services, and technically necessary service/security processing for this host. The authenticated customer application at `app.prompted.fi`, customer coaching/evidence, HR records, external lead databases, cold prospecting, campaign emails, and the unrelated Tekoälymörkö site are expressly OUT OF SCOPE.

This document is a structured **Article 6(1)(f) balancing assessment for controller decision**, not a legal opinion or an external legal-review certificate. The company's **adopted monthly manual review of closed marketing enquiries** is a separate confirmed operating decision; it did **not** imply consent to the balancing assessment or website launch.

## Decision test

For EACH purpose the controller must document three cumulative conditions, based on the real processing: **(1) a lawful, specific, real and present interest; (2) necessity, with less intrusive options considered; (3) a balance in which the person's rights and freedoms do not override the interest**. Use GDPR Articles 5, 6(1)(f), 13 and 21 and the EDPB Guidelines 1/2024 **public consultation Version 1.0** (not incorrectly presented as a final binding rule). This test is purpose-specific, not a generic declaration that all B2B processing is permitted.

## A. Voluntary inbound business enquiry and requested proposal

| Test or safeguard | Concrete finding |
| --- | --- |
| Purpose and controller interest | Answer a person who contacts Prompted Oy voluntarily about Literacy, Capability or Transformation; correspond about that *requested* enquiry and prepare a requested proposal. Commercially genuine, specified business interest, rather than speculative profiling. |
| Data categories | Necessary sender name/contact address, message, optional organisation and role, limited subsequent replies. Other personal/special-category data are **not requested**, and unrelated unsolicited sensitive material is treated separately. |
| Necessity and alternatives | A reply channel and adequate context are necessary for meaningful asynchronous answers; the same purpose cannot be achieved equally well without any way to reply. No website form, newsletter subscription, third-party enrichment or on-site account is required. Visitors can browse the site and use the fictional demo **without identifying themselves**. |
| Individual's reasonable expectations | A person who initiates a question at a business email address expects a relevant response, perhaps limited requested follow-up. They do **not** thereby expect added newsletter subscriptions, resale of contact data, profiling, indefinite generic campaigns or undisclosed sharing. |
| Potential impact and aggravating cases | Ordinary professional contact details typically create limited impacts, but unwanted follow-ups, accidental private/sensitive attachments, response to a shared mailbox, retained messages, provider access or transfer outside the EEA can cause harm. A minor, vulnerable person or an unexpected health/financial disclosure materially changes the analysis. |
| Technical and operational safeguards | Named owner **Jarkko Sjöman**, connected `jarkko@prompted.fi` mailbox, accepted Workspace CDPA **26 Oct**, separate manual Gmail labels for rights requests and website enquiries, **monthly review adopted 26 Oct** for closed website enquiries, and no blanket retention deadline or automatic deletion claim. Actual monthly operation/absence handling still requires evidence. Review access, identity and legal obligations on a case-by-case basis. |
| Individual rights | Enable access, erasure, objection, correction and restriction where applicable. Do not continue optional promotion if a person objects. Specific direct marketing is not justified automatically by this incoming-enquiry assessment; a future marketing programme needs its own GDPR/ePrivacy analysis. |
| Outcome of all three steps | **Provisionally favourable, strictly for proportionate responses to incoming enquiries** with the above safeguards and final controller confirmation. Residual risk is assessed as **low to moderate** for ordinary business correspondence and potentially higher for unsolicited sensitive content or unrelated promotional use (not covered). No inference that every historic message in Gmail is a website enquiry. |

**Alternative legal basis warning:** Article 6(1)(b) applies only where an individual requests steps toward a contract with **that individual** and processing is necessary for those steps. A representative negotiating their employer's B2B contract is not automatically an Article 6(1)(b) case; 6(1)(f) may be more appropriate.

## B. Web delivery, technical request processing and necessary security logs

| Test or safeguard | Concrete finding |
| --- | --- |
| Purpose and controller interest | Deliver FI/EN website content, prevent abuse, troubleshoot failures and maintain service/security availability. Legitimate present interest in a functioning, protected public website. |
| Data categories | Hosting/network infrastructure may see IP address, timestamp, URL/path requested, browser/device indicators, security event and error records. Technical platform processing may happen even without any visitor tracking script. |
| Necessity and less intrusive options | Basic request transmission (including necessary IP routing) and proportionate infrastructure security processing are needed to serve an ordinary website securely. A less intrusive static site was chosen: **no marketing analytics SDK, profiling, email-form backend or remote demo API** in the reviewed build. Do not add custom visitor ID or comprehensive page-view history by default. Review whether any logs can be minimised or shorter-lived in the real supplier configuration. |
| Reasonable expectations and risks | Visitors can reasonably expect brief technical delivery and abuse prevention. They do not expect behavioural advertising, shadow analytics or indiscriminate long-term records. IP/location inferences, unexpected international transfers and broad staff/provider access raise the privacy impact. |
| Directly verified operational evidence | Vercel project `prompted-site` is **preview-only, not attached to public `prompted.fi`**, and remains SSO-protected; live inspection on 26 Oct found **zero project connectors, project environment variables or team/project log Drains**. Protected-preview page sampling had no application `Set-Cookie`; local browser QA did not find custom analytics. These do not prove absence of Vercel edge/security logs or SSO cookies. |
| Provider legal context | Founder confirmed **Vercel Pro active since 12 Oct 2026**. Vercel's published DPA applies to defined Pro processing and contains subprocessor and international transfer safeguards, subject to its stated terms; the public DPA distinguishes Vercel's controller functions for certain service-generated data. The hosting provider may also independently determine handling of some platform/service data. |
| Retention and less intrusive logging | Official Vercel documentation lists Pro's ordinary runtime-log UI retention as **one day**, or **30 days with Observability Plus** where enabled. The add-on state is unknown; neither figure is an established deletion deadline for *all* CDN, edge, WAF, audit, backup or account logs. Public FI/EN wording therefore gives criteria, not a blanket promise. |
| Balancing and residual impact | **Provisionally favourable for necessary, proportionate website delivery and security**, with no custom tracking, limited site functionality and no log drains. Residual **low to moderate** risk is confined to the described minimum. **Not assessed or permitted here:** new identifying analytics, ad pixels, cross-site tracking, durable personal traffic history, expanded platform logging, or a materially different production setup. |
| Evidence still required | Final company review of the actual Vercel service/processors and applicable transfer arrangements; Observability Plus only if it would materially affect specific public claims. Verify public-origin requests and storage at staged cutover **before indexing or external launch**. Reassess if production injects extra scripts, non-essential device technologies, or unexpected processing. |

**Controller-role nuance:** Not every technical platform event necessarily falls under Prompted's processor instructions; some Vercel service data can be controlled by Vercel itself. The Article 6(1)(f) conclusion here concerns the **Prompted-determined necessary website purpose** in the actual service architecture, not a statement that Prompted is the controller of every record the Vercel service independently collects.

## C. Consequences for the FI/EN notices

- Both notices in `content.json` and tracked `fi/tietosuoja/index.html` / `en/privacy/index.html` list Prompted Oy, email contact, limited B2B purpose, technical security purpose, Article 6(1)(f), possible Article 6(1)(b), vendors, transfer framework, actual retention criteria, and data-subject rights. Content audit: `PRIVACY_FI_EN_CONTENT_REVIEW_2026-10-26.md`.
- The owner expressly **adopted a manual monthly review of closed website-related marketing enquiries on 26 Oct**; both notices state this as policy, not automatic deletion. Actual first review will be after the site is live and suitable enquiries exist.
- These notices must not claim that cookies never exist, that all service logs expire in one day, that data are exclusively EU-resident, or that the illustrative demo contains real customer outcomes.
- A newsletter, lead-enrichment integration, Meta/LinkedIn Pixel, identifiable analytics, forms, mass outreach or personalisation would require **new factual and legal review before enabling**; the current limited balancing conclusion would not cover them.
- The current website **terms** are distinct from `app.prompted.fi` and the products' contracts; the marketing site itself takes no orders or payments.

## D. Mitigations, decisions and evidence status

| Control | Status at 26 Oct |
| --- | --- |
| Controller identity and legal contact | Company publicly corroborated; Gmail mailbox and responsible owner verified |
| Gmail service provider CDPA | Accepted 26 Oct by owner's Admin Console screenshot |
| Manual monthly review of closed new-site enquiries | **Adopted 26 Oct** by owner; first real operating review has not occurred |
| Recognition of rights requests | Written SOP and separate Gmail triage label; no automated filter, additional drill or substitute person yet |
| Third-party analytics and custom profiling | Absent in reviewed source/preview; actual public domain still to test |
| Vercel team/project external drains and connectors | **Zero in connected API**, 26 Oct |
| Vercel Pro and standard DPA scope | Pro owner-confirmed; publicly stated standard Pro DPA applicability reviewed |
| Individual log categories, transfer details and Observability Plus | Not fully observed; no universal time-based promise made |
| Company adoption of **this** balancing assessment | **PENDING — explicit approval not yet given** |
| Entire FI/EN notice owner approval | **PENDING** |
| Public release authorisation | **PENDING**; separate seven-gate release control remains fail-closed |

## E. Ready-for-decision outcome (NOT an inferred signature)

**Proposed decision for Prompted Oy:** For the **two tightly defined processing purposes A and B only**, Article 6(1)(f) is a supportable lawful basis *if* the documented activity and safeguards match actual operations and no material new processing is added. Adoption requires the owner to confirm the described real purposes, safeguards and residual risks, and accept responsibility for handling rights requests and maintaining the adopted monthly review policy. Until this explicit decision, treat the outcome as **provisionally favourable / awaiting adoption**, not a binding sign-off.

**Sign-off:** Approver: **not yet signed** · Decision date: **pending** · Scope: Prompted marketing website only · External legal opinion: **not obtained** · Approval evidence: **pending**.

Do **not** change `privacy_legal` in `PUBLIC_RELEASE_APPROVALS.json` to approved on the strength of this draft alone. Likewise do not change `owner_release`, publish, merge or touch DNS or `app.prompted.fi`.

## Sources

- GDPR [Articles 5, 6(1)(f), 13 and 21](https://eur-lex.europa.eu/eli/reg/2016/679/oj).
- [EDPB SME: processing personal data lawfully](https://www.edpb.europa.eu/sme/be-compliant/process-personal-data-lawfully_en).
- [EDPB Guidelines 1/2024 on 6(1)(f), public consultation version](https://www.edpb.europa.eu/public-consultations/guidelines-12024-on-processing-of-personal-data-based-on-article-61f-gdpr_en).
- [European Commission: legal grounds for processing](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/legal-grounds-processing-data_en).
- [European Commission: rights and objection handling](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/dealing-requests-individuals_en).
- [Vercel Data Processing Addendum](https://vercel.com/legal/dpa); see also `VERCEL_PRIVACY_VERIFICATION_2026-10-26.md`.
