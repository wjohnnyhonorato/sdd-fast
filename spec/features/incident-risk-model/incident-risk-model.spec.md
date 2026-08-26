# Feature — Incident Risk Model

Status: planning

## Requirements
Intent: priorizar mudanças de produção para revisão humana antes da execução.
Scope: in=score e explicação; out=bloqueio ou aprovação automática.
Assumptions: incidentes ligados à mudança são raros e o vínculo histórico possui ruído.

Profile/ML:
- unit=`change_id` no instante de submissão; target=incidente causado em 24h.
- data=`change_dataset:v1`; split=temporal; eventos pós-submissão são proibidos.
- baseline=regra operacional atual; cortes críticos=produto e tipo de mudança.
- fallback=processo atual sem score; owner=Change Risk Team.

Acceptance:
- O score usa somente dados disponíveis no instante da submissão.
- O pipeline detecta features com timestamp posterior à decisão.
- Recall é maximizado sob precisão mínima de 10% no teste temporal.
- O modelo supera o baseline no mesmo conjunto e protocolo.
- Métricas por produto e tipo de mudança acompanham a métrica global.
- A explicação informa fatores associados, sem afirmar causalidade.
- Falha do modelo mantém o processo operacional anterior.

## Plan
- Validar definição de target e qualidade do vínculo mudança–incidente.
- Construir dataset temporal e testes de leakage.
- Reproduzir baseline e protocolo de avaliação.
- Treinar candidatos e selecionar pelo contrato de métricas.
- Publicar score, explicação, monitoramento e fallback.

## Validation
Expected:
- `test:temporal-leakage` e `test:feature-availability` passam.
- `run:incident-risk-candidate` registra baseline, modelo e slices.
- CI valida schema, inferência e fallback.

Observed:
- tests=pending
- run=pending
- monitoring=pending

Result: pending

## Act
Decision: replan até que target, baseline e limiar sejam aprovados.
Next: auditar uma amostra dos vínculos mudança–incidente com especialistas.
