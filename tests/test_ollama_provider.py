from unittest.mock import Mock, patch

from yby.providers import OllamaProvider, ProviderRequest


def test_ollama_provider_uses_local_configuration():
    with patch("yby.providers.ollama.ollama.Client") as client_class:
        provider = OllamaProvider(model="test-model", host="http://127.0.0.1:11434")

    assert provider.model == "test-model"
    assert provider.host == "http://127.0.0.1:11434"
    client_class.assert_called_once_with(host="http://127.0.0.1:11434")


def test_ollama_provider_parses_structured_output():
    fake_client = Mock()
    fake_client.chat.return_value = {"message": {"content": '{"answer":"ok"}'}}

    with patch("yby.providers.ollama.ollama.Client", return_value=fake_client):
        provider = OllamaProvider(model="test-model")
        result = provider.generate(ProviderRequest(text="status", response_schema={"type": "object"}))

    assert result.status == "success"
    assert result.output == {"answer": "ok"}
    fake_client.chat.assert_called_once()


def test_ollama_provider_handles_unavailable_server():
    fake_client = Mock()
    fake_client.chat.side_effect = RuntimeError("connection refused")

    with patch("yby.providers.ollama.ollama.Client", return_value=fake_client):
        result = OllamaProvider(model="test-model").generate(ProviderRequest(text="status"))

    assert result.status == "error"
    assert result.error_code == "ollama_unavailable"
