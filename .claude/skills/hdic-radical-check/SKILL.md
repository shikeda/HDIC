---
name: hdic-radical-check
description: TSJ（新撰字鏡）の部首単位の系統的点検キャンペーンを1部首ずつ進める。/loopから毎イテレーション呼ばれる想定、または「次の部首を点検して」といった単発の依頼でも使う。samples/planning/tsj_radical_check_progress.tsvの進捗トラッカーを見て次の対象を選び、hdic-tsv-validateで機械的に検出できる範囲の問題を洗い出し、見つかった問題は必ずユーザーに確認してからhdic-data-editで直す。トラッカー更新とコミットで1イテレーションを終える。
---

# hdic-radical-check

TSJ_entries.tsv を部首（`SJ_vol_radical`）単位で1つずつ回り、機械的に検出できる
範囲の問題を洗い出す定型フロー。過去のコミット履歴（例:
「新撰字鏡・連字の点検、山偏」）にある部首単位の点検作業を、進捗が追える形で
繰り返すためのもの。

## このSkillでできること・できないこと

**できること（機械的な検証）:**
- 対象部首のTSJ_entries.tsvの行について、`count_basic_stats.py` 相当の構造チェック
  （列数の乱れなど）
- `validate_hdic_integrity.py` が検出する参照切れ（`TBID`/`SYID`が
  `KTB.tsv`/`SYP.tsv`に実在するか）のうち、対象部首の行に該当するもの
- 表記・書式の既知のパターンからの逸脱（例: 宮澤氏引用がそのまま残っている等、
  `validate_hdic_integrity.py` のdocstringに記載のパターン）

**できないこと（このSkillの範囲外）:**
- 原本影印・活字翻刻との照合による字体・訓読の校訂そのもの。これは編集者の
  専門的判断を要する作業であり、このSkillはそれを代行しない。機械的な点検で
  「問題なし」であっても、それは「影印と照合して正しい」ことを意味しない。
- 見つかった問題の解釈・修正内容の決定。**必ずユーザーに提示し、承認を得てから
  `hdic-data-edit` skillで直す。** 過去に注記表記の意味を早合点して誤った判断を
  したことがある（`validate_hdic_integrity.py` のdocstring参照）。この教訓を
  このSkillでも徹底する。

## 1イテレーションの手順

1. **次の対象を選ぶ**
   `samples/planning/tsj_radical_check_progress.tsv` を読み、
   `status` が `未確認` の行のうち、`vol_radical` の順で最初の1件を選ぶ
   （`進行中` の行があればそれを優先する）。全行が `完了` なら、その旨を
   ユーザーに報告してループを止める（次に何をすべきかユーザーに確認する）。

2. **対象範囲を絞り込む**
   選んだ `vol_radical` に該当する `TSJ_entries.tsv` の行を `grep`/`awk` 等で
   抽出する。

3. **機械的な検証を行う**
   - `python3 samples/statistics/count_basic_stats.py TSJ_entries.tsv` の結果のうち、
     対象部首の行に関係する問題がないか確認する。
   - `python3 samples/scripts/validate_hdic_integrity.py` の出力のうち、
     対象部首の `SJID` を含む行がないか確認する。
   - 問題が見つからなければ手順5へ。

4. **問題が見つかった場合**
   - 具体的な行・値をユーザーに提示する。**このSkill自身は修正内容を判断しない。**
   - ユーザーから修正方針の確認が得られたら `hdic-data-edit` skillの手順で修正する。
   - 修正が複数ファイル・複数件にまたがる、または根拠の説明が要るものであれば
     `hdic-update-log` skillでログを残す。
   - 判断がつかない・ユーザーの確認が得られない場合は、その部首を `進行中` の
     ままトラッカーに記録し、**ループをここで止めて**ユーザーに報告する
     （自動ループの中で未確認のまま次に進まない）。

5. **トラッカーを更新する**
   対象行の `status` を `完了`（問題なし、または修正済みの場合）または
   `進行中`（判断待ちの場合）に、`last_checked_date` を実行日に更新する。
   見つけた内容や判断待ちの点があれば `notes` に一言残す。

6. **コミットする**
   - トラッカー更新のみのコミットと、データ修正のコミットは分ける
     （`hdic-data-edit` の慣習に合わせる）。
   - コミットメッセージ例: `chore: mark TSJ v6#60 山部第六十一 as checked
     (no issues found)` / `fix: correct ... (TSJ v6#60 山部第六十一 review)`
   - ユーザーの承認を得るまで `git commit` は実行しない。

7. **次のイテレーションへ**
   `/loop` から呼ばれている場合はここで1イテレーション終了。次のイテレーションは
   このSkillを最初から実行し、トラッカーの次の未確認部首に進む。単発の依頼として
   呼ばれた場合はここで終了し、結果をユーザーに報告する。

## /loopでの起動方法（ユーザー向けメモ）

このSkillはユーザーが `/loop` コマンドで明示的に起動する。例:
```
/loop hdic-radical-check skillでTSJの次の部首を1つ点検して
```
間隔を指定しなければ自己ペースで進む。問題が見つかって判断待ちになった場合は
ループが止まる設計なので、放置しても誤った自動修正が積み重なることはない。

## 注意

- 対象は `TSJ_entries.tsv` のみ（`samples/planning/tsj_radical_check_progress.tsv`
  も TSJ 専用）。`KTB.tsv`/`SYP.tsv`/`YYP.tsv` を同様の方式で回したくなった場合は、
  同じ形式のトラッカーを別途作成すること（このSkillを流用改変する）。
- `KRM.tsv` 系列は対象外（README.mdの記載どおり凍結中）。
