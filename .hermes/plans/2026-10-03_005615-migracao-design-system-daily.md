# Migração do Design System do Daily — Plano de Implementação

> **Para o Hermes:** executar este plano fase a fase, com apenas um ciclo de edição ativo por vez e revisão de conformidade + qualidade antes de avançar.

**Objetivo:** migrar incrementalmente o Daily para o Design System da Simplifique já desenhado no Figma, preservando lógica, autenticação, integrações, contratos de API, fontes de dados e regras de negócio.

**Arquitetura:** manter o backend e os payloads existentes congelados durante a migração visual. Introduzir tokens e componentes reutilizáveis no frontend, refatorar uma área por fase, validar cada fase no runtime local e público e manter cada entrega reversível.

**Stack atual:** Python stdlib + `ThreadingHTTPServer`, SQLite, HTML estático, CSS global, JavaScript sem build, Docker Compose/Traefik em produção.

**Figma:** arquivo `aGBW9EAvXjYm9Tz3KkkHcf`; Dark Theme `410:15`; BI Essentials `414:29`; Projeto Faseado `415:15`; Content Operations `416:15`; Daily Core Modules `422:15`.

---

## 1. Auditoria concluída

### Estado técnico

- Branch `main`, baseline auditado no commit `5ad8c10`.
- Repositório limpo e sem remote configurado.
- **121 testes passando**.
- **16 arquivos JavaScript** e **6 arquivos Python** com sintaxe válida.
- Runtime local e público respondendo `200` com o mesmo fingerprint `72c4e876bf599dbc`.
- Backend concentrado em `app.py`; todas as telas estão em `templates/index.html`.
- Frontend distribuído entre `static/style.css` e 16 módulos JavaScript.
- O CSS atual tem aproximadamente 50,8 KB, 659 blocos, poucos tokens e sobreposição significativa por cascata.
- Os assets estáticos são roteados manualmente em `app.py`; qualquer novo arquivo precisa ser registrado explicitamente.

### Componentes repetidos a consolidar

- escape de HTML;
- formatação de datas;
- KPIs;
- badges semânticos;
- alertas e estados de saúde;
- cabeçalhos de seção;
- empty/loading/error/unavailable;
- cards e listas;
- links Notion/Monday/ClickUp;
- abas e navegação;
- drawers/modais;
- cards de projetos, diagnósticos e atenção.

### Riscos estruturais

1. Cascata global pode alterar várias telas ao mesmo tempo.
2. JavaScript depende diretamente de IDs e da ordem do markup.
3. Navegação e listeners estão distribuídos entre vários módulos.
4. `app.js` mistura shell, diagnósticos, atenção e modal legado.
5. O modal `#detail` é compartilhado por fluxos novos e legados.
6. Não há suíte E2E nem regressão visual automatizada.
7. Reiniciar o systemd local não publica o container público.
8. `0`, `—`, `indisponível` e `stale` têm significados operacionais diferentes.
9. Ações, proveniência, CSRF, allowlists e restrições de conclusão local não podem ser enfraquecidos.
10. O fingerprint atual não cobre `login.html`, PNG, SVG e ícones; esses assets exigem verificação explícita.

---

## 2. Decisões de Design System antes da implementação

### Tokens-base

- Fonte: Inter.
- Light base: adotar `#F6F3EF` como base canônica; `#F8F3EB` fica como variação somente se um componente do Figma exigir contraste específico.
- Light surface: `#FBF7F1`.
- Dark base/surfaces: `#141210`, `#1A1714`, `#201C19`, `#2A2521`, `#312B26`.
- Marca/ação: `#FF7A2F`.
- Semânticas independentes para sucesso, atenção, crítico, informação e IA; não reutilizar laranja como substituto de todas elas.
- Escala inicial: gaps `8/10/12/14/16/18px`; padding `10/12/14/18px`; raios `7/8/9/10px`; pills `999px`.
- Tipografia: página `28px`; seção `16px`; card `12–15px`; KPI `20–22px`; apoio `9–11px`.

### Guardas

- Nenhum número demonstrativo do Figma será tratado como dado real.
- Métrica sem evidência será `—`, nunca zero.
- Máximo de um insight visual por área na Home.
- Não criar CRM próprio.
- Não transformar Saúde do Sistema em painel DevOps.
- Radar, copy, design, revisão, programação e publicação permanecem estados distintos.
- Conteúdos agendados exigem evidência do Zernio; data planejada não comprova programação.
- Diagnósticos de prospects permanecem separados de clientes contratados.
- Apenas uma navegação principal no mobile.

---

## 3. Fases, duração e critérios

A migração terá as **8 fases já definidas**. A auditoria é um checkpoint preparatório concluído, não uma nona fase de implementação.

