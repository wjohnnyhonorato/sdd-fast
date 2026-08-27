# SDD Fast

SDD Fast é um método leve para desenvolver com coding agents sem depender apenas do histórico do chat. Ele registra somente o contrato permanente do projeto, a tarefa atual e o histórico das entregas.

> Texto preserva intenção e limites; código mostra o comportamento; testes demonstram o funcionamento.

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
- `tasks/`: tarefas concluídas em ordem sequencial.

Não existem roadmap de tarefas, backlog de specs ou planos detalhados.

## Tarefa atual

```markdown
# Current task: <nome curto>

## O que fazer
<resultado que deve ser entregue>

## O que não fazer
<limites que devem ser respeitados>

## Testes de funcionamento
- [ ] <comportamento que demonstra o funcionamento>
- [ ] `<comando de teste, quando aplicável>`

## Checkpoint
<estado atual, próximo passo e eventual bloqueio>
```

O humano controla a tarefa e os testes. O agente pode propor testes e atualizar o checkpoint, mas não pode ampliar o escopo ou enfraquecer a validação sem aprovação.

## Fluxo

1. Humano e agente definem `CURRENT_TASK.md`.
2. O agente lê a tarefa, o código e os testes relacionados.
3. Implementa uma mudança pequena e verificável.
4. Executa os testes e atualiza o checkpoint.
5. Se precisar mudar o escopo, consulta o humano.
6. Após aprovação, move a tarefa para `tasks/NNN-nome-curto.md` e limpa a tarefa atual.

## Testes

Use a menor validação capaz de demonstrar o comportamento importante:

| Mudança | Validação preferencial |
|---|---|
| Função determinística | Teste unitário |
| Bug | Teste que reproduz a falha |
| Integração | Teste de integração |
| Tool ou routing | Teste de entrada, saída e caminho |
| Resposta de LLM | Eval por fatos e critérios, sem texto exato |
| Interface visual | Teste da lógica e verificação manual |

Projetos sem testes começam protegendo apenas o comportamento alterado pela tarefa atual. Não é necessário criar retroativamente uma suíte completa.

## Regras de simplicidade

- Apenas uma tarefa ativa.
- Preferencialmente entre 8 e 15 linhas.
- Nenhuma tarefa futura registrada.
- `tasks/` contém somente tarefas concluídas.
- Checkpoint não é diário de comandos.
- Não duplicar detalhes existentes no código, nos testes ou no README.

## Prompt inicial

```text
Leia AGENTS.md e examine o projeto. Ajude-me a definir CURRENT_TASK.md
com somente: o que fazer, o que não fazer, testes de funcionamento e
checkpoint. Não implemente antes da minha aprovação.
```
