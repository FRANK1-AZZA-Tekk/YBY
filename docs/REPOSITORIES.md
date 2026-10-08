# Governança dos repositórios YBY

## Objetivo

Este documento define a função de cada repositório do ecossistema, reduz duplicação e estabelece o fluxo seguro de migração.

## Repositório canônico

`FRANK1-AZZA-Tekk/YBY` é o núcleo oficial do projeto YBY. Deve concentrar contratos, domínio, roteamento, políticas, documentação e integrações estáveis.

## Mapa de repositórios

| Repositório | Papel | Regra |
| --- | --- | --- |
| `YBY` | Núcleo oficial | Novas capacidades estáveis devem nascer aqui. |
| `FRANK_ZER0` | Laboratório full-stack | Prototipagem de frontend, backend, Android, ESP32 e deploy. |
| `YBY-YOU-BY-YOURSELF` | Reservado | Não iniciar desenvolvimento paralelo sem decisão registrada. |
| `YBY-brasil` | Reservado/comunidade | Usar futuramente para documentação, comunidade ou distribuição. |
| `empathic-voice-interface-starter` | Laboratório de voz | Avaliar componentes de voz antes de migrá-los. |
| `codexskills` | Infraestrutura | Manter skills e automações separadas do runtime YBY. |
| `FRANK_ZERO` | Histórico | Não criar novas dependências sem decisão explícita. |

## Regra de migração

Um componente só deve ser migrado quando:

1. a licença for compatível;
2. a finalidade estiver clara;
3. não houver segredo ou dado sensível;
4. existirem testes mínimos;
5. as dependências forem justificadas;
6. houver documentação de origem;
7. o componente puder ser isolado do deploy original.

## Política de branches

- `main`: código revisado e integrado.
- `feature/*`: implementação incremental.
- `fix/*`: correções isoladas.
- `research/*`: experimentos que ainda não podem ser dependência do núcleo.

## Política de integração

O núcleo `YBY` não deve depender diretamente de protótipos em `FRANK_ZER0`. A direção da dependência é:

```text
FRANK_ZER0 experimenta → componente validado → YBY incorpora
```

## Segurança

Nenhum repositório deve versionar tokens, chaves, arquivos `.env` reais, dumps de telemetria privada ou credenciais de hardware.
