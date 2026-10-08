from unittest.mock import Mock

from yby.providers import MockProvider, ProviderRequest, ProviderRouter, ProviderResult


def test_mock_mode_uses_mock_provider():
    result = ProviderRouter(mode="mock").generate(ProviderRequest(text="oi"))

    assert result.provider == "mock"
    assert result.status == "success"


def test_ollama_mode_returns_ollama_result():
    router = ProviderRouter(mode="ollama")
    router.ollama = Mock()
    router.ollama.generate.return_value = ProviderResult("ollama", "test", "success", {"answer": "ok"})

    result = router.generate(ProviderRequest(text="oi"))

    assert result.provider == "ollama"
    router.ollama.generate.assert_called_once()


def test_openrouter_mode_returns_openrouter_result():
    router = ProviderRouter(mode="openrouter")
    router.openrouter = Mock()
    router.openrouter.generate.return_value = ProviderResult("openrouter", "test", "success", {"answer": "ok"})

    result = router.generate(ProviderRequest(text="oi"))

    assert result.provider == "openrouter"
    router.openrouter.generate.assert_called_once()


def test_auto_mode_falls_back_to_mock_not_cloud():
    router = ProviderRouter(mode="auto")
    router.ollama = Mock()
    router.ollama.generate.return_value = ProviderResult("ollama", "test", "error", None, error_code="unavailable")
    router.openrouter = Mock()
    router.mock = MockProvider()

    result = router.generate(ProviderRequest(text="oi"))

    assert result.provider == "mock"
    assert result.status == "success"
    router.openrouter.generate.assert_not_called()


def test_invalid_mode_is_rejected():
    try:
        ProviderRouter(mode="invalid")
    except ValueError as exc:
        assert "unsupported provider mode" in str(exc)
    else:
        raise AssertionError("invalid provider mode was accepted")
