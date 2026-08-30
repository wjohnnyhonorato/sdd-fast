# Por que o SDD Fast existe

Este documento registra a linha de raciocínio usada para criar o SDD Fast. Ele não adiciona etapas ao método e não precisa ser lido pelo agente durante cada tarefa. Sua função é permitir que pessoas e times avaliem as escolhas do método sem tratá-las como dogma.

## O problema que tentamos resolver

Coding agents aumentam muito a velocidade de produção de código, mas não eliminam quatro problemas clássicos:

1. desalinhamento sobre o que deve ser construído;
2. perda de contexto entre sessões;
3. código que parece pronto, mas não foi validado;
4. crescimento desnecessário de escopo e complexidade.

O curso da DeepLearning.AI responde a esses problemas com uma constituição do projeto e três documentos por feature. A experiência prática com esse formato mostrou um novo custo: documentos longos, repetição entre arquivos, revisão lenta e risco de a especificação deixar de acompanhar o código.

O SDD Fast procura preservar o valor do SDD sem transformar documentação em uma segunda implementação do sistema.

> Escrever antes o suficiente para alinhar; construir em pequenas partes; provar o resultado; preservar somente o que terá valor depois.

## Síntese das influências

### DeepLearning.AI: intenção persistente e validação

O curso demonstra que um agente trabalha melhor quando recebe contexto que não consegue inferir apenas do código: objetivo, restrições, escolhas relevantes e critérios de sucesso. Também separa planejamento, implementação e validação, mantendo o humano responsável pela aceitação.

O SDD Fast preserva essa base, mas reduz a quantidade e a longevidade dos documentos.

### Matt Pocock: práticas pequenas e combináveis

O repositório *Skills for Real Engineers* critica métodos que tentam controlar todo o processo. Em seu lugar, organiza práticas menores e combináveis para problemas concretos: alinhamento, linguagem de domínio, TDD, diagnóstico, design e revisão de código.

As ideias mais importantes incorporadas ao SDD Fast são:

- alinhar antes de implementar;
- trabalhar em pequenas mudanças com feedback rápido;
- usar testes e outras evidências para fechar o ciclo;
- revisar fidelidade à intenção e qualidade técnica separadamente;
- transformar uma prática em skill somente quando ela for recorrente.

O SDD Fast não exige instalar um conjunto de skills. Skills são extensões opcionais do método, não pré-requisitos.

### Attekita Dev: um fluxo profissional visível

O vídeo apresenta, na prática, o fluxo de skills do repositório de Matt Pocock: aprofundar o problema, consolidar uma especificação, decompor o trabalho e implementar com verificação. Ele é útil por mostrar que o valor não está em um prompt mágico, mas na passagem explícita entre alinhamento, execução e prova.

O SDD Fast retém essas transições, mas não obriga que cada uma produza um arquivo ou invoque uma skill diferente. Para uma tarefa comum, `CURRENT_TASK.md` é suficiente.

### Fabio Akita: o antídoto contra cerimônia e falsa fonte da verdade

A crítica do Akita destaca que especificações detalhadas podem se tornar programas escritos em prosa: continuam ambíguas, não compilam e tendem a apodrecer depois de mudanças diretas no código. Ele também argumenta que loops com verificação são, essencialmente, testes e revisão, e que superorquestração adiciona custo e modos de falha.

O SDD Fast aceita o núcleo dessa crítica:

- a tarefa não descreve todo o sistema;
- a especificação não substitui código, testes ou conhecimento técnico;
- documentos temporários não precisam permanecer sincronizados para sempre;
- agentes adicionais, grafos e skills não são requisitos do desenvolvimento cotidiano;
- uma nova etapa só é aceita se reduzir um problema observável.

## A decisão central

O curso se aproxima de **spec as source of truth**: a especificação orienta e deve permanecer coerente com a implementação. O SDD Fast adota **spec anchored development**:

