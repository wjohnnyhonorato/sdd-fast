# SDD Fast

SDD Fast é um método leve para desenvolver com coding agents sem vibe coding e sem depender apenas do histórico do chat. Ele preserva somente o contrato permanente do projeto, a tarefa atual e o histórico das entregas.

> A tarefa preserva intenção e limites; o código implementa o comportamento; testes, métricas e evals demonstram o funcionamento.

### Código compreensível por humanos

O SDD Fast busca produzir a menor solução que atenda à tarefa e possa ser facilmente revisada. O código deve ter responsabilidades, entradas e saídas claras, preferindo funções coesas quando apropriado.

Documentação deve explicar contratos, regras e decisões não evidentes, sem repetir mecanicamente o código. A comunicação do agente também deve ser curta e orientada ao que o humano precisa verificar ou decidir.

Enxuto não significa condensado. Código curto, porém obscuro, não atende a esse princípio.

## Artefatos

```text
AGENTS.md
CURRENT_TASK.md
tasks/
├── 001-primeira-entrega.md
└── 002-segunda-entrega.md
```

- `AGENTS.md`: contrato do projeto e regras permanentes.
- `CURRENT_TASK.md`: única tarefa em andamento.
- `tasks/`: histórico sequencial das tarefas concluídas.

Não existem roadmap obrigatório, backlog de specs ou plano técnico detalhado.

Código e validações descrevem o estado atual. Tarefas arquivadas são históricas e não precisam permanecer sincronizadas com mudanças futuras.

## Tarefa atual

```markdown
# Current task: <nome curto>

## O que fazer
<resultado observável que deve ser entregue>

## O que não fazer
<limites que devem ser respeitados>

## Como validar
- [ ] <comportamento ou propriedade que deve ser demonstrada>
- [ ] <evidência que o humano conseguirá inspecionar ou reproduzir>
- [ ] `<comando, métrica, artefato ou procedimento aplicável>`


## Checkpoint
<estado atual, próximo passo e eventual bloqueio>
```

O humano controla escopo e validação. O agente pode propor evidências e atualizar o checkpoint, mas não pode ampliar a tarefa ou enfraquecer a validação sem aprovação.

## Fluxo

1. Humano e agente definem uma tarefa pequena e observável.
2. O agente lê `AGENTS.md`, `CURRENT_TASK.md`, o código e as validações relacionadas.
3. Faz perguntas somente sobre ambiguidades que alterem comportamento, arquitetura, risco ou escopo.
4. Implementa uma pequena mudança vertical e verificável.
5. Executa a validação definida e atualiza o checkpoint.
6. Revisa o diff contra a tarefa e a qualidade técnica.
7. O humano avalia o resultado e decide se aprova, corrige ou interrompe.
8. Após aprovação, a tarefa vai para `tasks/NNN-nome-curto.md` e `CURRENT_TASK.md` é limpo.

## Como validar


Toda validação deve ser verificável por um humano. Isso significa apresentar o procedimento ou comando utilizado, o resultado observável e, quando aplicável, o artefato produzido.

A afirmação do agente de que uma validação foi executada ou passou não é evidência suficiente. O agente produz e organiza as evidências; o humano as inspeciona e decide se a tarefa pode ser aprovada.

Isso não significa criar relatórios extensos para todas as tarefas.
Deve ser usada a menor evidência confiável que permita ao humano
verificar a afirmação.

Use a menor evidência confiável capaz de demonstrar o comportamento importante:

| Mudança | Validação preferencial |
|---|---|
| Função determinística | Teste unitário com resultado conhecido |
| Bug | Teste de regressão que falha antes da correção |
| Integração | Teste de contrato ou integração |
| Modelo de ML | Baseline, split adequado, leakage, métrica e cortes relevantes |
| Inferência causal | Estimand, identificação, pressupostos, overlap e sensibilidade aplicáveis |
| Tool ou routing | Schema, entrada, saída, caminho, vazio e erro |
| Resposta de LLM | Eval por fatos, critérios e uso correto de tools, sem exigir texto exato |
| Interface visual | Teste do comportamento e verificação manual |

Projetos sem testes começam protegendo somente o comportamento alterado pela tarefa. Não é necessário criar retroativamente uma suíte completa.

TDD é útil quando o comportamento esperado é claro, especialmente para bugs e lógica determinística. Não é obrigatório em exploração de dados, protótipos ou trabalhos cuja evidência principal seja experimental.

## Revisão final

Antes da aprovação, compare o diff com a tarefa em dois eixos:

1. **Escopo:** algo solicitado ficou faltando, incorreto ou foi acrescentado sem necessidade?
2. **Qualidade:** existe complexidade, dependência, abstração ou risco desnecessário?

Uma revisão independente por outro agente é opcional e deve ser reservada a mudanças grandes ou de maior risco.

## Tamanho da tarefa

Uma tarefa está no tamanho adequado quando:

- entrega uma mudança observável;
- pode ser validada isoladamente;
- produz um diff compreensível;
- cabe, preferencialmente, em uma sessão de trabalho.

Se não couber, divida em entregas verticais sequenciais. Não crie um `plan.md`.

## O que deve sobreviver

| Informação | Destino |
|---|---|
| Intenção e limites atuais | `CURRENT_TASK.md` |
| Comportamento atual | Código e testes |
| Decisão permanente | `AGENTS.md` ou documentação existente |
| Problema recorrente | Regra, teste ou futura skill |
| Entrega concluída | `tasks/NNN-nome-curto.md` |
| Comando ou conversa sem valor futuro | Não preservar |

## Regras de simplicidade

- Apenas uma tarefa ativa, preferencialmente entre 8 e 15 linhas.
- Nenhuma tarefa futura registrada.
- Perguntas apenas sobre ambiguidades materiais.
- Checkpoint registra estado, próximo passo e bloqueios; não é diário de comandos.
- Não duplicar detalhes existentes no código, testes ou README.
- Uma prática só vira skill depois de demonstrar valor repetidamente.

## Prompt inicial

```text
Leia AGENTS.md e examine o projeto. Ajude-me a definir CURRENT_TASK.md
com somente: o que fazer, o que não fazer, como validar e checkpoint.
Pergunte apenas sobre ambiguidades que possam mudar a solução.
Não implemente antes da minha aprovação.
```

Depois da aprovação, basta pedir:

```text
Execute CURRENT_TASK.md, valide o resultado e revise o diff antes de concluir.
```
