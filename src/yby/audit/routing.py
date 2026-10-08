"""Privacy-preserving routing audit log."""

from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from threading import Lock
from typing import Any
from uuid import uuid4


@dataclass(frozen=True)
class AuditEntry:
    timestamp: str
    request_id: str
    provider: str
    model: str
    status: str
    router_mode: str
    data_class: str
    cloud_consent: bool
    sensitive_data_sent: bool
    reason: str | None
    latency_ms: float
    error_code: str | None

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


class RoutingAudit:
    """Bounded in-memory audit log that never stores prompt or output content."""

    def __init__(self, max_entries: int = 500) -> None:
        if max_entries < 1:
            raise ValueError("max_entries must be positive")
        self.max_entries = max_entries
        self._entries: list[AuditEntry] = []
        self._lock = Lock()

    def record(
        self,
        *,
        provider: str,
        model: str,
        status: str,
        router_mode: str,
        data_class: str,
        cloud_consent: bool,
        sensitive_data_sent: bool,
        reason: str | None = None,
        latency_ms: float = 0.0,
        error_code: str | None = None,
    ) -> AuditEntry:
        entry = AuditEntry(
            timestamp=datetime.now(UTC).isoformat(),
            request_id=str(uuid4()),
            provider=provider,
            model=model,
            status=status,
            router_mode=router_mode,
            data_class=data_class,
            cloud_consent=cloud_consent,
            sensitive_data_sent=sensitive_data_sent,
            reason=reason,
            latency_ms=max(0.0, latency_ms),
            error_code=error_code,
        )
        with self._lock:
            self._entries.append(entry)
            del self._entries[:-self.max_entries]
        return entry

    def list_entries(self) -> list[AuditEntry]:
        with self._lock:
            return list(self._entries)

    def clear(self) -> None:
        with self._lock:
            self._entries.clear()
