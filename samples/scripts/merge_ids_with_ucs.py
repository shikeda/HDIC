#!/usr/bin/env python3
"""
IDS構成データを ids.tsv と突合し、対応するUCS文字を持つ行だけを抽出する。

各見出し字IDSファイル（例: syp_head_char_ids.tsv, ktb_head_char_ids.tsv,
tsj_head_char_ids.tsv, krm_head_char_ids.tsv）は、1列目にIDS構成表記
（例: ⿰亻胃）を持つ。ids.tsv 側は「UCSコード 文字 IDS構成」の3カラム
（空白区切り）で、IDS構成をキーにUCSコードと実字を引き当てる。

使い方:
  python3 merge_ids_with_ucs.py <head_char_ids.tsv> <ids.tsv> <output.tsv>

出力フォーマット: <IDS構成>\t<文字>
"""

import argparse
import os


def merge_ids(head_char_ids_file: str, ids_file: str, output_file: str) -> None:
    # ids.tsv のデータを格納する辞書 { 3列目の構成データ: (1列目のUCS, 2列目の文字) }
    ids_dict: dict[str, tuple[str, str]] = {}

    if not os.path.exists(ids_file):
        print(f"エラー: {ids_file} が見つかりません。")
        return

    with open(ids_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # コメント行や空行をスキップ
            if not line or line.startswith("#"):
                continue

            # タブまたはスペース区切りに対応（念のためsplit()を使用）
            parts = line.split()
            # 少なくとも「コード、文字、構成」の3つの要素があるか確認
            if len(parts) >= 3:
                ucs_code = parts[0]
                char = parts[1]
                # 3列目以降が構成データ（スペースが含まれる場合を考慮して結合）
                structure = "".join(parts[2:])
                ids_dict[structure] = (ucs_code, char)

    if not os.path.exists(head_char_ids_file):
        print(f"エラー: {head_char_ids_file} が見つかりません。")
        return

    match_count = 0
    with open(head_char_ids_file, "r", encoding="utf-8") as f_in, open(
        output_file, "w", encoding="utf-8"
    ) as f_out:
        for line in f_in:
            line = line.strip()
            if not line:
                continue

            # 1列目（構成データ）を取得
            structure = line.split("\t")[0].strip()

            # ids.tsv の3列目と照合
            if structure in ids_dict:
                _ucs_code, char = ids_dict[structure]
                f_out.write(f"{structure}\t{char}\n")
                match_count += 1

    print(f"処理が完了しました。{match_count} 件のマッチを {output_file} に出力しました。")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("head_char_ids_file", help="見出し字IDS構成データ（例: ktb_head_char_ids.tsv）")
    parser.add_argument("ids_file", help="UCSコード対応表（例: ids.tsv）")
    parser.add_argument("output_file", help="出力先TSVファイル")
    args = parser.parse_args()

    merge_ids(args.head_char_ids_file, args.ids_file, args.output_file)


if __name__ == "__main__":
    main()
