# Part D: Data Quality Report

**Target Program:** B.Tech Computer Science and Engineering (CSE), Indian Institute of Technology Bhilai (IIT Bhilai)  
**Pipeline Execution Mode:** Deterministic, Schema-First, Zero-LLM/Embedding Pipeline  
**Execution Timestamp:** 10-11-2026  

---

## 1. Executive Summary & Inventory

The pipeline ingests raw course catalogues, academic regulations, and open learning resources, normalizes them against strict Pydantic models, conducts graph-theoretic and integrity validations, chunks syllabi and rules into embedding-ready units, and exports validated datasets.

| Entity Type | Raw Collected | Validated & Exported | Retrieval Chunks Generated | Target Requirement | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Courses** | 20 | 20 | 33 | $\ge 15$ | **Exceeded (+33%)** |
| **Academic Rules** | 14 | 14 | 14 | Individual quotable entries | **Fully Met** |
| **Open Resources** | 37 | 37 | 37 | $\ge 30$ | **Exceeded (+23%)** |
| **Total Chunks** | — | — | **84** | Structured with metadata | **Fully Met** |

---

## 2. Field Fill Percentage & Completeness Analysis

Every entity field is tracked and validated against Pydantic models with zero tolerance for missing mandatory attributes.

### A. Courses (20 Records)
| Field Name | Type | Expected | Actual Populated | Fill Percentage |
| :--- | :--- | :--- | :--- | :--- |
| `code` | String (Alphanumeric) | 20 | 20 | **100.0%** |
| `title` | String | 20 | 20 | **100.0%** |
| `department` | String | 20 | 20 | **100.0%** |
| `credits` | Float ($> 0$) | 20 | 20 | **100.0%** |
| `semester_offered` | Integer ($1 \le s \le 8$) | 20 | 20 | **100.0%** |
| `course_type` | Enum (core / elective) | 20 | 20 | **100.0%** |
| `mode` | Enum (offline) | 20 | 20 | **100.0%** |
| `prerequisites` | List[str] | 20 | 20 (empty list if none) | **100.0%** |
| `syllabus` | String ($> 10$ chars) | 20 | 20 | **100.0%** |
| `source_url` | HTTP/HTTPS URL | 20 | 20 | **100.0%** |
| `retrieved_on` | DD-MM-YYYY Date | 20 | 20 | **100.0%** |
| `source_type` | Literal["official"] | 20 | 20 | **100.0%** |

### B. Academic Rules (14 Records)
| Field Name | Type | Expected | Actual Populated | Fill Percentage |
| :--- | :--- | :--- | :--- | :--- |
| `id` | String | 14 | 14 | **100.0%** |
| `category` | Enum | 14 | 14 | **100.0%** |
| `text` | String (Verbatim policy) | 14 | 14 | **100.0%** |
| `numeric_limit` | Float / Optional | 14 | 14 | **100.0%** |
| `applies_to` | String | 14 | 14 | **100.0%** |
| `source_url` | HTTP/HTTPS URL | 14 | 14 | **100.0%** |
| `retrieved_on` | DD-MM-YYYY Date | 14 | 14 | **100.0%** |
| `source_type` | Literal["official"] | 14 | 14 | **100.0%** |

### C. Open Learning Resources (37 Records)
| Field Name | Type | Expected | Actual Populated | Fill Percentage |
| :--- | :--- | :--- | :--- | :--- |
| `id` | String | 37 | 37 | **100.0%** |
| `title` | String | 37 | 37 | **100.0%** |
| `provider` | Literal[NPTEL, MIT OCW] | 37 | 37 | **100.0%** |
| `course_code` | Foreign Key (Course code) | 37 | 37 | **100.0%** |
| `skill_covered` | String | 37 | 37 | **100.0%** |
| `licence` | String (Open license) | 37 | 37 | **100.0%** |
| `format` | String | 37 | 37 | **100.0%** |
| `duration_hours` | Float ($> 0$) | 37 | 37 | **100.0%** |
| `url` | HTTP/HTTPS URL | 37 | 37 | **100.0%** |
| `retrieved_on` | DD-MM-YYYY Date | 37 | 37 | **100.0%** |
| `source_type` | Literal["open-licence"] | 37 | 37 | **100.0%** |

---

## 3. Validation Suite & Catch Capabilities

The pipeline implements an assertive "fail-loudly" philosophy in [`src/validate.py`](file:///d:/Projects/Adobe/src/validate.py):

1. **DAG Acyclicity (Prerequisite Cycle Detection):**
   - *Algorithm:* 3-color Depth-First Search over directed prerequisite graph.
   - *Behavior:* If a dependency cycle is introduced (e.g., `CSL100 -> CSL202 -> CSL100`), the validator halts immediately and prints the exact cycle sequence (`[Prerequisite Cycle Error]`).
2. **Orphan Prerequisite Detection:**
   - *Algorithm:* Set-difference check against known course catalogue keys.
   - *Behavior:* Halts if a course references a code not present in the program catalogue.
3. **Primary Key / ID Uniqueness:**
   - Detects collision in course codes, rule IDs, or resource IDs.
4. **Mandatory Provenance Verification:**
   - Asserts valid HTTP/HTTPS URLs and ISO date strings (`DD-MM-YYYY`) on every entity.
5. **Foreign Key Referential Integrity:**
   - Asserts every open resource points to a validated course code.

---

## 4. Known Boundaries, Missing or Uncertain Data

1. **Non-CS Minor Offerings:**
   - The current dataset models B.Tech CSE in depth. If a CSE student asks about taking a minor in Mechatronics or Chemistry, those course syllabi are outside the primary CSE catalogue.
2. **Instructor-Specific Variations:**
   - While course syllabi and credit weights are officially fixed by the Academic Senate, specific textbooks and weekly lab problem distributions are determined at the discretion of the semester course instructor.
3. **Informal Co-Curricular Hours:**
   - Non-graded core units (NSS/NSO/Wellbeing) require 120 contact hours; logbook tracking is managed by Dean of Student Affairs records outside the academic catalogue.

---

## 5. Verification Protocol for Teammates

Any team member can audit and verify this dataset against the source materials using this 3-step checklist:

1. **Run the Automated Integrity Pipeline:**
   ```powershell
   python run_pipeline.py
   ```
   *Expected outcome:* Exits with code 0, reporting all 20 courses, 14 rules, 37 resources, and 84 chunks validated.
2. **Cross-Check with Official PDF:**
   - Open [`courseOfStudyIITBhilai.pdf`](file:///d:/Projects/Adobe/courseOfStudyIITBhilai.pdf).
   - Check Page 21–22: Verify B.Tech CSE course list, credit totals (144 academic + 12 non-graded).
   - Check Page 83–86: Verify syllabi and prerequisites for `CSL100`, `CSL201`, `CSL202`, `CSL251`, `CSL252`, `CSL253`, `CSL301`, `CSL302`, `CSL303`, `CSL304`, `CSL351`, `CSP352`.
   - Check Page 10–12: Verify 6-credit NPTEL limit, 25% overlap rule, and prerequisite failing grades ($F$, $FS$, $I$, $X$).
3. **Verify Open Educational Resource Links:**
   - Inspect [`SOURCES.md`](file:///d:/Projects/Adobe/SOURCES.md). Open any NPTEL or MIT OCW course link in a browser to confirm open licensing (CC-BY-SA or CC-BY-NC-SA) and active syllabus availability.
