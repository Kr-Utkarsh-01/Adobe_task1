# Part E: Ideas Note

**Product:** Adobe Personalized Learning Buddy for Students  
**Focus:** IIT Bhilai B.Tech Computer Science & Engineering  
**Data Substrate:** Source-traced curriculum, academic regulations, and mapped open educational resources (NPTEL / MIT OCW)

---

## 1. Three Questions the Buddy CAN Answer Well

### Question 1: Prerequisite Traversal & Semester Sequencing
> *"I failed Data Structures (CSL202) in Semester 3. Which upcoming courses am I blocked from taking in Semester 4 and 5, and what must I clear first?"*

- **How the Buddy Answers:**
  The system utilizes the validated Directed Acyclic Graph (DAG) in `src/validate.py` and `Course.prerequisites`.
  1. It performs a forward reachable search from `CSL202`.
  2. It immediately flags that `CSL252` (Design & Analysis of Algorithms) requires `CSL202`, and `CSL253` (Theory of Computation) requires `CSL202`.
  3. Cascading further, it detects that `CSL301` (Operating Systems) requires `CSL202`, and `CSL302` (Compiler Design) transitively requires `CSL253`.
  4. It cites official Rule `RULE_PREREQUISITE_PASS_GRADE` (failing grade blocks registration) and outputs a concrete remedial semester plan.

---

### Question 2: Academic Regulation & Credit Limit Compliance
> *"Can I earn academic credits towards my B.Tech degree by taking 3 NPTEL courses this summer totaling 8 credits?"*

- **How the Buddy Answers:**
  The system queries the quotable academic policy database (`data/processed/rules.json`).
  1. It retrieves Rule `RULE_NPTEL_MAX_CREDIT_LIMIT` (*"BTech students can take V-type courses / NPTEL up to a maximum of 6 credits during the entire program"*).
  2. It identifies that 8 credits exceeds the statutory 6-credit lifetime cap by 2 credits.
  3. It explicitly guides the student: 6 credits can be counted towards Program/Open electives subject to DUGC approval, while the additional 2 credits will not count toward the 144-credit graduation threshold.

---

### Question 3: Skill Gap Diagnosis & Open Resource Mapping
> *"I want to prepare for a Systems & Cloud Engineering internship before Semester 5. Which official institute courses and open resources should I focus on?"*

- **How the Buddy Answers:**
  The system uses semantic retrieval over `chunks.jsonl` filtered by topics `Virtualization`, `Concurrency`, `Socket Programming`, and `Containerization`.
  1. It maps the requirement directly to `CSP203` (Docker & Linux tools), `CSL301` (Operating Systems: xv6, paging, threads), and `CSL351` (Computer Networks: TCP/IP, sockets).
  2. Because the student is preparing *prior* to taking Semester 5, the buddy recommends the mapped open educational resources from NPTEL & MIT OCW:
     - `RES_MIT_CSP203_01` (*The Missing Semester of Your CS Education*, MIT OCW - 15h)
     - `RES_MIT_CSL301_02` (*Operating System Engineering 6.828*, MIT OCW - 40h)
     - `RES_NPTEL_CSL351_01` (*Computer Networks & IP*, NPTEL - 30h)
  3. It computes the total study hours (85 hours) and constructs a structured 6-week summer roadmap.

---

## 2. Three Questions the Buddy CANNOT Answer (and Why)

### Question 1: Subjective Grading Harshness & Instructor Discretion
> *"Is the professor for CSL302 (Compiler Design) an easy grader compared to the Artificial Intelligence instructor?"*

- **Why it Cannot Answer:**
  The knowledge base contains strictly official, objective institute curriculum and regulatory data (syllabi, credit structures, and senate rules). It explicitly excludes unverified student gossip, subjective ratings, or private grade distributions to maintain high data integrity and ethical compliance.

---

### Question 2: Real-Time Classroom Timetable Collisions
> *"Will CSL304 (AI) have a lecture or lab clash with my open elective on Tuesdays at 2:00 PM?"*

- **Why it Cannot Answer:**
  The pipeline models academic program structures and semester curriculum templates (Autumn vs. Spring), but does *not* ingest real-time semester room allocations or weekly timetable slots, which change every academic session and are published separately by the Academic Office right before registration.

---

### Question 3: Mental Health Counseling & Personal Grievance Redressal
> *"I feel completely overwhelmed by my academic workload and need help coping."*

- **Why it Cannot Answer:**
  While the system documents non-graded wellbeing requirements (`NCN100 Practices for Comprehensive Wellbeing`), it is an academic curriculum planner and not a medical or psychological counseling service. An ethical AI buddy must detect wellness distress, refuse to offer medical advice, and immediately refer the student to the institute's official student counseling cell and campus medical center.
