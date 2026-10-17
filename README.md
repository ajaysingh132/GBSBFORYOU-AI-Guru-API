# GBSBFORYOU AI Guru API and Native Language Model Research

FastAPI service scaffold for the GBSBFORYOU AI Guru learning workflow, alongside a public planning track for a Hindi-first language-model feasibility project.

> **Readiness notice:** the current app/core.py is a deterministic, rule-based scaffold. The provider request field is not yet connected to a real model provider. This repository does **not** contain a trained GBSBFORYOU foundation model. Do not claim production AI tutor or trained-model status until verified by code, training artifacts, and independent evaluation.

## Current API endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /v1/health | Health check |
| POST | /v1/teach | Teaching workflow |
| POST | /v1/diagnose | Diagnose learner understanding |
| POST | /v1/assess | Assess an answer |
| POST | /v1/remediate | Target a missing prerequisite |
| POST | /v1/mastery | Check mastery workflow |

Interactive API documentation is available at /docs when the app is running.

## Run locally

Python 3.11 or newer is recommended.

~~~bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
~~~

Then open http://127.0.0.1:8000/docs.

## Test

~~~bash
pytest -q
~~~

## Native Language Model v0.1 — project documents

The research/prototype track is at the proposal and feasibility stage. Its first goal is a reproducible small-model training pilot using documented, legally usable data—not a ChatGPT-equivalent product.

- [Project proposal](docs/native-language-model-project-proposal.md)
- [First-year budget (12 months)](docs/native-language-model-budget-2026.md)
- [Expert, collaborator and government support plan](docs/collaboration-and-government-support.md)
- [Hardware, central storage and data governance](docs/hardware-central-storage-plan.md)
- [12-agent operating manual](docs/native-language-model-agent-operations.md)
- [Team charter](docs/native-language-model-team-charter.md)
- [Development workflow and review gates](docs/native-language-model-workflow.md)
- [Feasibility issue #5](https://github.com/ajaysingh132/GBSBFORYOU-AI-Guru-API/issues/5)
- [Call for expert reviewers and institutional partners](https://github.com/ajaysingh132/GBSBFORYOU-AI-Guru-API/issues/6)

## Example request

~~~bash
curl -X POST http://127.0.0.1:8000/v1/teach \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Explain Python variables with an example",
    "class_level": "XII",
    "subject_code": "083",
    "session": "2026-27",
    "provider": "openai"
  }'
~~~

## Configuration and secrets

Copy .env.example to .env for local configuration. Never commit real API keys. Provider variables are documented for future adapter integration; this scaffold does not currently consume them.

## Integration roadmap

1. Integrate and test the reviewed AI Guru Brain v0.8 modules, CBSE XII CS curriculum adapter, RAG, and source registry without deleting source chunks.
2. Add provider-neutral model adapters and safe timeout/error handling.
3. Require evidence-backed citations and keep mastery unverified until assessment evidence supports a change.
4. Add authentication, rate limiting, monitoring, and privacy controls.
5. Verify deployment and staging behavior before connecting School OS.

See docs/launch-readiness.md. Keep curriculum/teaching knowledge separate from other research knowledge bases.

## Contribution and licensing

Please use GitHub Issues for scoped tasks and technical reviews. Do not upload secrets, private data, or unlicensed datasets. Code, datasets, and model weights may need different licensing decisions. Check the repository's current license status and obtain owner/legal review before claiming that any part is open-source or inviting reuse under a license.
