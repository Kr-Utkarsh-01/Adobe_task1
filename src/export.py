"""Export module.

Persists cleaned and validated datasets to data/processed/ and chunks to chunks.jsonl.
"""

import csv
import json
from pathlib import Path
from typing import List
from src.schemas import Course, AcademicRule, Resource, Chunk


def export_courses_to_csv(courses: List[Course], out_path: Path) -> None:
    """Write normalized courses to CSV with explicit prerequisite string."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for c in courses:
        data = c.model_dump()
        data["prerequisites"] = ", ".join(c.prerequisites)
        rows.append(data)
    
    if not rows:
        return

    with open(out_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def export_rules_to_json(rules: List[AcademicRule], out_path: Path) -> None:
    """Write normalized rules to JSON file."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, mode="w", encoding="utf-8") as f:
        json.dump([r.model_dump() for r in rules], f, indent=2)


def export_resources_to_csv(resources: List[Resource], out_path: Path) -> None:
    """Write normalized resources to CSV."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    rows = [r.model_dump() for r in resources]
    if not rows:
        return
    with open(out_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def export_chunks_to_jsonl(chunks: List[Chunk], out_path: Path) -> None:
    """Write chunks line-by-line in JSON Lines format."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, mode="w", encoding="utf-8") as f:
        for chk in chunks:
            f.write(json.dumps(chk.model_dump(), ensure_ascii=False) + "\n")
