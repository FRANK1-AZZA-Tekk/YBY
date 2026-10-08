"""Validation helpers for the YBY Intelligent UI contract."""

from typing import Any

ALLOWED_COMPONENTS = frozenset(
    {
        "metric",
        "alert",
        "chart",
        "table",
        "timeline",
        "diagram",
        "checklist",
        "form",
        "action",
        "tabs",
    }
)

ALLOWED_SOURCES = frozenset(
    {"measured", "datasheet", "calculated", "estimated", "simulated", "unknown"}
)


def validate_ui_state(state: dict[str, Any]) -> dict[str, Any]:
    """Validate the minimum contract without external dependencies."""
    for key in ("view", "title", "status", "components"):
        if key not in state:
            raise ValueError(f"missing UI field: {key}")
    if state["status"].get("level") not in {"normal", "warning", "critical"}:
        raise ValueError("invalid status level")
    if not isinstance(state["components"], list):
        raise ValueError("components must be a list")
    for component in state["components"]:
        if component.get("type") not in ALLOWED_COMPONENTS:
            raise ValueError(f"unsupported component: {component.get('type')}")
        if not component.get("id"):
            raise ValueError("component id is required")
        if component.get("source", "unknown") not in ALLOWED_SOURCES:
            raise ValueError("invalid component source")
    return state


def build_status_view(
    *, battery_percent: int, temperature_c: float, source: str = "simulated"
) -> dict[str, Any]:
    """Build a small status view suitable for the first MVP."""
    state = {
        "view": "device_status",
        "title": "Status do YBY",
        "status": {"level": "normal", "message": "Dispositivo operando normalmente"},
        "components": [
            {
                "type": "metric",
                "id": "battery",
                "label": "Bateria",
                "value": battery_percent,
                "unit": "%",
                "source": source,
            },
            {
                "type": "metric",
                "id": "temperature",
                "label": "Temperatura",
                "value": temperature_c,
                "unit": "°C",
                "source": source,
            },
        ],
    }
    return validate_ui_state(state)
