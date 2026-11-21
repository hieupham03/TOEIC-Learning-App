# TOEIC Learning App — Stage 03 B1: 3-Website Evidence Screen V0.1

**Review date:** 2026-11-21. **Scope:** read-only desk research of the three exact URLs the Product Owner provided. **Status:** analyst research DRAFT, not a content license, permission to scrape, QA certification, or MVP approval.

## URLs supplied by Product Owner

1. https://test.thetoeiclab.vn/
2. https://zenlishtoeic.vn/test-online-new/
3. https://study4.com/tests/toeic/  (web retrieval for catalog used https://study4.com//tests/toeic/ as an accessible equivalent)

PO previously stated they possess rights to all intended educational materials. Record as **PO SELF-ATTESTATION**. Whether that grant covers questions, images, audio and answers specifically hosted by each named platform, and delivery to another Android app, is **NOT DOCUMENTED FOR THESE THREE SOURCES**. Do not presume PO has no such rights.

## Findings by source

| Source | Verified from publicly readable pages | Not established | Re-use assessment |
|---|---|---|---|
| The TOEIC Lab / test.thetoeiclab.vn | Accessible page says `Đang kiểm tra đăng nhập...` | Full test catalog, number of items, Parts, actual audio/keys, export path, rights / terms for this subsite | **ACCESS BLOCKED / UNKNOWN**; could be re-evaluated with a permitted account or owner-provided catalog, without requesting credentials |
| Zenlish / test-online-new | Public catalog lists ten 2026 L&R Full Tests, additional years and Hacker collections, plus Mini Tests. Test 1 / Test 2 pages accessible; allow guest mode, selecting Parts and scoring (guest attempt/history not stored) | Actual full item/media payload is client-rendered; cannot confirm 200 unique questions per form, all audio/images/keys, correctness or machine-readable export; no explicit app reuse license identified on reviewed pages | **CATALOG STRONG / RIGHTS & ASSETS UNVERIFIED** |
| STUDY4 / tests/toeic | Catalog lists at least twenty TOEIC LR Collection sets; entries say 120 minutes, 7 Parts, 200 items. Sample Test details list all seven Parts, practice mode and full-test mode | Audio/answer keys not QA audited, item duplication not checked, content export permissions unknown | **CATALOG STRONG / DEFAULT WEBSITE TERMS RESTRICT REUSE** |

## Evidence and permitted handling

- The TOEIC Lab open URL: https://test.thetoeiclab.vn/ (login gate observed).
- Zenlish catalog: https://zenlishtoeic.vn/test-online-new/ ; samples https://zenlishtoeic.vn/stm-quizzes/test-1-2026/ and https://zenlishtoeic.vn/stm-quizzes/test-2-2026/ . Public guest page states guest attempts are graded but not saved in history.
- STUDY4 library: https://study4.com//tests/toeic/ ; example detail https://study4.com/tests/1211/sample-toeic-test-5/ (all Parts and 200 items shown); terms https://study4.com/terms/ , section 4 restricts copying/distributing content outside the rights granted.
- Zenlish pages did not furnish an express grant authorizing re-hosting test questions/media in a separate Android product. Absence of located license is **not proof no separate permission exists**.

## Counts: what they do and do not show

- Zenlish ten named 2026 test links and STUDY4 twenty catalog test entries are **provider-published listing counts** only. They are not 10 or 20 rights-cleared/QA-passed forms owned by the PO.
- No bulk harvesting, credentials, access circumvention, or test asset copying occurred.
- Content sourced from books, ETS collections, or third parties embedded inside websites can have distinct owners; the site's permission alone may not cover every asset.

## Gate implication

The three URLs resolve **source discovery/candidate catalog availability**, NOT the B1 **400 validated distinct items, rights-cleared audio/images, independent question-bank mapping, 2 comparable mocks, QA and budget** gates. G-SOURCE remains AMBER candidate-only; G-RIGHTS/G-MOCK/G-QA/G-COST stay OPEN for MVP lock. B1 two Full Mock forms remain mandatory and not waived.
