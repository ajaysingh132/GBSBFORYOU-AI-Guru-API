# GBSBFORYOU Native Language Model v0.1 — Public Project Proposal

**Project owner:** GBSBFORYOU, Bhopal, Madhya Pradesh, India  
**Status:** Proposal / feasibility stage; funding and compute are not yet secured  
**Planning horizon:** 12 months from approved start date  
**Version:** 0.1 — 17 October 2026

## Executive summary

GBSBFORYOU proposes a transparent, Hindi-first research and prototyping programme to develop the capability to train and evaluate a small language model from randomly initialized weights, using documented and legally usable data. The first milestone is a reproducible small-model training pilot—not a claim to have built a ChatGPT-equivalent system.

The project prioritizes free and open-source software, mobile-friendly project administration, public documentation, Indian-language data provenance, reproducible experiments, and independent evaluation. Expensive GPU use will be requested only after the architecture, data plan, and training experiment are reviewed. IndiaAI Compute or other institutional compute may reduce costs if the project meets eligibility and approval requirements; no subsidy is assumed to be secured.

## Problem and public-interest rationale

- High-quality Hindi and Indian-language AI requires careful data provenance, language-specific evaluation, and practical access to compute.
- Small teams need a reproducible pathway from data governance and tokenizer design to training and independent evaluation.
- The project can invite researchers, universities, language experts, software contributors, incubators, and public institutions to review or contribute defined work packages.

## Scope for v0.1

1. Establish governance, a task register, risk register, and contribution process.
2. Survey relevant research and model-training approaches.
3. Inventory legally usable Hindi-language datasets; record license, provenance, quality, and restrictions.
4. Build a data-cleaning and deduplication pipeline.
5. Design and test a tokenizer suitable for Hindi text.
6. Specify a small decoder-only language model and reproducible training configuration.
7. Run a small smoke-test or pilot training experiment when compute is available.
8. Evaluate using held-out Hindi tests, contamination checks, baseline comparisons, and documented limitations.
9. Publish reproducible reports and a go/no-go recommendation for the next phase.

## Explicit non-goals

- No claim that v0.1 is a production-grade assistant or ChatGPT-equivalent model.
- No claim of fully indigenous technology unless architecture, weights, data, compute, ownership, and governance are separately documented.
- No training on data whose rights or permitted use are unknown.
- No production deployment, public API promises, or model-weight release before independent review.
- No paid cloud account, GPU purchase, or recurring subscription without written approval.
- No secrets, personal data, private records, or restricted datasets in the public repository.

## Team structure

Four human supervisors coordinate twelve AI-assisted roles. AI roles are workflow profiles, not twelve salaried human employees and not yet twelve deployed autonomous services.

| Human supervisor | AI roles | Accountability |
|---|---|---|
| H1 — Research & Architecture | A1 Research Scout, A2 Architecture Analyst, A3 Compute & Cost Planner | Evidence, architecture, feasibility |
| H2 — Data & Language | A4 Data Discovery, A5 Data Quality & Dedup, A6 Tokenizer & Language | Data rights, data quality, language processing |
| H3 — Model Engineering | A7 Model Implementation, A8 Training Pipeline, A9 Instruction Data | Code, training, reproducibility |
| H4 — Quality, Safety & Documentation | A10 Evaluation, A11 Safety/Privacy/License, A12 Experiment & Documentation | Independent tests, risk controls, release evidence |
| Project owner / director | All workstreams | Scope, spending, partnerships, final go/no-go |

## Deliverables and gates

| Gate | Deliverable | Exit criterion |
|---|---|---|
| G0 Governance | Team charter, work register, risk register | Owners and approval rules recorded |
| G1 Research | Evidence-based research brief | Claims have sources and limitations |
| G2 Data readiness | Dataset inventory and rights matrix | Every candidate source has a documented use basis |
| G3 Data pipeline | Cleaning, deduplication and tokenizer tests | Reproducible tests pass on a small sample |
| G4 Architecture | Model spec and compute estimate | Independent technical review completed |
| G5 Pilot | Training script, logs and checkpoint if feasible | Run can be reproduced and cost is recorded |
| G6 Evaluation | Held-out evaluation report | Results and limitations independently reviewed |
| G7 Decision | Continue / revise / stop recommendation | Human approval recorded |

## Proposed first-year budget

The detailed line-item budget is in [First-year budget](native-language-model-budget-2026.md). The current planning estimate is **₹70.8 lakh for 12 months including 10% contingency**, assuming four full-time human supervisors, shared AI tooling, four workstations, central storage and backup, and a ₹5 lakh compute reserve. This is a planning estimate based on stated salary assumptions and observed retail listings—not a vendor quotation, approved grant, or committed expenditure.

A lean pilot can be smaller if human appointments are phased and compute is obtained in-kind. The project will seek modular support rather than assuming one scheme will fund the entire first-year plan.

## Support sought

- Technical review by NLP/ML researchers and Indian-language experts.
- Dataset discovery and rights review by libraries, universities, language institutions, and researchers.
- Mentorship and incubation from an eligible technology business incubator.
- Compute credits or subsidized GPU access, subject to eligibility and approval.
- Prototype grant support, subject to scheme and incubator eligibility.
- Hardware or storage sponsorship, cloud credits, student/research collaboration, and independent evaluation.

Support is requested, not secured. The project will not represent any institution as a partner or sponsor without written confirmation.

## Governance and transparency

- Public issue tracker for tasks and review requests.
- No credentials, personal information, or restricted data in GitHub.
- Every dataset must have a provenance and license record before use.
- Training experiments must record code version, data version, configuration, compute hours, cost, and evaluation.
- AI-generated outputs are drafts until reviewed by a responsible human.
- Budget, spending approvals, and in-kind contributions will be tracked separately.
- Contributions will be accepted only under a clearly stated repository code license; dataset and model-weight licensing will be decided separately after legal review.

## Current project status

This proposal and the team/process documents are published for discussion. The existing GBSBFORYOU-AI-Guru-API codebase remains a separate deterministic API scaffold; it is not the trained language model. Do not treat it as evidence that the model has already been trained.

## How to contribute

Open a GitHub issue with your role and relevant experience, the specific work package you can review or contribute to, expected deliverable, estimated time or in-kind resource, and any institutional affiliation or conflict of interest. Do not post private data, API keys, credentials, or copyrighted datasets in issues.
