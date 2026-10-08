from fastapi.testclient import TestClient

from yby.api.app import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["version"] == "0.1.0"


def test_version():
    response = client.get("/version")

    assert response.status_code == 200
    assert response.json()["contract_version"] == "1.0.0"


def test_device_status_is_explicitly_simulated():
    response = client.get("/api/device/status")

    assert response.status_code == 200
    body = response.json()
    assert body["source"] == "simulated"
    assert body["device_id"] == "yby-dev-001"


def test_intent_returns_contract_validated_ui_state():
    response = client.post("/api/intent", json={"text": "Como está o YBY?"})

    assert response.status_code == 200
    body = response.json()
    assert body["route"] == "local"
    assert body["ui_state"]["schema_version"] == "1.0.0"
    assert body["ui_state"]["components"]


def test_unknown_request_field_is_rejected():
    response = client.post("/api/intent", json={"text": "status", "unexpected": True})

    assert response.status_code == 422


def test_empty_intent_is_rejected():
    response = client.post("/api/intent", json={"text": ""})

    assert response.status_code == 422
