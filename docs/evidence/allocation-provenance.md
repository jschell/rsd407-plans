# Resource allocation evidence provenance

Sources in `data/manifests/allocation-sources.json` retain exact URL, publisher/document ID, entity, period, original byte hash/count, extraction method and limitations. PDFs are locally reviewed and not committed. September 2024 baseline reuses RSD407-SP-2024-SEP in the finance manifest. Both text extraction and visual review support cited pages. The bargaining PDF contains tracked changes; source authority is not final adoption authority.

## Reproduce

From repository root:

```sh
python scripts/finance_evidence.py retrieve --manifest data/manifests/allocation-sources.json --destination /tmp/rsd407-allocation-review
python scripts/finance_evidence.py verify --manifest data/manifests/allocation-sources.json --destination /tmp/rsd407-allocation-review
python scripts/archive_finance_sources.py --manifest data/manifests/allocation-sources.json --output /tmp/rsd407-allocation-archive-results.json
```

Use a fresh destination: retrieval never overwrites existing files. Local reviewed originals must match byte count and SHA-256; changed upstream bytes are a new version, not a silent replacement. `retrieve --archive` requires a hash-verified capture for every selected source. Archive results are authoritative per source: a request is not a verified capture. Record failed requests as preservation gaps. Do not copy results into the manifest without inspection.

## Discovery boundary

Public portal read-only search: `GET https://rsd407.community.diligentoneplatform.com/Services/ItemsService.svc/portal/search?criteria=strategic+plan&showDocuments=true&showTrackerItems=false&showMeetingItems=true`, followed by read-only search-details POST at `/Services/ItemsService.svc/portal/search/details` with the same query parameters, JSON body containing returned numeric IDs. Queries used: strategic plan, severity matrix, staffing, Financial Recovery. Search results are leads; assertions cite exact reviewed PDFs. No-result or omitted result does not establish absence of an artifact.

July 2025 completion assertions were reviewed visually on physical p7, January 2025 on p7, September 2026 on p6, bargaining tracked changes on p54, and recovery overview on pp21/23. Additional discovered updates not used for assertions are not represented as committed reviewed evidence.

## Decision-review extension

Two additional originals are registered: September 9, 2025 Draft minutes packet (pp4–5), and three-page Resolution 25-02. The existing finance-manifest May 13 packet RSD407-MOTION-25-65 supplies motion **25-60** (p5), resolution (pp140–142), and Exhibit A (p143). Evidence IDs identify exact documents; a packet ID named for one motion can contain other separately cited motions. Both packets retain Draft qualifiers.

The numeric CBA URL `/document/12156/` matches the previously registered UUID bytes exactly. Its p126 contains image-only weighting tables, manually transcribed after rendering, not missing fields or an empty matrix. Page125 alone contains a heading and cannot stand for the whole exhibit. Service-time boundary ambiguity is retained. Specialist FTE calculation reproduces with:

```sh
python scripts/allocation_evidence.py
```

This produces `data/allocation/derived.json`'s contents; source heading and line items remain distinct. Search details were inspected for up to 40 initial returned IDs for each extension query; broad absence is not asserted. The search recipe is unchanged, with queries REA agreement, severity, staff allocation, 2025-2027, additional support.
