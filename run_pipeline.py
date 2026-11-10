"""Main pipeline orchestration script for the Adobe Personalized Learning Buddy.

One-command execution taking raw source data to validated, normalized outputs and chunks.jsonl.
Strictly offline: Zero LLM / Embedding API calls.
Fails loudly on any data integrity or graph cycle error.
"""

import sys
from pathlib import Path
from src.ingest import ingest_raw_courses, ingest_raw_rules, ingest_raw_resources
from src.parse import parse_course, parse_academic_rule, parse_resource
from src.validate import run_all_validations, ValidationError
from src.chunk import generate_all_chunks
from src.export import (
    export_courses_to_csv,
    export_rules_to_json,
    export_resources_to_csv,
    export_chunks_to_jsonl
)


def run_pipeline() -> None:
    print("=" * 60)
    print("Starting Adobe Learning Buddy Knowledge Base Data Pipeline")
    print("=" * 60)

    base_dir = Path(__file__).resolve().parent
    raw_dir = base_dir / "data" / "raw"
    processed_dir = base_dir / "data" / "processed"
    chunks_path = base_dir / "chunks.jsonl"

    # Stage 1: Ingest
    print("\n[Stage 1/5] Ingesting raw source files from data/raw/ ...")
    raw_courses = ingest_raw_courses(raw_dir / "courses.csv")
    raw_rules = ingest_raw_rules(raw_dir / "rules.json")
    raw_resources = ingest_raw_resources(raw_dir / "resources.csv")
    print(f"  -> Ingested {len(raw_courses)} raw course rows")
    print(f"  -> Ingested {len(raw_rules)} raw rule definitions")
    print(f"  -> Ingested {len(raw_resources)} raw resource rows")

    # Stage 2: Parse and Normalize
    print("\n[Stage 2/5] Parsing and normalizing entities with Pydantic schemas ...")
    courses = [parse_course(row) for row in raw_courses]
    rules = [parse_academic_rule(r) for r in raw_rules]
    resources = [parse_resource(res) for res in raw_resources]
    print(f"  -> Successfully parsed {len(courses)} Courses")
    print(f"  -> Successfully parsed {len(rules)} Academic Rules")
    print(f"  -> Successfully parsed {len(resources)} Open Resources")

    # Stage 3: Strict Validation
    print("\n[Stage 3/5] Running strict validation checks (integrity & DAG checks) ...")
    try:
        val_result = run_all_validations(courses, rules, resources)
        print(f"  -> Integrity Status: {val_result['status']}")
        print(f"  -> Prerequisites Graph: Acyclic (DFS verified)")
        print(f"  -> Source URLs & Retrieval Dates: 100% verified")
    except ValidationError as e:
        print(f"\n[FATAL VALIDATION ERROR] Pipeline halted:\n{e}", file=sys.stderr)
        sys.exit(1)

    # Stage 4: Chunking
    print("\n[Stage 4/5] Chunking syllabi, rules, and resources for embedding readiness ...")
    chunks = generate_all_chunks(courses, rules, resources)
    print(f"  -> Generated {len(chunks)} retrieval-sized chunks with parent IDs and filter metadata")

    # Stage 5: Export
    print("\n[Stage 5/5] Exporting clean data to data/processed/ and chunks.jsonl ...")
    export_courses_to_csv(courses, processed_dir / "courses.csv")
    export_rules_to_json(rules, processed_dir / "rules.json")
    export_resources_to_csv(resources, processed_dir / "resources.csv")
    export_chunks_to_jsonl(chunks, chunks_path)
    print(f"  -> Exported: {processed_dir / 'courses.csv'}")
    print(f"  -> Exported: {processed_dir / 'rules.json'}")
    print(f"  -> Exported: {processed_dir / 'resources.csv'}")
    print(f"  -> Exported: {chunks_path}")

    print("\n" + "=" * 60)
    print("Pipeline completed successfully in 100% reproducible mode!")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()
