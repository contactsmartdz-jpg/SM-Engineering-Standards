#!/usr/bin/env python3
"""Validate required standard documents and relative Markdown links.

No external dependencies are needed. External hyperlinks and fragment anchors
are not checked because network/heading verification is a separate concern.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "governance/POLICY.md",
    "governance/DEFINITION_OF_READY.md",
    "governance/DEFINITION_OF_DONE.md",
    "quality-gates/QUALITY_GATES.md",
    "ai-agents/AGENT_RULES.md",
]
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SKIP_DIRS = {".git", "node_modules", ".venv", "venv"}
errors: list[str] = []

for relative in REQUIRED:
    if not (ROOT / relative).is_file():
        errors.append(f"Missing required file: {relative}")

documents = [
    path
    for path in ROOT.rglob("*.md")
    if not any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts)
]
for document in sorted(documents):
    for number, line in enumerate(document.read_text(encoding="utf-8").splitlines(), 1):
        for match in LINK_PATTERN.finditer(line):
            link = match.group(1).split(" ", 1)[0].strip("<>")
            if link.startswith("#"):
                continue
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            path_part = unquote(parsed.path)
            if not path_part:
                continue
            target = (document.parent / path_part).resolve()
            if not target.is_relative_to(ROOT):
                errors.append(f"{document.relative_to(ROOT)}:{number} points outside repo: {link}")
            elif not target.exists():
                errors.append(f"{document.relative_to(ROOT)}:{number} missing link: {link}")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)

print(f"Validated {len(documents)} Markdown documents and required paths.")
