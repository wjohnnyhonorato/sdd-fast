# Feature — RCA Companion Agent

Status: planning

## Requirements
Intent: ajudar o SRE a investigar uma anomalia usando RCA e observabilidade.
Scope: in=consulta, síntese e próximos passos; out=alteração automática de recursos.
Assumptions: candidatos do RCA são hipóteses priorizadas, não causas comprovadas.

Profile/Agent:
- graph=`rca-companion:v1`; state invariant=`anomaly_id` é imutável.
- tools allowed=`rca.read, traces.search, runbook.read`; prohibited=`*.write`.
- human gate=qualquer ação externa; stop=max_steps:8 ou conclusão com evidência.
- retry=1 por tool; fallback=encaminhar ao SRE com evidências coletadas.
- eval=`rca-cases:v1`; limits=p95<15s e custo médio<US$0,10.

Acceptance:
- Toda afirmação causal é apresentada como hipótese e ligada a uma evidência.
- O agente usa apenas tools permitidas e nunca executa escrita externa.
- Ausência ou erro de uma tool produz resposta parcial e fallback explícito.
- O workflow termina em até oito passos, inclusive em rotas de erro.
- O estado preserva `anomaly_id` em nodes, retries e interrupções.
- Pelo menos 90% dos casos de eval seguem política, tool e routing esperados.
- Resposta mostra candidatos, evidências, limitações e próximo passo humano.

## Plan
- Definir state, schemas e interfaces das tools.
- Implementar nodes de coleta, síntese, validação e resposta.
- Adicionar routing, parada, retry e fallback.
- Criar mocks e casos de eval para sucesso, erro e interrupção humana.
- Instrumentar traces, custo, latência e violações de política.

## Validation
Expected:
- Testes unitários cobrem nodes e tools com mocks.
- Testes de grafo cobrem routing, retry, parada e fallback.
- `eval:rca-cases-v1` mede política, groundedness e trajetória.
- `trace:rca-companion-v1` registra nodes, tools e handoffs.

Observed:
- tests=pending
- eval=pending
- traces=pending

Result: pending

## Act
Decision: replan até validar schemas das tools e dataset de eval.
Next: aprovar contratos de `rca.read`, `traces.search` e `runbook.read`.
