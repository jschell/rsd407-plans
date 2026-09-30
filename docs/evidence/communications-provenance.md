# Communications source provenance

New PDFs are registered in `data/manifests/communications-sources.json`; the portal-rendered audit summary HTML is separately registered in `data/manifests/communications-audit-html.json`. Each records exact retrieved URL, original-response SHA-256/length, format, extraction/review limitations and Internet Archive attempt. Original responses are not committed. Strategic sources reuse allocation manifest evidence IDs.

PDF reproduction: `python scripts/finance_evidence.py retrieve --manifest data/manifests/communications-sources.json --destination data/raw/finance`, then `verify` with the same options. Extract with `pdftotext -layout`. All PDF pages are physical; written-plan p6/p14 also visually reviewed.

Audit format exception: resource 5986 portal search reports `.pptx` and a `/home/public/document/5986` link, while the downloaded `/document/5986/` response is rendered HTML. The PDF-only helper intentionally does not process it. Retrieve that exact URL with an HTTP client, save response bytes as `.html`, and compare SHA-256/byte count to the separate manifest. Parse HTML text and inspect embedded image charts. Capture claims require the archived original HTML bytes to match; changed server HTML may prevent reproduction and is an explicit preservation limitation. This is not recovery of the original PPTX or full audit report.

Read-only portal searches `NSPRA`, `Communications Plan`, `Metrics`, `Ambassador` reviewed first 30 detail results per query September 30, 2026. These lead searches are not an exhaustive public inventory. Audit text headings and embedded parent/staff channel and SWOT charts reviewed. No numerical survey inference made without respondent denominators or sampling details. Plan p5–6/8/11/14 and presentation pp11–13 reviewed for channel descriptions, measurement claim and conflicts.

The 133% download claim is source-reported, not derived. Text labels/cadences and future deadlines are preserved. Capture failures/mismatches do not invalidate local content review but remain preservation gaps.

## Final bounded review

Read-only queries `communications update`, `end of year`, `website`, `Communications 2024`, `communications metrics` reviewed first 30 detail IDs per query. Followed the end-of-year report, separate October presentation record, November ambassador lead and September 2026 communications-update lead. Four additional PDF originals recorded with exact URLs/hashes/archive outcomes. Report pp3–7 visually reviewed because counts/charts are images missing from text extraction; other cited pages reviewed in text. No pixels were used to infer unlabelled podcast bar counts.

Reproduce screenshot arithmetic with `python scripts/communications_evidence.py`; compare output to `data/communications/derived.json`. Input preserves screenshot values, K rounding, printed period labels and exact source/page. Baseline-denominator growth and ending-denominator shares are explicitly different. Arithmetic does not cure unverified snapshot-window comparability, analytics filtering or unique-person definitions. In particular `unique visitors` and `new visitors` are distinct; platform usage is not district residents reached. No summed multi-platform audience or inferred podcast total.
