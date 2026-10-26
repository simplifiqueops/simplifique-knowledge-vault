# SimOps como Central Gerencial da Simplifique — Plano de Correção

> **Para o Hermes:** executar fase a fase, com um único ciclo de edição ativo por vez e revisão fail-closed antes de cada deploy.

**Objetivo:** tornar o SimOps a central diária confiável de acompanhamento gerencial da Simplifique, cobrindo operação, projetos, comercial, financeiro, planejamento e consulta gerencial por IA, sem criar fontes paralelas nem reconstruir a infraestrutura atual.

**Arquitetura:** preservar Notion como fonte operacional, Vault/EDCs como memória consolidada, SQLite como ledger/read model local, snapshots sanitizados como fronteira entre provedores e web app, systemd como agendador host-only e Docker/Traefik como runtime público. Evoluir por contratos versionados e releases imutáveis; nenhum collector ou worker poderá executar código não publicado.

**Tech stack atual reutilizado:** Python stdlib, SQLite, JavaScript sem framework, Docker Compose, Traefik, systemd --user, Notion, Monday, Zernio, Vault/Obsidian e Hermes cron/agents.

---

## 1. Critério de chegada

O plano estará concluído quando, em uma única sessão autenticada do SimOps, Pablo puder:

1. ver em até três minutos o que mudou, o que exige decisão, o que está atrasado e o que precisa acontecer;
2. acompanhar projetos, demandas, responsáveis e prazos a partir das fontes canônicas;
3. alterar status no Notion com confirmação e rastreabilidade;
4. consultar pipeline comercial acionável, sem misturar a base inteira com oportunidades reais;
5. consultar caixa realizado e previsto, receitas, despesas e compromissos financeiros;
6. visualizar agenda e capacidade mínima da semana;
7. consultar uma IA em modo read-only, com fontes e timestamps em cada resposta;
8. confiar que dados inválidos, vencidos ou incompatíveis aparecem como indisponíveis, sem números inventados;
9. verificar que todos os produtores, consumidores e workers pertencem à mesma release publicada.

Não fazem parte do MVP: integração bancária, previsão financeira por ML, drag-and-drop obrigatório, automação de decisões gerenciais, publicação social automática, ou atribuição de ROI/ROAS sem evidência.

---

## 2. Estado inicial comprovado

- Público no commit `e798723`; assets públicos conferidos por hash.
- 302 testes passam no commit publicado.
- Worktree contém alterações não publicadas e é usado diretamente por timers host-only.
- Radar atual: produtor gera 2 tópicos, consumidor público rejeita o snapshot por limite de comprimento divergente.
- Analytics atual: timer produz contrato de 365 dias, consumidor público ainda exige 30 dias; endpoint retorna `invalid`.
- Notion/Meu painel: 57 demandas, 57/57 graváveis, 12 status e 23 mutações históricas reconciliadas.
- Qualidade da fila: 24 demandas sem projeto documentado e 44 sem prazo.
- Reconciliação: snapshot antigo, 49 chaves não resolvidas.
- Comercial: 5.071 registros; 5.007 aparecem como sem contato, o que não representa uma fila executiva útil.
- Financeiro, agenda integrada e IA conversacional não existem no SimOps.
- Ledger: 139 eventos e 162 registros observados; ainda insuficiente para métricas maduras de ciclo/SLA.

---

## 3. Estratégia de execução

### Ordem obrigatória

1. estabilizar release e restaurar funcionalidades quebradas;
2. corrigir confiabilidade e classificação dos dados operacionais;
3. consolidar a superfície diária de decisão;
4. adicionar financeiro mínimo na arquitetura existente;
5. adicionar agenda/capacidade mínima;
6. adicionar IA gerencial read-only;
7. evoluir métricas históricas e marketing avançado.

Nenhuma fase posterior deve compensar falha da anterior. Se a evidência estiver indisponível, a interface deve mostrar `—` e o motivo.

### Cadência

- Um microciclo de implementação por vez.
- TDD: teste falha, implementação mínima, suíte focada, suíte completa.
- Revisão independente única e limitada ao diff da fase.
- Commit isolado por fase.
- Deploy somente após revisão aprovada.
- Verificação pública: health, fingerprint, assets, endpoint autenticado e UI renderizada.
- Rollback por commit/release, nunca por edição manual no servidor.

---

# FASE 0 — Estabilizar produção e restaurar Marketing

**Resultado visível:** Radar e Analytics voltam a funcionar; alterações locais deixam de afetar produção antes do deploy.

