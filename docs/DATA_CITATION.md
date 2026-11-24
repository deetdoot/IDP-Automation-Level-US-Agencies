# DATA_CITATION

Suggested citations follow the DataCite pattern: *Creator (PublicationYear). Title (Version). Publisher. Identifier.* The upstream datasets have **no DOI**. They are identified here by repository URL plus pinned commit, and the access date is given.

**Creator/publisher attribution:** The reporting federal agencies are the authors of the use-case records. The U.S. Office of Management and Budget is the compiler and publisher. Both repositories sit under the GitHub organization `ombegov`. The READMEs say the 2025 repository was "compiled" by OMB, and both list the maintainers' contact as OFCIO_AI@omb.eop.gov (the OMB Office of the Federal Chief Information Officer). Neither README names the Federal CIO Council as publisher, so it is not credited here. Publication year = year of the pinned commit.

## Upstream dataset 1: 2024 inventory
**DataCite style**
Reporting federal agencies (authors); U.S. Office of Management and Budget (compiler and publisher). (2025). *2024 Federal Agency AI Use Case Inventory* (commit 4a29d132291261d4829b187acd8af618e7295294; file `data/2024_consolidated_ai_inventory_raw_v2.csv`) [Data set]. GitHub. https://github.com/ombegov/2024-Federal-AI-Use-Case-Inventory/tree/4a29d132291261d4829b187acd8af618e7295294. Accessed 23 November 2026.

**APA 7 style**
Reporting federal agencies (authors); U.S. Office of Management and Budget (compiler and publisher). (2025). *2024 Federal agency AI use case inventory* [Data set]. GitHub. https://github.com/ombegov/2024-Federal-AI-Use-Case-Inventory (commit 4a29d13, accessed November 23, 2026)

## Upstream dataset 2: 2025 inventory
**DataCite style**
Reporting federal agencies (authors); U.S. Office of Management and Budget (compiler and publisher). (2026). *2025 Federal Agency AI Use Case Inventory* (commit 06c7ebeef5b376524211042bd9673b2a7fefd3e3; files `Data/2025_individually_reported_AI_use_cases.csv`, `Data/2025_consolidated_COTS_AI_use_cases.csv`) [Data set]. GitHub. https://github.com/ombegov/2025-Federal-Agency-AI-Use-Case-Inventory/tree/06c7ebeef5b376524211042bd9673b2a7fefd3e3. Accessed 23 November 2026.

**APA 7 style**
Reporting federal agencies (authors); U.S. Office of Management and Budget (compiler and publisher). (2026). *2025 Federal agency AI use case inventory* [Data set]. GitHub. https://github.com/ombegov/2025-Federal-Agency-AI-Use-Case-Inventory (commit 06c7ebe, accessed November 23, 2026)

Title note: the 2025 repository's name is "2025-Federal-Agency-AI-Use-Case-Inventory". Its README calls the work "2025 Federal Agency Artificial Intelligence (AI) Use Case Inventory".

## Reporting guidance (cite if you discuss reporting fields)
U.S. Office of Management and Budget. *Guidance on 2025 Agency Artificial Intelligence Reporting* (FINAL) (n.d.). PDF in the 2025 repository, `Reporting Instructions/`, commit 06c7ebe. No date is printed in the PDF.
OMB Memorandum M-25-21, *Accelerating Federal Use of AI through Innovation, Governance, and Public Trust* (Apr. 3, 2025). https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf (date as given in the repository's "Reporting Instructions.md").

## This data package
**DataCite style, with placeholder**
Ahamed, E. (2026). *Federal IDP inventory screen: data package for [PAPER TITLE]* (Version 1.0) [Data set]. [REPOSITORY, e.g. Zenodo]. https://doi.org/[DOI-TO-BE-ASSIGNED]

- **DOI: not yet assigned.** Do not cite a DOI until the repository mints one. If deposited on Zenodo, also record the concept DOI (all versions) and the version DOI.
- Suggested DataCite metadata: resourceTypeGeneral = Dataset; version = 1.0; language = en; subjects = artificial intelligence, intelligent document processing, OCR, U.S. federal government, AI use case inventory; RelatedIdentifier `IsDerivedFrom` → the two GitHub URLs above; RelatedIdentifier `IsSupplementTo` → the paper's DOI, once it has one.
- **Creator:** Emtiaz Ahamed, Master's student, University of Nevada, Las Vegas (UNLV). Contact: emon@unlv.nevada.edu (alternate: emtiaz.ahamed79@gmail.com). ORCID: not yet assigned. The paper title in the citation above remains the placeholder [PAPER TITLE]. License: CC BY 4.0 for `derived/` and `docs/` (`LICENSE-DATA`); MIT for `code/` and `tools/` (`LICENSE`, copyright 2026 Emtiaz Ahamed). The CC BY 4.0 license applies only to this package's own contributions, not to the `raw/` upstream files.
