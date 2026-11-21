# B1 — Two Mock QA Readiness and Stage 03 Requirements Handoff V0.1

**Status:** ANALYST PROPOSAL / NOT APPROVED AS ACCEPTANCE BASELINE.  
**Input:** Product Owner reported two sets inventoried. No underlying manifests or assets were accessed in this turn. Budget work has been explicitly deferred.

## 1. What is settled vs open

- **Settled as PO report:** Two Full Mock sets inventoried; source reuse rights for three named sites previously affirmed; B1 requires both mocks; source finding does not need to restart.
- **Open evidence:** For each mock, all 200 items independently correct by Part (P1=6, P2=25, P3=39, P4=30, P5=30, P6=16, P7=54), 100 Listening/100 Reading, audio and image/passage groups, answer keys, duplicate/overlap inventory and separation from practice content. User did not report these checks completed, so do not assume.
- **Unchanged:** Raw practice outcomes must not be represented as equated official ETS scores. The pilot needs a transparent progress metric, with limits on comparability across the two forms.

## 2. Proposed minimal review gate before mock data is declared READY TO USE

| QA ID | Check | Evidence to retain | Proposed blocking severity |
|---|---|---|---|
| QA-01 | Correct item counts and Part distribution per mock | Manifest summaries and missing-item report | Block for mismatch |
| QA-02 | Every item has one valid answer key; no ambiguous option from source | 100%-coverage answer audit log | Block wrong/unknown keys |
| QA-03 | Listening clips map to correct item groups; start/end and ordering checked | Clip-to-group map, playback spot-check + complete metadata audit | Block wrong/missing clips |
| QA-04 | Reading Part 6/7 associated passages, tables, graphics and context are complete | Passage/asset cross-reference | Block missing context |
| QA-05 | No duplicate questions across Mock A/B, and no leaked mock questions into practice bank | Cross-form duplicate report and exposure policy | Block known duplicates |
| QA-06 | For every used item, source ID, owner/rights status, and asset provenance are recorded | Rights metadata and exceptions register | Block unsupported rights |
| QA-07 | Assessment reports distinguish raw accuracy/Part diagnostics from ETS official scores | Reviewable reporting rules and misleading-claim checklist | Block official score claim without substantiation |
| QA-08 | Quiz duration, answer persistence, interruptions and long Reading accessibility covered in requirements | Requirements traceability and acceptance-case list | Block unaddressed critical behavior |

**Thresholds above are proposed for PO/QA review** and cannot be marked Passed without actual evidence. Some tests (e.g. interruption reliability and mobile readability) occur during later software testing, not before UI/implementation exists.

## 3. Evidence bundle to request later only if truly needed

A single combined summary for both mocks: stable form/source IDs, 7 Part counts, audio/answer/passage completeness, duplicate check, rights metadata provenance, reviewer/date and issue log. No item text, audio or files need to be uploaded merely to approve the requirements framework.

## 4. Priorities now

1. Continue PRD/SRS drafting of mock practice, scoring transparency, answer correction, access rights, auditability and family pilot flows.
2. Treat mock inventory as completed by PO declaration, while keeping QA outcome unverified.
3. Defer all budgets and avoid procurement; CP-04 remains tracked for the point when Product Owner reopens budget review.
4. Present one combined requirements/QA review, not serial research questions.
