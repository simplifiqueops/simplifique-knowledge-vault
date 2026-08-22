---
title: "RP — RAG Operacional Canônica"
version: "1.0"
status: "uso_interno"
project: "Realizando Potenciais"
compiled_at: "2026-08-19"
scope:
  - operação
  - gestão
  - comercial
  - funis
  - tecnologia
  - automações
  - campanhas
  - métricas
  - aprendizados
excludes:
  - teoria_metodologica_rp
  - rag_base_mestre_enviada
  - hipóteses_não_implementadas
  - tarefas_apenas_planejadas
---

# RP — RAG OPERACIONAL CANÔNICA

## 0. Finalidade

Esta base existe para fornecer a uma IA o **estado operacional e o histórico implementado da Realizando Potenciais (RP)**.

Ela deve responder perguntas como:

- Como os funis do RP realmente funcionaram?
- Quais ferramentas foram usadas?
- Quais automações foram implantadas?
- Quais gargalos já aconteceram?
- Quais resultados foram observados?
- Quais correções já foram aplicadas?
- Quais ativos operacionais existem?
- Quais aprendizados devem impedir que o time repita erros?

Esta base **não é a base metodológica da RP**. Conceitos como CSV, RUALI, Assinatura Emocional, Três Níveis e teoria da Cúpula devem existir em outra base especializada.

---

# 1. Regras de verdade desta RAG

## 1.1. O que pode entrar

Um item pode ser considerado conhecimento operacional canônico quando houver pelo menos uma evidência de:

- campanha publicada;
- página utilizada;
- automação funcionando;
- disparo executado;
- integração efetivamente usada;
- produto vendido;
- lead captado;
- reunião/evento realizado;
- número medido;
- correção implantada;
- processo efetivamente utilizado pelo time;
- decisão posteriormente observada em execução.

## 1.2. O que não pode virar verdade canônica

Não transformar em processo implantado:

- "vamos fazer";
- "precisamos fazer";
- brainstorm;
- ideia levantada em reunião;
- tarefa criada;
- tarefa atrasada;
- tarefa em progresso sem evidência de conclusão;
- proposta não validada;
- meta futura;
- promessa de entrega;
- hipótese de campanha;
- estratégia rejeitada;
- informação que só apareceu em copy e não na operação.

## 1.3. Estados recomendados

- `CONFIRMADO_ATUAL` — comprovado e ainda tratado como operação vigente.
- `CONFIRMADO_HISTORICO` — aconteceu, mas pode ter sido substituído.
- `APRENDIZADO_OPERACIONAL` — falha ou descoberta observada que deve orientar próximas decisões.
- `METRICA_HISTORICA` — número válido para um período/campanha.
- `ATIVO_HISTORICO` — ativo utilizado, mas cuja versão atual precisa ser confirmada.
- `SUPERADO` — processo que existiu e foi explicitamente substituído.
- `NAO_CANONIZAR` — registro útil para auditoria, mas não deve orientar execução atual.

## 1.4. Regra para a IA

Nunca responder "o RP faz X atualmente" com base apenas em um registro histórico.

Quando a informação for histórica, dizer explicitamente:

> "No ciclo/período X, o RP operou dessa forma."

---

# 2. Arquitetura de conhecimento recomendada

A inteligência do RP deve ser dividida em camadas.

## 2.1. RAG Operacional Canônica — esta base

Contém:

- processos executados;
- ferramentas;
- arquitetura de funil;
- responsáveis quando confirmados;
- métricas;
- ativos;
- falhas;
- correções;
- aprendizados.

É a principal base para responder ao time sobre **como a operação funciona ou funcionou**.

## 2.2. RAG Metodológica RP

Deve conter separadamente:

- CSV;
- RUALI;
- Assinatura Emocional;
- Cúpula da Decisão como metodologia;
- Três Níveis;
- ferramentas;
- transcrições didáticas;
- teoria;
- princípios;
- propriedade intelectual.

## 2.3. RAG Comercial e Marketing

Pode ser separada quando o volume crescer.

Deve conter:

- ICPs;
- públicos;
- campanhas;
- anúncios;
- copies aprovadas;
- objeções;
- páginas;
- ofertas;
- pesquisas;
- benchmarks por campanha.

## 2.4. RAG / Corpus de Reuniões

As reuniões devem existir **fora da base canônica**, como fonte histórica.

A função do corpus de reuniões é responder:

- quem decidiu;
- quando foi decidido;
- qual era o contexto;
- o que foi discutido;
- quais alternativas foram rejeitadas;
- qual era a intenção original.

