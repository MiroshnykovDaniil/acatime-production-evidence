# Reproducing the aggregate checks

```bash
python3 scripts/verify_aggregates.py
```

Expected output includes:

```text
rows: 17
min: 22.4114
max: 80.7947
median: 43.2971
all checks passed
```

This verifies the published arithmetic and checksums. It does not rerun the
production scheduler, because the production input data is private.
