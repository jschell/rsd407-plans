# Communications source provenance

New PDFs are registered in `data/manifests/communications-sources.json`; the portal-rendered audit summary HTML is separately registered in `data/manifests/communications-audit-html.json`. Each records exact retrieved URL, original-response SHA-256/length, format, extraction/review limitations and Internet Archive attempt. Original responses are not committed. Strategic sources reuse allocation manifest evidence IDs.

PDF reproduction: `python scripts/finance_evidence.py retrieve --manifest data/manifests/communications-sources.json --destination data/raw/finance`, then `verify` with the same options. Extract with `pdftotext -layout`. All PDF pages are physical; written-plan p6/p14 also visually reviewed.

Audit format exception: resource 5986 portal search reports `.pptx` and a `/home/public/document/5986` link, while the downloaded `/document/5986/` response is rendered HTML. The PDF-only helper intentionally does not process it. Retrieve that exact URL with an HTTP client, save response bytes as `.html`, and compare SHA-256/byte count to the separate manifest. Parse HTML text and inspect embedded image charts. Capture claims require the archived original HTML bytes to match; changed server HTML may prevent reproduction and is an explicit preservation limitation. This is not recovery of the original PPTX or full audit report.

Read-only portal searches `NSPRA`, `Communications Plan`, `Metrics`, `Ambassador` reviewed first 30 detail results per query September 30, 2026. These lead searches are not an exhaustive public inventory. Audit text headings and embedded parent/staff channel and SWOT charts reviewed. No numerical survey inference made without respondent denominators or sampling details. Plan p5–6/8/11/14 and presentation pp11–13 reviewed for channel descriptions, measurement claim and conflicts.

The 133% download claim is source-reported, not derived. Text labels/cadences and future deadlines are preserved. Capture failures/mismatches do not invalidate local content review but remain preservation gaps.
