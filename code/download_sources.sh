#!/usr/bin/env bash
# Reproduce raw/ from the upstream GitHub repositories at the pinned commits.
# Usage: bash download_sources.sh <empty_target_dir>
# Then run: (cd <target_dir> && sha256sum -c /path/to/raw/SHA256SUMS.txt)
set -euo pipefail
T="${1:?target dir}"; mkdir -p "$T"; cd "$T"
R24=ombegov_2024-Federal-AI-Use-Case-Inventory_4a29d13
R25=ombegov_2025-Federal-Agency-AI-Use-Case-Inventory_06c7ebe
C24=4a29d132291261d4829b187acd8af618e7295294
C25=06c7ebeef5b376524211042bd9673b2a7fefd3e3
git clone -q https://github.com/ombegov/2024-Federal-AI-Use-Case-Inventory.git _src24
git -C _src24 checkout -q "$C24"
git clone -q https://github.com/ombegov/2025-Federal-Agency-AI-Use-Case-Inventory.git _src25
git -C _src25 checkout -q "$C25"
echo "2024 HEAD: $(git -C _src24 rev-parse HEAD)"; echo "2025 HEAD: $(git -C _src25 rev-parse HEAD)"
mkdir -p "$R24/data" "$R24/validation" "$R25/Data" "$R25/Validation" "$R25/Reporting Instructions"
cp _src24/README.md "$R24/"
cp _src24/data/2024_consolidated_ai_inventory_raw_v2.csv _src24/data/2024_consolidated_ai_inventory_raw_v2.xls "$R24/data/"
cp _src24/validation/data_dictionary.yaml "$R24/validation/"
cp _src25/README.md "$R25/"
cp _src25/Data/2025_individually_reported_AI_use_cases.csv _src25/Data/2025_individually_reported_AI_use_cases.xlsx \
   _src25/Data/2025_consolidated_COTS_AI_use_cases.csv _src25/Data/2025_consolidated_COTS_AI_use_cases.xlsx \
   _src25/Data/README_datasets.md "$R25/Data/"
cp _src25/Validation/* "$R25/Validation/"
cp "_src25/Reporting Instructions/"* "$R25/Reporting Instructions/"
rm -rf _src24 _src25
