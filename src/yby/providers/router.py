"""Provider router with explicit privacy-aware cloud behavior."""

import os
from typing import Literal

from yby.audit import RoutingAudit
from yby.privacy import DataClass, PrivacyPolicy, PrivacyRequest

from .base import ProviderRequest, ProviderResult
from .mock import MockProvider
from .ollama import OllamaProvider
from .openrouter import OpenRouterProvider

ProviderMode = Literal["auto", "ollama", "mock", "openrouter"]


class ProviderRouter:
    def __init__(self, mode: ProviderMode | None = None, audit: RoutingAudit | None = None) -> None:
        configured = mode or os.getenv("YBY_PROVIDER_MODE", "auto")
        if configured not in {"auto", "ollama", "mock", "openrouter"}:
            raise ValueError(f"unsupported provider mode: {configured}")
        self.mode: ProviderMode = configured  # type: ignore[assignment]
        self.ollama = OllamaProvider()
        self.mock = MockProvider()
        self.openrouter = OpenRouterProvider()
        self.privacy = PrivacyPolicy()
        self.audit = audit or RoutingAudit()

    def _audit(self, result: ProviderResult, request: ProviderRequest, reason: str | None = None) -> None:
        try:
            self.audit.record(
                provider=result.provider,
                model=result.model,
                status=result.status,
                router_mode=self.mode,
                data_class=request.data_class,
                cloud_consent=request.cloud_consent,
                sensitive_data_sent=result.sensitive_data_sent,
                reason=reason or result.audit_reason,
                latency_ms=result.latency_ms,
                error_code=result.error_code,
            )
        except Exception:
            pass

    def generate(self, request: ProviderRequest) -> ProviderResult:
        if self.mode == "mock":
            result = self.mock.generate(request)
            self._audit(result, request, "explicit_mock_mode")
            return result
        if self.mode == "ollama":
            result = self.ollama.generate(request)
            self._audit(result, request, "explicit_ollama_mode")
            return result
        if self.mode == "openrouter":
            privacy_request = PrivacyRequest(text=request.text, data_class=DataClass(request.data_class), cloud_consent=request.cloud_consent)
            allowed, text, reason = self.privacy.prepare_cloud_request(privacy_request)
            if not allowed:
                result = ProviderResult("openrouter", "blocked", "blocked", None, error_code=reason, sensitive_data_sent=False, audit_reason=reason)
                self._audit(result, request, reason)
                return result
            cloud_request = ProviderRequest(text=text, system=request.system, response_schema=request.response_schema, cloud_consent=True, data_class=request.data_class)
            result = self.openrouter.generate(cloud_request)
            self._audit(result, request, "explicit_openrouter_mode")
            return result
        result = self.ollama.generate(request)
        if result.status == "success":
            self._audit(result, request, "auto_ollama_success")
            return result
        fallback = self.mock.generate(request)
        result = ProviderResult(
            provider=fallback.provider,
            model=fallback.model,
            status=fallback.status,
            output=fallback.output,
            latency_ms=result.latency_ms + fallback.latency_ms,
            error_code=f"ollama_fallback:{result.error_code or 'unknown'}",
            sensitive_data_sent=False,
            audit_reason="auto_ollama_failure_mock_fallback",
        )
        self._audit(result, request, result.audit_reason)
        return result
