#!/usr/bin/env python3
"""Reusable completeness scanner for PRD markdown files.

Usage:
    python verify-prd.py <path-to-prd.md> [section-prefix=F-] [max-id=NN]

Checks:
  1. Placeholder tokens (TODO/TBD/lorem/isi nanti/...).
  2. Feature-ID sequence (e.g. F-01..F-43) present and in order.
  3. Optionally greps leftover-concept terms passed after '--'.
Example:
    python verify-prd.py PRD-TRADEWITHRISAL.md -- pricing BEGINER EXPERT payment
"""
import re, sys

path = sys.argv[1]
src = open(path, encoding="utf-8").read()
errors = []

# 1. Placeholders
pat = re.compile(r"TODO|TBD|XXX|lorem|placeholder|isi nanti|belum diisi|\.\.\.$", re.I)
for i, line in enumerate(src.splitlines(), 1):
    if pat.search(line):
        errors.append(f"line {i}: placeholder -> {line.strip()[:80]}")

# 2. Feature-ID sequence (default prefix F-)
prefix = "F-"
m = re.findall(r"\*\*%s(\d+)[^*]*\*\*" % prefix, src)
if m:
    ids = [int(x) for x in m]
    expect = list(range(1, max(ids) + 1))
    missing = [x for x in expect if x not in ids]
    dup = [x for x in set(ids) if ids.count(x) > 1]
    if missing:
        errors.append(f"missing feature IDs: {missing}")
    if dup:
        errors.append(f"duplicate feature IDs: {dup}")
    print(f"feature IDs found: {len(ids)} (max {max(ids)})")

# 3. Leftover-concept grep (after --)
if "--" in sys.argv:
    idx = sys.argv.index("--")
    for term in sys.argv[idx + 1:]:
        hits = [i for i, l in enumerate(src.splitlines(), 1) if term.lower() in l.lower()]
        if hits:
            errors.append(f"leftover '{term}' at lines {hits[:10]}")

print(f"lines: {len(src.splitlines())}")
if errors:
    print("ERRORS:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("OK: completeness checks passed")
