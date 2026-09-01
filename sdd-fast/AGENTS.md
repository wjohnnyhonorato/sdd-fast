# AGENTS.md

## Contrato do projeto

- Problema: <problema que o projeto resolve>.
- Usuário principal: <quem usa o resultado>.
- Resultado esperado: <resultado principal>.
- Invariantes: <regras que nenhuma tarefa pode violar>.
- Base técnica: <tecnologias estruturais e estáveis>.
- Nunca fazer: <comportamentos permanentemente proibidos>.

## Antes de implementar

- Leia `CURRENT_TASK.md`, o código e as validações relacionadas.
- Se não houver tarefa definida, solicite uma ao humano.
- Pergunte somente se uma ambiguidade puder mudar comportamento, arquitetura, risco ou escopo.
- Se não houver ambiguidade material, prossiga sem criar plano ou documentação adicional.

## Implementação

- Faça somente **O que fazer** e respeite **O que não fazer**.
- Trabalhe em uma pequena mudança vertical e verificável.
- Preserve código e comportamento fora do escopo.
- Não adicione dependências, abstrações ou refatorações sem necessidade para a tarefa.
- Se precisar ampliar o escopo ou enfraquecer a validação, pare e solicite aprovação.
- Escreva a solução mais simples que atenda à tarefa, sem código
  especulativo ou abstrações para necessidades futuras.
- Prefira funções pequenas e coesas quando elas representarem
  naturalmente a solução.
- Cada unidade deve ter responsabilidade, entradas e saídas claras.
- Use nomes que expressem a intenção do código.
- Documente contratos, regras de negócio e decisões não evidentes.
- Não adicione comentários ou documentação que apenas repitam o código.
- Divida a implementação quando ela não puder ser compreendida
  e revisada com facilidade.

## Comunicação

- Seja direto e use textos claros e curtos.
- Informe primeiro o resultado ou o bloqueio relevante.
- Evite repetir contexto, código ou instruções já conhecidos.
- Explique somente decisões, riscos e limitações que ajudem o humano a revisar ou decidir.
- Não use textos longos para compensar ausência de evidência.

## Validação

- Siga **Como validar** usando a menor evidência confiável para a mudança.
- Teste comportamento observável por interfaces públicas, evitando detalhes internos.
- Para ML, considere baseline, split, leakage e métricas quando aplicáveis.
- Para causalidade, diferencie associação de efeito causal e valide os pressupostos aplicáveis.
- Para agentes, teste contratos, caminhos, erros, parada e critérios de eval aplicáveis.
- Não declare como executada ou aprovada uma validação que não ocorreu.
- Toda validação deve gerar evidência que um humano consiga
  inspecionar ou reproduzir.
- Informe o procedimento executado, o resultado observável e,
  quando aplicável, onde consultar o artefato gerado.
- Um resumo do agente ou a afirmação de que a validação
  "passou" não constitui evidência suficiente.
- Validações bem-sucedidas não substituem a revisão e a aprovação humana.

## Revisão

Antes de concluir, compare o diff com `CURRENT_TASK.md` e verifique:

- requisito ausente ou implementado incorretamente;
- alteração fora do escopo;
- complexidade, dependência ou abstração desnecessária;
- evidência insuficiente para afirmar que funciona.

Corrija o que estiver no escopo. Para os demais casos, informe ao humano.

## Conclusão

- Conclua somente quando a tarefa estiver atendida, validada e revisada.
- Apresente as alterações, os procedimentos de validação, os resultados observáveis, os artefatos aplicáveis e as limitações.
- Apresente as evidências ao humano e aguarde sua aprovação.
- Após aprovação, mova a tarefa para `tasks/NNN-nome-curto.md`.
- Use o próximo número sequencial, nunca reutilize números e redefina `CURRENT_TASK.md` como sem tarefa.
- Arquivos em `tasks/` são histórico, não descrição atual do sistema.
- Registre aqui somente regras permanentes; problemas recorrentes podem justificar uma regra, teste ou skill.

## Comandos

- Preparar projeto: `<comando do projeto>`
- Executar validações: `<comando de validação>`

