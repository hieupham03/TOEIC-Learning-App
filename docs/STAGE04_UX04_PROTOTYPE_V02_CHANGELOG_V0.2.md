# Stage04 UX04 — Focused Prototype V0.1 → V0.2 Change Log

**Status:** Analyst revision completed; candidate, **NOT** approved final UI.  
**Supersedes for review:** 26-page PDF V0.1; retained unchanged for historical comparison.  
**Current candidate:** 31-page clickable PDF V0.2. Original sample English sentences are authored specifically for this prototype, not sourced from Full Mock content.

| Issue | V0.2 candidate change | What is **NOT** proven |
|---|---|---|
| I01 Reading scroll/anchor | Dedicated passage P7-177 semantic anchor; return-to-context, return-to-question actions | Real Android scroll restoration, system Back and font reflow |
| I02 Save truthfulness | Separate PENDING, ACK-CONFIRMED, ACK-UNKNOWN, safe retry branches and standalone terminology screen | Real persistence, offline/online race and idempotency |
| I03 Interrupted mock | Distinct interrupt alert → noncomparable attempt → invalid results and explicit next actions; preserve only acknowledged answers | Exact clock/audio integrity detection and implementation quality |
| I04 Audio/timer | Always prominently labeled as simulation with no playback/countdown; no misleading playback control | Listening usability under actual audio/timing |
| I05 IA alternatives | IA-A Task Hub stays primary; IA-B Mode-centred remains navigable comparator | Any head-to-head user preference or superiority |
| I06 Reading alternative | W-02A passage/question with anchor versus W-02B expand/collapse comparator | Reduced taps/scroll/eyestrain in real use |
| I07 Score copy | Explicit **FICTITIOUS raw correct 130/200**, separate Listening/Reading and non-equivalent ETS warning; invalid attempts separated | Accurate real scoring or statistically equated mocks |
| I08 Family privacy/deletion | Explicit isolation, 7-day validated deletion request, routine ≤30-day post-pilot copy with clear PDF limits | Real authentication, access control, deletion and audit |

## Prototype structure

- **31 screens / 81 internal destinations**; all reachable from guide by link graph validation.
- **Two illustrative viewport contexts**: standard document layout and two larger phone-size renderings. NOT two physical Android devices.
- **9/9 scripted UX scenarios** have representative routes in the PDF; this is mapping coverage, not user task success or device test PASS.
- Link/visual PDF checks are document-quality checks only; **QA-01..08 tests remain unexecuted/not verified**.

## Change control

The S1-A/S2-A/S3-A locked MVP, business mock policies, data retention and Requirements Baseline are not modified. Actual content and budget conditions remain at their previously approved statuses. Any requested deviation must go to PO change control.
