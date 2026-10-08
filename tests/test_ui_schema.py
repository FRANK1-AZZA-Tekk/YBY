from yby.ui.schemas import build_status_view, validate_ui_state


def test_build_status_view_uses_simulated_source_by_default():
    state = build_status_view(battery_percent=78, temperature_c=34.2)

    assert state["view"] == "device_status"
    assert all(item["source"] == "simulated" for item in state["components"])


def test_unknown_component_is_rejected():
    state = {
        "view": "test",
        "title": "Test",
        "status": {"level": "normal", "message": "ok"},
        "components": [{"type": "execute_code", "id": "danger"}],
    }

    try:
        validate_ui_state(state)
    except ValueError as exc:
        assert "unsupported component" in str(exc)
    else:
        raise AssertionError("invalid component was accepted")
