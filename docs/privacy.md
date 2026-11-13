# Privacy and scope

The actual AcaTime production dataset is not public. It contains:

- student groups and subgroup variants;
- teachers and teaching assignments;
- real rooms and room constraints;
- institution-specific scheduling rules;
- complete faculty schedules.

Those data are not included in this repository. This release contains only
aggregate run results: scores, improvement percentages, durations and exit codes.

No student names, teacher names, group names, course names or schedule cells are
published. The published logs are sanitized: server addresses, paths and
institution-specific rule names are removed or replaced; see
`docs/log-sanitization.md`.

## What the aggregate data can and cannot prove

It can prove that the 17 validation runs were recorded and that the 22–81% range,
median and per-run percentages are computed correctly from the published scores.

It cannot prove that the exact production instance is reproducible, because the
input schedule and rules are withheld. That is why this is labelled
**aggregate evidence**, not a full reproduction package.

A future v0.2 may add an anonymised dataset if the university approves the
anonymisation and the result is checked for re-identification risk.
