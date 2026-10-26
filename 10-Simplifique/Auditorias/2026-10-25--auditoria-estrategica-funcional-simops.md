---
tipo: auditoria-estrategica-funcional
sistema: SimOps
data: 2026-10-25
status: concluida
escopo: artefato-publico-runtime-dados-automacoes-codigo
---

# Auditoria estratégica e funcional — SimOps

## Escopo e método

Auditoria realizada sobre o estado efetivo em 25/10/2026, distinguindo código local, artefato publicado, dados e rotinas em execução.

Evidências principais:

- artefato público `https://daily.simplifiqueops.com.br`, saudável e servindo exatamente os assets do commit `e798723`;
- leitura autenticada dos endpoints operacionais com sessão temporária removida ao final;
- SQLite `data/users.db` e seus read models/ledgers;
- snapshots reais de Notion, Monday, Comercial, Radar, Zernio e saúde;
- timers e serviços `systemd --user`;
- jobs Hermes de fechamento, Radar e fila social;
- suíte isolada do commit publicado: 302 testes aprovados;
- suíte do worktree atual: 318 testes aprovados, mas com alterações ainda não publicadas;
- validação visual por screenshot não executada porque o Chromium local não inicia sem `libatk-1.0.so.0`.

## Matriz de auditoria

| Funcionalidade ou requisito | Módulo relacionado | Status | Evidência concreta | Limitação identificada | Impacto operacional | Prioridade |
|---|---|---|---|---|---|---|
| Visão executiva da empresa | Visão geral | Atende parcialmente | `GET /api/executive-overview`; Operação e Comercial retornaram dados atuais | Marketing estava indisponível; não existe Financeiro | Não oferece visão completa da empresa em uma tela | P0 |
| Prioridades pessoais por urgência | Meu painel | Atende | `GET /api/my-panel`: 57 demandas, agrupadas por atraso, hoje, pendência externa, andamento e sem data | 44/57 estão sem data; prioridade fica pouco discriminada | Exige interpretação manual de grande parte da fila | P0 |
| Kanban por status canônico | Meu painel/Kanban | Atende | 12 status canônicos; 57/57 demandas elegíveis; assets públicos iguais ao commit `e798723` | Sem drag-and-drop por decisão de segurança; usa seletor | Execução diária já é possível sem base paralela | P1 |
| Alteração segura de status | Worker Notion | Atende | `POST /api/my-panel/status`; 23 requests históricos `reconciled`; timer ativo; concorrência otimista `GET/PATCH/GET` | Depende do snapshot e worker; não é instantâneo | Mutação confiável sem expor credencial no web app | P1 |
| Inventário de demandas | Demandas | Atende parcialmente | `GET /api/demands`: 88 abertas e 151 conclusões disponíveis | Diverge do escopo pessoal de 57 e contém 9 sem responsável; exige melhor distinção de escopo | Pode confundir inventário geral com foco pessoal | P1 |
| Contexto de projeto e carteira | Projetos/EDCs | Atende parcialmente | `GET /api/projects-overview`: 4 projetos contratados e 2 diagnósticos separados | Todos os quatro projetos aparecem em atenção; 5 EDCs estão vencidos pelo limiar de 7 dias | A central mostra contexto, mas parte dele pode estar desatualizada | P0 |
| Projeto corretamente associado às demandas | Notion/read model | Atende parcialmente | Meu painel: 57 itens por chave estável | 24/57 aparecem como `Projeto não informado` | Reduz leitura por cliente, capacidade e responsabilização | P0 |
| Prazos e responsáveis confiáveis | Notion/EDC | Atende parcialmente | Owner e datas não são inventados; 57 itens explicitamente atribuídos a Pablo | 44/57 sem prazo; no inventário geral, 9/88 sem responsável | Impede planejamento de capacidade e antecipação consistente | P0 |
| Alertas e fila de atenção | Atenção/Inteligência | Atende parcialmente | `GET /api/attention-queue`: 31 itens; `GET /api/intelligence`: 4 ações do Pablo, 2 projetos parados, 6 em risco, 15 dependências, 23 decisões | Regras são heurísticas de estado; não há deduplicação gerencial comprovada entre todas as listas | Exceções existem, mas ainda podem gerar ruído e manutenção mental | P1 |
| Antecipação de atrasos e gargalos | Overview/Métricas | Atende parcialmente | 4 atrasadas, 3 bloqueadas/externas e WIP 11 contra limiar 5 | Detecta sinais atuais; não prevê capacidade, tendência ou impacto futuro | Ajuda a reagir cedo, mas não faz planejamento preditivo | P1 |
| Planejamento de capacidade e agenda | SimOps | Não atende | Nenhum endpoint de agenda/capacidade; Notion Calendar e Google Calendar não são lidos pelo app | Sem compromissos reais, disponibilidade ou carga por período | Prioridades não viram plano executável de tempo | P0 |
| Histórico operacional auditável | Atividade/ledger | Atende parcialmente | SQLite: 139 eventos desde 25/09; 162 registros observados; `GET /api/activity` | Polling pode perder transições intermediárias; autoria e causalidade não são conhecidas | Há rastreabilidade de mudanças, mas não desempenho completo | P1 |
| Métricas de execução | Métricas | Atende parcialmente | `GET /api/metrics`: cobertura e carga atual por projeto | Tempo em status, ciclo, throughput, SLA e tendência permanecem indisponíveis | Não permite gerir produtividade ou previsibilidade por resultado | P1 |
| Saúde das integrações | Sistema | Atende parcialmente | `GET /api/integration-health`; snapshot recente; Notion, Monday, Comercial e ledger saudáveis | Estado geral `attention`; reconciliação antiga com 49 chaves não resolvidas; artefatos local/público divergentes | Problemas ficam visíveis, mas alguns permanecem sem correção automática | P0 |
| Reconciliação entre fontes | Reconciliação | Não atende no estado atual | Snapshot de 18/09, cerca de 900 h de idade, 49 chaves não resolvidas | Evidência vencida não sustenta consistência atual entre EDC e tracker | Pode haver itens sem vínculo ou leitura executiva incompleta | P0 |
| Atualização automática de demandas | Notion/Monday | Atende | `daily-notion-sync.timer` ativo a cada 15 min; fontes atuais com 137 Notion e 21 Monday | Monday é ponte de origem; Notion continua canônico | Reduz manutenção manual e centraliza a execução | P1 |
| Fechamento diário do estado | Hermes/Vault | Atende | Cron `Fechamento Notion → EDC`, 18h30, último status `ok` | Resultado depende da qualidade dos vínculos e dos EDCs | Mantém memória consolidada, mas herda lacunas de reconciliação | P1 |
| Gestão comercial | Comercial | Atende parcialmente | `GET /api/commercial`; snapshot atual com 5.071 registros, 59 follow-ups, 3 propostas/negociações e 29 parados há 14+ dias | 5.007 aparecem como sem contato; dado amplo demais para decisão rápida; módulo é somente leitura | Existe visibilidade, mas o volume reduz foco comercial e geração de receita | P0 |
| Gestão financeira executiva | Financeiro | Não atende | Não há rota, interface, tabela ou ingestão financeira no SimOps | Caixa, receita, despesas, contas, planejamento, ROI e ROAS ausentes | Impede que o SimOps seja central de comando empresarial | P0 |
| Radar e fila social | Social/Radar | Não atende no runtime atual | Snapshot tem 2 tópicos e cron do Radar está `ok`; `GET /api/social` retorna snapshot inválido e 0 tópicos | O produtor emitiu formatos com 82/86 caracteres; loader aceita no máximo 80 | A automação roda, mas o resultado não chega à decisão no painel | P0 |
| Analytics orgânico | Social Analytics | Não atende no runtime atual | Coletor horário ativo e snapshot com 365 dias declarados/28 dias comuns observados | Artefato público exige contrato de 30 dias; host passou a gravar 365 dias a partir de código local não publicado; endpoint retorna `invalid` | Gráficos e métricas ficam indisponíveis apesar da coleta bem-sucedida | P0 |
| Stories e mídia paga | Social/Ads | Não atende | Nenhum contrato publicado para Stories/Ads | Stories sem histórico persistido; Meta Ads não conectada; CPC, CPA, ROI e ROAS indisponíveis | Não há visão completa de marketing e aquisição | P1 |
| Pipeline de conteúdo | Social/SQLite | Atende parcialmente | 71 requests; 24 `ready`, 1 `copy_review`, 46 descartados; gates de aprovação e outbox | Publicação e resultado continuam em sistemas externos; Radar atual está quebrado | Fluxo existe, mas não fecha aprendizado e resultado no painel | P1 |
| Fila pessoal de Threads | Marketing/Threads | Atende parcialmente | 31 agendados, 21 rejeitados, 17 aguardando agendamento; snapshot do provedor recente | Worker de agendamento está intencionalmente pausado; 17 requests permanecem pendentes | Backlog não avança automaticamente | P1 |
| IA gerencial conversacional | SimOps | Não atende | Não existe rota, interface ou serviço de pergunta/resposta com recuperação de fontes | A aba Inteligência é determinística, não conversacional; Hermes opera fora do SimOps | Não é possível consultar a central por linguagem natural dentro do produto | P0 |
| Rastreabilidade e prevenção de invenção | Arquitetura/read models | Atende | Fontes canônicas explícitas, campos ausentes como `—`, snapshots sanitizados, autenticação, CSRF e validação fail-closed | Contratos rígidos sem coordenação de versão causaram indisponibilidades reais | Alta confiabilidade semântica, mas baixa tolerância a evolução não coordenada | P0 |
| Segurança do web app | Autenticação/Compose | Atende | Login, sessão, CSRF, CSP, headers, container read-only, sem credenciais de provedor no request path | 47 sessões expiradas continuam armazenadas; higiene, não quebra funcional | Boa base de segurança; limpeza periódica pode reduzir resíduo | P2 |
| Controle de versão e deploy | Git/Compose/systemd | Atende parcialmente | Público serve exatamente `e798723`; 302 testes do commit publicado passaram | Worktree tem 11 arquivos modificados; timers executam scripts diretamente desse worktree mutável; saúde acusa divergência | Código não publicado já altera produtores reais e quebra consumidores publicados | P0 |
| Usabilidade e acessibilidade | Frontend | Atende parcialmente | Navegação única, responsividade, controles acessíveis, tabelas e estados de erro cobertos por testes | Verificação visual renderizada não pôde ser concluída; há muitas abas e filas concorrentes | Estrutura é utilizável, mas ainda exige escolha entre superfícies sobrepostas | P1 |