A RAG Operacional usa a reunião como **evidência**, mas não copia automaticamente toda decisão para a verdade operacional.

Fluxo recomendado:

`REUNIÃO / WHATSAPP / CLICKUP / DADOS → EXTRAÇÃO → VALIDAÇÃO DE EXECUÇÃO → RAG OPERACIONAL CANÔNICA`

---

# 3. Entidade operacional

## RP-ORG-001 — Identificação

```yaml
id: RP-ORG-001
area: organização
tipo: identidade_operacional
status: CONFIRMADO_ATUAL
entidade: Realizando Potenciais
alias:
  - RP
```

A sigla `RP` é utilizada operacionalmente para Realizando Potenciais.

---

# 4. Gestão e governança

## RP-GOV-001 — ClickUp como ferramenta operacional

```yaml
id: RP-GOV-001
area: gestão
subarea: demandas
status: CONFIRMADO_HISTORICO
ferramenta: ClickUp
workspace: "Realizando Potenciais - OP"
```

O ClickUp foi utilizado como ferramenta formal de acompanhamento de demandas da operação RP.

Há histórico de estruturas específicas para ciclos do CSV/Webinário e acompanhamento de execução.

### Uso pela IA

Quando uma demanda estiver apenas no ClickUp, isso **não comprova entrega**. Status deve ser verificado antes de tratar como implementado.

---

## RP-GOV-002 — WhatsApp como canal de entrada operacional

```yaml
id: RP-GOV-002
area: gestão
subarea: comunicação
status: CONFIRMADO_HISTORICO
```

Parte das demandas e decisões do RP entra por grupos e conversas de WhatsApp, além de reuniões e ClickUp.

Isso gerou risco de informação operacional ficar distribuída entre canais.

### Aprendizado

A existência de uma solicitação em WhatsApp não equivale a uma demanda controlada.

---

## RP-GOV-003 — Risco recorrente de demanda fora do sistema

```yaml
id: RP-GOV-003
area: gestão
tipo: APRENDIZADO_OPERACIONAL
status: CONFIRMADO_HISTORICO
```

Foi explicitamente reconhecido em reunião que demandas discutidas em reunião ou grupos podiam não chegar ao ClickUp e ficar perdidas.

Foi iniciado um processo de quebra das demandas de reunião para inserção no ClickUp.

### Fonte

Reunião Time RP — 19/05/2026.

### Uso pela IA

Ao analisar execução:

1. verificar decisão;
2. verificar demanda registrada;
3. verificar evidência de entrega;
4. não assumir conclusão apenas porque houve reunião ou atribuição.

---

## RP-GOV-004 — Prioridade operacional por centro de gravidade

```yaml
id: RP-GOV-004
area: gestão
tipo: principio_operacional_observado
status: CONFIRMADO_HISTORICO
```

O time passou a utilizar explicitamente a ideia de **prioridade principal vs. oportunidade secundária** em períodos com múltiplos funis ativos.

Exemplo observado em maio/2026:

- Cúpula = prioridade;
- CSV perpétuo = oportunidade secundária.

### Aprendizado

A operação sofre quando um novo funil que começa a performar consome a atenção do time antes de a prioridade principal ser concluída.

---

# 5. Cúpula da Decisão — operação comercial

## RP-CD-001 — Sessão estratégica como mecanismo de venda

```yaml
id: RP-CD-001
produto: Cúpula da Decisão
area: comercial
tipo: processo_comercial
status: CONFIRMADO_HISTORICO
periodo_referencia: "2026-05"
```

A Cúpula operou com captação/qualificação seguida de **sessão estratégica** com a Vanessa como etapa central de conversão.

Em 19/05/2026, o time registrou:

- 414 contatos considerados na análise;
- 58 reuniões/sessões;
- aproximadamente 14% de passagem da lista para agendamento;
- aproximadamente 41% de conversão de reunião realizada para venda.

### Interpretação operacional

O gargalo observado naquele momento não estava principalmente no fechamento da sessão, mas no **volume e agendamento de leads qualificados**.

### Fonte

Reunião Time RP — 19/05/2026.

---

## RP-CD-002 — Agendamento priorizado sobre follow-up de fechamento

```yaml
id: RP-CD-002
produto: Cúpula da Decisão
area: comercial
tipo: regra_operacional
status: CONFIRMADO_HISTORICO
periodo_referencia: "2026-06"
```

Em 01/06/2026, havia 18 aplicações recebidas sem atendimento suficiente e espaços vagos na agenda da Vanessa.

Foi reforçada a prioridade:

1. atender leads novos;
2. agendar sessão;
3. depois acompanhar fechamento/onboarding.

