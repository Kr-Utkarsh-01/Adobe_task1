# Adobe Personalized Learning Buddy: Selection Assignment
## Workspace Initialization Context

### 1. Project Overview & Constraints
**Objective:** Build a source-traced knowledge base and a reproducible data pipeline for one specific academic program (e.g., B.Tech Computer Science). The pipeline must ingest raw data, normalize it, validate it strictly, chunk it for future embeddings, and export it cleanly.
**Time Window:** 24 hours.
**Strict Constraints:**
- NO LLM or Embedding API calls.
- Run from a single command (e.g., `python run_pipeline.py`).
- Data must be real, publicly available, and source-traced with licenses.
- Must "fail loudly" on validation errors (e.g., missing prerequisites, cycles).

### 2. Chosen Tech Stack: Schema-First Python
- **Core Engine:** Standard Python (`csv`, `json`, `pathlib`).
- **Validation:** `pydantic` (Highly recommended for strict schema enforcement, type checking, and failing loudly on bad data).
- **Execution:** A single orchestration script (`run_pipeline.py`).

### 3. Initial Repository Structure
Create this structure in your workspace to meet all submission requirements:

```text
adobe-selection-assignment/
├── data/
│   ├── raw/                  # Untouched source files (CSV, JSON, txt)
│   └── processed/            # Final clean CSV/JSON files (Pipeline output)
├── src/
│   ├── __init__.py
│   ├── schemas.py            # Pydantic models (Course, Rule, Resource, Chunk)
│   ├── ingest.py             # Logic to read from data/raw/
│   ├── parse.py              # Logic to normalize strings, credits, semesters
│   ├── validate.py           # Logic to check graph cycles, missing prereqs
│   ├── chunk.py              # Logic to split text into retrieval-sized blocks
│   └── export.py             # Logic to write to data/processed/ and chunks.jsonl
├── run_pipeline.py           # Main orchestration script (One-command run)
├── requirements.txt          # Contains pydantic
├── chunks.jsonl              # Final chunked output (Pipeline output)
├── SOURCES.md                # Mandatory: URL, retrieval date, license for every source
├── IDEAS.md                  # Mandatory: Part E deliverables (1 page)
├── REPORT.md                 # Mandatory: Data quality report (Part D)
└── README.md                 # Setup instructions and pipeline overview
```

### 4. Step-by-Step Implementation Plan

#### Phase 1: Data Collection (Manual/Semi-Automated)
1. **Courses:** Gather 15 core courses for one program. Note code, title, dept, credits, semester, type, mode, syllabus, and prerequisites. Save to `data/raw/courses.csv`.
2. **Rules:** Gather academic rules (credit limits, minor eligibility). Save to `data/raw/rules.json`.
3. **Resources:** Gather 30+ open resources (NPTEL, MIT OCW) mapping to the course skills. Save to `data/raw/resources.csv`.
4. **Documentation:** Immediately log all URLs, dates, and licenses in `SOURCES.md`.

#### Phase 2: Schema Design (`src/schemas.py`)
Define Pydantic models:
- `BaseEntity`: includes `source_url`, `retrieved_on`, `source_type`.
- `Course`, `AcademicRule`, `Resource`, `Chunk` inheriting from `BaseEntity`.

#### Phase 3: Pipeline Engineering (`src/` & `run_pipeline.py`)
1. **Ingest:** Read raw files using standard `csv`/`json`.
2. **Parse:** Clean up course codes (e.g., "CS 101" -> "CS101"), ensure credits are numeric. Load data into Pydantic models.
3. **Validate:** 
   - Check that all prerequisite course codes exist in the main course list.
   - Detect prerequisite cycles (e.g., A requires B, B requires A).
   - *If validation fails, raise an exception and halt execution.*
4. **Chunk:** Write a simple text splitter for syllabi and rules (e.g., splitting by paragraph or max token/word count). Map each chunk to its `parent_id`.
5. **Export:** Write validated models back out to `data/processed/` and append chunks to `chunks.jsonl` at the root.

#### Phase 4: Documentation & Deliverables
- Write `REPORT.md` (Part D): Detail entity counts, field fill percentages, validation checks implemented, and how to verify data.
- Write `IDEAS.md` (Part E): Detail 3 questions the buddy *can* answer (e.g., prerequisite paths, credit limits) and questions it *cannot* answer (e.g., subjective difficulty, scheduling conflicts).

### 5. Final Checklist Before Zipping/Pushing
- [ ] `data/raw/` contains original files.
- [ ] `data/processed/` contains cleaned files.
- [ ] `chunks.jsonl` exists in the root directory.
- [ ] `SOURCES.md` lists every source with license/date.
- [ ] `IDEAS.md` answers Part E prompts.
- [ ] `REPORT.md` answers Part D prompts.
- [ ] `python run_pipeline.py` runs start-to-finish without errors.
- [ ] NO API keys, LLM calls, or embedding logic present in the codebase.