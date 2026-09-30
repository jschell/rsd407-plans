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

The 2021–22 EL multi-year source must pass the period-integrity workflow before EL-derived assertions are populated.

## Completion criteria

Goal 1 synthesis is complete when:
1. each required assertion is populated or explicitly marked Cannot determine;
2. every material numerical assertion has reproducible provenance;
3. suppressed/missing values are not converted to estimates;
4. assessment methodology changes are disclosed;
5. implementation evidence is not presented as outcome attainment;
6. an independent rerun can reproduce the cited derived values.
