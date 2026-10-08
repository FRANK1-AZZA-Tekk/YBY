from unittest.mock import Mock

from yby.providers import MockProvider, ProviderRequest, ProviderRouter, ProviderResult


def test_mock_mode_uses_mock_provider():
    router = ProviderRouter(mode="mock")
    result = router.generate(ProviderRequest(text="oi"))

    assert result.provider == "mock"
    assert result.status == "success"


def test_ollama_mode_returns_ollama_result():
    router = ProviderRouter(mode="ollama")
    router.ollama = Mock()
    router.ollama.generate.return_value = ProviderResult("ollama", "test", "success", {"answer": "ok"})

    result = router.generate(ProviderRequest(text="oi"))

    assert result.provider == "ollama"
    router.ollama.generate.assert_called_once()


def test_auto_mode_falls_back_to_mock():
    router = ProviderRouter(mode="auto")
    router.ollama = Mock()
    router.ollama.generate.return_value = ProviderResult("ollama", "test", "error", None, error_code="unavailable")
    router.mock = MockProvider()

    result = router.generate(ProviderRequest(text="oi"))

    assert result.provider == "mock"
    assert result.status == "success"
    assert result.error_code == "ollama_fallback:unavailable"