## A. Diagnóstico executivo

O SimOps **já funciona como uma central operacional parcial**, sobretudo para demandas, projetos, exceções, comercial em leitura e saúde de integrações. Ele ainda **não funciona como central de comando completa da Simplifique**.

A lacuna não é ausência de código em geral. O problema é que a cadeia gerencial ainda não fecha em quatro pontos:

1. **Financeiro inexistente** no produto.
2. **IA gerencial não incorporada** ao SimOps.
3. **Planejamento temporal/capacidade ausente**.
4. **Contratos e fontes com drift operacional**, que hoje deixam Marketing e Analytics indisponíveis.

Abrindo o SimOps hoje, é possível saber em poucos minutos:

- quantas demandas estão ativas, atrasadas, em andamento e bloqueadas;
- quais demandas são de Pablo e alterar seus status com segurança;
- quais projetos, riscos, dependências e decisões exigem atenção;
- quais follow-ups e propostas existem no comercial.

Não é possível saber com a mesma confiabilidade:

- a situação financeira;
- o plano de caixa e resultado;
- a agenda e capacidade real;
- o desempenho social atual, porque os contratos estão incompatíveis;
- uma resposta gerencial sintetizada por IA dentro do sistema;
- o fluxo completo de planejamento até resultado econômico.

## B. Capacidades comprovadas

