# Arquitetura do YBY

## Estado atual

O repositório contém dois namespaces Python:

- `yby`: núcleo novo do Intelligent UI, roteamento e contratos.
- `yby_zero`: núcleo anterior, mantido temporariamente para compatibilidade.

Novas funcionalidades devem ser implementadas em `yby`. O namespace `yby_zero` não deve receber novas integrações paralelas sem uma decisão arquitetural registrada.

## Camadas planejadas

```text
interfaces → application → domain → infrastructure
```

- `domain`: intenções, decisões de rota, ações e estado da UI.
- `application`: orquestração e políticas.
- `infrastructure`: Ollama, OpenRouter, telemetria, persistência e observabilidade.
- `interfaces`: API, CLI, MCP e futuras interfaces móveis.

## Regras de fronteira

- O modelo não controla hardware diretamente.
- Ferramentas retornam dados estruturados.
- A UI é gerada a partir de schema validado.
- Dados sensíveis ficam locais por padrão.
- OpenRouter é provider substituível, não dependência do domínio.
- O modo mock deve continuar funcionando sem internet.

## Próxima integração

A próxima camada deve ser um provider mock e uma API local. OpenRouter e hardware somente depois que contratos, testes e políticas estiverem estáveis.