### FASE 1 — Tokens e componentes base

**Objetivo:** criar fundação visual reutilizável sem mudar a arquitetura funcional.

**Escopo:** tokens, tipografia, superfícies, botões, badges, KPIs, cards leves, alertas, ícones, loading/empty/error/unavailable, drawer e responsividade-base.

**Arquivos prováveis:**
- `static/style.css`
- `templates/index.html`
- possível novo `static/ui.js`
- `app.py`, somente se houver novo asset estático
- `test_app.py`

**Estimativa:** 2–3 h; 1 ciclo.

**Aceite:** componentes isolados funcionando nos dois temas; sem regressão nas telas existentes; tokens semânticos não colidem; navegação e ações permanecem intactas.

### FASE 2 — Visão Geral

**Objetivo:** transformar a Home em monitor executivo de Operação, Marketing e Comercial.

**Escopo:** faixa de estado geral, três áreas, poucos KPIs, máximo de um insight por área, fila consolidada de atenção e frescor das fontes.

**Arquivos prováveis:**
- `templates/index.html`
- `static/overview.js`
- `static/app.js`
- `static/intelligence.js`
- `static/style.css`
- `test_app.py`

**Estimativa:** 3–5 h; 1 ciclo, com checkpoint visual intermediário.

**Aceite:** perguntas gerenciais respondidas na primeira dobra; sem financeiro na Home; `—` para evidência ausente; 1920×1080, 1366×768 e mobile verificados.

### FASE 3 — Demandas

**Objetivo:** aplicar o padrão `422:15` preservando proveniência e fonte da verdade.

**Escopo:** projeto, título, responsável, prazo, status, prioridade, origem e quatro ações fixas: Notion, Monday, ClickUp e Encerrar no Daily.

**Arquivos prováveis:**
- `templates/index.html`
- `static/demands.js`
- `static/my-panel.js`
- `static/style.css`
- `test_app.py`

**Estimativa:** 2–4 h; 1 ciclo.

**Aceite:** ícones ativos/inativos corretos; URLs verificadas; conclusão local habilitada somente para itens comprovadamente locais; histórico preservado.

### FASE 4 — Projetos e Atenção

**Objetivo:** transformar Projetos em acervo operacional e consolidar exceções em uma fila única.

**Escopo:** lista leve, progresso/estado comprovado, drawer com objetivo, fases, demandas, decisões, dependências, bloqueios, responsáveis, histórico e próxima ação; atenção transversal por severidade.

**Arquivos prováveis:**
- `templates/index.html`
- `static/projects.js`
- `static/app.js`
- `static/attention-tabs.js`
- `static/style.css`
- `test_app.py`

**Estimativa:** 3–5 h; 1 ciclo, com validação separada do drawer.

**Aceite:** padrão `415:15` adaptado; nenhum modal legado quebrado; prospects não entram na carteira; severidade e progresso derivados de evidência.

### FASE 5 — Marketing

**Objetivo:** consolidar Content Operations no padrão `416:15`.

**Escopo:** Radar → Selecionado → Copy → Produção → Revisão → Programado → Publicado; inbox de aprovação; calendário mensal compacto; drawer com conteúdo completo; gargalos e BI operacional permitido.

**Arquivos prováveis:**
- `templates/index.html`
- `static/social.js`
- `static/style.css`
- `test_app.py`
- `test_sync_zernio_calendar.py`

**Estimativa:** 4–6 h; 1–2 ciclos por concentrar mais estados e gates.

**Aceite:** gates humanos preservados; célula do calendário sem copy integral; lane sem data; dois slots diários claros; Zernio é a evidência de programado/publicado; CTA bloqueado continua bloqueado.

### FASE 6 — Comercial e Diagnósticos

**Objetivo:** criar leitura gerencial consolidada sem construir CRM paralelo.

**Escopo:** leads para abordar, sem contato, follow-ups, propostas, oportunidades paradas, conversão quando comprovada, próximos movimentos, mudanças recentes e diagnósticos separados.

**Arquivos prováveis:**
- `templates/index.html`
- `static/commercial.js`
- `static/app.js`
- `static/style.css`
- `test_app.py`
- `test_commercial_sync.py`

**Estimativa:** 3–4 h; 1 ciclo.

**Aceite:** dados continuam vindos do Notion/CRM; sem edição local; funil só com estágios e denominadores válidos; prospects separados de contratados.

### FASE 7 — Saúde do Sistema

**Objetivo:** responder se o sistema que sustenta a operação está funcionando.

**Escopo:** integrações, automações, sincronizações, serviços essenciais, frescor, último sucesso, contagem, reconciliação e conclusão Saudável/Atenção/Crítico.

