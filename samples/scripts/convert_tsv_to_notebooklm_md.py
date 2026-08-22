#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
work/bunruigoi_classical.tsv（日本古典対照分類語彙表）・
work/bunruigoi_modern.tsv（bunruidb-fam、現代語）を、
LLM/NotebookLM等での検索・詳細抽出向けにエントリ単位のMarkdownへ変換する。

各ファイルは`見出し`の五十音の行（あ行・か行…）ごとに分割して出力する。
分割理由: 現代語ファイルは101,067件・全件出力で約27MBに達し、単一ファイルでは
NotebookLM等の1ソースあたりの上限を超えうるため。また検索・詳細抽出の観点でも、
関連する範囲だけを読み込める方が効率的。
"""

import csv
from pathlib import Path

# パス設定（スクリプト位置を基準に work ディレクトリを参照）
SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent.parent  # プロジェクトルート
WORK_DIR = BASE_DIR / "work"

# 五十音の行分け。小書き・濁音・半濁音は対応する清音の行に含める。
GOJUON_ROWS: dict[str, str] = {}
for row_name, chars in {
    "あ": "あいうえおぁぃぅぇぉ",
    "か": "かきくけこがぎぐげご",
    "さ": "さしすせそざじずぜぞ",
    "た": "たちつてとだぢづでどっ",
    "な": "なにぬねの",
    "は": "はひふへほばびぶべぼぱぴぷぺぽ",
    "ま": "まみむめも",
    "や": "やゆよゃゅょ",
    "ら": "らりるれろ",
    "わ": "わをん",
}.items():
    for c in chars:
        GOJUON_ROWS[c] = row_name

ROW_ORDER = ["あ", "か", "さ", "た", "な", "は", "ま", "や", "ら", "わ", "other"]

# 行の中をさらに個々のカナ（清音の列）単位で分けるためのマップ。
# 濁音・半濁音は対応する清音の列にまとめる（例: が→か列）。
KANA_COLUMNS: dict[str, str] = {}
for col_name, chars in {
    "あ": "あぁ", "い": "いぃ", "う": "うぅ", "え": "えぇ", "お": "おぉ",
    "か": "かが", "き": "きぎ", "く": "くぐ", "け": "けげ", "こ": "こご",
    "さ": "さざ", "し": "しじ", "す": "すず", "せ": "せぜ", "そ": "そぞ",
    "た": "た", "ち": "ち", "つ": "つっ", "て": "て", "と": "と",
    "だ": "だ", "ぢ": "ぢ", "づ": "づ", "で": "で", "ど": "ど",
    "な": "な", "に": "に", "ぬ": "ぬ", "ね": "ね", "の": "の",
    "は": "はばぱ", "ひ": "ひびぴ", "ふ": "ふぶぷ", "へ": "へべぺ", "ほ": "ほぼぽ",
    "ま": "ま", "み": "み", "む": "む", "め": "め", "も": "も",
    "や": "やゃ", "ゆ": "ゆゅ", "よ": "よょ",
    "ら": "ら", "り": "り", "る": "る", "れ": "れ", "ろ": "ろ",
    "わ": "わ", "を": "を", "ん": "ん",
}.items():
    for c in chars:
        KANA_COLUMNS[c] = col_name

# 個々の列を行にまとめる順序（サブ分割時のファイル出力順に使う）。
ROW_TO_COLUMNS = {
    "あ": ["あ", "い", "う", "え", "お"],
    "か": ["か", "き", "く", "け", "こ"],
    "さ": ["さ", "し", "す", "せ", "そ"],
    "た": ["た", "ち", "つ", "て", "と", "だ", "ぢ", "づ", "で", "ど"],
    "な": ["な", "に", "ぬ", "ね", "の"],
    "は": ["は", "ひ", "ふ", "へ", "ほ"],
    "ま": ["ま", "み", "む", "め", "も"],
    "や": ["や", "ゆ", "よ"],
    "ら": ["ら", "り", "る", "れ", "ろ"],
    "わ": ["わ", "を", "ん"],
}


def to_hiragana(text: str) -> str:
    return "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in text)


def gojuon_column(heading: str) -> str:
    """見出しの先頭文字から個々のカナの列（清音）を判定する。判定できなければ 'other'。"""
    if not heading:
        return "other"
    first = to_hiragana(heading)[0]
    return KANA_COLUMNS.get(first, "other")


def gojuon_row(heading: str) -> str:
    """見出しの先頭文字から五十音の行を判定する。判定できなければ 'other'。"""
    if not heading:
        return "other"
    first = to_hiragana(heading)[0]
    return GOJUON_ROWS.get(first, "other")


def is_valid_val(val: str | None) -> bool:
    """空文字や #N/A などの不要な値を除外判定"""
    if val is None:
        return False
    v = val.strip()
    return v != "" and v.upper() != "#N/A"


def build_classical_entry(row: dict) -> str:
    heading = row.get("見出し", "").strip()
    lines = [f"### {heading}"]
    field_map = [
        ("漢字", "漢字表記"),
        ("仮名（漢字）", "仮名（漢字）"),
        ("id", "ID"),
        ("語種", "語種"),
        ("品詞", "品詞"),
        ("意味分類", "意味分類"),
        ("分類", "分類"),
        ("注記", "注記"),
        ("作品", "作品"),
        ("合計", "出現合計"),
    ]
    for key, label in field_map:
        val = row.get(key)
        if is_valid_val(val):
            lines.append(f"- **{label}**: {val.strip()}")
    return "\n".join(lines)