- Artefato público saudável e identificado pelo commit `e798723`.
- 302 testes aprovados no commit publicado.
- 57 demandas pessoais atuais; 57/57 elegíveis para alteração de status.
- 12 estados canônicos do Notion e read-back seguro via worker.
- 23 mudanças de status já reconciliadas no banco.
- 4 projetos contratados separados de 2 diagnósticos/prospects.
- 139 eventos operacionais preservados desde o baseline.
- Notion, Monday, Comercial, status worker, coleta social e snapshot do Threads automatizados por timers.
- Fechamento Notion → EDC, Radar e fila social agendados pelo Hermes.
- Comercial atual, com listas limitadas e regras explícitas.
- Segurança fail-closed, autenticação, CSRF, CSP e separação de credenciais do processo web.

## C. Lacunas críticas

1. **Financeiro ausente.** Sem caixa, receitas, despesas, planejamento, ROI e ROAS, a central não responde pela empresa inteira.
2. **Marketing quebrado no runtime.** O Radar gerou 2 pautas, mas o loader recusou o contrato; analytics também está inválido por incompatibilidade 30 × 365 dias.
3. **Código local afeta produção sem deploy.** Timers executam o worktree mutável; isso quebrou o contrato do snapshot social publicado.
4. **Reconciliação vencida.** A evidência tem cerca de 900 horas e 49 chaves não resolvidas.
5. **Dados incompletos para planejamento.** 77,2% da fila pessoal não tem prazo e 42,1% não tem projeto documentado.
6. **IA não existe dentro do SimOps.** Hermes consegue operar externamente, mas o produto não oferece perguntas gerenciais fundamentadas.
7. **Sem agenda/capacidade.** O sistema identifica demanda, mas não transforma a fila em plano de tempo.
8. **Sem métricas históricas maduras.** Não há ciclo, throughput, SLA ou tendência comprovados.

