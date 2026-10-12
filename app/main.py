import os

import httpx
from fastapi import FastAPI
from .models import GuruRequest, GuruResponse
from .core import build_decision
from .supabase_store import save_interaction, supabase_configured


app = FastAPI(
    title="GBSBFORYOU AI Guru API",
    version="1.0.0",
    description=(
        "Education Intelligence API for teaching, diagnosis, "
        "assessment, remediation and mastery."
    ),
)


@app.get("/v1/health")
def health():
    return {
        "status": "ok",
        "api_version": "v1",
        "service": "ai-guru",
    }


@app.get("/v1/health/supabase")
def supabase_health():
    base_url = os.getenv("SUPABASE_URL", "").strip().rstrip("/")
    publishable_key = os.getenv("SUPABASE_PUBLISHABLE_KEY", "").strip()
    secret_configured = bool(
        os.getenv("SUPABASE_SECRET_KEY", "").strip()
        or os.getenv("SUPABASE_SERVICE_ROLE_KEY", "").strip()
    )

    if not base_url or not publishable_key:
        return {
            "status": "not_configured",
            "supabase_reachable": False,
            "database_writes_enabled": secret_configured,
            "database_write_status": "not_verified",
        }

    try:
        # Probe a real REST table endpoint instead of the PostgREST root.
        # limit=0 checks API access without reading student interaction data.
        response = httpx.get(
            f"{base_url}/rest/v1/ai_guru_interactions?select=id&limit=0",
            headers={"apikey": publishable_key},
            timeout=5.0,
        )

        if response.status_code in (401, 403):
            status = "authentication_error"
            reachable = True
        elif 200 <= response.status_code < 400:
            status = "connected"
            reachable = True
        elif response.status_code >= 500:
            status = "unavailable"
            reachable = False
        else:
            status = "configuration_error"
            reachable = True

        return {
            "status": status,
            "supabase_reachable": reachable,
            "database_writes_enabled": secret_configured,
            "database_write_status": (
                "configured_not_verified" if secret_configured else "not_configured"
            ),
        }
    except httpx.HTTPError:
        return {
            "status": "unavailable",
            "supabase_reachable": False,
            "database_writes_enabled": secret_configured,
            "database_write_status": (
                "configured_not_verified" if secret_configured else "not_configured"
            ),
        }


def _response(request: GuruRequest, mode: str) -> GuruResponse:
    decision = build_decision(request, mode)
    # Logging is best-effort: Supabase outages must not break teaching requests.
    save_interaction(decision)
    return GuruResponse(provider=request.provider, guru_decision=decision)


@app.post("/v1/teach", response_model=GuruResponse)
def teach(request: GuruRequest):
    return _response(request, "teach")


@app.post("/v1/diagnose", response_model=GuruResponse)
def diagnose(request: GuruRequest):
    return _response(request, "diagnose")


@app.post("/v1/assess", response_model=GuruResponse)
def assess(request: GuruRequest):
    return _response(request, "assess")


@app.post("/v1/remediate", response_model=GuruResponse)
def remediate(request: GuruRequest):
    return _response(request, "remediate")


@app.post("/v1/mastery", response_model=GuruResponse)
def mastery(request: GuruRequest):
    return _response(request, "mastery")