def build_modern_entry(row: dict) -> str:
    heading = row.get("見出し", "").strip()
    lines = [f"### {heading}"]

    if is_valid_val(row.get("見出し本体")):
        lines.append(f"- **見出し本体**: {row['見出し本体'].strip()}")
    if is_valid_val(row.get("読み")):
        lines.append(f"- **読み**: {row['読み'].strip()}")
    if is_valid_val(row.get("レコード種別")):
        lines.append(f"- **レコード種別**: {row['レコード種別'].strip()}")

    # 階層分類（類 > 部門 > 中項目 > 分類項目）をまとめて分かりやすく構成
    hierarchies = []
    for key in ["類", "部門", "中項目", "分類項目"]:
        val = row.get(key)
        if is_valid_val(val):
            hierarchies.append(f"{key}:{val.strip()}")
    if hierarchies:
        lines.append(f"- **階層分類**: {' / '.join(hierarchies)}")

    # 分類番号・段落詳細
    cat_num = (row.get("分類番号") or "").strip()
    details = []
    if is_valid_val(row.get("段落番号")):
        details.append(f"段落:{row['段落番号'].strip()}")
    if is_valid_val(row.get("小段落番号")):
        details.append(f"小段落:{row['小段落番号'].strip()}")
    if is_valid_val(row.get("語番号")):
        details.append(f"語番号:{row['語番号'].strip()}")
    if is_valid_val(cat_num):
        detail_str = f" （{' / '.join(details)}）" if details else ""
        lines.append(f"- **分類番号**: {cat_num}{detail_str}")

    return "\n".join(lines)


def convert(
    tsv_path: Path,
    output_stem: Path,
    title: str,
    build_entry,
    sort_key_field: str,
    fine_split_rows: frozenset[str] = frozenset(),
) -> None:
    """TSVを読み、`sort_key_field`列（常にカナである列）の五十音行ごとにエントリを分けてMarkdownを出力する。

    `見出し`列は漢字始まり（例: modern側の「者（もの）」）のことがあり、五十音判定には
    使えないため、判定用の列を呼び出し側で指定できるようにしている
    （classical側は`見出し`自体がカナなのでそれを使う、modern側は`読み`を使う）。

    `fine_split_rows` に含めた行（例: {"か", "さ"}）は、行単位ではなくさらに個々の
    カナの列単位（か→か・き・く・け・こ）でファイルを分ける。ファイルサイズが
    大きくなりすぎる行（NotebookLM等の1ソース上限を超える）だけを個別に指定する想定。
    """
    if not tsv_path.exists():
        print(f"[スキップ] ファイルが見つかりません: {tsv_path}")
        return

    print(f"変換中: {tsv_path.name} -> {output_stem.name}_<行>.md")
    entries_by_row: dict[str, list[str]] = {row_name: [] for row_name in ROW_ORDER}
    entries_by_column: dict[str, list[str]] = {}

    with open(tsv_path, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            heading = (row.get("見出し") or "").strip()
            if not heading:
                continue
            sort_key = (row.get(sort_key_field) or heading).strip()
            row_name = gojuon_row(sort_key)
            entry = build_entry(row)
            if row_name in fine_split_rows:
                col = gojuon_column(sort_key)
                entries_by_column.setdefault(col, []).append(entry)
            else:
                entries_by_row[row_name].append(entry)

    def write_file(suffix: str, label: str, entries: list[str]) -> None:
        output_path = output_stem.parent / f"{output_stem.name}_{suffix}.md"
        with open(output_path, mode="w", encoding="utf-8") as f:
            f.write(f"# {title}（{label}）\n\n")
            f.write(f"{len(entries)}件\n\n")
            f.write("\n\n---\n\n".join(entries))
            f.write("\n")
        print(f"  {output_path.name}: {len(entries)} 件")

    total = 0
    for row_name in ROW_ORDER:
        if row_name in fine_split_rows:
            for col in ROW_TO_COLUMNS.get(row_name, [row_name]):
                entries = entries_by_column.get(col, [])
                if not entries:
                    continue
                write_file(col, f"{row_name}行 / {col}列", entries)
                total += len(entries)
            continue
        entries = entries_by_row[row_name]
        if not entries:
            continue
        write_file(row_name, f"{row_name}行", entries)
        total += len(entries)

    print(f"完了: 合計 {total} 件のエントリを出力しました。")


def main() -> None:
    WORK_DIR.mkdir(parents=True, exist_ok=True)

    convert(
        tsv_path=WORK_DIR / "bunruigoi_modern.tsv",
        output_stem=WORK_DIR / "bunruigoi_modern",
        title="分類語彙表（現代語）",
        build_entry=build_modern_entry,
        sort_key_field="読み",
        # か行・さ行はファイルサイズが大きく（約5.5MB）NotebookLM等の1ソース上限に
        # 抵触しうるため、個々のカナ単位（か・き・く・け・こ / さ・し・す・せ・そ）に
        # さらに分割する。た行（約3.9MB）は分割不要と確認済み（NotebookLMで読込確認）。
        fine_split_rows=frozenset({"か", "さ"}),
    )

    convert(
        tsv_path=WORK_DIR / "bunruigoi_classical.tsv",
        output_stem=WORK_DIR / "bunruigoi_classical",
        title="分類語彙表（古典語）",
        build_entry=build_classical_entry,
        sort_key_field="見出し",
    )


if __name__ == "__main__":
    main()
