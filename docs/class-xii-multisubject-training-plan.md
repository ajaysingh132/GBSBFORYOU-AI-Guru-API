# Class XII Multi-Subject AI Guru Training Plan

## Goal
Extend GBSBFORYOU AI Guru from the initial CBSE Class XII Computer Science (083) pilot to a subject-aware Class XII learning system. Preserve the existing mobile-first, free-first approach and keep curriculum knowledge separate from application logic.

## Important current-state boundary
The current `app/core.py` is a deterministic, rule-based workflow scaffold. A successful `POST /v1/teach` response does not mean a subject model has been trained. Subject expertise must be grounded in approved curriculum sources, retrieval, citations, and tested answers before being described as production-ready.

## Curriculum baseline
- Board: CBSE, unless the learner profile explicitly selects another board/state.
- Class: XII.
- Academic session: 2026–27.
- Initial reference subject: Computer Science (083).
- Use official CBSE curriculum/syllabus, NCERT textbooks and official sample question papers/marking schemes where available.
- Keep source URL, document title, board, class, subject code, session, chapter/topic, page/section, language, retrieval date and content hash for every source chunk.
- Do not claim coverage for any chapter until the source inventory and retrieval checks confirm it.

## Subject rollout order
Build a registry that can support all streams, but onboard subjects in small verified batches:

### Batch 1 — common/high-priority
1. Mathematics (041)
2. Physics (042)
3. Chemistry (043)
4. Biology (044)
5. English Core (301)

### Batch 2 — Commerce
6. Accountancy (055)
7. Business Studies (054)
8. Economics (030)
9. Applied Mathematics (241), if selected by the learner

### Batch 3 — Humanities and electives
10. History (027)
11. Political Science (028)
12. Geography (029)
13. Psychology (037)
14. Sociology (039)
15. Informatics Practices (065)
16. Physical Education (048)
17. Other CBSE/state-board subjects added only after their current syllabus and subject code are verified.

Subject codes and offerings must be checked against the applicable official 2026–27 curriculum before being activated; this list is a planning registry, not a claim that every subject is offered by every school.

## Required architecture
1. **Subject registry:** board + class + academic session + subject code + language + syllabus version.
2. **Curriculum adapter:** chapter/topic map, learning outcomes, prerequisites, assessment pattern and subject-specific answer rubrics.
3. **Source ingestion:** official PDFs/pages, text extraction, page/section metadata, duplicate detection and content hashes.
4. **Retrieval (RAG):** retrieve evidence only from the selected board/class/subject/session; never mix unrelated knowledge bases.
5. **AI provider adapter:** provider-neutral interface; free/local options first, paid providers optional later. Never hard-code API keys.
6. **Teacher workflow:** teach → diagnose → assess → remediate → practice → mastery.
7. **Evidence policy:** answers should cite source title and page/section when evidence is available. If evidence is missing or conflicting, say so instead of inventing.
8. **Assessment:** subject-specific rubrics; mastery remains unverified until multiple independent checks support it.
9. **Privacy:** keep full student questions/answers out of the minimal audit table; store only the approved interaction metadata.
10. **Quality gates:** per-subject tests for syllabus coverage, factual correctness, worked solutions, language clarity, citations, refusal/uncertainty and cross-subject leakage.

## Delivery phases
- **Phase 0 — curriculum inventory:** list official source URLs and map chapters for each selected subject.
- **Phase 1 — reusable subject registry and adapter contract:** no subject is marked ready until its syllabus mapping is validated.
- **Phase 2 — first pilot:** add Mathematics (041) as the first non-CS pilot, pending official source inventory and user confirmation of priority.
- **Phase 3 — science batch:** Physics, Chemistry and Biology, each with formula/numerical/lab or diagram-specific checks as applicable.
- **Phase 4 — English and Commerce/Humanities batches:** use subject-specific evaluation rubrics rather than one generic rubric.
- **Phase 5 — staged deployment:** test each subject against a versioned evaluation set before exposing it to students.

## Acceptance criteria per subject
- Current session and syllabus verified against official sources.
- All prescribed chapters/topics mapped or explicitly marked missing.
- At least one curated question set per chapter with answer key/marking scheme where officially available.
- Automated checks pass for retrieval relevance, citation grounding, answer correctness and no unsupported claims.
- A small human-reviewed evaluation set passes before the subject is labeled “pilot-ready”.
- API returns the selected subject and session clearly; it must not silently fall back to Computer Science.

## Immediate engineering next steps
1. Add a versioned subject registry (starting with CS 083 and Mathematics 041 as planned).
2. Add tests that unknown subject codes are not silently treated as CS.
3. Add curriculum/source metadata contracts before loading textbooks or question papers.
4. Verify the Supabase persistence integration and deployment branch separately from curriculum work.
