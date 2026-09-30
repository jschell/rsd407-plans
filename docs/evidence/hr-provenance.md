# HR evidence provenance

Three primary PDFs were retrieved from exact Board portal URLs, reviewed locally, and registered in `data/manifests/hr-sources.json` with original-byte SHA-256, length and Internet Archive submission/capture results. Original PDFs are excluded from git. Existing strategic sources are reused from the allocation manifest. Evidence IDs and 1-based physical pages are cited in HR-01–HR-07.

Reproduce with `python scripts/finance_evidence.py retrieve --manifest data/manifests/hr-sources.json --destination data/raw/finance` and `python scripts/finance_evidence.py verify --manifest data/manifests/hr-sources.json --destination data/raw/finance`. The commands process the selected manifest; use `--archive` only for sources with verified captures. `pdftotext -layout` extracts review text; visually inspect tables and cited physical pages. Archived claims require original-byte hash match, not just a submission response.

Read-only portal search/search-details queries `Human Resources`, `retention`, `paraeducator`, `grow your own`, `hiring`, `onboarding` reviewed the first 30 returned IDs per query on September 30, 2026. Queries are leads, not an exhaustive inventory; non-discovery does not establish nonexistence. Separate the search's district student-promotion retention results from employee retention. Do not infer actual staff demographics from names or personnel-action lists.

Policy 5000 pp1–2, procedure 5010-P1 physical pp1–2/25 and Pathways slides pp2–6 reviewed. Historical demographic table p2, shortage slide p3 and July strategic p10 also visually inspected. Procedure's appended sections repeat printed page labels; use physical p25 for revision footer. Event year is not on the December 2 slide. Preserve this uncertainty.

No historical workforce table is treated as current; recruitment-pool comparisons are distinct from student-demographic comparisons. No staff records or individual complaint analysis are collected. Preservation gaps remain explicit in manifest; PDF review and hashing are independent of archive success.