| Elemento | Papel no SDD Fast |
|---|---|
| `AGENTS.md` | Contrato permanente e pequeno do projeto |
| `CURRENT_TASK.md` | Âncora temporária da intenção, dos limites e da validação |
| Código | Comportamento executável atual |
| Testes, métricas e evals | Evidência do comportamento e da qualidade |
| `tasks/` | Histórico da intenção no momento da entrega, sem obrigação de sincronização futura |
| Git | Histórico técnico e mecanismo de revisão das mudanças |

Assim, não existe uma única fonte da verdade para perguntas diferentes. Cada artefato responde à pergunta para a qual é mais confiável.

## Premissas do curso e decisões do SDD Fast

Legenda:

- **Mantida**: permanece essencialmente igual.
- **Simplificada**: o objetivo foi preservado com menos artefatos ou etapas.
- **Substituída**: o problema é resolvido por outro mecanismo.
- **Opcional**: usada apenas quando contexto, risco ou escala justificarem.
- **Retirada**: não faz parte do método padrão.

| Premissa ou prática do curso | Decisão | Como aparece no SDD Fast | Motivo |
|---|---|---|---|
| Evitar vibe coding | Mantida | Intenção, limites e validação são definidos antes da implementação | Código rápido sem contrato e sem prova aumenta retrabalho e dívida técnica |
| Registrar contexto que o agente não consegue inferir | Mantida | Contrato do projeto em `AGENTS.md` | Contexto organizacional, restrições e comandos reais não estão necessariamente no código |
| Separar contexto do projeto e contexto da feature | Mantida | `AGENTS.md` e `CURRENT_TASK.md` | Informações estáveis e temporárias possuem ciclos de vida diferentes |
| Criar uma constituição do projeto | Simplificada | Um contrato curto dentro de `AGENTS.md` | Evita três documentos permanentes e mantém junto o que o agente precisa ler |
| Manter `mission.md` | Substituída | Objetivo e limites duráveis entram no contrato do projeto ou README | Um arquivo separado só agrega valor quando a missão exige discussão própria |
| Manter `tech-stack.md` | Substituída | Restrições tecnológicas duráveis entram em `AGENTS.md`; detalhes ficam no projeto | Versões, dependências e comandos devem ser inferidos de arquivos executáveis sempre que possível |
| Manter `roadmap.md` | Retirada do núcleo | Roadmap pode existir na ferramenta de produto ou gestão adotada pelo time | Prioridades mudam, nem toda tarefa futura precisa entrar no contexto do coding agent e o método não deve competir com a gestão do produto |
| Tratar a constituição como documento vivo | Mantida | `AGENTS.md` muda quando o contrato permanente realmente muda | Regras estáveis precisam evoluir, mas não a cada tarefa |
| Transformar um item do roadmap em feature | Substituída | O humano escolhe a próxima mudança de valor e cria `CURRENT_TASK.md` | Desacopla desenvolvimento do formato de planejamento usado pela organização |
| Criar branch por feature | Opcional | Segue a política Git do time | Branch é estratégia de integração, não requisito para alinhar um agente |
| Criar pasta datada por feature | Substituída | Uma tarefa ativa e arquivo sequencial após conclusão | Reduz navegação e mantém o histórico simples |
| Produzir `requirements.md` | Simplificada | “O que fazer” e “O que não fazer” | Preserva comportamento e limites sem narrativa extensa |
| Produzir `plan.md` | Retirada do núcleo | Plano curto pode aparecer no chat ou no checkpoint quando necessário | Planos detalhados envelhecem rapidamente e frequentemente repetem implementação óbvia |
| Produzir `validation.md` | Simplificada | “Como validar” em `CURRENT_TASK.md` | A validação precisa acompanhar a tarefa, mas não exige um documento separado |
| Entrevistar o humano antes de especificar | Simplificada | Perguntas apenas sobre ambiguidades que alterem comportamento, arquitetura, risco ou escopo | Uma entrevista exaustiva em toda tarefa reduz velocidade e pode antecipar decisões irrelevantes |
| Revisar e aprovar a especificação antes de codificar | Mantida | Aprovação do `CURRENT_TASK.md` | O humano continua responsável pela intenção e pelos limites |
| Separar “o que/por que” de “como” | Mantida | A tarefa descreve resultado; o agente escolhe detalhes reversíveis | Evita microgerenciar o agente e registrar código em prosa |
| Usar a especificação como fonte oficial da feature | Redefinida | A tarefa é fonte da intenção aprovada; código e evidências representam o estado atual | Uma spec arquivada não deve competir com o comportamento executável depois de futuras mudanças |
| Implementar por grupos de tarefas | Simplificada | Pequenas entregas verticais e verificáveis | A unidade útil é uma mudança observável, não um checklist de atividade técnica |
| Permitir implementar uma feature inteira quando pequena | Mantida | Uma `CURRENT_TASK.md` pode ser concluída em uma sessão | Evita decomposição artificial |
| Dividir features grandes | Mantida | Dividir em tarefas verticais sequenciais | Diffs menores melhoram entendimento, feedback e reversibilidade |
| Validar a implementação contra a especificação | Mantida | Revisão de escopo compara o diff com `CURRENT_TASK.md` | Impede que velocidade substitua fidelidade |
| Validar qualidade além do funcionamento | Mantida | Revisão de qualidade procura complexidade, dependências e riscos desnecessários | Uma solução pode atender ao pedido e ainda degradar o sistema |
| Executar testes e verificações reais | Mantida | “Como validar” exige evidência executada | Declaração do agente não substitui prova |
| Usar a mesma validação para qualquer projeto | Retirada | A evidência varia entre software, ML, causalidade e agentes | Teste unitário não mede sozinho generalização, identificação causal ou qualidade semântica |
| Replanejar entre features | Simplificada | Aprendizados relevantes atualizam tarefa, contrato, teste ou skill | Melhoria é contínua; não precisa de uma cerimônia obrigatória entre entregas |
| Sincronizar specs e código | Redefinida | Apenas a tarefa ativa precisa refletir o trabalho atual | Arquivos arquivados são registro histórico, não documentação operacional |
| Versionar specs e código juntos | Mantida | Todos os artefatos úteis permanecem no Git | Permite revisar a intenção junto do diff que a implementou |
| Fazer commits pequenos | Mantida como prática | Commits acompanham mudanças coerentes e revisáveis | Melhora revisão e recuperação, sem exigir um commit por item burocrático |
| Preservar contexto entre sessões | Mantida | Contrato, tarefa e checkpoint curtos | Continuidade é necessária, mas histórico integral de conversa não é contexto de alta qualidade |
| Usar checkpoint para continuidade | Simplificada | Estado atual, próximo passo e bloqueio | Não deve virar diário de comandos ou duplicação do Git |
| Manter o humano como arquiteto e responsável final | Mantida | Humano aprova escopo e resultado | O agente amplia execução, mas não assume responsabilidade técnica ou de negócio |
| Autorizar comandos e ações do agente com cuidado | Mantida | Regras de segurança ficam no harness e no contrato do projeto | Autonomia deve respeitar risco, credenciais e reversibilidade |
| Fazer reengenharia de contexto em projetos legados | Mantida | Agente examina código, testes e docs antes de definir a tarefa | Em brownfield, o comportamento existente é parte essencial do contrato |
| Executar grandes partes do roadmap quando o contexto amadurecer | Não recomendada como padrão | Só ocorre se ainda formar uma tarefa pequena e verificável | Velocidade de geração não elimina risco de um diff grande e difícil de revisar |
| Automatizar o workflow com skills | Opcional | Uma prática recorrente e comprovada pode virar skill | Evita criar conhecimento e manutenção antes de existir demanda real |
| Criar skills locais ou globais | Mantida como possibilidade | Skill de projeto para domínio local; skill global para prática reutilizável | Mantém portabilidade sem carregar conhecimento irrelevante em todas as tarefas |
| Invocar skills conforme a necessidade | Mantida | Carregamento sob demanda | Reduz contexto e permite combinar somente as capacidades úteis |
| Tornar o processo independente do agente e do editor | Mantida | Markdown simples, Git e comandos do próprio projeto | Evita dependência desnecessária de um harness específico |
| Usar especificações para amplificação controlada | Mantida com limite | Poucas decisões orientam o agente, mas o diff permanece pequeno | Amplificação sem um limite de tamanho reduz a capacidade humana de revisão |
| Usar prompts curtos para tarefas simples | Mantida | O método mínimo usa dois pedidos curtos e os arquivos do projeto | Nem toda mudança justifica uma cerimônia completa |

