# CODEBOOK

Every column in the raw and derived tabular files in this package. Version 1.0, 2026-11-23.

Conventions: *Type* for raw files is the upstream-declared type where the upstream data dictionary gives one; otherwise it is `text` (all files are read by `code/screen.py` as strings, `dtype=str`). *Non-empty* is the number of rows with a non-blank value, computed on 2026-11-23 from the file in `raw/`. Descriptions for raw columns are quoted or condensed from the upstream data dictionaries; nothing has been added to them. Where no upstream description exists, this is stated.

## 1. Raw files

### 1.1 `raw/ombegov_2024-Federal-AI-Use-Case-Inventory_4a29d13/data/2024_consolidated_ai_inventory_raw_v2.csv`

62 columns, 2,133 data rows. Encoding: not declared upstream. The file does not decode as UTF-8 (byte 0x92 at offset 271) but does decode as Windows-1252 (cp1252), so cp1252 is inferred. screen.py reads it with `encoding="latin-1"`, so bytes 0x80–0x9F such as curly quotes stay C1 control characters in the text fields. Only the 0x92 quote in headers is changed to `'`. The header row holds the OMB questionnaire wording. There is no use case ID column. Header text is shown as decoded with cp1252. Some headers repeat in the file (for example "If Other, please explain."). pandas renames the repeats `.1`, `.2`, … when it reads them; screen.py uses none of the repeated columns.

Upstream field definitions are in `raw/ombegov_2024-Federal-AI-Use-Case-Inventory_4a29d13/validation/data_dictionary.yaml`, which uses numbered short names (e.g. `2_use_case_name`, `4_bureau`) rather than the CSV header text. **This codebook does not map the CSV headers to those YAML names.** The mapping has not been verified field by field. The header text is the question that agencies answered, so it is given as the description.

