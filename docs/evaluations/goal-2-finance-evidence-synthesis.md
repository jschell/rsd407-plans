# Goal 2 finance: evidence synthesis

Status: finance closeout assessment complete within the documented evidence limits; operational Goal 2 work remains separate. Source IDs resolve through `docs/evidence/finance-provenance.md` and `data/manifests/finance-sources.json`. Calculations are in `data/finance/derived.json` and reproducible with `scripts/finance_evidence.py`.

## Observations and derived results

| Period | General Fund total ending balance | Expenditures | Total / expenditures | Basis / evidence |
|---|---:|---:|---:|---|
| 2022-23 | $6,280,053.86 | $52,972,914.74 | 11.8552% | Audited actual; SAO-RSD407-2023-FIN |
| 2023-24 | $6,183,886.39 | $55,851,151.36 | 11.0721% | Audited actual; SAO-RSD407-2024-FIN |
| 2024-25 | $4,965,888.03 | $59,197,178.87 | 8.3887% | Audited actual; SAO-RSD407-2025-FIN |
| 2025-26 | $3,134,254 | $62,508,931 | 5.0141% | Budget estimate; RSD407-FY2026-BUDGET-SUMMARY |

FIN-01 (derived): total balances declined $96,167.47 in FY2024 and $1,217,998.36 in FY2025. These ratios describe total balances against actual expenditures for audited periods; they do not test a target defined against budgeted expenditures or an uncommitted/unassigned numerator.

FIN-02 (observation): March 26, 2024 minutes, motion 24-30, give leadership guidance to lower the budget ending balance to no lower than 7% (RSD407-MOTION-24-30, physical p3). The motion does not specify a fiscal year or expenditure denominator, nor explicitly create a committed fund-balance classification. FY2024 audited Note 14 characterizes the motion as a 7% minimum against budgeted expenditures (SAO-RSD407-2024-FIN, p46). September 2024 Goal 2A instead seeks 7% **uncommitted** balance by August 2025 (RSD407-SP-2024-SEP, p8). These definitions must remain distinct.

FIN-03 (conflict/derived): FY2025 Note 15 states 5%, while its policy reserve row is $4,143,803 (SAO-RSD407-2025-FIN, p46). Seven percent of actual expenditures is $4,143,802.5209; 5% is $2,959,858.9435. The row matches 7% after whole-dollar rounding. The balance sheet reports $4,899,256.79 unassigned (p19), including the policy reserve; $755,454 is not the whole unassigned balance. The published revised policy resolves the target definition, but does not correct the audited-note inconsistency.

FIN-04 (observation/derived): Policy 6000 specifies a target minimum of 5% **total** and 2.5% **unassigned**, both against total **actual** expenditures at fiscal year end, and permits Board-adopted annual estimated total balances departing from target (RSD407-POLICY-6000-2025, p1). Its footer records revision May 13, 2025 (p4). May 13 minutes record second-reading approval, motion 25-65 (RSD407-MOTION-25-65, p6); May 27 minutes record approval of May 13 minutes under motion 25-68 (RSD407-MAY27-2025-MINUTES, p4). Both retrieved minutes are marked Draft, so the published policy provides the independent corroboration; no separate delayed effective date was located. FY2025 total/actual is 8.3887%, and unassigned/actual is 8.2762%, exceeding the published 5%/2.5% numeric targets. This establishes numeric attainment under that definition, not all policy compliance or fiscal stability.

FIN-05 (conflict): FY2024 dashboard displays a 9% target and unsigned $96,167 change (RSD407-FY2024-YE, p3). The full year-end analysis describes a decrease and retains 9% (RSD407-FY2024-FULL, p3); audited statements establish the decline. The same full report's August revised budget table gives $56,472,108 expenditures (p7), while its F196 comparison gives $56,472,106 (p24), corroborated by the later F195 (RSD407-FY2025-F195, p5). Preserve the $2 discrepancy. Their 7% comparators are $3,953,047.56 and $3,953,047.42. FY2025 F195 budget expenditures are $62,082,341 (p5), giving $4,345,763.87 at 7%. These are historical comparators, not a silent choice of which budget motion 24-30 governs.

## Audit evidence

