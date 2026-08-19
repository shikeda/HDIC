#!/usr/bin/env python3
"""
HDICのルート直下TSVについて、クロスファイルの相互参照（FK）整合性と
主キーの重複を検証する（読み取り専用、データは一切変更しない）。

count_basic_stats.py は単一ファイルの構造（列数・空欄など）を検証するが、
「参照先のIDが実在するか」はチェックしない。本スクリプトはその隙間を埋める。

検証対象と関係（2026-08時点で確認済みのもの。KRM系ファイルは対象外 —
README.md の記載どおり、KRMデータの更新は github.com/shikeda/krm 側の
krm_*.tsv/.json に一本化されており、HDIC側の KRM.tsv 等は凍結されている）:

  主キー:
    TSJ_entries.tsv       SJID
    TSJ_entries.tsv       SJ2ID  (複数SJIDが1つのSJ2IDを共有しうる。ユニーク
                                   性はTSJ_definitions.tsvからの参照先としてのみ検証)
    TSJ_definitions.tsv   TSJ2ID
    KTB.tsv                TBID
    SYP.tsv                 SYID
    YYP.tsv                 YYID

  相互参照 (source.column -> target.column):
    TSJ_entries.tsv.TBID     -> KTB.tsv.TBID
    TSJ_entries.tsv.SYID     -> SYP.tsv.SYID
    TSJ_definitions.tsv.TSJ2ID -> TSJ_entries.tsv.SJ2ID
    KTB.tsv.SYID              -> SYP.tsv.SYID
    KTB.tsv.YYID              -> YYP.tsv.YYID
    YYP.tsv.TBID              -> KTB.tsv.TBID
    YYP.tsv.SYID              -> SYP.tsv.SYID

IDの表記ゆれ（TBIDには "-Shirafuji" のような校閲者注記サフィックスが付く場合が
あるなど）が実際に存在するため、ID書式の正規表現チェックは行わない。あくまで
「参照先に同じ文字列のキーが存在するか」だけを見る、緩い（false positiveを
出しにくい）検証にとどめる。

参照値の正規化ルール（いずれも実データで根拠を確認済み。詳細は
normalize_reference() のdocstring、および samples/logs/ の関連ログを参照）:
  - "0" は「対応なし」のプレースホルダとして丸ごとスキップする。
  - "△"/"▽" 単独は「対応なし」。YYP.tsvのヘッダーコメント（SYID列の説明）に
    「`△` indicates no direct correspondence was assigned」と明記されている。
  - "△(id)"/"▽(id)" は「直接対応ではないが候補IDを括弧内に注記した」もの。
    括弧を外側だけ剥がすのではなく、括弧内のIDを抽出して実在チェックの対象と
    する（丸ごとスキップしない）。括弧内が実在するIDであることは、KTB.tsvの
    複数件（1_029_A21 の △(a011b082) など）でSYP.tsvに実在することを確認済み。
  - 数字を含まない値（例: "(前項)"「直前の項目と同一」の意）はIDではないので
    丸ごとスキップする。前後の行の実際の値と突き合わせて意味を確認済み。
  - 末尾の "*" は「暫定的な同定」を示す注記接尾辞なので、削って本体のIDだけを
    照合する（括弧内の値についても同様）。

注意: "△(II68ウ5)" のような、宮澤俊雅『掲出字一覽表』（KTB.tsvヘッダーに
文献情報あり）の丁付け引用（ローマ数字+丁+オ/ウ）をそのまま転記したケースが
過去に存在したが、これはSYP.tsvのIDではなく別文献への参照であり、本来は
確定済みのSYP ID（判明していれば）に置き換えるべきもの。2026-08-19時点で
判明していた1件（KTB.tsv 2_073_B51 の𦝨）は △(a070b061) に修正済み。今後
同様の値が見つかった場合は、括弧内が実在ID形式でなければ本スクリプトは
「参照切れ」として報告するので、宮澤氏の一覧表を参照して確定IDに置き換える
（このスクリプト自身では判定できない）。

使い方:
  python3 samples/scripts/validate_hdic_integrity.py
  python3 samples/scripts/validate_hdic_integrity.py --format json

終了コード:
  0 - 問題なし
  1 - 重複キーまたは参照切れあり
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent

PLACEHOLDER_EXACT = {"0"}
ANNOTATED_CANDIDATE_RE = re.compile(r"^[△▽]\((.+)\)$")


def _strip_trailing_star(value: str) -> str:
    return value[:-1] if value.endswith("*") else value


def normalize_reference(value: str) -> str | None:
    """
    参照値を正規化する。実在チェック可能なIDに正規化できればそれを返し、
    プレースホルダ・純粋な注記（IDを含まない）なら None（=検証対象外）を返す。

    モジュールdocstringの「参照値の正規化ルール」を参照。
    """
    value = _strip_trailing_star(value)
    if value == "0":
        return None
    m = ANNOTATED_CANDIDATE_RE.match(value)
    if m:
        value = _strip_trailing_star(m.group(1))
    elif value in ("△", "▽"):
        return None
    return value if re.search(r"[0-9]", value) else None

PRIMARY_KEYS = {
    "TSJ_entries.tsv": ["SJID"],
    "TSJ_definitions.tsv": ["TSJ2ID"],
    "KTB.tsv": ["TBID"],
    "SYP.tsv": ["SYID"],
    "YYP.tsv": ["YYID"],
}

# (source_file, source_column, target_file, target_column)
FK_RELATIONS = [
    ("TSJ_entries.tsv", "TBID", "KTB.tsv", "TBID"),
    ("TSJ_entries.tsv", "SYID", "SYP.tsv", "SYID"),
    ("TSJ_definitions.tsv", "TSJ2ID", "TSJ_entries.tsv", "SJ2ID"),
    ("KTB.tsv", "SYID", "SYP.tsv", "SYID"),
    ("KTB.tsv", "YYID", "YYP.tsv", "YYID"),
    ("YYP.tsv", "TBID", "KTB.tsv", "TBID"),
    ("YYP.tsv", "SYID", "SYP.tsv", "SYID"),
]


def read_rows(path: Path) -> tuple[list[str], list[list[str]]]:
    header: list[str] | None = None
    rows: list[list[str]] = []
    with path.open(encoding="utf-8-sig", newline="") as f:
        for row in csv.reader(f, delimiter="\t"):
            if not row or all(cell == "" for cell in row):
                continue
            if row[0].lstrip("﻿").startswith("#"):
                continue
            if header is None:
                header = row
                continue
            rows.append(row)
    if header is None:
        raise SystemExit(f"No header row found in {path}")
    return header, rows


def column_values(header: list[str], rows: list[list[str]], column: str) -> list[str]:
    idx = header.index(column)
    return [row[idx] for row in rows if idx < len(row) and row[idx]]


def check_duplicates(cache: dict[str, tuple[list[str], list[list[str]]]]) -> list[dict]:
    findings = []
    for fname, columns in PRIMARY_KEYS.items():
        header, rows = cache[fname]
        for column in columns:
            if column not in header:
                continue
            values = column_values(header, rows, column)
            counts = Counter(values)
            dups = sorted(k for k, v in counts.items() if v > 1)
            if dups:
                findings.append(
                    {
                        "type": "duplicate_key",
                        "file": fname,
                        "column": column,
                        "count": len(dups),
                        "examples": dups[:10],
                    }
                )
    return findings


def check_fk_relations(cache: dict[str, tuple[list[str], list[list[str]]]]) -> list[dict]:
    findings = []
    for src_file, src_col, tgt_file, tgt_col in FK_RELATIONS:
        src_header, src_rows = cache[src_file]
        tgt_header, tgt_rows = cache[tgt_file]
        if src_col not in src_header or tgt_col not in tgt_header:
            continue
        target_keys = set(column_values(tgt_header, tgt_rows, tgt_col))
        source_values = column_values(src_header, src_rows, src_col)
        normalized = (normalize_reference(v) for v in source_values)
        missing = sorted({v for v in normalized if v is not None and v not in target_keys})
        if missing:
            findings.append(
                {
                    "type": "broken_reference",
                    "file": src_file,
                    "column": src_col,
                    "target": f"{tgt_file}.{tgt_col}",
                    "count": len(missing),
                    "examples": missing[:10],
                }
            )
    return findings


def render_text(findings: list[dict], files_checked: list[str]) -> str:
    lines = [
        "HDIC integrity check",
        f"files_checked: {', '.join(files_checked)}",
        f"finding_count: {len(findings)}",
        "",
    ]
    if not findings:
        lines.append("No duplicate keys or broken references found.")
        return "\n".join(lines)
    for f in findings:
        if f["type"] == "duplicate_key":
            lines.append(f"[duplicate_key] {f['file']}.{f['column']}: {f['count']} duplicated value(s)")
        else:
            lines.append(
                f"[broken_reference] {f['file']}.{f['column']} -> {f['target']}: "
                f"{f['count']} value(s) not found"
            )
        for ex in f["examples"]:
            lines.append(f"  - {ex}")
    return "\n".join(lines)


def render_json(findings: list[dict], files_checked: list[str]) -> str:
    return json.dumps(
        {"files_checked": files_checked, "finding_count": len(findings), "findings": findings},
        ensure_ascii=False,
        indent=2,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--output", type=Path, help="Write the report to this file instead of stdout")
    args = parser.parse_args()

    needed_files = sorted(set(PRIMARY_KEYS) | {f for rel in FK_RELATIONS for f in (rel[0], rel[2])})
    cache: dict[str, tuple[list[str], list[list[str]]]] = {}
    for fname in needed_files:
        path = REPO_ROOT / fname
        if not path.exists():
            raise SystemExit(f"Required file not found: {fname}")
        cache[fname] = read_rows(path)

    findings = check_duplicates(cache) + check_fk_relations(cache)

    report = render_json(findings, needed_files) if args.format == "json" else render_text(findings, needed_files)
    if args.output is None:
        print(report)
    else:
        args.output.write_text(report + "\n", encoding="utf-8")

    sys.exit(1 if findings else 0)


if __name__ == "__main__":
    main()
