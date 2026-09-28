# Relatório de clareza e lacunas do Daily Dashboard

**Auditoria:** 27/09/2026, 12:55 (America/Sao_Paulo)  
**Escopo:** Daily publicado, contratos locais, snapshots operacionais e coerência entre Operação, Marketing e Comercial.  
**Restrição:** não houve inspeção visual autenticada em navegador nesta execução porque os dois backends gráficos disponíveis falharam por bibliotecas do sistema ausentes (`libatk-1.0.so.0` e `libXi.so.6`). O artefato publicado foi comparado ao local pelo endpoint público de saúde e apresentou o mesmo fingerprint (`6fe4204f8ed93bed`).

## Síntese executiva

O Daily já apresenta uma arquitetura gerencial consistente: separa Operação, Marketing e Comercial; mantém prospects fora da carteira contratada; declara fontes e indisponibilidades; evita transformar ausência de evidência em zero; e não cria um segundo sistema de execução. O artefato público coincide com o local, os serviços essenciais estão saudáveis e a suíte de 103 testes passou.

As lacunas prioritárias não são de volume de telas. São de confiança operacional: o menu afirma “Daily sincronizado” mesmo quando a saúde consolidada está em atenção; o snapshot comercial está desatualizado; e a reconciliação possui 49 itens pendentes de revisão em evidência antiga. Também falta ligar uma solicitação social marcada como `ready` ao respectivo rascunho editável no Figma.

## O que já aparece

### Visão geral

- Resumo por categorias com Operação, Marketing e Comercial.
- Estado operacional com demandas ativas, em progresso, atrasadas, bloqueadas/externas e histórico de conclusões.
- Sinais de gargalo derivados de regras explícitas, sem inferência de desempenho histórico.
- Estado ausente ou desatualizado aparece como `Indisponível` ou `Atenção`.

### Operação

- **Meu painel:** demandas canônicas do Notion atribuídas explicitamente a Pablo, separadas em atrasadas, vencendo hoje, em progresso, pendências externas/bloqueadas e sem data.
- **Demandas:** execução por projeto, com Notion como fonte canônica e ícones independentes de Notion, Monday e ClickUp.
- **Projetos:** somente carteira contratada, com objetivo, saúde do EDC, fase, atualização, próximo movimento, riscos e demandas ativas.
- **Atividade recente:** mudanças observadas de status e prazo com timestamp da fonte e da detecção, sem atribuir autoria ou causalidade.
- **Métricas:** carga atual e cobertura do ledger; tempo em status, ciclo, throughput, tendência e SLA permanecem corretamente indisponíveis por falta de transições completas.
- **Saúde das integrações:** freshness, contagens, serviços, timers, reconciliação, EDCs e comparação entre artefato local e público.

### Marketing

- Radar Social com fatos, interpretações, hipóteses, riscos, fontes, confiança, decisão e formatos sugeridos.
- Botão **Gerar conteúdo** com aviso explícito de que solicitar não publica.
- Ciclo auditável `queued → in_production → ready`.
- Estado observado: 4 temas no radar, 3 com decisão `produzir` e 2 solicitações em `ready`.

### Comercial

- Prospects separados da carteira contratada.
- KPIs de P1 para contato, sem contato, follow-ups, propostas/negociações, parados há 14 dias e reuniões próximas.
- Listas limitadas a exceções e próximos movimentos, em vez de despejo integral da base.
- Limitações explícitas para responsável, fechamento, cliente, prazo do próximo follow-up, último contato e decisão.

## Lacunas priorizadas

### P0 — Corrigir o sinal global de sincronização

- **O que falta:** o rodapé lateral mostra “Daily sincronizado” e “Notion · Monday · Vault” de forma fixa, enquanto o snapshot consolidado está em `attention`.
- **Evidência atual:** Comercial está desatualizado e Reconciliação está desatualizada; portanto, a afirmação global de sincronização não é sustentada.
- **Fonte canônica:** `data/integration-health.json`, campo `overall.status` e estados por fonte.
- **Risco:** falsa confiança na atualização do Daily e tomada de decisão sobre informação velha.
- **Recomendação:** derivar texto, cor e motivo do indicador global do endpoint `/api/integration-health`; usar “Atualizado”, “Atenção” ou “Indisponível” e exibir o timestamp da última coleta válida.

### P1 — Atualizar e operacionalizar o Comercial

- **O que falta:** snapshot comercial recente e campos estruturados para responsável, data do próximo follow-up, último contato e decisão.
- **Evidência atual:** snapshot gerado em `2026-09-25T12:20:35.764247+00:00`, com 252 registros e idade de 51,5 horas no snapshot de saúde; limite documentado de 36 horas.
- **Fonte canônica:** Notion — base `Propostas - CRM`; snapshot `/home/simplifique/.hermes/state/daily-simplifique/notion-oportunidades.json`.
- **Risco:** priorização comercial com estado desatualizado e sem informação suficiente para determinar quem age, quando e com qual próximo movimento.
- **Recomendação:** executar a coleta comercial vigente; depois, adicionar os campos faltantes primeiro à base canônica e ao produtor do snapshot, medir cobertura real e só então ampliar os cards do Daily.

### P1 — Resolver a reconciliação de demandas

