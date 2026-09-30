# Finance evidence and reproduction

Plan 02 is in progress. Sources are identified in `data/manifests/finance-sources.json` by exact URL, report/document ID, publisher, period, retrieval timestamp, byte count and SHA-256. PDFs are reviewed locally and are **not stored in the repository**. Internet Archive request outcomes are recorded individually; a submission attempt is not a confirmed capture.

## Reproduce

Python standard library only, from the repository root:

```sh
python scripts/finance_evidence.py calculate --output /tmp/finance-derived.json
python scripts/finance_evidence.py retrieve --destination /tmp/rsd407-finance-review
python scripts/finance_evidence.py verify --destination /tmp/rsd407-finance-review
```

To request and hash-verify Internet Archive captures (writes a separate result file; does not silently update the manifest):

```sh
python scripts/archive_finance_sources.py --output /tmp/finance-archive-results.json
```

For retrieval, `finance_evidence.py retrieve --archive --destination /tmp/rsd407-archived-review` uses verified captures and fails if any source lacks one.

Use `--evidence-id SAO-RSD407-2025-FIN` to retry one source. Copy only inspected results into the manifest. A returned capture URL is marked verified only if the archived original PDF bytes match the observed SHA-256. A mismatch or failed request remains unresolved.

Use a fresh destination for retrieval: existing files are never overwritten. A hash mismatch fails verification and must be investigated, not accepted as the original snapshot. Calculations run offline from the committed source-value transcription; validating the transcription requires re-fetching matching PDFs or retrieving a matching confirmed archive. If neither is available, source-level reproduction is blocked even though arithmetic can still be reproduced.

Inspect the original PDF pages listed in `data/finance/observations.json`; page numbers mean 1-based physical PDF pages, not slide labels. `pdftotext -layout` can aid review, but FY2024 financial tables contain defective text encoding and must be inspected visually. Values were manually transcribed; no automatic extraction accuracy is claimed. Decimal strings preserve source precision. The script calculates total balance / expenditures and consecutive audited total-balance changes; it does not substitute those measures for unassigned reserve or policy compliance.

## Source inventory

| Evidence ID | Publisher / artifact | PDF pages used |
|---|---|---|
| SAO-RSD407-2023-FIN | SAO report 1034676 | 5 (findings), 20 (unassigned), 22 (totals) |
| SAO-RSD407-2024-FIN | SAO report 1037045 | 5 (findings), 22 (totals), 46 (motion/policy note) |
| SAO-RSD407-2025-FIN | SAO report 1039403 | 5 (findings), 19 (unassigned), 21 (totals), 46 (policy note) |
| SAO-RSD407-2023-ACC | SAO report 1034678 | 4 (selected-area results and scope) |
| SAO-RSD407-2024-ACC | SAO report 1037066 | 4 (selected-area results and scope) |
| SAO-RSD407-2025-ACC | SAO report 1039416 | 4 (selected-area results and scope) |
| RSD407-FY2024-YE | District year-end presentation | 3 (dashboard) |
| RSD407-FY2026-BUDGET-SUMMARY | District budget summary | 5 (General Operating column) |
| RSD407-SP-2024-SEP | District strategic-plan status | 8 (Goal 2A task 2) |
| RSD407-FY2026-BUDGET-PRESENTATION | District budget presentation | 3 (budget objective) |

Exact downloadable URLs and hashes reside in the manifest. The 2025-26 budget documents describe estimates; they are not FY2026 audited outcomes. No graph values are digitized.

## Preservation status at this checkpoint

Nine of ten source captures have been hash-verified. The FY2026 budget-summary capture request returned HTTP 404; it remains an explicit preservation gap. Do not mark Plan 02 fully reproducible until this source is preserved or a verified equivalent is obtained. The publisher URL remains available for hash-checked retrieval.
