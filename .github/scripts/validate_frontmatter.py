"""Validate YAML frontmatter in vault markdown notes.

Used by the auto-approve PR workflow to enforce the rigid contract for
each note type. See docs/superpowers/specs/2026-04-09-finance-knowledge-pipeline-design.md
section 4 for the schema.

Usage:
    python validate_frontmatter.py <file1.md> <file2.md> ...

Exits 0 on success, non-zero on any validation failure (with messages on
stderr).

Files under 99_Raw/ are skipped — they are raw scraper output and have
no required schema.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml


class ValidationError(Exception):
    """Raised when a note's frontmatter does not match its type's contract."""


# Per-type required frontmatter keys.
REQUIRED_KEYS: dict[str, list[str]] = {
    "concept": [
        "type", "title", "tags", "difficulty", "prerequisites",
        "related", "sources", "status", "updated",
    ],
    "formula": ["type", "title", "used_in", "updated"],
    "example": ["type", "title", "illustrates", "updated"],
    "question": ["type", "title", "tests", "difficulty", "updated"],
    "moc": ["type", "title", "chapter_order", "updated"],
    "source": [
        "type", "title", "site", "url", "raw_path",
        "contributed_to", "updated",
    ],
}

ALLOWED_DIFFICULTY = {"beginner", "intermediate", "advanced"}
ALLOWED_STATUS = {"stub", "draft", "reviewed", "stable", "deprecated"}

# Wiki-link list keys: every entry must look like "[[...]]"
WIKILINK_LIST_KEYS = {
    "prerequisites", "related", "sources",
    "used_in", "illustrates", "tests", "contributed_to",
}

WIKILINK_RE = re.compile(r"^\[\[[^\[\]]+\]\]$")

FRONTMATTER_RE = re.compile(
    r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL
)


def parse_frontmatter(text: str) -> dict[str, Any]:
    """Extract and parse the YAML frontmatter block at the top of a note."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValidationError("no YAML frontmatter found at start of file")
    raw = match.group(1)
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as e:
        raise ValidationError(f"invalid YAML in frontmatter: {e}") from e
    if not isinstance(data, dict):
        raise ValidationError("frontmatter is not a YAML mapping")
    return data


def validate_note(fm: dict[str, Any], path: Path) -> None:
    """Validate a parsed frontmatter dict for the given note path.

    Raises ValidationError on failure with a path-prefixed message.
    """
    if "type" not in fm:
        raise ValidationError(f"{path}: missing required key 'type'")

    note_type = fm["type"]
    if note_type not in REQUIRED_KEYS:
        raise ValidationError(
            f"{path}: unknown type '{note_type}' "
            f"(allowed: {sorted(REQUIRED_KEYS)})"
        )

    for key in REQUIRED_KEYS[note_type]:
        if key not in fm:
            raise ValidationError(
                f"{path}: missing required key '{key}' for type '{note_type}'"
            )

    # difficulty (concept, question)
    if "difficulty" in REQUIRED_KEYS[note_type]:
        if fm["difficulty"] not in ALLOWED_DIFFICULTY:
            raise ValidationError(
                f"{path}: difficulty '{fm['difficulty']}' not in {sorted(ALLOWED_DIFFICULTY)}"
            )

    # status (concept only)
    if note_type == "concept":
        if fm["status"] not in ALLOWED_STATUS:
            raise ValidationError(
                f"{path}: status '{fm['status']}' not in {sorted(ALLOWED_STATUS)}"
            )

    # wiki-link list values
    for key in WIKILINK_LIST_KEYS:
        if key not in fm:
            continue
        value = fm[key]
        if not isinstance(value, list):
            raise ValidationError(
                f"{path}: '{key}' must be a list, got {type(value).__name__}"
            )
        for entry in value:
            if not isinstance(entry, str) or not WIKILINK_RE.match(entry):
                raise ValidationError(
                    f"{path}: '{key}' entry {entry!r} is not a valid wiki-link "
                    "(expected '[[Note name]]')"
                )


def should_skip(path: Path) -> bool:
    """Skip files that don't need validation."""
    parts = path.parts
    if not parts:
        return True
    if parts[0] == "99_Raw":
        return True
    if path.name == ".gitkeep":
        return True
    if not path.name.endswith(".md"):
        return True
    return False


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: validate_frontmatter.py <file.md> [...]", file=sys.stderr)
        return 2

    errors: list[str] = []
    checked = 0

    for arg in argv[1:]:
        path = Path(arg)
        if should_skip(path):
            continue
        if not path.exists():
            errors.append(f"{path}: file does not exist")
            continue
        try:
            text = path.read_text(encoding="utf-8")
            fm = parse_frontmatter(text)
            validate_note(fm, path)
            checked += 1
        except ValidationError as e:
            errors.append(str(e))

    if errors:
        print(f"FAIL: {len(errors)} validation error(s):", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"OK: {checked} note(s) validated")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
