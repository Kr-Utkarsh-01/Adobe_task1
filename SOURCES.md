# Data Sources & Provenance Ledger

This document strictly tracks all official, openly licensed data sources collected for the **Adobe Personalized Learning Buddy: IIT Bhilai B.Tech Computer Science & Engineering (CSE)** knowledge base and reproducible data pipeline.

---

## 1. Official Institute Curriculum & Regulations

- **Source Entity:** IIT Bhilai (Indian Institute of Technology Bhilai)
- **Document / Portal:** *Course of Study & Academic Regulations (BTech Programs)*
- **Source URL:** [https://www.iitbhilai.ac.in/index.php?pid=new_schedule_programs](https://www.iitbhilai.ac.in/index.php?pid=new_schedule_programs)
- **Retrieval Date:** 2026-11-10
- **License / Terms:** Official Institute Publication (Public Institutional Information for Academic Reference)
- **Entities Derived:**
  - 20 Academic Courses ([`data/raw/courses.csv`](file:///d:/Projects/Adobe/data/raw/courses.csv)): Exact course codes, course names, departments, numeric credits ($L-T-P-C$), semester sequence, course types (core/elective), and authoritative syllabus descriptions.
  - 14 Academic Rules ([`data/raw/rules.json`](file:///d:/Projects/Adobe/data/raw/rules.json)): Minimum degree credits (144 + 12 non-graded units), credit distribution limits, semester workload bounds, prerequisite passing grades, $>25\%$ overlap exclusion rule, and the 6-credit NPTEL limit for V-type courses.

---

## 2. Open Educational Resources (NPTEL & MIT OpenCourseWare)

All learning resources are exclusively curated from **NPTEL (National Programme on Technology Enhanced Learning / SWAYAM)** and **MIT OpenCourseWare (MIT OCW)** under open educational licenses.

- **Retrieval Date:** 2026-11-10
- **Total Resources:** 37
- **Raw File:** [`data/raw/resources.csv`](file:///d:/Projects/Adobe/data/raw/resources.csv)

### Itemized Provenance Ledger

| Resource ID | Course Code | Title | Provider | License | Format | Duration | Source URL |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `RES_NPTEL_CSL100_01` | CSL100 | Problem Solving through Programming in C | NPTEL | CC-BY-SA 4.0 | video_lectures | 30h | [nptel.ac.in/courses/106105171](https://nptel.ac.in/courses/106105171) |
| `RES_MIT_CSL100_02` | CSL100 | Intro to Computer Science & Programming in Python | MIT OCW | CC-BY-NC-SA 4.0 | course_materials_and_video | 36h | [ocw.mit.edu/courses/6-0001](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/) |
| `RES_NPTEL_MAL100_01` | MAL100 | Calculus of One and Several Variables | NPTEL | CC-BY-SA 4.0 | video_lectures | 40h | [nptel.ac.in/courses/111104085](https://nptel.ac.in/courses/111104085) |
| `RES_MIT_MAL100_02` | MAL100 | Single Variable Calculus | MIT OCW | CC-BY-NC-SA 4.0 | video_lectures_and_exams | 35h | [ocw.mit.edu/courses/18-01sc](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) |
| `RES_MIT_MAL101_01` | MAL101 | Linear Algebra (Gilbert Strang) | MIT OCW | CC-BY-NC-SA 4.0 | video_lectures | 35h | [ocw.mit.edu/courses/18-06](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) |
| `RES_NPTEL_MAL101_02` | MAL101 | Linear Algebra - IIT Madras | NPTEL | CC-BY-SA 4.0 | video_lectures | 30h | [nptel.ac.in/courses/111106051](https://nptel.ac.in/courses/111106051) |
| `RES_NPTEL_ECL101_01` | ECL101 | Digital Electronic Circuits | NPTEL | CC-BY-SA 4.0 | video_lectures | 30h | [nptel.ac.in/courses/108105132](https://nptel.ac.in/courses/108105132) |
| `RES_MIT_ECL101_02` | ECL101 | Circuits and Electronics | MIT OCW | CC-BY-NC-SA 4.0 | video_lectures_and_labs | 38h | [ocw.mit.edu/courses/6-002](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/) |
| `RES_NPTEL_CSL201_01` | CSL201 | Discrete Mathematics - IIT Ropar | NPTEL | CC-BY-SA 4.0 | video_lectures | 30h | [nptel.ac.in/courses/106106183](https://nptel.ac.in/courses/106106183) |
| `RES_MIT_CSL201_02` | CSL201 | Mathematics for Computer Science | MIT OCW | CC-BY-NC-SA 4.0 | course_notes_and_videos | 40h | [ocw.mit.edu/courses/6-042j](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) |
| `RES_NPTEL_CSL202_01` | CSL202 | Programming, Data Structures and Algorithms in Python | NPTEL | CC-BY-SA 4.0 | video_lectures | 20h | [nptel.ac.in/courses/106106145](https://nptel.ac.in/courses/106106145) |
| `RES_MIT_CSL202_02` | CSL202 | Introduction to Algorithms (6.006) | MIT OCW | CC-BY-NC-SA 4.0 | video_lectures_and_problem_sets | 36h | [ocw.mit.edu/courses/6-006](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) |
| `RES_MIT_CSP203_01` | CSP203 | The Missing Semester of Your CS Education | MIT OCW | CC-BY-NC-SA 4.0 | video_lectures_and_exercises | 15h | [missing.csail.mit.edu](https://missing.csail.mit.edu/) |
| `RES_NPTEL_CSP203_02` | CSP203 | Linux Basics and Shell Scripting | NPTEL | CC-BY-SA 4.0 | video_lectures | 20h | [nptel.ac.in/courses/106105221](https://nptel.ac.in/courses/106105221) |
| `RES_MIT_MAL403_01` | MAL403 | Introduction to Probability and Statistics | MIT OCW | CC-BY-NC-SA 4.0 | lecture_notes_and_exams | 36h | [ocw.mit.edu/courses/18-05](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2014/) |
| `RES_NPTEL_MAL403_02` | MAL403 | Probability and Statistics - IIT Kharagpur | NPTEL | CC-BY-SA 4.0 | video_lectures | 30h | [nptel.ac.in/courses/111105041](https://nptel.ac.in/courses/111105041) |
| `RES_NPTEL_CSL251_01` | CSL251 | Computer Organization and Architecture | NPTEL | CC-BY-SA 4.0 | video_lectures | 30h | [nptel.ac.in/courses/106105163](https://nptel.ac.in/courses/106105163) |
| `RES_MIT_CSL251_02` | CSL251 | Computation Structures | MIT OCW | CC-BY-NC-SA 4.0 | video_lectures_and_labs | 40h | [ocw.mit.edu/courses/6-004](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/) |
| `RES_MIT_CSL252_01` | CSL252 | Design and Analysis of Algorithms (6.046J) | MIT OCW | CC-BY-NC-SA 4.0 | video_lectures | 34h | [ocw.mit.edu/courses/6-046j](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/) |
| `RES_NPTEL_CSL252_02` | CSL252 | Design and Analysis of Algorithms - IIT Madras | NPTEL | CC-BY-SA 4.0 | video_lectures | 30h | [nptel.ac.in/courses/106106131](https://nptel.ac.in/courses/106106131) |
| `RES_NPTEL_CSL253_01` | CSL253 | Theory of Computation - IIT Kanpur | NPTEL | CC-BY-SA 4.0 | video_lectures | 30h | [nptel.ac.in/courses/106104148](https://nptel.ac.in/courses/106104148) |
| `RES_MIT_CSL253_02` | CSL253 | Automata, Computability, and Complexity | MIT OCW | CC-BY-NC-SA 4.0 | course_notes_and_problem_sets | 32h | [ocw.mit.edu/courses/6-045j](https://ocw.mit.edu/courses/6-045j-automata-computability-and-complexity-spring-2011/) |
| `RES_NPTEL_CSL301_01` | CSL301 | Operating System Fundamentals - IIT Kharagpur | NPTEL | CC-BY-SA 4.0 | video_lectures | 30h | [nptel.ac.in/courses/106105214](https://nptel.ac.in/courses/106105214) |
| `RES_MIT_CSL301_02` | CSL301 | Operating System Engineering (6.828) | MIT OCW | CC-BY-NC-SA 4.0 | lab_assignments_and_lectures | 40h | [ocw.mit.edu/courses/6-828](https://ocw.mit.edu/courses/6-828-operating-system-engineering-fall-2012/) |
| `RES_NPTEL_CSL302_01` | CSL302 | Compiler Design - IIT Kharagpur | NPTEL | CC-BY-SA 4.0 | video_lectures | 30h | [nptel.ac.in/courses/106105190](https://nptel.ac.in/courses/106105190) |
| `RES_NPTEL_CSL302_02` | CSL302 | Principles of Compiler Design - IIT Madras | NPTEL | CC-BY-SA 4.0 | video_lectures | 32h | [nptel.ac.in/courses/106106052](https://nptel.ac.in/courses/106106052) |
| `RES_NPTEL_CSL303_01` | CSL303 | Database Management System - IIT Kharagpur | NPTEL | CC-BY-SA 4.0 | video_lectures | 25h | [nptel.ac.in/courses/106105175](https://nptel.ac.in/courses/106105175) |
| `RES_MIT_CSL303_02` | CSL303 | Database Systems (6.830) | MIT OCW | CC-BY-NC-SA 4.0 | lecture_notes_and_labs | 35h | [ocw.mit.edu/courses/6-830](https://ocw.mit.edu/courses/6-830-database-systems-fall-2010/) |
| `RES_MIT_CSL304_01` | CSL304 | Artificial Intelligence (6.034) | MIT OCW | CC-BY-NC-SA 4.0 | video_lectures_and_demos | 35h | [ocw.mit.edu/courses/6-034](https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/) |
| `RES_NPTEL_CSL304_02` | CSL304 | AI: Search Methods for Problem Solving | NPTEL | CC-BY-SA 4.0 | video_lectures | 30h | [nptel.ac.in/courses/106106126](https://nptel.ac.in/courses/106106126) |
| `RES_NPTEL_CSL351_01` | CSL351 | Computer Networks and Internet Protocol | NPTEL | CC-BY-SA 4.0 | video_lectures | 30h | [nptel.ac.in/courses/106105183](https://nptel.ac.in/courses/106105183) |
| `RES_MIT_CSL351_02` | CSL351 | Computer Networks (6.829) | MIT OCW | CC-BY-NC-SA 4.0 | lecture_notes_and_assignments | 35h | [ocw.mit.edu/courses/6-829](https://ocw.mit.edu/courses/6-829-computer-networks-fall-2002/) |
| `RES_MIT_CSP352_01` | CSP352 | Generative AI and LLMs for Software Systems | MIT OCW | CC-BY-NC-SA 4.0 | lecture_materials_and_code | 24h | [ocw.mit.edu/eecs](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/) |
| `RES_NPTEL_CSP352_02` | CSP352 | Software Engineering and Modern Development | NPTEL | CC-BY-SA 4.0 | video_lectures | 30h | [nptel.ac.in/courses/106105182](https://nptel.ac.in/courses/106105182) |
| `RES_NPTEL_CSL512_01` | CSL512 | Parallel and Distributed Algorithms | NPTEL | CC-BY-SA 4.0 | video_lectures | 25h | [nptel.ac.in/courses/106104120](https://nptel.ac.in/courses/106104120) |
| `RES_NPTEL_CSL515_01` | CSL515 | Randomized Algorithms - IIT Delhi | NPTEL | CC-BY-SA 4.0 | video_lectures | 30h | [nptel.ac.in/courses/106102011](https://nptel.ac.in/courses/106102011) |
| `RES_MIT_CSL612_01` | CSL612 | Advanced Complexity Theory | MIT OCW | CC-BY-NC-SA 4.0 | lecture_notes_and_problems | 32h | [ocw.mit.edu/courses/18-405j](https://ocw.mit.edu/courses/18-405j-advanced-complexity-theory-fall-2001/) |
