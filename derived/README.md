# derived/: outputs of code/screen.py (v1.0, 2026-11-23)

| File | Contents |
|---|---|
| idp_screen_include_and_needs_review.csv | Keyword-matched, de-duplicated rows with rule decision `include` or `needs author review` (2024: 99 + 45; 2025: 128 + 75) |
| idp_screen_excluded_keyword_matches.csv | Keyword-matched rows with rule decision `exclude` (2024: 82; 2025: 91) |
| idp_screen_per_agency_counts.csv | Include / needs-review counts per agency and year |
| idp_screen_paper_tools_lookup.csv | Where the paper's named tools and pilots appear in each inventory |
| idp_screen_step_counts.csv | Screening flow counts, for a PRISMA-style diagram |
| idp_screen_duplicates_removed.csv | Rows removed as duplicates (2024: 2; 2025: 0) |
| idp_screen_all_tables.xlsx | All of the above in one workbook, plus Keywords, Rules and Sources tabs |
| run_log.txt | Console output of the run |
| author_decisions/ | **Pending.** The author's own decisions will be added later |

All `decision` values here come from the rules, not from the author. Column definitions are in docs/CODEBOOK.md.
