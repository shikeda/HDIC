# Sample Output Guide

This note explains how to read the output of `count_basic_stats.py` in a way that is accessible to humanities researchers who use spreadsheets regularly but are new to Python.

## Example command

```bash
python3 samples/statistics/count_basic_stats.py TSJ_entries.tsv
```

## Example output

```text
file: TSJ_entries.tsv
level: beginner
comment_line_count: 96
blank_line_count: 0
header_line_number: 97
data_start_line_number: 98
row_count: 24381
column_count: 11
irregular_row_count: 0
trailing_missing_column_count: 0
max_column_count_seen: 11
```

## How to read each value

- `file`
  The filename that was analyzed.
  This is useful when you save output and compare several datasets later.

- `level`
  The statistics level used for the report.
  `beginner` means the output focuses on safe structural understanding rather than interpretation.

- `comment_line_count`
  The number of comment lines before the header.
  In HDIC files, lines beginning with `#` often contain project information, documentation, and column explanations.
  These lines are not data rows.

- `blank_line_count`
  The number of completely empty lines.
  A value of `0` is common and usually means the file is compactly formatted.

- `header_line_number`
  The line number where the header row appears in the original file.
  This matters because many HDIC TSV files do not begin immediately with data.

- `data_start_line_number`
  The first line number where actual tabular data begins.
  This helps you check whether the script is reading the correct starting point.

- `row_count`
  The number of data rows.
  For humanities research, this can be read as the rough scale of the table:
  how many entries, definitions, wakun items, or linkage records are included.

- `column_count`
  The number of columns defined by the header.
  This tells you how many kinds of information each row is expected to contain.

- `irregular_row_count`
  The number of rows that have more columns than expected.
  This is important because it can indicate broken TSV structure, missing internal separators, or accidental extra columns.
  If this value is greater than `0`, the file should be checked carefully.

- `trailing_missing_column_count`
  The number of rows where final empty fields were omitted.
  In humanities datasets, this is often normal rather than an error.
  For example, a final `Remarks` column may be empty in most rows and therefore left out in the raw TSV line.

- `max_column_count_seen`
  The largest number of columns found in any data row.
  If this is larger than `column_count`, some rows contain extra fields and may require cleanup.

## Column-by-column counts

The script also reports:

```text
column_counts:
- SJID: non_empty=24381, empty=0
- SJ_entry_remarks: non_empty=2411, empty=21970
```

These values can be read as follows.

- `non_empty`
  How many rows actually contain data in that column.

- `empty`
  How many rows leave that column blank.

For humanities researchers, this helps answer questions such as:

- Is this column essential or optional?
- Is a note field heavily used or only occasional?
- Is this table mainly complete, or does it contain many gaps?

## How to interpret the output in research practice

### 1. Structural check

First, check whether the TSV can be read safely.

- `irregular_row_count = 0`
  usually means there are no obvious overlong rows.
- `max_column_count_seen = column_count`
  usually means the widest row matches the header structure.

### 2. Scale check

Then check the scale of the dataset.

- a high `row_count` means a large table
- a high `column_count` means a more complex table

This helps you decide whether to start with Excel, a filtered subset, or a more focused file.

### 3. Optional field check

Look at columns with many blank cells.

For example, if `Remarks` is mostly empty, that usually means:

- remarks exist only for special cases
- the field is structurally present but not central to every row

This is often normal in philological data.

## Reading the output as a humanities researcher

You do not need to read these values as programming diagnostics only.
They can also be read as clues to the editorial character of the dataset.

Examples:

- many rows but few columns
  a compact, regular table
- fewer rows but many columns
  a more specialized or research-rich table
- many blank cells in note columns
  notes are selective rather than universal
- many trailing omitted empty columns
  the file may be structurally regular even if the raw lines look uneven

## When to investigate further

Look more closely when:

- `irregular_row_count` is not zero
- `max_column_count_seen` is greater than `column_count`
- a key column has unexpectedly many blanks
- the script output does not match your reading of the file in Excel

## Excel-oriented advice

If you mainly use Excel, the output is best understood as a pre-check before import.

- confirm the file is UTF-8
- confirm the file is TAB-separated
- confirm the table structure is stable
- only then import into Excel

This reduces the risk of misread columns or hidden structural problems.

---

# 出力例の読み方

このメモは、`count_basic_stats.py` の出力を、Python に不慣れでも Excel を日常的に使う人文系研究者が読めるように説明するためのものです。

## 実行例

```bash
python3 samples/statistics/count_basic_stats.py TSJ_entries.tsv
```

