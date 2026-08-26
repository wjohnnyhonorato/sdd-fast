# Prompts mínimos para Code Agents

Prompts para Cursor, GitHub Copilot, Cline, Codex e outros agentes capazes de examinar e alterar um repositório.

Substitua os campos `<...>`. Sempre peça ao agente para ler a constitution e a feature relevante antes de agir.

## Princípios de interação

- O agente propõe; o humano aprova decisões de produto, ciência, risco e arquitetura.
- O agente não inventa requisitos nem altera limiares para acomodar resultados.
- Perguntas devem ser reservadas a ambiguidades que alterem a solução.
- O plano contém somente passos relevantes; detalhes de edição ficam com o agente.
- Evidências são referenciadas por ID ou link, não copiadas integralmente para a spec.

## G1 — Setup Greenfield

```text
Analise este repositório e o contexto fornecido.
Identifique objetivo, usuários, limites, stack, testes, pipelines
e fontes de verdade para código, dados, modelos, prompts e evals.
Separe fatos, inferências e decisões ainda abertas.
Faça perguntas somente sobre ambiguidades que alterem o projeto.
Não crie specs nem implemente código ainda.
```

**Humano:** responde decisões materiais e corrige inferências.

**Saída:** contexto suficiente para criar a constitution.

## G2 — Criar ou revisar a constitution

```text
Crie ou revise spec/constitution.md usando o contexto aprovado.
Inclua apenas Outcome, Scope, Principles, Tech Stack estável,
Roadmap Now/Next/Later, Quality Gates, Sources of Truth,
Definition of Done e Sync Rule.
Não invente decisões nem transforme roadmap em backlog.
Não copie versões disponíveis no lockfile. Limite: cerca de 60 linhas.
Aguarde minha aprovação antes de implementar código.
```

**Humano:** aprova outcome, escopo, stack, roadmap e gates.

## G3 — Criar uma feature spec

```text
Leia spec/constitution.md e o código relacionado à feature <nome>.
Crie spec/features/<id>/<id>.spec.md com Requirements, Plan,
Validation e Act. Use até 7 critérios verificáveis e 3–7 passos.
Inclua somente pressupostos que podem invalidar a solução.
Indique evidências esperadas, sem inventar resultados observados.
Não implemente ainda. Liste decisões que exigem aprovação humana.
```

**Humano:** aprova escopo, pressupostos, critérios e plano.

## M1 — Especializar uma feature de ML

```text
Revise a feature spec como contrato de ML preditivo.
Inclua, de forma compacta: população, unidade e instante da decisão,
target e horizonte, dataset, split, leakage, baseline, métrica,
limiar, cortes críticos, drift e fallback quando aplicáveis.
Não invente valores. Marque decisões ausentes como OPEN.
Mantenha a spec com cerca de 60 linhas.
```

## C1 — Especializar uma feature causal

```text
Revise a feature spec como contrato de inferência causal.
Inclua estimand, tratamento, desfecho, unidade, população,
horizonte, pressupostos/DAG, identificação, overlap,
sensibilidade, validade externa e limiar de decisão.
Não trate associação como causalidade. Marque lacunas como OPEN.
Não implemente o estimador antes da aprovação humana.
```

## A1 — Especializar uma feature de agente/LangGraph

```text
Revise a feature spec como contrato de workflow agentic.
Inclua objetivo, invariantes de estado, tools permitidas/proibidas,
ações com aprovação humana, parada, retries, fallback, eval set,
graders e limites de qualidade, custo, latência e passos.
Referencie versões de prompt/modelo/grafo; não copie seu conteúdo.
Não amplie a autonomia do agente sem aprovação humana.
```

## G4 — Implementar o próximo incremento

```text
Leia a constitution e spec/features/<id>/<id>.spec.md.
Implemente somente o próximo incremento do Plan.
Atualize testes ou evals correspondentes.
Não altere o contrato de aceite sem me avisar.
Ao final, informe arquivos alterados, verificações executadas,
e qualquer divergência encontrada entre código e spec.
```

**Humano:** decide dúvidas de produto, ciência, risco e arquitetura.

## G5 — Executar Check/Validation

```text
Valide a implementação contra cada critério da feature spec.
Execute testes, métricas ou evals aplicáveis.
Classifique cada critério como pass, fail ou inconclusive.
Atualize Validation somente com status e IDs/links das evidências.
Não altere limiares para fazer o resultado passar.
Mostre limitações e critérios ainda sem evidência.
```

**Humano:** avalia validade das evidências e decide o próximo estado.

## G6 — Executar Act/Replan

```text
A validação da feature <id> falhou ou ficou inconclusiva.
Identifique se a causa está no código, dados, hipótese, plano
ou contrato. Proponha a menor correção justificável.
Não reduza métricas ou critérios para acomodar o resultado.
Atualize Act com accept, replan ou stop e a justificativa.
Aguarde aprovação antes de modificar contrato ou código.
```

## S1 — Sincronizar specs e código antes do merge

```text
Compare o diff atual com constitution e feature specs.
Procure mudanças de comportamento, escopo, interfaces, dados,
target/estimand, modelos, prompts, tools, routing e guardrails.
Atualize somente mudanças reais de contrato no mesmo PR.
Não copie detalhes presentes no código, testes ou trackers.
Liste divergências, specs alteradas e critérios sem evidência.
Se não houver impacto, proponha uma justificativa spec-impact: none.
```

**Humano:** confirma que as mudanças foram intencionais e aprova o merge.

## R1 — Revisar constitution e roadmap

```text
Compare features aceitas, interrompidas e abertas com a constitution.
Proponha a menor atualização necessária em Outcome, premissas,
Quality Gates e Roadmap Now/Next/Later.
Não transforme o roadmap em backlog ou histórico de entregas.
Remova conteúdo superado e preserve decisões ainda vigentes.
Aguarde minha aprovação antes de editar a constitution.
```

## B1 — Descobrir um projeto Brownfield

```text
Analise código, testes, configuração, pipelines, dados, modelos,
prompts e observabilidade deste projeto existente.
Reconstrua o comportamento atual em três grupos:
CONFIRMED por código/teste; INFERRED; OPEN para validação humana.
Identifique fontes de verdade e riscos de divergência documental.
Não proponha uma reescrita nem tente documentar todo o legado.
```

## B2 — Criar a primeira spec Brownfield

```text
Com base apenas nos fatos validados do projeto existente,
crie uma constitution mínima e a spec da feature ativa <id>.
Na feature, separe comportamento atual do delta desejado.
Use Requirements, Plan, Validation e Act.
Registre dúvidas como OPEN; não transforme inferências em fatos.
Mantenha cada arquivo com cerca de 60 linhas.
```

## Prompt curto para uma nova sessão

```text
Leia spec/constitution.md e spec/features/<id>/<id>.spec.md.
Informe o estado atual, próximo passo do PDCA e decisões abertas.
Não implemente até confirmar que código e specs estão coerentes.
```

## Prompt curto para encerrar uma sessão

```text
Antes de encerrar, compare alterações, testes e feature spec.
Atualize Validation e Act quando houver evidência.
Sinalize qualquer mudança comportamental ainda não sincronizada.
```
