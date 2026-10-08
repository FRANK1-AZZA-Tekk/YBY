from yby.audit import AuditEntry, SQLiteRoutingAudit


def entry(model: str) -> AuditEntry:
    return AuditEntry(
        timestamp="2026-10-08T03:00:00+00:00",
        request_id=f"req-{model}",
        provider="mock",
        model=model,
        status="success",
        router_mode="mock",
        data_class="public",
        cloud_consent=False,
        sensitive_data_sent=False,
        reason="test",
        latency_ms=1.0,
        error_code=None,
    )


def test_sqlite_audit_persists_and_rotates(tmp_path):
    audit = SQLiteRoutingAudit(tmp_path / "audit.sqlite", max_entries=2)
    audit.record(entry("one"))
    audit.record(entry("two"))
    audit.record(entry("three"))

    entries = audit.list_entries()
    assert [item.model for item in entries] == ["two", "three"]


def test_sqlite_audit_clear(tmp_path):
    audit = SQLiteRoutingAudit(tmp_path / "audit.sqlite")
    audit.record(entry("one"))
    audit.clear()

    assert audit.list_entries() == []
