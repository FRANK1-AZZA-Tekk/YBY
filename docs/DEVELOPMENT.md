# Desenvolvimento do YBY

## Ambiente

Requisitos:

- Python 3.11 ou superior.
- Ambiente virtual recomendado.

Instalação:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install ".[dev]"
```

No Windows PowerShell, ative o ambiente com:

```powershell
.venv\\Scripts\\Activate.ps1
```

## Verificações locais

```bash
python -m ruff format --check src tests
python -m ruff check src tests
python -m pytest -q --cov=src/yby --cov-report=term-missing
```

## Regras

- Não colocar chaves no código.
- Não enviar dados sensíveis para provedores cloud sem consentimento.
- Não executar comandos de hardware diretamente a partir de texto de modelo.
- Manter estados simulados identificados como `simulated`.
- Atualizar testes ao alterar o schema.
- Não fazer push direto na `main`.

## Contrato de UI

O arquivo `schemas/yby_ui.schema.json` é o contrato de dados entre backend, modelos e futuros frontends. Toda alteração deve incluir testes de compatibilidade e rejeição de entradas inválidas.

## Integração futura

OpenRouter, Ollama, FastAPI, MCP, BLE e hardware devem ser adicionados em camadas separadas, preservando o modo mock e o fallback local.
