#!/usr/bin/env python3
"""Reproducible IDP keyword screen of the official OMB consolidated federal AI use case inventories.
Run from the code/ folder: python3 screen.py   (inputs in ../raw, keywords in ./keywords.json, outputs in ../derived)
"""
import json, re, hashlib, os
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "..", "raw"); OUT = os.path.join(HERE, "..", "derived")
os.makedirs(OUT, exist_ok=True)
KW = json.load(open(os.path.join(HERE, "keywords.json")))
STRONG = {k: re.compile(v, re.I) for k, v in KW["strong"].items()}
WEAK = {k: re.compile(v, re.I) for k, v in KW["weak"].items()}
DOCN = re.compile(KW["document_noun"], re.I)
EXCL_V1 = {k: re.compile(v, re.I) for k, v in KW["exclusion_triggers"].items()}
EXCL_V2 = dict(EXCL_V1, **{k: re.compile(v, re.I) for k, v in KW["exclusion_triggers_amendment_v2"].items() if not k.startswith("_")})

def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
def norm(s): return re.sub(r"\W+", " ", str(s)).strip().lower()

F24 = os.path.join(RAW, "ombegov_2024-Federal-AI-Use-Case-Inventory_4a29d13", "data", "2024_consolidated_ai_inventory_raw_v2.csv")
F25 = os.path.join(RAW, "ombegov_2025-Federal-Agency-AI-Use-Case-Inventory_06c7ebe", "Data", "2025_individually_reported_AI_use_cases.csv")
F25C = os.path.join(RAW, "ombegov_2025-Federal-Agency-AI-Use-Case-Inventory_06c7ebe", "Data", "2025_consolidated_COTS_AI_use_cases.csv")

d24 = pd.read_csv(F24, dtype=str, encoding="latin-1").fillna("")   # file is cp1252, not UTF-8
d24.columns = [c.replace("\x92", "'") for c in d24.columns]
d25 = pd.read_csv(F25, dtype=str).fillna("")
d25c = pd.read_csv(F25C, dtype=str).fillna("")

# Unified view
P24 = "What is the intended purpose and expected benefits of the AI?"
O24 = "Describe the AI system's outputs."
RS24 = "Is the AI use case rights-impacting, safety-impacting, both, or neither?"
u24 = pd.DataFrame({
    "year": "2024", "row_in_file": d24.index + 2,  # +2 = header + 1-based
    "agency": d24["Agency"], "agency_abbr": d24["Agency Abbreviation"], "bureau": d24["Bureau"],
    "use_case_id": "",  # 2024 consolidated file has no use case ID column
    "name": d24["Use Case Name"], "topic": d24["Use Case Topic Area"] + " " + d24["Other (Use Case Topic Area)"],
    "technique": "",  # no technique/classification field in 2024 file
    "purpose": d24[P24], "outputs": d24[O24],
    "stage": d24["Stage of Development"], "impact_flag": d24[RS24].str.strip(),
})
u25 = pd.DataFrame({
    "year": "2025", "row_in_file": d25.index + 2,
    "agency": d25["agency_name"], "agency_abbr": d25["agency"], "bureau": d25["agency_bureau"],
    "use_case_id": d25["id"], "name": d25["use_case_name"], "topic": d25["topic_area"],
    "technique": d25["classification"], "purpose": d25["problem_solved"] + " " + d25["benefits"],
    "outputs": d25["system_outputs"], "stage": d25["development_stage"], "impact_flag": d25["is_high_impact"],
})
FIELDS = ["name", "topic", "technique", "purpose", "outputs"]

def classify(text, EXCL=EXCL_V2):
    s = sorted(k for k, r in STRONG.items() if r.search(text))
    w = sorted(k for k, r in WEAK.items() if r.search(text))
    e = sorted(k for k, r in EXCL.items() if r.search(text))
    dn = bool(DOCN.search(text))
    if s and not e:
        dec, rule = "include", "R1: strong document-processing keyword, no exclusion trigger"
    elif s and e:
        dec, rule = "needs author review", "R2: strong keyword but exclusion trigger(s): " + "; ".join(e)
    elif w and dn and not e:
        dec, rule = "needs author review", "R3: only weak keyword(s) plus a document noun"
    elif w and e:
        dec, rule = "exclude", "R4b: only weak keyword(s) plus exclusion trigger(s): " + "; ".join(e)
    elif w:
        dec, rule = "exclude", "R4a: only weak keyword(s), no document noun"
    else:
        dec, rule = "", ""
    return s, w, e, dec, rule

