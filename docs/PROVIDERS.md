# Providers de IA do YBY

## Modos

Configure `YBY_PROVIDER_MODE`:

- `auto`: tenta Ollama e usa MockProvider se o serviço local falhar.
- `ollama`: exige Ollama local; erros não são enviados para a nuvem.
- `mock`: respostas determinísticas para testes e desenvolvimento offline.
- `openrouter`: usa OpenRouter somente quando selecionado explicitamente.

## Fluxo

```text
ProviderRouter
├── OllamaProvider
├── MockProvider
└── OpenRouterProvider (explícito)
```

## OpenRouter

O provider usa a API compatível com OpenAI em `https://openrouter.ai/api/v1`. O modelo é configurado por `YBY_OPENROUTER_MODEL` e a chave por `OPENROUTER_API_KEY`.

Quando há schema de resposta, o provider envia `response_format` com `json_schema` e exige providers que suportem os parâmetros solicitados usando `require_parameters: true`.

## Segurança

- OpenRouter não é fallback automático.
- Dados sensíveis não devem ser enviados.
- A chave deve existir somente em variável de ambiente.
- O modo `auto` nunca escala silenciosamente para cloud.
- Falhas retornam `ProviderResult` controlado.

## Próxima etapa

Adicionar política explícita de sanitização e consentimento antes de permitir que o aplicativo selecione `openrouter` fora do ambiente de desenvolvimento.
