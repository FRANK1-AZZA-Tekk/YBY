import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from yby.ui.schemas import build_status_view, validate_ui_state


SCHEMA_PATH = Path(__file__).parents[1] / "schemas" / "yby_ui.schema.json"


def load_schema():
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def validate_against_json_schema(state):
    validator = Draft202012Validator(load_schema())
    errors = sorted(validator.iter_errors(state), key=lambda error: list(error.path))
    if errors:
        raise AssertionError("; ".join(error.message for error in errors))


def test_build_status_view_matches_json_schema():
    state = build_status_view(battery_percent=78, temperature_c=34.2)

    validate_against_json_schema(state)

    assert state["view"] == "device_status"
    assert all(item["source"] == "simulated" for item in state["components"])


def test_all_declared_sources_are_accepted():
    for source in ("measured", "datasheet", "calculated", "estimated", "simulated", "unknown"):
        state = build_status_view(battery_percent=78, temperature_c=34.2, source=source)
        validate_against_json_schema(state)


def test_unknown_component_is_rejected_by_python_validator():
    state = {
        "view": "test",
        "title": "Test",
        "status": {"level": "normal", "message": "ok"},
        "components": [{"type": "execute_code", "id": "danger"}],
    }

    with pytest.raises(ValueError, match="unsupported component"):
        validate_ui_state(state)


def test_unknown_component_is_rejected_by_json_schema():
    state = {
        "view": "test",
        "title": "Test",
        "status": {"level": "normal", "message": "ok"},
        "components": [{"type": "execute_code", "id": "danger"}],
    }

    validator = Draft202012Validator(load_schema())
    assert not validator.is_valid(state)


def test_invalid_status_level_is_rejected_by_json_schema():
    state = {
        "view": "test",
        "title": "Test",
        "status": {"level": "unknown", "message": "invalid"},
        "components": [],
    }

    validator = Draft202012Validator(load_schema())
    assert not validator.is_valid(state)


def test_extra_root_field_is_rejected_by_json_schema():
    state = {
        "view": "test",
        "title": "Test",
        "status": {"level": "normal", "message": "ok"},
        "components": [],
        "unexpected": True,
    }

    validator = Draft202012Validator(load_schema())
    assert not validator.is_valid(state)


def test_invalid_source_is_rejected_by_json_schema():
    state = build_status_view(battery_percent=78, temperature_c=34.2)
    state["components"][0]["source"] = "invented"

    validator = Draft202012Validator(load_schema())
    assert not validator.is_valid(state)
