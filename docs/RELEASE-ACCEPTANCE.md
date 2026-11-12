# Prototype release: entry and acceptance repair

## Sprint goal
A user opening the repository site root reaches the complete eight-module workbench, can follow the example journey, and can export and restore their project. A source commit alone is not a release acceptance result.

## Observed defect and cause
The inspected index.html remained the original report-preview screen (SHA f81ddc1a957d54f0c6464318556737fb287661c5). The eight-module app was in workbench.html. The site root therefore did not expose the completed module navigation. This repair redirects the default entry to workbench.html and provides a visible fallback link.

## Backlog and acceptance criteria
- P0: default entry opens workbench.html. Automated browser assertion added.
- P0: all eight navigation items open their panels. Automated assertion added.
- P0: Scope 2 alternatives stay separate; example LB 277.4 and MB 236.6 tCO2e; 15 Scope 3 categories; three missing references. Assertions added.
- P0: product example equals 1360 kgCO2e/FU; allocation and cut-off warnings remain. Assertions added.
- P0: library has 69 rows; eight-digit prefix lookup works; CSV is accessible. Assertions added.
- P0: library selection carries provenance into the CBAM scenario; archived data triggers an XML issue. Assertions added.
- P0: per-tonne values are not divided by output twice; 1.89 tCO2e/t remains 1.89. Assertion added.
- P0: forecast test equals EUR 24240; unentered SEFA stays blocked. Assertions added.
- P1: local collaboration request can be created. Assertion added.
- P1: project export, reset and import preserve work. Assertion added.
- P1: desktop and 390px mobile journeys run without page errors. Screenshots captured by the test.

## Increment delivered
Homepage repair, executable Chromium acceptance script and GitHub Actions workflow. Existing application, CSV and data are retained unchanged in this increment. The workflow tests a local HTTP server, not the public GitHub Pages deployment.

## Definition of done
1. Commit exists on target branch.
2. Prototype acceptance workflow passes on that commit; review the artifact result and screenshots.
3. Deployed site root and CSV are manually checked in a real end-user browser.
4. Data and filing limitations remain visible.
5. No unresolved P0 acceptance failure.

At preparation time the new workflow has NOT run. Browser acceptance and public deployment are therefore pending, not passed. GitHub Actions availability, permissions, network and Pages settings may require owner review.

## Sprint review journey
Root > overview > GHG inventory > product footprint > CN library > CBAM steps 1-6 > forecast > collaboration > reporting > export/reset/import. The reviewer checks desktop and mobile. One HTML document is acceptable for a prototype only if navigation exposes every module and the journey passes; it is not a substitute for a multi-user backend.

## Retrospective and next increments
Failure: published code was described as usable without checking the entry URL. Prevention: root-entry and whole-journey assertions now run on main pushes and pull requests. Do not describe backend or filing features as implemented.

Remaining work: authenticated organisations and tenant isolation; persistent evidence storage and audit history; authorised invitations and roles; verified definitive-period default datasets; official schema validation; jurisdiction-specific calculations; complete 27-language translations; public deployment automation with an explicit browser check. Archived reference values are not current defaults. XML is not official or submission-ready. Collaboration is local, not cloud.
