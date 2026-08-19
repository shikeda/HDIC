---
name: hdic-data-edit
description: HDICのルート直下データファイル（TSJ_entries.tsv, TSJ_definitions.tsv, TSJ_wakun.tsv, KTB.tsv, SYP.tsv, YYP.tsv等）の内容を修正する依頼が来たときに使う。1行〜数行単位の直接編集を安全に行い、count_basic_stats.py・finalize_hdic_edit.py・validate_hdic_integrity.pyを組み合わせて後始末し、diff確認とコミットメッセージ案の提示までを行う定型フロー。KRM.tsv/KRM_definitions.tsv/KRM_wakun.tsvは対象外（github.com/shikeda/krmのkrm_*.tsvに一本化されており凍結中）。
---

# hdic-data-edit

HDICのルート直下TSV（`KRM.tsv`系を除く。README.md参照）を修正する依頼を受けたときの手順。

## 手順

1. **対象行の特定**
   - 依頼が「旧行→新行」の形式（TSVの1行をまるごと貼られた）なら、その旧行を
     そのまま `old_string` に使えばよい。
   - 依頼が「`s0628b402` の定義文の『抬字』を『枱字』に直して」のような
     セル指定なら、まず `grep` で対象行を確認してから旧行・新行を組み立てる。
   - 変更後の列数が変更前と一致することを確認する（TSVはタブ区切り固定列数）。
   - 変更対象のIDが他ファイルから参照されている（`TBID`/`SYID`/`YYID`/
     `TSJ2ID`/`SJ2ID` 列など）場合、関連ファイルにも同様の値が存在しないか
     `grep` で確認しておく（後述の検証で機械的な転記漏れとして検出されることが
     多いため、先に把握しておくと後の手戻りが減る）。

2. **Editツールで行を書き換える**
   - `Edit` の `old_string`/`new_string` に行全体を渡す（部分列だけでなく行全体を
     渡すと、同じ値を持つ他の行との誤マッチを避けやすい）。
   - `old_string` が複数行にマッチしてエラーになった場合は、ID列などを含めて
     一意になるまで前後の文脈を広げる。安易に `replace_all` は使わない。
   - 複数ファイルにまたがる修正（例: `KTB.tsv` の確定を受けて `TSJ_entries.tsv`
     側の古い転記も直す）なら、この手順をファイルごとに繰り返す。

3. **`hdic-tsv-validate` skillの手順を実行する**
   `count_basic_stats.py` と（該当すれば）`validate_hdic_integrity.py` を実行する。
   問題が見つかっても、**注記表記（`△(id)` や `(前項)` のような値）の意味を
   自分で決め打ちしない**。前後の行や関連ファイルと突き合わせて根拠を確認できる
   範囲でのみ判断し、判断がつかない・複数の解釈がありうる場合はユーザーに確認する。
   実例: 過去に「注記だからノイズとして無視してよい」と早合点したが、実際には
   ユーザーだけが知る出典（宮澤俊雅『掲出字一覽表』等）に基づく意図的な注記で、
   桁落ちなどの実修正が必要なケースだった。

4. **後始末スクリプトを実行する**
   ```bash
   python3 samples/scripts/finalize_hdic_edit.py
   ```
   - 引数なしで実行すると、`git diff` から変更されたTSV/TXTを自動検出し、
     それぞれの `Version` をHEAD基準で+1、`Last update`/`Last modified` を
     実行日に更新する。
   - このスクリプトを複数回実行しても、コミット前なら同じ結果に収束する
     （安全に再実行可）。

5. **diffを提示する**
   `git diff --stat` と、データ行の変更部分の `git diff` を要約してユーザーに見せる。
   ヘッダーのVersion/Last update行の変化も一言添える。

6. **コミットメッセージ案を提示し、確認を待つ**
   - 既存の履歴の書式に合わせる（例: `fix: correct 抬字 to 枱字 for 鈶 definition
     (s0628b402)`）。件名は英語、対象のIDで特定できるようカッコ書きで添える。
   - **ツール・スクリプトの追加/変更**（`finalize_hdic_edit.py` 自体の修正など）と
     **データ行の修正**は、別コミットに分ける（このリポジトリの既存の慣習）。
   - **ユーザーの明示的な承認を得るまで `git commit` は実行しない。**
   - コミット時は対象ファイルを明示的に `git add <file>...` で指定する
     （`git add -A`/`git add .` は使わない）。複数の関心事（ツール追加とデータ
     修正など）を同時に編集している場合、**必ず `git diff --cached --stat` で
     ステージ内容を確認してから** `git commit` する。コミットメッセージの
     内容とステージされているファイルが一致しているかを必ず確認すること
     （過去に、ツール追加の説明文のままデータ修正だけがステージされた状態で
     コミットしてしまい、`git reset --soft HEAD~1` でやり直した実例がある）。

## 注意

- `finalize_hdic_edit.py` はデータ行を一切変更しない。ヘッダー更新専用。
- `validate_hdic_integrity.py` は読み取り専用。データは一切変更しない。
- 複数の見出し語にまたがる一括修正（数十件規模）は、1件ずつこの手順を回すより、
  すべてのEditを終えてから `finalize_hdic_edit.py` を1回だけ実行する方が正しい
  （Versionは「今回の変更全体」に対して1回だけ上がる想定）。
- `git push` は別途明示的な指示がない限り行わない。