### Aprendizado

Quando a conversão da sessão é alta, deixar horários da agenda vazios é uma perda operacional maior do que atrasar relatórios administrativos.

### Fonte

Reunião Comercial — 01/06/2026.

---

## RP-CD-003 — Qualificação automatizada antes da sessão

```yaml
id: RP-CD-003
produto: Cúpula da Decisão
area: automação
ferramenta: FullFunnel
status: CONFIRMADO_HISTORICO
```

O fluxo de Cúpula utilizou perguntas automatizadas para avaliar fit profissional e necessidade antes de o lead seguir no pipeline comercial.

Foram usados elementos de qualificação como:

- atuação profissional;
- atendimento de pessoas;
- necessidade;
- capacidade/condição financeira em versões do fluxo.

---

## RP-CD-004 — Oportunidade era criada tarde demais

```yaml
id: RP-CD-004
produto: Cúpula da Decisão
area: automação
tipo: problema_corrigido
status: SUPERADO
data_referencia: "2026-06-01"
```

Problema observado:

Leads podiam entrar na conversa de WhatsApp e não aparecer na pipeline cedo o suficiente porque a criação da oportunidade acontecia apenas após etapas posteriores da automação.

Consequência:

- leads ficavam visíveis em conversas;
- comercial tinha dificuldade de distinguir quem precisava de ação;
- risco de lead ficar sem acompanhamento.

---

## RP-CD-005 — Criação de oportunidade antecipada

```yaml
id: RP-CD-005
produto: Cúpula da Decisão
area: automação
tipo: correcao_implantada
status: CONFIRMADO_HISTORICO
data_referencia: "2026-06-01"
```

A automação foi alterada durante a reunião para criar a oportunidade mais cedo.

Após a alteração, quando o lead demonstrava fit profissional na sequência inicial, ele já passava a aparecer na pipeline.

### Fonte

Reunião Comercial — 01/06/2026.

### Uso pela IA

Princípio reutilizável:

> Um lead que já demonstrou intenção/fit não deve ficar invisível ao comercial aguardando a conclusão de uma automação longa.

---

## RP-CD-006 — Timeout de automação

```yaml
id: RP-CD-006
produto: Cúpula da Decisão
area: automação
tipo: configuracao_operacional
status: CONFIRMADO_HISTORICO
periodo_referencia: "2026-06"
```

O fluxo do FullFunnel utilizou `timeout` entre perguntas.

Foi identificado que timeout curto poderia fazer o lead sair do fluxo sem completar a sequência.

Durante a revisão, o time discutiu/ampliou timeout e follow-up dentro da janela de conversa.

### Aprendizado

Automação de qualificação precisa diferenciar:

- erro técnico;
- lead que parou;
- lead que foi desqualificado;
- lead que concluiu.

---

## RP-CD-007 — Tag de desqualificação

```yaml
id: RP-CD-007
produto: Cúpula da Decisão
area: crm
status: CONFIRMADO_HISTORICO
tag_exemplo: "desqualificado SCD"
```

Leads sem fit podiam receber tag específica de desqualificação e sair do caminho de abordagem prioritária.

---

## RP-CD-008 — Escada de aproveitamento comercial

```yaml
id: RP-CD-008
area: comercial
tipo: arquitetura_de_oferta
status: CONFIRMADO_HISTORICO
periodo_referencia: "2026-06"
```

Foi efetivamente usado/orientado o aproveitamento de leads que não fechavam a oferta principal.

Fluxo operacional registrado:

`CÚPULA → CSV → oferta de menor ticket`

Naquele período, o produto de menor ticket utilizado era o **Desafio 38 Dias**.

Energia Infinita aparecia como substituição futura e, portanto, não deve ser tratada como já implantada naquele registro.

### Fonte

Reunião Comercial — 01/06/2026.

---

## RP-CD-009 — Relatório comercial por origem

```yaml
id: RP-CD-009
produto: Cúpula da Decisão
area: dados
status: CONFIRMADO_HISTORICO
periodo_referencia: "2026-07"
```

A operação passou a consolidar planilha com dados por origem, incluindo:

- leads;
- qualificados;
- sessões agendadas;
- sessões realizadas;
- cancelamentos;
- vendas;
- leads sem retorno;
- desqualificados;
- perfil para outros produtos;
- posteriormente objeções.

Em 17/07/2026, foi mostrado um acumulado de **574 leads para Cúpula** na planilha em construção.

### Fonte

Reunião RP — 17/07/2026.

---

# 6. CSV / WCSV — webinar recorrente

