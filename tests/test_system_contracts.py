import json
from pathlib import Path

from jsonschema import Draft202012Validator

CONTRACTS = Path(__file__).parents[1] / "contracts"


def load_validator(name):
    schema = json.loads((CONTRACTS / name).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def assert_valid(name, payload):
    errors = list(load_validator(name).iter_errors(payload))
    assert not errors, [error.message for error in errors]


def assert_invalid(name, payload):
    assert not load_validator(name).is_valid(payload)


def test_all_contracts_are_valid_json_schema_documents():
    for path in CONTRACTS.glob("*.schema.json"):
        Draft202012Validator.check_schema(json.loads(path.read_text(encoding="utf-8")))


def test_telemetry_contract():
    assert_valid("telemetry.schema.json", {"schema_version": "1.0.0", "device_id": "yby-001", "timestamp": "2026-10-08T03:00:00Z", "source": "measured", "metrics": {"battery_percent": 78}})
    assert_invalid("telemetry.schema.json", {"schema_version": "2.0.0", "device_id": "yby-001", "timestamp": "now", "source": "measured", "metrics": {}})


def test_command_contract():
    assert_valid("command.schema.json", {"schema_version": "1.0.0", "command_id": "cmd-1", "device_id": "yby-001", "action": "set_power_mode", "risk": "low", "requires_confirmation": False, "parameters": {"mode": "economy"}})
    assert_invalid("command.schema.json", {"schema_version": "1.0.0", "command_id": "cmd-1", "device_id": "yby-001", "action": "execute_anything", "risk": "low", "requires_confirmation": False, "parameters": {}})


def test_event_contract():
    assert_valid("event.schema.json", {"schema_version": "1.0.0", "event_id": "evt-1", "event_type": "telemetry_received", "timestamp": "2026-10-08T03:00:00Z", "source": "device", "payload": {}})
    assert_invalid("event.schema.json", {"schema_version": "1.0.0", "event_id": "evt-1", "event_type": "unknown", "timestamp": "2026-10-08T03:00:00Z", "source": "device", "payload": {}})


def test_provider_result_contract():
    assert_valid("provider_result.schema.json", {"schema_version": "1.0.0", "provider": "mock", "model": "mock-v1", "status": "success", "output": {"text": "ok"}})
    assert_invalid("provider_result.schema.json", {"schema_version": "2.0.0", "provider": "mock", "model": "mock-v1", "status": "success", "output": "ok"})


def test_ui_state_contract():
    assert_valid("ui_state.schema.json", {"schema_version": "1.0.0", "view": "device_status", "title": "Status", "status": {"level": "normal", "message": "ok"}, "components": []})
    assert_invalid("ui_state.schema.json", {"schema_version": "1.0.0", "view": "device_status", "title": "Status", "status": {"level": "normal", "message": "ok"}, "components": [{"type": "execute_code", "id": "danger"}]})
