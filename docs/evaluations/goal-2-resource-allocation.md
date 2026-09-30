# Goal 2A — Resource Allocation and IEP Staffing

Status: bounded public-evidence assessment complete. Initial checkpoint and subsequent decision review are distinguished below. Exact reviewed URLs and SHA-256 hashes are in `data/manifests/allocation-sources.json`; September 2024 baseline resolves through the existing finance manifest. Physical PDF pages are 1-based. Original task labels are in `data/allocation/observations.json`.

## Status chronology

ALLOC-01 (observation): September 2024 Goal 2A task 1 calls for collaborative analysis of budget, personnel and time to align services, due August 2025; task 3 calls for review/use of a data-based process for additional staff supporting individual students with IEPs, due June 2025. Both are In Progress (RSD407-SP-2024-SEP, p8).

ALLOC-02 (observation): January 2025 retains both tasks and reports In Progress (RSD407-SP-2025-JAN, p7). July 2025 marks both Completed, while the 7% reserve task remains In Progress (RSD407-SP-2025-JUL, p7). These are district completion assertions; neither cited page supplies the underlying staffing rule, allocation decision, meeting output, or outcome comparison.

ALLOC-03 (observation): September 2026 Goal 2A task 2 calls for implementation/evaluation of a multi-year Financial Recovery Framework to align budgeting, forecasting and staffing allocations and rebuild balance, due August 2027, In progress (RSD407-SP-2026-SEP, p6). This is a later work item under the same objective, not evidence that the earlier IEP process was completed or abandoned. Task numbers changed and should not be matched by number alone.

## Process leads and authority limits

ALLOC-04 (observation): the district-published REA bargaining document contains tracked-change provisions for a special-education leadership team making allocation/support recommendations, a workload committee, and a severity matrix for 2026–27, with committee dates October 15, 2025 through January 15, 2026 (RSD407-REA-2025-REDLINE, physical p54 / printed p49). Visual review confirms tracked changes. This is a proposal/edited bargaining artifact; final ratification, effective terms, matrix completion and actual use require separate evidence. It is not automatically the process declared Completed in July 2025, particularly given the later dates.

ALLOC-05 (observation): the FY2027 budget presentation describes a recovery-framework overview and defers a detailed presentation to October–November alongside FY2026 year-end actuals (RSD407-FY2027-BUDGET-PRESENTATION, p21). Its six-component outline includes staffing aligned to funded levels and an enrollment-based set-aside (p23). The presentation describes intentions and asserts components shaped the budget; it does not supply a traceable before/after staffing decision for the original 2025 tasks.

ALLOC-06 (evaluation): initial implementation classification is **Cannot determine independently**, with district-reported completion retained. Goal attainment is **Cannot determine**. The task design plausibly connects needs data to support decisions, but current evidence establishes status assertions and later proposed mechanisms rather than implementation fidelity or reduced barriers to learning. Do not infer ineffectiveness from unavailable evidence or improvement from task completion.

## Initial checkpoint gaps (before decision review)

| Question | Minimum useful evidence | Current state |
|---|---|---|
| What was the completed 2025 IEP staffing process? | Dated adopted rule/matrix, approval and effective period | Not established in reviewed sources |
| Was it used? | De-identified decision or aggregate staffing allocation tied to rule inputs and resulting support | Not established |
| Did collaborative resource analysis change allocation? | Dated needs-analysis output and identifiable Board/budget staffing decision | Not established |
| Did barriers/support improve? | Comparable aggregate caseload, service delivery or access measure with baseline and period | Not established |
| Did later framework change staffing decisions? | Adopted framework, allocations and monitoring outputs | Overview located; later deep-dive remains a future item as of September 30, 2026 |

The subsequent targeted agreement and Board-decision review is recorded below. Search later recovery allocations only where they directly answer continuity/evolution. Do not widen into new OSPI outcome collection or analyze student-specific records. If targeted public-source searches do not yield decision traces, close with explicitly bounded Cannot determine findings and a list of unavailable artifacts rather than endless exploration.

## Agreement authority and visible matrix

ALLOC-07 (observation): September 9, 2025 minutes record motion 25-101 adding the 2025–2027 REA agreement to consent, followed by motion 25-102 approving the amended consent agenda, Carried (RSD407-SEP09-2025-MINUTES, pp4–5). The packet is explicitly Draft. This establishes a recorded Board approval event, with the draft qualification; it does not establish a clean signed final version or validate every proposed term. The event is later than the July 2025 completion report and cannot by itself explain that earlier process claim.

