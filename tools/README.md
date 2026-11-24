# tools/: author screening interface (not data)

`IDP_Screener.html` is a single offline HTML file (no network needed). The author used it to record his own screening decisions on the keyword-matched rows. It embeds 523 rows: 2025 include/needs review (205, including 2 paper tools with no keyword match), 2025 rule-excluded (91), and 2024 matches (226) plus SSA PATH 2024. The embedded text was copied from the files in `derived/`.

- It is **not a data file**. The authoritative values are in `raw/` and `derived/`.
- It shows the rule-based verdict for reference only and never pre-fills a decision.
- Decisions are saved in the browser's localStorage. Use **Export CSV** to save them, then place the export in `derived/author_decisions/` for a later package version.
- Opening the file in a different browser or profile starts with no saved decisions.
- A second, online copy of this screener exists with trimmed text (the 205 cards from the 2025 deck only). It is not part of this package. Decisions saved in one copy do not appear in the other.
