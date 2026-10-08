"""Pydantic request and response models for the local YBY API."""

from typing import Any, Literal

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: Literal["ok"]
    service: str = "yby-api"
    mode: Literal["local", "mock"] = "local"


class DeviceStatus(BaseModel):
    device_id: str = Field(min_length=1, max_length=128)
    battery_percent: float = Field(ge=0, le=100)
    temperature_c: float = Field(ge=-100, le=200)
    ble_connected: bool
    wifi_connected: bool
    power_mode: Literal["performance", "balanced", "economy"]
    firmware: str = Field(min_length=1, max_length=128)
    source: Literal["measured", "simulated"]


class IntentRequest(BaseModel):
    text: str = Field(min_length=1, max_length=4000)
    device_id: str = Field(default="yby-dev-001", min_length=1, max_length=128)


class UIStatus(BaseModel):
    level: Literal["normal", "warning", "critical"]
    message: str = Field(max_length=1000)


class UIComponent(BaseModel):
    type: Literal["metric", "alert", "chart", "table", "timeline", "diagram", "checklist", "form", "action", "tabs"]
    id: str = Field(min_length=1, max_length=128)
    label: str | None = Field(default=None, max_length=256)
    value: Any = None
    unit: str | None = Field(default=None, max_length=32)
    source: Literal["measured", "datasheet", "calculated", "estimated", "simulated", "unknown"] = "unknown"
    risk: Literal["low", "medium", "high"] | None = None
    requires_confirmation: bool = False
    allowed: bool = True


class UIState(BaseModel):
    schema_version: Literal["1.0.0"] = "1.0.0"
    view: str = Field(min_length=1, max_length=128)
    title: str = Field(min_length=1, max_length=256)
    status: UIStatus
    components: list[UIComponent]


class IntentResponse(BaseModel):
    route: Literal["local", "openrouter", "mock", "tool"]
    reason: str
    ui_state: UIState
