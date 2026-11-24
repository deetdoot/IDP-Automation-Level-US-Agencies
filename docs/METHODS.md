# METHODS: keyword screen of the U.S. federal AI use case inventories for intelligent document processing (IDP)

Package version 1.0, 2026-11-23 (America/Los_Angeles, PST, UTC-8). Generative AI tools assisted with data retrieval, running the rule-based screen, and drafting documentation under the author's direction; the author defined the screening rules and classes and is responsible for all content.

## 1. Sources
| Dataset | Repository @ pinned commit | Upstream version statement | File(s) used |
|---|---|---|---|
| 2024 Federal Agency AI Use Case Inventory | github.com/ombegov/2024-Federal-AI-Use-Case-Inventory @ `4a29d132291261d4829b187acd8af618e7295294` (commit 2025-01-23 13:14 PST) | README: "As of January 23, 2025": 41 agency submissions, 2133 AI use cases | `data/2024_consolidated_ai_inventory_raw_v2.csv` (the "v2" file from commit 739f686, "Add updated 2024 Inventory with 376 additional use cases") |
| 2025 Federal Agency AI Use Case Inventory | github.com/ombegov/2025-Federal-Agency-AI-Use-Case-Inventory @ `06c7ebeef5b376524211042bd9673b2a7fefd3e3` (commit 2026-05-14 05:36 PDT) | README: "As of April 13, 2026": 41 submissions with individually reported use cases, 3,611 use cases, 445 high-impact | `Data/2025_individually_reported_AI_use_cases.csv` (main); `Data/2025_consolidated_COTS_AI_use_cases.csv` (supplementary) |

Downloaded 2026-11-23. Checksums are in `raw/SHA256SUMS.txt`. For a from-scratch re-download check, see `docs/VERIFICATION_LOG.md`.

## 2. Fields searched (case-insensitive Python `re`)
- 2024: `Use Case Name`; `Use Case Topic Area` + `Other (Use Case Topic Area)`; `What is the intended purpose and expected benefits of the AI?`; `Describe the AI system's outputs.` The file has no technique field and no use case ID.
- 2025: `use_case_name`; `topic_area`; `classification`; `problem_solved` + `benefits`; `system_outputs`.
- Not searched: data descriptions, risk/assessment text, vendor names, contact fields.
- COTS 2025 (supplementary): `AI Use Case` + `Name of Commercial Product or Service Used`.

## 3. Keyword lists (`code/keywords.json`)
The exact regexes are in `code/keywords.json`. They are summarised here.
- **Strong:** OCR; optical character recognition; intelligent character recognition; text recognition; handwrit*; intelligent document processing; IDP; document processing; document understanding; document(s) classif*; document extraction; text extraction; extract… from … document/form/PDF/scan/paper; form(s) processing; scanned; digitiz*/digitis*; paper-based / paper forms|documents|records|files|applications; key-value; table extraction; redact*; PII detection, or detect|identify|flag|screen … PII.
- **Weak:** data extraction; information extraction; records.
- **Document noun** (used by R3): documents, forms, PDFs, paper, letters, correspondence, submissions, application packages/forms, case files, files.
- **Exclusion triggers, v1:** chatbot / virtual assistant / virtual agent / conversational; code assistant / generation / completion, GitHub Copilot; speech / audio / voice; non-document image/video (satellite, aerial, imagery, video, camera, x-ray, radiograph, mammography, CT, MRI, facial / face recognition, lidar, drone, wildlife, body scan); general-purpose LLM / productivity (ChatGPT, Gemini, Copilot, workplace productivity, enterprise generative / GenAI / LLM).
- **Exclusion triggers, v2 amendment:** license plate / plate reader, pathology, on-person, dispensing; "co-pilot"; "office of civil rights" (an acronym collision with OCR); network traffic, secure access service edge, compromise email, phishing.

## 4. Rules
| Rule | Decision | Condition |
|---|---|---|
| R1 | include | at least one strong keyword and no exclusion trigger |
| R2 | needs author review | at least one strong keyword and at least one exclusion trigger |
| R3 | needs author review | weak keyword(s) only, a document noun present, no exclusion trigger |
| R4a | exclude | weak keyword(s) only, no document noun |
| R4b | exclude | weak keyword(s) only, at least one exclusion trigger |
| de-dup | n/a | within each year, rows with identical normalized (lower-case, non-word characters collapsed) agency + name + purpose; first row kept |

