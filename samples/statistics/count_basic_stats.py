#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass
class TsvStructure:
    file_name: str
    comment_line_count: int
    blank_line_count: int
    header_line_number: int
    data_start_line_number: int
    row_count: int
    column_count: int
    column_names: list[str]
    non_empty_cell_counts: dict[str, int]
    empty_cell_counts: dict[str, int]
    irregular_row_count: int
    trailing_missing_column_count: int
    max_column_count_seen: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Count beginner-level statistics for an HDIC TSV file."
    )
    parser.add_argument(
        "input_tsv",
        nargs="?",
        default="TSJ_entries.tsv",
        help="Path to the input TSV file (default: TSJ_entries.tsv)",
    )
    parser.add_argument(
        "--level",
        "-l",
        default="beginner",
        choices=["beginner"],
        help="Statistics level to compute (currently only: beginner)",
    )
    parser.add_argument(
        "--format",
        choices=["text", "tsv", "json"],
        default="text",
        help="Output format (default: text)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Write the statistics report to this file instead of stdout",
    )
    parser.add_argument(
        "--export-clean-tsv",
        type=Path,
        help="Write a comment-free TSV for easy Excel import",
    )
    return parser.parse_args()


def read_tsv_structure(path: Path) -> tuple[TsvStructure, list[list[str]]]:
    comment_line_count = 0
    blank_line_count = 0
    header_line_number = 0
    data_start_line_number = 0
    irregular_row_count = 0
    trailing_missing_column_count = 0
    max_column_count_seen = 0
    header: list[str] | None = None
    data_rows: list[list[str]] = []

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle, delimiter="\t")
        for line_number, row in enumerate(reader, start=1):
            if not row or all(cell == "" for cell in row):
                blank_line_count += 1
                continue

            first_cell = row[0].lstrip("\ufeff")
            if first_cell.startswith("#"):
                if header is None:
                    comment_line_count += 1
                continue

            max_column_count_seen = max(max_column_count_seen, len(row))

            if header is None:
                header = row
                header_line_number = line_number
                data_start_line_number = line_number + 1
                continue

            if len(row) > len(header):
                irregular_row_count += 1
            elif len(row) < len(header):
                trailing_missing_column_count += 1

            data_rows.append(pad_row(row, len(header)))

    if header is None:
        raise SystemExit(f"No header row found in {path}")

    non_empty_cell_counts = {column_name: 0 for column_name in header}
    empty_cell_counts = {column_name: 0 for column_name in header}

    for row in data_rows:
        for column_name, cell in zip(header, row):
            if cell == "":
                empty_cell_counts[column_name] += 1
            else:
                non_empty_cell_counts[column_name] += 1

    structure = TsvStructure(
        file_name=str(path),
        comment_line_count=comment_line_count,
        blank_line_count=blank_line_count,
        header_line_number=header_line_number,
        data_start_line_number=data_start_line_number,
        row_count=len(data_rows),
        column_count=len(header),
        column_names=header,
        non_empty_cell_counts=non_empty_cell_counts,
        empty_cell_counts=empty_cell_counts,
        irregular_row_count=irregular_row_count,
        trailing_missing_column_count=trailing_missing_column_count,
        max_column_count_seen=max_column_count_seen,
    )
    return structure, data_rows


def pad_row(row: list[str], target_length: int) -> list[str]:
    if len(row) >= target_length:
        return row[:target_length]
    return row + [""] * (target_length - len(row))


def count_basic_stats(path: Path) -> tuple[TsvStructure, list[list[str]]]:
    return read_tsv_structure(path)


def render_text(stats: TsvStructure) -> str:
    lines = [
        f"file: {stats.file_name}",
        "level: beginner",
        f"comment_line_count: {stats.comment_line_count}",
        f"blank_line_count: {stats.blank_line_count}",
        f"header_line_number: {stats.header_line_number}",
        f"data_start_line_number: {stats.data_start_line_number}",
        f"row_count: {stats.row_count}",
        f"column_count: {stats.column_count}",
        f"irregular_row_count: {stats.irregular_row_count}",
        f"trailing_missing_column_count: {stats.trailing_missing_column_count}",
        f"max_column_count_seen: {stats.max_column_count_seen}",
        "",
        "column_names:",
    ]
    lines.extend(f"- {column_name}" for column_name in stats.column_names)
    lines.append("")
    lines.append("column_counts:")
    for column_name in stats.column_names:
        lines.append(
            f"- {column_name}: non_empty={stats.non_empty_cell_counts[column_name]}, "
            f"empty={stats.empty_cell_counts[column_name]}"
        )
    return "\n".join(lines)


def render_tsv(stats: TsvStructure) -> str:
    rows = [
        ["section", "key", "value"],
        ["summary", "file", stats.file_name],
        ["summary", "level", "beginner"],
        ["summary", "comment_line_count", str(stats.comment_line_count)],
        ["summary", "blank_line_count", str(stats.blank_line_count)],
        ["summary", "header_line_number", str(stats.header_line_number)],
        ["summary", "data_start_line_number", str(stats.data_start_line_number)],
        ["summary", "row_count", str(stats.row_count)],
        ["summary", "column_count", str(stats.column_count)],
        ["summary", "irregular_row_count", str(stats.irregular_row_count)],
        ["summary", "trailing_missing_column_count", str(stats.trailing_missing_column_count)],
        ["summary", "max_column_count_seen", str(stats.max_column_count_seen)],
    ]
    for index, column_name in enumerate(stats.column_names, start=1):
        rows.append(["column_name", str(index), column_name])
    for column_name in stats.column_names:
        rows.append(
            [
                "column_count",
                column_name,
                f"non_empty={stats.non_empty_cell_counts[column_name]};empty={stats.empty_cell_counts[column_name]}",
            ]
        )
    return "\n".join("\t".join(row) for row in rows)


def render_json(stats: TsvStructure) -> str:
    payload = {
        "file": stats.file_name,
        "level": "beginner",
        "comment_line_count": stats.comment_line_count,
        "blank_line_count": stats.blank_line_count,
        "header_line_number": stats.header_line_number,
        "data_start_line_number": stats.data_start_line_number,
        "row_count": stats.row_count,
        "column_count": stats.column_count,
        "column_names": stats.column_names,
        "non_empty_cell_counts": stats.non_empty_cell_counts,
        "empty_cell_counts": stats.empty_cell_counts,
        "irregular_row_count": stats.irregular_row_count,
        "trailing_missing_column_count": stats.trailing_missing_column_count,
        "max_column_count_seen": stats.max_column_count_seen,
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def export_clean_tsv(path: Path, header: list[str], data_rows: list[list[str]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(header)
        writer.writerows(data_rows)


def write_output(text: str, output_path: Path | None) -> None:
    if output_path is None:
        print(text)
        return
    output_path.write_text(text + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    input_path = Path(args.input_tsv)
    stats, data_rows = count_basic_stats(input_path)

    if args.export_clean_tsv is not None:
        export_clean_tsv(args.export_clean_tsv, stats.column_names, data_rows)

    if args.format == "text":
        report = render_text(stats)
    elif args.format == "tsv":
        report = render_tsv(stats)
    else:
        report = render_json(stats)

    write_output(report, args.output)


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
