import json
from pathlib import Path

from jsonschema import Draft202012Validator

SCHEMA_PATH = Path(__file__).parents[1] / "schemas" / "yby_ui.schema.json"


def test_ui_schema_is_valid_draft_2020_12_schema():
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)


def test_ui_schema_rejects_unknown_component_and_extra_root_field():
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    state = {
        "view": "test",
        "title": "Test",
        "status": {"level": "normal", "message": "ok"},
        "components": [{"type": "execute_code", "id": "danger"}],
        "unexpected": True,
    }

    errors = list(Draft202012Validator(schema).iter_errors(state))
    assert len(errors) >= 2


def test_ui_schema_accepts_minimal_valid_state():
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    state = {
        "view": "device_status",
        "title": "Status do YBY",
        "status": {"level": "normal", "message": "ok"},
        "components": [],
    }

    assert Draft202012Validator(schema).is_valid(state)
