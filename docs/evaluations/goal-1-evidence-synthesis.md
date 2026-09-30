# Goal 1 Evidence Synthesis

## Scope

This document evaluates the 2022–27 strategic-plan Goal 1 using a bounded set of material assertions. It does not treat the full OSPI analytical output as a list of independent findings.

**Goal 1:** Increase the growth of each and every student in achieving district student outcomes.

The synthesis distinguishes:
- **Observation** — directly reported evidence.
- **Derived result** — reproducible calculation from observations.
- **Evaluation** — interpretation against the strategic objective.
- **Limitation** — suppression, methodology, target, comparability, or causal constraint.

Task completion is not evidence that a student outcome was achieved.

## Evaluation rules

Outcome status:
- **Met** — an explicit measurable target is supported by comparable outcome evidence.
- **Partially met** — evidence supports some, but not all, material parts of an objective.
- **Not met** — comparable evidence contradicts an explicit measurable target.
- **Cannot determine** — no measurable target or insufficient comparable evidence.

Challenge direction:
- **Narrowing** — a comparable outcome disparity decreases.
- **Persistent** — a material disparity remains across comparable observations.
- **Widening** — a comparable disparity increases.
- **Cannot determine** — suppression or comparability prevents a defensible direction.

No causal claim is made from temporal association alone.

## Required assertion set

The final synthesis should contain only assertions supported by the validated Goal 1 pipeline and primary district evidence.

### G1-A — Overall achievement

**G1-A1. ELA achievement direction.**
Test district assessment outcomes over comparable plan-period observations; include WA-relative context where an exact match exists.

**G1-A2. Mathematics achievement direction.**
Same standard as G1-A1.

**G1-A3. Science achievement direction.**
Same standard where comparable assessment evidence exists.

Assessment results must carry the September 2026 OSPI republication/methodology comparability note where applicable.

### G1-B — Student growth

**G1-B1. ELA growth direction.**
Use median SGP or the corresponding OSPI growth outcome, not student counts.

**G1-B2. Mathematics growth direction.**
Use the same construction and distinguish absolute district movement from movement relative to Washington.

### G1-C — Graduation

**G1-C1. Four-year graduation direction.**
Use comparable district graduation-rate observations.

**G1-C2. Five-year graduation direction.**
Include only if it materially changes interpretation or addresses a documented district concern.

### G1-D — Achievement gaps / “each and every student”

Prioritize groups explicitly identified in district strategic-plan/SIP evidence.

**G1-D1. Low-income achievement gap.**

**G1-D2. Students with Disabilities achievement gap.**

**G1-D3. English Learner outcome/gap.**

For each, select a small number of material assessment/growth/graduation indicators. Report exact-context subgroup-minus-All-Students gaps and longitudinal gap change. Do not aggregate unrelated grades, subjects, tests, schools, or indicators into a synthetic district score.

Additional groups may be added only when a district source identifies them as a material strategic concern or an existing assertion cannot otherwise be evaluated.

### G1-E — Implementation versus outcomes

**G1-E1. Evidence of implementation.**
Identify documented Goal 1 activities/supports from strategic-plan status reports and SIPs.

**G1-E2. Outcome linkage.**
State whether the evidence establishes only implementation, temporal association, or a stronger outcome link. Do not infer causation from implementation plus subsequent outcome movement.

### G1-F — Overall Goal 1 determination

Synthesize G1-A through G1-E. If the strategic plan lacks explicit numerical targets, say so and avoid converting directional aspirations into invented thresholds.


## Findings from validated OSPI run

**Authoritative analytical run:** GitHub Actions run `36744065183`, artifact `11111512770`, artifact SHA-256 `a20428371aa7a9ed24d8fa6b48c57adde7025562fc798199dc022d07604a29f3`. The run validated 29/29 required source acquisitions. Derived outputs contain 22,215 exact-context district/WA comparisons, 16,684 district longitudinal changes, 81,106 subgroup gaps, and 39,312 subgroup-gap changes.

### G1-A — Overall achievement

