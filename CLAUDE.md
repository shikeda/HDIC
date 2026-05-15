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
│   ├── planning/     # Design notes (HDIC_root_files_survey.md is the authoritative file inventory)
│   ├── agents/       # AGENTS.md — agent guidance
│   └── logs/         # Change logs for data corrections
└── v1.2/             # Deprecated; KRM data moved to github.com/shikeda/krm
```

## Key Reference

`samples/planning/HDIC_root_files_survey.md` contains a comprehensive file-by-file inventory with column names, row counts, and structural notes for every dataset in the repository root. Consult it before writing analysis scripts.