## RP-WCSV-001 — Webinar entrou em operação real

```yaml
id: RP-WCSV-001
produto: O Comando da Sua Vida
funil: WCSV
area: funil
status: CONFIRMADO_HISTORICO
data_referencia: "2026-07-17"
```

O RP executou um primeiro ciclo de webinar recorrente ligado ao CSV.

Números operacionais observados:

- 320 leads de tráfego considerados válidos;
- aproximadamente 32 acessos simultâneos/observados no ambiente;
- 3 sinais de interesse comercial relatados;
- 1 geração de boleto relatada.

### Limite

Os 32 acessos não podem ser tratados como presença exata porque havia membros do time e acessos posteriores.

### Fonte

Reunião RP — 17/07/2026.

---

## RP-WCSV-002 — Falha de rastreamento de presença

```yaml
id: RP-WCSV-002
produto: O Comando da Sua Vida
funil: WCSV
area: dados
tipo: APRENDIZADO_OPERACIONAL
status: CONFIRMADO_HISTORICO
data_referencia: "2026-07-17"
```

A captação estava no FullFunnel, enquanto a aula rodava em estrutura de webinar que não devolvia corretamente ao FullFunnel a identidade dos participantes ao vivo.

Consequência:

- o RP tinha os leads captados;
- tinha UTMs e origem;
- mas não conseguia identificar com segurança quais leads específicos estavam ao vivo.

Isso impediu priorização comercial precisa.

---

## RP-WCSV-003 — Testes inflaram contagem no FullFunnel

```yaml
id: RP-WCSV-003
produto: O Comando da Sua Vida
area: dados
tipo: APRENDIZADO_OPERACIONAL
status: CONFIRMADO_HISTORICO
```

No primeiro ciclo, o FullFunnel mostrava cerca de 374 registros enquanto o tráfego apontava 320 leads válidos.

A diferença foi atribuída a aproximadamente 50+ testes internos feitos durante a preparação.

### Uso pela IA

Nunca usar número bruto de formulário como lead real sem excluir:

- testes;
- duplicações;
- QA interno.

---

## RP-WCSV-004 — Leads tagueados por origem e ciclo

```yaml
id: RP-WCSV-004
produto: O Comando da Sua Vida
area: crm
ferramenta: FullFunnel
status: CONFIRMADO_HISTORICO
```

Os leads do WCSV foram mantidos no FullFunnel com tags e informações de:

- origem;
- UTM;
- campanha;
- dados padrão de contato.

A intenção operacional implementada era preservar esses leads para ações posteriores, em especial aquecimento até Black Friday.

---

## RP-WCSV-005 — Redundância de armazenamento de leads

```yaml
id: RP-WCSV-005
produto: O Comando da Sua Vida
area: dados
status: CONFIRMADO_HISTORICO
```

No ciclo analisado, os leads estavam disponíveis em mais de um ponto:

- FullFunnel;
- Hotmart;
- planilha/central do WCSV.

### Aprendizado

A redundância reduziu o risco de perda total de base, mas aumenta a necessidade de definir uma fonte principal para reporting.

---

## RP-WCSV-006 — Página de replay existiu no primeiro teste

```yaml
id: RP-WCSV-006
produto: O Comando da Sua Vida
area: web
status: CONFIRMADO_HISTORICO
```

No primeiro teste, havia uma página de replay preparada na infraestrutura de webinar, com possibilidade de liberar acesso e direcionar para compra.

### Limite

O time posteriormente discutiu reduzir dependência de replay no modelo recorrente. Não tratar replay como regra atual do WCSV.

---

## RP-WCSV-007 — Cadência semanal

```yaml
id: RP-WCSV-007
produto: O Comando da Sua Vida
area: operação
status: CONFIRMADO_HISTORICO
periodo_referencia: "2026-07"
```

Após o primeiro teste, o time estruturou o WCSV como operação semanal:

- captação;
- aula;
- carrinho/abordagem;
- próxima captação;
- revisão de resultado.

A reunião de 17/07 consolidou o princípio de recorrência semanal.

### Limite

Datas específicas mudaram durante a discussão e não devem ser canonizadas como calendário permanente.

---

## RP-WCSV-008 — Uso do webinar como construção de base

```yaml
id: RP-WCSV-008
produto: O Comando da Sua Vida
area: estratégia_operacional
status: CONFIRMADO_HISTORICO
```

O webinar não foi tratado somente como venda direta.

Também passou a funcionar como mecanismo de:

- aquisição de leads;
- tagueamento;
- nutrição;
- construção de base para Black Friday;
- criação de público para outras ofertas.

