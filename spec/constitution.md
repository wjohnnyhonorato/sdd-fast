# Constitution — Operational Intelligence Reference

## Outcome
Reduzir tempo e risco de decisões operacionais usando modelos e agentes
com evidências rastreáveis e revisão humana.

## Scope
In: modelos de risco, análise de anomalias e assistência a investigação.
Out: mudanças automáticas em produção e decisões disciplinares sobre pessoas.

## Principles
- Evidência probabilística ou causal nunca é apresentada como certeza.
- Semântica temporal e prevenção de leakage precedem otimização de métricas.
- O agente recebe contexto compacto produzido por ferramentas especializadas.
- Ações externas exigem aprovação humana explícita.
- Código, specs e evidências mudam juntos.

## Tech Stack
- Python gerenciado com `uv`.
- scikit-learn/DoWhy para modelos; LangGraph para workflows agentic.
- Interface de LLM substituível, sem dependência do provedor no domínio.
- pytest para testes; MLflow para runs/modelos; plataforma de traces para agentes.
- Dados e credenciais não são enviados a provedores não autorizados.

## Roadmap
- Now: estimar risco de incidente e priorizar revisão humana.
- Next: explicar anomalias usando evidências de RCA e observabilidade.
- Later: recomendar procedimentos operacionais com aprovação humana.

## Quality Gates
- Splits e avaliações respeitam o instante real da decisão.
- Baseline, limitações e cortes críticos são reportados.
- Agentes respeitam tools, parada, custo e fallback definidos na feature.
- Toda saída operacional informa evidência, incerteza e responsável.

## Sources of Truth
- Code/tests: repositório e CI.
- Data/features: catálogo e versões de dataset.
- Models/runs: MLflow ou registry equivalente.
- Prompts/evals/traces: registry e plataforma de observabilidade agentic.

## Definition of Done
- Critérios possuem evidências reproduzíveis.
- Fallback, monitoramento e owner estão definidos quando aplicáveis.
- Constitution, feature spec e comportamento entregue estão coerentes.

## Sync Rule
Mudança comportamental atualiza a spec no mesmo PR.
Sem impacto: declarar `spec-impact: none` com justificativa.

