# Contribuindo com o YBY

## Fluxo

1. Crie uma branch a partir de `main`.
2. Faça uma alteração pequena e focada.
3. Atualize testes e documentação.
4. Execute o pipeline local.
5. Abra um pull request.
6. Aguarde o CI antes do merge.

## Verificações locais

```bash
python -m pip install ".[dev]"
python -m ruff format --check src tests
python -m ruff check src tests
python -m pytest -q --cov=yby --cov-report=term-missing
```

## Segurança

- Nunca versionar chaves ou tokens.
- Não enviar dados sensíveis para cloud sem consentimento.
- Não aceitar comandos arbitrários de modelos.
- Validar tool calls e estados de UI.
- Não alterar a `main` diretamente.

## Escopo

Cada pull request deve explicar o problema, a solução, os testes executados e as limitações conhecidas. Mudanças em `schemas/` exigem testes de aceitação e rejeição.
