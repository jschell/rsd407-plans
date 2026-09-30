#!/usr/bin/env python3
"""Write the OSPI collection report as GitHub Actions Markdown."""
from pathlib import Path
import os
import pandas as pd

report = Path("ospi_riverview/collection_report.csv")
summary = Path(os.environ["GITHUB_STEP_SUMMARY"])
with summary.open("a", encoding="utf-8") as out:
    out.write("## OSPI collection\n\n")
    if not report.exists():
        out.write("No collection report was produced.\n")
        raise SystemExit(0)
    df = pd.read_csv(report).fillna("")
    out.write(f"Validated: **{int((df.status == 'OK').sum())}/{len(df)}** required dataset-periods\n\n")
    out.write("| Family | Period | Dataset | Status | Scoped rows | Riverview rows |\n")
    out.write("|---|---|---|---|---:|---:|\n")
    for _, r in df.iterrows():
        out.write(f"| {r.family} | {r.period} | {r.dataset_id} | {r.status} | {r.scoped_rows} | {r.riverview_rows} |\n")
