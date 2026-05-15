# HDIC Root Files Survey

This note summarizes the files directly under `~/hdic-git/HDIC` based on their actual contents, not only on filename conventions.

## Overall structure

The repository root mainly contains TSV/TXT datasets for several Hanzi dictionaries used in early Japan and related source-link tables.

- `TSJ*`: Tenjibon *Shinsen Jikyō*.
- `KRM*`: Kanchiinbon *Ruiju Myōgishō*.
- `KTB*`: Kōsanji-bon *Tenrei Banshō Meigi*.
- `SYP*`: Songben *Yupian*.
- `GLS*`: *Longkan Shoujing* source-link data.
- `YQF.tsv`: metadata comments for *Yupian* quoted fragments, but no tabular body is currently present.

Recurring file patterns:

- main dictionary files: full text or entry-level datasets
- `*_definitions*`: definition-level splits
- `*_wakun*`: extracted Japanese readings
- `*_ndl*` / `*_keio*`: mappings from dictionary locations to image/library URLs
- `*_Seal*`: image region coordinates for seal-script forms

## File-by-file findings

### Documentation and license

- `README.md`
  - Project overview for HDIC.
  - Lists publication dates, target dictionaries, and the HDIC Viewer URL.
  - Describes intended meanings of many root files, but some details are older than the current file set.

- `LICENSE`
  - Contains the full text of Creative Commons BY-NC-SA 4.0.
  - This differs from `README.md`, which says CC BY-SA 4.0. The root documentation and license file are inconsistent on this point.

### TSJ: Tenjibon Shinsen Jikyō

- `TSJ_entries.tsv`
  - 11 columns, 24,381 data rows.
  - Header: `SJID`, `SJ2ID`, `SJ_Rinsen`, `SJ_vol_radical`, `SJ_radical`, `Entry`, `Entry_original`, `SJ_source`, `SJ_entry_remarks`, `TBID`, `SYID`.
  - Full headword list. Includes cross-references to `KTB` and `SYP`.

- `TSJ_definitions.tsv`
  - 5 columns, 19,979 data rows.
  - Header: `TSJ2ID`, `Entry_word`, `SJ_def`, `SJ_remarks`, `ZhangLei_page`.
  - Definition-level table keyed by `TSJ2ID`.

- `TSJ_wakun.tsv`
  - 15 columns, 3,828 data rows.
  - Header includes reading forms in man'yogana, historical kana, normalized kana, and reference IDs such as `nikkoku_id`.
  - Specialized wakun extraction table with editorial notes.

- `TSJ_ndl.tsv`
  - 5 columns, 789 data rows.
  - Header: `SJ_vol`, `SJ_vol_leaf`, `SJ_Rinsen_p`, `NDL_URL_813.2-Sy968s_1916`, `NIJL_Shoryobu_micro`.
  - Page/link mapping table from TSJ locations to NDL and NIJL resources.

### KRM: Kanchiinbon Ruiju Myōgishō

- `KRM.tsv`
  - 12 columns, 32,607 data rows.
  - Header: `KRID_n`, `KRID_sn`, `KR2ID`, `KRID`, `KR_Tenri_p`, `KR_vol_name`, `KR_radical`, `KR_vol_radical`, `Entry`, `Entry_original`, `Def`, `Remarks`.
  - Main full-text table. Definitions are embedded in the `Def` column.

- `KRM_definitions.tsv`
  - 9 columns, 86,796 data rows.
  - Header: `KRID_no`, `KR2ID`, `Entry`, `Def`, `Def_code`, `Def_name`, `Word_form`, `JK_URL`, `Remarks`.
  - Fine-grained definition table with type codes such as `和訓`, `義注`, and `音注`.

- `KRM_wakun.tsv`
  - 10 columns, 36,354 data rows.
  - Header: `KRID_wakun_no`, `KR2ID`, `Entry`, `Def`, `Word_form`, `Wakun_Hanzi`, `Wakun_variant`, `Hanzi_variant`, `JK_ID`, `Remarks`.
  - Large wakun extraction table with normalized word forms and variant notation.