**Estimativa:** 3–5 horas de agente ativo; 1 dia corrido incluindo revisão e deploy.

## Tarefa 0.1 — Preservar e separar o worktree atual

**Objetivo:** impedir perda das mudanças existentes e criar uma base limpa de release.

**Ações:**

1. inventariar cada arquivo modificado e classificá-lo por tema: analytics, Threads, sync Notion ou documentação;
2. criar branches/worktrees isolados para cada tema sem misturar mudanças;
3. confirmar que `e798723` permanece reproduzível e com 302 testes verdes;
4. registrar qual código cada timer está executando hoje;
5. não descartar nenhuma alteração sem diff e destino explícitos.

**Evidência de conclusão:** `git status` limpo no worktree de release e diffs antigos preservados em branches isoladas.

## Tarefa 0.2 — Tornar collectors e workers release-bound

**Arquivos prováveis:**

- `/home/simplifique/apps/daily-dashboard/deploy.sh`
- `/home/simplifique/apps/daily-dashboard/install-social-analytics-units.sh`
- `/home/simplifique/apps/daily-dashboard/install-status-units.sh`
- `/home/simplifique/apps/daily-dashboard/install-threads-personal-units.sh`
- `/home/simplifique/apps/daily-dashboard/systemd/*.service`
- testes de instalação correspondentes.

**Abordagem:**

- criar diretório de release imutável ou caminho `current` atualizado atomicamente somente pelo deploy;
- apontar `ExecStart` dos timers para a release publicada, não para o worktree editável;
- incluir fingerprint/revisão da release nos snapshots;
- rejeitar no consumidor snapshot produzido por release incompatível, preservando o último snapshot válido;
- atualizar as units apenas pelo instalador versionado e verificar o read-back do `systemctl --user cat`.

**Testes:**

- unit não referencia worktree mutável;
- deploy atualiza web e producer para a mesma revisão;
- producer incompatível não substitui último snapshot válido;
- rollback restaura producer e consumer juntos.

## Tarefa 0.3 — Corrigir contrato do Radar

**Arquivos prováveis:**

- produtor do Radar em `~/.hermes/skills/creative/simplifique-market-radar/`;
- `/home/simplifique/apps/daily-dashboard/app.py`;
- `/home/simplifique/apps/daily-dashboard/test_app.py`.

**Decisão recomendada:** definir um schema versionado compartilhado e um limite único. Não aumentar o limite apenas no consumidor sem validar o produtor.

**Aceite:**

- o snapshot atual com 2 tópicos passa no validator;
- `GET /api/social` retorna `snapshot_status=available` e 2 tópicos;
- o cron seguinte continua compatível;
- nenhuma chave extra ou texto ilimitado é aceito.

## Tarefa 0.4 — Finalizar corretamente Analytics 365 dias

**Arquivos:**

- `sync_zernio_analytics.py`
- `app.py`
- `static/social-analytics.js`
- `static/style.css`
- `templates/index.html`
- `test_sync_zernio_analytics.py`
- `test_app.py`
- `README.md`.

**Correções obrigatórias já identificadas:**

- escala que preserve variações negativas de seguidores;
- linha interrompida em intervalos sem dados;
- taxa de engajamento somente com numerador e denominador pareados;
- semanas, meses e anos parciais rotulados como parciais;
- anos derivados do período solicitado e também de séries apenas de seguidores;
- rejeição de datas duplicadas;
- Stories e Ads permanecem fora deste release.

**Aceite:**

- endpoint público `available`;
- modos Dia/Semana/Mês/Ano funcionam com tabela exata;
- cobertura atual aparece como provisória, não completa;
- assets públicos correspondem ao commit;
- screenshot em 1366×768, 1920×1080 e mobile.

## Gate da Fase 0

- Radar disponível.
- Analytics disponível.
- Health sem divergência local/público.
- Nenhuma unit executa script de worktree editável.
- Suíte completa e revisão independente aprovadas.

---

# FASE 1 — Confiabilidade e classificação dos dados operacionais

**Resultado visível:** toda demanda pessoal tem contexto suficiente para ser classificada; exceções de qualidade aparecem separadas da prioridade.

**Estimativa:** 4–7 horas de agente ativo, mais decisões humanas sobre itens realmente ambíguos; 1–2 dias corridos.

## Tarefa 1.1 — Atualizar a reconciliação

**Fontes:** Notion, Monday, snapshot compartilhado e EDCs.

**Ações:**

