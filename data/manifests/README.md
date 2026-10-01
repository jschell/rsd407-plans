# Data Manifests

Store machine-readable provenance here.

Each dataset manifest should include source ID, publisher, canonical URL, dataset/resource ID, reporting period, retrieval timestamp, retrieval method, raw artifact, transformation script/version, organization identifiers, and limitations.

`iteration-sources.json` records the prior-plan inventory's acquired HTML/PDF sources. Historical `retrieval_url` values are Wayback `id_` original-byte replays; SHA-256 describes reviewed replay bytes, not a live-original comparison. `internet_archive` records new save submissions separately from existing captures. Re-fetch the retrieval URL (or `url` for live sources), run `sha256sum`, and compare `sha256` before using the cited pages. The current September 2024 PDF reuses `RSD407-SP-2024-SEP` from `finance-sources.json`. No original PDFs are committed. Search result hashes and exact bounded archive queries are in `data/strategic-plans/inventory-search-log.json`.

`early-plan-sources.json` records eight original district Board PDFs retrieved through Wayback and one district-authored entry report hosted by WASA. Re-fetch `retrieval_url` where present, otherwise `url`, and verify SHA-256 before reviewing cited PDF pages. Archived bytes were hashed without a live-original comparison; all new capture submission failures remain separate. Scope and immutable search-index response are in `data/strategic-plans/early-search-log.json`. Turnover inputs/output are reproducible with `python scripts/early_turnover.py`; percentages are Board reports with unavailable counts/denominators, not independently audited retention outcomes.
