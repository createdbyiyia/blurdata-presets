#!/usr/bin/env python3
"""Checks recognition.json, the signs BlurData 1.6.3+ uses to suggest a preset for an opened document.

usage: python3 tools/check-recognition.py        (from the repository root, or any folder)

Errors (exit status 1):
  - catalog.json lists the file: "recognition": {"url": ".../recognition.json", "path": "recognition.json"}
  - recognition.json: a "presets" list; every id once and listed in catalog.json
  - every entry: at least 3 signs, each a non-empty phrase with weight 1, 2 or 3, no phrase twice
    (after the app's folding: lower case, accents removed, punctuation as spaces)
  - "label" in en, de, es, fr, it, without em or en dashes
  - "refines": ids of other entries
  - thresholds, when present: numbers at or above the app's floors
Warnings: catalog presets without signs (the app never suggests them), a phrase used by many presets.
"""
import json
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ["en", "de", "es", "fr", "it"]
errors, warnings = [], []


def words(s):
    """Same folding as DocumentRecognizer.words in the app."""
    s = s.lower().replace("ß", "ss").replace("œ", "oe").replace("æ", "ae")
    s = "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")
    return [w for w in re.split(r"[^\w]|_", s) if w]


def main():
    with open(os.path.join(ROOT, "catalog.json"), encoding="utf-8") as fh:
        cat = json.load(fh)
    ref = cat.get("recognition")
    if not isinstance(ref, dict) or not str(ref.get("url", "")).endswith("recognition.json"):
        errors.append("catalog.json: no \"recognition\" object with the url of recognition.json")
    elif ref.get("path") and not str(ref["url"]).endswith(ref["path"]):
        errors.append("catalog.json: recognition url does not end with its path")
    catalog_ids = {e.get("id") for e in cat.get("presets", [])}
    with open(os.path.join(ROOT, "recognition.json"), encoding="utf-8") as fh:
        rec = json.load(fh)
    entries = rec.get("presets")
    if not isinstance(entries, list):
        errors.append("recognition.json: presets missing")
        entries = []
    ids = set()
    phrase_users = {}
    for e in entries:
        pid = e.get("id")
        if not isinstance(pid, str) or not pid:
            errors.append("entry without id")
            continue
        if pid in ids:
            errors.append("%s: listed twice" % pid)
        ids.add(pid)
        if pid not in catalog_ids:
            errors.append("%s: not in catalog.json" % pid)
        signs = e.get("signs")
        if not isinstance(signs, list) or len(signs) < 3:
            errors.append("%s: fewer than 3 signs" % pid)
            signs = signs if isinstance(signs, list) else []
        seen = set()
        for s in signs:
            text, weight = (s, 1) if isinstance(s, str) else (s.get("text"), s.get("weight", 1))
            if not isinstance(text, str) or not words(text):
                errors.append("%s: empty sign %r" % (pid, s))
                continue
            if weight not in (1, 2, 3):
                errors.append("%s: sign %r weight %r (1, 2 or 3)" % (pid, text, weight))
            key = " ".join(words(text))
            if key in seen:
                errors.append("%s: sign %r twice" % (pid, text))
            seen.add(key)
            phrase_users.setdefault(key, set()).add(pid)
        label = e.get("label") or {}
        for lang in LANGS:
            v = label.get(lang)
            if not isinstance(v, str) or not v.strip():
                errors.append("%s: label %s missing" % (pid, lang))
            elif "—" in v or "–" in v:
                errors.append("%s: label %s has a dash" % (pid, lang))
    for e in entries:
        for r in e.get("refines", []) or []:
            if r not in ids:
                errors.append("%s: refines unknown %s" % (e.get("id"), r))
    floors = {"suggest": 2, "auto": 6, "autoTurningOff": 6, "margin": 2, "minSigns": 2}
    for k, v in (rec.get("thresholds") or {}).items():
        if k not in floors:
            errors.append("thresholds: unknown %s" % k)
        elif not isinstance(v, (int, float)) or v < floors[k]:
            errors.append("thresholds: %s must be a number of at least %s" % (k, floors[k]))
    for pid in sorted(catalog_ids - ids):
        warnings.append("%s: no signs (never suggested)" % pid)
    for key, users in sorted(phrase_users.items()):
        if len(users) >= 3:
            warnings.append("sign %r used by %d presets: %s" % (key, len(users), ", ".join(sorted(users))))
    for w in warnings:
        print("warning:", w)
    for e in errors:
        print("ERROR:", e)
    print("%d presets with signs, %d signs, %d errors, %d warnings"
          % (len(ids), sum(len(e.get("signs", [])) for e in entries), len(errors), len(warnings)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
