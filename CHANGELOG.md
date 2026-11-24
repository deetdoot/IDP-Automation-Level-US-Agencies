# CHANGELOG

Format based on Keep a Changelog. Versions follow MAJOR.MINOR: MINOR adds files or decisions, and MAJOR changes sources or rules.

## [Unreleased] v1.1 (planned)
- Add the author's screening decisions in `derived/author_decisions/`, exported from `tools/IDP_Screener.html`.
- Add the repository DOI once deposited. No DOI has been assigned.

## [1.0] 2026-11-23 (PST)
### Added
- `raw/`: 18 unmodified upstream files from `ombegov/2024-Federal-AI-Use-Case-Inventory` @ 4a29d13 and `ombegov/2025-Federal-Agency-AI-Use-Case-Inventory` @ 06c7ebe, kept in the upstream folder layout, plus `SHA256SUMS.txt`.
- `code/`: `screen.py`, `keywords.json`, `download_sources.sh`, `requirements.txt`, `RUN.md`.
- `derived/`: rule-based screen outputs (6 CSVs, 1 XLSX, run log). Author decisions are pending.
- `docs/`: METHODS, CODEBOOK, DATA_CITATION, DATA_AVAILABILITY (draft), VERIFICATION_LOG.
- `tools/IDP_Screener.html`: the offline author screening interface (not data).
- `LICENSE`: MIT License, copyright 2026 Emtiaz Ahamed, covering `code/` and `tools/` only.
- `LICENSE-DATA`: CC BY 4.0 covering `derived/` and `docs/` only.

### Changed
- Documentation, still version 1.0, dated 2026-11-23. Author affiliation, contact emails, and ORCID: not yet assigned.
- Upstream credit: the reporting federal agencies as authors, and the U.S. Office of Management and Budget as compiler and publisher (README and docs/DATA_CITATION.md).
- The 2025 OMB guidance PDF is cited as n.d. No date is printed in the PDF.
- Generative-AI assistance is stated in README and docs/METHODS.md. The author defined the screening rules and classes and is responsible for all content.
- The DOI remains a placeholder. No Zenodo deposit yet.

### Changed, compared with the working copy (`inventory-screen/`)
- `screen.py`: only the input paths (now `../raw/<repo>_<commit>/...`), the output folder (`../derived`) and the output file names changed (prefixed `idp_screen_`; the XLSX is renamed `idp_screen_all_tables.xlsx`). No logic changed. The outputs were verified identical (see docs/VERIFICATION_LOG.md).
- `raw/` file names: the working copy used flattened names such as `2024_2024_consolidated_ai_inventory_raw_v2.csv`. The package uses the upstream paths. The file contents are identical (same SHA-256).
- Added upstream files that the working copy did not have: 2025 COTS `.xlsx`, `Data/README_datasets.md`, `Validation/README.md`, `data_dictionary.json`, `data_sourcing_summary.md`, `data_standardization_report_AI_COTS.md`, `Reporting Instructions/Reporting Instructions.md`.

### Screening protocol history (before packaging)
- Keyword lists and v1 exclusion triggers were fixed before the first run.
- After reading the v1 include output, the v2 exclusion triggers were added. This moved 5 (2024) and 9 (2025) rows from include to needs author review, and nothing else. The v1 decisions are kept in `decision_v1`. See docs/METHODS.md §5, including the caveat about the timestamps inside keywords.json.