- `KRM_ndl.txt`
  - 5 columns, 1,322 data rows.
  - Header: `Book`, `Radical`, `Kazama`, `Tenri`, `NDL_url`.
  - Source alignment table linking KRM book/radical positions to print editions and NDL pages.

### KTB: Kōsanji-bon Tenrei Banshō Meigi

- `KTB.tsv`
  - 12 columns, 18,932 data rows.
  - Header: `TBID`, `TB_vol_radical`, `TB_radical`, `Entry`, `Entry_type`, `Entry_diff`, `TB_def`, `SYID`, `YYID`, `TB_remarks`, `Lv_page`, `Zang_page`.
  - Full-text dataset. Includes entry type labels such as `Regular_seal`, `Embedded_seal`, and `Embedded_clerical`.

- `KTB_entries.txt`
  - 9 columns, 18,931 data rows.
  - Header: `TBID`, `TB_vol_radical`, `TB_radical`, `Entry`, `Entry_type`, `Entry_diff`, `SYID`, `YYID`, `TB_remarks`.
  - Entry-only version of KTB without the main definition/page columns found in `KTB.tsv`.

- `KTB_ndl.txt`
  - 4 columns, 1,841 data rows.
  - Header: `Vol_radical`, `KTB_vol Radical`, `Book_leaf`, `NDL_url`.
  - Mapping from volume/radical and book leaf positions to NDL pages.

- `KTB_ndl_Seal.tsv`
  - 6 columns, 1,042 data rows.
  - Header: `TB_Seal_ID`, `NDL_IIIF_Image_API_Base_URI`, `x`, `y`, `width`, `height`.
  - IIIF image crop coordinates for seal-script glyph regions.

### SYP: Songben Yupian

- `SYP.tsv`
  - 9 columns, 22,809 data rows.
  - Header: `SYID`, `SY_vol_radical`, `SY_radical`, `Entry`, `Entry_original`, `SY_def`, `Zang_page`, `KSY_diff`, `SY_remarks`.
  - Main Songben *Yupian* text dataset.

- `SYP_keio.tsv`
  - 7 columns, 987 data rows.
  - Header: `Vol_radical`, `Book`, `Leaf`, `Recto-verso`, `Radical`, `Keio_url`, `Page_iiif`.
  - Link table from SYP positions to Keio IIIF manifests/pages.

### Other supporting files

- `GLS_ndl.txt`
  - 4 columns, 761 data rows.
  - Header: `GLS_Zhonghua`, `GLS_vol_radical`, `GLS_radical`, `NDL_url`.
  - NDL page mapping table for *Longkan Shoujing* radicals.

- `YQF.tsv`
  - No non-comment tabular body detected.
  - The current file consists of comment lines documenting abbreviation systems and bibliographic sources for *Yupian* quoted fragments.

## Practical takeaways for sample scripts

- If a file starts with many `#` lines, the first real header may appear much later in the file.
- `TSJ_entries.tsv`, `KRM.tsv`, `KTB.tsv`, and `SYP.tsv` are the main starting points for entry-level analysis.
- Wakun analysis should use `TSJ_wakun.tsv` or `KRM_wakun.tsv`, not the full-text files.
- Image linking tasks should use `TSJ_ndl.tsv`, `KRM_ndl.txt`, `KTB_ndl.txt`, `KTB_ndl_Seal.tsv`, `SYP_keio.tsv`, or `GLS_ndl.txt`.

---

# HDIC 直下ファイル調査メモ

このメモは、`~/hdic-git/HDIC` 直下にあるファイルについて、ファイル名だけでなく実際の中身を確認した結果をまとめたものです。

## 全体構成

