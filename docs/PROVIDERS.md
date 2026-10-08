# Providers de IA do YBY

## Modos

Configure `YBY_PROVIDER_MODE`:

- `auto`: tenta Ollama e usa MockProvider se o serviço local falhar.
- `ollama`: exige Ollama local; erros não são enviados para a nuvem.
- `mock`: respostas determinísticas para testes e desenvolvimento offline.

## Fluxo

```text
ProviderRouter
├── OllamaProvider
└── MockProvider
```

## Segurança

- Não existe fallback cloud nesta etapa.
- Dados não saem do computador.
- O provider não recebe ferramentas de hardware.
- O resultado é padronizado como `ProviderResult`.
- Falhas do Ollama são registradas no `error_code` do fallback.

## Próxima etapa

Adicionar OpenRouter como provider explícito, com política separada de privacidade e consentimento. Ele nunca deve ser introduzido como fallback silencioso para dados sensíveis.
