"""Ingestion module to read raw course, rule, and resource files from data/raw/."""

import csv
import json
from pathlib import Path
from typing import List, Dict, Any


def ingest_raw_courses(raw_path: Path) -> List[Dict[str, Any]]:
    """Read data/raw/courses.csv into raw dictionary rows."""
    if not raw_path.exists():
        raise FileNotFoundError(f"Raw courses file not found: {raw_path}")
    with open(raw_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [dict(row) for row in reader]


def ingest_raw_rules(raw_path: Path) -> List[Dict[str, Any]]:
    """Read data/raw/rules.json into raw dictionary objects."""
    if not raw_path.exists():
        raise FileNotFoundError(f"Raw rules file not found: {raw_path}")
    with open(raw_path, mode="r", encoding="utf-8") as f:
        data = json.load(f)
        if not isinstance(data, list):
            raise ValueError(f"Expected a JSON list of rules, got {type(data)}")
        return data


def ingest_raw_resources(raw_path: Path) -> List[Dict[str, Any]]:
    """Read data/raw/resources.csv into raw dictionary rows."""
    if not raw_path.exists():
        raise FileNotFoundError(f"Raw resources file not found: {raw_path}")
    with open(raw_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [dict(row) for row in reader]