FIN-06 (observation): FY2023, FY2024 and FY2025 financial/single-audit reports list no financial-statement or federal-award findings (SAO-RSD407-2023/2024/2025-FIN, PDF p5). Each accountability report describes material compliance and adequate safeguarding controls in selected areas (SAO-RSD407-2023/2024/2025-ACC, PDF p4). Scope varies by year. Financial reports express an unmodified regulatory-basis opinion and an adverse GAAP opinion arising from the reporting basis; no whole-system control-effectiveness opinion is expressed.

FIN-07 (observation/evaluation): FY2019–FY2022 financial/single-audit reports also list no financial-statement or federal-award findings (SAO-RSD407-2019/2020/2021/2022-FIN, p5). Their accountability reports describe material compliance and adequate safeguards in selected areas (corresponding ACC IDs, p4). Major federal programs differ: FY2019–FY2020 IDEA; FY2021 Education Stabilization Fund; FY2022 Child Nutrition and Education Stabilization. This supports continuity before the recent three-year slice, with scope qualifications.

FIN-08 (observation): FY2017 contains federal finding 2017-001: inadequate Title I time-and-effort and paraprofessional controls, a material weakness, and $50,312 questioned costs (SAO-RSD407-2017-FIN, pp5–6,16). Financial-statement findings were absent (p5). Questioned costs are an audit category, not a determination of theft or a final repayment. Later reports with different major programs cannot alone establish correction of this specific finding. FY2018 follow-up is reviewed below (FIN-11).

## Earlier reserve anchors

FIN-09 (observation/derived): audited General Fund totals and expenditure ratios are below. Exact transcriptions and physical pages are committed in observations; formulas are committed in the calculation script.

| Fiscal year end | Total balance | Expenditures | Total / expenditures | Evidence |
|---|---:|---:|---:|---|
| 2010 | $2,186,100.21 | $28,282,682.78 | 7.7295% | SAO-RSD407-2010-FIN, pp15–16; scanned tables visually reviewed |
| 2017 | $4,034,488.34 | $37,480,441.28 | 10.7642% | SAO-RSD407-2017-FIN, pp24–25 |
| 2018 | $4,276,743.93 | $40,632,892.55 | 10.5253% | SAO-RSD407-2018-FIN, pp21–22 |
| 2019 | $7,340,277.12 | $45,740,916.99 | 16.0475% | SAO-RSD407-2019-FIN, pp19–20 |
| 2020 | $8,162,657.92 | $47,257,070.37 | 17.2729% | SAO-RSD407-2020-FIN, p21; rotated table visually reviewed |
| 2021 | $8,285,778.41 | $47,508,443.83 | 17.4406% | SAO-RSD407-2021-FIN, p21 |
| 2022 | $7,310,473.12 | $51,234,734.75 | 14.2686% | SAO-RSD407-2022-FIN, p22 |

FIN-10 (evaluation): the continuous FY2017–FY2025 series shows growth through FY2021 followed by four annual declines, rather than decline only beginning FY2024. FY2010 and FY2017 are earlier plan-era anchors; missing FY2011–FY2016 observations are not interpolated. Changes across gaps are explicitly tagged nonconsecutive by the calculator. Nominal dollar growth between distant anchors is not inflation-adjusted improvement or evidence of strategic-plan causation.

## Follow-up and early audit baseline

FIN-11 (observation): the FY2018 management-supplied prior-finding schedule marks 2017-001 Fully Corrected, describing adoption of an internal audit process and ongoing implementation of a Business Office procedure (SAO-RSD407-2018-FIN, pp6–7). Separately, the auditor selected Title I and IDEA as major programs, issued an unmodified compliance opinion, and reported no financial-statement or federal-award findings (p5). The management assertion and auditor's findings are distinct: together they support correction by the following audit, without certifying every control indefinitely or establishing final repayment of questioned costs. The schedule reproduces prior Title I spending as $181,537 (p6), whereas the original FY2017 finding states $381,537 (SAO-RSD407-2017-FIN, p6). Preserve both; the original report governs its original observation.

