# krm_wakun.tsv の japan_knowledge_id 設定（サカリ系 wakun 7件）

## 概要

別リポジトリ `github.com/shikeda/krm` の `krm_wakun.tsv` について、サカリ系の和訓7件に `japan_knowledge_id` を設定した。修正は2026-10-20に実施し、`krm` 側のコミット `d2fb7b6` に含まれる。HDIC 側の KRM は凍結中のため、編集先は `/home/ikeda/Hdic_data/krm` である。

## 検出方法

データ作成者（池田氏）からの直接の依頼による。スクリプトによる自動検出ではない。

## 問題

次の7件の `japan_knowledge_id` が空欄だった。

| wakun_id | hanzi_entry | wakun_elements |
|---|---|---|
| F08919_05 | 榮 | サカリナリ（HHH__） |
| F11172_03 | 燻／熏／熏 | サカリナリ |
| F11205_03 | 熾 | サカリナリ |
| F12793_02 | 状 | サカリナリ |
| F17534_08 | 慴 | サカリナリ |
| F23781_02 | 蓁／蓁 | サカリナリ |
| F11168_03 | 㶼 | サカリニ |

## 修正内容

### krm_wakun.tsv

- 上の7件の `japan_knowledge_id` を、いずれも `200201b67bfcT81pKcWz` に設定した。
- F11168_03 は行末の空欄が省略されていた（9列）ため、タブを補って10列にそろえた。
- 値はユーザー指定のとおりである。JapanKnowledge 側での照合は、この作業では行っていない。

### 付随する更新

- `finalize_krm_edit.py` を実行し、`krm_wakun.tsv` の Version を 1.2.26 から 1.2.27 に、Last update を October 20, 2026 に更新した。
- `krm_wakun.json` を再生成した（TSV が正本で、JSON は生成物）。

## 結果

- `count_basic_stats.py krm_wakun.tsv`: `irregular_row_count` は 0、`max_column_count_seen` は 10 で `column_count` と一致した。
- 変更ファイルは `krm_wakun.tsv` と `krm_wakun.json` の2つで、コミットは `d2fb7b6` である。