def run(u):
    u = u.copy()
    txt = u[FIELDS].agg(" ".join, axis=1)
    res = txt.apply(classify)
    u["strong_kw"] = res.str[0].str.join("; "); u["weak_kw"] = res.str[1].str.join("; ")
    u["matched_keywords"] = (res.str[0] + res.str[1]).str.join("; ")
    u["exclusion_triggers"] = res.str[2].str.join("; ")
    u["decision"] = res.str[3]; u["reason"] = res.str[4]
    u["decision_v1"] = txt.apply(lambda t: classify(t, EXCL_V1)[3])
    total = len(u)
    m = u[u["matched_keywords"] != ""].copy()
    m["dedup_key"] = m["agency"].map(norm) + "|" + m["name"].map(norm) + "|" + m["purpose"].map(norm)
    dups = m[m.duplicated("dedup_key", keep="first")]
    md = m.drop_duplicates("dedup_key", keep="first").copy()
    return u, total, m, dups, md

u24, t24, m24, dup24, md24 = run(u24)
u25, t25, m25, dup25, md25 = run(u25)

# Cross-year link: same agency abbreviation + normalized name
k24 = set(zip(u24.agency_abbr.str.upper().str.strip(), u24.name.map(norm)))
md25["also_in_2024_same_name"] = [("yes" if (a.upper().strip(), norm(n)) in k24 else "")
                                  for a, n in zip(md25.agency_abbr, md25.name)]
md24["also_in_2024_same_name"] = ""

steps = []
for y, t, m, dups, md in [("2024", t24, m24, dup24, md24), ("2025", t25, m25, dup25, md25)]:
    vc = md["decision"].value_counts()
    steps += [
        (y, "1 total entries in file", t),
        (y, "2 keyword matches (any strong or weak keyword)", len(m)),
        (y, "3 after de-duplication (agency+name+purpose)", len(md)),
        (y, "4a screen: include (R1)", int(vc.get("include", 0))),
        (y, "4b screen: needs author review (R2/R3)", int(vc.get("needs author review", 0))),
        (y, "4c screen: exclude (R4a/R4b)", int(vc.get("exclude", 0))),
    ]
    v1 = md["decision_v1"].value_counts()
    steps += [(y, "4a-v1 include under v1 exclusion triggers (before amendment)", int(v1.get("include", 0))),
              (y, "4b-v1 needs author review under v1", int(v1.get("needs author review", 0)))]
steps = pd.DataFrame(steps, columns=["inventory", "step", "count"])

# 2025 deployed-only view (paper's own rule: pilots/pre-deployment not coded)
inc25 = md25[md25.decision == "include"]
steps.loc[len(steps)] = ["2025", "5 include AND development_stage == Deployed", int((inc25.stage == "Deployed").sum())]

COLS = ["year", "agency", "agency_abbr", "bureau", "use_case_id", "name", "stage", "impact_flag",
        "matched_keywords", "strong_kw", "weak_kw", "exclusion_triggers", "decision", "reason", "decision_v1",
        "also_in_2024_same_name", "row_in_file", "purpose", "outputs"]
screened = pd.concat([md24, md25])[COLS]
keep = screened[screened.decision.isin(["include", "needs author review"])]
excl = screened[screened.decision == "exclude"]

# Per-agency counts
pa = (screened.assign(n=1).pivot_table(index="agency", columns=["year", "decision"], values="n",
                                       aggfunc="sum", fill_value=0))
pa.columns = [f"{y} {d}" for y, d in pa.columns]
for c in ["2024 include", "2024 needs author review", "2025 include", "2025 needs author review"]:
    if c not in pa: pa[c] = 0
pa = pa[["2025 include", "2025 needs author review", "2024 include", "2024 needs author review"]]
pa["2025 include (Deployed)"] = inc25[inc25.stage == "Deployed"].groupby("agency").size().reindex(pa.index).fillna(0).astype(int)
pa = pa.sort_values(["2025 include", "2024 include"], ascending=False).reset_index()

# Paper tools
TOOLS = [
    ("IMAGEN (SSA)", "SSA", None, r"IMAGEN"),
    ("VA Privacy Act Automation (VA-24-2545)", "VA", "VA-24-2545", r"Privacy Act Automation"),
    ("State Declassification", "STATE", None, r"Declassification Review"),
    ("VA ADS (VA-24-4722)", "VA", "VA-24-4722", r"^Automated Decision Support"),
    ("USCIS ELIS Evidence Classifier (DHS-16)", "DHS", "DHS-16", r"ELIS Evidence Classifier"),
    ("IRS TREAS-IRS-64", "TREAS", "TREAS-IRS-64", r"Word Processor AI for Digitalization"),
    ("SSA PATH (excluded in paper)", "SSA", None, r"Proactive Triage and Analysis of Hearings"),
    ("NARA-0005 PII pilot (excluded)", "NARA", "NARA - 0005", r"Screen and Flag for Personally Identifiable"),
    ("NARA-0011 FOIA Discovery pilot (excluded)", "NARA", "NARA - 0011", r"FOIA\) Discovery AI Pilot"),
]
rows = []
for label, ab, tid, pat in TOOLS:
    for y, u in [("2024", u24), ("2025", u25)]:
        hit = u[(u.agency_abbr.str.upper().str.strip() == ab) & u.name.str.contains(pat, regex=True)]
        if tid and y == "2025":
            hit = pd.concat([hit, u[u.use_case_id.str.strip() == tid]]).drop_duplicates("row_in_file")
        if hit.empty:
            rows.append([label, y, "not found", "", "", "", "", "", "", ""]); continue
        for _, r in hit.iterrows():
            rows.append([label, y, "found", r.use_case_id, r["name"], r.stage, r.impact_flag,
                         r.matched_keywords or "(no keyword match)", r.decision or "not matched", r.row_in_file])
