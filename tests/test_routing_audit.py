from yby.audit import RoutingAudit


def test_audit_does_not_store_prompt_or_output():
    audit = RoutingAudit()
    entry = audit.record(provider="mock", model="mock-v1", status="success", router_mode="mock", data_class="public", cloud_consent=False, sensitive_data_sent=False, reason="test", latency_ms=2.5)

    data = entry.as_dict()
    assert "prompt" not in data
    assert "output" not in data
    assert data["provider"] == "mock"


def test_audit_is_bounded():
    audit = RoutingAudit(max_entries=2)
    for index in range(3):
        audit.record(provider="mock", model=str(index), status="success", router_mode="mock", data_class="public", cloud_consent=False, sensitive_data_sent=False)

    entries = audit.list_entries()
    assert len(entries) == 2
    assert entries[0].model == "1"


def test_audit_rejects_invalid_size():
    try:
        RoutingAudit(max_entries=0)
    except ValueError as exc:
        assert "max_entries" in str(exc)
    else:
        raise AssertionError("invalid audit size was accepted")
