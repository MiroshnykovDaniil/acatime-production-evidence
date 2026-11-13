# Sanitized run logs

This directory contains **gzip-compressed, sanitized logs** for the 17 validation
runs.

Inspect one:

```bash
gzip -dc logs/20260902-012136/run-1.log.gz | less
```

Sanitization:

- removed the local server address and any URLs;
- removed local filesystem paths;
- replaced institution-specific rule names with `rule_<id>`;
- replaced the semester label with `[semester]`;
- kept algorithm parameters, scores, iteration counters and exit information.

No student, teacher, group or course names are included.

`MANIFEST.json` records the SHA-256 of each sanitized file and of its internal
source log. The raw logs remain in the internal AcaTime workspace.

The representative `199,180 → 256,450` run is not in this 17-run validation set.
