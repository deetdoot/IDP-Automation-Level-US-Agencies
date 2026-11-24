# VERIFICATION_LOG: checksum re-verification (2026-11-23, PST)

## Original acquisition
The 11 source files in the working folder `inventory-screen/raw/` have file times of 19:10:14–19:10:16 PST on 2026-11-23. They were fetched from the pinned commits. The exact commands of that first fetch were not logged, so the steps below are the documented, re-tested procedure. The checksums of that first copy went into the working `SHA256SUMS.txt`.

## Re-download from scratch, 2026-11-23
1. **19:36 PST, git route.** Fresh `git clone` of both repositories into `/tmp/reverify`, then `git checkout` of the pinned commits. `git rev-parse HEAD` gave 4a29d132291261d4829b187acd8af618e7295294 and 06c7ebeef5b376524211042bd9673b2a7fefd3e3. These were also the remote default-branch heads at that time, so neither repository had changed since the pinned commit. Each of the 11 originally downloaded files was compared with the fresh copy: **11/11 SHA-256 MATCH**.
2. **19:38:52–19:38:54 PST, packaged script.** `code/download_sources.sh` was run into an empty temp dir and then `sha256sum -c raw/SHA256SUMS.txt` was run: **18/18 OK** (all files in `raw/`). The fresh tree had 18 files, the same as the manifest.
3. **19:38 PST, curl route.** The three CSVs were downloaded again from `https://raw.githubusercontent.com/ombegov/<repo>/<commit>/<path>` and hashed: all three **MATCH**.

| File | SHA-256 |
|---|---|
| 2024_consolidated_ai_inventory_raw_v2.csv | 789e1bac6d2551e8f90e5cfc5feb37ac23c6ca9f302f5af92fea8a577caa0a83 |
| 2025_individually_reported_AI_use_cases.csv | a62721202ca4b110ce3c53ffdb688d05ad27a35971a7afda4f1179b2493e31d0 |
| 2025_consolidated_COTS_AI_use_cases.csv | bd18984bdc41f8fc818c9d145de78ebe2563ee0ffab29fe7e96de4c223c8ba17 |

## Re-run of the screen
`code/screen.py` was run against the packaged `raw/`. All six output CSVs and `run_log.txt` are **byte-identical** to the earlier working-folder outputs. In the XLSX, all 9 sheets have identical cell values.

## License check
Both cloned trees were listed at the pinned commits (`find -iname 'LICENSE*' -o -iname 'COPYING*'`): **no LICENSE or COPYING file exists in either repository.** A text search of all `.md` files for "license", "public domain" and "copyright" found no license statement. (The only hits were about software licenses inside the COTS data report.) The GitHub license API was not usable because of an unauthenticated rate limit and a "Not Found" response.
