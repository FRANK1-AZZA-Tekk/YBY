# Política de privacidade do YBY

## Classes

- `public`: conteúdo que não identifica pessoas nem expõe segredos.
- `internal`: arquitetura, firmware, telemetria e documentos internos do YBY.
- `sensitive`: nomes, localização, endereço, e-mail, telefone, dados financeiros ou contexto pessoal.
- `restricted`: senhas, tokens, chaves privadas, biometria e credenciais.

## Regras cloud

1. Ollama é o padrão local.
2. OpenRouter não é fallback automático.
3. `sensitive` e `restricted` são bloqueados para cloud por padrão.
4. Conteúdo público ou interno exige consentimento explícito.
5. Quando permitido, a sanitização ocorre antes do envio.
6. O usuário deve ser informado sobre a rota escolhida.

## Limitações

A classificação inicial usa regras simples por palavras-chave e não substitui revisão de segurança. Antes de produção, deve ser substituída ou complementada por classificação estruturada, políticas por fonte e auditoria.
