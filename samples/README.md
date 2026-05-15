# HDIC Samples

This directory contains sample analyses for HDIC datasets.

You can:
- count entries
- compare dictionaries
- extract wakun
- analyze definition patterns
- connect entries to IIIF images

Recommended starting files:
- TSJ_entries.tsv
- TSJ_wakun.tsv
- KRM.tsv

Beginner-friendly starting points:
Start with TSJ_entries.tsv if you are unsure.

| Purpose | Open this file |
| --- | --- |
| Basic entries | `TSJ_entries.tsv` |
| Wakun analysis | `TSJ_wakun.tsv` |
| Detailed definitions | `KRM_definitions.tsv` |
| IIIF images | `SYP_keio.tsv` |

The beginner statistics tool is also useful as a TSV safety check before opening data in Excel or using it in AI-assisted analysis.
It can help detect:
- malformed TSV rows
- missing TAB separators between columns
- trailing or missing empty columns at the end of a row

## Basic statistics

```bash
python3 samples/statistics/count_basic_stats.py TSJ_entries.tsv
```

## Opening TSV files in Excel

Recommended procedure (Windows Excel):

1. Open Excel
2. Data -> From Text/CSV
3. Select UTF-8 encoding
4. Select TAB delimiter

Do not open TSV files by double-clicking them directly,
because Excel may misinterpret encoding or delimiters.

## HDIC TSV conventions

Most HDIC datasets follow these conventions:

- UTF-8 encoding
- TAB-separated columns
- `#` comment lines before headers
- optional omission of trailing empty fields
- stable identifier columns (e.g. `TSJID`, `KRID`, `SYID`)

Some datasets may contain:

- embedded annotations
- image linkage tables
- IIIF coordinate data

## Dataset characteristics

Different HDIC datasets have different structures.

Examples:

- TSJ: entry-oriented and cross-linked
- SYP: uniform definition-centered structure
- KRM: research-oriented multi-layer data
- KTB: linkage and IIIF-oriented datasets

## AI-assisted analysis

HDIC samples are designed to work with AI coding assistants such as:

- Codex
- Claude Code
- Gemini CLI

Recommended workflow:

1. inspect TSV structure
2. run beginner statistics
3. validate TSV consistency
4. perform exploratory analysis

## Example outputs

See:

- [sample_output.md](statistics/sample_output.md)

## TSV Handling Policy

The statistics tool distinguishes:

- irregular rows (more columns than expected)
- trailing omitted empty columns

because many humanities TSV datasets omit final empty fields.

In practice, this means:

- rows with extra columns are treated as structural problems
- rows that only omit empty fields at the end are counted separately
- omitted trailing empty fields are padded back internally before counting blank cells

Detailed root-file survey:
[HDIC_root_files_survey.md](planning/HDIC_root_files_survey.md)

---

# HDIC サンプル

このディレクトリには、HDIC データセットを対象にしたサンプル分析を置きます。

できること:
- 項目数を数える
- 辞書どうしを比較する
- 和訓を抽出する
- 定義のパターンを分析する
- 項目を IIIF 画像に対応づける

推奨する開始ファイル:
- TSJ_entries.tsv （特におすすめ）
- TSJ_wakun.tsv
- KRM.tsv

初心者向けの入り口:

| 目的 | 開くファイル |
| --- | --- |
| 基本項目 | `TSJ_entries.tsv` |
| 和訓分析 | `TSJ_wakun.tsv` |
| 詳細定義 | `KRM_definitions.tsv` |
| IIIF画像 | `SYP_keio.tsv` |

beginner 向け統計ツールは、Excel で開く前や AI エージェントで処理する前の TSV 点検にも使えます。
次のような問題の検出に役立ちます。
- TSV の列ずれ行
- 列と列のあいだの TAB 区切り欠落
- 行末の余分な空欄列、または不足している空欄列

## 基本統計

```bash
python3 samples/statistics/count_basic_stats.py TSJ_entries.tsv
```

## ExcelでTSVを開く方法

推奨手順（Windows 版 Excel）:

1. Excel を開く
2. 「データ」→「テキストまたは CSV から」
3. 文字コードで UTF-8 を選ぶ
4. 区切り文字で TAB を選ぶ

TSV ファイルを直接ダブルクリックして開く方法はおすすめしません。  
Excel が文字コードや区切り文字を誤認することがあるためです。

## HDIC の TSV 慣例

HDIC のデータセットの多くは、次のような慣例に従っています。

- UTF-8 文字コード
- TAB 区切り
- ヘッダの前に `#` コメント行がある
- 行末の空欄項目が省略されることがある
- 安定した ID 列がある
  例: `TSJID`, `KRID`, `SYID`

データセットによっては、次のような内容も含みます。

- 本文中の注記
- 画像参照対応表
- IIIF 座標データ

## データセットごとの特徴

HDIC のデータセットは、すべて同じ構造ではありません。

例:

- TSJ: 見出し字中心で、他資料との対応づけが多い
- SYP: 比較的そろった定義中心の構造
- KRM: 研究用に細かく分かれた多層データ
- KTB: 対応表や IIIF 利用を意識したデータが多い

## AI 支援分析

HDIC samples は、次のような AI コーディング支援ツールでの利用を想定しています。

- Codex
- Claude Code
- Gemini CLI

推奨する流れ:

1. TSV の構造を確認する
2. beginner 統計を実行する
3. TSV の整合性を点検する
4. 探索的な分析に進む

## 出力例

参照:

- [sample_output.md](statistics/sample_output.md)

## TSV処理方針

統計ツールは、次の 2 つを区別して扱います。

- 列数が想定より多い不規則行
- 行末の空欄列が省略されている行

これは、人文系の TSV データでは末尾の空欄項目が省略されることがよくあるためです。

実際の処理方針は次のとおりです。

- 余分な列がある行は、構造上の問題として扱う
- 行末の空欄省略だけの行は、別に数える
- 行末で省略された空欄列は、空欄数を数える前に内部で補って読む

詳細な直下ファイル調査メモ:
[HDIC_root_files_survey.md](planning/HDIC_root_files_survey.md)