ALLOC-08 (observation): the bargaining artifact's physical p125 is a Severity Matrix heading; physical p126 contains **image tables** for service time, instructional support and behavioral support, plus a total-student-weight worksheet (RSD407-REA-2025-REDLINE, printed pp120–121). Text extraction misses the tables. They have been visually reviewed and transcribed in `data/allocation/observations.json`. Service-time weights range 1–4; instructional and behavioral support weights each range 0–2. A source-specified zero weight is not a missing-data replacement. The original time bands overlap at 12.5 hours and do not define the interval from 24 to 25 or values above 30. No boundary rules are invented. This page does not establish a mapping from total weight to staff FTE, filled-in caseloads or actual staffing decisions. Numeric portal URL `/document/12156/` yields the same original SHA-256 as the existing UUID source, so it is recorded as an alternate URL rather than independent corroboration.

## Decision trace and limits

ALLOC-09 (observation): Resolution 25-02 says the Board reviewed enrollment, revenues/expenditures, vacancies and resignations, found financial necessity, adopted a reduced educational program, and directed implementation (RSD407-RESOLUTION-25-02, pp1–3). Its three-page standalone file omits Exhibit A and has unexecuted signature spaces. The previously preserved May 13 packet records approval by motion 25-60, Carried, and contains Exhibit A (RSD407-MOTION-25-65, pp5,140–143, finance manifest). That packet's evidence ID originally refers to another motion on p6, but identifies the entire exact packet; the reviewed allocation motion is **25-60**, not 25-65. Minutes are marked Draft. This is a documented Board authorization with stated financial inputs, not proof of subsequent deployed staffing or of the strategic-task analysis causing the reductions.

ALLOC-10 (observation/derived conflict): Exhibit A lists a 1.1 FTE instructional paraeducator reduction, without specifying that the position is special education. The specialist heading says 1.5 FTE while line items specify ESA Nurse 1.0, Mental Health Counselor 0.5, and LAP Teacher 0.9, summing to 2.4 FTE, a 0.9 FTE discrepancy (RSD407-MOTION-25-65, physical p143). `scripts/allocation_evidence.py` reproduces the calculation in `data/allocation/derived.json`. No corrected aggregate or actual deployment is inferred.

## Final classifications

ALLOC-11 (evaluation under `docs/methodology/evaluation-framework.md`):

| Component | Classification | Supported finding and limit |
|---|---|---|
| Task design | Appropriate but incomplete | Needs analysis and staff-support rules are plausible routes to reducing barriers; status pages and worksheet lack a verifiable outcome measure/decision trace. |
| Resource-analysis implementation | Cannot determine | District reports Completed (ALLOC-02); Board records a reduction authorization and financial inputs (ALLOC-09), but the collaboration output and its connection to that decision are unverified. |
| IEP staffing-process implementation | Cannot determine | District reports Completed; weighting artifact and later agreement approval found (ALLOC-07/08), but July 2025 process identity and actual use remain unverified. |
| Allocation decision authorization | Implemented at the recorded approval level | Motion 25-60 records approval; actual deployment, final staffing totals and changes after approval cannot be determined. This narrow finding does not classify the whole strategic task as implemented. |
| Equitable support / barrier reduction | Cannot determine goal attainment | No comparable caseload/service-access outcome trace established by the reviewed status reports, agreement/matrix or reduction decision. Financial reductions are not an outcome proxy. |
| Recurrence | Evolving challenge | July 2025 completion assertions followed by later severity-matrix development and September 2026 recovery allocations (ALLOC-02–05/07–09). This is evolution of documented work, not evidence of recurrent failure or causal deterioration. |

## Completion boundary and reopening evidence

The targeted review covered plan-status updates, the Board-linked bargaining artifact and worksheet, recorded agreement approval, a May 2025 allocation authorization and its position exhibit, and later recovery context. Queries were REA agreement, severity, staff allocation, 2025-2027, and additional support, alongside the initial search terms. Details were inspected for up to the first 40 returned IDs per query; this is a bounded search, not a census proving records do not exist. Search hits are discovery leads, not negative evidence of absence.

Close Plan 03 with district-reported completion retained and independent implementation/goal attainment **Cannot determine**. Do not label the task Not implemented or the goal Not met. Remaining useful artifacts are a dated clean adopted staffing process, the July 2025 collaboration output, de-identified decisions showing rule inputs and resulting support, final deployed staffing reconciled to Exhibit A, and comparable aggregate caseload/service-access measures. These can reopen the assessment; no further broad exploration or waiting for future recovery reports is required. Proceed to Plan 04 safety implementation.
