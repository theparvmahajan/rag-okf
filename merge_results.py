#!/usr/bin/env python3
"""
Merge a re-run subset of results (e.g. the 35 previously-empty-answer
questions, rerun after the generator fix) back into the original full
results file, so you end up with one complete, corrected results file
instead of two partial ones.

Records in --patch overwrite records with the same id in --base. Order
follows --base (i.e. the original eval-set order). Any id present in
--patch but not --base is appended at the end.

Usage:
    python3 merge_results.py \
        --base eval_runs/baseline_qwen35_4b_before_token_fix.jsonl \
        --patch eval_runs/baseline_qwen35_4b_fixed35.jsonl \
        --output eval_runs/baseline_qwen35_4b_merged.jsonl
"""
import argparse
import json
from pathlib import Path


def load(path: Path) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base", required=True, help="Original full results file")
    ap.add_argument("--patch", required=True, help="Rerun results for the previously-failed subset")
    ap.add_argument("--output", required=True, help="Where to write the merged file")
    args = ap.parse_args()

    base = load(Path(args.base))
    patch = load(Path(args.patch))
    patch_by_id = {r["id"]: r for r in patch}

    merged = []
    replaced = 0
    for r in base:
        if r["id"] in patch_by_id:
            merged.append(patch_by_id.pop(r["id"]))
            replaced += 1
        else:
            merged.append(r)
    appended = list(patch_by_id.values())  # any patch ids not present in base at all
    merged.extend(appended)

    still_empty = [r["id"] for r in merged if r.get("error") is None and not r.get("answer")]
    errors = [r["id"] for r in merged if r.get("error")]

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        for r in merged:
            f.write(json.dumps(r) + "\n")

    print(f"Merged {len(base)} base + {len(patch)} patch -> {len(merged)} records")
    print(f"  replaced: {replaced}")
    if appended:
        print(f"  appended (id only in patch): {[r['id'] for r in appended]}")
    print(f"Wrote: {args.output}")
    if still_empty:
        print(f"\nStill empty-answer after merge ({len(still_empty)}): {still_empty}")
    if errors:
        print(f"Generation errors after merge ({len(errors)}): {errors}")
    if not still_empty and not errors:
        print("\nAll records have a non-empty answer with no error.")


if __name__ == "__main__":
    main()