**G1-A1 — ELA achievement. Observation/derived result:** In 2024–25, Riverview's All Students SBAC ELA `percent_consistent_grade` exceeded the matched Washington value at every reported tested grade (3–8 and 10) and for the All Grades row. Examples include grade 3, 54.8% district versus 47.8% WA; grade 8, 64.4% versus 48.5%; and grade 10, 78.0% versus 58.9%. The All Grades comparison was 63.4% versus 50.9% (+12.5 percentage points). Source dataset: `h5d9-vgwi`; derived output: `goal1_core_wa_comparisons.csv`.

**Evaluation:** Positive current outcome evidence. The data support that district ELA achievement was above the matched statewide level in 2024–25. A formal Goal 1 attainment determination cannot be made from this comparison alone because the strategic plan does not define a numerical ELA target.

**G1-A2 — Mathematics achievement. Observation/derived result:** In 2024–25, Riverview's All Students SBAC math `percent_consistent_grade` exceeded the matched Washington value at every reported tested grade (3–8 and 10) and for All Grades. The All Grades comparison was 52.4% district versus 40.7% WA (+11.7 points). Grade-level examples include grade 3, 59.4% versus 51.2%; grade 5, 55.4% versus 41.9%; and grade 8, 51.7% versus 35.5%. Source dataset: `h5d9-vgwi`; derived output: `goal1_core_wa_comparisons.csv`.

**Evaluation:** Positive current outcome evidence, but not sufficient to declare the strategic goal met without a defined target.

**G1-A3 — Science achievement. Observation/derived result:** 2024–25 WCAS science `percent_consistent_grade` was above Washington at each matched All Students grade: grade 5, 68.6% versus 51.4%; grade 8, 54.8% versus 42.1%; grade 11, 52.1% versus 36.9%. The All Grades comparison was 58.4% versus 43.3%. Source dataset: `h5d9-vgwi`.

**Evaluation:** Positive current outcome evidence.

**Assessment limitation:** OSPI republished historical assessment data in September 2026 using a changed methodology based on students tested rather than students expected to test. Current 2024–25 district-versus-WA comparisons are internally matched within the same release. Longitudinal assessment claims are therefore treated conservatively and are not used here as the primary evidence of improvement over the full plan period.

### G1-B — Student growth

**G1-B1/G1-B2 — ELA and mathematics growth. Observation/derived result:** For 2024–25 All Students median SGP, the All Grades district result was 51 in ELA versus the WA median of 50 and 52 in math versus 50. Grade-level results were mixed: Riverview was above 50 in 7 of 12 matched grade/subject comparisons and below 50 in 5. Stronger examples included grade 5 ELA 58 and math 62; weaker examples included grade 7 ELA 40 and grade 6 ELA/math 45.5. Source dataset: `hv7j-ib7g`; derived output: `goal1_core_wa_comparisons.csv`.

**Evaluation:** Mixed but slightly positive current growth evidence. District-wide All Grades medians were above the statewide median, but this was not uniform across grades. This does not support a claim that every grade or every student group experienced above-state growth.

### G1-C — Graduation

**G1-C1 — Four-year graduation. Observation:** Riverview All Students four-year graduation rates were 87.64% (2018–19), 91.81% (2021–22), 93.58% (2022–23), 91.16% (2023–24), and 92.31% (2024–25). In 2024–25, Washington's corresponding rate was 82.64%, placing Riverview about 9.67 percentage points higher. Source datasets: `6iji-4nux`, `i23g-ymbg`, `kigx-4b2d`, `76iv-8ed4`, `isxb-523t`.

**Derived result:** The 2024–25 district rate was about 4.67 points above 2018–19, but below the district's 2022–23 value. The series therefore shows improvement relative to the pre-plan baseline with year-to-year fluctuation, not continuous annual improvement.

**Evaluation:** Positive graduation evidence; formal target attainment remains Cannot determine where no explicit numerical strategic-plan target is specified.

### G1-D — Achievement gaps / each and every student

For assessment gaps below, the measure is the 2024–25 exact-context subgroup minus All Students `percent_consistent_grade`. No grades, subjects, tests, or schools are averaged into a synthetic performance score; the median is reported only as a descriptive summary of the set of exact-context gaps.

**G1-D1 — Low-Income. Observation/derived result:** All 20 matched 2024–25 district assessment contexts for the `Low-Income` group were below All Students. The median gap was -27.0 percentage points, with observed exact-context gaps ranging from -35.3 to -12.0 points. Example: grade 3 ELA was 20.7% versus 54.8% All Students (-34.1 points), and grade 3 math was 24.1% versus 59.4% (-35.3 points). Source dataset: `h5d9-vgwi`; derived output: `goal1_subgroup_gaps.csv`.

