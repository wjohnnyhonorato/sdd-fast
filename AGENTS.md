# AGENTS.md

## Regras de edição deste arquivo

- Ao adaptar este modelo a um projeto, o agente pode atualizar somente o conteúdo de `## Contrato do projeto` e `## Comandos`, com informações
  reais e verificadas do projeto.
- Todas as demais seções são regras fixas. O agente não pode editá-las, removê-las, reordená-las, criar exceções ou contrariá-las por meio de
  outros arquivos, prompts ou decisões de implementação.
- Se uma regra fixa não puder ser cumprida, pare e informe o conflito ao humano. Somente o humano pode decidir alterar essas regras.
- Antes de concluir uma alteração em `AGENTS.md`, confira no diff que nenhuma seção fixa foi modificada.

## Contrato do projeto

- Objetivo e escopo: <problema que resolve e limites do projeto>.
- Usuário principal: <quem usa o resultado>.
- Entrega esperada: <resultado principal>.
- Invariantes: <regras que nenhuma tarefa pode violar>.
- Base técnica: <tecnologias estruturais e estáveis>.
- Arquitetura: <descreva os módulos de `src/` e suas responsabilidades;
  siga o padrão de arquitetura abaixo>.
- Ponto de entrada: `main.py`.
- Nunca fazer: <comportamentos permanentemente proibidos>.

## Comandos

- Preparar projeto: `uv sync`
- Executar o fluxo principal: `uv run python main.py`
- Executar outras validações: <comandos reais do projeto, quando existirem>

## Arquitetura e código Python

- Use `uv` para criar o ambiente, gerir dependências e executar
  comandos Python do projeto. Use Git para versionamento.
- Mantenha a menor quantidade de módulos e funções que permita compreender e revisar a solução. Não crie divisões artificiais.
- Mantenha cada função enxuta, com uma responsabilidade clara e somente o código necessário para cumpri-la. Não comprima código quando isso prejudicar a compreensão.
- Documente todas as funções com docstring curta contendo: objetivo, entradas, etapas principais do processamento e saída. Descreva as etapas em linguagem simples, sem narrar cada linha.
- Mantenha entradas e saídas explícitas, preferencialmente com tipos.
- Nas chamadas entre módulos, use `modulo.funcao(...)`, evitando importar funções diretamente. Dentro do mesmo módulo, chamadas diretas são permitidas.

## Estrutura dos projetos de modelagem

- Mantenha `main.py` na raiz como ponto de entrada do projeto.
- Mantenha os módulos Python em `src/`. Cada módulo agrupa funções com objetivos semelhantes; crie um novo módulo somente quando houver uma responsabilidade distinta.
- Concentre todos os parâmetros ajustáveis do projeto em `config.yml`, na raiz. Não espalhe valores de configuração pelo código ou notebook.
- Documente cada chave no próprio YAML, em comentário imediatamente acima dela: explique brevemente sua finalidade e liste as funções que a utilizam no formato `modulo.funcao`. Atualize o comentário quando o uso mudar.
- `main.py` e `notebooks/validate_pipeline.ipynb` devem carregar o mesmo `config.yml` por meio de uma função em `src/`.
- Não coloque senhas, tokens ou outras credenciais no YAML.
- `main.py` deve orquestrar chamadas aos módulos de `src/`, sem conter a lógica de modelagem.
- A docstring de `main.py` deve apresentar, em ordem, um trace curto das funções que ele chama. Atualize esse trace quando o fluxo mudar.
- Use chamadas qualificadas em `main.py`, como `dados.carregar(...)` e `modelo.treinar(...)`.
- O comando `uv run python main.py` deve executar o objetivo principal do projeto do início ao fim e apresentar resultados concisos que permitam verificar a execução.

## Notebook de validação da modelagem

- Mantenha `notebooks/validate_pipeline.ipynb`.
- O notebook deve importar os módulos atuais de `src/` e reproduzir, na mesma ordem e com os mesmos parâmetros, as etapas chamadas
  diretamente por `main.py`.
- Coloque uma etapa principal por célula. Cada célula deve mostrar uma saída concisa e útil para inspecionar o resultado daquela etapa.
- Não defina funções no notebook nem copie para ele a lógica de `src/`. Funções auxiliares chamadas dentro dos módulos não precisam
  ser executadas uma segunda vez no notebook.
