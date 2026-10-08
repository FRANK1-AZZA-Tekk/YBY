"""Provider router with explicit privacy-aware cloud behavior."""

import os
from typing import Literal

from yby.privacy import DataClass, PrivacyPolicy, PrivacyRequest

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
        self.privacy = PrivacyPolicy()

    def generate(self, request: ProviderRequest) -> ProviderResult:
        if self.mode == "mock":
            return self.mock.generate(request)
        if self.mode == "ollama":
            return self.ollama.generate(request)
        if self.mode == "openrouter":
            privacy_request = PrivacyRequest(
                text=request.text,
                data_class=DataClass(request.data_class),
                cloud_consent=request.cloud_consent,
            )
            allowed, text, reason = self.privacy.prepare_cloud_request(privacy_request)
            if not allowed:
                return ProviderResult("openrouter", "blocked", "blocked", None, error_code=reason, sensitive_data_sent=False)
            cloud_request = ProviderRequest(
                text=text,
                system=request.system,
                response_schema=request.response_schema,
                cloud_consent=True,
                data_class=request.data_class,
            )
            return self.openrouter.generate(cloud_request)
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
