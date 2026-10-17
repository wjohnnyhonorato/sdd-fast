# SDD Fast para Data Science e Agentes

Método enxuto para desenvolver com coding agents com velocidade, controle humano e evidências. Foi pensado para projetos de software, Data Science, Machine Learning, inferência causal e agentes de IA.

> A tarefa preserva intenção e limites; o código implementa o comportamento; testes, métricas e evals demonstram o funcionamento.

## O método em uma página

1. Defina uma tarefa pequena com um comportamento observável, limites e validação.
2. O agente compreende o contexto necessário, implementa e produz evidências.
3. O humano examina os arquivos alterados e as evidências, pede correções ou aprova.
4. Após a aprovação, arquive a tarefa e escolha a próxima.

O método não exige roadmap, pasta de especificação por feature, plano técnico detalhado nem uma suíte de testes para cada pequena alteração.

## Arquivos do projeto

| Artefato | Papel |
|---|---|
| `AGENTS.md` | Contrato permanente do projeto e instruções para o agente |
| `CURRENT_TASK.md` | Única tarefa ativa: comportamento, limites, validação e checkpoint |
| `FUTURE_TASKS.md` | Memória de possíveis trabalhos e dependências; não autoriza sua execução |
| `tasks/NNN-nome-curto.md` | Histórico de tarefas concluídas |
| Código e validações | Comportamento atual e evidências de funcionamento |
| Git | Histórico técnico e revisão das alterações |

O agente lê `AGENTS.md`, `CURRENT_TASK.md` e `FUTURE_TASKS.md` no início de cada tarefa. As ideias futuras ajudam a identificar dependências e a escolher a próxima tarefa, mas somente `CURRENT_TASK.md` define o escopo aprovado. O humano pode pedir mudanças em `FUTURE_TASKS.md` a qualquer momento; o agente pode sugerir ideias, mas só registra, altera ou remove itens quando receber um pedido explícito. Tarefas arquivadas são histórico e não são carregadas por padrão.

## Como começar

1. Copie [AGENTS.md](AGENTS.md), [CURRENT_TASK.md](CURRENT_TASK.md) e [FUTURE_TASKS.md](FUTURE_TASKS.md) para a raiz do projeto.
2. Preencha no `AGENTS.md` o objetivo, as restrições, a arquitetura e os comandos reais do projeto.
3. Defina em `CURRENT_TASK.md` um comportamento principal, o que está fora do escopo e como um humano verificará o resultado.

Para preparar a tarefa com o agente:

```text
Leia AGENTS.md, CURRENT_TASK.md e FUTURE_TASKS.md. Examine progressivamente
o projeto. Ajude-me a definir uma tarefa atual com o que fazer,
o que não fazer, como validar e checkpoint.
Pergunte apenas sobre ambiguidades que possam mudar a solução.
Não implemente antes da minha aprovação.
```

Se usar Devin CLI, instale a pasta [sddstart](.agents/skills/sddstart/) no projeto ou nas skills pessoais e chame `/sddstart`. A skill prepara os arquivos e a tarefa; ela para antes da implementação.

Depois de aprovar a tarefa:

```text
Execute CURRENT_TASK.md, valide o resultado e revise o diff antes de concluir.
```

## Tamanho e contexto da tarefa

Uma tarefa entrega uma mudança observável, pode ser validada isoladamente e produz uma alteração que o humano consegue revisar, preferencialmente em uma sessão. Se houver entregas independentes ou o trabalho crescer demais, divida em tarefas verticais sequenciais.

Prefira iniciar cada tarefa em uma nova sessão do coding agent. O agente reconstrói o contexto a partir do contrato, da tarefa, dos lembretes futuros, da estrutura, do código e das validações relacionadas. Em projetos desconhecidos, amplia a leitura conforme o alcance e o risco da mudança, sem carregar preventivamente o repositório inteiro. Não reinicie a sessão no meio da mesma tarefa.

O checkpoint registra somente estado atual, próximo passo e bloqueios. Passos internos não precisam virar subtarefas documentadas ou ciclos completos de validação.

## Código e arquitetura em projetos Python de modelagem

O [modelo de AGENTS.md](AGENTS.md) estabelece este padrão para os projetos de modelagem:

```text
main.py
config.yml
pyproject.toml
uv.lock
src/
├── __init__.py
├── dados.py
└── modelo.py
notebooks/
└── validate_pipeline.ipynb
```

Os nomes dos módulos são ilustrativos. Use `uv` para ambiente, dependências e execução; Git para versionamento. Crie apenas os módulos e funções necessários, agrupados por responsabilidade. Toda função tem uma docstring curta com objetivo, entradas, etapas principais e saída. Código enxuto deve continuar fácil de entender.

