#!/usr/bin/env python3
"""
IDS表記をUnicode文字に変換するスクリプト。

使い方:
  # 単一ファイルを変換して標準出力へ
  python3 replace_ids_with_ucs.py <input.tsv> --mapping <mapping.tsv>

  # 単一ファイルを変換して出力先ファイルへ
  python3 replace_ids_with_ucs.py <input.tsv> --mapping <mapping.tsv> -o <output.tsv>

  # フォルダ内の全TSVを変換（出力先フォルダへ）
  python3 replace_ids_with_ucs.py <input_dir/> --mapping <mapping.tsv> -d <output_dir/>

  # 変換対象のIDS一覧を確認するだけ（ドライラン）
  python3 replace_ids_with_ucs.py <input.tsv> --mapping <mapping.tsv> --dry-run

マッピングファイルは対象の辞書ごとに異なる（例: ktb_head_char_ids_with_ucs_matched.tsv,
tsj_head_char_ids_with_ucs_matched.tsv, krm_head_char_ids_with_ucs_matched.tsv）ため、
--mapping で明示的に指定する。辞書を取り違えると誤変換になるため、デフォルト値は持たせない。
"""

import argparse
import sys
from pathlib import Path


def load_mapping(mapping_path: Path) -> dict[str, str]:
    """IDS → Unicode文字のマッピングを読み込む。長いパターンを先にマッチさせるため降順ソート済み辞書を返す。"""
    mapping = {}
    with mapping_path.open(encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line or line.startswith("#") or line.startswith("ids\t"):
                continue
            parts = line.split("\t")
            if len(parts) >= 2:
                ids, kanji = parts[0], parts[1]
                if ids and kanji:
                    mapping[ids] = kanji
    # 長いパターンを先に置換して部分マッチを防ぐ
    return dict(sorted(mapping.items(), key=lambda x: len(x[0]), reverse=True))


def replace_ids_in_text(text: str, mapping: dict[str, str]) -> str:
    for ids, kanji in mapping.items():
        text = text.replace(ids, kanji)
    return text


def process_file(input_path: Path, mapping: dict[str, str], output_path: Path | None = None, dry_run: bool = False) -> int:
    """ファイルを処理して置換件数を返す。"""
    content = input_path.read_text(encoding="utf-8")
    replaced = replace_ids_in_text(content, mapping)
    count = sum(content.count(ids) for ids in mapping if ids in content)

    if dry_run:
        found = [(ids, kanji) for ids, kanji in mapping.items() if ids in content]
        print(f"[{input_path.name}] {len(found)} 種のIDS、計 {count} 箇所")
        for ids, kanji in found:
            n = content.count(ids)
            print(f"  {ids} → {kanji}  ({n}箇所)")
        return count

    if output_path is None:
        sys.stdout.write(replaced)
    else:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(replaced, encoding="utf-8")
        print(f"[{input_path.name}] {count} 箇所を置換 → {output_path}")

    return count


def main():
    parser = argparse.ArgumentParser(
        description="IDS表記（⿰亻胃 など）をUnicode文字に変換する",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("input", help="入力ファイルまたはフォルダ")
    parser.add_argument("-o", "--output", help="出力ファイル（単一ファイル処理時）")
    parser.add_argument("-d", "--output-dir", help="出力フォルダ（フォルダ処理時）")
    parser.add_argument("--mapping", required=True, help="マッピングTSVファイル（対象の辞書に対応するものを指定）")
    parser.add_argument("--dry-run", action="store_true", help="置換せず、対象IDS一覧を表示するだけ")
    args = parser.parse_args()

    mapping_path = Path(args.mapping)
    if not mapping_path.exists():
        print(f"エラー: マッピングファイルが見つかりません: {mapping_path}", file=sys.stderr)
        sys.exit(1)

    mapping = load_mapping(mapping_path)
    print(f"マッピング読み込み: {len(mapping)} 件 ({mapping_path.name})", file=sys.stderr)

    input_path = Path(args.input)

    if input_path.is_dir():
        tsv_files = sorted(input_path.glob("*.tsv"))
        if not tsv_files:
            print(f"エラー: {input_path} にTSVファイルが見つかりません", file=sys.stderr)
            sys.exit(1)
        output_dir = Path(args.output_dir) if args.output_dir else None
        if output_dir is None and not args.dry_run:
            print("エラー: フォルダ処理時は -d <output_dir> を指定してください", file=sys.stderr)
            sys.exit(1)
        total = 0
        for tsv in tsv_files:
            out = (output_dir / tsv.name) if output_dir else None
            total += process_file(tsv, mapping, out, args.dry_run)
        print(f"\n合計 {total} 箇所を処理", file=sys.stderr)

    elif input_path.is_file():
        output_path = Path(args.output) if args.output else None
        process_file(input_path, mapping, output_path, args.dry_run)

    else:
        print(f"エラー: {input_path} が見つかりません", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
