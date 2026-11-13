#!/usr/bin/env python3
"""Verify the aggregate 17-run evidence package."""

from __future__ import annotations

import csv
import hashlib
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "runs.csv"
MANIFEST = ROOT / "summaries" / "MANIFEST.json"
LOG_MANIFEST = ROOT / "logs" / "MANIFEST.json"

EXPECTED_ROWS = 17
EXPECTED_MIN = 22.4114
EXPECTED_MAX = 80.7947
EXPECTED_MEDIAN = 43.2971


def main() -> int:
    rows = list(csv.DictReader(RUNS.open(newline="")))
    assert len(rows) == EXPECTED_ROWS, f"expected 17 runs, got {len(rows)}"

    percentages = []
    for row in rows:
        default = int(row["default_score"])
        genetic = int(row["genetic_score"])
        delta = int(row["delta"])
        percent = float(row["percent"])
        assert delta == genetic - default, f"delta mismatch: {row}"
        expected = delta / default * 100
        assert abs(expected - percent) < 0.001, f"percent mismatch: {row}"
        assert int(row["exit_code"]) == 0, f"failed run: {row}"
        percentages.append(percent)

    mn = min(percentages)
    mx = max(percentages)
    med = statistics.median(percentages)
    mean = statistics.mean(percentages)
    assert abs(mn - EXPECTED_MIN) < 0.001
    assert abs(mx - EXPECTED_MAX) < 0.001
    assert abs(med - EXPECTED_MEDIAN) < 0.001

    manifest = json.loads(MANIFEST.read_text())
    for entry in manifest:
        path = ROOT / entry["file"]
        assert path.exists(), f"missing summary: {path}"
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        assert digest == entry["sha256"], f"checksum mismatch: {path}"

    log_manifest = json.loads(LOG_MANIFEST.read_text())
    assert len(log_manifest) == EXPECTED_ROWS, "expected 17 sanitized logs"
    for entry in log_manifest:
        path = ROOT / entry["output"]
        assert path.exists(), f"missing sanitized log: {path}"
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        assert digest == entry["output_sha256"], f"log checksum mismatch: {path}"

    print(f"rows: {len(rows)}")
    print(f"min: {mn:.4f}")
    print(f"max: {mx:.4f}")
    print(f"median: {med:.4f}")
    print(f"mean: {mean:.4f}")
    print("all checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