## Adaptação para Data Science, ML, inferência causal e agentes

O curso trata principalmente de desenvolvimento de software. No trabalho de Data Science, “funciona” pode significar coisas diferentes. Por isso, o SDD Fast substitui a ideia de uma suíte universal de testes pela menor evidência confiável adequada à afirmação feita.

| Tipo de entrega | Evidência principal |
|---|---|
| Transformação determinística | Teste com entrada e saída conhecidas |
| Modelo de ML | Baseline, split adequado, leakage, métricas e análise dos cortes relevantes |
| Inferência causal | Estimand, identificação, pressupostos, overlap e análises de sensibilidade aplicáveis |
| Tool de agente | Schema, resultado normal, vazio, erro e preservação dos dados retornados |
| Routing ou grafo | Caminhos, transições, parada, fallback e estado |
| Resposta de LLM | Evals baseadas em fatos, critérios e uso correto de tools |
| Exploração | Resultado reproduzível e decisão que o experimento permite tomar |

Essa adaptação evita dois erros opostos: dispensar validação porque o trabalho é experimental ou exigir testes unitários onde métricas, desenho experimental e análise de pressupostos são as evidências corretas.

## O que o SDD Fast deliberadamente não promete

- Não garante que o agente interpretará corretamente uma tarefa ambígua.
- Não substitui conhecimento de engenharia, ciência de dados ou domínio.
- Não torna código gerado automaticamente confiável.
- Não define gestão de produto, priorização ou governança organizacional completa.
- Não exige TDD em todo tipo de trabalho.
- Não transforma toda prática útil em documento, skill, agente especializado ou grafo.
- Não é uma metodologia comprovada por estudo experimental; é uma síntese pragmática que deve ser avaliada pelo resultado no time.