**Arquivos prováveis:**
- `templates/index.html`
- `static/integration-health.js`
- `static/style.css`
- `test_app.py`

**Estimativa:** 2–4 h; 1 ciclo.

**Aceite:** conclusão primeiro e detalhe sob demanda; falha crítica sobe para Atenção; sem logs brutos ou controles de infraestrutura; oneshot e timer tratados corretamente.

### FASE 8 — Atividade e telas secundárias

**Objetivo:** fechar a coerência visual do produto.

**Escopo:** atividade, métricas, navegação, conta, login e estados auxiliares; remover duplicações visuais remanescentes sem remover funcionalidades.

**Arquivos prováveis:**
- `templates/index.html`
- `templates/login.html`
- `static/activity.js`
- `static/metrics.js`
- `static/navigation.js`
- `static/account.js`
- `static/login.js`
- `static/style.css`
- `test_app.py`

**Estimativa:** 3–5 h; 1 ciclo, com login verificado separadamente.

**Aceite:** navegação final Visão Geral, Operação, Marketing, Comercial e Sistema; telas secundárias coerentes; login verificado separadamente; ausência de navegação mobile duplicada.

---

## 4. Estimativa total

- **Implementação:** 8 fases.
- **Ciclos de trabalho:** 8–9, porque Marketing pode exigir dois ciclos.
- **Esforço ativo estimado:** **22–36 horas de agente**.
- **Calendário concentrado:** 3–5 dias úteis, se as fases forem aprovadas sem espera.
- **Calendário recomendado, com revisão humana e deploy faseado:** **5–8 dias úteis**.

A faixa já inclui TDD, suíte completa, sintaxe, responsividade, deploy, read-back público e correções da fase. Não inclui mudança de regra de negócio, criação de novos produtos, contratos de API novos ou reconstrução do backend.

### Cadência recomendada

- Fases 1, 3 e 7: um ciclo curto cada.
- Fases 2, 4, 6 e 8: um ciclo cada, com verificação visual antes do deploy.
- Fase 5: um ou dois ciclos, por concentrar o estado editorial mais sensível.
- Revisão humana ao fim de cada fase antes da próxima publicação.
- Nunca manter duas fases editando `style.css` e `index.html` em paralelo.

---

## 5. Protocolo de cada fase

1. Criar branch ou checkpoint reversível.
2. Registrar baseline visual e funcional da tela.
3. Escrever testes de contrato/markup antes da refatoração.
4. Implementar somente a fase ativa.
5. Rodar testes focados.
6. Rodar `python3 -m unittest -q`.
7. Rodar sintaxe de todos os JS e Python alterados.
8. Rodar `git diff --check`.
9. Verificar loading, empty, error, partial evidence e unavailable.
10. Validar em 1920×1080, 1366×768 e mobile.
11. Validar ações, links, autenticação e CSRF afetados.
12. Fazer commit único e reversível da fase.
13. Publicar pelo fluxo real do Docker/Traefik.
14. Confirmar `/health`, fingerprint e marcadores dos assets alterados.
15. Fazer read-back visual e funcional do domínio público.
16. Registrar alterações e só então liberar a próxima fase.

---

## 6. Ordem de implantação e rollback

A ordem oficial é **1 → 2 → 3 → 4 → 5 → 6 → 7 → 8**.

Cada fase terá seu próprio commit e deploy. Se uma fase falhar:

- reverter somente o commit da fase;
- republicar o último artefato verificado;
- confirmar fingerprint e funcionalidade;
- corrigir em novo ciclo, sem avançar.

Fases grandes podem ser divididas internamente em subciclos, mas continuam sendo aprovadas como uma única fase funcional. Isso reduz o tamanho da janela de trabalho sem criar um novo faseamento para o usuário.

---

## 7. Fora do escopo

- reconstrução do produto;
- alteração do schema SQLite;
- troca de backend ou framework;
- criação de CRM próprio;
- mudanças em regras de autenticação ou autorização;
- remoção de funcionalidades sem equivalente visual;
- métricas financeiras ou de mídia paga ainda inexistentes;
- observabilidade DevOps detalhada;
- dark mode completo antes de os módulos light estarem consistentes, salvo decisão explícita.

---

## 8. Primeiro ciclo recomendado

Começar somente pela **FASE 1**. Ao final, entregar:

- mapa final de tokens;
- componentes base reutilizáveis;
- demonstração controlada em uma área não crítica ou sandbox interno;
- suíte completa e verificação responsiva;
- comparação visual com `410:15` e `422:15`;
- nenhum endpoint, payload, regra ou ação alterados.

A FASE 2 só começa após a aprovação visual e funcional da fundação.
