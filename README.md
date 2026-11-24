# Federal IDP Inventory Data: keyword screen of U.S. federal AI use case inventories for intelligent document processing

- **Version:** 1.0
- **Date:** 2026-11-23 (America/Los_Angeles, PST, UTC-8)
- **Author / contact:** Emtiaz Ahamed, Master's student, University of Nevada, Las Vegas (UNLV). Contact: emon@unlv.nevada.edu (alternate: emtiaz.ahamed79@gmail.com). ORCID: not yet assigned.
- **Persistent identifier:** *none yet*. A DOI will be added on deposit (for example Zenodo). See `docs/DATA_CITATION.md`. No DOI has been assigned.
- **License of this package:** CC BY 4.0 for data and documentation (`derived/`, `docs/`); MIT for code (`code/`, `tools/`). These licenses do not cover `raw/`. See "License" below.
- **Assistance:** Generative AI tools assisted with data retrieval, running the rule-based screen, and drafting documentation under the author's direction; the author defined the screening rules and classes and is responsible for all content.

## Purpose
This package supports the data-source section of the author's review paper on intelligent document processing (IDP) in U.S. federal agencies, including OCR, classification, evidence pointing and decision assistance. It holds the public sources used, untouched, with checksums. It also holds a reproducible keyword screen that finds candidate IDP use cases in the 2024 and 2025 Federal Agency AI Use Case Inventories, plus the screen outputs and full documentation. The structure follows the FAIR principles:
- **Findable:** a DOI on deposit, and DataCite metadata in docs/DATA_CITATION.md.
- **Accessible:** open formats (CSV, Markdown, XLSX) with no login.
- **Interoperable:** a codebook, upstream data dictionaries and UTF-8 derived CSVs.
- **Reusable:** provenance, pinned commits, checksums, code, versions and license notes.

## Directory tree
```
federal-idp-inventory-data_v1.0_2026-11-23/
├── README.md                      this file
├── CHANGELOG.md
├── LICENSE                        MIT, for code/ and tools/ only
├── LICENSE-DATA                   CC BY 4.0, for derived/ and docs/ only
├── raw/                           unmodified upstream files (upstream folder layout kept)
│   ├── SHA256SUMS.txt             SHA-256 of every file under raw/ (run sha256sum -c from inside raw/)
│   ├── ombegov_2024-Federal-AI-Use-Case-Inventory_4a29d13/
│   │   ├── README.md
│   │   ├── data/2024_consolidated_ai_inventory_raw_v2.csv     ← used by screen.py
│   │   ├── data/2024_consolidated_ai_inventory_raw_v2.xls
│   │   └── validation/data_dictionary.yaml
│   └── ombegov_2025-Federal-Agency-AI-Use-Case-Inventory_06c7ebe/
│       ├── README.md
│       ├── Data/2025_individually_reported_AI_use_cases.csv   ← used by screen.py (main)
│       ├── Data/2025_individually_reported_AI_use_cases.xlsx
│       ├── Data/2025_consolidated_COTS_AI_use_cases.csv       ← used by screen.py (supplementary)
│       ├── Data/2025_consolidated_COTS_AI_use_cases.xlsx
│       ├── Data/README_datasets.md
│       ├── Reporting Instructions/Guidance on 2025 Agency Artificial Intelligence Reporting (FINAL).pdf
│       ├── Reporting Instructions/Reporting Instructions.md
│       └── Validation/{README.md, data_dictionary.md, data_dictionary.json, data_sourcing_summary.md,
│                       data_standardization_report.md, data_standardization_report_AI_COTS.md}
├── code/
│   ├── screen.py                  keyword screen → derived/
│   ├── keywords.json              regex lists (strong, weak, document noun, v1 + v2 exclusion triggers)
│   ├── download_sources.sh        reproduces raw/ from GitHub at the pinned commits
│   ├── requirements.txt           Python 3.13.5; pandas 3.0.6, numpy 2.5.5, openpyxl 3.1.5, …
│   └── RUN.md                     how to run
├── derived/                       outputs of screen.py (rule-based; NOT author decisions)
│   ├── README.md
│   ├── idp_screen_include_and_needs_review.csv
│   ├── idp_screen_excluded_keyword_matches.csv
│   ├── idp_screen_per_agency_counts.csv
│   ├── idp_screen_paper_tools_lookup.csv
│   ├── idp_screen_step_counts.csv
│   ├── idp_screen_duplicates_removed.csv
│   ├── idp_screen_all_tables.xlsx
│   ├── run_log.txt
│   └── author_decisions/README.md PENDING: the author's screening decisions will be added later
├── docs/
│   ├── METHODS.md                 sources, fields, keywords, rules, protocol change log, step counts, limitations
│   ├── CODEBOOK.md                every column of the raw and derived tables
│   ├── DATA_CITATION.md           citations for the upstream datasets and this package (DOI placeholder)
│   ├── DATA_AVAILABILITY.md       DRAFT data availability statement
│   └── VERIFICATION_LOG.md        checksum re-verification record
└── tools/
    ├── README.md
    └── IDP_Screener.html          offline author screening interface (not data; see tools/README.md)
```

