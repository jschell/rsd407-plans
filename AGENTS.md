# Agent Instructions

All research in this repository must be independently testable.

1. Record provenance for every externally acquired datum.
2. Prefer authoritative primary sources.
3. Preserve source values before normalization.
4. Never turn suppression/missing values into zero.
5. Give every material assertion an evidence ID.
6. Distinguish:
   - observation: directly supported by source;
   - derived result: reproducible calculation;
   - evaluation: interpretation under documented criteria.
7. Record conflicts rather than silently resolving them.
8. Do not infer task completion equals outcome achievement.
9. Keep plans in `docs/plans/active`, `queue`, or `complete`.
10. A plan is complete only when its evidence and outputs are committed and its verification criteria are satisfied.
