# Research process and reproduction guide

This guide explains how to follow the completed research, trace a finding and reproduce its calculations. For the substantive conclusion and its implications, start with the [README](../README.md) and [cross-era evaluation](evaluations/cross-era-synthesis.md).

## Follow the research plans

Research work plans live in `docs/plans/active/`, `docs/plans/queue/` and `docs/plans/complete/`. These are the repository's work instructions; they are distinct from the district's strategic plans reconstructed in `docs/strategic-plans/`.

Plans 00–12 are complete within their declared evidence boundaries. No active or queued research remains. Each completed plan records its objective, outputs, verification and stopping rule. Completion means the research was performed and its gaps documented, not that district strategic goals were achieved.

The prior-iteration sequence is:

| Work plan | Output to follow |
| --- | --- |
| [08: Inventory and boundaries](plans/complete/08-prior-plan-inventory.md) | [Iteration inventory](strategic-plans/iteration-inventory.md) and [plan history](strategic-plans/plan-history.md) |
| [09: Early iterations](plans/complete/09-early-plan-iterations.md) | [Early-cycle evaluation](evaluations/early-plan-iterations.md) |
| [10: Middle-era reconstruction](plans/complete/10-middle-era-reconstruction.md) | [2014 bridge and 2015–2020 review](evaluations/middle-plan-iterations.md) |
| [11: 2020–2025 evaluation](plans/complete/11-plan-2020-2025-evaluation.md) | [2020–2025 review](evaluations/plan-2020-2025.md) |
| [12: Cross-era synthesis](plans/complete/12-cross-era-evaluation.md) | [Cross-era final evaluation](evaluations/cross-era-synthesis.md) and [machine-readable synthesis](../data/synthesis/cross-era-evaluation.json) |

The synthesis preserves 47 historical objective evaluations and seven current snapshot objectives. Twelve inventory candidates have either bounded reviews or insufficient-evidence closeouts; they are not twelve confirmed separate governing plans. Earlier reports' “next plan” passages describe historical handoffs; the completed plan files and final synthesis identify current status.

## Trace a finding to its evidence

1. Locate the assertion ID in a report, such as `TRANS-TARGET-03`, `FIN-04` or `CROSS-ELA-3`.
2. Open the synthesis's `assertion_index` entry. It supplies the originating file and JSON pointer or report locator. The broader narrative is in the linked domain or era report.
3. Follow the source IDs to `source_index` and the original records in `data/manifests/`. Inspect the publisher URL, source-byte hash, reporting period, physical page and preservation status where recorded. OSPI workflow provenance and selected values are also recorded in the analytical inputs and reports.
4. Inspect the preserved source values, formula and transformation script. Distinguish source observations, derived results and evaluator judgments.
5. Check the limitations and contrary evidence before accepting the conclusion. Reproducing a number does not require accepting the interpretation.

Generated synthesis entries point back into the synthesis and identify its builder; they do not carry a recursive self-hash. Imported files and source manifests have their recorded hashes. Shared sources and repeated pointers are not independent observations.

## Rebuild the cross-era synthesis

From a checkout of this repository, run the following commands at the repository root with Python 3. The synthesis builder uses only the Python standard library and performs no network acquisition.

```sh
git rev-parse HEAD
python scripts/build_cross_era_synthesis.py --output /tmp/rsd407-cross-era-evaluation.json
diff -u data/synthesis/cross-era-evaluation.json /tmp/rsd407-cross-era-evaluation.json
```

Record the commit returned by the first command. At the reviewed commit, a successful rebuild should produce no differences. The JSON records input hashes and retains the original historical evaluations, current domain findings, coverage, thematic crosswalk, version links, recurrence judgments and separate outcome-level/gap/Washington calculations.

This rebuild checks synthesis from committed inputs. It does not independently reacquire every source, reconstruct every PDF register or verify district implementation. Curated crosswalks and evaluation judgments still require independent examination.

## Reproduce the underlying evaluations

Use the reproduction sections and scripts identified by each report:

| Evidence area | Reproduction entry point |
| --- | --- |
| Early observations and turnover | [Early-cycle review](evaluations/early-plan-iterations.md#reported-outcomes-and-reproducible-changes) |
| Middle-era PDF registers, OSPI selection and calculations | [Middle-era reproduction](evaluations/middle-plan-iterations.md#reproduction-and-closure) |
| 2020–2025 register, selected OSPI values and diagnostics | [Transition reproduction](evaluations/plan-2020-2025.md#reproduction-verification-and-stop) |
| Current academic outcomes | [Goal 1 findings and workflow provenance](evaluations/goal-1-evidence-synthesis.md#findings-from-validated-ospi-run) |
| Current domain calculations and preservation | [Current-plan reproduction](evaluations/final-synthesis.md#reproduction-and-preservation) |

Read each script's input requirements before running it. PDF extraction and original workflow-artifact selection require the corresponding source files and any dependencies used by that script; they are not supplied by the standard-library synthesis rebuild.

Source PDFs were reviewed locally and are excluded from git. Manifests retain original URLs, SHA-256 hashes and archive results. Obtain the publisher or recorded archive bytes and verify their hashes before treating them as the reviewed source. `capture_verified` requires equality between reviewed original bytes and the archive replay. A viewer link, submitted capture request or different replay hash is not verified preservation.

Goal 1 records [Actions run 36744065183](https://github.com/jschell/rsd407-plans/actions/runs/36744065183), artifact 11111512770 and its hash. Workflow retention is finite. Committed selected values support recalculation; a fresh acquisition must receive new provenance and is not presumed byte-identical.

## Interpretation and provenance rules

- Record source, retrieval method/date, identifiers, reporting period and transformations for acquired data.
- Prefer authoritative primary sources; preserve source values before normalization.
- Give material assertions stable evidence IDs and separate observation, derived result and evaluation.
- Retain conflicting definitions and values rather than silently selecting a convenient one.
- Preserve suppression and missing values; never turn them into zeros.
- Separate task completion, implementation fidelity and outcome attainment.
- Separate outcome levels, focal-group gaps and Washington comparisons; do not invent a composite score or causal effect.
- Keep goal versions and deadlines distinct. Reused codes or related later tasks do not establish earlier completion.

See the [provenance standard](methodology/reproducibility.md), [evaluation framework](methodology/evaluation-framework.md) and [agent instructions](../AGENTS.md).

## Repository map

| Location | Contents |
| --- | --- |
| `docs/methodology/` | Evaluation and reproducibility rules |
| `docs/evidence/` | Evidence ledgers and provenance |
| `docs/evaluations/` | Domain, era and final evaluations |
| `docs/strategic-plans/` | District plan history and reconstruction |
| `docs/plans/active\|queue\|complete/` | Repository research work plans |
| `data/manifests/` | Source URLs, hashes and preservation records |
| `data/strategic-plans/` and `data/synthesis/` | Registers, preserved values, calculations and matrices |
| `scripts/` | Collection and transformation scripts |

## Reopening and corrections

Reopen only when a concrete authoritative artifact could materially change a conclusion: a governing register or revision, matched outcome and definition, dated implementation/fidelity record, or corrected calculation or source. The [final report](evaluations/cross-era-synthesis.md#completion-and-finite-reopening) gives the finite conditions.

For a correction, identify the assertion ID, provide the source and exact locator, explain the affected definition or calculation, and retain the previous observation alongside the correction. Update affected outputs and their hashes together, reproduce the relevant calculations, and commit the explanation. A new title, forecast or broadly available dataset alone does not restart collection.


## Track unresolved commitments across versions

[Plan 13](plans/complete/13-commitment-disposition-tracker.md) records this bounded tracker implementation and verification.

The [commitment disposition tracker](evaluations/commitment-disposition.md) separates original attainment from observed successor scope and formal decision/closure. Its curated review file records comparisons and evidence; its deterministic builder generates the JSON register and readable report. Follow that report's update procedure before changing a disposition. No entry closes automatically because a new plan omits it or related work continues. This is a bounded69-entry register of54 objectives,14 metrics and one bond criterion, with overlapping units rather than a complete task census.

```sh
python scripts/build_commitment_disposition.py
python -m unittest discover -s tests -p test_commitment_disposition.py
```