- **O que falta:** revisão e classificação dos 49 registros em `missing_review`.
- **Evidência atual:** reconciliação gerada em `2026-09-18T02:13:37.487191-03:00`, idade observada de 226,6 horas; resumo com 2 registros ativos existentes e 49 pendentes de revisão.
- **Fonte canônica:** `/home/simplifique/.hermes/state/daily-simplifique/notion-demand-reconciliation.json`, com validação posterior no Notion.
- **Risco:** demanda do Vault sem correspondência operacional, vínculo errado ou duplicidade silenciosa.
- **Recomendação:** renovar a reconciliação e apresentar no Daily a decomposição dos 49 itens por motivo verificável: sem chave, concluído no Notion, prospect intencionalmente local, fora do fluxo ou conflito real.

### P1 — Tornar `ready` revisável no fluxo Social

- **O que falta:** o card Social mostra `Pronto`, mas o contrato da tabela `social_content_requests` não armazena URL/ID do artefato, decisão de QA ou contagem de frames.
- **Evidência atual:** existem 2 solicitações em `ready`; a interface exibe apenas estado e data.
- **Fonte canônica:** SQLite `social_content_requests`, outbox processado e read-back do nó/Section no Figma.
- **Risco:** `ready` não leva o usuário ao rascunho que precisa revisar; o estado operacional fica desconectado do entregável.
- **Recomendação:** adicionar ao read model um vínculo verificado de revisão (`figma_url`, `figma_section_id`, `qa_decision`, `updated_at`), escrito pela esteira somente após read-back do Figma. Não transformar isso em aprovação de exportação ou publicação.

### P2 — Corrigir a nomenclatura de diagnósticos

- **O que falta:** o título “Diagnóstico de clientes” contradiz a própria descrição, que afirma serem prospects.
- **Fonte canônica:** política comercial da Simplifique e estado de contratação explícita no CRM/EDC.
- **Risco:** apresentar prospect como cliente por linguagem, mesmo que o payload mantenha a separação técnica correta.
- **Recomendação:** renomear para “Diagnósticos comerciais” ou “Prospects em diagnóstico”.

### P2 — Manter métricas históricas em espera até haver evidência

- **O que falta:** transições completas e comparáveis para tempo em status, ciclo, throughput, tendência, atraso recorrente e SLA.
- **Evidência atual:** ledger com baseline em 25/09/2026, 102 registros observados e apenas 1 evento; há 50 conclusões locais legadas, que não equivalem a transições completas.
- **Fonte canônica:** ledger `demand_events`, timestamps da fonte e da detecção, mais regra formal de SLA quando existir.
- **Risco:** ativar indicadores prematuramente e apresentar zeros ou tendências sem base temporal.
- **Recomendação:** manter a coleta após cada sincronização válida; publicar métricas somente quando houver entrada e saída observadas para a mesma demanda, janela e amostra declaradas.

### P2 — Tornar atualização e freshness visíveis no cabeçalho

- **O que falta:** o cabeçalho possui espaço para atualização, mas a comunicação global ainda depende de textos genéricos como “Atualização automática”.
- **Fonte canônica:** timestamps dos snapshots e `integration-health.json`.
- **Risco:** o usuário não distingue atualização do código, atualização da tela e freshness dos dados.
- **Recomendação:** exibir “Dados verificados em …” com o pior estado relevante e manter timestamps específicos dentro de cada área.

## Estado técnico verificado

- Artefato público: `https://daily.simplifiqueops.com.br/health` respondeu `status: ok` e fingerprint `6fe4204f8ed93bed`.
- Artefato local: mesmo fingerprint do público.
- `daily-dashboard.service`: `active/running`, último resultado `success`.
- `daily-notion-sync.service`: `inactive/dead` após execução `oneshot`, com `Result=success` e `ExecMainStatus=0`.
- `daily-notion-sync.timer`: `active/waiting`.
- Notion: 89 registros, evidência dentro do limite.
- Origem Monday: 13 registros, evidência dentro do limite.
- EDCs desatualizados: 0 pela regra atual de 7 dias.
- Testes: 103 executados, todos aprovados.
- Contrato interno: `python3 app.py check` aprovou 9 projetos; saída atual indicou 7 em atenção e nenhum classificado como crítico ou estável.
- JavaScript: todos os módulos em `static/*.js` passaram em `node --check`.

## Ordem recomendada

1. Remover a mensagem fixa de sincronização e vinculá-la à saúde real.
2. Atualizar o snapshot comercial.
3. Renovar e tratar a reconciliação dos 49 registros.
4. Conectar solicitações Social `ready` ao rascunho validado no Figma.
5. Corrigir “Diagnóstico de clientes”.
6. Continuar acumulando eventos antes de ativar métricas históricas.

## Fontes locais auditadas

- `/home/simplifique/apps/daily-dashboard/templates/index.html`
- `/home/simplifique/apps/daily-dashboard/app.py`
- `/home/simplifique/apps/daily-dashboard/static/overview.js`
- `/home/simplifique/apps/daily-dashboard/static/my-panel.js`
- `/home/simplifique/apps/daily-dashboard/static/projects.js`
- `/home/simplifique/apps/daily-dashboard/static/commercial.js`
- `/home/simplifique/apps/daily-dashboard/static/social.js`
- `/home/simplifique/apps/daily-dashboard/static/activity.js`
- `/home/simplifique/apps/daily-dashboard/static/integration-health.js`
- `/home/simplifique/apps/daily-dashboard/data/integration-health.json`
- `/home/simplifique/apps/daily-dashboard/data/users.db` (somente leitura)
- `/home/simplifique/.hermes/state/daily-simplifique/notion-oportunidades.json`
- `/home/simplifique/.hermes/state/daily-simplifique/notion-demand-reconciliation.json`
- `/home/simplifique/.hermes/state/simplifique-market-radar/latest.json`
