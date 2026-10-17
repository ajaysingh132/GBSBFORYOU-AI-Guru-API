# GBSBFORYOU-LM — 12 AI Agent Operating Manual
**Version:** 0.2 (operational draft)  
**Status:** Defined roles and operating rules; agents are not yet deployed as autonomous services.  
**Parent documents:** [Team Charter](native-language-model-team-charter.md) · [End-to-end Workflow](native-language-model-workflow.md)

## 1. Purpose and authority
This manual turns the 12 agent profiles into an operational system aligned to four human supervisors. Each agent must produce an inspectable artifact, cite its sources where applicable, report uncertainty, and hand off work in a defined format. Agents do not approve their own work, authorize spending, accept dataset rights, or release a model.

### Human supervision map
- **H1 Research & Architecture Supervisor:** A1, A2, A3
- **H2 Data & Language Supervisor:** A4, A5, A6
- **H3 Model Engineering Supervisor:** A7, A8, A9
- **H4 Quality, Safety & Documentation Supervisor:** A10, A11, A12

The Project Director sets priorities and approves major gates. H4 can block a release on quality, privacy, licensing, or documentation grounds.

## 2. Standard agent cycle
Every task follows this sequence:
1. **Receive:** Read task ID, objective, scope, deadline/priority, approved inputs, and forbidden actions.
2. **Plan:** Return a short plan and list missing inputs before doing costly or irreversible work.
3. **Execute:** Work only within scope; use approved sources and tools.
4. **Validate:** Run relevant checks; distinguish observed facts from assumptions.
5. **Report:** Return artifact links/paths, evidence, tests, limitations, risks, and recommendation.
6. **Handoff:** Send the result to the named human supervisor and downstream agent.
7. **Revise:** Address review comments; preserve earlier versions and record changes.

### Required task record
- `task_id`
- `title`
- `assigned_agent`
- `human_supervisor`
- `objective`
- `approved_inputs`
- `deliverable`
- `acceptance_checks`
- `risk_level` (low / medium / high)
- `status` (backlog / ready / in_progress / review / blocked / accepted / rejected)
- `evidence_and_sources`
- `tests_run`
- `limitations_and_unknowns`
- `handoff_to`
- `human_decision`

An agent may recommend acceptance, but only its assigned human supervisor can set `accepted`. Any missing source, rights question, safety concern, unexpected cost, or failed test must be stated explicitly.

## 3. Agent-by-agent operating procedures

### A1 — Research Scout | Supervisor H1
**Goal:** Establish evidence-backed technical knowledge for the model project.
**Trigger:** New research question, architecture decision, or unresolved technical claim.
**Procedure:** Clarify the question → search primary documentation/papers → check date and scope → compare at least two sources for consequential claims → summarize evidence and disagreement → list implications and unknowns.
**Deliverable:** `research-brief.md` with question, findings, citations/URLs, source dates, confidence, open questions, and recommended next decision.
**Acceptance checks:** Every key technical claim has a source; source is actually relevant; facts and assumptions are separated; no unsupported claim about Indian government support or free compute.
**Handoff:** A2 and A3; H1 approves.

### A2 — Architecture Analyst | Supervisor H1
**Goal:** Propose a small model design that fits the declared use case and available compute.
**Trigger:** A1 research brief and current compute constraints are available.
**Procedure:** State intended capability → compare candidate architectures/configurations → estimate parameters and context length → identify tokenizer/data assumptions → identify failure modes → recommend a smallest viable pilot.
**Deliverable:** `architecture-proposal.md` plus machine-readable config draft.
**Acceptance checks:** Alternatives and trade-offs recorded; parameter count reproducible; training-data and compute assumptions explicit; proposal does not claim a useful assistant before evaluation.
**Handoff:** A3, A7, A8; H1 approves.

### A3 — Compute & Cost Planner | Supervisor H1
**Goal:** Determine whether the proposed experiment can be run within approved compute, time, storage, and cost limits.
**Trigger:** Draft architecture/config exists or resource assumptions change.
**Procedure:** Estimate model/optimizer/activation memory, dataset storage, checkpoints, throughput uncertainty and run duration → identify device requirements → compare available execution options → set budget and stop conditions.
**Deliverable:** `compute-feasibility.md` with assumptions, min/likely/high scenarios, limits, and stop conditions.
**Acceptance checks:** No fabricated performance guarantees; current resource availability is verified; free-tier assumptions are clearly marked; human budget approval is recorded.
**Handoff:** H1, H3, A8. No training run begins without human authorization.

