# AcaTime production validation evidence

Aggregate, privacy-preserving evidence for the faculty-scale results reported in
the TAAPSD 2026 paper:

> **ACATIME HYBRID GENETIC ALGORITHM FOR UNIVERSITY COURSE TIMETABLING**

**Archived version:** `v0.1.0` — DOI [10.5281/zenodo.24199144](https://doi.org/10.5281/zenodo.24199144)  
**Concept DOI:** [10.5281/zenodo.24199143](https://doi.org/10.5281/zenodo.24199143)

**Status:** v0.1, aggregate-only. The raw faculty data and raw schedules are not
included because they contain institutional and personal information.

## What this release covers

This release contains the **17 validation runs** from 2026-09-02:

- faculty-scale dataset: 830 student groups, 7,485 lesson slots;
- 17 runs, all successful (`exit_code = 0`);
- improvement over the Default schedule: **22.41%–80.79%**;
- median improvement: **43.30%**;
- mean improvement: **47.51%**.

Every run improved the Default schedule. The per-run source summaries are in
`summaries/`; the consolidated table is `runs.csv`. Sanitized, gzip-compressed
logs for all 17 runs are in `logs/`.

## What this release does not cover

It does **not** include:

- raw production schedules, students, teachers, rooms or rules;
- the separate representative production/API run reported as
  `199,180 → 256,450 (+28.7%)`;
- the `186,550 → 247,750 (+33%)` run;
- the later anonymised production dataset.

Those runs are not part of the 17-run validation set and are not claimed as
verified here. A future v0.2 may add an anonymised production dataset and the
representative runs once their records are recovered and cleared for release.

## Files

```text
runs.csv                  consolidated 17-run results
summaries/                original per-run summary.csv files
summaries/MANIFEST.json   source paths and SHA-256 checksums
configs/                  shared GA parameters
docs/claims.md            claim-to-evidence map
docs/privacy.md           what is withheld and why
docs/provenance.md        source and checksum details
scripts/verify_aggregates.py
logs/                     sanitized run logs (gzip)
```

## Verify

```bash
python3 scripts/verify_aggregates.py
logs/                     sanitized run logs (gzip)
```

It checks:

- exactly 17 rows;
- every `percent` equals `delta / default_score * 100`;
- the reported 22–81% range and median;
- SHA-256 checksums of the copied summary files;
- the sanitized-log manifest and hashes.

## Code

The public AcaTime GA/ITC code is in:

<https://github.com/MiroshnykovDaniil/acatime-itc2019>

The production AcaTime backend and the faculty dataset are not public.

## License

- Aggregate data, logs and documentation: **CC BY 4.0**.
- Verification scripts: **Apache-2.0**.

See `LICENSE` and `LICENSES.md`.
