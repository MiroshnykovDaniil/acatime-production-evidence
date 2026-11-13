#!/usr/bin/env python3
"""Create sanitized gzip logs for the 17 validation runs.

The source logs are in the internal AcaTime workspace and are not part of this
repository. This script documents the sanitization applied before publication.
"""

from __future__ import annotations

import gzip
import hashlib
import json
import re
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = Path(os.environ["ACATIME_BENCHMARK_RESULTS"])
SOURCES = [
    "20260902-012136",
    "20260902-013359",
    "20260902-014708",
    "20260902-010032",
    "20260902-010500",
]
OUT = ROOT / "logs"
MANIFEST = OUT / "MANIFEST.json"


def sanitize(text: str) -> str:
    # Remove local server addresses and any URL.
    text = text.replace("http://localhost:5129/", "[server]")
    text = re.sub(r"https?://\S+", "[url]", text)

    # Replace local paths.
    text = re.sub(r"/Users/\S+", "[path]", text)

    # Learn rule names from the cheap-eval registration lines and replace them.
    rule_names = dict(
        re.findall(r"CheapEval: правило (\d+) '([^']+)'", text)
    )
    for rule_id, name in rule_names.items():
        text = text.replace(name, f"rule_{rule_id}")

    # Fallback for rule-name lines of the form:
    #   [0] Some rule name - 108 - -20040
    text = re.sub(
        r"(\[0\]\s+)[^-\n]+?(\s+-\s+(\d+)\s+-)",
        lambda m: m.group(1) + f"rule_{m.group(3)}" + m.group(2),
        text,
    )

    # Keep the term generic; no institution-specific semester label.
    text = text.replace("2025-2026 1й сем.", "[semester]")
    return text


def main() -> int:
    OUT.mkdir(exist_ok=True)
    manifest = []
    for source in SOURCES:
        src_dir = SOURCE_ROOT / source
        dst_dir = OUT / source
        dst_dir.mkdir(parents=True, exist_ok=True)
        for src in sorted(src_dir.glob("run-*.log")):
            raw = src.read_text(errors="ignore")
            clean = sanitize(raw)
            dst = dst_dir / f"{src.stem}.log.gz"
            with gzip.open(dst, "wt", encoding="utf-8") as f:
                f.write(clean)
            manifest.append(
                {
                    "source": str(src.relative_to(SOURCE_ROOT)),
                    "output": str(dst.relative_to(ROOT)),
                    "source_sha256": hashlib.sha256(src.read_bytes()).hexdigest(),
                    "output_sha256": hashlib.sha256(dst.read_bytes()).hexdigest(),
                }
            )
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"wrote {len(manifest)} sanitized logs to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