## Provenance

### Upstream publisher
Both repositories are in the GitHub organization **`ombegov`**. The 2025 README says "OMB compiled this repository from agencies' publicly available inventories". Both READMEs give the maintainer contact OFCIO_AI@omb.eop.gov (the OMB Office of the Federal CIO). The 2024 README names the maintainers as Morgan Zimmerman and Varoon Mathur. The underlying records are self-reported by each federal agency under EO 13960, the Advancing American AI Act, and OMB M-24-10 (2024) or M-25-21 (2025). The reporting federal agencies are credited as the authors of those records. The U.S. Office of Management and Budget is credited as compiler and publisher. The Federal CIO Council is not named as publisher in either README and is not credited.

### Sources and pinned versions
| Dataset | Repository | Pinned commit (commit time) | Upstream "as of" date |
|---|---|---|---|
| 2024 Federal Agency AI Use Case Inventory | https://github.com/ombegov/2024-Federal-AI-Use-Case-Inventory | `4a29d132291261d4829b187acd8af618e7295294` (2025-01-23 13:14 PST): "Update README.md with new use case totals and summary statistics" | README: "As of January 23, 2025": 41 agency submissions, 2133 AI use cases, 351 rights- and/or safety-impacting |
| 2025 Federal Agency AI Use Case Inventory | https://github.com/ombegov/2025-Federal-Agency-AI-Use-Case-Inventory | `06c7ebeef5b376524211042bd9673b2a7fefd3e3` (2026-05-14 05:36 PDT): "Update README.md" | README: "As of April 13, 2026": 56 agency submissions in total, 41 with individual use cases, 46 with COTS, 3,611 individual use cases, 445 high-impact |

On 2026-11-23 both pinned commits were still the head of each repository's default branch.

**Access date:** 2026-11-23. First fetch around 19:10 PST; re-verified 19:36–19:39 PST.

### Step-by-step download procedure (reproducible)
Requirements: `git`, `bash`, `sha256sum` (GNU coreutils), and internet access. No account or login is needed.

**Option A: scripted (recommended).** This is the same procedure as `code/download_sources.sh`.
```bash
mkdir fresh_raw && cd fresh_raw
git clone https://github.com/ombegov/2024-Federal-AI-Use-Case-Inventory.git _src24
git -C _src24 checkout 4a29d132291261d4829b187acd8af618e7295294
git clone https://github.com/ombegov/2025-Federal-Agency-AI-Use-Case-Inventory.git _src25
git -C _src25 checkout 06c7ebeef5b376524211042bd9673b2a7fefd3e3
# copy the files listed in the tree above into
#   ombegov_2024-Federal-AI-Use-Case-Inventory_4a29d13/ and
#   ombegov_2025-Federal-Agency-AI-Use-Case-Inventory_06c7ebe/
# keeping the upstream relative paths (download_sources.sh does this), then:
sha256sum -c /path/to/package/raw/SHA256SUMS.txt      # every line should print OK
```
or simply: `bash code/download_sources.sh /tmp/fresh_raw && (cd /tmp/fresh_raw && sha256sum -c /path/to/package/raw/SHA256SUMS.txt)`

