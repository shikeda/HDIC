# TSJ Beginner Statistics Notes

このメモは、`count_basic_stats.py` で確認した新撰字鏡 (`TSJ`) 関連 TSV の基本統計を、初心者向けに読みやすくまとめたものです。

対象ファイル:

- `TSJ_entries.tsv`
- `TSJ_definitions.tsv`
- `TSJ_wakun.tsv`
- `TSJ_ndl.tsv`

## 全体像

TSJ には、ひとつの大きな表だけではなく、役割の違う 4 種類の TSV があります。

- `TSJ_entries.tsv`
  見出し字の一覧です。いちばん基本になる入口ファイルです。
- `TSJ_definitions.tsv`
  見出し字に対する定義をまとめた表です。
- `TSJ_wakun.tsv`
  和訓を抜き出した表です。
- `TSJ_ndl.tsv`
  画像・ページ参照のための対応表です。

この 4 ファイルを見ると、TSJ データは
「見出し字」
「定義」
「和訓」
「画像参照」
を分けて管理していることが分かります。

## 基本統計から分かる特徴

### 1. `TSJ_entries.tsv` は最も基本になる表

- データ行数は `24,381` 行です。
- 列数は `11` 列です。
- `SJID`、`SJ2ID`、`SJ_Rinsen`、`SJ_vol_radical`、`Entry` など、見出し字を識別し、他資料と対応づける列がそろっています。
- `TBID` と `SYID` がかなり多く埋まっているので、`篆隷万象名義` や `宋本玉篇` との比較の入口にもなります。

初心者にとっては、まずこのファイルを見れば
「どの字がどこに立項されているか」
をつかみやすいです。

### 2. `TSJ_definitions.tsv` は定義中心の表

- データ行数は `19,979` 行です。
- 列数は `5` 列で、比較的シンプルです。
- `TSJ2ID` と `Entry_word` を軸に、`SJ_def` に定義本文が入っています。
- `SJ_remarks` は `1,631` 件だけ埋まっており、注記は必要なところだけ付けられていると考えられます。

このファイルは、語義や説明の文章を読みたいときに向いています。

### 3. `TSJ_wakun.tsv` は和訓研究用の表

- データ行数は `3,828` 行です。
- 列数は `15` 列で、4 ファイルの中では最も細かい情報を持っています。
- `reading_kana_kanji`、`reading_historical_kana`、`def_manyogana`、`nikkoku_id` など、和訓の表記や参照情報がそろっています。
- `remarks` は `291` 件だけなので、全件に長い注があるわけではありません。

つまり、TSJ 全体の中から和訓に関係するデータだけを研究しやすい形に切り出した表といえます。

### 4. `TSJ_ndl.tsv` は画像参照のための表

- データ行数は `789` 行です。
- 列数は `5` 列です。
- すべての列が `789` 件埋まっており、欠けがありません。
- `NDL_URL_813.2-Sy968s_1916` と `NIJL_Shoryobu_micro` があるため、紙面画像への接続に使いやすい表です。

このファイルは、本文の分析というより、画像・影印とデータをつなぐための案内表です。

### 5. `TSJ_entries.tsv` には少数の不規則行がある

- `TSJ_entries.tsv` だけ `irregular_row_count = 3` でした。
- `max_column_count_seen = 12` で、ヘッダの 11 列より多い行が少数あります。

これは初心者にとって大事な点で、TSV は「いつも完全にきれいな表」とは限りません。
したがって、Excel で開く前に `count_basic_stats.py` で構造確認をする意味があります。

## 初心者向けメモ

### 1. file size とは何か

`file size` は、そのファイルがディスク上でどれくらいの大きさかを示します。

今回の TSJ ファイルでは:

- `TSJ_entries.tsv`: 約 `2.3M`
- `TSJ_definitions.tsv`: 約 `1.3M`
- `TSJ_wakun.tsv`: 約 `531K`
- `TSJ_ndl.tsv`: 約 `94K`

初心者向けに言えば、

- サイズが大きいほど、行数や情報量が多いことが多い
- `TSJ_entries.tsv` と `TSJ_definitions.tsv` はやや大きい
- `TSJ_ndl.tsv` はかなり小さく、参照表として扱いやすい

という理解で十分です。

### 2. encoding とは何か

`encoding` は、文字をファイルの中でどのように保存しているかを表す設定です。

今回の TSJ ファイルはすべて:

- `UTF-8`

でした。

これは日本語や漢字を扱うときによく使う標準的な文字コードです。  
Excel で開くときに文字化けする場合は、「UTF-8 で読み込む」と意識するとよいです。

### 3. delimiter とは何か

`delimiter` は、列と列の区切り記号のことです。

今回の TSJ ファイルでは:

- `TAB` 区切り

です。

つまり、見た目には空白のように見えても、実際には「タブ」で列が分かれています。  
Excel に取り込むときは、「区切り文字 = タブ」を選ぶと列が正しく分かれます。

## sample_values

実際のデータがどのような形かをつかむため、先頭付近の値を少しだけ抜き出します。

### TSJ_entries.tsv

sample_values:

SJID:
- s0104a601
- s0104a602
- s0104a603

Entry:
- 天
- 𬻃
- 𠀘

### TSJ_definitions.tsv

sample_values:

TSJ2ID:
- s0104a601
- s0104a602a
- s0104a701

Entry_word:
- 天
- 𬻃⿳一丷兀𠕹⿳一⿰从兀
- ⿸疒⿱龷天

### TSJ_wakun.tsv

sample_values:

tsj_id:
- s0104a705
- s0104a804
- s0104b102

entry_text:
- 鬵
- 昋
- 𠿓

### TSJ_ndl.tsv

sample_values:

SJ_vol_leaf:
- s0000a
- s0000b
- s0001a

SJ_Rinsen_p:
- 1
- 2
- 3

## Excel に持っていくときの入口

初心者には、次の順で進めるのがおすすめです。

1. `count_basic_stats.py` で行数・列数・空欄数を確認する
2. 必要なら `--export-clean-tsv` でコメント行を除いた TSV を作る
3. Excel でその TSV を開く
4. 区切り文字に `タブ` を指定する
5. 文字コードは `UTF-8` を意識する

## まとめ

TSJ の基本統計からは、次のことが分かります。

- `TSJ_entries.tsv` は見出し字の中心データ
- `TSJ_definitions.tsv` は定義本文を見るための表
- `TSJ_wakun.tsv` は和訓研究向けの専用表
- `TSJ_ndl.tsv` は画像参照のための対応表
- TSJ データは、目的別に分けて整備された使いやすい構成を持つ
- ただし `TSJ_entries.tsv` には少数の不規則行があるので、最初に構造確認するのが安全
