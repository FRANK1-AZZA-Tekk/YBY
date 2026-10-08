import sqlite3

import pytest

from yby.audit import AuditEntry, SQLiteRoutingAudit


def make_entry(model: str = "mock-v1", *, sensitive: bool = False) -> AuditEntry:
    return AuditEntry(
        timestamp="2026-10-08T03:00:00+00:00",
        request_id=f"req-{model}",
        provider="mock",
        model=model,
        status="success",
        router_mode="mock",
        data_class="sensitive" if sensitive else "public",
        cloud_consent=sensitive,
        sensitive_data_sent=sensitive,
        reason="unit-test",
        latency_ms=12.5,
        error_code=None,
    )


def test_sqlite_creates_database_and_table(tmp_path):
    database = tmp_path / "audit.sqlite"

    SQLiteRoutingAudit(database)

    assert database.exists()
    with sqlite3.connect(database) as connection:
        tables = connection.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='routing_audit'"
        ).fetchall()
    assert tables == [("routing_audit",)]


def test_sqlite_persists_entries_after_reopen(tmp_path):
    database = tmp_path / "audit.sqlite"
    SQLiteRoutingAudit(database).record(make_entry())

    reopened = SQLiteRoutingAudit(database)
    entries = reopened.list_entries()

    assert len(entries) == 1
    assert entries[0] == make_entry()


def test_sqlite_round_trip_preserves_all_fields(tmp_path):
    audit = SQLiteRoutingAudit(tmp_path / "audit.sqlite")
    original = make_entry("ollama-v1", sensitive=True)

    audit.record(original)
    restored = audit.list_entries()[0]

    assert restored.timestamp == original.timestamp
    assert restored.request_id == original.request_id
    assert restored.provider == original.provider
    assert restored.model == original.model
    assert restored.status == original.status
    assert restored.router_mode == original.router_mode
    assert restored.data_class == original.data_class
    assert restored.cloud_consent is True
    assert restored.sensitive_data_sent is True
    assert restored.reason == original.reason
    assert restored.latency_ms == original.latency_ms
    assert restored.error_code == original.error_code


def test_sqlite_rotates_oldest_entries(tmp_path):
    audit = SQLiteRoutingAudit(tmp_path / "audit.sqlite", max_entries=2)
    audit.record(make_entry("one"))
    audit.record(make_entry("two"))
    audit.record(make_entry("three"))

    assert [item.model for item in audit.list_entries()] == ["two", "three"]


def test_sqlite_clear_removes_all_entries(tmp_path):
    audit = SQLiteRoutingAudit(tmp_path / "audit.sqlite")
    audit.record(make_entry())

    audit.clear()

    assert audit.list_entries() == []


def test_sqlite_accepts_path_objects(tmp_path):
    audit = SQLiteRoutingAudit(tmp_path / "nested" / "audit.sqlite")

    audit.record(make_entry())

    assert len(audit.list_entries()) == 1


def test_sqlite_rejects_invalid_max_entries(tmp_path):
    with pytest.raises(ValueError, match="max_entries"):
        SQLiteRoutingAudit(tmp_path / "audit.sqlite", max_entries=0)


def test_sqlite_does_not_store_prompt_or_output_columns(tmp_path):
    database = tmp_path / "audit.sqlite"
    SQLiteRoutingAudit(database).record(make_entry())

    with sqlite3.connect(database) as connection:
        columns = {row[1] for row in connection.execute("PRAGMA table_info(routing_audit)")}

    assert "prompt" not in columns
    assert "output" not in columns
