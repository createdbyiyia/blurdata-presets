# BlurData Presets

Community-curated **Document Presets** for [BlurData](https://blurdata.app) — the native macOS app that automatically detects and redacts PII in PDFs, screenshots, images and videos.

A preset is a JSON file describing which detectors should run on a specific type of document (German payslip, US W-2, bank statement…), so a user can switch from "manual toggling everything" to "one click, the right things are detected" depending on the file.

The BlurData app fetches [`catalog.json`](catalog.json) at runtime when the user opens **Browse Community Presets**. After download, each preset is cached locally and works fully offline.

## Available presets

| Preset | Country | Use case |
|---|---|---|
| 🇩🇪 [German Payslip](presets/de/lohnabrechnung.json) | DE | Steuerident-Nr., Rentenversicherungs-Nr., Krankenversicherungs-Nr., DE dates, IBAN |
| 🇮🇹 [Italian Busta Paga](presets/it/busta-paga.json) | IT | Codice Fiscale, Partita IVA, Matricola INPS, IT dates, IBAN |
| 🇺🇸 [US W-2 / Pay Stub](presets/us/w2-paystub.json) | US | SSN, EIN, ZIP, US dates, dollar wages |
| 🧾 [Generic Invoice](presets/generic/invoice.json) | — | Invoice numbers, EU VAT IDs, dates, IBAN (amounts kept visible) |
| 🏦 [Bank Statement](presets/generic/bank-statement.json) | — | IBAN, BIC/SWIFT, masked & full cards, transaction refs |

## Contributing a new preset

The fastest way:

1. **You're technical** → fork this repo, add your preset under `presets/<country>/<name>.json`, add it to `catalog.json`, open a PR. See [CONTRIBUTING.md](CONTRIBUTING.md) for the schema and regex safety rules.
2. **You're not technical** → fill the [request form on blurdata.app](https://blurdata.app/request-preset). Describe the document and which fields need to be redacted; iyia will write the JSON and publish it here.

## How the app uses this repo

When a user opens *Browse Community Presets* in BlurData:

1. App fetches `https://raw.githubusercontent.com/createdbyiyia/blurdata-presets/main/catalog.json`
2. Displays the list with name, emoji, country, description, tags
3. On "Install", fetches the specific preset JSON and saves it as a Custom preset locally
4. From that moment, the preset works offline like any bundled preset

No telemetry. No user data is sent.

## License

[MIT](LICENSE) — use, modify, redistribute. Attribution to BlurData appreciated but not required.
