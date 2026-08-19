# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

HDIC (Integrated Database of Hanzi Dictionaries in Early Japan / 平安時代漢字字書総合データベース) is a scholarly data repository, not a software application. The repository contains structured TSV/TXT datasets transcribed from medieval Chinese and early Japanese Hanzi dictionaries, along with sample analysis scripts.

License: CC BY-SA 4.0. Contact: ikeda.shoju@gmail.com

## Running the Statistics Tool

The primary utility script validates TSV structure and reports basic statistics:

```bash
# Basic usage (run from repo root)
python3 samples/statistics/count_basic_stats.py TSJ_entries.tsv

# With output format options
python3 samples/statistics/count_basic_stats.py TSJ_entries.tsv --format json
python3 samples/statistics/count_basic_stats.py TSJ_entries.tsv --format tsv

# Export a comment-free TSV for Excel import
python3 samples/statistics/count_basic_stats.py TSJ_entries.tsv --export-clean-tsv clean.tsv

# Write report to file
python3 samples/statistics/count_basic_stats.py KRM.tsv --output report.txt
```

Run this tool before opening any TSV in Excel or processing it with scripts to detect malformed rows, missing TAB separators, or irregular column counts.

**Before committing any change to a root-level `*.tsv`/`*.txt` dataset file, run `count_basic_stats.py` on each changed file and confirm `irregular_row_count == 0` and `max_column_count_seen` matches `column_count`.** This is not optional — several past corrections (see `samples/logs/`) were only caught after the fact because this check was skipped before committing.

If the change touches an ID that other files cross-reference (`SJID`/`SJ2ID`, `TBID`, `SYID`, `YYID`, `TSJ2ID`), also run `python3 samples/scripts/validate_hdic_integrity.py` to check that cross-file references still resolve (read-only; does not modify data). As of 2026-08 there are known pre-existing broken references unrelated to any single edit — a non-zero exit code only means *some* reference is broken, not necessarily one you just introduced; check whether the IDs you touched appear in the output before treating it as a regression.

## Editing a Single Data Row

For a small, targeted correction (one or a few rows in one file):

1. Locate the row (`grep`) and edit it in place with the `Edit` tool, changing only the cell(s) that need correcting.
2. Run `count_basic_stats.py` on the changed file (see above).
3. Run `python3 samples/scripts/finalize_hdic_edit.py` — it auto-detects the changed TSV/TXT files from `git diff` and bumps each file's header `Version` (patch) and `Last update`/`Last modified` date. It never touches data rows and is safe to re-run before committing.
4. If the edit touched a cross-referenced ID, run `validate_hdic_integrity.py` (see above).
5. Show the diff and propose a commit message; do not commit without explicit user approval.

## TSV File Conventions

All HDIC datasets follow these conventions:

- **Encoding**: UTF-8 (with optional BOM)
- **Delimiter**: TAB
- **Comment lines**: Lines beginning with `#` appear before the header and must be skipped
- **Header**: The first non-comment, non-blank line
- **Trailing empty fields**: May be omitted at end of rows (this is normal, not an error)
- **Stable IDs**: Each dataset has a stable identifier column (e.g., `SJID`, `KRID`, `SYID`, `TBID`)

## Dataset Structure

### Main entry-level files (starting points for analysis)

| File | Dictionary | Rows | Key column |
|---|---|---|---|
| `TSJ_entries.tsv` | Tenjibon *Shinsen Jikyō* | 24,381 | `SJID` |
| `KRM.tsv` | Kanchiinbon *Ruiju Myōgishō* | 32,607 | `KRID` |
| `KTB.tsv` | Kōsanji-bon *Tenrei Banshō Meigi* | 18,932 | `TBID` |
| `SYP.tsv` | Songben *Yupian* | 22,809 | `SYID` |

### Split/specialized tables

- `*_definitions.tsv` — definition-level splits (e.g., `KRM_definitions.tsv` has 86,796 rows with `Def_code` values like `和訓`, `義注`, `音注`)
- `*_wakun.tsv` — Japanese readings (*wakun*) extraction tables; use these (not main files) for wakun analysis
- `*_ndl.*` / `*_keio.tsv` — page-to-image URL mappings (NDL Digital Collections, Keio IIIF)
- `*_ndl_Seal.tsv` — IIIF crop coordinates for seal-script glyph images

Cross-references between dictionaries are embedded in the main files (e.g., `TSJ_entries.tsv` contains `TBID` and `SYID` columns linking to KTB and SYP).

## Data Handling Principles

- **Preserve original orthography**: Do not normalize or regularize variant characters (異体字) automatically
- **Katakana wakun are linguistic data**: Treat them as primary scholarly evidence, not display artifacts
- **Historical annotations**: Preserve embedded annotations exactly as they appear
- **IDS notation**: Some `Entry_original` cells contain IDS (Ideographic Description Sequences) like `⿸疒⿱龷天` for unencoded characters — handle these as-is

## Analysis Tools and Libraries

Preferred Python libraries for sample scripts:

- `pandas`, `csv` — TSV processing
- `matplotlib` — visualization
- `regex` — pattern matching (supports Unicode better than `re`)
- `pathlib` — file paths

Avoid heavy frameworks. Scripts in `samples/statistics/` are designed to be self-contained.

## Directory Layout

```
HDIC/
├── *.tsv / *.txt     # Primary dataset files (root level)
├── samples/
│   ├── statistics/   # Analysis scripts (count_basic_stats.py)
│   ├── scripts/      # Reusable utility scripts (e.g. IDS/UCS matching across dictionaries)
│   ├── planning/     # Design notes (HDIC_root_files_survey.md is the authoritative file inventory)
│   ├── agents/       # AGENTS.md — agent guidance
│   └── logs/         # Change logs for data corrections
├── work/             # Scratch workspace (gitignored) — intermediate/derived files only,
│                      # never the only copy of a reusable script; promote reusable scripts
│                      # to samples/scripts/ instead of leaving them here
└── v1.2/             # Deprecated; KRM data moved to github.com/shikeda/krm
```

## Key Reference

`samples/planning/HDIC_root_files_survey.md` contains a comprehensive file-by-file inventory with column names, row counts, and structural notes for every dataset in the repository root. Consult it before writing analysis scripts.

## Commands

### Safe to run without asking

Read-only inspection commands can be run freely:

- `git status`, `git diff`, `git log`, `git show` (read-only forms)
- `python3 samples/statistics/count_basic_stats.py ...` (and other read-only scripts under `samples/`)

### Always confirm before running

- `git push` (sends data externally)
- `git commit` (unless the user has already approved the specific change)
- Any destructive filesystem operation (`rm`, overwriting a root-level `*.tsv`/`*.txt` dataset file) on files not created in the current session
