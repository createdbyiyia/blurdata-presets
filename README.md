# BlurData Presets

Community-curated **Document Presets** for [BlurData](https://blurdata.app) — the native macOS app that automatically detects and redacts PII in PDFs, screenshots, images and videos.

A preset is a JSON file describing which detectors should run on a specific type of document (German payslip, US W-2, bank statement…), so a user can switch from "manual toggling everything" to "one click, the right things are detected" depending on the file.

The BlurData app fetches [`catalog.json`](catalog.json) at runtime when the user opens **Browse Community Presets**. After download, each preset is cached locally and works fully offline.

## Available presets (19)

| Preset | Country | Detects |
|---|---|---|
| 🇩🇪 [German Payslip](presets/de/lohnabrechnung.json) | DE | Detects Steuerident-Nr |
| 🇮🇹 [Italian Busta Paga](presets/it/busta-paga.json) | IT | Detects Codice Fiscale, Partita IVA, Matricola INPS, IBAN, Italian dates and phone numbers, plus names, addres… |
| 🇺🇸 [US W-2 / Pay Stub](presets/us/w2-paystub.json) | US | Detects SSN, EIN, US dates, US ZIP codes, US phone numbers, bank routing numbers (context-anchored), plus name… |
| 🏥 [US Medical Records](presets/us/medical-records.json) | US | Detects patient names, DOB (multiple formats), MRN (6+ digit runs without decimals), SSN, full US addresses, Z… |
| 🇬🇧 [UK Medical Records](presets/uk/medical-records.json) | GB | Detects NHS numbers, UK dates (dd/mm/yyyy and long form), UK postcodes, UK phones, NI numbers, hospital number… |
| 🧾 [Generic Invoice](presets/generic/invoice.json) | — | Detects invoice numbers, dates, EU VAT IDs, IBAN, BIC/SWIFT (context-anchored), international phones, plus nam… |
| 🏦 [Bank Statement](presets/generic/bank-statement.json) | — | Detects IBAN, BIC/SWIFT (context-anchored), masked card numbers, full card numbers (13-19 digits), transaction… |
| 🌎 [Common Surnames (US + Canada)](presets/us/common-surnames.json) | — | For guest lists, reservation calendars, employee rosters |
| 🧾 [Italian Fattura](presets/it/fattura.json) | IT | Detects Partita IVA, Codice Fiscale, IBAN, the SDI recipient code, Italian dates and phone numbers, plus names… |
| 📜 [Italian Atto / Contratto](presets/it/atto-contratto.json) | IT | Detects Codice Fiscale, Partita IVA, IBAN, the notarial Repertorio/Raccolta number, Italian dates and phone nu… |
| ⚖️ [Italian Sentenze / Atti Giudiziari](presets/it/atti-giudiziari.json) | IT | Detects codice fiscale (personal and company), partita IVA, cadastral references (foglio, particella, subalter… |
| 🏛️ [Italian Visura](presets/it/visura.json) | IT | Detects Partita IVA, Codice Fiscale, REA number, cadastral references (Foglio / Particella / Subalterno), IBAN… |
| 🧾 [German Rechnung](presets/de/rechnung.json) | DE | Detects USt-IdNr, Steuernummer, IBAN, BIC/SWIFT, German dates, phones, street addresses and PLZ + city, plus n… |
| 🪪 [German Personalausweis](presets/de/personalausweis.json) | DE | Detects the Ausweisnummer, CAN/Zugangsnummer, Steuer-ID, the machine-readable zone (MRZ), date of birth and Ge… |
| 🏦 [German Kontoauszug](presets/de/kontoauszug.json) | DE | Detects IBAN, BIC/SWIFT, Bankleitzahl (BLZ), Kontonummer, German dates, phones and addresses, plus account hol… |
| 🚗 [German Führerschein](presets/de/fuehrerschein.json) | DE | Detects the Führerscheinnummer, date and place of birth, issue/expiry dates and German addresses, plus names |
| 🪪 [Spanish DNI / NIE](presets/es/dni.json) | ES | Detects the DNI (8 digits + letter), NIE, the support number (IDESP), dates of birth and Spanish addresses, pl… |
| 🧾 [Spanish Factura](presets/es/factura.json) | ES | Detects NIF / CIF / DNI, IBAN, Spanish dates and phone numbers, plus names, addresses and emails |
| 🇧🇪 [Belgian Legal Documents (FR)](presets/be/documents-juridiques.json) | BE | Detects the BCE company number, cadastral references, Belgian addresses and postal codes, company names by leg… |

## What you can anonymize, in your language

- 🇮🇹 **Italiano**: anonimizzazione di sentenze, atti giudiziari, atti notarili, buste paga, fatture e visure. Rileva codice fiscale, partita IVA, dati catastali (foglio, particella, subalterno), targhe, IBAN e date.
- 🇩🇪 **Deutsch**: Lohnabrechnungen und Dokumente schwärzen. Erkennt Steuer-ID, Rentenversicherungsnummer, Krankenversicherungsnummer, IBAN und Datumsangaben.
- 🇪🇸 **Español**: anonimizar nóminas y documentos. Detecta DNI/NIE, número de la Seguridad Social, IBAN y fechas.
- 🇫🇷 **Français**: anonymiser des documents juridiques belges (citations, conclusions, actes). Détecte le numéro BCE, les références cadastrales, les adresses et l'IBAN.
- 🇬🇧 **English**: redact payslips, W-2s, invoices, bank statements and court documents. Detects SSN, EIN, National Insurance numbers, IBAN, card numbers and dates.

All processing happens on-device in the BlurData app: documents never leave your Mac.

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