---

# 7. Black Friday — benchmark histórico

## RP-BF-001 — Resultado Black Friday registrado

```yaml
id: RP-BF-001
area: performance
campanha: Black Friday RP
tipo: METRICA_HISTORICA
status: CONFIRMADO_HISTORICO
dados:
  meta_leads: 2500
  leads_captados: 1016
  atingimento_meta_captacao: "aprox. 40%"
  vendas_totais: 66
  novos_clientes: 46
  renovacoes: 20
  conversao_total: "aprox. 6.49%"
  conversao_novos_clientes: "aprox. 4.52%"
```

Os números foram recuperados e apresentados em reunião de 17/07/2026 como histórico da Black Friday anterior.

### Uso pela IA

Usar como benchmark histórico, não como taxa esperada para qualquer lançamento.

### Fonte

Reunião RP — 17/07/2026.

---

## RP-BF-002 — Captação abaixo da meta

```yaml
id: RP-BF-002
area: performance
campanha: Black Friday RP
tipo: APRENDIZADO_OPERACIONAL
status: CONFIRMADO_HISTORICO
```

O maior desvio explícito foi captação:

- meta: 2.500 leads;
- realizado: 1.016.

A operação atingiu aproximadamente 40% da meta de captação.

### Aprendizado

Projetar venda sem garantir volume de entrada suficiente gera pressão excessiva nas etapas finais do funil.

---

# 8. Imersão dos 3 Níveis — agosto/2026

## RP-IMERSAO-001 — Produto colocado à venda

```yaml
id: RP-IMERSAO-001
produto: Imersão dos 3 Níveis
area: produto
status: CONFIRMADO_HISTORICO
evento: "2026-08-15"
```

A Imersão dos 3 Níveis saiu do planejamento e entrou em operação comercial real em agosto/2026.

Foram utilizados ingressos de baixo ticket com versões na faixa de:

- R$47;
- R$97.

Os valores devem ser tratados como oferta histórica da campanha.

---

## RP-IMERSAO-002 — Vendas registradas antes do evento

```yaml
id: RP-IMERSAO-002
produto: Imersão dos 3 Níveis
area: performance
tipo: METRICA_HISTORICA
status: CONFIRMADO_HISTORICO
data_referencia: "2026-08-13"
```

Antes do evento, o projeto registrou 28 vendas, sendo 24 pagantes em um dos levantamentos operacionais consolidados.

Distribuição relatada:

- 17 atribuídas ao tráfego pago;
- 7 orgânicas;
- 3 vendas associadas a anúncios em vídeo.

### Limite

Tratar como fotografia do momento, não resultado final da campanha.

---

# 9. WhatsApp, API e automações

## RP-WA-001 — Dependência operacional do WhatsApp

```yaml
id: RP-WA-001
area: tecnologia
subarea: whatsapp
status: CONFIRMADO_HISTORICO
```

WhatsApp foi utilizado em larga escala para:

- captação;
- qualificação;
- mensagens utility;
- recuperação de carrinho;
- acompanhamento comercial;
- comunicação de eventos.

Essa dependência transformou indisponibilidade do canal em risco operacional crítico.

---

## RP-WA-002 — Bloqueio após alto volume

```yaml
id: RP-WA-002
area: tecnologia
subarea: whatsapp
tipo: incidente
status: CONFIRMADO_HISTORICO
data_referencia: "2026-08-13/14"
```

O número principal sofreu restrição/bloqueio durante uma operação de alto volume.

Durante o incidente:

- automações foram interrompidas;
- recuperação de carrinho precisou de ação manual;
- o time precisou restaurar a conexão.

---

## RP-WA-003 — API restaurada

```yaml
id: RP-WA-003
area: tecnologia
subarea: whatsapp
tipo: correcao_implantada
status: CONFIRMADO_HISTORICO
data_referencia: "2026-08-14"
```

A conexão da API foi restaurada por meio da reconexão/vinculação da conta no ecossistema Meta/Facebook.

Após testes, o time confirmou que as automações voltaram a funcionar.

### Fonte

Impromptu Zoom Meeting — 14/08/2026.

---

## RP-WA-004 — Volume observado

```yaml
id: RP-WA-004
area: tecnologia
subarea: whatsapp
tipo: METRICA_HISTORICA
status: CONFIRMADO_HISTORICO
data_referencia: "2026-08-14"
dados:
  mensagens_enviadas_aprox: 15000
  mensagens_recebidas_aprox: 3000
  conversas_iniciadas_7_dias: 5946
```

Os números foram citados durante a restauração da API.

### Limite

