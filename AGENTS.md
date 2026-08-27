# AGENTS.md

## Project contract

- Purpose: <problema que o projeto resolve>.
- Primary user: <quem usa o resultado>.
- Expected outcome: <resultado principal esperado>.
- Invariants: <regras que nenhuma tarefa pode violar>.
- Technical base: <tecnologias estruturais e estáveis>.
- Never: <comportamentos permanentemente proibidos>.

## Workflow

- Leia `CURRENT_TASK.md` antes de modificar o projeto.
- Se não houver tarefa definida, solicite uma ao humano.
- Faça somente **O que fazer** e respeite **O que não fazer**.
- Trabalhe em mudanças pequenas e preserve o que estiver fora do escopo.
- Se precisar ampliar a tarefa, pare e solicite aprovação.
- O humano controla a tarefa e os testes; o agente atualiza o checkpoint.

## Tests

- Use a menor validação capaz de demonstrar o funcionamento.
- Automatize comportamentos determinísticos, bugs e interfaces.
- Para LLMs, teste critérios e fatos, não a redação exata.
- Execute os testes relacionados e a suíte disponível antes de concluir.
- Não declare como aprovado um teste que não foi executado.

## Completion

- Conclua somente quando a tarefa estiver atendida e os testes passarem.
- Apresente o resultado ao humano e aguarde sua aprovação.
- Mova a tarefa para `tasks/NNN-nome-curto.md`.
- Use o próximo número sequencial e nunca reutilize números.
- Redefina `CURRENT_TASK.md` como sem tarefa.
- `tasks/` contém apenas tarefas concluídas; não crie backlog ou roadmap.

## Commands

- Preparar projeto: `<comando do projeto>`
- Executar testes: `<comando de testes>`
