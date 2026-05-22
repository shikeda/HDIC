# AGENTS.md

This file provides guidance to coding agents working in this repository.

## Project Overview

HDIC (Integrated Database of Hanzi Dictionaries in Early Japan / 平安時代漢字字書総合データベース) is a scholarly data repository, not an application codebase. The repository contains structured TSV/TXT datasets, documentation, and small analysis utilities for medieval Chinese and early Japanese Hanzi dictionaries.

License: CC BY-SA 4.0. Contact: ikeda.shoju@gmail.com

## Working Style

- Treat the repository as a data publication project.
- Prefer conservative edits: preserve text, orthography, and annotations unless the task explicitly requires normalization.
- When changing released TSV files, also check whether related documentation (`README.md`, changelog files, legends, or agent guidance) should be updated.
- Avoid introducing schema changes casually. If a column name or meaning changes, update the comment header and any builder scripts together.

## TSV File Conventions

All HDIC datasets follow these conventions:

- Encoding: UTF-8 (BOM may appear in some files)
- Delimiter: TAB
- Comment lines: lines beginning with `#` before the header
- Header: first non-comment, non-blank line
- Trailing empty fields: may be omitted
- Stable IDs: each file has its own key column such as `SJID`, `KRID`, `TBID`, `SYID`, `YYID`, or `entry_id`

Do not remove or rewrite comment headers unless the task specifically asks for metadata changes.

## Main Dataset Files

Primary entry-level TSV files in the repository root:

- `TSJ_entries.tsv`
- `KRM.tsv`
- `KTB.tsv`
- `SYP.tsv`
- `YYP.tsv`
- `ZRM.tsv`

Specialized or split tables include:

- `*_definitions.tsv`
- `*_wakun.tsv`
- `*_ndl.*`
- `*_keio.tsv`
- `*_ndl_Seal.tsv`
- `ZRM_changelog.md` and similar release notes

## YYP-specific Notes

- `YYP.tsv` is a fragment-based full-text table for the surviving old manuscript portions of the original *Yupian* preserved in Japan.
- Key columns are `YYID`, `YY_vol_radical`, `Entry`, `Lv_page`, `Yao_page`, `YY_def`, `YY_remarks`, `TBID`, `SYID`, and `YY_img_filename`.
- `Lv_page` refers to the reference framework of Lv Hao 呂浩.
- `Yao_page` is available only for a small portion of the dataset.
- `YY_img_filename` refers to an internal working image set and should not be treated as a public image field.
- `YY_remarks` includes mixed editorial notes such as `重文`, `有再注字`, `字体注`, and `原本補入`.
- `YYP.tsv` is still provisional; when making philologically sensitive decisions, consult facsimiles and published printed transcriptions.

## ZRM-specific Notes

- `ZRM.tsv` is generated from working materials; if the release TSV changes, check whether the builder logic or changelog should also change.
- `definition` currently preserves parenthetical `（ ）` and bracketed `【 】` notes in place.
- `remarks` may be sparsely populated and can derive from separate source data.

## Validation

Use the statistics tool before and after non-trivial TSV edits:

```bash
python3 samples/statistics/count_basic_stats.py YYP.tsv --level beginner
python3 samples/statistics/count_basic_stats.py ZRM.tsv --level beginner
```

This tool is useful for checking:

- irregular row counts
- missing TAB separators
- header location
- non-empty/empty column counts

## Preferred Editing Pattern

When working on derived TSV files:

1. Inspect the existing comment header.
2. Inspect any builder or export script related to that file.
3. Make the smallest consistent change across data, legend, README, and changelog.
4. Re-run structural validation.

## Key References

- `README.md` for public-facing dataset descriptions
- `CLAUDE.md` for parallel agent guidance
- `samples/planning/HDIC_root_files_survey.md` for file inventory and structure