| # | Column (header as in file) | Type | Non-empty | Description | Used by screen.py |
|---|---|---|---|---|---|
| 1 | Use Case Name | text | 2133 | Upstream questionnaire field (header text). No separate description verified. | name; searched |
| 2 | Agency | text | 2133 | Upstream questionnaire field (header text). No separate description verified. | agency |
| 3 | Agency Abbreviation | text | 2133 | Upstream questionnaire field (header text). No separate description verified. | agency_abbr |
| 4 | Bureau | text | 2108 | Upstream questionnaire field (header text). No separate description verified. | bureau |
| 5 | Use Case Topic Area | text | 2092 | Upstream questionnaire field (header text). No separate description verified. | topic; searched |
| 6 | Other (Use Case Topic Area) | text | 198 | Upstream questionnaire field (header text). No separate description verified. | topic; searched |
| 7 | Is the AI use case found in the below list of general commercial AI products and services? | text | 2086 | Upstream questionnaire field (header text). No separate description verified. |  |
| 8 | What is the intended purpose and expected benefits of the AI? | text | 2122 | Upstream questionnaire field (header text). No separate description verified. | purpose; searched |
| 9 | Describe the AI system’s outputs. | text | 2086 | Upstream questionnaire field (header text). No separate description verified. | outputs; searched |
| 10 | Stage of Development | text | 2129 | Upstream questionnaire field (header text). No separate description verified. | stage |
| 11 | Is the AI use case rights-impacting, safety-impacting, both, or neither? | text | 2094 | Upstream questionnaire field (header text). No separate description verified. | impact_flag |
| 12 | Date Initiated | text | 1271 | Upstream questionnaire field (header text). No separate description verified. |  |
| 13 | Date when Acquisition and/or Development began | text | 982 | Upstream questionnaire field (header text). No separate description verified. |  |
| 14 | Date Implemented | text | 679 | Upstream questionnaire field (header text). No separate description verified. |  |
| 15 | Date Retired | text | 142 | Upstream questionnaire field (header text). No separate description verified. |  |
| 16 | Was the AI system involved in this use case developed (or is it to be developed) under contract(s) or in-house?  | text | 1153 | Upstream questionnaire field (header text). No separate description verified. |  |
| 17 | Provide the Procurement Instrument Identifier(s) (PIID) of the contract(s) used. | text | 501 | Upstream questionnaire field (header text). No separate description verified. |  |
| 18 | Is this AI use case supporting a High-Impact Service Provider (HISP) public-facing service? | text | 1055 | Upstream questionnaire field (header text). No separate description verified. |  |
| 19 | Which HISP is the AI use case supporting? | text | 133 | Upstream questionnaire field (header text). No separate description verified. |  |
| 20 | Which public-facing service is the AI use case supporting? | text | 66 | Upstream questionnaire field (header text). No separate description verified. |  |
| 21 | Does this AI use case disseminate information to the public? | text | 1029 | Upstream questionnaire field (header text). No separate description verified. |  |
| 22 | How is the agency ensuring compliance with Information Quality Act guidelines, if applicable? | text | 276 | Upstream questionnaire field (header text). No separate description verified. |  |
| 23 | Does this AI use case involve personally identifiable information (PII) that is maintained by the agency? | text | 1049 | Upstream questionnaire field (header text). No separate description verified. |  |
| 24 | Has the Senior Agency Official for Privacy (SAOP) assessed the privacy risks associated with this AI use case? | text | 988 | Upstream questionnaire field (header text). No separate description verified. |  |
| 25 | Do you have access to an enterprise data catalog or agency-wide data repository that enables you to identify whether or not the necessary datasets exist and are ready to develop your use case? | text | 1204 | Upstream questionnaire field (header text). No separate description verified. |  |
| 26 | If Other, please explain. | text | 160 | Upstream questionnaire field (header text). No separate description verified. |  |
| 27 | Describe any agency-owned data used to train, fine-tune, and/or evaluate performance of the model(s) used in this use case. | text | 822 | Upstream questionnaire field (header text). No separate description verified. |  |
| 28 | Is there available documentation for the model training and evaluation data that demonstrates the degree to which it is appropriate to be used in analysis or for making predictions? | text | 1157 | Upstream questionnaire field (header text). No separate description verified. |  |
| 29 | Which, if any, demographic variables does the AI use case explicitly use as model features? | text | 177 | Upstream questionnaire field (header text). No separate description verified. |  |
| 30 | If Other, please explain. | text | 82 | Upstream questionnaire field (header text). No separate description verified. |  |
| 31 | Does this project include custom-developed code? | text | 1035 | Upstream questionnaire field (header text). No separate description verified. |  |
| 32 | Does the agency have access to the code associated with the AI use case? | text | 1029 | Upstream questionnaire field (header text). No separate description verified. |  |
| 33 | If the code is open-source, provide the link for the publicly available source code. | text | 70 | Upstream questionnaire field (header text). No separate description verified. |  |
| 34 | Does this AI use case have an associated Authority to Operate (ATO) for an AI system? | text | 1170 | Upstream questionnaire field (header text). No separate description verified. |  |
| 35 | System Name | text | 755 | Upstream questionnaire field (header text). No separate description verified. |  |
| 36 | How long have you waited for the necessary developer tools to implement the AI use case?  | text | 1040 | Upstream questionnaire field (header text). No separate description verified. |  |
| 37 | For this AI use case, is the required IT infrastructure provisioned via a centralized intake form or process inside the agency? | text | 1181 | Upstream questionnaire field (header text). No separate description verified. |  |
| 38 | If Other, please explain. | text | 119 | Upstream questionnaire field (header text). No separate description verified. |  |
| 39 | Do you have a process in place to request access to computing resources for model training and development of the AI involved in this use case? | text | 1176 | Upstream questionnaire field (header text). No separate description verified. |  |
| 40 | If Other, please explain. | text | 142 | Upstream questionnaire field (header text). No separate description verified. |  |
| 41 | Has communication regarding the provisioning of your requested resources been timely? | text | 1147 | Upstream questionnaire field (header text). No separate description verified. |  |
| 42 | If Other, please explain. | text | 214 | Upstream questionnaire field (header text). No separate description verified. |  |
| 43 | How are existing data science tools, libraries, data products, and internally-developed AI infrastructure being re-used for the current AI use case? | text | 1116 | Upstream questionnaire field (header text). No separate description verified. |  |
| 44 | Has information regarding the AI use case, including performance metrics and intended use of the model, been made available for review and feedback within the agency? | text | 1135 | Upstream questionnaire field (header text). No separate description verified. |  |
| 45 | Has your agency requested an extension to implement the minimum risk management practices for this AI use case? | text | 632 | Upstream questionnaire field (header text). No separate description verified. |  |
| 46 | Has an AI impact assessment been conducted for this AI use case? | text | 277 | Upstream questionnaire field (header text). No separate description verified. |  |
| 47 | Has the AI use case been tested in operational or real-world environments to understand the performance and impact it may have on affected individuals or communities? | text | 215 | Upstream questionnaire field (header text). No separate description verified. |  |
| 48 | What are the key risks from using the AI for this particular use case and how were they identified? | text | 232 | Upstream questionnaire field (header text). No separate description verified. |  |
| 49 | Has an independent evaluation of the AI use case been conducted? | text | 239 | Upstream questionnaire field (header text). No separate description verified. |  |
| 50 | Is there a process to monitor performance of the AI system’s functionality and changes to its impact on rights or safety as part of the post-deployment plan for the AI use case? | text | 215 | Upstream questionnaire field (header text). No separate description verified. |  |
| 51 | For this particular use case, can the AI carry out a decision or action without direct human involvement that could result in a significant impact on rights or safety? | text | 272 | Upstream questionnaire field (header text). No separate description verified. |  |
| 52 | If Other, please explain. | text | 6 | Upstream questionnaire field (header text). No separate description verified. |  |
| 53 | How is the agency providing reasonable and timely notice regarding the use of AI when people interact with an AI-enabled service as a result of this AI use case? | text | 260 | Upstream questionnaire field (header text). No separate description verified. |  |
| 54 | If Other, please explain. | text | 88 | Upstream questionnaire field (header text). No separate description verified. |  |
| 55 | Is the AI used to significantly influence or inform decisions or actions that could have an adverse or negative impact on specific individuals or groups? | text | 272 | Upstream questionnaire field (header text). No separate description verified. |  |
| 56 | What steps has the agency taken to detect and mitigate significant disparities in the model’s performance across demographic groups for this AI use case? | text | 170 | Upstream questionnaire field (header text). No separate description verified. |  |
| 57 | What steps has the agency taken to consult and incorporate feedback from groups affected by this AI use case? | text | 262 | Upstream questionnaire field (header text). No separate description verified. |  |
| 58 | If Other, please explain. | text | 71 | Upstream questionnaire field (header text). No separate description verified. |  |
| 59 | Is there an established fallback and escalation process for this AI use case in the event that an impacted individual or group would like to appeal or contest the AI system’s outcome? | text | 209 | Upstream questionnaire field (header text). No separate description verified. |  |
| 60 | If No, please explain. | text | 68 | Upstream questionnaire field (header text). No separate description verified. |  |
| 61 | Where practicable and consistent with applicable law and governmentwide policy, is there an established mechanism for individuals to opt-out from the AI functionality in favor of a human alternative? | text | 261 | Upstream questionnaire field (header text). No separate description verified. |  |
| 62 | If Other, please explain. | text | 83 | Upstream questionnaire field (header text). No separate description verified. |  |

