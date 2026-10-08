"""Provider router with explicit privacy-aware cloud behavior."""

import os
from datetime import UTC, datetime
from typing import Literal
from uuid import uuid4

from yby.audit import AuditEntry, RoutingAudit, SQLiteRoutingAudit
from yby.privacy import DataClass, PrivacyPolicy, PrivacyRequest

from .base import ProviderRequest, ProviderResult
from .mock import MockProvider
from .ollama import OllamaProvider
from .openrouter import OpenRouterProvider

ProviderMode = Literal["auto", "ollama", "mock", "openrouter"]


class ProviderRouter:
    def __init__(self, mode: ProviderMode | None = None, audit=None) -> None:
        configured = mode or os.getenv("YBY_PROVIDER_MODE", "auto")
        if configured not in {"auto", "ollama", "mock", "openrouter"}:
            raise ValueError(f"unsupported provider mode: {configured}")
        self.mode: ProviderMode = configured  # type: ignore[assignment]
        self.ollama = OllamaProvider()
        self.mock = MockProvider()
        self.openrouter = OpenRouterProvider()
        self.privacy = PrivacyPolicy()
        self.audit = audit or self._build_audit()

    @staticmethod
    def _build_audit():
        backend = os.getenv("YBY_AUDIT_BACKEND", "memory")
        max_entries = int(os.getenv("YBY_AUDIT_MAX_ENTRIES", "500"))
        if backend == "sqlite":
            return SQLiteRoutingAudit(os.getenv("YBY_AUDIT_DB_PATH", "data/yby_audit.sqlite"), max_entries=max_entries)
        if backend != "memory":
            raise ValueError(f"unsupported audit backend: {backend}")
        return RoutingAudit(max_entries=max_entries)

    def _audit(self, result: ProviderResult, request: ProviderRequest, reason: str | None = None) -> None:
        entry = AuditEntry(
            timestamp=datetime.now(UTC).isoformat(),
            request_id=str(uuid4()),
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
        try:
            if isinstance(self.audit, SQLiteRoutingAudit):
                self.audit.record(entry)
            else:
                self.audit.record(
                    provider=entry.provider,
                    model=entry.model,
                    status=entry.status,
                    router_mode=entry.router_mode,
                    data_class=entry.data_class,
                    cloud_consent=entry.cloud_consent,
                    sensitive_data_sent=entry.sensitive_data_sent,
                    reason=entry.reason,
                    latency_ms=entry.latency_ms,
                    error_code=entry.error_code,
                )
        except Exception:
            pass
