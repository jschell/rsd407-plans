# Plan 01 follow-up — EL period integrity and evidence synthesis

## Purpose

Close the remaining correctness issue before using Goal 1 derived outputs for evaluative findings. This is a bounded closeout task, not an expansion of the OSPI analytical framework.

## Scope

1. Inspect the 2021–22 English Learner source dataset (Socrata `3vhd-qaf3`), whose published title indicates it contains 2021–22 through the most current year.
2. Record the distinct source school years present in the normalized artifact.
3. Ensure analysis for source period `2021-22` includes only rows belonging to that requested reporting period. Preserve the acquired source artifact unchanged.
4. Add a regression check preventing a period-labelled analytical input from silently containing observations from other reporting periods.
5. Re-run the existing Goal 1 pipeline and verify acquisition, core indicators, WA comparisons, subgroup gaps, and longitudinal gap changes remain internally consistent.

## Evidence synthesis after correctness verification

Do not add further generalized datasets or transformations. Select only material indicators tied to Goal 1 / Goal 1B and construct approximately 10–20 evidence assertions.

Each assertion must contain:

- strategic-plan objective or documented challenge;
- observation(s);
- derived result(s);
- district-vs-Washington context where relevant;
- evaluation: met / partially met / not met / cannot determine, or persistent / narrowing / widening as appropriate;
- limitations and comparability notes;
- reproducible source dataset IDs, reporting periods, and transformation/output references.

Prioritize assessment achievement, growth, graduation, and district-identified achievement-gap groups. Treat enrollment as context and WSIF as corroboration rather than independent outcome universes.

## Stop condition

Plan 01 analytical development is frozen after the EL period-integrity correction. Additional data exploration requires a specific unresolved assertion in the evidence synthesis.

Plan 01 is complete when the selected assertions are independently reproducible from committed source/provenance and derived outputs and the Goal 1 evidence synthesis is committed.


## Closeout

**Status:** Complete.

Final validated analytical execution: GitHub Actions run `36744065183`, artifact `11111512770`, SHA-256 `a20428371aa7a9ed24d8fa6b48c57adde7025562fc798199dc022d07604a29f3`.

The run validated 29/29 required acquisitions and produced 22,215 district/WA comparisons, 16,684 district longitudinal changes, 13,783 core district/WA comparisons, 11,170 core longitudinal changes, 81,106 subgroup gaps, and 39,312 subgroup-gap changes. The final Goal 1 assertions are recorded in `docs/evaluations/goal-1-evidence-synthesis.md`.

Known limitations are retained in the synthesis rather than treated as unfinished engineering work, including assessment-release comparability, suppression, and the absence of a single numerical Goal 1 attainment threshold.
