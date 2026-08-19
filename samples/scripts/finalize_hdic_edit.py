#!/usr/bin/env python3
"""
HDICのルート直下TSV/TXTを編集した後の後始末を行う。

- 変更対象ファイルは `git diff --name-only HEAD` から自動検出する
  （引数でファイルを明示指定することも可能）。
- 各ファイルのヘッダーコメントにある `Version:` を、git HEAD時点の値を基準に
  patchを+1して書き換える（複数回実行しても、コミットするまでは同じ結果に
  収束する＝二重加算しない）。
- `Last update` / `Last modified`（ファイルによってラベルが異なる）を実行日
  （ISO 8601, YYYY-MM-DD）に更新する。
- ヘッダー以外の行（データ行）は一切変更しない。データ行の編集は Edit ツール
  等で先に済ませておくこと。

使い方:
  python3 samples/scripts/finalize_hdic_edit.py               # git diffから自動検出
  python3 samples/scripts/finalize_hdic_edit.py FILE1 FILE2    # 対象ファイルを明示指定
  python3 samples/scripts/finalize_hdic_edit.py --dry-run       # 書き換えず変更内容を表示のみ
"""

from __future__ import annotations

import argparse
import datetime
import re
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent

VERSION_RE = re.compile(r"^(#[ \t]*)(Version)([ \t]*:[ \t]*)(\d+)\.(\d+)\.(\d+)\s*$")
LAST_UPDATE_RE = re.compile(r"^(#[ \t]*)(Last update|Last modified)([ \t]*:[ \t]*)(\d{4}-\d{2}-\d{2})\s*$")


def run_git(args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, check=True
    )
    return result.stdout


def detect_changed_files() -> list[str]:
    output = run_git(["diff", "--name-only", "HEAD"])
    candidates = [line.strip() for line in output.splitlines() if line.strip()]
    return [f for f in candidates if f.endswith((".tsv", ".txt")) and "/" not in f]


def read_head_version(rel_path: str) -> tuple[int, int, int] | None:
    try:
        content = run_git(["show", f"HEAD:{rel_path}"])
    except subprocess.CalledProcessError:
        return None
    for line in content.splitlines():
        m = VERSION_RE.match(line)
        if m:
            return int(m.group(4)), int(m.group(5)), int(m.group(6))
    return None


def finalize_file(rel_path: str, dry_run: bool) -> bool:
    path = REPO_ROOT / rel_path
    if not path.exists():
        print(f"スキップ: {rel_path} が見つかりません", file=sys.stderr)
        return False

    head_version = read_head_version(rel_path)
    if head_version is None:
        print(f"スキップ: {rel_path} にVersionヘッダーが見つかりません（HEAD時点）", file=sys.stderr)
        return False
    major, minor, patch = head_version
    new_version = f"{major}.{minor}.{patch + 1}"
    today = datetime.date.today().isoformat()

    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    version_updated = False
    date_updated = False
    changes: list[str] = []

    for i, line in enumerate(lines):
        stripped = line[:-1] if line.endswith("\n") else line
        m = VERSION_RE.match(stripped)
        if m:
            new_line = f"{m.group(1)}{m.group(2)}{m.group(3)}{new_version}\n"
            if stripped != new_line.rstrip("\n"):
                changes.append(f"  Version: {m.group(4)}.{m.group(5)}.{m.group(6)} -> {new_version}")
                lines[i] = new_line
            version_updated = True
            continue
        m = LAST_UPDATE_RE.match(stripped)
        if m:
            new_line = f"{m.group(1)}{m.group(2)}{m.group(3)}{today}\n"
            if stripped != new_line.rstrip("\n"):
                changes.append(f"  {m.group(2)}: {m.group(4)} -> {today}")
                lines[i] = new_line
            date_updated = True
            continue

    if not version_updated:
        print(f"警告: {rel_path} でVersion行を書き換えられませんでした", file=sys.stderr)
    if not date_updated:
        print(f"警告: {rel_path} でLast update/Last modified行を書き換えられませんでした", file=sys.stderr)

    if not changes:
        print(f"[{rel_path}] 変更なし（既に最新の状態です）")
        return True

    print(f"[{rel_path}]")
    for c in changes:
        print(c)

    if not dry_run:
        path.write_text("".join(lines), encoding="utf-8")

    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("files", nargs="*", help="対象ファイル（省略時は git diff から自動検出）")
    parser.add_argument("--dry-run", action="store_true", help="書き換えず、変更内容の表示のみ行う")
    args = parser.parse_args()

    target_files = args.files if args.files else detect_changed_files()
    if not target_files:
        print("対象ファイルがありません（git diff --name-only HEAD で検出されたTSV/TXTなし）")
        return

    ok = True
    for rel_path in target_files:
        if not finalize_file(rel_path, args.dry_run):
            ok = False

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
