from fastapi import FastAPI
from .models import GuruRequest, GuruResponse
from .core import build_decision


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


@app.post("/v1/teach", response_model=GuruResponse)
def teach(request: GuruRequest):
    decision = build_decision(request, "teach")

    return GuruResponse(
        provider=request.provider,
        guru_decision=decision,
    )


@app.post("/v1/diagnose", response_model=GuruResponse)
def diagnose(request: GuruRequest):
    decision = build_decision(request, "diagnose")

    return GuruResponse(
        provider=request.provider,
        guru_decision=decision,
    )


@app.post("/v1/assess", response_model=GuruResponse)
def assess(request: GuruRequest):
    decision = build_decision(request, "assess")

    return GuruResponse(
        provider=request.provider,
        guru_decision=decision,
    )


@app.post("/v1/remediate", response_model=GuruResponse)
def remediate(request: GuruRequest):
    decision = build_decision(request, "remediate")

    return GuruResponse(
        provider=request.provider,
        guru_decision=decision,
    )


@app.post("/v1/mastery", response_model=GuruResponse)
def mastery(request: GuruRequest):
    decision = build_decision(request, "mastery")

    return GuruResponse(
        provider=request.provider,
        guru_decision=decision,
    )
