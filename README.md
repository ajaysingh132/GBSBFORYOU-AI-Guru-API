# GBSBFORYOU AI Guru API

FastAPI service scaffold for the GBSBFORYOU AI Guru learning workflow:
teaching, diagnosis, assessment, remediation, and mastery tracking.

> **Readiness notice:** the current `app/core.py` is a deterministic,
> rule-based scaffold. The `provider` request field is not yet connected
> to a real model provider. Do not treat this version as a production AI
> tutor or claim curriculum-grounded answers until the Brain v0.8 integration,
> source citations, security controls, and staging tests are complete.

## Current endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/v1/health` | Health check |
| POST | `/v1/teach` | Teaching workflow |
| POST | `/v1/diagnose` | Diagnose learner understanding |
| POST | `/v1/assess` | Assess an answer |
| POST | `/v1/remediate` | Target a missing prerequisite |
| POST | `/v1/mastery` | Check mastery workflow |

Interactive API documentation is available at `/docs` when the app is running.

## Run locally

Python 3.11 or newer is recommended.

```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open `http://127.0.0.1:8000/docs`.

## Test

```bash
pytest -q
```

## Example request

```bash
curl -X POST http://127.0.0.1:8000/v1/teach \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Explain Python variables with an example",
    "class_level": "XII",
    "subject_code": "083",
    "session": "2026-27",
    "provider": "openai"
  }'
```

## Configuration and secrets

Copy `.env.example` to `.env` for local configuration. Never commit real
API keys. Provider variables are documented for future adapter integration;
this scaffold does not currently consume them.

## Integration roadmap

1. Integrate and test the reviewed AI Guru Brain v0.8 modules, CBSE XII CS
   curriculum adapter, RAG, and source registry without deleting source chunks.
2. Add provider-neutral model adapters and safe timeout/error handling.
3. Require evidence-backed citations and keep mastery unverified until
   assessment evidence supports a change.
4. Add authentication, rate limiting, monitoring, and privacy controls.
5. Verify deployment and staging behavior before connecting School OS.

See [launch readiness checklist](docs/launch-readiness.md).
Keep curriculum/teaching knowledge separate from other research knowledge bases.
