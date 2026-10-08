"""Provider contracts used by the YBY application."""

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ProviderRequest:
    text: str
    system: str | None = None
    response_schema: dict[str, Any] | None = None
    cloud_consent: bool = False
    data_class: str = "internal"


@dataclass(frozen=True)
class ProviderResult:
    provider: str
    model: str
    status: str
    output: Any
    latency_ms: float = 0.0
    error_code: str | None = None
    sensitive_data_sent: bool = False
