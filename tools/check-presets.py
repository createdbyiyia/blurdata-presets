#!/usr/bin/env python3
"""Structure checks for catalog.json and every preset it lists.

usage: python3 tools/check-presets.py        (from the repository root, or any folder)

Errors (exit status 1):
  - catalog.json: version, presets list, unique ids, path and url of every entry (url ends with the path)
  - every listed file exists, its id is the catalog id and its version equals the catalog presetVersion
  - required fields and types (id, version, name, description, patterns; name, regex, description,
    enabled in every pattern)
  - pattern names unique inside a preset: the app shows one row per pattern and uses the name as the
    Pseudonymize label, so patterns that belong together are one pattern with alternation
  - builtin keys among the detectors the app knows
Warnings: preset files not listed in the catalog, catalog name / description / tags different from the file,
a preset without builtin.
Regexes are not compiled here (Python's engine is not the app's NSRegularExpression): test them in Swift.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILTIN = {"email", "name", "address", "ip", "url", "amount", "accountNumber", "licensePlate", "barcode", "phone",
           "signature"}  # signature: handwritten signatures, BlurData 1.6.5 (older apps ignore unknown keys)
errors, warnings = [], []


def err(msg):
    errors.append(msg)


def check_preset(entry, data):
    pid = entry["id"]
    for key, typ in (("id", str), ("version", int), ("name", str), ("description", str), ("patterns", list)):
        if not isinstance(data.get(key), typ) or isinstance(data.get(key), bool) and typ is int:
            err("%s: field %s missing or not %s" % (pid, key, typ.__name__))
    if not isinstance(data.get("builtin"), dict):
        warnings.append("%s: no builtin object (the app keeps the user's detector switches)" % pid)
    if data.get("id") != pid:
        err("%s: file id is %r" % (pid, data.get("id")))
    if data.get("version") != entry.get("presetVersion"):
        err("%s: version %r but catalog presetVersion %r" % (pid, data.get("version"), entry.get("presetVersion")))
    seen = {}
    for i, p in enumerate(data.get("patterns") or []):
        for key, typ in (("name", str), ("regex", str), ("description", str), ("enabled", bool)):
            if not isinstance(p.get(key), typ):
                err("%s: pattern %d: field %s missing or not %s" % (pid, i, key, typ.__name__))
        name = p.get("name")
        if name in seen:
            err("%s: pattern name %r used twice (patterns %d and %d): merge them into one pattern" % (pid, name, seen[name], i))
        seen.setdefault(name, i)
        if isinstance(p.get("regex"), str) and not p["regex"].strip():
            err("%s: pattern %r has an empty regex" % (pid, name))
    for k, v in (data.get("builtin") or {}).items():
        if k not in BUILTIN:
            err("%s: unknown builtin key %r" % (pid, k))
        elif v is not None and not isinstance(v, bool):
            err("%s: builtin %s must be true, false or null" % (pid, k))
    for key in ("name", "emoji", "language", "country", "description", "tags"):
        if key in entry and entry.get(key) != data.get(key):
            warnings.append("%s: catalog %s differs from the file" % (pid, key))


def main():
    with open(os.path.join(ROOT, "catalog.json"), encoding="utf-8") as fh:
        cat = json.load(fh)
    if not isinstance(cat.get("version"), int):
        err("catalog: version missing or not an integer")
    entries = cat.get("presets")
    if not isinstance(entries, list):
        err("catalog: presets missing")
        entries = []
    ids, listed = set(), set()
    for e in entries:
        pid = e.get("id")
        if not isinstance(pid, str):
            err("catalog: entry without id")
            continue
        if pid in ids:
            err("catalog: id %s listed twice" % pid)
        ids.add(pid)
        for key in ("presetVersion", "name", "path", "url"):
            if key not in e:
                err("catalog: %s has no %s" % (pid, key))
        path = e.get("path", "")
        if not str(e.get("url", "")).endswith("/" + path):
            err("catalog: %s url does not end with its path" % pid)
        full = os.path.join(ROOT, path)
        listed.add(os.path.normpath(full))
        if not os.path.isfile(full):
            err("catalog: %s: file %s not found" % (pid, path))
            continue
        try:
            with open(full, encoding="utf-8") as fh:
                data = json.load(fh)
        except ValueError as x:
            err("%s: %s is not valid JSON (%s)" % (pid, path, x))
            continue
        check_preset(e, data)
    for folder, _, files in os.walk(os.path.join(ROOT, "presets")):
        for f in files:
            full = os.path.normpath(os.path.join(folder, f))
            if f.endswith(".json") and full not in listed:
                warnings.append("presets/%s is not in catalog.json" % os.path.relpath(full, os.path.join(ROOT, "presets")))
    for w in warnings:
        print("warning: " + w)
    for e in errors:
        print("ERROR: " + e)
    print("catalog v%s, %d presets, %d errors, %d warnings" % (cat.get("version"), len(entries), len(errors), len(warnings)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
