---
name: sdd-fast-start
description: Prepare a new or existing project for SDD-Fast, or resume work after switching projects. Use when the user asks to start, adopt, or resume the method; stop before implementing a task.
---

# Iniciar ou retomar SDD-Fast

Objetivo: deixar o projeto e a tarefa atual prontos para uma sessão de trabalho curta. Esta skill prepara contexto; as regras permanentes continuam em `AGENTS.md`.

## Identifique o cenário

1. Confirme a raiz do projeto atual. Examine a lista de arquivos da raiz, o estado do Git quando existir, os pontos de entrada, a configuração de ambiente e as validações relacionadas. Amplie a leitura somente se necessário.
2. Determine se o projeto já tem `AGENTS.md` e `CURRENT_TASK.md`:
   - **Novo:** faltam os dois arquivos. Prepare a adoção do método.
   - **Parcial:** falta um deles. Preserve o existente e acrescente apenas o ausente.
   - **Retomada:** ambos existem. Leia-os; não recopie modelos nem reescreva o contrato.
3. Leia as instruções em `AGENTS.md` e informe conflitos antes de realizar alguma modificação.

## Novo projeto ou adoção parcial

1. Obtenha os modelos `AGENTS.md`, `CURRENT_TASK.md` e `FUTURE_TASKS.md` da cópia local do método indicada pelo humano. Se não houver caminho, procure uma cópia local reconhecível. Como alternativa, use a versão `develop` de `https://github.com/wjohnnyhonorato/sdd-fast`, se acessível. Confirme que são os arquivos do método antes de copiá-los. Se nenhuma fonte estiver disponível, peça o caminho ao humano; não improvise os modelos.
3. Para um `AGENTS.md` recém-copiado, investigue apenas o necessário para preencher `## Contrato do projeto` e `## Comandos` com fatos verificáveis. Não altere as demais seções. Em projeto existente, relate incompatibilidades com a arquitetura prescrita sem refatorá-lo nesta etapa.
4. Se faltarem objetivo, usuário, entrega ou restrições que mudem o contrato, faça perguntas curtas. Não invente dados para substituir campos ainda indefinidos.

## Tarefa atual

1. Leia `CURRENT_TASK.md` e `FUTURE_TASKS.md`. Se houver uma tarefa real, preserve-a e use o checkpoint para identificar estado, próximo passo e bloqueios. Não a troque por outra ideia automaticamente.
2. Se não houver tarefa real, use `FUTURE_TASKS.md` como base de sugestão, se `FUTURE_TASKS.md` estiver vazio use o `## Contrato do projeto` como base de sugestão. FAça perguntas para definir **um comportamento principal**, limites e itens de `Como validar`. Cada item deve conter afirmação observável, resultado esperado e evidência reproduzível pelo humano, preencha `CURRENT_TASK.md` quando houver informação suficiente; caso contrário, faça apenas mais perguntas.
3. Não use uma ideia futura contida em `FUTURE_TASKS.md` como escopo aprovado.

## Encerramento

- Pare antes da implementação. Não instale dependências, crie código, execute testes extensos, arquive tarefas ou altere a estrutura do projeto nesta preparação.
- Confira os arquivos modificados e, se `AGENTS.md` mudou, verifique no diff que apenas `## Contrato do projeto` e `## Comandos` foram editados.
- Responda de forma curta: projeto identificado, situação do método, tarefa atual, arquivos preparados e decisão ou informação necessária para começar. Se uma tarefa já estiver pronta e aprovada, indique que a próxima sessão pode executá-la.