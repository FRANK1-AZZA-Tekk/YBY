# YBY Routing Policy

## Ordem de decisão

1. Dados sensíveis permanecem locais.
2. Telemetria é obtida por ferramentas controladas pelo backend.
3. Tarefas simples usam regras ou provedor local.
4. Tarefas complexas podem usar OpenRouter.
5. Ações de hardware exigem validação e, quando necessário, confirmação.

## Rotas iniciais

| Caso | Rota |
| --- | --- |
| Dados sensíveis | `local` |
| Tarefa simples | `local` |
| Raciocínio complexo | `openrouter` |
| Teste automatizado | `mock` |
| Hardware | `tool` + política |

## Fora do escopo desta etapa

- Chaves de API.
- Chamadas reais ao OpenRouter.
- Comunicação BLE.
- Controle de hardware.
- Persistência de telemetria.
- Deploy público.
