# Evidence Source Ledger

This file is the human-readable provenance index. Machine-readable manifests belong in `data/manifests/`.

| Evidence ID | Publisher | Source | Period | Authority | Status / limitation |
|---|---|---|---|---|---|
| OSPI-RSD407 | OSPI | Report Card / Data Portal, org 100222, district 17407 | multi-year | Primary | Plan 01 complete; run 36744065183 / artifact 11111512770; see Goal 1 evidence synthesis |
| SAO-RSD407-2024 | WA State Auditor | Riverview audit reports | FY2024 | Primary external | Used in finance evaluation |
| SAO-RSD407-2025 | WA State Auditor | Riverview audit reports | FY2025 | Primary external | Used in finance evaluation |
| RSD407-SP-CURRENT | Riverview SD | 2022–27 Strategic Plan/status reports | current | Primary | Core plan source |
| RSD407-SIP-CHS | Riverview SD | Cedarcrest SIP | 2023–26 evidence | Primary | School-level evidence |
| RSD407-SIP-TOLT | Riverview SD | Tolt SIP | 2024–25 | Primary | School-level implementation evidence |

Expand this ledger whenever evidence is added.

## Finance primary-source inventory

The thirty reviewed finance sources, exact URLs, retrieval metadata, source hashes and Internet Archive request outcomes are recorded in `data/manifests/finance-sources.json`. Page-level references and reproduction instructions are in [finance provenance](finance-provenance.md). Material finance assertions are FIN-01 through FIN-13 in `docs/evaluations/goal-2-finance-evidence-synthesis.md`; they supersede broad source references for those assertions.

## Resource allocation initial inventory

Seven reviewed allocation PDFs resolve through `data/manifests/allocation-sources.json` and [allocation provenance](allocation-provenance.md). ALLOC-01–ALLOC-11 distinguish task-status claims from allocation decisions and outcomes. FIN-14 uses the same manifest for later recovery context. Plan 03 assessment is complete within its bounds; no independent outcome-attainment claim is made.

## Safety initial inventory

Four reviewed primary PDFs resolve through `data/manifests/safety-sources.json` and [safety provenance](safety-provenance.md). SAFE-01–SAFE-08 reuse the plan-status sources and distinguish control design/adoption from completed execution and outcomes. Plan 04 is active.

Plan 04 procedure reconciliation adds eight locally reviewed policy, procedure, blank-form and approval PDFs to `data/manifests/safety-sources.json` (SAFE-09–SAFE-14). Exact URLs, byte counts, SHA-256 and capture outcomes are recorded; no original PDFs are committed. Portal/PDF date differences and Draft approval status are explicit in the safety evaluation.

Plan 04 closeout: six additional department/accounting/assessment/survey PDFs complete the eighteen-source safety manifest. SAFE-15–SAFE-20 document partial access work, readiness limits and final classifications. Provenance and archive outcomes remain explicit; no original PDFs or individual case records committed.

Plan 05 HR initial checkpoint: three newly reviewed policy/procedure/recruitment-event PDFs in `data/manifests/hr-sources.json`, plus reused strategic sources. HR-01–HR-07 distinguish task completion from current workforce composition, retention, recruiting efficiency and learning coverage. Historical 2013 workforce/2000 pool data and undated event year are explicit; originals are not committed.

Plan 05 closeout adds four reviewed Board/department PDFs, completing seven HR sources. HR-08–HR-13 attribute dated orientation and professional-learning activity while retaining absent matched aggregate outcome measures. Bounded research is complete; Plan 06 Communications is next. Exact hashes and archive outcomes remain in HR manifest.