リポジトリ直下には、主として日本古辞書・漢字字書に関する TSV/TXT データと、その画像リンク対応表が置かれています。

- `TSJ*`: 天治本『新撰字鏡』
- `KRM*`: 観智院本『類聚名義抄』
- `KTB*`: 高山寺本『篆隷万象名義』
- `SYP*`: 宋本『玉篇』
- `GLS*`: 『龍龕手鏡』の典拠ページ対応データ
- `YQF.tsv`: 『玉篇』逸文の典拠略号などを説明するコメント群。現状では表形式データ本体は見当たりません

共通するファイルパターン:

- 本体データ: 見出し語単位または全文テキスト単位のデータ
- `*_definitions*`: 定義単位に分割したデータ
- `*_wakun*`: 和訓抽出データ
- `*_ndl*` / `*_keio*`: 辞書中の位置と画像・所蔵機関 URL の対応表
- `*_Seal*`: 篆書字形の画像切り出し座標

## ファイル別の確認結果

### 文書・ライセンス

- `README.md`
  - HDIC 全体の概要説明です。
  - 公開日、対象辞書、HDIC Viewer へのリンクが記載されています。
  - 直下ファイルの説明もありますが、現状のファイル構成や名称と少しずれている箇所があります。

- `LICENSE`
  - Creative Commons BY-NC-SA 4.0 の全文です。
  - 一方で `README.md` では CC BY-SA 4.0 と書かれており、両者の表記は一致していません。

### TSJ: 天治本『新撰字鏡』

- `TSJ_entries.tsv`
  - 11 列、24,381 行のデータです。
  - ヘッダ: `SJID`, `SJ2ID`, `SJ_Rinsen`, `SJ_vol_radical`, `SJ_radical`, `Entry`, `Entry_original`, `SJ_source`, `SJ_entry_remarks`, `TBID`, `SYID`
  - 見出し字の総覧です。`KTB` と `SYP` への対応 ID も含みます。

- `TSJ_definitions.tsv`
  - 5 列、19,979 行のデータです。
  - ヘッダ: `TSJ2ID`, `Entry_word`, `SJ_def`, `SJ_remarks`, `ZhangLei_page`
  - `TSJ2ID` をキーとする定義単位のテーブルです。

- `TSJ_wakun.tsv`
  - 15 列、3,828 行のデータです。
  - 万葉仮名、歴史的仮名遣い、正規化した読み、参照 ID などを含みます。
  - 和訓抽出専用のテーブルで、注記列もあります。

- `TSJ_ndl.tsv`
  - 5 列、789 行のデータです。
  - ヘッダ: `SJ_vol`, `SJ_vol_leaf`, `SJ_Rinsen_p`, `NDL_URL_813.2-Sy968s_1916`, `NIJL_Shoryobu_micro`
  - TSJ 内の位置と NDL・NIJL の画像参照先を結ぶ対応表です。

### KRM: 観智院本『類聚名義抄』

- `KRM.tsv`
  - 12 列、32,607 行のデータです。
  - ヘッダ: `KRID_n`, `KRID_sn`, `KR2ID`, `KRID`, `KR_Tenri_p`, `KR_vol_name`, `KR_radical`, `KR_vol_radical`, `Entry`, `Entry_original`, `Def`, `Remarks`
  - 全文テキスト版の主データです。定義は `Def` 列にまとまって入っています。

- `KRM_definitions.tsv`
  - 9 列、86,796 行のデータです。
  - ヘッダ: `KRID_no`, `KR2ID`, `Entry`, `Def`, `Def_code`, `Def_name`, `Word_form`, `JK_URL`, `Remarks`
  - 定義を細かく分割したテーブルで、`和訓`、`義注`、`音注` などの種別コードを持ちます。

- `KRM_wakun.tsv`
  - 10 列、36,354 行のデータです。
  - ヘッダ: `KRID_wakun_no`, `KR2ID`, `Entry`, `Def`, `Word_form`, `Wakun_Hanzi`, `Wakun_variant`, `Hanzi_variant`, `JK_ID`, `Remarks`
  - 正規化語形や異表記を含む大規模な和訓抽出テーブルです。