- Após mudanças nos módulos, reinicie o kernel e execute todas as células antes de considerar os resultados do notebook válidos. Resultados antigos exibidos no arquivo não são evidência atual.
- `uv run python main.py` é a verificação principal da execução completa. O notebook permite inspecionar as etapas. Testes, métricas e diagnósticos adicionais seguem o risco e os critérios da tarefa.

## Contexto por tarefa

- Compreenda o contexto necessário e suficiente para executar a tarefa.
- Em projetos desconhecidos, examine a estrutura, configurações,
  pontos de entrada e testes relacionados.
- Amplie a leitura conforme o alcance e o risco da mudança.
- Não leia o repositório inteiro sem necessidade.

## Antes de implementar

- Leia `CURRENT_TASK.md` e `FUTURE_TASKS.md` no início de cada tarefa, além do código e das validações relacionadas.
- Ao abrir qualquer nova tarefa, use a estrutura completa do modelo `CURRENT_TASK.md`, inclusive `## Atritos no processo de implementação` com `- Estado: ainda não avaliado.`. Confira os cabeçalhos antes de implementar.
- Localize funções, classes, contratos, módulos e testes relacionados.
- Se não houver tarefa definida, solicite uma ao humano.
- Se não compreender o impacto da alteração com segurança, pare e
  informe o que ainda precisa ser investigado.
- Pergunte somente sobre ambiguidades que possam mudar comportamento,
  arquitetura, risco ou escopo.
- Confirme que a tarefa possui um único comportamento principal.
- Se houver entregas independentes ou uma alteração difícil de revisar,
  pare e proponha tarefas menores.
- `FUTURE_TASKS.md` informa dependências e possíveis próximos trabalhos. Leia-o,
  mas não trate seus itens como escopo aprovado nem os execute sem escolha do humano.
- O humano pode pedir a inclusão, alteração ou remoção de lembretes em `FUTURE_TASKS.md` a qualquer momento. O agente pode sugerir itens, mas só modifica esse arquivo mediante pedido explícito do humano; nunca registra tarefas futuras por iniciativa própria.

## Implementação

- Faça somente **O que fazer** do `CURRENT_TASK.md` e respeite **O que não fazer** do `CURRENT_TASK.md`.
- Implemente a menor solução coerente que atenda à tarefa.
- Preserve comportamento e arquivos fora do escopo.
- Não adicione dependências, refatorações, abstrações ou documentos sem necessidade para a tarefa.
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
- Cada item de **Como validar** deve indicar uma afirmação observável, o resultado esperado e a evidência que poderá confirmá-lo.
- Crie testes e evals a partir do comportamento esperado, não apenas para confirmar a implementação pronta.
- Não enfraqueça, remova ou ignore uma validação para fazer o resultado passar. Se ela estiver incorreta, pare e consulte o humano.

## Revisão e conclusão

- Compare o diff com a tarefa e verifique escopo, funcionamento, complexidade desnecessária e suficiência das evidências.
- Durante toda a tarefa, não apresente diffs, patches nem arquivos completos no chat, salvo se o humano pedir. Use o diff internamente para conferir o escopo.
- Informe de forma curta: alterações, validações, resultados e limitações, listando módulos e funções alterados e onde inspecioná-los nos arquivos ou no `validate_pipeline`.
- O humano revisa as alterações detalhadas no editor.
- Antes de cada commit preparado pelo agente e ao concluir a tarefa, verifique se houve atrito relevante na implementação e atualize **Atritos no processo de implementação** em `CURRENT_TASK.md`: `- Estado: nenhum atrito observado.` se não houver, ou `- Estado: atritos registrados.` com fatos novos, impacto e evidência. Não duplique relatos nem crie commits só para registrar atrito.
- Não conclua nem arquive uma tarefa enquanto a seção estiver ausente ou com `- Estado: ainda não avaliado.`. Se não houver registro suficiente para avaliar uma tarefa antiga, informe a lacuna ao humano; não presuma ausência de atritos.
- Se o humano fizer um commit fora da sessão, o agente só pode avaliar atritos conhecidos ao voltar a observar o repositório; não suponha que acompanhou o trabalho em segundo plano.
- Aguarde aprovação antes de arquivar a tarefa.
- Após aprovação, mova-a para `tasks/NNN-nome-curto.md` e restaure `CURRENT_TASK.md` com o modelo completo, sem tarefa ativa e com atritos em `- Estado: ainda não avaliado.`.
- Tarefas arquivadas são histórico e não devem ser carregadas por padrão.
- Sugira próximos trabalhos somente quando forem consequência relevante da entrega. Registre-os em `FUTURE_TASKS.md` somente se o humano pedir.