Não interpretar os números como limite oficial da Meta.

---

## RP-WA-005 — Cadência reduzida após incidente

```yaml
id: RP-WA-005
area: tecnologia
subarea: whatsapp
tipo: APRENDIZADO_OPERACIONAL
status: CONFIRMADO_HISTORICO
data_referencia: "2026-08-14"
```

Após o incidente, foi adotada postura mais conservadora:

- aproximadamente 20 mensagens por hora para ações manuais/controladas;
- evitar envio noturno;
- acompanhar qualidade da conta.

### Regra

`20 mensagens/hora` é uma medida operacional adotada pelo time naquele contexto, **não um limite universal da API**.

---

# 10. FullFunnel

## RP-FF-001 — CRM e automação

```yaml
id: RP-FF-001
area: tecnologia
ferramenta: FullFunnel
status: CONFIRMADO_HISTORICO
```

FullFunnel foi utilizado pelo RP para:

- formulários;
- automações;
- pipeline;
- WhatsApp/API;
- tags;
- histórico de inscrição;
- registro de execução;
- páginas/quiz em determinados ciclos;
- exportação de contatos;
- acompanhamento de origem.

---

## RP-FF-002 — Investigação de automações pelo histórico

```yaml
id: RP-FF-002
area: tecnologia
ferramenta: FullFunnel
tipo: procedimento_operacional
status: CONFIRMADO_HISTORICO
```

O time utilizou:

- Histórico de Inscrição;
- Registro de Execução;

para identificar onde um lead parou dentro de uma automação.

### Aprendizado

Ao investigar "lead travado", distinguir:

1. automação esperando;
2. timeout;
3. erro;
4. lead que simplesmente não respondeu;
5. saída por regra de qualificação.

---

## RP-FF-003 — Exportação de contatos utilizada

```yaml
id: RP-FF-003
area: dados
ferramenta: FullFunnel
status: CONFIRMADO_HISTORICO
data_referencia: "2026-08"
```

A equipe utilizou exportações do FullFunnel para gerar listas e fazer cruzamentos de campanhas/pesquisas.

---

# 11. Listas e base histórica

## RP-DATA-001 — Base histórica de grande volume

```yaml
id: RP-DATA-001
area: dados
tipo: ativo_operacional
status: CONFIRMADO_ATUAL
estimativa_total_leads: 52000
estimativa_ex_alunos_vanessa: 40000
```

O RP trabalha com uma base histórica estimada em aproximadamente 52 mil contatos, dos quais cerca de 40 mil são alunos/ex-alunos da Vanessa.

### Uso pela IA

A base histórica deve ser tratada como ativo estratégico para:

- reativação;
- segmentação;
- lookalikes/públicos;
- campanhas específicas;
- ofertas por estágio de relacionamento.

### Limite

Os números são estimativas operacionais e devem ser recalculados quando houver uma base consolidada atual.

---

## RP-DATA-002 — Campos usados em listas FullFunnel

```yaml
id: RP-DATA-002
area: dados
tipo: esquema_operacional
status: CONFIRMADO_HISTORICO
campos_padrao:
  - Phone
  - Email
  - First
  - Last
  - Business
  - Source
  - Additional
  - Notes
  - Tags
```

Em processos de organização de listas, esse padrão foi utilizado como referência.

Também foram trabalhadas tags para histórico de aluno, turma, origem e ações específicas.

---

# 12. Operação comercial

## RP-COM-001 — Não desperdiçar lead sem fit para oferta principal

```yaml
id: RP-COM-001
area: comercial
tipo: principio_operacional
status: CONFIRMADO_HISTORICO
```

O comercial utilizou lógica de redirecionamento para outra oferta quando o lead:

- não tinha fit para Cúpula;
- não tinha momento;
- não tinha condição para ticket principal;
- tinha fit para CSV ou produto de entrada.

---

## RP-COM-002 — Lead novo precisa de velocidade

```yaml
id: RP-COM-002
area: comercial
tipo: APRENDIZADO_OPERACIONAL
status: CONFIRMADO_HISTORICO
```

As reuniões comerciais mostraram perda de eficiência quando leads novos ficaram aguardando enquanto o time priorizava:

- report;
- organização;
- follow-up secundário;
- onboarding;
- outras demandas.

### Regra operacional derivada

Quando houver janela de venda dependente de agenda:

`LEAD NOVO QUALIFICADO → CONTATO → AGENDAMENTO`

vem antes de tarefas administrativas.

---

# 13. Performance e mensuração

## RP-METRIC-001 — Não confundir lead com teste

