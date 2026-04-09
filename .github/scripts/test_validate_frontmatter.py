"""Tests for validate_frontmatter.py.

Run with: pytest .github/scripts/test_validate_frontmatter.py -v
"""
from pathlib import Path
import pytest

from validate_frontmatter import (
    parse_frontmatter,
    validate_note,
    REQUIRED_KEYS,
    ValidationError,
)


def make_note(frontmatter: str, body: str = "# Title\n\ncontent") -> str:
    return f"---\n{frontmatter}\n---\n\n{body}\n"


# parse_frontmatter

def test_parse_frontmatter_extracts_yaml_block():
    note = make_note("type: concept\ntitle: WACC")
    fm = parse_frontmatter(note)
    assert fm == {"type": "concept", "title": "WACC"}


def test_parse_frontmatter_missing_block_raises():
    with pytest.raises(ValidationError, match="no YAML frontmatter"):
        parse_frontmatter("# Just a heading\n\nNo frontmatter.")


def test_parse_frontmatter_malformed_yaml_raises():
    note = "---\ntype: concept\ntitle: [unclosed\n---\nbody"
    with pytest.raises(ValidationError, match="invalid YAML"):
        parse_frontmatter(note)


# validate_note - concept

def test_concept_with_all_required_keys_passes():
    fm = {
        "type": "concept",
        "title": "WACC",
        "tags": ["valuation"],
        "difficulty": "intermediate",
        "prerequisites": ["[[Cost of equity]]"],
        "related": ["[[DCF valuation]]"],
        "sources": ["[[CFI - WACC guide]]"],
        "status": "draft",
        "updated": "2026-04-09",
    }
    validate_note(fm, Path("20_Concepts/Valuation/WACC.md"))


def test_concept_missing_required_key_fails():
    fm = {
        "type": "concept",
        "title": "WACC",
    }
    with pytest.raises(ValidationError, match="missing required key"):
        validate_note(fm, Path("20_Concepts/Valuation/WACC.md"))


def test_concept_wrong_difficulty_fails():
    fm = {
        "type": "concept",
        "title": "WACC",
        "tags": [],
        "difficulty": "expert",
        "prerequisites": [],
        "related": [],
        "sources": [],
        "status": "draft",
        "updated": "2026-04-09",
    }
    with pytest.raises(ValidationError, match="difficulty"):
        validate_note(fm, Path("20_Concepts/Valuation/WACC.md"))


def test_concept_wrong_status_fails():
    fm = {
        "type": "concept",
        "title": "WACC",
        "tags": [],
        "difficulty": "beginner",
        "prerequisites": [],
        "related": [],
        "sources": [],
        "status": "in_review",
        "updated": "2026-04-09",
    }
    with pytest.raises(ValidationError, match="status"):
        validate_note(fm, Path("20_Concepts/Valuation/WACC.md"))


def test_concept_invalid_wikilink_in_prerequisites_fails():
    fm = {
        "type": "concept",
        "title": "WACC",
        "tags": [],
        "difficulty": "beginner",
        "prerequisites": ["Cost of equity"],
        "related": [],
        "sources": [],
        "status": "draft",
        "updated": "2026-04-09",
    }
    with pytest.raises(ValidationError, match="wiki-link"):
        validate_note(fm, Path("20_Concepts/Valuation/WACC.md"))


# validate_note - formula

def test_formula_with_all_required_keys_passes():
    fm = {
        "type": "formula",
        "title": "WACC formula",
        "used_in": ["[[WACC]]"],
        "updated": "2026-04-09",
    }
    validate_note(fm, Path("40_Formulas/WACC formula.md"))


def test_formula_missing_used_in_fails():
    fm = {
        "type": "formula",
        "title": "WACC formula",
        "updated": "2026-04-09",
    }
    with pytest.raises(ValidationError, match="missing required key"):
        validate_note(fm, Path("40_Formulas/WACC formula.md"))


# validate_note - moc

def test_moc_with_all_required_keys_passes():
    fm = {
        "type": "moc",
        "title": "Valuation MOC",
        "chapter_order": 3,
        "updated": "2026-04-09",
    }
    validate_note(fm, Path("10_MOCs/Valuation MOC.md"))


# validate_note - source

def test_source_with_all_required_keys_passes():
    fm = {
        "type": "source",
        "title": "CFI - WACC guide",
        "site": "Corporate Finance Institute",
        "url": "https://example.com",
        "raw_path": "99_Raw/CFI/wacc-guide.md",
        "contributed_to": ["[[WACC]]"],
        "updated": "2026-04-09",
    }
    validate_note(fm, Path("90_Sources/CFI - WACC guide.md"))


# validate_note - type detection

def test_unknown_type_fails():
    fm = {"type": "blogpost", "title": "x", "updated": "2026-04-09"}
    with pytest.raises(ValidationError, match="unknown type"):
        validate_note(fm, Path("20_Concepts/x.md"))


def test_missing_type_fails():
    fm = {"title": "x", "updated": "2026-04-09"}
    with pytest.raises(ValidationError, match="missing required key.*type"):
        validate_note(fm, Path("20_Concepts/x.md"))
