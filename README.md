# BlurData Presets

Community-curated **Document Presets** for [BlurData](https://blurdata.app), the native macOS app that automatically detects and redacts PII in PDFs, scans, screenshots and images, or replaces it with consistent labels like [PERSON_1] (Pseudonymize) so documents can go to ChatGPT, Claude or any AI, with an optional clean Markdown export.

A preset is a JSON file describing which detectors should run on a specific type of document (German payslip, US W-2, bank statement…), so a user can switch from "manual toggling everything" to "one click, the right things are detected" depending on the file.

The BlurData app fetches [`catalog.json`](catalog.json) at runtime when the user opens **Browse Community Presets**. After download, each preset is cached locally and works fully offline.

## Available presets (30)

| Preset | Country | Detects |
|---|---|---|
| 🇩🇪 [German Payslip](presets/de/lohnabrechnung.json) | DE | German Lohn-/Gehaltsabrechnung. Detects Steuerident-Nr., Rentenversicherungs-Nr., Krankenversicherungs-Nr.… |
| 🇮🇹 [Italian Busta Paga](presets/it/busta-paga.json) | IT | Italian payslip. Detects Codice Fiscale, Partita IVA, Matricola INPS, IBAN, Italian dates and phone numbers… |
| 🇺🇸 [US W-2 / Pay Stub](presets/us/w2-paystub.json) | US | US tax forms and pay stubs (W-2, W-4, 1099, generic paystubs). Detects SSN, EIN, US dates, US ZIP codes, US… |
| 🏥 [US Medical Records](presets/us/medical-records.json) | US | US medical records and clinical notes. Detects patient names, DOB (multiple formats), MRN (6+ digit runs… |
| 🇬🇧 [UK Medical Records](presets/uk/medical-records.json) | GB | UK hospital and GP records. Detects NHS numbers, UK dates (dd/mm/yyyy and long form), UK postcodes, UK… |
| 🧾 [Generic Invoice](presets/generic/invoice.json) | — | Generic invoice or receipt. Detects invoice numbers, EU VAT IDs, IBAN, BIC/SWIFT (context-anchored), phone… |
| 🏦 [Bank Statement](presets/generic/bank-statement.json) | — | Bank or credit card statement. Detects IBAN, BIC/SWIFT (context-anchored), masked card numbers, full card… |
| 🌎 [Common Surnames (US + Canada)](presets/us/common-surnames.json) | — | Opt-in preset that hides ~10,400 common surnames across the US and Canada — top 10k US Census 2010 plus… |
| 🧾 [Italian Fattura](presets/it/fattura.json) | IT | Italian invoice (fattura). Detects Partita IVA, Codice Fiscale, IBAN, the SDI recipient code, Italian dates… |
| 📜 [Italian Atto / Contratto](presets/it/atto-contratto.json) | IT | Italian legal deed or contract (atto notarile, contratto). Detects Codice Fiscale, Partita IVA, IBAN, the… |
| ⚖️ [Italian Sentenze / Atti Giudiziari](presets/it/atti-giudiziari.json) | IT | Italian court judgments and judicial acts (sentenze, decreti, verbali, atti di stato civile). Detects codice… |
| 🏛️ [Italian Visura](presets/it/visura.json) | IT | Italian company or cadastral record (visura camerale / catastale). Detects Partita IVA, Codice Fiscale, REA… |
| 🧾 [German Rechnung](presets/de/rechnung.json) | DE | German invoice (Rechnung). Detects USt-IdNr, Steuernummer, IBAN, BIC/SWIFT, German dates, phones, street… |
| 🪪 [German Personalausweis](presets/de/personalausweis.json) | DE | German ID card (Personalausweis) or passport copy. Detects the Ausweisnummer, CAN/Zugangsnummer, Steuer-ID… |
| 🏦 [German Kontoauszug](presets/de/kontoauszug.json) | DE | German bank statement (Kontoauszug). Detects IBAN, BIC/SWIFT, Bankleitzahl (BLZ), Kontonummer, German dates… |
| 🚗 [German Führerschein](presets/de/fuehrerschein.json) | DE | German driving licence (Führerschein) copy. Detects the Führerscheinnummer, date and place of birth… |
| 🪪 [Spanish DNI / NIE](presets/es/dni.json) | ES | Spanish ID (DNI) or foreigner ID (NIE) copy. Detects the DNI (8 digits + letter), NIE, the support number… |
| 🧾 [Spanish Factura](presets/es/factura.json) | ES | Spanish invoice (factura). Detects NIF / CIF / DNI, IBAN, Spanish dates and phone numbers, plus names… |
| 🇧🇪 [Belgian Legal Documents (FR)](presets/be/documents-juridiques.json) | BE | Belgian legal documents in French (citations, conclusions, actes). Detects the BCE company number, cadastral… |
| 📈 [US Brokerage Account Statement](presets/us/brokerage-statement.json) | US | US individual brokerage account statement (Schwab, Fidelity, Vanguard, Merrill, Morgan Stanley, IBKR and… |
| ⚖️ [German Court Order (Gerichtsbeschluss)](presets/de/gerichtsbeschluss.json) | DE | German court orders, decisions and judicial correspondence (Beschluss, Urteil, Verfügung). Detects… |
| 🇨🇭 [Swiss Medical Records (Dossier médical)](presets/ch/medical-records.json) | CH | Swiss medical records in French, German or Italian: discharge letters, consultation reports, lab results… |
| 🇫🇷 [French Payslip, Invoice & Tax Notice](presets/fr/documents-administratifs.json) | FR | French bulletin de paie, facture and avis d'impôt. Detects the NIR (numéro de sécurité sociale), SIRET… |
| 🧾 [US Broker Tax Statement (Consolidated 1099)](presets/us/consolidated-1099.json) | US | Year-end tax statement from a US broker (Form 1099 Composite / Consolidated 1099 from Schwab, Fidelity… |
| 🔧 [German Workshop Order (Werkstattauftrag)](presets/de/werkstattauftrag.json) | DE | German workshop and repair orders (Werkstattauftrag, Reparaturauftrag, Auftragsbestätigung) from dealer… |
| 🇬🇧 [UK Tax Return (SA100, SA302, P60, P45)](presets/uk/tax-return.json) | GB | UK Self Assessment documents: the SA100 tax return, the SA302 tax calculation and the P60 and P45… |
| 🚜 [US Equipment Invoice / Sales Order](presets/us/equipment-invoice.json) | US | Invoices, sales orders and quotes from US machinery and equipment dealers (forestry, construction,… |
| 🇩🇪 [German Medical Records (Arztbrief, Befund)](presets/de/medical-records.json) | DE | German Arztbrief, Entlassungsbrief, Befundbericht, Laborbefund, Muster 6, Reha-Entlassungsbericht. Detects patient and… |
| 🇵🇹 [Portuguese Medical Records (Relatório, Análises, Receita)](presets/pt/medical-records.json) | PT | Portuguese análises clínicas, nota de alta, relatório clínico and imagiologia, receita sem papel, atestado médico. Detects patient and… |
| 🇬🇧 [UK Social Care (Care Act)](presets/uk/social-care.json) | GB | English adult social care records: Care Act assessments, care and support plans and one-page profiles, personal budget… |

## What you can anonymize, in your language

- 🇮🇹 **Italiano**: anonimizzazione di sentenze, atti giudiziari, atti notarili, buste paga, fatture e visure. Rileva codice fiscale, partita IVA, dati catastali (foglio, particella, subalterno), targhe, IBAN e date.
- 🇩🇪 **Deutsch**: Lohnabrechnungen, Rechnungen, Kontoauszüge, Personalausweis, Führerschein, Gerichtsbeschlüsse, Werkstattaufträge sowie Arztbriefe, Entlassungsbriefe, Befundberichte und Laborbefunde schwärzen. Erkennt Steuer-ID, Rentenversicherungsnummer, Krankenversicherungsnummer, LANR, BSNR, IK, USt-IdNr, Ausweisnummer, IBAN, Kfz-Kennzeichen, FIN (nur die letzten 6 Stellen), Patientennamen mit Namenszusätzen (von, zu, van der), Geburtsdaten und Datumsangaben.
- 🇫🇷 **Français**: anonymiser et caviarder un bulletin de paie, une facture ou un avis d'impôt (France), des documents juridiques belges et des dossiers médicaux suisses. Détecte le NIR (numéro de sécurité sociale), SIRET, SIREN, TVA intracommunautaire, numéro fiscal, numéro AVS, numéro BCE, références cadastrales, adresses et IBAN.
- 🇪🇸 **Español**: anonimizar DNI, NIE y facturas. Detecta DNI, NIE, NIF/CIF, IBAN, teléfonos y fechas.
- 🇵🇹 **Português**: anonimizar registos médicos: boletins de análises clínicas, notas de alta, relatórios clínicos e de imagiologia, guias de tratamento da receita sem papel e atestados médicos. Deteta nomes de doentes e médicos, data de nascimento, número de utente do SNS, NIF, NISS, Cartão de Cidadão, números ADSE, SAMS e de seguros, processo e episódio, código de acesso e de opção da receita, cédula profissional, moradas, códigos postais e telefones.
- 🇬🇧 **English**: redact payslips, W-2s, broker tax statements (Consolidated 1099), invoices, bank and brokerage statements, medical records, adult social care records (Care Act assessments, support plans, Direct Payments) and court documents. Detects SSN, EIN, National Insurance and NHS numbers, IBAN, routing and account numbers, card numbers and dates.

Every preset works with both modes of the app: **Redact** removes the data from the file for good, **Pseudonymize** swaps it for consistent labels ([PERSON_1], [IBAN_1]…) so the document keeps its meaning for an AI, and can be saved as Markdown.

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