```yaml
id: RP-METRIC-001
area: dados
tipo: regra_de_qualidade
status: CONFIRMADO_HISTORICO
```

Toda análise de formulário deve separar:

- leads válidos;
- testes internos;
- duplicações;
- membros do time;
- acessos de QA.

---

## RP-METRIC-002 — Não confundir presença com pico de audiência

```yaml
id: RP-METRIC-002
area: dados
tipo: regra_de_qualidade
status: CONFIRMADO_HISTORICO
```

Um número de pessoas simultaneamente no player não representa necessariamente:

- pessoas únicas;
- leads identificados;
- comparecimento total.

A falha foi observada no WCSV de julho/2026.

---

## RP-METRIC-003 — Reporting por etapa

```yaml
id: RP-METRIC-003
area: dados
tipo: modelo_de_reporting
status: CONFIRMADO_HISTORICO
```

O RP já trabalhou com reporting contendo:

- novos leads;
- contatos realizados;
- respostas;
- vendas;
- perdas;
- motivo da perda;
- origem;
- qualificação;
- agendamento;
- sessão realizada;
- objeção.

Esse padrão é mais útil para IA do que apenas número final de vendas.

---

# 14. Riscos operacionais observados

## RP-RISK-001 — Fragmentação de informação

```yaml
id: RP-RISK-001
area: gestão
tipo: risco
status: APRENDIZADO_OPERACIONAL
```

Informações relevantes já ficaram divididas entre:

- WhatsApp;
- reunião;
- ClickUp;
- FullFunnel;
- Hotmart;
- planilhas.

### Mitigação recomendada

A IA deve apontar conflitos de fonte e privilegiar:

1. dado de sistema;
2. evidência de execução;
3. decisão documentada;
4. relato posterior.

---

## RP-RISK-002 — Muitas frentes simultâneas

```yaml
id: RP-RISK-002
area: gestão
tipo: risco
status: APRENDIZADO_OPERACIONAL
```

Há recorrência de sobreposição entre:

- Cúpula;
- CSV;
- webinar;
- eventos;
- imersões;
- disparos;
- conteúdo;
- novas ofertas.

O risco observado é dispersar a capacidade operacional antes de concluir a prioridade principal.

---

## RP-RISK-003 — Dependência de ação manual pós-automação

```yaml
id: RP-RISK-003
area: comercial
tipo: risco
status: APRENDIZADO_OPERACIONAL
```

Mesmo com automação, conversão dependeu de:

- contato humano;
- agendamento;
- follow-up;
- recuperação;
- leitura de contexto.

A automação não substituiu comercial.

---

## RP-RISK-004 — Automação pode esconder lead

```yaml
id: RP-RISK-004
area: tecnologia
tipo: risco
status: APRENDIZADO_OPERACIONAL
```

Fluxos longos ou gatilhos tardios podem deixar lead no WhatsApp sem oportunidade visível no pipeline.

Esse problema já ocorreu e foi corrigido na operação Cúpula.

---

# 15. Ativos conhecidos

## RP-ASSET-001 — Domínios e infraestrutura web

```yaml
id: RP-ASSET-001
area: web
status: CONFIRMADO_HISTORICO
ativos:
  - "lp.vocenocomando.com.br"
  - "vocenocomando.com.br"
```

O ecossistema RP utiliza páginas próprias e Hotmart/FullFunnel em diferentes etapas.

Versões e responsabilidades devem ser conferidas antes de alterar um ativo.

---

## RP-ASSET-002 — Quiz WCSV

```yaml
id: RP-ASSET-002
area: web
tipo: ATIVO_HISTORICO
status: ATIVO_HISTORICO
url: "https://links.fullfunnel.app/widget/quiz/JGcpfCpaDbJ3Lz9KfjC"
```

O quiz foi utilizado em ciclos do WCSV.

Confirmar se permanece ativo antes de reutilizar.

---

# 16. Regras de consulta para a IA

## 16.1. Pergunta: "Qual é o funil atual?"

Responder apenas com um fluxo marcado `CONFIRMADO_ATUAL`.

Se só houver histórico:

> "Tenho registro de que, em [período], o fluxo era..."

## 16.2. Pergunta: "Isso foi feito?"

Exigir evidência de:

- publicação;
- entrega;
- disparo;
- venda;
- integração funcionando;
- dado medido.

Se só houver reunião ou tarefa:

> "Foi decidido/atribuído, mas não encontrei comprovação de implementação."

## 16.3. Pergunta: "Quem é responsável?"

Diferenciar:

- responsável definido naquele ciclo;
- responsável atual.

Não perpetuar owner antigo sem confirmação.

