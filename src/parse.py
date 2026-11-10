"""Parsing and normalization module.

Transforms raw string inputs into clean, normalized types validated by Pydantic models.
"""

import re
from typing import List, Dict, Any
from src.schemas import Course, AcademicRule, Resource


def normalize_code(code_str: str) -> str:
    """Standardize course code to uppercase alphanumeric without spaces (e.g. 'CS 100' -> 'CSL100')."""
    if not code_str:
        return ""
    return re.sub(r"\s+", "", code_str).upper()


def parse_prerequisites(prereqs_str: Any) -> List[str]:
    """Parse comma/semicolon/slash separated prerequisite string into normalized list of course codes."""
    if not prereqs_str or not str(prereqs_str).strip():
        return []
    parts = re.split(r"[,;/\s]+", str(prereqs_str).strip())
    cleaned = [normalize_code(p) for p in parts if p.strip() and p.strip().lower() != "none"]
    return [c for c in cleaned if c]


def parse_course(row: Dict[str, Any]) -> Course:
    """Parse and validate raw course record into Course schema."""
    code = normalize_code(row.get("code", ""))
    prereqs = parse_prerequisites(row.get("prerequisites", ""))
    
    return Course(
        code=code,
        title=str(row.get("title", "")).strip(),
        department=str(row.get("department", "")).strip(),
        credits=float(row.get("credits", 0.0)),
        semester_offered=int(row.get("semester_offered", 1)),
        course_type=str(row.get("course_type", "core")).strip().lower(),
        mode=str(row.get("mode", "offline")).strip().lower(),
        prerequisites=prereqs,
        syllabus=str(row.get("syllabus", "")).strip(),
        source_url=str(row.get("source_url", "")).strip(),
        retrieved_on=str(row.get("retrieved_on", "")).strip(),
        source_type=str(row.get("source_type", "official")).strip().lower()
    )


def parse_academic_rule(item: Dict[str, Any]) -> AcademicRule:
    """Parse and validate raw academic rule into AcademicRule schema."""
    numeric_lim = item.get("numeric_limit")
    if numeric_lim is not None and str(numeric_lim).strip() != "":
        numeric_lim = float(numeric_lim)
    else:
        numeric_lim = None

    return AcademicRule(
        id=str(item.get("id", "")).strip(),
        category=str(item.get("category", "")).strip().lower(),
        text=str(item.get("text", "")).strip(),
        numeric_limit=numeric_lim,
        applies_to=str(item.get("applies_to", "")).strip(),
        source_url=str(item.get("source_url", "")).strip(),
        retrieved_on=str(item.get("retrieved_on", "")).strip(),
        source_type=str(item.get("source_type", "official")).strip().lower()
    )


def parse_resource(row: Dict[str, Any]) -> Resource:
    """Parse and validate raw resource into Resource schema."""
    return Resource(
        id=str(row.get("id", "")).strip(),
        title=str(row.get("title", "")).strip(),
        provider=str(row.get("provider", "")).strip(),
        course_code=normalize_code(row.get("course_code", "")),
        skill_covered=str(row.get("skill_covered", "")).strip(),
        licence=str(row.get("licence", "")).strip(),
        format=str(row.get("format", "")).strip(),
        duration_hours=float(row.get("duration_hours", 0.0)),
        url=str(row.get("url", "")).strip(),
        source_url=str(row.get("url", "")).strip(),
        retrieved_on=str(row.get("retrieved_on", "")).strip(),
        source_type=str(row.get("source_type", "open-licence")).strip().lower()
    )
