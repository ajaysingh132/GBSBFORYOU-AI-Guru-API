# AI Guru Expanded Curriculum Evaluation Matrix

## Purpose
Test breadth and instructional behavior separately from infrastructure health. A successful HTTP status is not proof of a correct, source-grounded teaching answer.

## Coverage inventory
For each available Class XII subject and syllabus session, maintain:
- official subject code/name and source URL
- chapters and subtopics expected
- resource IDs currently indexed
- missing chapters/resources
- last checked date and source version

Do not mark a subject "complete" until every expected chapter is mapped or explicitly marked unavailable.

## Per-chapter question set
Create at least one test for each applicable category:
1. Recall/definition
2. Conceptual explanation in Hindi
3. Worked example/application
4. Misconception diagnosis from an incorrect student answer
5. Short exam-style answer
6. Multi-step reasoning/problem solving where relevant
7. Source citation/page locator
8. Out-of-syllabus or insufficient-evidence handling
9. Remediation followed by a fresh concept check
10. Mastery decision based on repeated independent evidence

## Required result fields
- case_id, class_level, subject_code, session, chapter, learning_objective
- prompt and (when applicable) student answer
- expected concepts/rubric
- expected source IDs or approved source list
- actual response and citations
- factual accuracy, curriculum alignment, explanation quality, Hindi clarity
- unsupported-claim flag, citation correctness, safety/privacy flags
- pass/fail, reviewer notes, model/provider and test timestamp

## Test layers
### A. Source ingestion
- valid PDF, valid HTML, duplicate file, unreadable PDF, oversized file, unsupported MIME type
- missing author/licence metadata
- broken URL, timeout, rate limit, server error
- source update/superseded document

### B. Retrieval/RAG
- exact chapter retrieval
- similar terminology across subjects
- stale source excluded when superseded
- source citation points to the retrieved document and correct page/section
- no evidence available: abstain or clearly label general knowledge
- supplementary source not represented as official syllabus requirement

### C. Teaching and assessment
- teach, diagnose, assess, remediate, mastery
- correct and incorrect student answers
- Hindi and English prompts
- ambiguous prompts and missing prerequisites
- never claim mastery without sufficient evidence

### D. API/operations
- health checks
- request validation
- timeouts and provider failure
- rate limits/authentication before public launch
- database configured vs actually verified
- no secrets or full student answers in logs
- regression tests preserve existing endpoint contracts

## Reporting
Report per-subject and per-chapter coverage, accuracy, citation correctness, and failure types. Do not combine these into one headline score that hides missing chapters. Clearly separate automated checks from human-reviewed results.

## Current baseline note
The inspected main branch has a deterministic rule-based decision scaffold; its provider field is not evidence of a real model call. Therefore current route/HTTP tests must not be reported as proof of generative AI quality or curriculum-grounded reasoning.