## 出力例

```text
file: TSJ_entries.tsv
level: beginner
comment_line_count: 96
blank_line_count: 0
header_line_number: 97
data_start_line_number: 98
row_count: 24381
column_count: 11
irregular_row_count: 0
trailing_missing_column_count: 0
max_column_count_seen: 11
```

## 各数値の意味

- `file`
  解析したファイル名です。
  複数のファイルを見比べるときの確認用になります。

- `level`
  どのレベルの統計を使ったかを示します。
  `beginner` は、解釈よりもまず構造確認を重視した出力です。

- `comment_line_count`
  ヘッダの前にあるコメント行数です。
  HDIC では `#` で始まる行に、資料説明や列説明が入っていることが多く、これはデータ本体ではありません。

- `blank_line_count`
  完全に空白の行数です。
  `0` であれば、空行をほとんど含まない整ったファイルだと考えてよいです。

- `header_line_number`
  元ファイルの何行目にヘッダがあるかを示します。
  HDIC では最初からすぐデータが始まらないことが多いので、重要な確認項目です。

- `data_start_line_number`
  実データが始まる行番号です。
  スクリプトが正しい位置から表を読んでいるかを確かめるのに役立ちます。

- `row_count`
  データ行数です。
  人文研究の感覚で言えば、その表に何件の項目・定義・和訓・対応情報が入っているかを見る数値です。

- `column_count`
  ヘッダで定義された列数です。
  1 行ごとに何種類の情報を持つ表なのかを示します。

- `irregular_row_count`
  想定より列数の多い行の数です。
  これは TSV 構造の乱れ、途中の区切り欠落、余分な列の混入などを示す可能性があります。
  `0` でなければ、構造点検が必要です。

- `trailing_missing_column_count`
  行末の空欄列が省略されている行数です。
  人文系データでは、これは異常ではなくよくある書き方です。
  たとえば最後の `Remarks` 列が空なら、その空欄を行末で省いている場合があります。

- `max_column_count_seen`
  実際に見つかった行の中で、最も多かった列数です。
  これが `column_count` より大きい場合は、余分な列を持つ行があると考えられます。

## 列ごとの数値の読み方

スクリプトは次のような出力も返します。

```text
column_counts:
- SJID: non_empty=24381, empty=0
- SJ_entry_remarks: non_empty=2411, empty=21970
```

ここで見る点は次の 2 つです。

- `non_empty`
  その列に実際に値が入っている行数

- `empty`
  その列が空欄の行数

これは人文研究では、たとえば次のような判断に役立ちます。

- この列は必須項目か、補助項目か
- 注記欄は広く使われているか、特殊例だけか
- この表は全体として情報がよく埋まっているか

## 研究実務での読み方

### 1. まず構造を見る

最初に、その TSV を安全に読めるかを確認します。

- `irregular_row_count = 0`
  なら、列が増えすぎた行は見つかっていない
- `max_column_count_seen = column_count`
  なら、最大列数はヘッダと一致している

### 2. 次に規模を見る

- `row_count` が大きい
  項目数の多い大きな表
- `column_count` が大きい
  扱う情報の種類が多い表

これにより、最初から Excel で全件を見るべきか、より小さい表から入るべきかを判断しやすくなります。

### 3. 空欄の多い列を見る

たとえば `Remarks` の空欄が非常に多い場合は、

- 注記は特殊例だけに付く
- その列は構造上はあるが、毎行必須ではない

と理解できます。

## 人文系研究者向けの見方

これらの数値は、単なるプログラム診断ではなく、資料の編集構造を知る手がかりでもあります。

例:

- 行数が多く列数が少ない
  比較的そろった単純な表
- 行数は少ないが列数が多い
  研究向けに情報を細かく付した表
- 注記列の空欄が多い
  注記は選択的に付されている
- 行末省略が多い
  生の TSV 行の見た目は不均一でも、構造自体は規則的なことがある

## さらに確認した方がよい場合

次のようなときは、もう一段詳しく調べると安全です。

- `irregular_row_count` が 0 でない
- `max_column_count_seen` が `column_count` より大きい
- 重要な列なのに空欄が予想外に多い
- Excel で見た印象とスクリプト結果が食い違う

## Excel を使う人への実務メモ

Excel を中心に使う場合は、この出力を「取り込み前の点検結果」と考えるのがよいです。

- UTF-8 か確認する
- TAB 区切りか確認する
- 表の構造が安定しているか確認する
- その上で Excel に取り込む

これにより、列ずれや文字化けを見落としにくくなります。
