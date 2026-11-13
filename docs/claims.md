# Claims and evidence

## The 22–81% claim

The paper reports:

> 17 validation runs improved the best Default schedule by 22–81%.

Evidence:

- `runs.csv`: 17 rows from the 2026-09-02 validation session;
- `summaries/*.csv`: the original per-run summary files;
- `scripts/verify_aggregates.py`: recomputes the range, median and per-run
  percentages;
- `logs/`: sanitized, gzip-compressed logs for all 17 runs.

Measured values:

| Metric | Value |
|---|---:|
| runs | 17 |
| minimum | 22.4114% |
| maximum | 80.7947% |
| median | 43.2971% |
| mean | 47.5134% |
| failed runs | 0 |

## The representative-run claim

The separate `199,180 → 256,450 (+28.7%)` run is **not** part of this release.
It was a separate production/API run, and its raw log is not in the current
evidence package. The same applies to the `+33%` run.

Therefore:

- this DOI supports the **22–81%** claim only;
- do not cite it as proof of `199,180 → 256,450` or `+33%`;
- those runs require their own recovered records before being added.

## Source

The 17 runs come from these `benchmark-results` directories:

```text
20260902-012136   5 runs
20260902-013359   5 runs
20260902-014708   5 runs
20260902-010032   1 run
20260902-010500   1 run
```

The range and median are computed only from these 17 rows.