1. gerar uma nova reconciliação somente leitura;
2. classificar as 49 chaves em: resolvida, encerrada, duplicada, sem vínculo, ambígua ou exceção intencional;
3. aplicar automaticamente apenas vínculos unívocos;
4. apresentar ambiguidades para decisão humana;
5. publicar snapshot novo e verificar `unresolved_keys`.

**Aceite:** `unresolved_keys=0` ou cada exceção possui classe, motivo e próxima ação explícitos.

## Tarefa 1.2 — Classificar demandas sem projeto

**Ações:**

- tentar associação somente por `project_name`, tag canônica ou chave de proveniência;
- não inferir projeto por semelhança textual;
- criar classe explícita `Simplifique interno`, `sem projeto validado` ou projeto canônico;
- corrigir origem no Notion quando houver evidência e read-back autorizado.

**Aceite:** nenhuma demanda pessoal aparece como projeto vazio; casos não resolvidos aparecem como `Sem projeto validado`, não como associação inventada.

## Tarefa 1.3 — Tratar ausência de prazo sem inventar datas

**Modelo recomendado:** adicionar um estado de planejamento separado da data:

- `com prazo`;
- `sem prazo deliberado`;
- `backlog`;
- `aguardando terceiro`;
- `precisa de decisão de prazo`.

**Aceite:** as 44 demandas atuais deixam de formar um bloco indiferenciado; nenhuma recebe data inferida.

## Tarefa 1.4 — Reduzir ruído comercial

**Reaproveitar:** `/api/commercial`, snapshot do Notion e listas limitadas existentes.

**Ações:**

- separar contatos/base total de oportunidades ativas;
- definir escopo do pipeline por status comercial comprovado;
- manter os 5.007 registros fora da fila prioritária quando não forem oportunidades;
- mostrar qualidade da base como indicador separado;
- preservar prospect ≠ cliente.

**Aceite:** a tela responde “quem exige ação comercial agora?” sem usar a base inteira como denominador implícito.

## Gate da Fase 1

- reconciliação atualizada;
- 100% das demandas pessoais classificadas por projeto ou exceção explícita;
- ausência de prazo tratada por estado, não por invenção;
- Comercial com fila acionável e qualidade da base separada.

---

# FASE 2 — Superfície diária única de decisão

**Resultado visível:** ao abrir o SimOps, Pablo vê no máximo 5–8 decisões ou ações prioritárias e depois acessa detalhes por área.

**Estimativa:** 3–5 horas de agente ativo; 1 dia corrido.

## Tarefa 2.1 — Reusar a fila de atenção como entrada principal

**Arquivos:**

- `app.py` — `build_attention_queue_payload` e `build_executive_overview_payload`;
- `static/overview.js`;
- `static/attention-tabs.js`;
- `templates/index.html`;
- `static/style.css`;
- `test_app.py`.

**Regras:**

- máximo 8 itens;
- ordenar por consequência comercial, prazo explícito, bloqueio e decisão pendente;
- deduplicar o mesmo problema entre Operação, Sistema e Projeto;
- separar ação de Pablo de alerta de qualidade de dados;
- cada item deve ter motivo, fonte, responsável quando comprovado e próximo passo.

## Tarefa 2.2 — Simplificar navegação sem remover detalhes

- manter Visão geral, Operação, Marketing, Comercial e Sistema;
- mover inventários completos para disclosure/telas secundárias;
- evitar filtros globais redundantes;
- não criar nova tela quando a informação cabe em overview, atenção ou drawer existente.

## Tarefa 2.3 — Definir ritual diário

**Fluxo:**

1. abrir Visão geral;
2. tratar a fila de atenção;
3. escolher no máximo 3 focos;
4. conferir agenda/capacidade quando a Fase 4 existir;
5. atualizar status no mesmo painel;
6. fechamento automático às 18h30.

**Aceite:** teste de uso consegue responder em até três minutos o que mudou, o que está bloqueado e quais são os próximos focos.

---

# FASE 3 — Financeiro executivo mínimo

**Resultado visível:** caixa, receitas, despesas e compromissos da Simplifique disponíveis em modo read-only.

**Estimativa:** 8–14 horas de agente ativo; 2–4 dias corridos, incluindo criação e validação das bases do Notion e entrada dos primeiros dados reais.

## Tarefa 3.1 — Criar contrato canônico no Notion

**Bases já aprovadas:**

1. `Financeiro — Contas`;
2. `Financeiro — Movimentações`;
3. `Financeiro — Planejamento`.

**Princípios:**

