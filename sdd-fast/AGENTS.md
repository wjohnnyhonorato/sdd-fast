# AGENTS.md

## Contrato do projeto

- Objetivo e escopo: <problema que resolve e limites do projeto>.
- Usuário principal: <quem usa o resultado>.
- Entrega esperada: <resultado principal>.
- Invariantes: <regras que nenhuma tarefa pode violar>.
- Base técnica: <tecnologias estruturais e estáveis>.
- Arquitetura: código reutilizável em `src/<pacote>`, organizado
  em módulos por responsabilidade; pontos de entrada permanecem
  pequenos e sem lógica do domínio.
- Ponto de entrada: <arquivo.py na raiz, main.py, api.py, app.py ou outro mais aplicável> 
- Nunca fazer: <comportamentos permanentemente proibidos>.

## Antes de implementar

- Leia `CURRENT_TASK.md`, o código e as validações relacionadas.
- Se não houver tarefa definida, solicite uma ao humano.
- Pergunte somente sobre ambiguidades que possam mudar comportamento, arquitetura, risco ou escopo.
- Confirme que a tarefa possui um único comportamento principal.
- Se houver entregas independentes ou um diff difícil de revisar, pare e proponha tarefas menores.

## Implementação

- Faça somente **O que fazer** do `CURRENT_TASK.md` e respeite **O que não fazer** do `CURRENT_TASK.md`.
- Implemente a menor solução coerente que atenda à tarefa.
- Preserve comportamento e arquivos fora do escopo.
- Não adicione dependências, refatorações, abstrações ou documentos sem necessidade para a tarefa.
- Prefira módulos e funções pequenos e coesos, cada um com responsabilidade, entradas e saídas claras.
- Documente funções com descrição do que faz, entradas e saidas, em linguagem simples.
- Mantenha entradas e saídas explícitas, preferencialmente com tipagem.
- Para ampliar o escopo ou enfraquecer a validação, solicite aprovação.
- Passos internos podem orientar a execução, mas não devem virar novas entregas, artefatos ou ciclos completos de validação.
- Antes de pausar, solicitar aprovação ou encerrar sem concluir, atualize **Checkpoint** do `CURRENT_TASK.md` com estado atual, próximo passo e eventual bloqueio, sem registrar um diário de comandos.
- Se o trabalho crescer além do previsto ou deixar de convergir para um diff pequeno, pare em estado seguro, atualize o checkpoint e proponha a divisão da tarefa.

## Validação

- Siga **Como validar** usando a menor evidência confiável para a mudança.
- Durante a implementação, execute primeiro as validações diretamente afetadas; amplie somente quando o risco de regressão justificar.
- Apresente o procedimento, o resultado observável e o artefato aplicável de forma que o humano possa inspecionar ou reproduzir.
- Não declare como executada ou bem-sucedida uma validação que não ocorreu.
- Validação bem-sucedida não substitui a aprovação humana.
- Use evidência adequada à entrega: testes para comportamento determinístico; métricas, diagnósticos causais ou evals quando aplicáveis.
- Em projetos sem cobertura, proteja somente o comportamento alterado; não crie uma suíte retroativa sem solicitação.

## Revisão e conclusão

- Compare o diff com a tarefa e verifique escopo, funcionamento, complexidade desnecessária e suficiência das evidências.
- Não reproduza o diff nem arquivos completos no chat.
- Informe de forma curta: alterações, validações, resultados e limitações, listando modulos e funções alterados.
- O humano revisa as alterações detalhadas pelo pelo editor.
- Aguarde aprovação antes de arquivar a tarefa.
- Após aprovação, mova-a para `tasks/NNN-nome-curto.md` e redefina
  `CURRENT_TASK.md` como sem tarefa.
- Tarefas arquivadas são histórico e não devem ser carregadas por padrão.

## Comandos

- Preparar projeto: `<comando do projeto>`
- Executar validações: `<comando de validação>`