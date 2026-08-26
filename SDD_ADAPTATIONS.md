# Adaptações do SDD para ML e Agentes

Este documento explica por que o método deste repositório difere do fluxo apresentado no curso da DeepLearning.AI.

O objetivo não foi simplesmente remover conteúdo. A adaptação reduz fontes manuais de verdade, preserva o ciclo de especificação e acrescenta controles necessários para ML, inferência causal e agentes.

## Comparação

| Elemento | Método apresentado no curso | SDD Lean ML | Motivo da alteração | Princípio preservado |
|---|---|---|---|---|
| Constitution | Mission, tech stack e roadmap orientam o projeto | Os três permanecem, resumidos a decisões estáveis | Manter direção com menor custo de revisão | Contexto persistente |
| Tech stack | Registra tecnologias do projeto | Mantém somente escolhas estruturais e difíceis de mudar | Evitar duplicar lockfile e inventário de dependências | Restrições explícitas |
| Roadmap | Organiza a evolução planejada | Usa apenas `Now`, `Next` e `Later`, orientados a resultados | Guiar o projeto sem virar backlog | Direção antes da implementação |
| Artefatos da feature | Requirements, plan e validation aparecem como artefatos distintos | Um `<feature-id>.spec.md` com três seções e uma decisão `Act` | Reduzir arquivos e pontos de divergência sem gerar nomes ambíguos | Requisitos, planejamento e validação continuam separados logicamente |
| Requirements | Documento específico descreve a mudança | Seção curta com intenção, escopo, pressupostos e até 7 critérios | Facilitar revisão humana frequente | Contrato verificável |
| Plan | Artefato próprio orienta o code agent | Seção com 3–7 passos relevantes | Evitar plano detalhado que envelhece antes do código | Implementação orientada pela spec |
| Validation | Artefato próprio descreve a verificação | Seção com evidência esperada, observada e status | Aproximar evidência do critério correspondente | Aceite baseado em prova |
| Ciclo da feature | Planejar, implementar, validar e replanejar | PDCA explícito: Plan, Do, Check e Act | Tornar o ciclo fácil de aplicar e ensinar | Desenvolvimento iterativo |
| Replanejamento | Novo planejamento após feedback da implementação | Atualização da mesma feature spec, com decisão explícita | Evitar versões paralelas da verdade atual | Aprendizado incorporado à spec |
| Resultados de validação | Podem ser descritos no material da feature | A spec guarda status e IDs; resultados completos ficam nas ferramentas | Não duplicar CI, trackers, registries, evals ou traces | Rastreabilidade reproduzível |
| Rigor documental | O processo pode comportar diferentes artefatos conforme o trabalho | Um padrão mínimo; cada profissional acrescenta o necessário | Evitar classificação anterior e fricção | Disciplina mínima comum |
| Revisão humana | O humano revisa decisões e resultados ao longo do fluxo | Responsabilidade humana e condição de parada aparecem em cada etapa e prompt | Evitar delegar decisões materiais ao agente | Controle humano |
| Sincronização | Specs devem acompanhar implementação e feedback | Comparação contínua mais gate `spec-impact` antes do merge | Transformar princípio em procedimento verificável | Spec como fonte de verdade |
| Histórico | Artefatos registram evolução da feature | Git e PR guardam história; specs mostram o estado vigente | Evitar crescimento permanente dos arquivos | Rastreabilidade sem duplicação |
| Brownfield | O fluxo pode ser aplicado sobre projetos existentes | Reconstrói fatos do código/testes e adota SDD por feature | Evitar documentar todo o legado antes de entregar valor | Contexto antes da mudança |
| ML | Método geral de desenvolvimento de software | Adiciona dados, tempo, target, leakage, baseline, métricas, slices e drift | Comportamento de ML depende do sistema de dados e do mundo externo | Critérios verificáveis do domínio |
| Inferência causal | Não é um foco específico do curso | Adiciona estimand, DAG/pressupostos, identificação, overlap e sensibilidade | Separar efeito causal de associação preditiva | Hipótese e validade explícitas |
| Agentes/LangGraph | Code agents são usados para desenvolver software | Acrescenta estado, tools, autonomia, parada, fallback, evals, custo e traces | O agente executa trajetórias não determinísticas e interage com sistemas | Limites e validação observável |

## O que foi consolidado, não removido

O curso separa informações para facilitar o aprendizado do fluxo. Neste método:

- `Requirements` continua definindo o contrato;
- `Plan` continua orientando a execução;
- `Validation` continua verificando o resultado;
- `Act` torna explícita a decisão de aceitar ou replanejar;
- as quatro partes vivem em um único arquivo para serem revisadas juntas.

Separar seções preserva a função de cada informação. Consolidar o arquivo reduz links quebrados, atualizações parciais e divergências entre documentos.

## O que foi deslocado

| Informação | Fonte de verdade escolhida |
|---|---|
| tarefas e andamento diário | issue, PR ou conversa do agente |
| versões exatas de dependências | lockfile |
| resultados de experimentos | experiment tracker |
| versão e estágio do modelo | model registry |
| resultados de testes | CI |
| evals e trajetórias do agente | eval platform e traces |
| histórico de alterações | Git e PR |

A spec mantém somente referências necessárias para localizar essas evidências.

## O que foi acrescentado

O método adiciona controles que não são universais em software tradicional:

- semântica temporal de dados e prevenção de leakage;
- baseline e protocolo de avaliação de ML;
- contrato causal e pressupostos de identificação;
- tools permitidas e proibidas para agentes;
- limites de autonomia e aprovação humana;
- testes de trajetórias, custo, latência e término;
- fallback, monitoramento e resposta a drift.

Esses itens aumentam o rigor onde o código, sozinho, não descreve o comportamento do sistema.

## Limite da adaptação

Não existe uma norma científica única denominada “SDD para ML”. Os tamanhos de arquivo e limites de critérios deste repositório são heurísticas operacionais. Devem ser avaliados pela capacidade de evitar ambiguidade, reduzir retrabalho e manter specs sincronizadas — não pelo cumprimento mecânico de uma quantidade de linhas.

## Referências

1. [DeepLearning.AI — Spec-Driven Development with Coding Agents](https://www.deeplearning.ai/courses/spec-driven-development-with-coding-agents/).
2. [OpenSpec — Concepts](https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md).
3. Sculley, D. et al. [Hidden Technical Debt in Machine Learning Systems](https://proceedings.neurips.cc/paper_files/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf). NeurIPS, 2015.
4. [OpenAI — Evaluate Agent Workflows](https://developers.openai.com/api/docs/guides/agent-evals).
