"""Optional SQLite persistence for privacy-preserving routing audit."""

import sqlite3
from pathlib import Path
from threading import Lock

from .routing import AuditEntry


class SQLiteRoutingAudit:
    def __init__(self, path: str | Path, max_entries: int = 500) -> None:
        if max_entries < 1:
            raise ValueError("max_entries must be positive")
        self.path = Path(path)
        self.max_entries = max_entries
        self._lock = Lock()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self._connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS routing_audit (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    request_id TEXT NOT NULL,
                    provider TEXT NOT NULL,
                    model TEXT NOT NULL,
                    status TEXT NOT NULL,
                    router_mode TEXT NOT NULL,
                    data_class TEXT NOT NULL,
                    cloud_consent INTEGER NOT NULL,
                    sensitive_data_sent INTEGER NOT NULL,
                    reason TEXT,
                    latency_ms REAL NOT NULL,
                    error_code TEXT
                )
                """
            )
            connection.commit()

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.path)

    def record(self, entry: AuditEntry) -> AuditEntry:
        with self._lock, self._connect() as connection:
            connection.execute(
                """
                INSERT INTO routing_audit
                (timestamp, request_id, provider, model, status, router_mode,
                 data_class, cloud_consent, sensitive_data_sent, reason,
                 latency_ms, error_code)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    entry.timestamp,
                    entry.request_id,
                    entry.provider,
                    entry.model,
                    entry.status,
                    entry.router_mode,
                    entry.data_class,
                    int(entry.cloud_consent),
                    int(entry.sensitive_data_sent),
                    entry.reason,
                    entry.latency_ms,
                    entry.error_code,
                ),
            )
            connection.execute(
                """
                DELETE FROM routing_audit
                WHERE id NOT IN (
                    SELECT id FROM routing_audit ORDER BY id DESC LIMIT ?
                )
                """,
                (self.max_entries,),
            )
            connection.commit()
        return entry

    def list_entries(self) -> list[AuditEntry]:
        with self._lock, self._connect() as connection:
            rows = connection.execute(
                """
                SELECT timestamp, request_id, provider, model, status, router_mode,
                       data_class, cloud_consent, sensitive_data_sent, reason,
                       latency_ms, error_code
                FROM routing_audit ORDER BY id ASC
                """
            ).fetchall()
        return [
            AuditEntry(
                timestamp=row[0], request_id=row[1], provider=row[2], model=row[3],
                status=row[4], router_mode=row[5], data_class=row[6],
                cloud_consent=bool(row[7]), sensitive_data_sent=bool(row[8]),
                reason=row[9], latency_ms=row[10], error_code=row[11],
            )
            for row in rows
        ]

    def clear(self) -> None:
        with self._lock, self._connect() as connection:
            connection.execute("DELETE FROM routing_audit")
            connection.commit()
