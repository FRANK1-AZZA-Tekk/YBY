# YBY Intelligent UI

## Objetivo

Criar uma interface declarativa e orientada a tarefas para o ecossistema YBY. O modelo pode sugerir componentes, mas o backend valida o estado e o frontend renderiza somente componentes permitidos.

## Princípios

- Function over Form.
- Dados medidos, calculados, estimados e simulados devem ser diferenciados.
- O hardware não recebe comandos arbitrários gerados pelo modelo.
- A interface deve funcionar sem OpenRouter quando a tarefa puder ser executada localmente.
- Toda ação deve possuir um identificador explícito, política de risco e validação.

## Componentes iniciais

- `metric`
- `alert`
- `chart`
- `table`
- `timeline`
- `diagram`
- `checklist`
- `form`
- `action`
- `tabs`

## Fluxo

```text
intenção → roteador → ferramenta/provedor → estado UI → validação → frontend
```

Esta primeira versão contém somente o contrato e a base Python. A integração real com hardware, OpenRouter, Ollama e frontend será feita em etapas posteriores.
