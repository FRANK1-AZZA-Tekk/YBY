# Auditoria de roteamento

## Objetivo

Registrar decisões do roteador sem armazenar prompts, respostas, chaves ou dados pessoais.

## Campos

- timestamp UTC;
- request_id;
- provider;
- modelo;
- status;
- modo do roteador;
- classe do dado;
- consentimento cloud;
- indicador de envio sensível;
- motivo;
- latência;
- código de erro.

## Armazenamento

A implementação inicial usa memória e possui limite configurável de registros. Isso é adequado para desenvolvimento, mas não é persistente nem suficiente para auditoria de produção.

## Segurança

O log não armazena o texto da solicitação nem a resposta do modelo. O método de auditoria também não deve receber API keys ou tokens.

## Próxima evolução

Adicionar exportação estruturada opcional para SQLite local, com retenção, rotação e proteção de acesso. Nunca exportar prompts brutos por padrão.
