"""Shared domain models for the YBY foundation."""

from dataclasses import dataclass
from typing import Literal

Route = Literal["local", "openrouter", "mock", "tool"]


@dataclass(frozen=True)
class Intent:
    text: str
    sensitive: bool = False
    complexity: Literal["simple", "complex"] = "simple"
    requires_hardware: bool = False


@dataclass(frozen=True)
class RouteDecision:
    route: Route
    reason: str


@dataclass(frozen=True)
class UIComponent:
    type: str
    id: str
    label: str | None = None
    value: object | None = None
    unit: str | None = None
    source: str = "unknown"
    risk: str | None = None
    requires_confirmation: bool = False
    allowed: bool = True
