# Provider local Ollama

## Objetivo

O YBY usa Ollama como provider local para preservar privacidade, reduzir custo e manter funcionamento sem OpenRouter.

A API local padrão do Ollama fica em `http://localhost:11434/api`. Ela não exige autenticação quando executada localmente. [Ollama API](https://docs.ollama.com/api/introduction)

## Instalação

1. Instale o Ollama.
2. Baixe um modelo compatível, por exemplo:

```bash
ollama pull llama3.2:3b
```

3. Verifique o serviço:

```bash
ollama list
```

4. Instale o projeto YBY:

```bash
python -m pip install ".[dev]"
```

## Configuração

```bash
export YBY_OLLAMA_BASE_URL=http://localhost:11434
export YBY_OLLAMA_MODEL=llama3.2:3b
```

No Windows PowerShell:

```powershell
$env:YBY_OLLAMA_BASE_URL="http://localhost:11434"
$env:YBY_OLLAMA_MODEL="llama3.2:3b"
```

## Saída estruturada

O provider usa `format` com JSON Schema. O Ollama suporta structured outputs usando o campo `format`, permitindo restringir a saída do modelo a um schema previsível. [Ollama Structured Outputs](https://docs.ollama.com/capabilities/structured-outputs)

## Segurança

- O provider aponta para localhost por padrão.
- Não envia dados para a nuvem.
- O modelo não recebe ferramentas de hardware nesta etapa.
- Respostas inválidas são convertidas em erro controlado.
- O fallback ainda é o modo mock da API.

## Limitações

A API `/api/intent` ainda usa o roteador local e a UI simulada. O método `ask_local_model` prepara a integração sem substituir o fluxo principal antes de adicionarmos `ProviderResult` completo e fallback explícito.
