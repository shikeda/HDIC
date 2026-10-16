# TSJ 績・緝麻（s0401b801, s1229a307g）の注記追加と見出し字の訂正

## 概要

`TSJ_definitions.tsv` と `TSJ_entries.tsv` について、s0401b801（績）の `SJ_remarks` に考証を追加し、s1229a307g の見出し字「縃麻」を「緝麻」に訂正した。修正は2026-10-16に実施し、コミット `fcda8e6` に含まれる。構造確認には `count_basic_stats.py` を、参照の確認には `validate_hdic_integrity.py` を使った。

## 検出方法

データ作成者（池田氏）からの直接の修正依頼による。スクリプトによる自動検出ではない。

## 問題

- s0401b801（績）: `SJ_def` 中の「𦂒」字と和訓「乎宇牟」について、`SJ_remarks` に考証がなかった。
- s1229a307g: `Entry_word` が「縃麻」となっていたが、「緝麻」とすべきもの。原字は「⿰糸𦙃」で、「緝」の俗字にあたる。
- s1229a307（`TSJ_entries.tsv`）: `Entry` が「縃」、`Entry_original` が「◯」で、原字形が記録されていなかった。

## 修正内容

### TSJ_definitions.tsv

- s0401b801（績）`SJ_remarks`（新規追加。ユーザー提供の文面をそのまま入力した）
  - “𦂒”字未詳，張磊《校注》疑“緝”字訛衍。和訓“乎宇牟”即“ヲウム”，謂績麻苧成絲，乃名詞“ヲ（麻・苧）”與動詞“ウム（績む）”之連語。《新撰字鏡》臨時雜要字“緝麻”及《類聚名義抄》“績”、“紡”亦有此訓。
- s1229a307g
  - `Entry_word`: 縃麻 → 緝麻
  - `SJ_remarks`（新規追加）: “緝”原作“⿰糸𦙃”，緝之俗字。

### TSJ_entries.tsv

- s1229a307
  - `Entry`: 縃 → 緝
  - `Entry_original`: ◯ → ⿰糸𦙃
- 同じ `SJ2ID`（s1229a307g）に属する s1229a308（麻）は変更していない。

根拠はいずれもユーザーが示した考証による。各出典の原文は、この作業では照合していない。

## 結果

- `count_basic_stats.py`: `TSJ_definitions.tsv`（5列）と `TSJ_entries.tsv`（11列）のどちらも `irregular_row_count` は 0 で、`max_column_count_seen` は `column_count` と一致した。
- `validate_hdic_integrity.py`: 既知の参照切れのため終了コードは 1 だった。出力に s1229a307 は現れず、今回の修正による新たな参照切れはない。
- ヘッダーは `finalize_hdic_edit.py` で更新した。
  - `TSJ_definitions.tsv`: Version 1.2.71 → 1.2.72
  - `TSJ_entries.tsv`: Version 1.1.87 → 1.1.88
  - Last modified はいずれも 2026-10-16
