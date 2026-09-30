# Safety evidence provenance

Four reviewed PDFs resolve through `data/manifests/safety-sources.json`, with original URL, document ID, entity, period, byte count, SHA-256, extraction method and limitations. Original PDFs are not committed. Task chronology reuses September 2024 from the finance manifest and July 2025/September 2026 from the allocation manifest. Archive outcomes are per-source; failed requests remain gaps.

From repository root, using a fresh destination:

```sh
python scripts/finance_evidence.py retrieve --manifest data/manifests/safety-sources.json --destination /tmp/rsd407-safety-review
python scripts/finance_evidence.py verify --manifest data/manifests/safety-sources.json --destination /tmp/rsd407-safety-review
python scripts/archive_finance_sources.py --manifest data/manifests/safety-sources.json --output /tmp/rsd407-safety-archive-results.json
```

Retrieval never overwrites prior bytes. `--archive` requires each capture to be hash-verified; a submission is not preservation. Render cited pages with `pdftoppm` and review alongside extracted text. EOP adoption placeholders are preserved and separately resolved through the recorded Board motion; the published 2019 HIB version remains explicitly historical until latest-version reconciliation. The EOP's procedural requirements and general assertions are distinguished from completed drill/training records.

Discovery used the public portal search/details recipe recorded in allocation provenance, with terms key card, RFID, Threat Assessment, CPS, and Emergency Operations Plan. Up to 30 initial returned IDs per term were reviewed as leads, not a census. Search results do not establish artifact absence. No raw student incident records are gathered.