FIN-12 (observation): FY2010 financial/federal summary reports no significant deficiencies, material weaknesses or reportable federal findings under OMB Circular A-133 (SAO-RSD407-2010-FIN, p4). The corresponding accountability report covers September 2008–August 2010 and reports adequate safeguarding and compliance in selected areas (SAO-RSD407-2010-ACC, p4); it also states the district had been free of findings for five years (p7), a source-reported historical statement rather than independent review of five additional reports. Standards, thresholds, programs and accountability periods differ from later audits. FY2018 accountability conclusions also report compliance and adequate safeguards in selected areas (SAO-RSD407-2018-ACC, p4).

## Finance closeout classification

FIN-13 (evaluation under `docs/methodology/evaluation-framework.md`):

| Component | Classification | Evidence and limit |
|---|---|---|
| Financial reporting and recurring audit responsibilities | Sustained responsibility | Early clean baseline (FIN-12), specific FY2017 weakness (FIN-08), FY2018 follow-up (FIN-11), and subsequent scoped results (FIN-06/07). Not uninterrupted historical absence of findings or proof of plan causation. |
| Title I control issue | Resolved or institutionalized, supported as of FY2018 audit | Management reported correction and auditor retested Title I without new findings (FIN-11). Long-term implementation fidelity and questioned-cost settlement not established. |
| Reserve stewardship | Evolving challenge | Reserve ratio rose to 17.4406% in FY2021, then fell to 8.3887% in FY2025 (FIN-09/10). Numeric FY2025 revised-policy targets met (FIN-04); decline still matters. |
| Original September 2024 7% uncommitted objective | Cannot determine goal attainment | Strategic-plan uncommitted numerator is not demonstrably identical to audited unassigned or total; denominator unspecified (FIN-02). Revised-policy numeric attainment does not retroactively prove this objective met. |
| Revised 2025 5% total / 2.5% unassigned objective | Met for FY2025 numeric balances | Reproducible actual-expenditure comparison (FIN-04), limited to the published definition and fiscal year. FY2026 budget is a forecast, not an achieved outcome. |
| Documentation of reserve targets | Measurement failure in reconciliation | The 5% note versus 7% amount, 9% dashboard, unspecified motion denominator, and $2 budget discrepancy remain explicit (FIN-02/03/05). This classification concerns consistency of evidence, not a finding of financial misstatement materiality. |
| Task design and implementation | Appropriate but incomplete / Partially implemented at the evidence level | Board motion, policy revision and audited balances establish actions; causal improvement and full control/process fidelity are not demonstrated. |

## Closeout boundaries

Plan 02 ends with the original strategic objective's attainment **Cannot determine**, the revised policy's FY2025 numeric targets **Met**, and fiscal stewardship an **Evolving challenge** within a **Sustained responsibility**. There is no single unqualified claim of overall Goal 2 attainment.

The exact budget intended by motion 24-30 remains unspecified in the retrieved primary motion. Documented FY2024 and FY2025 denominators and separate calculations are available; choosing one as the unique governed budget would exceed the evidence. This is a closed analytical limitation, not a missing calculation. Audited unassigned remains distinct from strategic-plan uncommitted.

No inflation-adjusted or peer-district comparison is claimed. FY2011–FY2016 annual reserves remain unreviewed between anchors. Archive failures remain preservation gaps with publisher URLs and byte hashes available; no capture is labelled preserved without a matching hash. Reopen this finance assessment if corrected policy/audit notes, certified minutes changing the motion, questioned-cost disposition, or new actual-year data changes a material conclusion. Operations and allocation outcomes proceed under Plan 03 and later plans.

## Later allocation/recovery context discovered under Plan 03

FIN-14 (observation): September 2026 status update calls for a Financial Recovery Framework aligning budgets, forecasts and staffing to rebuild fund balance (RSD407-SP-2026-SEP, p6; source resolves via `data/manifests/allocation-sources.json`). FY2027 budget overview describes 5% minimum / 7% goal / 10% target at GL 891 (RSD407-FY2027-BUDGET-PRESENTATION, p23) and a later detailed presentation (p21). These are later district design statements; they neither amend the published 2025 policy by themselves nor establish achieved FY2026/FY2027 outcomes. Preserve the differing classifications/definitions rather than merging them with FIN-04. They reinforce the evolving-challenge classification; allocation implications proceed under Plan 03.
