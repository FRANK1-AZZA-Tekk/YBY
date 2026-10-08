# Contratos compartilhados

## Objetivo

Definir formatos estáveis entre o núcleo Python, o frontend, o aplicativo, o firmware e providers de IA.

## Contratos previstos

```text
contracts/
├── ui_state.schema.json
├── telemetry.schema.json
├── command.schema.json
├── event.schema.json
└── provider_result.schema.json
```

## Regras gerais

- Todo contrato deve ter versão.
- Campos desconhecidos devem ser rejeitados ou explicitamente marcados como extensíveis.
- Dados devem informar sua origem: `measured`, `calculated`, `estimated`, `simulated` ou `unknown`.
- Ações devem ter identificador, risco e política de confirmação.
- O frontend não é fonte de verdade da telemetria.
- O modelo não executa comandos diretamente.

## Fluxo de dados

```text
ESP32 → telemetria → backend → política → provider/UI
usuário → intenção → router → ferramenta/provider → estado validado
ação → validação → confirmação → backend → comando permitido → ESP32
```

## Evolução

Alterações incompatíveis exigem nova versão do contrato, testes de migração e documentação. O schema atual da Intelligent UI permanece a primeira referência para o estado visual.
