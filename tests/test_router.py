from yby.core.models import Intent
from yby.router import HybridRouter


def test_sensitive_intent_stays_local():
    decision = HybridRouter().decide(Intent("dados pessoais", sensitive=True))

    assert decision.route == "local"


def test_hardware_intent_uses_controlled_tool():
    decision = HybridRouter().decide(Intent("ler status", requires_hardware=True))

    assert decision.route == "tool"


def test_complex_non_sensitive_intent_can_use_openrouter():
    decision = HybridRouter().decide(Intent("diagnóstico complexo", complexity="complex"))

    assert decision.route == "openrouter"