These are rule-based decisions only. No row was included or excluded by hand. Author screening of the include and needs-review rows is **pending** (see `derived/author_decisions/`).

## 5. Change log of the screening protocol
1. **Keyword lists and v1 exclusion triggers** were written before the first screening run.
2. **First run (v1).** The author/assistant read the R1 (include) output and found clear non-document false positives, such as license-plate OCR, body scanners, and "Office of Civil Rights" matched as OCR.
3. **Amendment (v2), made after the first run.** Exclusion triggers were added (section 3). The amendment only moved rows from *include* to *needs author review*: 5 rows in 2024 and 9 in 2025, computed from `decision_v1` vs `decision`. It moved no row to *exclude* and changed no other decision. The v1 decision is kept for every row in `decision_v1`.
4. **No changes after v2.** The v2 run is the one shipped in `derived/`.

> **Timestamp caveat (unverified):** `keywords.json` contains the annotations `"frozen_at": "2026-11-23 19:20 PST (before any screening was run)"` and an amendment note "Added 2026-11-23 ~19:35 PST". These clock times **do not agree with the file system**: the raw files were written at 19:10 PST, `keywords.json` and `screen.py` were last modified at 19:12:53 PST, and the v2 outputs at 19:12:57 PST on 2026-11-23. The v1 output files were overwritten and no longer exist. The *order* of events (keywords → v1 run → v2 amendment) is the assistant's working record, not an independently timestamped log. Do not cite the clock times in the paper. `keywords.json` is shipped unchanged so that its checksum matches the run.

## 6. Step counts (from `derived/idp_screen_step_counts.csv`)
| Step | 2024 | 2025 |
|---|---|---|
| Total entries in file | 2133 | 3611 |
| Keyword matches (any strong or weak keyword) | 228 | 294 |
| After de-duplication | 226 | 294 |
| Include (R1), v2 triggers | 99 | 128 |
| Needs author review (R2/R3), v2 | 45 | 75 |
| Exclude (R4a/R4b) | 82 | 91 |
| Include under v1 triggers / needs review under v1 | 104 / 40 | 137 / 66 |
| Include and `development_stage` = Deployed | n/a | 60 |

Needs-review rows by rule (from the `reason` column): 2024 has 25 R2 and 20 R3; 2025 has 35 R2 and 40 R3. The 2025 COTS file (900 rows: 45 agencies × 20 fixed generic categories. There are 21 distinct strings because 2 rows have a leading space) had **0** keyword matches.

## 7. Paper tools
`derived/idp_screen_paper_tools_lookup.csv` locates IMAGEN (SSA), VA-24-2545, State AI-Augmented Declassification Review, VA-24-4722 (ADS), DHS-16 (USCIS ELIS Evidence Classifier), TREAS-IRS-64, SSA PATH, and NARA-0005 / NARA-0011 in each inventory. State Declassification and SSA PATH have no keyword match. IMAGEN and VA ADS (2025) match only the weak keyword "records".

## 8. Limitations
- The inventories are self-reported by agencies and then compiled and standardized by OMB. A keyword screen finds only what the agency wrote.
- The 2024 file has no use case IDs. 704 of the 3,611 rows in the 2025 file have a blank `id`. IDs are not globally unique.
- Agency names differ between years. Use `agency_abbr` with care.
- The impact fields are not comparable across years (M-24-10 rights/safety-impacting vs. M-25-21 high-impact).
- R1 includes still contain false positives, for example DHS-4 (PII in cybersecurity data) and VA-25-1102 (an OCR mention in an embedding project). Author review is needed before any count is reported as "IDP use cases".
- The 2024 CSV is read as latin-1, so cp1252 punctuation (curly quotes, dashes) in text fields is kept as C1 control characters. This does not affect any keyword regex.
- The Keywords tab of the XLSX lists the v1 exclusion triggers only. The v2 additions are in `code/keywords.json` and in this document.

## 9. Author screening (pending)
The author will screen the 205 rows in the 2025 include and needs-review set, and optionally the others, using `tools/IDP_Screener.html`. He will record include / exclude / unsure, capability classes, and an exclusion reason. The results will be added to `derived/author_decisions/` in a later version.