**Evaluation:** Persistent material disparity in current assessment outcomes. This evidence does not support treating Goal 1B's achievement-gap concern as resolved.

**G1-D2 — Students with Disabilities. Observation/derived result:** Of 16 matched 2024–25 assessment contexts, 15 were below All Students and one was equal. The median gap was -34.8 percentage points; exact-context gaps ranged from -53.0 to 0.0 points. Grade 3 math was 26.3% versus 59.4% All Students (-33.1 points); grade 3 ELA was 21.1% versus 54.8% (-33.7 points).

**Evaluation:** Persistent material disparity.

**G1-D3 — English Language Learners. Observation/derived result:** Five unsuppressed matched 2024–25 assessment contexts were available for the English Language Learners group; all five were below All Students. Their median gap was -43.5 percentage points, with gaps from -51.3 to -39.7 points. Example: grade 4 ELA was 27.3% versus 68.4% All Students (-41.1 points), and grade 4 math was 22.7% versus 66.2% (-43.5 points). Suppressed contexts are not estimated.

**Evaluation:** The available unsuppressed evidence shows a large current disparity, but the smaller observable set and suppression require more caution than for the Low-Income group.

### G1-E — Implementation versus outcomes

District strategic-plan/SIP evidence documents implementation activities intended to support aligned curriculum, intervention, assessment, and subgroup improvement. These activities establish that work was undertaken; they do not by themselves establish that the work caused the outcome patterns above.

The outcome evidence is mixed in the sense relevant to the strategic goal: district-wide achievement and graduation compare favorably with Washington, and overall growth medians are slightly above the statewide median, while substantial Low-Income, Students with Disabilities, and English Learner disparities remain.

**Evaluation:** Implementation evidence should be reported separately from outcome attainment. Temporal coexistence of an initiative and an outcome change is not treated as causal evidence.

### G1-F — Overall Goal 1 determination

**Formal attainment: Cannot determine.** The strategic goal is directional — increasing growth of each and every student — but the reviewed plan does not provide a single numerical Goal 1 threshold that permits a reproducible Met/Not Met determination.

The evidence nevertheless supports several narrower findings:

- 2024–25 district All Students achievement was above Washington in every matched ELA, math, and science `percent_consistent_grade` comparison reviewed.
- 2024–25 All Grades median SGP was slightly above the statewide median in both ELA and math, with meaningful grade-level variation.
- Four-year graduation in 2024–25 was above both the 2018–19 district value and the 2024–25 Washington rate, while fluctuating during the plan period.
- Large current achievement disparities remain for Low-Income students, Students with Disabilities, and the observable English Learner assessment contexts.

Accordingly, the evidence supports **positive overall district outcomes alongside a persistent Goal 1B equity challenge**. This statement is descriptive of the measured outcomes and does not substitute an invented target for the strategic plan.


## Assertion evidence record

Each completed assertion must include:

| Field | Requirement |
|---|---|
| Assertion ID | Stable ID above |
| Strategic objective | Goal/objective text or documented challenge |
| Observation | Source-reported values/facts |
| Derived result | Reproducible calculation, if any |
| Evaluation | Outcome status or challenge direction |
| Evidence IDs | Dataset IDs / district document evidence IDs |
| Reporting periods | Exact periods used |
| Transformation | Script/output used for derived result |
| Limitations | Suppression, comparability, methodology, target, causality |
| Verification | How another evaluator can reproduce/test it |

## Data boundary

The generalized OSPI analytical layer is frozen. Do not add datasets, metrics, models, or exploratory transformations unless one of the assertions above exposes a specific unresolved evidence requirement.

The 2021–22 EL multi-year source period-integrity correction is complete. Raw/normalized acquisition remains preserved while analytical rows are constrained to the requested reporting period.

## Completion criteria

Goal 1 synthesis is complete when:
1. each required assertion is populated or explicitly marked Cannot determine;
2. every material numerical assertion has reproducible provenance;
3. suppressed/missing values are not converted to estimates;
4. assessment methodology changes are disclosed;
5. implementation evidence is not presented as outcome attainment;
6. an independent rerun can reproduce the cited derived values.
