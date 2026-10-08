"""Provider router with explicit local-first and cloud behavior."""

import os
from typing import Literal

from .base import ProviderRequest, ProviderResult
from .mock import MockProvider
from .ollama import OllamaProvider
from .openrouter import OpenRouterProvider

ProviderMode = Literal["auto", "ollama", "mock", "openrouter"]


class ProviderRouter:
    def __init__(self, mode: ProviderMode | None = None) -> None:
        configured = mode or os.getenv("YBY_PROVIDER_MODE", "auto")
        if configured not in {"auto", "ollama", "mock", "openrouter"}:
            raise ValueError(f"unsupported provider mode: {configured}")
        self.mode: ProviderMode = configured  # type: ignore[assignment]
        self.ollama = OllamaProvider()
        self.mock = MockProvider()
        self.openrouter = OpenRouterProvider()

    def generate(self, request: ProviderRequest) -> ProviderResult:
        if self.mode == "mock":
            return self.mock.generate(request)
        if self.mode == "ollama":
            return self.ollama.generate(request)
        if self.mode == "openrouter":
            return self.openrouter.generate(request)
        result = self.ollama.generate(request)
        if result.status == "success":
            return result
        fallback = self.mock.generate(request)
        return ProviderResult(
            provider=fallback.provider,
            model=fallback.model,
            status=fallback.status,
            output=fallback.output,
            latency_ms=result.latency_ms + fallback.latency_ms,
            error_code=f"ollama_fallback:{result.error_code or 'unknown'}",
            sensitive_data_sent=False,
        )