- `KRM_ndl.txt`
  - 5 列、1,322 行のデータです。
  - ヘッダ: `Book`, `Radical`, `Kazama`, `Tenri`, `NDL_url`
  - 観智院本の冊・部首位置と版面・NDL 画像を対応づける表です。

### KTB: 高山寺本『篆隷万象名義』

- `KTB.tsv`
  - 12 列、18,932 行のデータです。
  - ヘッダ: `TBID`, `TB_vol_radical`, `TB_radical`, `Entry`, `Entry_type`, `Entry_diff`, `TB_def`, `SYID`, `YYID`, `TB_remarks`, `Lv_page`, `Zang_page`
  - 本文付きの主データです。`Regular_seal`、`Embedded_seal`、`Embedded_clerical` などの字形種別を含みます。

- `KTB_entries.txt`
  - 9 列、18,931 行のデータです。
  - ヘッダ: `TBID`, `TB_vol_radical`, `TB_radical`, `Entry`, `Entry_type`, `Entry_diff`, `SYID`, `YYID`, `TB_remarks`
  - `KTB.tsv` から定義列やページ列を外した見出し語中心の版です。

- `KTB_ndl.txt`
  - 4 列、1,841 行のデータです。
  - ヘッダ: `Vol_radical`, `KTB_vol Radical`, `Book_leaf`, `NDL_url`
  - 巻・部首・丁番号と NDL 画像 URL の対応表です。

- `KTB_ndl_Seal.tsv`
  - 6 列、1,042 行のデータです。
  - ヘッダ: `TB_Seal_ID`, `NDL_IIIF_Image_API_Base_URI`, `x`, `y`, `width`, `height`
  - 篆書字形部分を切り出すための IIIF 座標データです。

### SYP: 宋本『玉篇』

- `SYP.tsv`
  - 9 列、22,809 行のデータです。
  - ヘッダ: `SYID`, `SY_vol_radical`, `SY_radical`, `Entry`, `Entry_original`, `SY_def`, `Zang_page`, `KSY_diff`, `SY_remarks`
  - 宋本『玉篇』本文の主データです。

- `SYP_keio.tsv`
  - 7 列、987 行のデータです。
  - ヘッダ: `Vol_radical`, `Book`, `Leaf`, `Recto-verso`, `Radical`, `Keio_url`, `Page_iiif`
  - SYP 内の位置と慶應の IIIF マニフェスト・ページ情報の対応表です。

### その他の補助ファイル

- `GLS_ndl.txt`
  - 4 列、761 行のデータです。
  - ヘッダ: `GLS_Zhonghua`, `GLS_vol_radical`, `GLS_radical`, `NDL_url`
  - 『龍龕手鏡』の部首位置と NDL ページを対応づける表です。

- `YQF.tsv`
  - 非コメント行から成る表形式データ本体は確認できませんでした。
  - 現状の中身は、『玉篇』逸文に関する略号説明と参考文献情報のコメント行です。

## サンプルスクリプト作成時の実務メモ

- `#` コメント行が多数続くファイルでは、実際のヘッダ行がかなり後ろに現れることがあります。
- 見出し語・本文レベルの分析は `TSJ_entries.tsv`、`KRM.tsv`、`KTB.tsv`、`SYP.tsv` から始めるのが基本です。
- 和訓分析には全文ファイルではなく、`TSJ_wakun.tsv` または `KRM_wakun.tsv` を使うのが適切です。
- 画像リンクや紙面参照には `TSJ_ndl.tsv`、`KRM_ndl.txt`、`KTB_ndl.txt`、`KTB_ndl_Seal.tsv`、`SYP_keio.tsv`、`GLS_ndl.txt` を使えます。