## 16.4. Pergunta: "Qual benchmark usar?"

Mostrar:

- campanha;
- período;
- tamanho de amostra;
- etapa da conversão.

Nunca misturar:

- lead → venda;
- sessão → venda;
- presença → venda;
- contato → agendamento.

---

# 17. Formato padrão para novos chunks

```yaml
id: RP-[AREA]-[NUMERO]
projeto: Realizando Potenciais
area:
subarea:
produto:
tipo:
status:
data_referencia:
validade:
fonte_tipo:
fonte:
evidencia:
```

Depois do YAML:

### Fato operacional

Descrição objetiva do que aconteceu.

### Consequência

O que isso mudou.

### Uso pela IA

Como o conhecimento deve orientar resposta/execução.

### Não inferir

O que não pode ser concluído a partir do registro.

---

# 18. Processo de manutenção

## Entrada nova

Toda nova informação deve passar por:

1. capturar fonte;
2. identificar se é ideia, decisão, execução ou resultado;
3. procurar evidência posterior;
4. transformar em chunk;
5. marcar data;
6. marcar status;
7. registrar fonte;
8. substituir/superar versões antigas sem apagá-las.

## Revisão periódica

Recomenda-se uma revisão quinzenal ou mensal para identificar:

- processos superados;
- responsáveis alterados;
- ferramentas substituídas;
- ofertas encerradas;
- novos benchmarks;
- incidentes;
- aprendizados.

---

# 19. Fontes de reunião usadas nesta consolidação

As reuniões foram utilizadas como **evidência de execução** e não como substituto da RAG canônica.

### 19/05/2026 — Reunião Time RP
https://fathom.video/calls/677016074

Confirma, entre outros:

- Cúpula como prioridade naquele ciclo;
- 414 contatos / 58 reuniões;
- aproximadamente 14% de agendamento;
- aproximadamente 41% de conversão de reunião para venda;
- uso do ClickUp e problema de demandas que ficavam fora dele.

### 01/06/2026 — Reunião Comercial
https://fathom.video/calls/692317793

Confirma, entre outros:

- fluxo comercial Cúpula;
- prioridade de agendamento;
- 18 aplicações aguardando;
- automação FullFunnel;
- antecipação da criação de oportunidade;
- uso de timeout e histórico de execução;
- escada Cúpula → CSV → Desafio 38 Dias.

### 17/07/2026 — Reunião RP
https://fathom.video/calls/751777480

Confirma, entre outros:

- primeiro ciclo real do WCSV;
- 320 leads válidos;
- diferença causada por testes;
- dificuldade de identificar presença;
- 3 sinais de interesse;
- tagueamento;
- estrutura semanal;
- números históricos da Black Friday;
- planilha de Cúpula com 574 leads acumulados naquele momento.

### 14/08/2026 — Impromptu Zoom Meeting
https://fathom.video/calls/784713845

Confirma, entre outros:

- restauração da API do WhatsApp;
- retorno das automações;
- aproximadamente 15 mil mensagens enviadas;
- aproximadamente 3 mil recebidas;
- 5.946 conversas iniciadas em 7 dias;
- adoção de cadência mais conservadora após incidente.

---

# 20. Resumo executivo para contexto curto

A Realizando Potenciais opera múltiplos funis de produtos e usa principalmente FullFunnel, Hotmart, WhatsApp, páginas próprias, planilhas e ClickUp.

Os registros operacionais mostram que a Cúpula da Decisão depende fortemente de qualificação + agendamento de sessão estratégica. Em maio/2026, a conversão de sessão realizada para venda estava próxima de 41%, tornando volume e agendamento os principais gargalos do momento. Em junho, o funil FullFunnel foi corrigido porque oportunidades estavam sendo criadas tarde demais.

O CSV foi colocado em um modelo de webinar recorrente em julho/2026. O primeiro teste trouxe 320 leads válidos, mas houve falha de rastreamento dos participantes ao vivo porque captação e player não estavam integrados adequadamente. O público foi preservado com tags e origem para nutrição posterior.

A Black Friday histórica usada como referência teve 1.016 leads para uma meta de 2.500, 66 vendas totais, 46 novos clientes e 20 renovações.

Em agosto/2026, durante a operação da Imersão dos 3 Níveis, o WhatsApp/API sofreu restrição após alto volume. A conexão foi restaurada e as automações voltaram. O time passou a adotar envio mais conservador e evitar períodos noturnos.

A principal regra desta RAG é: **decisão não é implementação**. Só deve virar verdade operacional aquilo que possui evidência de execução, uso ou resultado.
