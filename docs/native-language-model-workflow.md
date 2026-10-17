# GBSBFORYOU Native Language Model — End-to-End Workflow
**Version:** Draft v0.1  
**Companion document:** [Team charter and agent profiles](native-language-model-team-charter.md)

## Workflow overview

Research question → source review → data rights approval → dataset preparation → tokenizer experiment → model design and compute audit → code review → pilot training → independent evaluation → improvement loop → release decision.

Each stage has an explicit gate. A failed gate sends the work back to the responsible stage; it must not be silently bypassed.

## Stage 0 — Project setup and governance
**Lead:** Project Director; **support:** H1–H4  
**Tasks:**
- Confirm scope: first goal is a small Hindi-focused model trained from randomly initialized weights.
- Create a project decision log, risk register, task board and experiment register.
- Set compute/time/budget limits and define who can authorize a training run.
- Keep this research work separate from the production AI Guru API implementation.
**Exit criteria:** scope, roles, limits and repository rules approved.

## Stage 1 — Evidence-based research
**Lead:** A1, A2, A3; **review:** H1  
**Tasks:**
- Review primary sources for tokenizer design, small Transformer training, data processing and evaluation.
- Compare at least two plausible small-model configurations.
- Estimate parameter count, context length, token volume, memory, compute time and costs.
- Record assumptions and uncertainties.
**Exit criteria:** written architecture proposal and compute feasibility report approved by H1 and Project Director.

## Stage 2 — Data sourcing and rights
**Lead:** A4; **support:** A5, A6; **review:** H2 and H4  
**Tasks:**
- Build a dataset manifest with source URL, collection date, language, format, license/terms, size and known restrictions.
- Exclude sources with unclear or incompatible rights until clarified.
- Avoid personal/sensitive information and unauthorized scraping.
- Separate training, validation and test data; preserve provenance.
**Exit criteria:** H2 approves source manifest; H4 signs off on unresolved rights/privacy risks. No data enters training before approval.

## Stage 3 — Data preparation and tokenizer
**Lead:** A5, A6; **review:** H2  
**Tasks:**
- Normalize only where justified; preserve original data and transformation scripts.
- Detect duplicates, corrupted records, language mismatches and suspicious contamination.
- Train a tokenizer on approved data only.
- Evaluate token fertility/sequence length and coverage on Hindi, numerals, punctuation and code-mixed samples.
**Exit criteria:** versioned dataset manifest, preprocessing code, tokenizer artifact and quality report are reproducible and approved.

## Stage 4 — Architecture and implementation
**Lead:** A2, A7; **support:** A3; **review:** H1 and H3  
**Tasks:**
- Freeze a small model config only after compute estimates.
- Implement model, tokenizer interface, data loader, loss calculation and checkpoint save/load.
- Add unit tests for tensor shapes, forward pass, loss, gradient flow, save/load and deterministic configuration where applicable.
- Pin dependencies and document the execution environment.
**Exit criteria:** tests pass, parameter count is recorded, and H3 approves the code and resource budget.

## Stage 5 — Smoke test and pilot training
**Lead:** A8; **support:** A7, A3; **review:** H3  
**Tasks:**
- Run a tiny synthetic/sanitized smoke test before any meaningful training.
- Verify loss decreases on a tiny sample as a pipeline check; this is not evidence of useful language ability.
- Start a limited pilot run only after human approval.
- Track loss, tokens processed, throughput, memory, failures and estimated cost.
- Save checkpoints and verify that training can resume.
**Stop conditions:** budget/time cap reached, repeated numerical failure, data anomaly, memory failure, or unexpected cost. Stop and report rather than retry indefinitely.
**Exit criteria:** pilot completed or safely stopped with logs, checkpoint state and a documented recommendation.

## Stage 6 — Independent evaluation
**Lead:** A10; **support:** A9, A11, A12; **review:** H4  
**Tasks:**
- Evaluate only on held-out data that was not used for training or tuning.
- Report training and validation loss; use perplexity only when the tokenization/setup makes it meaningful.
- Test Hindi text continuation, basic instruction following if instruction tuning has occurred, code samples only if in scope, and known failure cases.
- Record memorization/leakage checks, harmful outputs, bias/coverage gaps and uncertainty.
**Exit criteria:** report includes methods, test-set provenance, results, examples, limitations and reproducibility instructions. No cherry-picked-only reporting.

## Stage 7 — Improvement loop
**Lead:** relevant team; **review:** corresponding supervisor  
If evaluation fails:
1. Classify failure: data, tokenizer, model capacity, optimization, instruction data, or evaluation bug.
2. Create a new task with evidence and a hypothesis.
3. Change one major variable at a time where practical.
4. Record config and dataset version; do not overwrite the previous checkpoint.
5. Repeat evaluation on the same fixed test set and, when necessary, a separate challenge set.
**Exit criteria:** measurable improvement or a clear decision to stop/change scope.

## Stage 8 — Release decision
**Lead:** Project Director; **mandatory sign-off:** H3 and H4  
A release candidate must include:
- model weights and checksum;
- exact code/config/dependency versions;
- dataset manifest and rights summary;
- training and evaluation reports;
- known limitations and intended-use statement;
- model card and reproduction steps;
- security scan and secrets check.
**Release states:** research-only / internal experiment / limited pilot / approved public release.
A model is not approved for student-facing use merely because training completed.

## Stage 9 — Integration with AI Guru (later, separate approval)
Only after the model demonstrates adequate task-specific quality:
- expose it behind a provider-neutral adapter;
- keep the current AI Guru API behavior unchanged until integration tests pass;
- compare outputs against baseline models using a fixed evaluation set;
- add timeout, fallback, logging and privacy controls;
- test in staging before any School OS integration.
The existing AI Guru API repository currently documents a deterministic rule-based scaffold; do not represent it as already running this new model.

## Daily operating cycle
1. Each human supervisor assigns bounded tasks to their three agents.
2. Agents return artifacts with sources, tests and limitations.
3. Supervisor marks each task review / blocked / accepted.
4. A12 updates the experiment and decision logs.
5. Project Director resolves cross-team blockers and approves gated actions.
6. No agent can approve its own work or spend compute beyond the approved cap.

## Required project registers
- Task register
- Source and dataset-rights manifest
- Architecture decision record
- Compute/cost estimate
- Experiment register
- Risk and issue register
- Evaluation results
- Model/checkpoint inventory
- Release checklist

## Initial milestones (duration to be estimated after compute audit)
- M0: charter and governance approved
- M1: research/compute feasibility report approved
- M2: data manifest and rights review approved
- M3: tokenizer and preprocessing pipeline tested
- M4: small model implementation passes unit tests
- M5: smoke test and first pilot training logged
- M6: independent evaluation and go/no-go decision