## Critério para evoluir o método

Uma nova regra, etapa, skill ou artefato só deve entrar no SDD Fast quando houver resposta clara para estas perguntas:

1. Qual falha recorrente ela resolve?
2. Qual evidência mostrará que resolveu?
3. O benefício supera o custo de criação, leitura e manutenção?
4. Ela precisa ser obrigatória ou pode ser acionada somente quando relevante?
5. Já existe código, teste, Git ou ferramenta do time que resolve o mesmo problema?

Se essas respostas não forem claras, o método não cresce.

## Referências utilizadas

- [DeepLearning.AI — Spec-Driven Development with Coding Agents](https://www.deeplearning.ai/courses/spec-driven-development-with-coding-agents/)
- [Repositório de materiais do curso](https://github.com/https-deeplearning-ai/sc-spec-driven-development-files)
- [Matt Pocock — Skills for Real Engineers](https://github.com/mattpocock/skills)
- [Attekita Dev — O Fluxo de Skills que faz a IA Programar Como um Engenheiro de Verdade](https://www.youtube.com/watch?v=SreK3gB6Gso)
- [Fabio Akita — Hot take: Harness, Loop Engineering, Graph Engineering são Bullshit](https://akitaonrails.com/2026/08/18/hot-take-harness-loop-engineering-graph-engineering-sao-bullshit/)

## Conclusão

O SDD Fast não é uma versão apressada do SDD. É uma escolha de fronteira:

- especificar intenção, não reescrever o sistema em prosa;
- planejar até reduzir o risco relevante, não até eliminar toda incerteza;
- implementar em pequenos incrementos, não em grandes gerações difíceis de revisar;
- validar com evidência adequada, não com confiança na resposta do agente;
- preservar conhecimento útil, não todo o processo que o produziu.

O objetivo é aumentar a velocidade de aprendizado e entrega sem abrir mão de controle, engenharia e responsabilidade humana.