### A4 — Data Discovery Agent | Supervisor H2
**Goal:** Find candidate data sources appropriate for Hindi-focused pretraining.
**Trigger:** Scope and language priorities approved.
**Procedure:** Search official/open repositories and dataset cards → record source, license, language, format, size, collection date, restrictions, personal-data concerns and provenance → flag ambiguity rather than assume permission.
**Deliverable:** `data-source-manifest.csv` and a rights-questions list.
**Acceptance checks:** Each source has traceable provenance; license/terms are linked; ambiguous or incompatible sources are marked blocked; no unauthorized scraping.
**Handoff:** A5 and H2; A11 reviews rights/privacy risks.

### A5 — Data Quality & Dedup Agent | Supervisor H2
**Goal:** Make approved data consistent, traceable, and fit for training.
**Trigger:** H2 has approved the candidate sources for processing.
**Procedure:** Validate file formats → measure encoding and language mix → detect exact/near duplicates → identify empty, malformed, spam-like or sensitive records → create deterministic transformations → preserve source IDs and exclusion reasons.
**Deliverable:** preprocessing scripts, quality report, dataset manifest/version and exclusion log.
**Acceptance checks:** Input remains recoverable; transformation steps are reproducible; train/validation/test separation is respected; no unapproved source enters output.
**Handoff:** A6, A8 and H2.

### A6 — Tokenizer & Language Agent | Supervisor H2
**Goal:** Evaluate tokenization for Hindi Devanagari and approved language/code-mixed examples.
**Trigger:** An approved sample dataset is available.
**Procedure:** Define normalization policy → compare tokenizer candidates → measure vocabulary coverage, token count/sequence length and unusual splits → inspect edge cases (matras, nukta, punctuation, numerals, English mixing) → document limitations.
**Deliverable:** tokenizer configuration/artifact, test examples, coverage report and usage instructions.
**Acceptance checks:** Tests are repeatable; original text handling is documented; no claim that tokenizer alone creates language understanding.
**Handoff:** A7 and A8; H2 approves.

### A7 — Model Implementation Agent | Supervisor H3
**Goal:** Implement the approved model architecture as tested code.
**Trigger:** H1 approves architecture and H3 approves implementation scope.
**Procedure:** Implement model and config → add unit tests for tensor shapes, forward pass, loss, gradient flow and save/load → pin dependencies → document initialization method → submit code for review.
**Deliverable:** versioned model code, config, tests, dependency list and parameter-count output.
**Acceptance checks:** Tests pass in a clean environment; weights are randomly initialized for a from-scratch run; no pretrained model weights are silently loaded; secrets are absent.
**Handoff:** A8 and H3.

### A8 — Training Pipeline Agent | Supervisor H3
**Goal:** Build a bounded, reproducible training run with logs and recovery.
**Trigger:** Approved dataset/tokenizer/model code and compute budget are available.
**Procedure:** Validate inputs → run a tiny smoke test → verify loss/gradient/checkpoint behavior → request human approval for pilot → train within time/cost limits → log config, seed where relevant, token count, loss, throughput, memory and errors → verify resume.
**Deliverable:** training script/config, run log, checkpoint inventory/checksums, resource summary and stop/continue recommendation.
**Acceptance checks:** No unapproved cloud enrollment or spend; stop conditions work; checkpoint can be loaded; training/validation data are not accidentally mixed.
**Handoff:** A10 and H3. Stop immediately on budget cap, data anomaly, repeated numerical failure, or unexpected cost.

### A9 — Instruction Data Agent | Supervisor H3; co-review H4
**Goal:** Prepare a small, lawful instruction-format dataset only after base-model pretraining is validated.
**Trigger:** Project Director authorizes instruction-data phase.
**Procedure:** Define target tasks → create/collect only permitted examples → validate schema and answer quality → separate training and evaluation sets → check overlap with held-out tests → document synthetic versus human-authored material.
**Deliverable:** versioned instruction dataset specification, quality report and split manifest.
**Acceptance checks:** Rights/provenance are documented; held-out evaluation items are excluded from training; generated examples are labelled as synthetic; H4 review completed.
**Handoff:** A8 and A10.

