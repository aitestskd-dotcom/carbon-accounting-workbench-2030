# Synthetic report demonstration data

All organisations, evidence identifiers, activity values and emission factors in demo-factory.json are fictional. The full-year scenario is not a record of actual or forecast operations. Do not use it for regulatory reporting or commercial decisions.

## Use with the proposed prototype
Download demo-factory.json, open the workbench, select Restore JSON backup and confirm replacing the working dataset. The schema matches the proposed prototype backup format. Then open Importer report and select Print / save PDF. This procedure requires the prototype index.html to be published separately; these data files alone do not generate reports or enable GitHub Pages.

## Expected arithmetic
Natural gas: 2,000,000 kWh x 0.2 kgCO2e/kWh / 1,000 = 400 tCO2e.
Diesel: 20,000 litres x 2.5 kgCO2e/litre / 1,000 = 50 tCO2e.
Illustrative Scope 1 total: 450 tCO2e.
Electricity: 3,000,000 kWh x 0.35 kgCO2e/kWh / 1,000 = 1,050 tCO2e.
Selected activity total: 1,500 tCO2e.
Illustrative process intensity: 1,500 / 10,000 tonnes output = 0.15 tCO2e/tonne.
These are simple test expectations, not a statutory CBAM method or complete product footprint.

## Demonstration checks
- Two of three records have fictional evidence references; electricity deliberately has none.
- References are placeholders, not uploaded evidence or independently checked records.
- Generated report must remain marked DRAFT / SYNTHETIC DATA / NOT VERIFIED.
- Changing output changes the illustrative intensity, not the activity emissions.
- Zero or negative output and negative activity/factor inputs must be flagged by the application.
- Saving, restoring and PDF printing require browser testing before sharing externally.

No client login, live ERP, central database, legal monitoring or independent verification is delivered by this dataset.
