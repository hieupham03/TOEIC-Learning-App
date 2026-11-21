# Stage 04 — UX-04 Scenario Coverage / Observation Register V0.1

**Method:** Review of **click-through prototype paths** against approved scenario protocol. No recruited participants; **user-study n=0**. “PATH PRESENT” is not “user completed test”.

| Scenario | Candidate path | Desk path exists? | Actual participant result |
|---|---|---|---|
| UT-01 5-minute practice | HOME → PARTSELECT → PRACTICE | YES | NOT RUN |
| UT-02 start 200-question mock | HOME → MOCKLIST → RULES | YES | NOT RUN |
| UT-03 Part7 refind passage | PASSAGE → READQUESTION → ANCHOR | YES | NOT RUN; scroll restore only simulated |
| UT-04 pending vs acknowledged answer | PRACTICE → PENDING → SAVED / SAVEERR | YES | NOT RUN; backend not implemented |
| UT-05 interrupted mock | LISTENING → INTERRUPTED → INVALID | YES | NOT RUN; timer not implemented |
| UT-06 feedback after eligible practice | SAVED → FEEDBACK → PARTSELECT | YES | NOT RUN; content QA not evidenced |
| UT-07 interpret raw results | LISTENING → RESULTS → PROGRESS | YES | NOT RUN; mock score fictitious |
| UT-08 privacy/deletion visibility | HOME → PRIVACY | YES | NOT RUN; actual isolation not implemented |
| UT-09 content unavailable | MOCKLIST → UNAVAILABLE → MOCKLIST | YES | NOT RUN; QA content gates still active |

**Reviewer evidence:** All 26 screens reachable from initial page via internal links; PDF contains more than 90 internal link annotations. This is link-path integrity of the PDF, not an Android application test.

**Data collection sheet for possible voluntary short walkthrough:** anonymous participant code, informed consent, context/device, scenario ID, outcome, confusion, participant quote only if recorded/consented, investigator help, issue severity, follow-up. Leave all fields blank until a real session occurs.

**No forced new 120-min Mock** and no budget work.
