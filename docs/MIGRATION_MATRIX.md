# Matriz de migração do ecossistema

## Legenda

- `avaliar`: requer inspeção de código, licença e testes.
- `migrar`: candidato a extração para o núcleo.
- `manter`: permanece no repositório de origem.
- `adiar`: útil, mas fora do MVP.

| Origem | Componente | Valor | Risco | Ação | Destino provável |
| --- | --- | --- | --- | --- | --- |
| `YBY` | UI schema | alto | baixo | manter | `YBY/schemas` |
| `YBY` | roteador inicial | alto | baixo | manter/evoluir | `YBY/src/yby` |
| `YBY` | políticas local-first | alto | médio | consolidar | `YBY/src/yby` |
| `FRANK_ZER0` | backend | alto | alto | avaliar | `YBY/infrastructure` |
| `FRANK_ZER0` | frontend | alto | médio | avaliar | app/dashboard futuro |
| `FRANK_ZER0` | ESP32 | médio | alto | adiar e testar | firmware separado |
| `FRANK_ZER0` | Android | médio | médio | adiar | aplicativo futuro |
| `FRANK_ZER0` | Docker/deploy | médio | alto | manter isolado | laboratório |
| `FRANK_ZER0` | Prometheus | médio | médio | avaliar depois dos eventos | observabilidade |
| `empathic-voice-interface-starter` | voz | alto | médio | avaliar | módulo de voz futuro |
| `codexskills` | skills | médio | médio | manter separado | infraestrutura |
| `YBY-brasil` | comunidade | potencial | baixo | reservar | documentação/comunidade |
| `YBY-YOU-BY-YOURSELF` | distribuição | potencial | baixo | reservar | produto/distribuição |

## Critérios de aceitação

Antes da migração, o componente deve ter:

- licença identificada;
- dependências listadas;
- testes reproduzíveis;
- ausência de segredos;
- documentação de configuração;
- interface independente do deploy original;
- plano de rollback.

## Ordem recomendada

1. contratos compartilhados;
2. ferramentas e providers mock;
3. backend local;
4. frontend baseado em schema;
5. telemetria simulada;
6. hardware real;
7. cloud/deploy.
