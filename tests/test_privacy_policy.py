from yby.privacy import DataClass, PrivacyPolicy, PrivacyRequest


def test_classifies_restricted_data():
    assert PrivacyPolicy().classify("qual é minha senha?") == DataClass.RESTRICTED


def test_classifies_sensitive_data():
    assert PrivacyPolicy().classify("encontre meu endereço") == DataClass.SENSITIVE


def test_cloud_requires_consent():
    request = PrivacyRequest("pergunta pública", data_class=DataClass.PUBLIC)
    allowed, _, reason = PrivacyPolicy().prepare_cloud_request(request)

    assert allowed is False
    assert reason == "cloud_not_authorized"


def test_cloud_sanitizes_authorized_request():
    request = PrivacyRequest("analise o email do projeto", data_class=DataClass.PUBLIC, cloud_consent=True)
    allowed, text, reason = PrivacyPolicy().prepare_cloud_request(request)

    assert allowed is True
    assert "[REDACTED]" in text
    assert reason == "authorized_sanitized"