## D. Funcionalidades existentes subutilizadas

- `GET /api/attention-queue` já reúne 31 exceções de Operação, Comercial, Sistema e Marketing; deveria ser a fila principal de decisão, não mais uma aba secundária.
- O ledger possui 139 eventos e janela de um mês; já pode sustentar auditoria de mudanças e, após melhorar cobertura, métricas provisórias.
- Há 24 conteúdos em `ready` e 1 em `copy_review`; o gargalo atual parece estar depois da produção, não na geração de pauta.
- O histórico de 151 conclusões está disponível, mas ainda não é convertido em leitura de resultado ou capacidade.
- A saúde das integrações detectou corretamente a divergência local/público e a reconciliação vencida; falta transformar alertas P0 em ação operacional controlada.
- A Inteligência determinística já estrutura riscos, dependências, mudanças e decisões; ela pode ser usada como camada de recuperação para uma futura IA, sem começar do zero.

## E. Plano de evolução

### P0 — Essencial para operar diariamente e gerar receita

1. Restaurar o contrato do Radar e fazer as 2 pautas atuais aparecerem no SimOps.
2. Corrigir a incompatibilidade de analytics e impedir que timers executem código não publicado; produtores devem rodar por release versionada.
3. Atualizar a reconciliação e resolver/classificar as 49 chaves.
4. Criar a base financeira canônica no Notion e uma visão read-only no SimOps: caixa realizado/previsto, receitas, despesas, contas e planejamento.
5. Tornar obrigatórios ou operacionalmente tratados `projeto` e `prazo` nas demandas prioritárias; começar pelos 24 sem projeto e 44 sem data.
6. Enxugar o Comercial para oportunidades acionáveis; separar os 5.007 registros sem contato do verdadeiro pipeline prioritário.
7. Criar a primeira consulta gerencial por IA em modo somente leitura, com fontes citadas, timestamp, permissões e resposta fail-closed.
8. Integrar agenda real e criar um plano diário/semana baseado em compromissos e capacidade.

### P1 — Inteligência, previsibilidade e acompanhamento

1. Consolidar a fila de atenção como tela inicial de decisão, deduplicada e limitada.
2. Evoluir o ledger para intervalos completos e liberar métricas provisórias de ciclo, throughput e tempo em status.
3. Implantar histórico de Stories; conectar Meta Ads antes de expor CPC, CPA, ROI ou ROAS.
4. Conectar planejamento financeiro a produto/oferta e canal, somente com receita atribuída e investimento comprovado.
5. Fechar o ciclo planejamento → tarefa → execução → entrega → resultado, preservando a evidência em cada passagem.
6. Retomar o worker pessoal do Threads somente após corrigir e revisar os blockers já conhecidos.
7. Realizar teste visual real em desktop e mobile após restaurar o browser automatizado.

### P2 — Sofisticação

1. Previsão de capacidade e risco por tendência, apenas após histórico suficiente.
2. Cenários financeiros e metas por produto/oferta.
3. Resumos gerenciais automáticos personalizados e comparação entre períodos.
4. Drag-and-drop como melhoria progressiva, mantendo o seletor acessível e o mesmo fluxo seguro.
5. Limpeza automática de sessões expiradas e melhorias de observabilidade/deploy.

## F. MVP operacional

O menor conjunto para usar o SimOps diariamente de forma confiável, sem reconstrução, é:

1. **Estabilizar os releases:** timer não executa worktree sujo; produtor e consumidor são publicados juntos.
2. **Restaurar Marketing e Analytics:** Radar válido e analytics compatível no endpoint público.
3. **Limpar a base de execução:** classificar as 24 demandas sem projeto e tratar as 44 sem prazo por exceção explícita.
4. **Atualizar a reconciliação:** eliminar ou justificar as 49 chaves não resolvidas.
5. **Adicionar Financeiro read-only:** três bases canônicas no Notion e uma tela executiva de caixa, receitas, despesas e planejamento.
6. **Adicionar agenda/capacidade mínima:** compromissos do dia/semana e limite de trabalho em progresso.
7. **Adicionar IA gerencial read-only:** perguntas sobre operação, comercial e financeiro com fonte e data em cada resposta.
8. **Usar a fila de atenção como entrada diária:** no máximo 5–8 decisões/ações realmente prioritárias.

Com esse MVP, o SimOps passa de um bom painel operacional fragmentado para uma ferramenta principal de gestão. Sem esses ajustes, ele continua útil para monitorar e executar demandas, mas não substitui consultas manuais nem oferece visão empresarial completa.