**Option B: single files with curl.** Raw URLs are pinned to the commit:
```bash
B24=https://raw.githubusercontent.com/ombegov/2024-Federal-AI-Use-Case-Inventory/4a29d132291261d4829b187acd8af618e7295294
B25=https://raw.githubusercontent.com/ombegov/2025-Federal-Agency-AI-Use-Case-Inventory/06c7ebeef5b376524211042bd9673b2a7fefd3e3
curl -fLO "$B24/data/2024_consolidated_ai_inventory_raw_v2.csv"
curl -fLO "$B25/Data/2025_individually_reported_AI_use_cases.csv"
curl -fLO "$B25/Data/2025_consolidated_COTS_AI_use_cases.csv"
sha256sum 2024_consolidated_ai_inventory_raw_v2.csv 2025_individually_reported_AI_use_cases.csv 2025_consolidated_COTS_AI_use_cases.csv
# expected:
# 789e1bac6d2551e8f90e5cfc5feb37ac23c6ca9f302f5af92fea8a577caa0a83  2024_consolidated_ai_inventory_raw_v2.csv
# a62721202ca4b110ce3c53ffdb688d05ad27a35971a7afda4f1179b2493e31d0  2025_individually_reported_AI_use_cases.csv
# bd18984bdc41f8fc818c9d145de78ebe2563ee0ffab29fe7e96de4c223c8ba17  2025_consolidated_COTS_AI_use_cases.csv
```
(Paths that contain spaces, such as `Reporting Instructions/…`, must be URL-encoded as `%20` for curl.)

**Step 3: run the screen.** `cd code && pip install -r requirements.txt && python3 screen.py > ../derived/run_log.txt`. See `code/RUN.md`.

**Re-verification result (2026-11-23):** a from-scratch re-download by both git and curl matched every stored checksum: 18/18 files via the script, 11/11 against the first working copy, and 3/3 CSVs via curl. Re-running screen.py reproduced all derived CSVs byte for byte. Details are in `docs/VERIFICATION_LOG.md`.

### What each raw file is
| File (under the repo folder) | What it is |
|---|---|
| 2024 `data/2024_consolidated_ai_inventory_raw_v2.csv` | OMB-consolidated 2024 inventory, "v2", added in commit 739f686 ("Add updated 2024 Inventory with 376 additional use cases"). 2,133 rows × 62 columns. **Analysed.** |
| 2024 `data/2024_consolidated_ai_inventory_raw_v2.xls` | Spreadsheet version of the same table (not analysed) |
| 2024 `validation/data_dictionary.yaml` | Upstream field definitions for 2024 |
| 2024 `README.md` | Upstream README: scope, summary counts, exclusions, contact |
| 2025 `Data/2025_individually_reported_AI_use_cases.csv` | OMB-consolidated 2025 individually reported use cases. 3,611 rows × 36 columns. **Analysed (main).** |
| 2025 `Data/2025_individually_reported_AI_use_cases.xlsx` | Spreadsheet version, with the long OMB template headers and strings (not analysed) |
| 2025 `Data/2025_consolidated_COTS_AI_use_cases.csv` / `.xlsx` | 2025 consolidated COTS reporting: 900 rows (45 agencies × 20 fixed categories) × 5 columns. **CSV analysed as a supplement** (0 keyword matches) |
| 2025 `Data/README_datasets.md` | Upstream description of the datasets folder |
| 2025 `Validation/data_dictionary.md` / `.json` | Upstream column definitions, types, valid values and recodings |
| 2025 `Validation/data_sourcing_summary.md` | Per-agency source URLs, retrieval method and dates, and column remappings used by OMB |
| 2025 `Validation/data_standardization_report.md`, `…_AI_COTS.md` | Upstream recoding and standardization logs |
| 2025 `Validation/README.md` | Upstream overview of the Validation folder |
| 2025 `Reporting Instructions/*.pdf`, `Reporting Instructions.md` | OMB's 2025 reporting guidance to agencies |
| 2025 `README.md` | Upstream README: summary counts, reporting changes, exclusion criteria, schedule |

