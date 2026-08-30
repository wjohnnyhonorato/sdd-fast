# SDD Fast para Data Science e Agentes

Método enxuto para desenvolver com coding agents com velocidade, controle humano e evidências, sem depender do histórico do chat ou criar documentação excessiva.

Foi pensado para projetos de software, Data Science, Machine Learning, inferência causal e agentes de IA.

> A tarefa preserva intenção e limites; o código implementa o comportamento; testes, métricas e evals demonstram o funcionamento.

## Princípios

- Uma única tarefa ativa, pequena e verificável.
- Perguntas somente quando a resposta puder mudar comportamento, arquitetura, risco ou escopo.
- A menor validação confiável para o tipo de entrega.
- Revisão do diff antes da aprovação humana.
- Regras e skills surgem de problemas recorrentes, não de antecipação.
- Código e evidências descrevem o estado atual; tarefas arquivadas preservam apenas o histórico.

## Estrutura no projeto

```text
AGENTS.md
CURRENT_TASK.md
tasks/
├── 001-primeira-entrega.md
└── 002-segunda-entrega.md
```

| Artefato | Função |
|---|---|
| `AGENTS.md` | Contrato do projeto e regras permanentes para agentes |
| `CURRENT_TASK.md` | Única mudança em andamento, seus limites e como validá-la |
| `tasks/` | Histórico sequencial das tarefas concluídas |
| Código | Comportamento atual do sistema |
| Testes, métricas e evals | Evidências de funcionamento |
| Git | Histórico técnico das modificações |

Não existem roadmap obrigatório, backlog de specs ou plano técnico detalhado.

## Como começar

1. Copie [AGENTS.md](sdd-fast/AGENTS.md) e [CURRENT_TASK.md](sdd-fast/CURRENT_TASK.md) para a raiz do projeto.
2. Preencha o contrato e os comandos reais em `AGENTS.md`.
3. Defina a primeira tarefa em `CURRENT_TASK.md`.
4. Peça ao agente para executar a tarefa, validar o resultado e revisar o diff.
5. Após a aprovação humana, arquive a tarefa em `tasks/NNN-nome-curto.md`.

O método completo e exemplos de validação estão em [sdd-fast.md](sdd-fast/sdd-fast.md). A justificativa das escolhas e a comparação com o SDD do curso estão em [RATIONALE.md](sdd-fast/RATIONALE.md).

## Para cientistas de dados

Validação não significa apenas teste unitário:

- ML pode exigir baseline, split temporal, métrica e teste de leakage;
- inferência causal pode exigir estimand, identificação, overlap e sensibilidade;
- agentes podem exigir contratos de tools, routing, parada, fallback e evals;
- interfaces podem combinar testes automatizados e verificação manual.

Esses itens entram somente quando forem relevantes para a tarefa atual.

## Referências

- [DeepLearning.AI — Spec-Driven Development with Coding Agents](https://www.deeplearning.ai/courses/spec-driven-development-with-coding-agents/)
- [Matt Pocock — Skills for Real Engineers](https://github.com/mattpocock/skills)
- [AkitaOnRails — crítica a Harness, Loop e Spec-Driven Development](https://akitaonrails.com/2026/08/18/hot-take-harness-loop-engineering-graph-engineering-sao-bullshit/)
- [DORA — Working in Small Batches](https://dora.dev/capabilities/working-in-small-batches/)
- [Thoughtworks Technology Radar — Spec-Driven Development](https://www.thoughtworks.com/radar/techniques/spec-driven-development)