`main.py` orquestra o fluxo, sem lógica de modelagem, e sua docstring registra a ordem das chamadas. Entre módulos, use chamadas qualificadas, como `dados.carregar(...)`; dentro do mesmo módulo, chamadas diretas são permitidas.

`uv run python main.py` executa o objetivo principal de ponta a ponta. O notebook `notebooks/validate_pipeline.ipynb` importa os módulos atuais de `src/` e reproduz, uma etapa principal por célula, a mesma ordem e os mesmos parâmetros das chamadas diretas do `main.py`. Cada célula mostra uma saída concisa para inspeção. Não defina funções nem duplique a lógica dos módulos no notebook.

Após mudar `src/`, reinicie o kernel e execute todas as células antes de considerar os resultados do notebook atuais. A execução completa verifica o fluxo, mas a qualidade de um modelo exige as evidências definidas na tarefa.

## Validação verificável

Cada item de “Como validar” conecta **afirmação observável, resultado esperado e evidência** que o humano pode inspecionar ou reproduzir:

```markdown
- [ ] O pipeline conclui a execução. Esperado: gera o arquivo de
      resultados. Evidência: executar `uv run python main.py` e
      inspecionar o arquivo produzido.
```

Testes e evals partem do comportamento esperado, não do código já escrito. O agente não pode enfraquecer ou ignorar uma validação para fazê-la passar; se ela estiver incorreta, explica o problema e consulta o humano. Um relato de que “passou” não substitui a evidência.

Escolha a menor evidência confiável para a mudança:

| Mudança | Evidência útil |
|---|---|
| Função determinística ou bug | Resultado conhecido ou teste de regressão |
| Integração | Contrato, entrada e saída observadas |
| Modelo de ML | Baseline, split adequado, leakage, métricas e cortes relevantes |
| Inferência causal | Estimand, identificação, pressupostos, overlap e sensibilidade aplicáveis |
| Agente ou LLM | Contratos de tools, caminhos do grafo, falhas e evals de comportamento |
| Interface | Comportamento testado e inspeção visual |

Nem toda tarefa requer todas essas verificações. Em projetos sem cobertura, proteja primeiro o comportamento alterado, sem criar uma suíte retroativa por padrão. TDD ajuda quando o comportamento é claro, mas não é obrigatório em exploração ou experimentos.

## Revisão e conclusão

Antes de aprovar, revise os arquivos alterados no editor:

- **Escopo:** o resultado atende à tarefa sem acrescentar entregas?
- **Qualidade:** há complexidade, dependência, abstração ou risco desnecessário?
- **Evidência:** o procedimento e os resultados permitem verificar as afirmações?

O agente informa de forma curta o que alterou, quais validações executou, seus resultados e limitações. A aprovação é do humano. Depois dela, mova a tarefa para `tasks/NNN-nome-curto.md` e deixe `CURRENT_TASK.md` sem tarefa ativa. Sugestões de trabalhos futuros só entram em `FUTURE_TASKS.md` se o humano pedir.

Uma prática recorrente pode virar uma skill quando demonstrar valor. Revisão por outro agente é opcional em mudanças maiores ou de maior risco.

## Por que este formato

O [RATIONALE.md](RATIONALE.md) registra as escolhas do método e sua relação com o SDD do curso da DeepLearning.AI. Ele serve à revisão do método; o agente não precisa lê-lo a cada tarefa.

## Referências

- [DeepLearning.AI — Spec-Driven Development with Coding Agents](https://www.deeplearning.ai/courses/spec-driven-development-with-coding-agents/)
- [Materiais práticos do curso](https://github.com/https-deeplearning-ai/sc-spec-driven-development-files)
- [Matt Pocock — Skills for Real Engineers](https://github.com/mattpocock/skills)
- [Tech Leads Club — TLC Spec Lean](https://github.com/tech-leads-club/agent-skills/blob/main/packages/skills-catalog/skills/(development)/tlc-spec-lean/SKILL.md)
- [Attekita Dev — fluxo de skills](https://www.youtube.com/watch?v=SreK3gB6Gso)
- [AkitaOnRails — crítica a Harness, Loop e SDD](https://akitaonrails.com/2026/08/18/hot-take-harness-loop-engineering-graph-engineering-sao-bullshit/)
- [DORA — Working in Small Batches](https://dora.dev/capabilities/working-in-small-batches/)
- [Thoughtworks Technology Radar — Spec-Driven Development](https://www.thoughtworks.com/radar/techniques/spec-driven-development)
