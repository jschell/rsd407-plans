# Plan 01 — OSPI Outcome Analysis

## Objective
Produce a reproducible longitudinal Goal 1 outcome dataset.

## Inputs
OSPI assessment, growth, graduation, SQSS, English Learner, enrollment, and WSIF datasets.

## Requirements
- preserve raw rows and suppression;
- record dataset IDs and retrieval metadata;
- filter Riverview using org ID 100222 / district 17407;
- retain Washington comparisons;
- retain relevant schools/student groups;
- normalize separately from raw data;
- calculate absolute change, WA-relative change, focal-group change, and gap change.

## Verification
An independent evaluator can rerun the collector and reproduce every derived Goal 1 metric.

## Completion
Move to `complete` only after source files, normalized outputs, calculations, and assertions are committed.


## GitHub Actions execution

Collection now runs through `.github/workflows/ospi-collect.yml` using manual `workflow_dispatch`.

The workflow:
- installs pinned dependencies from `requirements-ospi.txt`;
- runs `scripts/pull_ospi_riverview.py`;
- uploads raw/normalized rows, collection report, run manifest, and ZIP for 90 days;
- preserves artifacts even on collector failure;
- fails the job if any required dataset does not validate.

The run manifest records retrieval timestamp, Git commit/run ID, Python version, district identifiers, source hosts, and SHA-256 hashes of collected artifacts.

An independent evaluator can rerun the workflow at the same commit and compare the collection report and hashes.
