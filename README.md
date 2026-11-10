# Adobe Personalized Learning Buddy: Knowledge Base & Data Pipeline

A source-traced knowledge base and reproducible data pipeline for **B.Tech Computer Science & Engineering (CSE)** at **IIT Bhilai**.

---

## 1. Project Overview

This repository builds the foundational data substrate for an AI-powered personalized learning buddy. It ingests official curriculum data, academic rules, and open learning resources, normalizes them against strict schemas, validates prerequisite graphs and integrity constraints, and exports clean metadata-rich chunks ready for downstream embedding.

### Ground Rules & Constraints Met
- **Strictly Offline:** Zero LLM or Embedding API calls. Pipeline terminates cleanly with structured `chunks.jsonl`.
- **Single-Command Execution:** Fully reproducible via `python run_pipeline.py`.
- **Source-Traced & Ethical:** 100% of data is derived from official institute publications ([`courseOfStudyIITBhilai.pdf`](courseOfStudyIITBhilai.pdf)) and open-licensed resources (NPTEL, MIT OCW). No private student records or unauthorized data.
- **Fail-Loudly Validation:** Custom graph cycle detection and integrity assertions halt execution on bad data.

---

## 2. Repository Structure

```text
.
├── courseOfStudyIITBhilai.pdf    # Source PDF: Official IIT Bhilai Course of Study
├── data/
│   ├── raw/                      # Untouched source datasets
│   │   ├── courses.csv           # 20 Courses (Core + Elective)
│   │   ├── rules.json            # 14 Quotable Academic Rules
│   │   └── resources.csv         # 37 Open Resources (NPTEL & MIT OCW)
│   └── processed/                # Normalized & validated pipeline output
│       ├── courses.csv           # Cleaned Course Catalogue
│       ├── rules.json            # Formatted Academic Regulations
│       └── resources.csv         # Standardized Open Educational Content
├── src/
│   ├── __init__.py
│   ├── schemas.py                # Strict Pydantic models (BaseEntity, Course, Rule, Resource, Chunk)
│   ├── ingest.py                 # File ingestion logic
│   ├── parse.py                  # Normalization & parsing logic
│   ├── validate.py               # Integrity checks & 3-color DFS DAG cycle detection
│   ├── chunk.py                  # Semantic text chunker with filter metadata
│   └── export.py                 # Exporters for CSV, JSON, and JSONL
├── run_pipeline.py               # Main orchestration script (One-command run)
├── chunks.jsonl                  # 84 retrieval-sized chunks ready for embedding
├── requirements.txt              # Pipeline dependencies (pydantic, pypdf)
├── SOURCES.md                    # Detailed provenance ledger with licenses and URLs
├── REPORT.md                     # Part D: Data quality and field completeness report
├── IDEAS.md                      # Part E: 3 questions buddy can answer vs 3 it cannot
└── README.md                     # Setup instructions and architectural documentation
```

---

## 3. Quickstart & Usage

### Prerequisites
- Python 3.10+
- `pip install -r requirements.txt`

### Run the Pipeline
Execute the entire pipeline with a single command:

```powershell
python run_pipeline.py
```

### Pipeline Execution Stages
1. **Ingest:** Reads raw files untouched from `data/raw/`.
2. **Parse & Normalize:** Enforces uppercase codes (e.g., `CSL100`), numeric credits, and validates against Pydantic models.
3. **Validate:** Executes graph-theoretic DFS cycle detection, checks for missing prerequisites, checks duplicate keys, and verifies source URLs. Fails loudly on any error.
4. **Chunk:** Splits syllabi, rules, and resources into retrieval units with rich filtering metadata.
5. **Export:** Writes normalized tables to `data/processed/` and exports `chunks.jsonl`.

---

## 4. Deliverables Checklist

- [x] **`data/raw/`**: Contains untouched source files (`courses.csv`, `rules.json`, `resources.csv`).
- [x] **`data/processed/`**: Contains cleaned, validated files.
- [x] **`chunks.jsonl`**: 84 chunks with `chunk_id`, `parent_id`, `entity_type`, `text`, `source_url`, and `filter_metadata`.
- [x] **`SOURCES.md`**: Itemized ledger with official portal URLs, retrieval dates, and open licenses.
- [x] **`REPORT.md`**: Part D Data Quality Report covering field fill rates, DAG checks, and verification procedures.
- [x] **`IDEAS.md`**: Part E deliverables detailing 3 answerable and 3 unanswerable questions.
- [x] **Single-Command:** `python run_pipeline.py` executes cleanly without network calls or LLM dependencies.