- somente Simplifique;
- entrada manual inicialmente;
- caixa realizado e previsto;
- vencimento e pagamento separados;
- valor ausente = `—`, nunca zero;
- ROI/ROAS somente com investimento e receita atribuída comprovados.

**Antes da criação:** confirmar propriedades, relações, opções e exemplos com Pablo; criar apenas após aprovação da estrutura final.

## Tarefa 3.2 — Reusar o padrão de snapshot

**Arquivos prováveis:**

- criar `/home/simplifique/.hermes/tools/notion_finance_sync.py`;
- criar snapshot em `~/.hermes/state/daily-simplifique/notion-finance.json`;
- criar unit/timer host-only;
- montar snapshot read-only no Compose.

**Contrato:** schema fechado, identidade das três fontes, collected_at, data_as_of, cobertura, contas, movimentações e planejamento sanitizados.

## Tarefa 3.3 — Adicionar leitura financeira no SimOps

**Arquivos:** `app.py`, `templates/index.html`, `static/finance.js`, `static/style.css`, `test_app.py`, `compose.yml`, `README.md`.

**Primeiros indicadores:**

- saldo realizado;
- entradas e saídas realizadas no período;
- caixa previsto em 7/30/90 dias;
- contas vencidas e próximas;
- receita e despesa por categoria;
- planejamento versus realizado quando houver cobertura.

**Aceite:** totais reconciliados contra uma amostra manual do Notion e snapshot stale/invalid ocultando valores antigos.

---

# FASE 4 — Agenda e capacidade mínima

**Resultado visível:** compromissos do dia/semana e capacidade disponível ao lado das prioridades.

**Estimativa:** 5–8 horas de agente ativo; 1–2 dias corridos, condicionado a uma leitura real e autorizada do calendário.

## Tarefa 4.1 — Verificar fonte real de agenda

- testar leitura efetiva de Google Calendar ou conector disponível;
- não inferir agenda a partir de datas de Notion;
- se nenhuma leitura real for autorizada, classificar como `não disponível` e interromper a fase.

## Tarefa 4.2 — Snapshot read-only de agenda

- collector host-only;
- eventos sanitizados, sem descrição sensível desnecessária;
- timezone `America/Sao_Paulo`;
- janela hoje + 7 dias;
- freshness e cobertura explícitas.

## Tarefa 4.3 — Planejamento de capacidade

- não criar alocação automática;
- mostrar compromissos, blocos livres e WIP atual;
- permitir selecionar até 3 focos diários;
- manter Pomodoro local como apoio, sem virar tracker.

**Aceite:** plano diário não conflita com compromissos conhecidos e ausência de agenda nunca vira “dia livre”.

---

# FASE 5 — IA gerencial read-only e fundamentada

**Resultado visível:** perguntas gerenciais respondidas com dados do SimOps, fonte e timestamp.

**Estimativa:** 8–14 horas de agente ativo; 2–4 dias corridos após as fontes P0 estarem estáveis.

## Tarefa 5.1 — Criar context pack gerencial

**Reusar:** payloads existentes de overview, atenção, projetos, comercial, financeiro, métricas e saúde.

**Contrato:**

- dados mínimos necessários;
- timestamp e status de cada fonte;
- URLs/paths de evidência sanitizados;
- permissões do usuário;
- limite de tamanho;
- nenhuma credencial;
- nenhuma mutação.

## Tarefa 5.2 — Integrar Hermes fora do request web

**Padrão:** request autenticado → registro SQLite/outbox → worker Hermes → resposta persistida → UI consulta resultado.

**Por quê:** evita tokens, latência e falhas de modelo dentro do processo web.

**Restrições:**

- resposta deve citar fonte e data;
- se a fonte necessária estiver stale/invalid, a resposta deve dizer que não pode concluir;
- IA não pode alterar Notion, financeiro ou agenda nesta fase;
- prompt e saída devem ser auditáveis e limitados;
- perguntas de usuários diferentes não compartilham contexto.

## Tarefa 5.3 — Casos de uso iniciais

1. “O que exige minha atenção hoje?”
2. “Quais projetos estão bloqueados e por quê?”
3. “Quais oportunidades comerciais exigem follow-up?”
4. “Qual é a situação do caixa para os próximos 30 dias?”
5. “O que mudou desde o último fechamento?”

**Aceite:** conjunto de perguntas adversariais prova que a IA recusa inferências sem fonte e não mistura prospect com cliente.

---

# FASE 6 — Métricas históricas, Stories e Ads

**Resultado visível:** tendências e desempenho apenas quando houver cobertura suficiente.

