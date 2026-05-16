# Contributing a preset

There are two paths.

## Path A — you can read JSON and regex

1. Fork this repo.
2. Add your preset file under `presets/<country-code>/<short-name>.json` (e.g. `presets/fr/bulletin-de-salaire.json`). Use lowercase, hyphens, no spaces.
3. Add a corresponding entry to `catalog.json`. The `url` field must be the raw.githubusercontent URL of the file you just added.
4. Run the regex safety check (see "Safety rules" below).
5. Open a PR with: what document type, which country, which fields are detected, an example you tested against (you can share an anonymized screenshot — never share real PII).

A maintainer reviews and merges. The new preset appears in *Browse Community Presets* in the app within minutes.

## Path B — you can't write regex

Use the [request form on blurdata.app](https://blurdata.app/request-preset). Describe the document type and which fields need to disappear. Attach an anonymized sample if possible. A maintainer will write the JSON and publish it.

## Schema

Minimal preset:

```json
{
  "id": "fr.bulletin-de-salaire",
  "version": 1,
  "name": "French Payslip",
  "emoji": "🇫🇷",
  "description": "French bulletin de salaire — detects NIR, French addresses, dates, IBAN.",
  "language": "fr",
  "country": "FR",
  "tags": ["payslip", "france", "bulletin de salaire"],
  "patterns": [
    {
      "name": "NIR (Numéro de sécurité sociale)",
      "regex": "\\b[12]\\d{2}(?:0[1-9]|1[0-2])\\d{2}\\d{3}\\d{3}\\d{2}\\b",
      "description": "French social security number — 15 digits with structure",
      "enabled": true
    }
  ],
  "builtin": {
    "email": true,
    "name": true,
    "address": true,
    "ip": false,
    "url": false,
    "amount": false,
    "accountNumber": true,
    "licensePlate": false
  }
}
```

### Fields

| Field | Required | Notes |
|---|---|---|
| `id` | yes | Stable identifier like `<country>.<short-name>` — never changes after publication |
| `version` | yes | Bump when you change the patterns (Integer, starts at 1) |
| `name` | yes | Human title shown in the app |
| `emoji` | no | One emoji shown next to the name |
| `description` | yes | 1–2 sentences explaining what the preset is for |
| `language` | no | ISO 639-1 code (`de`, `it`, `en`…) |
| `country` | no | ISO 3166-1 alpha-2 (`DE`, `IT`, `US`…) or `null` if generic |
| `tags` | no | Search/filter keywords |
| `patterns` | yes | Array of `{name, regex, description, enabled}` — see safety rules below |
| `builtin` | yes | Built-in detector overrides: keys are `email`, `name`, `address`, `ip`, `url`, `amount`, `accountNumber`, `licensePlate`. `true` enables, `false` disables, `null` (or absent) leaves user preference untouched |

## Safety rules for regex

- **Always use `\b` word boundaries** to avoid matching inside longer tokens.
- **Never use unbounded `.*` greedy quantifiers** — they cause catastrophic backtracking on big PDFs.
- **No nested unbounded quantifiers** like `(a+)+` or `(a|aa)+`. These hang the app.
- **Anchor structure** when possible. `\b\d{11}\b` is fine, `\d+` everywhere is not.
- **Use non-capturing groups** `(?:...)` unless you need a capture.
- **Test with a real example** before submitting. Drop your preset into BlurData and verify it matches the things you want and ignores the things you don't.
- **No PII in description or examples.** Use clearly fake data (`123-45-6789`, `RSSMRA85A01F205X`) — never real.

## Naming

Folder structure:
- `presets/<iso-country>/<short-name>.json` for country-specific (e.g. `presets/fr/bulletin-de-salaire.json`)
- `presets/generic/<short-name>.json` for generic / cross-country presets (e.g. `presets/generic/medical-record.json`)

File names: lowercase, hyphenated, English when possible (`bulletin-de-salaire.json`, not `BulletinDeSalaire.json`).

## Review checklist (what maintainer checks)

- [ ] Regex compiles in Swift's `NSRegularExpression`
- [ ] No catastrophic backtracking (tested with 50KB random text input, returns in <100ms)
- [ ] All examples in `description` and `name` are synthetic
- [ ] `id` is unique and follows the `<country>.<name>` convention
- [ ] `catalog.json` entry matches the actual file path
- [ ] `builtin` toggles are sensible for the document type (e.g. don't disable `address` on a payslip)

## License

Submitted presets are released under the repo's MIT license. By opening a PR you agree to this.