The 2024 repository also contains `2023_consolidated_ai_inventory_raw.csv` and the older `2024_consolidated_ai_inventory_raw.csv/.xls` (without "v2"). These were **not used** and are not included.

### Known upstream caveats
- **Self-reported.** Agencies report their own use cases. OMB compiled and standardized them. Some details may be withheld from public release (README). Out of scope upstream: National Security Systems, Intelligence Community systems, most R&D (2024) or basic/applied research (2025), Department of Defense (2024 README) or "Department of War" (2025 README) use cases, and use cases whose release would conflict with law or policy (README exclusion sections). Coverage is therefore incomplete by design.
- **Revisions.** Each repository is a snapshot "as of" the README date (2024: January 23, 2025; 2025: April 13, 2026). The 2025 README says "Updates to this repository will be processed on a rolling basis", so later commits may change the data. Always cite the commit.
- **Missing IDs.** The 2024 consolidated file has no use case ID column. In 2025, 704 of 3,611 rows have a blank `id`: all ED, GSA, HHS, SSA, STATE and TVA rows. IDs are not unique across agencies.
- **Encoding.** The 2024 CSV is not UTF-8. It decodes as Windows-1252 (inferred; not declared upstream). The 2025 CSVs are UTF-8 with BOM, read as `utf-8-sig` per the upstream data dictionary.
- **Recoding.** 2025 multiple-choice values were recoded upstream to valid options, and the CSV uses shorter strings than the XLSX (Validation README and data_standardization_report.md).
- **Comparability.** The impact designation changed between years: rights/safety-impacting (M-24-10) in 2024, high-impact (M-25-21) in 2025. The 2025 questionnaire has fewer fields. Agency names differ across years, and the 2024 file has 42 distinct `Agency` strings against 41 submissions in the README.
- **Small upstream documentation inconsistencies.** The 2025 README's "Repository Structure" lists `Guidance_on_2025_Agency_Artificial_Intelligence_Reporting.pdf` and `data_standardization_report_COTS_AI.md`. The files are actually named `Guidance on 2025 Agency Artificial Intelligence Reporting (FINAL).pdf` and `data_standardization_report_AI_COTS.md`.

## License
- **Upstream data (`raw/`):** at the pinned commits, **neither repository contains a LICENSE file, and neither README states license terms** (checked 2026-11-23; see docs/VERIFICATION_LOG.md). Works of the U.S. federal government are generally not subject to copyright in the United States under **17 U.S.C. §105**, so the inventories are likely public domain in the U.S. This status is **likely, not legally verified.** The text was written by many agencies and may include contractor-written or third-party material, and §105 does not by itself settle status outside the U.S. The CC BY 4.0 license applies only to this package's own contributions, not to the `raw/` upstream files.
- **Data and documentation:** `derived/` and `docs/` are licensed under CC BY 4.0. See `LICENSE-DATA` and https://creativecommons.org/licenses/by/4.0/legalcode.
- **Code:** `code/` and `tools/` are licensed under the MIT License, copyright 2026 Emtiaz Ahamed. See `LICENSE`.

## Status and limitations
- `derived/` holds **rule-based** screen results only. The author's own screening decisions are **pending** and will be added in v1.1.
- The keyword screen finds only what agencies wrote. Some known IDP tools have no keyword match, and some R1 includes are false positives. See docs/METHODS.md §7–8.
- Items described as unverified in this package, including the upstream public-domain status under 17 U.S.C. §105, are likely, not legally verified.
