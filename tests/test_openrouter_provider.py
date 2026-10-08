from unittest.mock import Mock, patch

from yby.providers import OpenRouterProvider, ProviderRequest


def test_openrouter_requires_api_key():
    with patch.dict("os.environ", {}, clear=True):
        provider = OpenRouterProvider(model="test-model")

    result = provider.generate(ProviderRequest(text="oi"))

    assert result.status == "blocked"
    assert result.error_code == "missing_openrouter_api_key"
    assert result.sensitive_data_sent is False


def test_openrouter_parses_structured_output():
    fake_response = Mock()
    fake_response.choices = [Mock(message=Mock(content='{"answer":"ok"}'))]

    with patch.dict("os.environ", {"OPENROUTER_API_KEY": "test-key"}), patch("yby.providers.openrouter.OpenAI") as openai:
        openai.return_value.chat.completions.create.return_value = fake_response
        provider = OpenRouterProvider(model="test-model")
        result = provider.generate(ProviderRequest(text="oi", response_schema={"type": "object"}))

    assert result.status == "success"
    assert result.output == {"answer": "ok"}
    call = openai.return_value.chat.completions.create.call_args.kwargs
    assert call["extra_body"]["provider"]["require_parameters"] is True


def test_openrouter_does_not_mark_blocked_request_as_sent():
    with patch.dict("os.environ", {}, clear=True):
        result = OpenRouterProvider(model="test-model").generate(ProviderRequest(text="oi"))

    assert result.sensitive_data_sent is False