**Estimativa:** posterior ao MVP; dividir em ciclos independentes.

## Métricas operacionais

- aumentar frequência e completude do ledger;
- registrar entrada e saída de status;
- só então liberar tempo em status, ciclo, throughput e SLA;
- sempre exibir janela, sample size e estado provisório.

## Stories

- iniciar persistência de insights por Story;
- não reconstruir passado inexistente;
- exibir histórico apenas a partir da primeira coleta comprovada.

## Ads

- conectar conta Meta Ads e verificar identidade;
- coletar investimento, cliques e conversões separadamente do orgânico;
- CPA requer custo e conversão atribuída;
- ROI/ROAS requer investimento e receita atribuída;
- indisponível = `—`.

---

## 4. Validação transversal

### Testes automatizados

Em cada fase:

```bash
python3 -m unittest discover -s . -p 'test_*.py'
for file in static/*.js; do node --check "$file"; done
python3 -m py_compile app.py *.py
docker compose config >/dev/null
git diff --check
```

### Verificação operacional

- serviço e timer avaliados separadamente;
- oneshot saudável somente com `Result=success` e `ExecMainStatus=0`;
- endpoint autenticado exercitado com sessão temporária removida ao final;
- public health pronto antes de verificar assets;
- hashes dos assets públicos iguais aos da release;
- snapshot read-back após coleta;
- nenhuma credencial em container, snapshot, log ou resposta.

### Verificação visual

- restaurar browser automatizado antes de aprovar mudanças visuais;
- capturas em 1920×1080, 1366×768 e mobile;
- conferir loading, vazio, parcial, stale, invalid e erro;
- teclado, foco e contraste em claro/escuro.

---

## 5. Riscos e controles

| Risco | Controle |
|---|---|
| Worktree altera produção | releases imutáveis e units apontando para `current` atômico |
| Contrato producer/consumer diverge | schema versionado, teste de compatibilidade e último snapshot válido |
| “Limpeza” inventa projeto/prazo | classes explícitas de não resolvido e decisão humana para ambiguidades |
| Financeiro mostra zero falso | `null/—`, reconciliação de amostra e coverage/freshness |
| IA inventa resposta | context pack fechado, citações, recusa em fonte indisponível e sem mutações |
| Mais telas aumentam complexidade | reutilizar overview, atenção, comercial e padrão de snapshots |
| Operação fica cara | stdlib, SQLite, systemd e infraestrutura atual; nenhuma plataforma nova no MVP |
| Projeto vira uma reconstrução | fases reversíveis, escopo YAGNI e deploy por capacidade gerencial concreta |

---

## 6. Marcos e decisão de continuidade

### Marco M0 — Confiabilidade técnica

Fase 0 concluída. O sistema volta a entregar tudo que já deveria entregar sem drift.

### Marco M1 — Uso diário assistido

Fases 1 e 2 concluídas. SimOps pode ser a tela inicial diária, ainda complementado por financeiro e agenda externos.

### Marco M2 — Central gerencial mínima

Fases 3 e 4 concluídas. Operação, comercial, financeiro e agenda estão visíveis no mesmo lugar.

### Marco M3 — Central gerencial com IA

Fase 5 concluída. Perguntas gerenciais são respondidas com evidência e sem mutações.

### Marco M4 — Inteligência histórica

Fase 6 concluída conforme a cobertura real permitir.

---

## 7. Estimativa consolidada

- **M0:** 1 dia corrido.
- **M1:** mais 2–3 dias corridos, incluindo decisões de classificação.
- **M2:** mais 3–6 dias corridos, condicionado à estrutura financeira e acesso de agenda.
- **M3:** mais 2–4 dias corridos após M2.
- **M4:** depende da acumulação de histórico; não deve ser acelerado com dados sintéticos.

Estimativa total até uma central gerencial mínima sem IA: **6–10 dias corridos**, trabalhando faseadamente e com validações. Com IA read-only fundamentada: **8–14 dias corridos**. A estimativa pressupõe respostas rápidas apenas nas ambiguidades de dados e na aprovação do schema financeiro.

---

## 8. Primeira decisão

A execução deve começar exclusivamente pela **Fase 0**. Não iniciar Financeiro, Agenda ou IA enquanto producer/consumer puderem divergir e enquanto Radar/Analytics permanecerem indisponíveis.

Ao concluir a Fase 0, reapresentar:

- mudanças visíveis;
- testes e revisão;
- artefato público verificado;
- estado dos timers;
- riscos remanescentes;
- estimativa atualizada para M1.