tools = pd.DataFrame(rows, columns=["paper tool", "inventory", "found", "use_case_id", "name in inventory",
                                    "stage", "impact flag", "matched keywords", "screen decision", "row_in_file"])

# Supplementary: 2025 consolidated COTS file (separate structure; not part of main counts)
ct = (d25c["AI Use Case"] + " " + d25c["Name of Commercial Product or Service Used"])
cres = ct.apply(classify)
d25c["matched_keywords"] = (cres.str[0] + cres.str[1]).str.join("; ")
d25c["decision"] = cres.str[3]; d25c["reason"] = cres.str[4]
cots = d25c[d25c.matched_keywords != ""]

sources = pd.DataFrame([
    ["2024 consolidated inventory v2 (CSV)", "https://raw.githubusercontent.com/ombegov/2024-Federal-AI-Use-Case-Inventory/4a29d132291261d4829b187acd8af618e7295294/data/2024_consolidated_ai_inventory_raw_v2.csv", "repo commit 4a29d13 (2025-01-23); README 'As of January 23, 2025'", sha(F24)],
    ["2025 individually reported use cases (CSV)", "https://raw.githubusercontent.com/ombegov/2025-Federal-Agency-AI-Use-Case-Inventory/06c7ebeef5b376524211042bd9673b2a7fefd3e3/Data/2025_individually_reported_AI_use_cases.csv", "repo commit 06c7ebe (2026-05-14); README 'As of April 13, 2026'", sha(F25)],
    ["2025 consolidated COTS use cases (CSV)", "https://raw.githubusercontent.com/ombegov/2025-Federal-Agency-AI-Use-Case-Inventory/06c7ebeef5b376524211042bd9673b2a7fefd3e3/Data/2025_consolidated_COTS_AI_use_cases.csv", "repo commit 06c7ebe (2026-05-14)", sha(F25C)],
], columns=["source", "url", "version", "sha256"])
sources["accessed"] = "2026-11-23"

kwdf = pd.DataFrame([(t, k, v) for t in ["strong", "weak"] for k, v in KW[t].items()] +
                    [("document_noun", "document noun", KW["document_noun"])] +
                    [("exclusion", k, v) for k, v in KW["exclusion_triggers"].items()],
                    columns=["type", "label", "regex (case-insensitive)"])
rules = pd.DataFrame([
    ["R1", "include", "≥1 strong keyword and no exclusion trigger"],
    ["R2", "needs author review", "≥1 strong keyword but ≥1 exclusion trigger"],
    ["R3", "needs author review", "only weak keyword(s), a document noun present, no exclusion trigger"],
    ["R4a", "exclude", "only weak keyword(s), no document noun"],
    ["R4b", "exclude", "only weak keyword(s) and ≥1 exclusion trigger"],
    ["fields", "", "2024: name, topic area(+other), purpose/benefits, outputs. 2025: use_case_name, topic_area, classification, problem_solved+benefits, system_outputs"],
    ["dedup", "", "within each year, rows with identical normalized agency + name + purpose; first kept"],
], columns=["rule", "decision", "condition"])

keep.to_csv(os.path.join(OUT, "idp_screen_include_and_needs_review.csv"), index=False)
excl.to_csv(os.path.join(OUT, "idp_screen_excluded_keyword_matches.csv"), index=False)
pa.to_csv(os.path.join(OUT, "idp_screen_per_agency_counts.csv"), index=False)
tools.to_csv(os.path.join(OUT, "idp_screen_paper_tools_lookup.csv"), index=False)
steps.to_csv(os.path.join(OUT, "idp_screen_step_counts.csv"), index=False)
pd.concat([dup24, dup25])[["year", "agency", "use_case_id", "name", "row_in_file"]].to_csv(os.path.join(OUT, "idp_screen_duplicates_removed.csv"), index=False)
with pd.ExcelWriter(os.path.join(OUT, "idp_screen_all_tables.xlsx")) as xw:
    for nm, df in [("StepCounts", steps), ("Included_Borderline", keep), ("PerAgency", pa), ("PaperTools", tools),
                   ("Excluded_Matches", excl), ("COTS2025_Matches", cots), ("Keywords", kwdf), ("Rules", rules),
                   ("Sources", sources)]:
        df.to_excel(xw, sheet_name=nm, index=False)
print(steps.to_string(index=False)); print(tools.to_string(index=False))
print(pa.head(25).to_string(index=False))
print("COTS matches", len(cots), cots.decision.value_counts().to_dict())
