#!/usr/bin/env python3
"""Fail on file types and credential patterns that do not belong in the public kit."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BLOCKED_SUFFIXES = {
    ".csv", ".tsv", ".xlsx", ".xls", ".pdf", ".doc", ".docx",
    ".db", ".sqlite", ".sqlite3", ".log", ".zip", ".tar", ".gz",
    ".png", ".jpg", ".jpeg", ".webp",
}
BLOCKED_NAMES = {".env", "id_rsa", "id_ed25519"}
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "Anthropic key": re.compile(r"sk-ant-[A-Za-z0-9_-]{16,}"),
    "GitHub token": re.compile(r"gh[oprsu]_[A-Za-z0-9]{20,}"),
    "Google API key": re.compile(r"AIza[0-9A-Za-z_-]{20,}"),
}


def repository_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, text=True, capture_output=True, check=False
    )
    if result.returncode == 0:
        return [ROOT / line for line in result.stdout.splitlines() if line]
    return [path for path in ROOT.rglob("*") if path.is_file() and ".git" not in path.parts]


def main() -> int:
    files = repository_files()
    problems: list[str] = []
    for path in files:
        relative = path.relative_to(ROOT)
        if path.name in BLOCKED_NAMES or path.suffix.lower() in BLOCKED_SUFFIXES:
            problems.append(f"blocked file: {relative}")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            problems.append(f"unexpected binary file: {relative}")
            continue
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                problems.append(f"{label} pattern: {relative}")

    if problems:
        print("Public-repository check failed:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print(f"Public-repository check passed for {len(files)} files.")
    print("A human review for names and career details is still required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