### 1.2 `raw/ombegov_2025-Federal-Agency-AI-Use-Case-Inventory_06c7ebe/Data/2025_individually_reported_AI_use_cases.csv`

36 columns, 3,611 data rows. Encoding UTF-8 with BOM (`utf-8-sig`), per the upstream data dictionary. Types and instructions below are condensed from `raw/ombegov_2025-Federal-Agency-AI-Use-Case-Inventory_06c7ebe/Validation/data_dictionary.md` ("Original Excel Header" is the OMB template header).

| # | Column | Upstream type | Non-empty | Original Excel header | Upstream instruction (condensed) | Used by screen.py |
|---|---|---|---|---|---|---|
| 1 | `agency` | free_text | 3611 | (generated by OMB) | This column was generated by OMB. The abbreviated name of the reporting agency (e.g., USDA). | agency_abbr |
| 2 | `agency_name` | free_text | 3611 | (generated by OMB) | This column was generated by OMB. The full name of the reporting agency (e.g., The Department of Agriculture). | agency |
| 3 | `id` | structured_text | 2907 | Use Case ID  [Agency Abbrev.] – [#] | Unique identifier for AI use case. Use cases should maintain the same ID if included in previous year’s inventory. However, in their public inventories, agencies are permitted to remove the “Use Case ID” column. Required: Yes | use_case_id |
| 4 | `use_case_name` | free_text | 3610 | Use Case Name | Title of the AI use case. Required: Yes | name; searched |
| 5 | `agency_bureau` | free_text | 3554 | Bureau/Component | Specific organization(s) within the agency responsible for the AI use case. Required: Yes | bureau |
| 6 | `contact_email` | free_text | 2496 | Email Address | Email address of the individual or team who works with or is responsible for the AI use case. However, in their public inventories, agencies may replace the “Email Address” column with an email address designated for public inquiries. Required: Yes |  |
| 7 | `is_withheld` | multiple_choice | 2479 | Should this AI use case be withheld from public reporting? | Whether the AI use case should be withheld from public reporting and the reason for why. Required: Yes |  |
| 8 | `development_stage` | multiple_choice | 3273 | Stage of Development | The AI use case’s current stage of development. Required: Yes | stage |
| 9 | `is_high_impact` | multiple_choice | 3185 | Is the AI use case high-impact? | Whether the AI use case is high-impact, as defined in Section 5 of the appendix to OMB Memorandum M-25-21. Required: Yes | impact_flag |
| 10 | `HI_justification` | free_text | 827 | Justification | Provide a justification for why the use case is determined to be not high-impact. Required: Yes, but question should only appear if “Presumed high-impact, but determined not high-impact” is selected for the previous question. |  |
| 11 | `topic_area` | multiple_choice | 3008 | Use Case Topic Area | The topic area that most closely aligns with the AI use case. Required: Yes, for pre-deployment, pilot and deployed use cases. | topic; searched |
| 12 | `classification` | multiple_choice | 2949 | AI Classification | The classification of AI technology that most closely aligns with the AI use case. Note that an AI use case may rely on multiple classifications; however, agencies should select the choice that most closely aligns. Required: Yes, for pre-deployment, pilot a… | technique; searched |
| 13 | `problem_solved` | free_text | 3018 | What problem is the AI intended to solve? | What problem is the AI intended to solve? Required: Yes, for pre-deployment, pilot and deployed use cases. | purpose; searched |
| 14 | `benefits` | free_text | 2954 | What are the expected benefits and positive outcomes from the AI for an agency’s mission and/or the general public? | Description of the expected benefits and positive outcomes from the AI for an agency’s mission and/or the general public. Expected benefits may include, for example: cost savings, reducing customer wait times, or improving access to government benefits. Req… | purpose; searched |
| 15 | `system_outputs` | free_text | 2845 | Describe the AI system’s outputs. | Description of what the AI system outputs, whether it’s a prediction, recommendation, decision, etc. Required: Yes, for pre-deployment, pilot and deployed use cases. | outputs; searched |
| 16 | `operational_date` | date | 1402 | Date when AI use case became operational or the pilot’s start date | Date when the AI use case was fully operational or the pilot’s start date. Required: Yes, for pilot and deployed use cases. |  |
| 17 | `contracting_usage` | multiple_choice | 1604 | Was the system involved in this use case purchased from a vendor or developed under contract(s) or in-house? | Whether the system involved in the use case was developed, or is expected to be developed, exclusively with contracting resources, in-house, or a combination of both. Required: Yes, for pilot and deployed use cases. |  |
| 18 | `vendor_name` | free_text | 790 | Vendor(s) Name | Identification of the vendor(s) involved in the use case’s development and/or maintenance. Required: Yes, but question should only appear if “Purchased from a vendor” or “Developed with both contracting and in-house resources” is selected for the previous q… |  |
| 19 | `have_ato` | multiple_choice | 1542 | Does this AI use case have an associated Authorization to Operate (ATO)? | Whether the AI use case itself has an associated Authorization to Operate (ATO), or is part of another system that has an ATO. Required: Yes, for pilot and deployed use cases. |  |
| 20 | `system_name_ato` | free_text | 906 | System(s) Name | Name of the system(s) associated with this AI use case, according to the ATO. Required: Yes, but question should only appear if “Yes” is selected for the previous question and development stage is pilot or deployed. |  |
| 21 | `data_description` | free_text | 1290 | Describe any data used to  train, fine-tune, and/or  evaluate performance of the  model(s) used in this use  case. | General description of the data used in the AI’s design, development, training, testing, and operation. This should include a description of any data provided by the agency, whether the datasets are research datasets, publicly available, external, etc. and … |  |
| 22 | `link_to_data` | free_text | 206 | If the data is required to be  publicly disclosed as an  open government data asset,  provide a link to the entry on the Federal Data Catalog. | If the data is required to be publicly disclosed as an open government data asset, provide a link to the entry on the Federal Data Catalog. Required: No |  |
| 23 | `has_pii` | multiple_choice | 1511 | Does this AI use case  involve personally  identifiable information (PII)  that is maintained by the  agency? | Whether the AI use case involves personally identifiable information (PII), as defined in OMB Circular A-130. Required: Yes, for pilot and deployed use cases. |  |
| 24 | `pia_url` | free_text | 235 | If publicly available, provide  the link to the AI use case’s associated Privacy Impact Assessment (PIA). | Whether the AI use case itself has an associated PIA, or is part of another system that has a PIA. Required: No |  |
| 25 | `demographic_features` | select_multiple | 3611 | Which, if any, demographic  variables does the AI use  case explicitly use as model  features? | Identification of the demographic features explicitly utilized in the AI use case’s data/model(s). Required: Yes, for pilot and deployed use cases. |  |
| 26 | `has_custom_code` | multiple_choice | 1712 | Does this project include  custom-developed code? | Whether this AI project includes “custom developed code,” as defined in OMB Memorandum M-25-21. Required: Yes, for pilot and deployed use cases. |  |
| 27 | `code_url` | free_text | 248 | If the code is open source, provide the link for the  publicly available source  code. | Link to publicly available source code for the AI use case, if available. Required: No |  |
| 28 | `hi_testing_conducted` | multiple_choice | 258 | Has pre-deployment testing been conducted for this AI  use case?      Practice: Complete AI Impact Assessment | Whether pre-deployment testing has been conducted for the AI use case, consistent with Section 4(b)(i) of the appendix to OMB Memorandum M-25-21. Required: Yes, only for high-impact deployed use cases |  |
| 29 | `hi_assessment_completed` | multiple_choice | 236 | Has an AI impact assessment been completed for this AI use case?     Practice: Complete AI Impact Assessment | Whether an AI impact assessment for the AI use case has been completed, consistent with Section 4(b)(ii) of the appendix to OMB Memorandum M-25- 21. Required: Yes, only for high-impact deployed use cases |  |
| 30 | `hi_potential_impacts` | free_text | 247 | What are the potential  impacts of using the AI for  this particular use case and  how were they identified?        Subpractice: Complete AI  Impact Assessment | Identification of the reasonably foreseeable impacts from using the AI use case, to include impacts on the privacy, civil rights, and civil liberties of the public. Required: Yes, only for high-impact deployed use cases |  |
| 31 | `hi_independent_review` | multiple_choice | 266 | Has as independent review  of the AI use case been  conducted?         Sub practice Complete AI  Impact Assessment | Whether an independent review of the AI use case has been conducted by an office, oversight board, or individual within the agency who has not been involved in the AI’s development.Required: Yes, only for high-impact deployed use cases |  |
| 32 | `hi_ongoing_monitoring` | multiple_choice | 267 | Is there a process to conduct ongoing monitoring to identify any adverse impacts to the performance and security of the AI functionality, as well as to privacy, civil rights, and civil liberties?  Practice: Conduct Ongoing Monitoring for Performance and Potential Adverse Impacts | Whether a process to conduct ongoing monitoring for the AI use case has been established, consistent with Section 4(b)(iii) of the appendix to OMB Memorandum M-25-21. Required: Yes, only for high-impact deployed use cases |  |
| 33 | `hi_training_established` | multiple_choice | 281 | Has the agency established sufficient and periodic  training for operators of the  AI to interpret and act on the  its output and managed associated risks?   Practice: Ensure Adequate Human Training and Assessment | Whether sufficient and periodic training for operators of the AI use case has been established, consistent with Section 4(b)(iv) of the appendix to OMB Memorandum M-25-21. Required: Yes, only for high-impact deployed use cases |  |
| 34 | `hi_failsafe_presence` | multiple_choice | 291 | Does this AI use case have an appropriate fail-safe that minimizes the risk of significant harm?      Practice: Provide Additional Human Oversight, Intervention, and Accountability | Whether the AI use case has an appropriate fail-safe that minimizes the risk of significant harm, consistent with Section 4(b)(v) of the appendix to OMB Memorandum M-25-21. Required: Yes, only for high-impact deployed use cases |  |
| 35 | `hi_appeal_process` | multiple_choice | 290 | Is there an established appeal process in the event that an impacted individual would like to appeal or  contest the AI system’s  outcome?   Practice: Offer Consistent Remedies or Appeals | Whether there is an established appeal process for this AI use case in the event that an impacted individual would like to appeal or contest the AI system’s outcome, consistent with Section 4(b)(vi) of the appendix to OMB Memorandum M-25-21. Required: Yes, … |  |
| 36 | `hi_public_consultation` | select_multiple | 3611 | What steps has the agency taken to consult and incorporate feedback from end users of this AI use case and the public?     Practice: Consult and Incorporate Feedback from End Users and the Public | Identification of what steps the agency has taken to consult and incorporate feedback from end users of this AI use case and the public, consistent with Section 4(b)(vii) of the appendix to OMB Memorandum M-25-21. Required: Yes, only for high-impact deploye… |  |

### 1.3 `raw/ombegov_2025-Federal-Agency-AI-Use-Case-Inventory_06c7ebe/Data/2025_consolidated_COTS_AI_use_cases.csv`

5 columns, 900 data rows: one row per agency (45 agencies) × each of 20 fixed commercial off-the-shelf (COTS) use case categories. `AI Use Case` has 21 distinct strings because 2 rows of "Improving the quality of written communications using AI tools." have a leading space. Upstream standardization notes are in `Validation/data_standardization_report_AI_COTS.md`. The upstream data dictionary does not describe these columns individually; descriptions below are taken from the column headers only.

| # | Column | Type | Non-empty | Description | Used by screen.py |
|---|---|---|---|---|---|
| 1 | Agency | text | 900 | Reporting agency. |  |
| 2 | AI Use Case | text | 900 | One of the fixed COTS use case categories in the OMB template. | searched (supplementary) |
| 3 | Agency Use (Y/N)? | text | 884 | Whether the agency reports using AI for this category (Y/N; standardized upstream). |  |
| 4 | Name of Commercial Product or Service Used | text | 446 | Free text product/service name(s). | searched (supplementary) |
| 5 | Estimated # of Licenses/Users | text | 436 | Banded estimate (e.g. 5001-10,000, 10,000-50,000, 50,000+, per the upstream standardization report). |  |

The `.xls`/`.xlsx` files in `raw/` are the upstream spreadsheet versions of the same tables. They are kept for completeness and are not read by screen.py. They are not identical to the CSVs. The upstream Validation/README.md says the .xlsx files use the longer OMB template column names and strings, and the .csv files use shorter recoded ones. This package has not compared them cell by cell.

## 2. Derived files (`derived/`, written by `code/screen.py`)

### 2.1 `idp_screen_include_and_needs_review.csv` and `idp_screen_excluded_keyword_matches.csv`

Same 19 columns. The first file holds rows with `decision` = `include` or `needs author review` (2024: 144, 2025: 203). The second holds rows with `decision` = `exclude` (2024: 82, 2025: 91). Both cover keyword-matched, de-duplicated rows of the 2024 and 2025 individual inventories.

| Column | Type | Description | Source field(s) |
|---|---|---|---|
| year | text (`2024`/`2025`) | Inventory year | which raw file |
| agency | text | Full agency name | 2024 `Agency`; 2025 `agency_name` |
| agency_abbr | text | Agency abbreviation | 2024 `Agency Abbreviation`; 2025 `agency` |
| bureau | text | Bureau/component | 2024 `Bureau`; 2025 `agency_bureau` |
| use_case_id | text | Agency use case ID; always blank for 2024 (no ID column) and blank for 704 2025 rows | 2025 `id` |
| name | text | Use case name | 2024 `Use Case Name`; 2025 `use_case_name` |
| stage | text | Development stage, verbatim | 2024 `Stage of Development`; 2025 `development_stage` |
| impact_flag | text | Impact designation, verbatim. **Not comparable across years** (2024: rights/safety-impacting under M-24-10; 2025: high-impact under M-25-21) | 2024 `Is the AI use case rights-impacting, safety-impacting, both, or neither?`; 2025 `is_high_impact` |
| matched_keywords | text, `; `-separated | All strong + weak keyword labels matched (labels = keys in `code/keywords.json`) | computed over searched fields |
| strong_kw | text, `; `-separated | Strong keyword labels matched | computed |
| weak_kw | text, `; `-separated | Weak keyword labels matched | computed |
| exclusion_triggers | text, `; `-separated | Exclusion-trigger labels matched (v1 + v2 lists) | computed |
| decision | categorical: `include` / `needs author review` / `exclude` | Rule-based screen decision using v2 triggers (rules R1–R4b, docs/METHODS.md). **Not the author's decision** | computed |
| reason | text | Rule that fired, with the triggers that fired | computed |
| decision_v1 | categorical | Decision the same rules give with only the v1 exclusion triggers (before the amendment) | computed |
| also_in_2024_same_name | text (`yes`/blank) | 2025 rows only: same agency abbreviation and normalized name appear in the 2024 file. Blank for 2024 rows | computed |
| row_in_file | integer | Line number in the raw CSV (header = line 1, so first data row = 2). With `year`, this is the stable row key (`year-row_in_file`) | computed |
| purpose | text | 2024: purpose/benefits answer. 2025: `problem_solved` + space + `benefits` | 2024 `What is the intended purpose and expected benefits of the AI?`; 2025 `problem_solved`, `benefits` |
| outputs | text | System outputs, verbatim | 2024 `Describe the AI system's outputs.`; 2025 `system_outputs` |

Searched text = `name` + topic (2024 `Use Case Topic Area` + `Other (Use Case Topic Area)`; 2025 `topic_area`) + technique (2025 `classification`; none in 2024) + `purpose` + `outputs`, joined with spaces. Topic and technique are searched but not written to these files.

### 2.2 `idp_screen_per_agency_counts.csv`

| Column | Type | Description |
|---|---|---|
| agency | text | Full agency name as written in the inventory. Names differ between years, so one agency can appear on two rows |
| 2025 include | integer | Count of 2025 rows with decision = include |
| 2025 needs author review | integer | Count of 2025 rows with decision = needs author review |
| 2024 include | integer | Count of 2024 rows with decision = include |
| 2024 needs author review | integer | Count of 2024 rows with decision = needs author review |
| 2025 include (Deployed) | integer | 2025 includes with `development_stage` exactly `Deployed` |

### 2.3 `idp_screen_paper_tools_lookup.csv`

Lookup of the paper's named tools and pilots in each inventory (match on agency abbreviation + name regex, plus use case ID for 2025; patterns are in screen.py `TOOLS`).

| Column | Type | Description |
|---|---|---|
| paper tool | text | Label used in the paper |
| inventory | text | 2024 or 2025 |
| found | text | `found` / `not found` |
| use_case_id | text | ID in the inventory (blank for 2024) |
| name in inventory | text | Use case name as reported |
| stage | text | Development stage, verbatim |
| impact flag | text | Impact field, verbatim |
| matched keywords | text | Keyword labels matched, or `(no keyword match)` |
| screen decision | text | Rule-based decision, or `not matched` |
| row_in_file | integer | Line number in the raw CSV |

### 2.4 `idp_screen_step_counts.csv`

| Column | Type | Description |
|---|---|---|
| inventory | text | 2024 or 2025 |
| step | text | Screening step (flow-diagram counts; see docs/METHODS.md) |
| count | integer | Number of rows |

### 2.5 `idp_screen_duplicates_removed.csv`

Rows dropped by de-duplication (same normalized agency + name + purpose within a year; first kept). Columns: year, agency, use_case_id, name, row_in_file (definitions as in 2.1).

### 2.6 `idp_screen_all_tables.xlsx`

One workbook with the tables above plus reference tabs: StepCounts, Included_Borderline (= 2.1 first file), PerAgency, PaperTools, Excluded_Matches, COTS2025_Matches (0 rows: the COTS file had no keyword match), Keywords (type, label, regex; **lists only the v1 exclusion triggers, not the v2 additions, which are in code/keywords.json**), Rules (rule, decision, condition), and Sources (source, url, version, sha256, accessed).

### 2.7 `run_log.txt`

Console output of `python3 screen.py` (step counts, paper tools, top 25 agencies, COTS match count).

### 2.8 `author_decisions/` (pending)

Empty for now. It is for the author's own screening decisions, exported from tools/IDP_Screener.html. The export columns are row_key, agency, name, ID, year, decision, classes, reason, note, timestamp; see `derived/author_decisions/README.md`.
