# Prompted Oy — privacy-request continuity and monthly review monitoring

**Date:** 26 October 2026. **Responsible human:** Jarkko Sjöman. **Operational status: assisted monitoring CONFIGURED, first scheduled run and absence recovery NOT VERIFIED.**

## What is now configured

The founder's connected Gmail address is `jarkko@prompted.fi`. A ChatGPT conditional scheduled check named **Promptedin tietosuojapyyntövalvonta** was created and is **enabled**, first planned for **27 October 2026, 08:00 Europe/Helsinki**, daily thereafter. It searches for potential new and unanswered data-subject rights requests (even when the wording does not contain “GDPR”) and notifies the founder if something reasonably actionable is found. Notification is minimal, avoiding unnecessary reproduction of personal messages. The task does **not** reply, delete, reclassify or grant rights automatically.

The same daily task was updated to produce the adopted **once-per-calendar-month manual marketing-enquiry review reminder on the first day of the month**. The standalone monthly task was **not created**, because the user's plan reported a maximum of five scheduled tasks; no other existing tasks were disabled or replaced. If there are no eligible new website-specific cases, a zero-case result is appropriate. This does not extend the policy to unrelated historical inbox records.

## Important limits and remaining prelaunch work

- No scheduled check has yet run or been observed to succeed; the task's first planned iteration is 27 October. We cannot represent an enabled schedule as evidence of successful Gmail analysis, notification delivery or actual user action.
- Daily checks are **not** real-time guarantees, a formal backup person, uninterrupted account access, or an SLA that ensures Article 12's one-month rights-response deadline. A disconnected connector, disabled task, empty subject search, OAuth expiry, outages or notifications not seen by the founder can interrupt coverage.
- The company owner must ensure they can receive alerts while away or designate a trustworthy stand-in with access/secure response procedures. A general public inbox acknowledgment is **not** a substitute for the human rights determination. The connected Gmail connector does not expose Gmail vacation-reply, forwarding-filter or Workspace delegation settings; none were silently changed.
- Preserve a private rights-request log with receipt, scope, identity verification only if reasonably needed, due date, action, reply date, and outcome. Do not publish client correspondence or contact details into public GitHub.
- Check a genuine scheduled run and delivery, verify recovery/contact procedure for periods when the owner has no access, then record evidence before updating `rights_request_absence_continuity` to `verified` in the release manifest. It is **pending** as of 26 October.

**Source:** owner-confirmed privacy handling duty and approved monthly review; connected Gmail profile; confirmed successful creation/update of the enabled automation, 26 October 2026. No mail was sent, deleted, changed or exposed by creating this note.
