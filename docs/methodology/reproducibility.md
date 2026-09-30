# Reproducibility and Provenance Standard

## Required provenance

Every acquired dataset or document must record:

- source/evidence ID;
- publisher;
- title;
- canonical URL;
- retrieval date;
- reporting period;
- organization/entity identifiers;
- dataset/resource ID where applicable;
- retrieval method (API, CSV export, PDF, Board packet, etc.);
- raw artifact name or immutable reference;
- transformation script/version;
- known suppression, comparability, or extraction limitations.

## Evidence IDs

Use stable IDs such as:

- `OSPI-ASSESS-2024-25`
- `OSPI-GRAD-2024-25`
- `SAO-RSD407-2025-FIN`
- `RSD407-SP-2025-JUL`

Evaluations cite these IDs. Evidence ledgers map IDs to sources.

## Three evidence layers

### Observation
A fact represented directly by the source.

### Derived result
A deterministic calculation from observations. Record formula and inputs.

### Evaluation
A judgment under the documented evaluation framework. Record supporting evidence IDs and contrary/limiting evidence.

## Reproduction requirement

A second evaluator should be able to:
1. locate the same source;
2. retrieve or inspect the same source values;
3. rerun transformations/calculations;
4. obtain the same derived result;
5. independently accept or dispute the evaluation.

## Conflicts

When sources disagree:
- retain both observations;
- identify source hierarchy;
- test differences in period/definition/aggregation;
- do not silently choose a preferred number.

## Data retention

Where licensing/public-access rules permit:
- retain raw downloads unchanged;
- generate normalized/derived files separately;
- never overwrite raw source data.
