from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def sample_request(**overrides):
    payload = {
        "question": "Explain Python variables with an example",
        "class_level": "XII",
        "subject_code": "083",
        "session": "2026-27",
        "provider": "openai",
    }
    payload.update(overrides)
    return payload


def test_health_endpoint():
    response = client.get("/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["service"] == "ai-guru"


def test_teach_contract():
    response = client.post("/v1/teach", json=sample_request())
    assert response.status_code == 200
    body = response.json()
    assert body["api_version"] == "v1"
    assert body["provider"] == "openai"
    decision = body["guru_decision"]
    assert decision["class_level"] == "XII"
    assert decision["subject_code"] == "083"
    assert decision["session"] == "2026-27"
    assert decision["mode"] == "teach"
    assert decision["mastery_status"] == "not_yet_verified"
    assert len(decision["teaching_plan"]) >= 1


def test_all_learning_routes_return_expected_mode():
    routes = {
        "/v1/teach": "teach",
        "/v1/diagnose": "diagnose",
        "/v1/assess": "assess",
        "/v1/remediate": "remediate",
        "/v1/mastery": "mastery",
    }
    for route, expected_mode in routes.items():
        response = client.post(route, json=sample_request())
        assert response.status_code == 200, route
        assert response.json()["guru_decision"]["mode"] == expected_mode


def test_empty_question_is_rejected():
    response = client.post("/v1/teach", json=sample_request(question=""))
    assert response.status_code == 422


def test_unknown_provider_is_rejected():
    response = client.post(
        "/v1/teach",
        json=sample_request(provider="unknown-provider"),
    )
    assert response.status_code == 422


def test_question_length_is_limited():
    response = client.post(
        "/v1/teach",
        json=sample_request(question="x" * 12001),
    )
    assert response.status_code == 422
