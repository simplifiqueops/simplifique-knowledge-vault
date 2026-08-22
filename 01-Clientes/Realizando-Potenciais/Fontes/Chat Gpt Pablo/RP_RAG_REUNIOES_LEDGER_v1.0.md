---
title: "RP — Corpus de Reuniões / Ledger de Evidências"
version: "1.0"
status: "fonte_historica"
project: "Realizando Potenciais"
compiled_at: "2026-08-19"
purpose: "proveniência para a RAG Operacional Canônica"
---

# RP — CORPUS DE REUNIÕES / LEDGER DE EVIDÊNCIAS

## 0. Função desta base

Este arquivo **não é a verdade operacional atual do RP**.

Ele é um índice de evidências extraídas de reuniões e serve para responder:

- onde uma decisão apareceu;
- quando um processo foi alterado;
- qual contexto levou a uma correção;
- quais números foram apresentados;
- o que era hipótese;
- o que foi confirmado durante a própria reunião.

A RAG Operacional Canônica deve ser consultada primeiro.

A reunião deve ser consultada quando for necessário:

- auditar origem de uma regra;
- reconstruir contexto;
- verificar responsabilidade;
- entender mudança;
- recuperar histórico.

---

# 1. Política de ingestão de reuniões

## Não canonizar automaticamente

Uma reunião contém simultaneamente:

- fatos;
- opiniões;
- ideias;
- hipóteses;
- decisões;
- tarefas;
- números;
- brincadeiras;
- contradições;
- propostas rejeitadas.

Por isso:

`TRANSCRIÇÃO ≠ VERDADE OPERACIONAL`

Fluxo correto:

`TRANSCRIÇÃO → EXTRAÇÃO → CLASSIFICAÇÃO → EVIDÊNCIA DE EXECUÇÃO → RAG CANÔNICA`

---

# 2. Estados para trechos de reunião

- `FATO_REPORTADO`
- `DADO_REPORTADO`
- `DECISAO`
- `IMPLEMENTACAO_AO_VIVO`
- `HIPOTESE`
- `IDEIA`
- `TAREFA`
- `REJEITADO`
- `PROBLEMA`
- `APRENDIZADO`

Apenas `IMPLEMENTACAO_AO_VIVO`, `FATO_REPORTADO` com evidência e `DADO_REPORTADO` validado devem alimentar diretamente a RAG canônica.

---

# 3. Reunião — 19/05/2026

```yaml
id: RP-MTG-2026-05-19
title: Reunião Time RP
url: https://fathom.video/calls/677016074
```

## Evidências relevantes

### Cúpula

`DADO_REPORTADO`

- 414 contatos na análise;
- 58 reuniões;
- ~14% de passagem para agendamento;
- ~41% de conversão de reunião realizada para venda.

`APRENDIZADO`

A conversão depois da sessão estava saudável; o gargalo era gerar/agendar mais reuniões qualificadas.

### Gestão

`PROBLEMA`

Demandas discutidas fora do ClickUp podiam ficar perdidas.

`DECISAO/PROCESSO`

Foi iniciada uma rotina para quebrar demandas oriundas de reunião e levá-las para o ClickUp.

### Prioridade

`DECISAO`

Cúpula era prioridade; CSV perpétuo era oportunidade secundária naquele ciclo.

---

# 4. Reunião — 01/06/2026

```yaml
id: RP-MTG-2026-06-01
title: Reunião Comercial - Perpétuo CSV
url: https://fathom.video/calls/692317793
```

## Evidências relevantes

### Gargalo de atendimento

`FATO_REPORTADO`

Havia 18 aplicações recebidas e agenda com espaços ainda disponíveis.

`DECISAO`

Agendamento deveria vir antes de tarefas administrativas e follow-ups secundários.

### FullFunnel

`PROBLEMA`

Lead podia estar em conversa sem aparecer cedo na pipeline.

`IMPLEMENTACAO_AO_VIVO`

O gatilho de criação de oportunidade foi movido para uma etapa anterior da automação.

### Timeout

`FATO_REPORTADO`

Fluxo usava timeout entre perguntas.

`APRENDIZADO`

Era necessário diferenciar quem:

- travou;
- não respondeu;
- foi desqualificado;
- concluiu.

### Escada comercial

`FATO_REPORTADO`

Foi apresentado fluxo operacional:

Cúpula → CSV → Desafio 38 Dias.

Energia Infinita ainda apareceu como item futuro naquele momento.

---

# 5. Reunião — 17/07/2026

```yaml
id: RP-MTG-2026-07-17
title: Reunião RP
url: https://fathom.video/calls/751777480
```

## Evidências relevantes

### WCSV

`DADO_REPORTADO`

- 320 leads válidos;
- FullFunnel mostrava ~374 por causa de testes;
- ~32 pessoas observadas no ambiente ao vivo;
- 3 sinais de interesse;
- 1 boleto relatado.

`PROBLEMA`

A captação no FullFunnel não permitiu identificar corretamente os presentes no player/webinar.

`APRENDIZADO`

Não usar pico de audiência como presença única identificada.

### CRM

`FATO_REPORTADO`

Leads estavam tagueados e com origem/UTMs preservadas.

### Operação semanal

`DECISAO`

O WCSV foi organizado como recorrência semanal.

A discussão de datas mudou ao longo da reunião, portanto **não canonizar dias específicos**.

### Black Friday histórica

`DADO_REPORTADO`

- meta: 2.500 leads;
- realizado: 1.016;
- 66 vendas;
- 46 novos;
- 20 renovações;
- ~6,49% total;
- ~4,52% novos clientes.

### Cúpula — relatório

`DADO_REPORTADO`

Planilha mostrada com 574 leads acumulados naquele momento e divisão por:

- origem;
- qualificação;
- sessões;
- vendas;
- não retorno;
- desqualificação.

---

# 6. Reunião — 14/08/2026

```yaml
id: RP-MTG-2026-08-14
title: Impromptu Zoom Meeting
url: https://fathom.video/calls/784713845
```

## Evidências relevantes

### WhatsApp

`PROBLEMA`

Conta/API havia sofrido restrição durante operação de alto volume.

`IMPLEMENTACAO_AO_VIVO`

A conexão foi refeita e testada.

`FATO_REPORTADO`

Automações voltaram a funcionar.

`DADO_REPORTADO`

- ~15 mil mensagens enviadas;
- ~3 mil recebidas;
- 5.946 conversas iniciadas em 7 dias.

`DECISAO OPERACIONAL`

Adotar envio mais conservador, com referência de ~20 mensagens/hora para a ação controlada e evitando noite.

`IMPORTANTE`

Esse número não é limite oficial da Meta.

---

# 7. Como adicionar uma nova reunião

Usar o formato:

```yaml
id:
title:
date:
url:
participants:
topics:
```

Depois separar cada trecho relevante em:

### [tipo]

- evidência;
- contexto;
- impacto;
- se houve implementação;
- qual chunk canônico foi atualizado.

---

# 8. Relação com a RAG Canônica

Sempre que uma reunião gerar alteração confirmada:

1. manter o registro aqui;
2. criar/atualizar chunk na RAG Operacional;
3. colocar `fonte` com ID da reunião;
4. se substituir processo anterior, marcar o anterior como `SUPERADO`;
5. nunca apagar histórico.

---

# 9. Regra final

A reunião guarda **memória e contexto**.

A RAG Operacional guarda **verdade utilizável**.

A IA do time deve consultar a verdade utilizável primeiro e recorrer às reuniões para explicar, auditar ou reconstruir o caminho.
