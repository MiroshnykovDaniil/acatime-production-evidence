# Provenance

## Source

The per-run summaries were copied from the internal AcaTime benchmark workspace:

```text
benchmark-results/20260902-012136/
benchmark-results/20260902-013359/
benchmark-results/20260902-014708/
benchmark-results/20260902-010032/
benchmark-results/20260902-010500/
```

Only `summary.csv` files were copied into `summaries/`. The 17 run logs were
sanitized and gzip-compressed into `logs/`. Raw run logs, schedules, and production
data are not included.

## Checksums

`summaries/MANIFEST.json` records the source directory, copied file and SHA-256
for every summary. `scripts/verify_aggregates.py` checks those hashes.

## Configuration

`configs/validation-config.json` documents the shared GA parameters extracted
from the validation run logs. Dynamic values (evaluation timings, operation
counters and the local server address) are excluded.

The 17 summaries are the authoritative per-run records; the config file is
supporting context, not a substitute for the source logs.