### A10 — Evaluation Agent | Supervisor H4
**Goal:** Independently measure model behavior and report limitations.
**Trigger:** A checkpoint and fixed evaluation protocol are available.
**Procedure:** Verify checkpoint/config identity → run held-out tests → report loss/perplexity only when meaningful → test Hindi continuation and approved task-specific abilities → inspect failures, leakage and variability → compare only against a documented baseline.
**Deliverable:** `evaluation-report.md` with commands, metrics, sample failures, limitations and reproducibility details.
**Acceptance checks:** No cherry-picking; test-set provenance is known; evaluation data were not used for training/tuning; conclusions match evidence.
**Handoff:** H4, A2, A7 and A8. H4 determines whether results meet the agreed gate.

### A11 — Safety, Privacy & License Agent | Supervisor H4
**Goal:** Detect risks before data use, external execution, or release.
**Trigger:** New dataset, dependency, external service, release candidate, or reported incident.
**Procedure:** Review license/provenance/privacy notes → scan repository changes for secrets → check data minimization and retention → record model-use risks → propose mitigations → escalate unclear legal questions to a qualified human.
**Deliverable:** risk register, findings with severity, remediation owner and release checklist.
**Acceptance checks:** Findings have evidence and severity; unresolved high risks block progression; agent does not claim to provide final legal advice.
**Handoff:** H4 and relevant supervisor; critical issues go to Project Director.

### A12 — Experiment & Documentation Agent | Supervisor H4
**Goal:** Keep every project decision and experiment traceable.
**Trigger:** Any task reaches review/accepted, a run starts/stops, or a decision changes.
**Procedure:** Record task ID and commit/version → link dataset/config/checkpoint IDs → record actual run results (never estimates as facts) → update changelog, model-card draft and milestone board → identify missing artifacts.
**Deliverable:** experiment register, decision log, changelog and reproducibility checklist.
**Acceptance checks:** Entries point to real artifacts; dates and versions are consistent; failed runs are retained in the record; no results are invented.
**Handoff:** All supervisors and Project Director.

## 4. Team handoffs and dependency graph
A1 → A2 → A3 → H1 architecture/compute gate  
A4 → H2/A11 rights gate → A5 → A6 → H2 data/tokenizer gate  
A2 + A3 + approved data/tokenizer → A7 → A8 → H3 pilot-training gate  
A9 begins only when separately authorized; A10 evaluates; A11 reviews risks; A12 records evidence  
A10 + A11 + A12 → H4 quality/release gate → Project Director go/no-go

A downstream agent must return `blocked` if its required input is not approved. It must not invent missing data or bypass a gate.

## 5. Human review and escalation rules
- **Low risk:** routine, reversible analysis or code/test generation within approved scope; supervisor reviews the artifact.
- **Medium risk:** dataset transformation, dependency change, model config change, or evaluation protocol change; explicit supervisor approval before execution.
- **High risk:** spending money, enrolling an external service, uploading private data, changing production services, deleting data, publishing a model, or student-facing deployment; explicit Project Director approval plus relevant supervisor sign-off.
- **Stop and escalate:** unclear data rights, secret exposure, unexpected costs, sensitive personal data, reproducible test failure, data leakage, or a claim unsupported by evidence.
- Never place secrets or private data in issues, commits, logs, or agent prompts.

## 6. Cadence and reporting
**Per task:** report when blocked, when an artifact is ready for review, and when a risk appears.  
**Daily (or each active work session):** each supervisor reviews their three agents' status and records blockers.  
**Milestone review:** H1–H4 submit a concise status: completed evidence, failed checks, unresolved risks, next actions, resource use, and a go/no-go recommendation.  
No schedule implies continuous autonomous execution; actual automation must be implemented and tested separately.

## 7. Standard agent response template
- Task ID / agent / supervisor:
- Status:
- Objective:
- Work completed:
- Artifacts and commit links:
- Evidence and sources:
- Tests/checks run:
- Results:
- Assumptions and limitations:
- Risks/blockers:
- Recommended next action:
- Human decision required:

## 8. Definition of operational readiness
The 12-agent framework is operational only when:
1. each role has a prompt/config and bounded tool permissions;
2. tasks are assigned through a shared tracker;
3. artifacts are saved to version control or a controlled data store;
4. human review gates are enforced;
5. tests and logs are visible;
6. failure, stop and escalation behavior has been tested.

This document defines the operating design; it does not itself instantiate or run the agents.
