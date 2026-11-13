# Log sanitisation

The internal `run-*.log` files are not published verbatim. The public copies are
gzip-compressed after the following transformations:

1. `http://localhost:5129/` → `[server]`
2. any `http(s)://...` → `[url]`
3. `/Users/...` paths → `[path]`
4. institution-specific rule names → `rule_<rule-id>`
5. `2025-2026 1й сем.` → `[semester]`

Retained:

- algorithm parameters;
- score progression;
- iteration and mutation counts;
- final scores and runtimes;
- exit information.

The `scripts/sanitize_logs.py` script documents the exact transformation. It
requires `ACATIME_BENCHMARK_RESULTS` to point at the internal benchmark-results
directory; the public repo does not contain that directory.

## What is not present

No student, teacher, group or course names are present in the logs. No raw
schedule cells are included.
