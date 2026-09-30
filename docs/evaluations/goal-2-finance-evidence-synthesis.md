# Goal 2 finance: evidence synthesis

Status: provisional; Plan 02 remains active. Source IDs resolve through `docs/evidence/finance-provenance.md` and `data/manifests/finance-sources.json`. Calculations are in `data/finance/derived.json` and reproducible with `scripts/finance_evidence.py`.

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

FIN-08 (observation): FY2017 contains federal finding 2017-001: inadequate Title I time-and-effort and paraprofessional controls, a material weakness, and $50,312 questioned costs (SAO-RSD407-2017-FIN, pp5–6,16). Financial-statement findings were absent (p5). Questioned costs are an audit category, not a determination of theft or a final repayment. Later reports with different major programs cannot alone establish correction of this specific finding. FY2018 follow-up remains to be reviewed.

## Earlier reserve anchors

FIN-09 (observation/derived): audited General Fund totals and expenditure ratios are below. Exact transcriptions and physical pages are committed in observations; formulas are committed in the calculation script.

| Fiscal year end | Total balance | Expenditures | Total / expenditures | Evidence |
|---|---:|---:|---:|---|
| 2010 | $2,186,100.21 | $28,282,682.78 | 7.7295% | SAO-RSD407-2010-FIN, pp15–16; scanned tables visually reviewed |
| 2017 | $4,034,488.34 | $37,480,441.28 | 10.7642% | SAO-RSD407-2017-FIN, pp24–25 |
| 2019 | $7,340,277.12 | $45,740,916.99 | 16.0475% | SAO-RSD407-2019-FIN, pp19–20 |
| 2020 | $8,162,657.92 | $47,257,070.37 | 17.2729% | SAO-RSD407-2020-FIN, p21; rotated table visually reviewed |
| 2021 | $8,285,778.41 | $47,508,443.83 | 17.4406% | SAO-RSD407-2021-FIN, p21 |
| 2022 | $7,310,473.12 | $51,234,734.75 | 14.2686% | SAO-RSD407-2022-FIN, p22 |

FIN-10 (evaluation): the continuous FY2019–FY2025 series shows growth through FY2021 followed by four annual declines, rather than decline only beginning FY2024. FY2010 and FY2017 are earlier plan-era anchors; missing FY2011–FY2016 and FY2018 observations are not interpolated. Changes across gaps are explicitly tagged nonconsecutive by the calculator. Nominal dollar growth between distant anchors is not inflation-adjusted improvement or evidence of strategic-plan causation.

## Bounded remaining work

1. Review FY2018 prior-finding follow-up and early plan-era audit conclusions before classifying correction/recurrence.
2. Determine whether surviving Board budget/adoption evidence resolves motion 24-30's fiscal-year applicability; otherwise retain a bounded uncertainty.
3. Make the final fiscal-stewardship classification, preserving the uncommitted/unassigned distinction and 5%/7%/9% documentation conflicts.
4. Record remaining archive failures as preservation gaps; no failed capture is described as preserved. Plan 02 remains active until final review.
