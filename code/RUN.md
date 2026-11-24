# How to run

Requirements: Python 3.13.5 (the tested version) and the packages in `requirements.txt`. The download script also needs `git`, `bash` and `sha256sum` (coreutils).

```bash
cd code
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt

# (optional) re-download the raw sources into a scratch dir and check them against the shipped checksums
bash download_sources.sh /tmp/fresh_raw
(cd /tmp/fresh_raw && sha256sum -c "$OLDPWD/../raw/SHA256SUMS.txt")   # or give the absolute path to raw/SHA256SUMS.txt

# run the screen (reads ../raw and ./keywords.json, writes ../derived, prints a log)
python3 screen.py > ../derived/run_log.txt
```

The run is deterministic. With the shipped `raw/` and `keywords.json`, all six CSVs and `run_log.txt` come out byte-identical to the files in `derived/` (checked 2026-11-23). The `.xlsx` is not byte-identical between runs because the file stores its own write time, but every cell value matches.

Files:
- `screen.py`: the keyword screen (rules R1–R4b, de-duplication, paper-tool lookup, per-agency counts).
- `keywords.json`: the regex lists (strong keywords, weak keywords, document noun, v1 exclusion triggers, and the v2 amendment).
- `download_sources.sh`: reproduces `raw/` from GitHub at the pinned commits.
- `requirements.txt`: the tested package versions.

Note: in this package, screen.py has only its file paths and output file names changed from the working copy used on 2026-11-23. Its outputs were confirmed identical to the earlier run's outputs (see CHANGELOG.md).
