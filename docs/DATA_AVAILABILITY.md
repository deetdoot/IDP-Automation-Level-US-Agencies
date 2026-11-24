# DATA_AVAILABILITY: DRAFT for the author (not final)

> **DRAFT.** Fill in the bracketed items and check that the wording fits the journal's required template (for example Springer Nature, Elsevier or PLOS) before submission.

## Draft statement (long form)
The data analysed in this study are secondary, publicly available data. They come from the U.S. Federal Agency AI Use Case Inventories, consolidated by the U.S. Office of Management and Budget and published on GitHub: the 2024 inventory (https://github.com/ombegov/2024-Federal-AI-Use-Case-Inventory, commit 4a29d13) and the 2025 inventory (https://github.com/ombegov/2025-Federal-Agency-AI-Use-Case-Inventory, commit 06c7ebe). Both were accessed on 23 November 2026. Unmodified copies of the source files used, with SHA-256 checksums, are provided with the derived screening outputs, the screening code (Python), the keyword lists, a codebook and a methods description in the data package *[TITLE]*, version 1.0, available at [REPOSITORY] (https://doi.org/[DOI]) under CC BY 4.0 for data and documentation and the MIT License for code. The keyword screen can be reproduced exactly from these files. The author's manual screening decisions [are included in version X / will be added in a later version]. No restricted, confidential or human-participant data were used.

## Draft statement (short form)
All data used are publicly available from the U.S. Federal AI Use Case Inventories (OMB; github.com/ombegov, 2024 inventory commit 4a29d13 and 2025 inventory commit 06c7ebe; accessed 23 November 2026). Source files, code and derived data are archived at [REPOSITORY] (https://doi.org/[DOI]).

## Draft code availability statement (if the journal asks for one)
The screening code (`screen.py`, `keywords.json`, `download_sources.sh`) is included in the data package at [REPOSITORY] (https://doi.org/[DOI]) under the MIT License.

## Items to decide or verify before submission
- [ ] Repository and DOI. Not yet deposited; no DOI exists.
- [x] License for the package. CC BY 4.0 for `derived/` and `docs/`; MIT for `code/` and `tools/`. See README "License". The upstream works are likely public domain under 17 U.S.C. §105; this is likely, not legally verified. The CC BY 4.0 license does not cover `raw/`.
- [ ] Whether the author decisions will be included at submission (v1.1).
- [x] Generative AI assistance is disclosed in README and docs/METHODS.md. The author defined the screening rules and classes and is responsible for all content.
- [ ] Journal-specific wording or template.
