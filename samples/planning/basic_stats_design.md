# basic_stats_design

## Purpose

`count_basic_stats.py` is a beginner-friendly statistics script for HDIC TSV files.

Goals:

- help users understand TSV structure
- provide safe first access to HDIC data
- support Codex / Claude Code / Gemini CLI workflows
- provide reusable statistics for dictionary studies

---

## Level Design

### beginner

Purpose:

- become familiar with TSV files
- understand overall structure

Main statistics:

- file name
- comment line count
- header line number
- data start line number
- row count
- column count
- column names
- non-empty cell counts
- empty cell counts

Notes:

- interpretation-heavy statistics are excluded
- output should remain short and readable

### standard

Purpose:

- understand dictionary structure
- compare datasets

Planned statistics:

- unique headword count
- wakun count
- definition count
- URL count
- radical count
- duplicate ID count
- average text length
- sample values

Notes:

- intended for humanities researchers
- useful for research memos and reports

### research

Purpose:

- analyze dataset characteristics
- support lexicographical and philological research

Planned statistics:

- IDS symbol frequency
- variant character frequency
- definition length distribution
- annotation ratio
- phonetic note ratio
- frequent values
- character type statistics

Notes:

- interpretation may depend on dataset structure
- results may require manual verification

---

## CLI Policy

Basic syntax:

```bash
python3 count_basic_stats.py INPUT.tsv --level beginner
```

Examples:

```bash
python3 count_basic_stats.py TSJ_entries.tsv --level beginner
python3 count_basic_stats.py KRM.tsv --level standard
python3 count_basic_stats.py TSJ_wakun.tsv --level research
```

Possible short options:

```bash
-l beginner
-l standard
-l research
```

Future shorthand candidates:

```bash
-l b
-l s
-l r
```

---

## Comment-line Handling

Rules:

- lines beginning with `#` are treated as comments
- empty lines are ignored
- the first non-comment line is treated as the header
- UTF-8 BOM should be supported
- delimiter is TAB

Additional checks:

- irregular column counts
- maximum column count seen

---

## Output Formats

Planned formats:

- text
- tsv
- json

Examples:

```bash
--format text
--format tsv
--format json
```

Notes:

- text is human-readable
- TSV is spreadsheet-friendly
- JSON is AI-agent-friendly

---

## Implementation Policy

Suggested internal structure:

- `read_tsv_structure()`
- `count_basic_stats()`
- `render_text()`
- `render_tsv()`
- `render_json()`

Shared processing should be reusable across levels.
