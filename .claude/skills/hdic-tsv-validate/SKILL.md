---
name: hdic-tsv-validate
description: HDICのルート直下TSV/TXT（TSJ_entries.tsv, TSJ_definitions.tsv, KTB.tsv, SYP.tsv, YYP.tsv等）を変更した後、コミット前に構造とクロスファイル参照の整合性を点検する定型フロー。「変更後にチェックして」「コミット前に確認して」といった依頼、または他のskill（hdic-data-edit等）から呼び出される。count_basic_stats.pyとvalidate_hdic_integrity.pyをまとめて実行し、結果を要約する。
---

# hdic-tsv-validate

HDICのルート直下データファイルを変更した後、コミット前に必ず行う点検の定型フロー。
CLAUDE.mdの「コミット前検証」ルールをこのSkillで実行する。

## 手順

1. **対象ファイルの特定**
   - 引数でファイルが指定されていればそれを対象にする。
   - 指定がなければ `git diff --name-only HEAD` で変更されたルート直下の
     `*.tsv`/`*.txt` を対象にする（`work/`・`samples/`配下は対象外）。

2. **構造検証（count_basic_stats.py）**
   ```bash
   python3 samples/statistics/count_basic_stats.py <file>
   ```
   対象ファイルそれぞれについて実行し、`irregular_row_count == 0` と
   `max_column_count_seen == column_count` を確認する。どちらかが崩れていたら、
   該当ファイルのどの行が原因か（`grep` 等で）特定し、ユーザーに報告する。
   自分で「直してよい」と判断せず、まず状況を報告すること。

3. **クロスファイル参照検証（validate_hdic_integrity.py）**
   変更ファイルが `SJID`/`SJ2ID`/`TSJ2ID`/`TBID`/`SYID`/`YYID` のいずれかの列を
   含む場合（TSJ_entries.tsv, TSJ_definitions.tsv, KTB.tsv, SYP.tsv, YYP.tsv）、
   以下を実行する。
   ```bash
   python3 samples/scripts/validate_hdic_integrity.py
   ```
   - 終了コード0なら「参照切れなし」として報告終了。
   - 終了コード1の場合、**出力された `broken_reference`/`duplicate_key` の
     具体的な値が、今回自分が編集したIDと一致するかを確認する**
     （`grep` で編集前後の値を照合するなど）。一致しなければ「既知の
     未解決事項であり今回の変更とは無関係」と明記して報告する。一致すれば
     今回の編集が原因の可能性が高いので、ユーザーに報告し、勝手に修正しない。

4. **結果の要約をユーザーに提示する**
   - 構造・参照ともに問題なし → その旨を簡潔に報告し、コミット準備完了と伝える。
   - 問題あり → 該当ファイル・行・値を具体的に示す。

## 注意

- どちらのスクリプトも読み取り専用。データは一切変更しない。
- `validate_hdic_integrity.py` の参照値の正規化ルール（`△`/`▽`/括弧付き注記/
  末尾`*`/前後の項目参照など）はスクリプト自身のdocstringに詳細な根拠とともに
  記載されている。新しい注記パターンに遭遇して解釈に迷った場合は、
  スクリプトのロジックを勝手に拡張して「これはこういう意味のはずだ」と
  仮定しない。実データを前後の行や関連ファイルと突き合わせて根拠を確認するか、
  それでも判断がつかなければユーザー（データの作成者）に確認する。
  過去に一度、`△(id)` のような注記表記を「意味のない注記だから丸ごと無視してよい」
  と早合点したが、実際には括弧内のIDが実在する検証可能な参照だったケースがある。
  注記の意味を機械的に決め打ちしないこと。
