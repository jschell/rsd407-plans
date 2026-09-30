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
